---
layout: post
title: "FP Launchpad Kickoff"
date: 2026-03-30
image: /assets/images/logo_with_name.png
---

FP Launchpad will hold its kickoff on **Monday, April 13, 2026** at the **IC&SR Building, IIT Madras**. The day-long event features talks by leading researchers from industry and academia, covering hardware design, security, formal verification, compilers, programming languages, and AI-augmented software engineering.

Registration opens at 9:30 AM. The inauguration begins at 10:00 AM with welcoming remarks from Dr KC Sivaramakrishnan (Centre Head) and the Director of IIT Madras.

## Schedule

<div class="schedule-table" markdown="0">
<table>
  <colgroup>
    <col/><col/><col/><col/>
  </colgroup>
  <thead>
    <tr><th>Time</th><th>Event</th><th>Speaker</th><th>Title</th></tr>
  </thead>
  <tbody>
    <tr style="background-color: #f0f0f0;"><td>09:30 &ndash; 10:00</td><td colspan="3" style="text-align: center;"><strong>Registration</strong></td></tr>
    <tr><td>10:00 &ndash;10:30</td><td>Inauguration</td><td>* <a href="https://kcsrk.info">KC Sivaramakrishnan</a>, Assistant Professor, IIT Madras <br/> * Director, IITM</td><td>Welcoming remarks</td></tr>
    <tr><td>10:30 &ndash;11:15</td><td>Session 1</td><td>Rishiyur S. Nikhil, CTO and Co-founder, <a href="https://bluespec.com/">Bluespec</a></td><td><a href="#nikhil">Functional Programming and Concurrent Atomic Transactions for Complex Hardware Design</a></td></tr>
    <tr style="background-color: #f0f0f0;"><td>11:15 &ndash; 11:30</td><td colspan="3" style="text-align: center;"><strong>Networking break</strong></td></tr>
    <tr><td>11:30 &ndash;12:15</td><td>Session 2</td><td><a href="https://www.cse.iitm.ac.in/~chester/">Chester Rebeiro</a>, Professor, IIT Madras</td><td>Trusted hardware for security critical software</td></tr>
    <tr><td>12:15 &ndash;01:00</td><td>Session 3</td><td><a href="https://www.linkedin.com/in/krishnan-raghavan-834aa091/">Krishnan Raghavan</a>, CTO and Co-founder, <a href="https://www.pramaanalabs.ai/">Pramaana Labs</a></td><td>Towards verifiable governance with LLMs and Lean</td></tr>
    <tr style="background-color: #f0f0f0;"><td>01:00 &ndash; 02:15</td><td colspan="3" style="text-align: center;"><strong>Networking lunch</strong></td></tr>
    <tr><td>02:15 &ndash;03:00</td><td>Session 4</td><td><a href="https://www.cse.iitb.ac.in/~manas/">Manas Thakur</a>, Assistant Professor, IIT Bombay</td><td><a href="#thakur">From Precise Analysis to Efficient JIT Optimization — The Story of an Object Transformed by CompL</a></td></tr>
    <tr><td>03:00 &ndash;03:45</td><td>Session 5</td><td><a href="https://anil.recoil.org/">Anil Madhavapeddy</a>, Professor, University of Cambridge</td><td><a href="#madhavapeddy">TESSERA: Functionally Programming Petabytes of Earth Observations</a></td></tr>
    <tr style="background-color: #f0f0f0;"><td>03:45 &ndash; 04:15</td><td colspan="3" style="text-align: center;"><strong>Networking break</strong></td></tr>
    <tr><td>04:15 &ndash;04:30</td><td>Session 6</td><td>Ron Minsky, Jane Street (Remote)</td><td>Donor Address</td></tr>
    <tr><td>04:30 &ndash;05:15</td><td>Session 7</td><td><a href="https://cs.brown.edu/~sk/">Shriram Krishnamurthi</a>, Professor, Brown University (Remote)</td><td><a href="#krishnamurthi">A Programming Language for Lightweight Diagramming</a></td></tr>
    <tr><td>05:15 &ndash;06:00</td><td>Session 8</td><td><a href="https://ilyasergey.net/">Ilya Sergey</a>, Associate Professor, National University of Singapore</td><td><a href="#sergey">Mechanising a Regex-Based Borrow Checker: An Experiment in AI-Assisted Metatheory</a></td></tr>
  </tbody>
</table>
</div>

