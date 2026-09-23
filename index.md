---
layout: home
title: Home
---

<div class="home-hero">
  <h1>Jie Lei</h1>
  <p class="home-role">Creator of Python2Verilog &middot; Founder, AlgoSilicon</p>
  <p class="lede">I build Python2Verilog, a framework that takes an algorithm all the way to working FPGA silicon, as IP cores and complete hardware systems, with the evidence attached. Every design it produces is checked layer by layer, so its correctness rests on evidence rather than assumption.</p>
  <p class="links-row">
    <a href="{{ '/work/' | relative_url }}">Work</a>
    <a href="{{ '/blog/' | relative_url }}">Blog</a>
    <a href="https://github.com/{{ site.github_username }}">GitHub</a>
    <a href="{{ site.google_scholar }}">Scholar</a>
  </p>
</div>

For most engineers, getting an algorithm onto an FPGA means rewriting it by hand, line by line, and then spending weeks convincing themselves the hardware still does what the original did. It is slow, and it is easy to get subtly wrong.

Python2Verilog takes a different path. Starting from a working algorithm, the hardware is built in stages: first an executable math reference, then a hardware-timed model, then the circuit, then the board and the application on top. AI proposes the candidates, standard engineering tools run them, and independent checks decide what is accepted, including checks that have first been shown to catch deliberately planted faults. Correctness comes from the chain, not from anyone's word, and every design that passes becomes a reusable family for the next one.

The framework is not tied to one field. Its demonstrations so far span error correction, signal processing and wireless systems: 5G and deep-space decoders, one of them now sold as a licensed core; a Wi-Fi transceiver carrying live video over a real radio link on a custom board; a complete 4G base-station physical layer; and a Wi-Fi receiver that runs on a pocket-sized radio. Before building it, I spent many years on image processing and computer vision hardware, including image compression for lunar and Mars missions. The most recent work is written up on the blog.

<p class="links-row">
  <a href="{{ '/blog/' | relative_url }}">Read the latest post &rarr;</a>
  <a href="{{ '/work/' | relative_url }}">See the design showcase &rarr;</a>
</p>
