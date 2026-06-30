---
layout: post
title: "Why We Automate the Path from Algorithm to Silicon"
date: 2026-07-01
lang: en
translation_id: automating-algorithm-to-silicon
reading_time: 7
excerpt: "High-value radio and FPGA hardware spends most of its life idle, because crossing from an algorithm to a working system on it is still done by hand. This is the gap we are closing, and how checking every layer to the bit makes machine-generated hardware something you can trust."
---

High-value radio and FPGA hardware, the kind that can cost as much as a car, spends most of its
life idle. A lab or a team buys a software radio or an FPGA board, runs a few captures, and the
board goes on the shelf. The hardware can do far more than capture and playback. What stops it is
that doing real custom work on it is genuinely hard.

The other posts on this blog are evidence that it does not have to be: a Wi-Fi receiver generated
and brought up on a pocket radio, a decoder clocked past a commercial part, twenty decoders out of
one flow. This post is the why behind all of them.

## The compute is bought, and it sits idle

The barrier has two parts, and a project has to clear both.

The first is turning a software algorithm into efficient hardware. A processor runs one
instruction after another; a chip's fabric runs hundreds of operations in the same clock tick. The
same algorithm written merely to run, and written to run fast and small, are two different
designs, and the distance between them is a specialist skill.

The second is getting that hardware to actually run on the board: the interfaces, the data
movement, the drivers, the software around it. It takes someone fluent in both the low-level
fabric and the high-level software, and when something breaks it is hard to tell which layer
broke.

Those two barriers together keep expensive hardware underused, and keep the pool of people willing
to learn the craft shrinking.

<figure>
  <a class="zoom" href="{{ '/assets/blog/automating-algorithm-to-silicon/en/pain.png' | relative_url }}">
    <img src="{{ '/assets/blog/automating-algorithm-to-silicon/en/pain.png' | relative_url }}" alt="Costly hardware sits idle behind two barriers: turning a software algorithm into efficient logic, and integrating that logic so it runs on the board.">
  </a>
  <figcaption>Two barriers stand between an algorithm and a working system: writing efficient hardware, and integrating it so it actually runs on the board.</figcaption>
</figure>

## Why the existing tools fall short

Vendors have built tools to lower the barrier, and they help. The common experience is still the
same: the demo runs, and the moment you put your own design through it, problems appear. The flow
needs a lot of manual editing, and the tools move quickly.

Raising the level of abstraction does not close the gap on its own. The high-level tools that turn
C-like code into hardware leave a real gap in speed against hand-written logic, and getting good
results out of them still takes deep hardware experience.

The newer idea, letting a large language model write the hardware directly, runs into a problem it
cannot escape. The model produces hardware that looks reasonable and is functionally wrong. On the
standard benchmarks the best methods have pushed functional correctness up toward nine in ten, and
the rest is still wrong, with no method removing it entirely. The missing piece is trust.

<figure>
  <a class="zoom" href="{{ '/assets/blog/automating-algorithm-to-silicon/en/tool-gap.png' | relative_url }}">
    <img src="{{ '/assets/blog/automating-algorithm-to-silicon/en/tool-gap.png' | relative_url }}" alt="Existing tools leave a gap: the demo runs but your own design breaks, the flow stays manual, and a model writing the hardware directly produces wrong logic.">
  </a>
  <figcaption>Every existing path leaves the same gap: the demo runs, your own design breaks, the flow stays manual, and a model writing hardware directly still produces wrong logic.</figcaption>
</figure>

## One flow, from an algorithm to a working product

What we build is one automation flow that carries a Python algorithm through optimized hardware to
a running, integrated product on a real device. Not only the FPGA fabric: the same flow places
work on the host processor, the embedded core, and the accelerators that sit alongside them, and
lets them share the job.

The flow generates optimized hardware from the algorithm, closes the timing and trims the
resources, the parts of the work no one enjoys, and then carries the design onto the board: the
integration, the simulation before and after silicon, and the on-device test. Strung together,
that is one path from an algorithm to something that runs. The algorithm is at the front, the
working system is at the end, and the hard, tedious middle is automated.