All sessions include opportunities for Q&A and discussion.

## Talks

### Functional Programming and Concurrent Atomic Transactions for Complex Hardware Design {#nikhil}

**Rishiyur S. Nikhil, Ph.D.** --- Co-founder and CTO, <a href="https://bluespec.com/">Bluespec</a>, Inc.

**Abstract.** For several decades, most hardware (HW) has been designed using certain legacy programming languages (Verilog and VHDL). In this talk we'll show how we can move from these somewhat impoverished legacy languages to more advanced HW-design languages, applying the same ideas that have given us high-level languages for software: Functional Programming, Atomic Transactions, Expressive Types, Strong Typing, Higher-order Parameterization, Modularity and Compositionality, and so on. We will also identify some future research directions.

**Bio.** Rishiyur Nikhil received his B.Tech. degree in EE from IIT Kanpur, and his Masters and Ph.D. degrees in Computer Science from U. Pennsylvania. He was a faculty member in MIT's Lab for Computer Science, researching functional programming, dataflow and multithreaded computer architectures, and continued this work at Digital Equipment Corp.'s Cambridge Research Lab. In 2003 he co-founded <a href="https://bluespec.com/">Bluespec</a>, Inc., and remains CTO, working on the BSV and BH High-Level Hardware Design Languages and their applications, using ideas from Haskell and atomic transactions. He has created several open-source RISC-V CPU and System designs, and chaired the RISC-V Foundation's technical group that selected the RISC-V ISA formal spec in Sail.

### From Precise Analysis to Efficient JIT Optimization — The Story of an Object Transformed by CompL {#thakur}

