---
layout: home
title: Home
---

<div class="home-hero">
  <h1>Jie Lei</h1>
  <p class="home-role">Research Fellow, University of Technology Sydney</p>
  <p class="lede">I build tools that turn algorithms into trustworthy hardware. My current work pairs AI with a disciplined, layer-by-layer verification method, so a design can be generated in days and still be proven correct, not just assumed to be.</p>
  <p class="links-row">
    <a href="{{ '/work/' | relative_url }}">Work</a>
    <a href="{{ '/blog/' | relative_url }}">Blog</a>
    <a href="https://github.com/{{ site.github_username }}">GitHub</a>
    <a href="{{ site.google_scholar }}">Scholar</a>
  </p>
</div>

For most engineers, getting an algorithm onto an FPGA means rewriting it by hand, line by line, and then spending weeks convincing themselves the hardware still does what the original did. It is slow, and it is easy to get subtly wrong.

I work on a different path. Starting from a reference design, an AI assistant generates the hardware in stages: first an executable math reference, then a hardware-timed model, then the circuit itself. The key is not that a machine wrote the code, but that every stage is checked against the one above it automatically. Correctness comes from the chain, not from anyone's word.

That method has produced a complete Wi-Fi receiver that runs on a pocket-sized radio, forward-error-correction decoders that reach commercial-grade clock speeds, signal-processing cores for space and 5G, and more. The most recent of these is written up on the blog.

<p class="links-row">
  <a href="{{ '/blog/' | relative_url }}">Read the latest post &rarr;</a>
  <a href="{{ '/work/' | relative_url }}">See the design showcase &rarr;</a>
</p>
