---
layout: post
title: "Talk: Property Based Testing to Verify Pipelined CPU Hardware — Rishiyur S. Nikhil"
date: 2026-04-09
---

**Speaker:** [Rishiyur S. Nikhil](https://github.com/rsnikhil) — CTO and Co-founder, [Bluespec](https://bluespec.com/)

**Date:** Friday, April 10, 2026, 2:00 PM – 3:30 PM IST

**Venue:** SSB 334 (A M Turing Hall), Department of CSE, IIT Madras

## Abstract

Property Based Testing of software is well established--- Haskell QuickCheck was the pioneer; Wikipedia lists ports to about 40 other programming languages. In this talk we describe our experience using QuickCheck with _hardware_, to verify "Fife", a 6-stage pipelined RISC-V CPU. We describe the setup for TestRIG (from the University of Cambridge): its use of Haskell QuickCheck for RISC-V test generation and for shrinking; use of the official RISC-V Formal Model written in the Sail ISA Description Language; necessary configuration of TestRIG and the Sail RISC-V Formal Model.

We describe necessary instrumentation for "Direct Instruction Injection" and effect-reporting in any implementation being tested (much of it reusable across implementations). We describe how to deal with a complication: a pipelined CPU's speculative instruction execution, due to branch and PC prediction, and traps. We describe proposed extensions to TestRIG to handle non-deterministic events (such as interrupts) and micro-architectural properties (not shared across implementations). We also briefly describe BlueCheck, an implementation of QuickCheck written in the hardware design language Bluespec BSV, so that BlueCheck can itself be run in hardware (such as an FPGA) along with the CPU design being tested, for much greater testing speed.

## Bio

Rishiyur Nikhil is CTO and co-founder of Bluespec, Inc., where he promotes high-level languages and methodologies for the design and verification of complex digital hardware. He is a key contributor to the BSV and BH open-source High-Level Hardware Design Languages and their applications, which use ideas from Haskell and atomic rule-based specs. He has created several open-source RISC-V CPU and System designs, and chaired the RISC-V Foundation's technical group that selected the RISC-V ISA formal spec in Sail.

His degrees are from U. Pennsylvania (CS PhD) and IIT Kanpur (EE BTech). His interests and R&D career (at MIT, Digital Equipment Corp. and some startups) span full systems, from formal methods and high-level programming languages to CPUs and system micro-architectures.