<figure>
  <a class="zoom" href="{{ '/assets/blog/automating-algorithm-to-silicon/en/mission.png' | relative_url }}">
    <img src="{{ '/assets/blog/automating-algorithm-to-silicon/en/mission.png' | relative_url }}" alt="One pipeline: a Python algorithm to optimized hardware to system integration to an on-board product, landing on FPGA, embedded core, host CPU, and accelerators.">
  </a>
  <figcaption>One path, from a Python algorithm to a running on-board product, landing on whichever processors the deployment needs.</figcaption>
</figure>

## The hard part is trust

Getting a machine to write hardware is not the hard part. Getting it to write hardware you can
trust is. The answer is a chain of three models, where each one is the reference for the next,
plus a set of automatic guardrails.

The three are a mathematical model, a clock-accurate model, and the hardware itself. The
mathematical model, checked against the governing standard, is the arbiter of right and wrong. The
clock-accurate model mirrors the hardware tick by tick. The hardware is generated from it and
checked against it, bit for bit, with the test cases generated by the math and never written by
hand. Three models, identical to the bit, or it does not pass.

Around that chain sit guardrails that an automatic check enforces: every number traces to a real
tool report, nothing is rewritten before it is measured, and a design that runs continuously is
tested back to back with no reset. I have written about this in more detail in the post on how the
Wi-Fi receiver is proven correct layer by layer. The short version is that trustworthy
machine-written hardware comes not from the model being clever, but from every step being checked
against an independent reference.

<figure>
  <a class="zoom" href="{{ '/assets/blog/automating-algorithm-to-silicon/en/trust-chain.png' | relative_url }}">
    <img src="{{ '/assets/blog/automating-algorithm-to-silicon/en/trust-chain.png' | relative_url }}" alt="A chain of three models, math then clock-accurate then hardware, checked to the bit at each step, with a ring of automatic guardrails.">
  </a>
  <figcaption>Three models, checked to the bit at each step, with a ring of automatic guardrails. Wrong hardware never clears the gate to the next stage.</figcaption>
</figure>

## It is proven, not promised

The method is not a plan. It is already on real silicon.

A complete Wi-Fi receiver runs on a pocket-sized radio, recovering every one of the eight standard
modes over the air, bit for bit, with the design split across the radio's fabric and a laptop
because it was too large for the small chip alone. A 5G error-correcting decoder, generated from a
Python description, was optimized to clock past a paid commercial part on the same chip. Twenty
decoder configurations came out of one flow, each checked against the standard. Each of those is
written up, in plain language, on this blog.

## What comes next

Two directions. One is platforms, from the pocket radio out to the larger software-radio and RF
system-on-chip boards. The other is processors, from the FPGA out to the CPU, the embedded core,
and the accelerators working together. The aim is the same throughout: turn the path from an
algorithm to silicon into an automation flow you can trust, so the compute people already own gets
used, instead of sitting on a shelf.

<figure>
  <a class="zoom" href="{{ '/assets/blog/automating-algorithm-to-silicon/en/roadmap.png' | relative_url }}">
    <img src="{{ '/assets/blog/automating-algorithm-to-silicon/en/roadmap.png' | relative_url }}" alt="Two directions ahead: platforms from the pocket radio to larger software radios and RF system-on-chip boards, and processors from FPGA to CPU, embedded core, and accelerators.">
  </a>
  <figcaption>Two directions ahead: more platforms, and more processors working together.</figcaption>
</figure>

Most of us have a board on a shelf and an algorithm in a file, and a quiet sense that connecting
the two would cost more than it is worth. What would change if it did not?

## Notes

- The case studies behind this post, the Wi-Fi receiver, the LDPC decoders, and the Viterbi
  folding, are on the [blog index]({{ '/blog/' | relative_url }}).
- A live over-the-air demo of the Wi-Fi receiver replays real captured data in the browser at
  [algosilicon.com/assets/demos/wlan-pluto-rx](https://algosilicon.com/assets/demos/wlan-pluto-rx/).
- The few proof points here are qualitative summaries of measured results detailed in those posts.
