---
layout: blog-post
title: "FPL Kickoff Recap: Our Launch at IIT Madras"
date: 2026-05-06
author: FP Launchpad
published: false
---

On April 13, 2026, we held the kickoff of the FP Launchpad at the IC&SR Building, IIT Madras. The auditorium filled up with students from IIT Madras and colleges across Chennai, alongside researchers, faculty, and industry guests. There were fresh flowers at the entrance, Indian filter coffee to get things going, and a speaker lineup that cut across hardware design, security, formal verification, compilers, and AI-assisted software engineering. Here's a full recap of the day — talk by talk, with direct quotes from the recordings.

---

## Opening

### KC Sivaramakrishnan — Opening Address

<img src="https://kcsrk.info/assets/profile.jpeg" style="width:48px;height:48px;border-radius:50%;object-fit:cover;vertical-align:middle;margin-right:8px;"> [KC Sivaramakrishnan](https://kcsrk.info), Assistant Professor, IIT Madras

<iframe width="100%" height="315" src="https://www.youtube.com/embed/fV4-cdVSkBk" frameborder="0" allowfullscreen></iframe>

KC opened with the problem the centre exists to solve:

> "AI agents are writing a lot of the software and they are writing it in a fragile and insecure way. And what is also happening recently is this: they are also extremely great at exploiting vulnerabilities. So one of the things that happened, maybe some of you followed it last week, was the frontier model developed by Anthropic. They said, look, this is too powerful. It can craft exploits — full exploits, chaining together multiple exploits. And they said, look, this is too powerful. We are not going to release it."

That's the double bind: AI is writing more code than ever, and separately, it is exceptionally good at breaking it. India produces around 150,000 CS graduates a year, yet the foundational pieces of the stack — the languages, the runtimes, the formal methods tooling — are almost entirely built elsewhere. The FP Launchpad aims to change that.

The centre is built around three pillars: research, education and training, and systems and community. KC was explicit that the systems work comes first:

> "The most important one is the systems and community aspect. I did a postdoc with Anil, and in that systems research group the philosophy was: go build software that you think has to exist and other people will use it. And as you do, interesting research problems will come out. It was never about papers first. It was: this thing does not exist, we have a problem here, let's just go build it."

The north star projects reflect this: verifiable voting infrastructure (with IIT Madras's Process Research Group), digital public infrastructure for environmental planning (with Anil's group at Cambridge), and a formally verified, AI-assisted rebuild of the foundational software stack. KC also made a point worth emphasising for anyone who reads "functional programming" and thinks it's narrow:

> "Even though it says FP Launchpad, for us, functional programming is just a tool. We want to solve problems in networking, we want to solve problems in AI, we want to solve problems in hardware design."

To staff all of this, FPL is running a [post-baccalaureate fellowship](https://fplaunchpad.org) — a two-year fully funded position with travel support, targeting eight fellows per year. Applications are open.

The centre's founding donor is [Jane Street](https://www.janestreet.com), who have committed US$2.5 million over four years.

---

### Prof. V. Kamakoti — Inaugural Address

<img src="https://heritage.iitm.ac.in/sites/default/files/2022-03/prof-kamakoti.png" style="width:48px;height:48px;border-radius:50%;object-fit:cover;vertical-align:middle;margin-right:8px;"> [Prof. V. Kamakoti](https://heritage.iitm.ac.in/directors-gallery/prof-v-kamakoti), Director, IIT Madras

<iframe width="100%" height="315" src="https://www.youtube.com/embed/zreZprRVoGA" frameborder="0" allowfullscreen></iframe>

Prof. Kamakoti, who had to attend to an urgent commitment on the day, delivered his address as a recorded video. His diagnosis was sharp: the state of software development is becoming decoupled from verification and performance. When large software systems are assembled from components written by different teams, cross-cutting optimisations don't happen and the bugs of one layer affect another — and AI-generated code is accelerating exactly this pattern.

His framing of the problem: every layer of the software stack (hardware, microarchitecture, OS, compilers, application) is designed as a virtual machine, deliberately hiding what's below. That abstraction is what makes software engineering tractable — but it also means a vulnerability in any layer is invisible to the others. Verification has to happen during construction, not bolted on afterwards.

He pointed to [Shakti](https://shakti.org.in), IIT Madras's open-source RISC-V processor family (taped out four times, with a server-class chipset in development with IBM), as proof that India can build a full hardware-software stack from scratch. "Verification is directly proportional to scale," he said. Small toy programs don't count. FPL will work on large systems.

---

## Full Playlist

All 10 talks are available on YouTube:

<iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PLvhoCCkcBeAv4fgWRw5o1q2IpTEAIZBXP" frameborder="0" allowfullscreen></iframe>

---

## Research Talks

### Functional Programming and Concurrent Atomic Transactions for Complex Hardware Design

<img src="https://avatars.githubusercontent.com/u/3867081?v=4" style="width:48px;height:48px;border-radius:50%;object-fit:cover;vertical-align:middle;margin-right:8px;"> [Rishiyur S. Nikhil](https://github.com/rsnikhil), CTO and Co-founder, Bluespec

<iframe width="100%" height="315" src="https://www.youtube.com/embed/aNqWJyDkyoQ" frameborder="0" allowfullscreen></iframe>

Nikhil's talk opened with a provocation:

> "Software is hardware and hardware is software."

That slogan captures 25 years of trying to close the schism between hardware designers and software engineers — a schism that [Bluespec](https://bluespec.com) was built to bridge. The core pitch is that the same abstractions that transformed software — expressive types, higher-order parameterisation, modularity, atomic transactions — can do the same for hardware.

Bluespec's rules express behaviour as guarded atomic transactions: when a condition holds, fire atomically. Nikhil explained why this matters for hardware specifically:

> "Hardware is typically much more concurrent than any parallel software you write, right? At a very fine grain level, everything is happening at once. This way of specifying them makes it more amenable to verification — some detail that you would have had to take care of manually at a lower level is now automated, and assuming you trust the compiler, the user doesn't have to think about it at all. And here the atomicity is key."

The Q&A surfaced the familiar adoption challenge. Persuading hardware teams to switch languages is even harder than persuading software teams to adopt OCaml or Haskell, because the cost of a wrong bet at tape-out time is very high:

> "In the hardware case, people are extremely conservative because of the costs involved, especially if you're doing ICs as opposed to FPGAs. To get even the simplest IC, the first one, you've already blown..."

His answer is interoperability — Bluespec designs generate Verilog, and the Verilog output is, he was proud to note, "actually very, very nice." Existing IP can integrate incrementally, which is the only realistic path in a field where decades of code are already written in legacy languages.

Nikhil is a member of the FPL advisory board. FPL's verifiable voting infrastructure project targets the Shakti RISC-V platform, which was itself designed using the hardware design ideas Nikhil has championed.

---

### Trusted Hardware for Security-Critical Software

<img src="https://www.cse.iitm.ac.in/~chester/pubs/chet.png" style="width:48px;height:48px;border-radius:50%;object-fit:cover;vertical-align:middle;margin-right:8px;"> [Chester Rebeiro](https://www.cse.iitm.ac.in/~chester/), Professor, IIT Madras

<iframe width="100%" height="315" src="https://www.youtube.com/embed/Tgmyjkfrnew" frameborder="0" allowfullscreen></iframe>

Chester Rebeiro's research sits at the intersection of hardware and security — specifically, how to use hardware-level mechanisms to give software guarantees it could never achieve on its own. He opened with a backstory that shows how much Shakti changed the field for him personally:

> "I did my PhD between 2009 and 2013 and my work was on microarchitectural attacks. Back then I didn't have much choice. I started off looking at Intel CPUs, looking at how programs' execution times vary. I could run a program, give it inputs, look at the output, measure execution time, look at hardware performance counters. But there was not much more I could do — I didn't have access to the actual hardware."

That changed in November 2013:

> "I visited IIT Madras and I spoke to Professor Kamakoti, who told me about the Shakti initiative. That was a different kind of turn for me, because now I could actually design a processor from scratch. I could set up the entire software stack, run Linux on a RISC-V processor, instantiate the processor on an FPGA. And very importantly for me, I could actually do clean-slate security research. Something which was not possible before."

The talk covered two projects, both built on Shakti. **TESLA** is a lightweight Trusted Execution Environment for legacy embedded applications: it isolates a sensitive application from even a compromised OS, using hardware-configurable register windows that open precise byte-level memory regions at the kernel boundary rather than deep-copying parameters — keeping overhead low without sacrificing isolation. **FIDES** attacks the complementary problem: intra-application isolation for mixed-language programs. When OCaml and C share a process, a bug in the C component can trash the OCaml heap. FIDES uses hardware-assisted compartments to isolate components while keeping fast function calls within a typesafe region — so writing secure code actually performs better than mixing in unsafe C.

Chester is a faculty member in IIT Madras CS, making him a natural collaborator for FPL. The work on TESLA and FIDES directly feeds into FPL's goal of a verifiably secure foundational software stack: hardware guarantees are the bedrock on which everything else is built.

---

### Towards Verifiable Governance with LLMs and Lean

<img src="https://media.licdn.com/dms/image/v2/C5603AQGjQKQtzd8A_Q/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1647665493390?e=2147483647&v=beta&t=ZyRZiDVsvFHmwT1nMmXSL0k0gs45oSEw0Aox4B5SYnE" style="width:48px;height:48px;border-radius:50%;object-fit:cover;vertical-align:middle;margin-right:8px;"> [Krishnan Raghavan](https://www.linkedin.com/in/krishnan-raghavan-834aa091/), CTO and Co-founder, Pramaana Labs

<iframe width="100%" height="315" src="https://www.youtube.com/embed/NeL8kw6Z8hA" frameborder="0" allowfullscreen></iframe>

Krishnan Raghavan is an IIT Madras CS alum who went on to Google (Maps data accuracy) and then Glean (enterprise search) before founding [Pramaana Labs](https://www.pramaanalabs.ai), which is working on making AI correct for legal and governance applications. The problem is straightforward to state: LLMs are fluent but not reliable, and when governments use AI to process tax filings or citizen benefits, reliability is not optional. His approach is to use LLMs for translation but not for reasoning — take natural language statute text, translate it into [Lean 4](https://lean-lang.org) via a domain-specific legal DSL, and let the proof assistant handle verification.

The live demo showed his system formalising provisions of the Indian Income Tax Act 2025 into Lean. Introduce a contradictory provision, and the system flags it in real time as the DSL typechecks in the browser. The example he chose was pointed:

> "Tax is not monotonic — sometimes when people earn more, they end up net earning less. Because of this, we can programmatically and formally identify all such places. Wherever we can define a notion of fairness, we can write a theorem that runs on top of all of this and our prover will try to prove or disprove it."

KC asked in the Q&A whether you could go further — not just formalising existing laws but synthesising consistent laws by construction. Krishnan was direct: once everything is formalised, those questions become tractable. On the question of ambiguity that's deliberately baked into legal text (the kind that requires judges to interpret), he noted:

> "There are genuinely places in legal text that are left ambiguous. But a large majority of the cases, it's more of a chicken-and-egg problem — if people had known about these ambiguities when they were writing laws, they would have been more than happy to clarify them. A system like this can help in a majority of those cases."

The Lean-based techniques he is applying to governance overlap directly with what FPL fellows will be working on.

---

### From Precise Analysis to Efficient JIT Optimization

<img src="https://www.cse.iitb.ac.in/~manas/images/profile.jpg" style="width:48px;height:48px;border-radius:50%;object-fit:cover;vertical-align:middle;margin-right:8px;"> [Manas Thakur](https://www.cse.iitb.ac.in/~manas/), Assistant Professor, IIT Bombay

<iframe width="100%" height="315" src="https://www.youtube.com/embed/ovsQmlQmbNE" frameborder="0" allowfullscreen></iframe>

Manas Thakur is an IIT Madras alumnus (his PhD thesis on precise Java program analysis won the IBM Best Thesis Award) who now leads the [CompL](https://www.cse.iitb.ac.in/~manas/) research group at IIT Bombay. He opened by flashing a single number on the slide — 20 million — and asking the room how many of them still write code. His talk tackled a long-standing tension in compiler design: precise static analysis is expensive, and JIT compilers need to be fast. The conventional wisdom is that you have to choose one. His group is showing you don't.

The key idea is **optimistic stack allocation**: instead of always heap-allocating objects (safe but slow, because of GC pressure), do precise static analysis to figure out which objects can safely go on the stack, and allocate them there. When the JIT's runtime assumptions turn out to be wrong — because Java is dynamic and objects can escape in ways the static analysis didn't predict — you heapify them at that point. The surprising additional result is that information flows in both directions: speculative JIT data improves the precision of the static analysis, so AOT and JIT end up benefiting each other rather than competing.

Asked in Q&A about formal proofs of correctness, Manas noted:

> "There are informal proofs — intuitive informal proofs that tell you: if you know which statements may make an object escape, and if you have inserted checks at all those points, and if you make sure your recursive heapification is right, you won't go wrong. I would in fact say giving a formal proof would be relatively easy here. What's genuinely difficult is giving a guarantee that your implementation actually does what you say. That is extremely hard."

Manas's work on compiler analysis and runtime optimisation is directly relevant to FPL's interest in building high-performance functional systems.

---

### Mechanising a Regex-Based Borrow Checker: An Experiment in AI-Assisted Metatheory

<img src="https://ilyasergey.net/assets/img/ilya-2021-2.jpg" style="width:48px;height:48px;border-radius:50%;object-fit:cover;vertical-align:middle;margin-right:8px;"> [Ilya Sergey](https://ilyasergey.net/), Associate Professor, National University of Singapore

<iframe width="100%" height="315" src="https://www.youtube.com/embed/rXvjRABLGKw" frameborder="0" allowfullscreen></iframe>

Ilya called the event "absolutely fabulous" and then immediately started talking about borrows. That's his register — warm but precise — and it suited a talk that was genuinely surprising in both its subject and its method.

The subject is a borrow checker for [Move](https://move-language.github.io/move/), the smart contract language used by Aptos and Sui. Move has a linear type system that prevents duplicate spending, but it doesn't have a borrow checker in the Rust sense — which means temporary references can create aliasing patterns that are easy to reason about incorrectly. Ilya's approach is to build the borrow checker using **Brzozowski derivatives**: a classical technique from formal language theory, applied so that the borrow state of any program point is expressed as a regular expression over the program's execution traces. Kleene star handles the hard case — unbounded aliasing from loops and recursion. The result is a checker that is not just correct but *provably* correct.

The method is where it gets remarkable:

> "By working very, very much part time, mostly over three very intense weeks — I have other duties, I run a research group, I have a family, I need to teach classes — basically that was me just every once in a while coming and giving extra instructions to Claude Code. A few times I had to snap it out of some unproductive loops. I produced nearly 40,000 lines of Lean. I think that outside of MathLib formalizations, this is probably the second largest formalization of a programming language metatheory."

The Lean formalisation contains zero `sorry` placeholders — zero unproven gaps. He was also candid about what this felt like from the inside:

> "When I was a grad student, I spent three days once writing a TikZ diagram. I'm very angry now when I think about those three days of my life that I'll never get back."

What changed is not that AI wrote the proofs: it's that AI handled the mechanical, routine parts of proof construction well enough that Ilya could spend almost all his time on the part that actually requires insight — designing the right invariants. The bottleneck shifted from *writing* proofs to *specifying* what needed to be proved.

On bugs found in the process:

> "The bugs that we actually discovered were, sadly, not on the soundness side but on the completeness side. For three million functions — if there were soundness bugs, they would probably have been exploited and the blockchain would have stopped being alive because all the money would have been siphoned."

This is the clearest live demonstration FPL has seen of what AI-assisted formal verification looks like in practice. It's not science fiction and it's not a toy. It's 39K lines of sorry-free Lean in three weeks, on a real problem in a production language. AI-assisted formal verification is central to FPL's research agenda, and Ilya's workflow here is close to what FPL fellows working on mechanised metatheory will be doing from day one.

---

### Donor Address

<img src="https://avatars.githubusercontent.com/u/715302?v=4" style="width:48px;height:48px;border-radius:50%;object-fit:cover;vertical-align:middle;margin-right:8px;"> Yaron Minsky, Co-head of Technology, Jane Street

<iframe width="100%" height="315" src="https://www.youtube.com/embed/ytknR-B5Tf8" frameborder="0" allowfullscreen></iframe>

Yaron Minsky has been at Jane Street long enough to remember when the firm's bet on OCaml looked like a bold gamble. He introduced himself with characteristic dryness:

> "My role at Jane Street was the somewhat odd claim to fame of having imposed a comically unpopular programming language on the firm."

It doesn't look like a gamble anymore. Jane Street now runs over 85 million lines of OCaml in production. His message at the kickoff was not retrospective, though. It was forward-looking, and slightly mischievous.

His main technical thread was [OxCaml](https://github.com/oxcaml/oxcaml), Jane Street's fork of the OCaml compiler that introduces a system of modes — uniqueness, locality, and contention. The core idea is that OCaml and Rust share a philosophical goal (correct, performant systems code) but have taken different paths. OxCaml tries to import Rust's ownership discipline into OCaml's type system without surrendering OCaml's expressiveness.

Shriram Krishnamurthi, joining remotely from Brown, threw Yaron a pointed question after the talk: there's a grad student at IIT Madras thinking about working with KC, but now wondering whether agentic AI has made programming languages irrelevant. "How do you save KC here?" Yaron's answer was direct:

> "We actually use agentic AI enormously and get a lot of benefit out of it — despite the fact that, you might be surprised to learn, OCaml itself is not a large portion of the training set. And yet the models are quite effective working in our tools. We think they're in many ways more effective than building large complex systems in Python, because the rigor and constraint you get from a language like OCaml is both useful within the agentic loop itself for giving feedback, and also useful for verifying the results."

His closing line was half a joke, half a genuine instruction: "Grad students, don't worry about AI taking your jobs. Go work with KC."

Jane Street is FPL's founding donor, with a commitment of US$2.5 million over four years. OxCaml is open-source, and the mode system it's building is directly relevant to FPL's goal of a verifiably safe foundational software stack.

---

### A Programming Language for Lightweight Diagramming

<img src="https://cs.brown.edu/~sk/Images/me-2019-04-10-small.jpg" style="width:48px;height:48px;border-radius:50%;object-fit:cover;vertical-align:middle;margin-right:8px;"> [Shriram Krishnamurthi](https://cs.brown.edu/~sk/), Professor, Brown University

<iframe width="100%" height="315" src="https://www.youtube.com/embed/O5bLF5YekkU" frameborder="0" allowfullscreen></iframe>

Shriram joined remotely from Brown and opened with an admission:

> "This is such an honour. I wish I was there in person. I can't tell you how exciting it is to see FP have a centre in India — a centre in South India. My only regret is it's in the wrong city of South India. I only say this because I'm a Bangalorean."

He's one of the people who helped build the intellectual foundation that FPL is inheriting, and his excitement was genuine.

The talk was on [sPyTial](https://cs.brown.edu/~sk/), a diagramming language aimed at a gap that's been bothering him for a long time: the space between D3 (powerful but has no concept of what a diagram *means*) and formal specification tools like Alloy (semantically precise but not approachable). sPyTial sits in between. It's a language for describing spatial layouts that has an actual semantics — not just a rendering model. He set up the problem by asking the audience to describe a data structure and watching as they immediately started drawing in the air:

> "You said AVL search tree, and then you did this — you started to draw a picture in the sky. There's this spatiality in all of our data structures. Sometimes it's inherent, like a Tic Tac Toe board or a chess puzzle. Sometimes it's a spatiality we ascribe to it, like binary search trees or decision diagrams. But anytime you try to describe it, you go to a board and start doing this with your hand — something about the left and something about the right."

sPyTial's constraint solver works with the semantics of spatial relationships, not just their rendering, so you can write a diagram that's *correct* in the same sense that a program is correct. The cognitive science grounding — starting from how humans actually interpret spatial encodings rather than how tools render them — is what makes it distinctive. A Lean prototype means you can prove properties of entire diagram families.

The practical embedding story is Python, Rust, and Pyret. Shriram is a member of the FPL advisory board, and sPyTial is a natural vehicle for FPL fellows interested in the intersection of programming languages, HCI, and formal methods.

---

### TESSERA: Functionally Programming Petabytes of Earth Observations

<img src="https://anil.recoil.org/images/anil-headshot.webp" style="width:48px;height:48px;border-radius:50%;object-fit:cover;vertical-align:middle;margin-right:8px;"> [Anil Madhavapeddy](https://anil.recoil.org/), Professor, University of Cambridge

<iframe width="100%" height="315" src="https://www.youtube.com/embed/-tBv-j5IbmM" frameborder="0" allowfullscreen></iframe>

Anil closed the day. He opened with something that doesn't get said often enough:

> "I've worked with KC for many, many years, and it's a bit like having a kid leave home to see him all grown up now, running his own centre here. And the reason I'm so excited is that most of my good ideas have come from collaboration — from working with other people and trying to build something real, as KC said at the beginning, and then figuring out how to get to some impossible goal."

The impossible goal he chose a few years ago: figure out where all life on Earth is.

[TESSERA](https://geotessera.org) is a foundation model for satellite Earth observation — pixel-wise embeddings for Sentinel-1 and Sentinel-2 multispectral data. The goal is to do for geospatial intelligence what LLMs did for language: compress the world's satellite archive (petabytes, growing continuously) into a form that makes downstream tasks tractable with very few labels. Each pixel gets a 128-dimensional embedding that captures a full year's worth of observations across 12 spectral bands. The challenge is that the same patch of ground looks completely different in different seasons — the model needs to understand it as *one place* across all those observations:

> "We take pictures over the planet, sample a few million pictures. Here we have two pictures that are the same place. Are they really the same place? It's the same place — just taken at a different time of year. Spectrally these look completely different. It was daytime here, it's nighttime there, some clouds. And so what we do is, for every point on Earth, we stack as many observations over that same spot and we keep them in order of the seasons."

What falls out of the model is the breadth of what becomes tractable. Fire detection from pixel clusters. Predicting species habitat without ever seeing the animal. Improving rainfall prediction for remote Indian villages by correlating ground features with weather patterns. The OCaml, Python, and TypeScript interfaces mean FP practitioners can work with it directly.

TESSERA is one of FPL's north star projects. The digital public infrastructure for environmental planning — using satellite data for India's water systems and habitats — will be built on exactly this foundation, in direct collaboration with Anil's group at Cambridge.
