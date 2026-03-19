---
layout: page
title: Charter
permalink: /charter/
---

FP Launchpad is a centre at [IIT Madras](https://www.iitm.ac.in/), founded in January 2026, that aims to build long-term research and educational capacity in functional programming, bringing together principled programming languages and systems research, open artefacts, and the training of future researchers and engineers. The centre has been established with generous support from [Jane Street](https://www.janestreet.com/), with a commitment of INR 23.5 crore (approximately USD 2.5 million). The focus is on the [OCaml](https://ocaml.org/) programming language and its ecosystem, as well as [OxCaml](https://oxcaml.org/), a rapidly evolving set of extensions to OCaml that aims to bridge the gap between performance and correctness.

## Three Pillars

FP Launchpad pursues the following objectives across three aligned areas:

**Research**: Advance the state of the art in FP systems through sustained research on programming languages, compilers and runtime systems, and pragmatic formal verification, including the use of modern interactive theorem provers such as Lean to specify and validate critical properties. The O(x)Caml programming language will be the primary research vehicle. Success is measured through high-quality peer-reviewed publications and durable research artefacts that influence both academic and industrial practice.

**Education and Training**: Build strong research and engineering capacity in systems, with particular attention to the gap between demand and opportunities in India. The objective is to identify and train the next generation of system builders by providing them with rigorous foundations in functional programming, systems and formal reasoning, exposure to real system problems, and the time and intellectual space to experiment and grow.

**Systems and Community**: Develop and deploy real systems that demonstrate the practical impact of functional approaches, while building an active research and practitioner community around them. This includes sustained work on the broader O(x)Caml ecosystem, open-source collaboration, and community building.

## Approach

FP Launchpad's activities are organised as a tightly coupled loop that links education and training, long-horizon research, and open systems building. The loop begins by developing early-career systems researchers through [**post-baccalaureate research fellowships**](/2026/03/06/applications-open-post-bacc-fellowship.html) that provide the time and mentorship needed to do impactful work, complemented by graduate- and undergraduate-level courses, intensive summer and winter schools, and Dagstuhl-style research seminars. To broaden access to systems education across India and serve as pathways into research and advanced systems work, the centre will offer MOOC courses on the well-established [NPTEL](https://nptel.ac.in/) platform. The centre also has funding earmarked for short-term visiting positions at partner institutions, enabling fellows to collaborate and immerse themselves in active systems-building environments.

The fellows then engage in long-horizon research on functional systems, with an emphasis on building, evaluating, and maintaining real systems rather than isolated prototypes. Research hypotheses are explored through the design and deployment of impactful open-source systems in collaboration with the broader systems community in India and elsewhere.

## Illustrative Projects

- An open-source, verifiable voting system for general elections, built on top of [Shakti](https://shakti.org.in/) RISC-V processor, [MirageOS](https://mirage.io/) unikernels and O(x)Caml.
- A programmable public infrastructure for environmental planning, combining [TESSERA](https://github.com/ucam-eo/geotessera)'s satellite-derived representations with [CoRE Stack](https://core-stack.org/) data and compositional functional models in O(x)Caml to support auditable indicators and scenario analysis for India's water and habitat systems.
- A formally verified runtime system for O(x)Caml in O(x)Caml guaranteeing memory safety and functional correctness properties. The focus will also include formal verification of tools for debugging and observability, such as eBPF-based tracing, continuous runtime contract checking, and deterministic record and replay.

## Impact

A successful example of a tight feedback loop is the OxCaml project, where a principled, fast-moving language is nevertheless used in production at scale within Jane Street. Tight integration between research, implementation, and deployment enables rapid iteration, with failures detected early and rolled back safely without disrupting users. FP Launchpad aims to capture this spirit: research conducted in close proximity to real systems, continuous feedback from deployment and adoption, and educational programmes grounded in direct engagement with evolving, production-quality software. Alumni of FP Launchpad are expected to emerge as researchers, graduate students, maintainers, and engineers capable of leading and sustaining complex software systems.
