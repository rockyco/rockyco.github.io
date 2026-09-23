---
layout: page
title: About
permalink: /about/
---

I build Python2Verilog, a framework that takes an executable algorithm to working FPGA silicon, as
IP cores and complete hardware systems, and I am the founder of AlgoSilicon, a small company that
builds and licenses verified FPGA IP. The framework is not tied to one application domain: so far it
has produced error-correction decoders (LDPC, turbo and Viterbi), signal-processing cores such as
FFTs and filters, and complete wireless physical layers for Wi-Fi, 4G and 5G, each taken from the
algorithm and its fixed-point behaviour through the architecture, the circuit and timing closure, to
hardware running on real boards.

Python2Verilog is an individual project; its results led to a government commercialisation grant from
Australia's Economic Accelerator. Every design
is built as a math reference, then a hardware-timed model, then the circuit, and each layer is checked against
the one above it before the result is confirmed again on silicon. AI proposes candidates, but independent checks,
proven to catch planted faults, decide what is accepted. Designs that pass become reusable families and ship as
modular kits, from portable RTL up to a working application on a board.

Before building it, I spent twenty years on signal-processing hardware, leading a university research group in
image processing and computer vision on FPGA, including on-board image compression for lunar and Mars missions.

## Experience

**Founder and Principal FPGA Engineer** - AlgoSilicon Ltd, United Kingdom (2026 - present)
FPGA IP cores and design services built with Python2Verilog, from architecture through
verification to customer delivery. Current lines: error correction, DSP and wireless physical layers.

**Research Fellow** - University of Technology Sydney, Australia (Dec 2023 - Dec 2025)
Wireless physical-layer and MAC hardware on RFSoC and Zynq platforms, and an algorithm-to-hardware
framework that generates verified designs, in collaboration with MathWorks and AMD/Xilinx
engineering teams.

**Professor** - Xidian University, China (2020 - 2023)
Led a research group in algorithm-hardware co-design and FPGA implementation for satellite and
airborne payloads.

**Associate Professor** - Xidian University, China (2010 - 2020)
Image coding and hyperspectral image processing, and their FPGA implementation for satellite and
airborne systems.

**Visiting Scholar** - University of California, Los Angeles, USA (2014 - 2016)
Research with Prof. Jason Cong on high-throughput FPGA accelerators using high-level synthesis.

## Education

**PhD, Signal and Information Processing** - Xidian University (2006 - 2010)

**MEng, Telecommunication and Information Systems** - Xidian University (2003 - 2006)

**BEng, Electronic and Information Engineering** - Xidian University (1999 - 2003)

## Elsewhere

- [Google Scholar]({{ site.google_scholar }}) - full publication list and citation metrics
- [GitHub](https://github.com/{{ site.github_username }}) - open-source frameworks and designs
- [LinkedIn](https://www.linkedin.com/in/jie-lei-601342112) - professional profile
- Email: [jiejielei@gmail.com](mailto:jiejielei@gmail.com)