**[Manas Thakur](https://www.cse.iitb.ac.in/~manas/)** --- Assistant Professor, IIT Bombay

**Abstract.** Object-oriented programming and just-in-time (JIT) compilation are two pillars of modern large software systems. Yet, combining them effectively poses challenges while designing performant systems: object allocation, memory access, and garbage collection introduce significant overheads, while JIT compilers must keep program analysis lightweight and fast. This talk explores how precise program analysis — traditionally considered too expensive for JIT settings — can enable aggressive memory optimizations in modern JVMs without sacrificing efficiency.

I will present our recent work on static-analysis–guided optimistic stack allocation, supported by dynamic heapification to ensure correctness in the presence of language and runtime dynamism. I will also discuss how speculative JIT information can improve the precision of statically computed results. Together, these techniques demonstrate how ahead-of-time analysis and just-in-time compilation can be combined to achieve both precision and efficiency, leading to reduced garbage collection, improved performance, and new opportunities for memory optimizations in managed-language runtimes.

**Bio.** Manas Thakur is a faculty member in the Department of Computer Science and Engineering at Indian Institute of Technology (IIT) Bombay. His research interests include program analysis, compiler optimizations, and programming languages. Manas holds PhD and Masters degrees in Computer Science and Engineering from IIT Madras. His thesis titled "Precise and Efficient Analysis of Java Programs" won one of the institute research awards and the IBM Best Thesis Award in 2019-20. Prior to joining IITB, Manas was at IIT Mandi where he received the Teaching Honour Roll Award in 2021; and recently, he was honoured with the Faculty of the Year 2024 award by IBM Centre for Advanced Studies. Manas's research group at IIT Bombay, named CompL [pronunciation: Compel], specializes in JIT compilers and has developed efficient optimization strategies for Java, JavaScript and R.

### TESSERA: Functionally Programming Petabytes of Earth Observations {#madhavapeddy}

**[Anil Madhavapeddy](https://anil.recoil.org/)** --- Professor of Planetary Computing, University of Cambridge

**Abstract.** I'll present TESSERA (geotessera.org), a pixel-wise foundation model for multi-modal (Sentinel-1/2) earth observation time series that learns robust, label-efficient embeddings. Our goal with TESSERA is to make manipulating global satellite intelligence as easy as LLMs did for natural language, but also with the robustness of functional programming!

Towards this we release global, annual, 10m, pixel-wise embeddings together with open weights and code and lightweight adaptation heads, providing practical tooling for large-scale retrieval and inference at planetary scale. As with any good foundation model, there are a staggering array of downstream tasks which can benefit. TESSERA embeddings deliver state-of-the-art accuracy with high label efficiency across diverse classification, segmentation, and regression tasks.

In this talk, I'll take you through an array of problems our users are applying it to, ranging from the ecological to the urban to the temporal. By the end of the talk, I'll aim to have you identify a seemingly impossible spatial problem that is now within range to solve yourself using our O(x)Caml, Python or Typescript interfaces. Bring your favourite coding agents too!

### A Programming Language for Lightweight Diagramming {#krishnamurthi}

**[Shriram Krishnamurthi](https://cs.brown.edu/~sk/) and Siddhartha Prasad** --- Brown University

**Abstract.** Formal modeling tools such as Alloy enable users to incrementally define, explore, verify, and diagnose specifications for complex systems. A critical component of these tools is a visualizer that lets users graphically explore generated models. However, a default visualizer that knows nothing about the domain can be unhelpful and can even actively violate presentational and cognitive principles. At the other extreme, full-blown custom visualization requires significant effort as well as knowledge that a tool user might not possess. Custom visualizations can also exhibit bad (even silent) failures. The same needs and demands apply to programming languages, which are virtually never accompanied by data structure visualizers.

We chart a middle ground between the extremes of default and fully-customizable visualization. We capture essential domain information for lightweight diagramming. To identify key elements of these diagrams, we ground the design in both cognitive science and in a corpus of custom visualizations. We distill from these sources a small set of orthogonal primitives, and use the primitives to guide a diagramming language.

We show how to endow the diagramming language with a spatial semantics and prove that it enjoys key properties. We also show how it can be embedded into three very different languages: Python, Rust, and Pyret. We present a novel counterfactual debugging aid for diagramming errors, combining textual and visual output. We evaluate the language and system for expressiveness, performance, and diagnostic quality. We thus define a new point in the design space of diagramming: through a language that is lightweight, effective, and driven by cognitively sound principles.

**Bio.** Shriram is the Vice President for Programming Languages at Brown University in Providence, RI, USA. He's not, really, but that's what it says on his business card. At heart, he's a person of ill-repute: a Schemer, Racketeer, and Pyreteer. He believes tropical fruit are superior to all other kinds. He is terrified of success, because he may be forced to buy a suit. On a more serious note, he's a professor at Brown who has created several influential systems (such as DrRacket, Margrave, Flapjax, and Lambda-JS) and written multiple widely-used books. He has won SIGPLAN's Robin Milner Young Researcher Award, SIGPLAN's Software Award (jointly), SIGSOFT's Influential Educator Award, SIGPLAN's Distinguished Educator Award (jointly), and other recognitions.

### Mechanising a Regex-Based Borrow Checker: An Experiment in AI-Assisted Metatheory {#sergey}

**[Ilya Sergey](https://ilyasergey.net/)** --- Associate Professor, National University of Singapore

**Abstract.** I will present a mechanised metatheory and a soundness proof for a regex-based borrow checker for Move, a Rust-inspired smart contract language used by Sui and Aptos blockchains. The type system tracks aliasing as regular expressions over field paths, using Brzozowski derivatives for field borrows and Kleene star for unbounded aliasing from calls and loops. In this model, write safety in the presence of aliasing reduces to a decidable regex emptiness check. Working with Claude Code over 27 intensive days, a single researcher has produced a full mechanisation of Move in 39K LOC of sorry-free Lean code. The formalisation has been extensively tested against the production Move compiler for compatibility and can serve as a reference implementation. Reflecting on the outcomes of this experiment, I will argue that AI-assisted formalisation of realistic programming languages shifts the bottleneck from writing proofs to designing invariants, making machine-checked mechanisation a practical tool for iterative prototyping of correct-by-construction type systems.

**Bio.** Ilya Sergey is an Associate Professor at the School of Computing of National University of Singapore, where he leads the Verified Systems Engineering lab. Ilya got his PhD in Computer Science at KU Leuven. Before joining NUS, he was a postdoctoral researcher at IMDEA Software Institute and a faculty at University College London. Ilya does research in programming language design and implementation, software verification, and distributed systems. He is a Program Committee Co-Chair for OOPSLA'27; he was the General Chair for ICFP 2025 and organised the ICFP Programming Contest in 2019. He is a recipient of several distinguished paper awards at POPL and PLDI, the 2019 Dahl-Nygaard Junior Prize, Yale-NUS Distinguished Researcher award, and academic research awards from Ethereum Foundation, Google, Meta, and Amazon.

---

If you have questions, reach out to [contact@fplaunchpad.org](mailto:contact@fplaunchpad.org).
