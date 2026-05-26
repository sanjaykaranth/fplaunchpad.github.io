#!/usr/bin/env python3
"""
Daily digest: fetches all configured feeds, collects posts from the last 25 hours,
and writes a single _blog/ digest post. Skips posts already seen in previous digests.
"""

import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import feedparser
import yaml

REPO_ROOT = Path(__file__).parent.parent
FEEDS_FILE = REPO_ROOT / "_data" / "feeds.yml"
BLOG_DIR = REPO_ROOT / "_blog"
WINDOW_HOURS = 24 * 7


def load_feeds():
    with open(FEEDS_FILE) as f:
        return yaml.safe_load(f)


def load_seen_urls():
    seen = set()
    for post_file in BLOG_DIR.glob("*-digest.md"):
        content = post_file.read_text()
        match = re.search(r'^included_urls:\n((?:  - .+\n)*)', content, re.MULTILINE)
        if match:
            for line in match.group(1).strip().splitlines():
                url = line.strip().lstrip("- ").strip()
                if url:
                    seen.add(url)
    return seen


def strip_html(text):
    return re.sub(r'<[^>]+>', '', text or '').strip()


def fetch_posts_for_group(feed_list, seen_urls, since):
    posts = []
    for feed_info in feed_list:
        try:
            parsed = feedparser.parse(feed_info['feed'])
        except Exception as e:
            print(f"Warning: could not fetch {feed_info['url']}: {e}", file=sys.stderr)
            continue

        for entry in parsed.entries:
            published = None
            for attr in ('published_parsed', 'updated_parsed'):
                val = getattr(entry, attr, None)
                if val:
                    published = datetime(*val[:6], tzinfo=timezone.utc)
                    break

            if not published or published < since:
                continue

            url = entry.get('link', '')
            if not url or url in seen_urls:
                continue

            summary = strip_html(getattr(entry, 'summary', ''))
            if len(summary) > 280:
                summary = summary[:280].rsplit(' ', 1)[0] + '...'

            posts.append({
                'title': entry.get('title', 'Untitled'),
                'url': url,
                'author': feed_info['name'],
                'published': published,
                'excerpt': summary,
            })

    return sorted(posts, key=lambda p: p['published'], reverse=True)


def render_group(posts, heading):
    if not posts:
        return ''
    lines = [f'## {heading}\n']
    by_author = {}
    for post in posts:
        by_author.setdefault(post['author'], []).append(post)
    for author, author_posts in by_author.items():
        lines.append(f'### {author}\n')
        for post in author_posts:
            lines.append(f'**[{post["title"]}]({post["url"]})**\n')
            if post['excerpt']:
                lines.append(f'{post["excerpt"]}\n')
            lines.append('')
    return '\n'.join(lines)


def create_digest(member_posts, collaborator_posts, date):
    date_str = date.strftime('%-d %B %Y')
    filename = date.strftime('%Y-%m-%d') + '-digest.md'

    all_posts = member_posts + collaborator_posts
    urls_yaml = '\n'.join(f'  - {p["url"]}' for p in all_posts)

    body = render_group(member_posts, 'FPL Members') + render_group(collaborator_posts, 'Friends')

    content = f"""---
layout: blog-post
title: "FPL Reading — {date_str}"
date: {date.strftime('%Y-%m-%d')}
digest: true
included_urls:
{urls_yaml}
---

*A daily digest of posts from FPL members and collaborators.*

{body}"""

    filepath = BLOG_DIR / filename
    filepath.write_text(content)
    total = len(all_posts)
    print(f"Created {filepath} with {total} posts ({len(member_posts)} members, {len(collaborator_posts)} collaborators)")


def main():
    feeds = load_feeds()
    seen_urls = load_seen_urls()
    since = datetime.now(timezone.utc) - timedelta(hours=WINDOW_HOURS)

    member_posts = fetch_posts_for_group(feeds.get('members', []), seen_urls, since)
    collaborator_posts = fetch_posts_for_group(feeds.get('friends', []), seen_urls, since)

    if not member_posts and not collaborator_posts:
        print("No new posts found, skipping digest")
        return

    create_digest(member_posts, collaborator_posts, datetime.now(timezone.utc))


if __name__ == '__main__':
    main()
