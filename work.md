---
layout: page
title: Work
permalink: /work/
---

Everything below was generated and verified with the same AI-assisted method: a design is built
as a math reference, then a hardware-timed model, then the circuit, and each layer is
machine-checked against the one above it. The result is hardware that is fast, compact, and
proven correct by construction. These are described in plain terms; the underlying numbers live
in the design reports.

<div class="cards">

  <div class="card">
    <h3>The framework</h3>
    <p>An AI-assisted toolchain that turns a high-level algorithm into trustworthy FPGA hardware. Where a known design family fits, it emits proven hardware directly; where it does not, it explores carefully and folds the result back into the library. The verification chain is what makes its output trustworthy.</p>
    <p class="meta"><a href="https://github.com/{{ site.github_username }}">Code on GitHub</a></p>
  </div>

  <div class="card">
    <h3>802.11a Wi-Fi receiver</h3>
    <p>A complete Wi-Fi receiver, generated without anyone hand-writing the hardware, that decodes standard signals end to end and runs on a pocket-sized, USB-powered radio. Fed a standard waveform from MATLAB's own toolbox, it recovers the transmitted image bit-for-bit across every supported modulation.</p>
    <p class="meta"><a href="{{ '/blog/' | relative_url }}">Read the full write-up</a></p>
  </div>

  <div class="card">
    <h3>5G error-correction decoder</h3>
    <p>The forward-error-correction engine at the heart of a 5G base station, generated and tuned automatically across a wide range of code configurations and reaching clock speeds on par with commercial-grade IP. It shows that disciplined automation can match hand-optimized hardware at scale.</p>
  </div>

  <div class="card">
    <h3>Deep-space decoder</h3>
    <p>An error-correction decoder for the codes that protect interplanetary links, where a signal crossing the solar system must survive extreme noise. Generated as a family spanning several code sizes and rates for satellite and deep-space missions.</p>
  </div>

  <div class="card">
    <h3>Streaming spectral engine</h3>
    <p>A fast Fourier transform core, the spectral heart of OFDM radios such as Wi-Fi and 5G. It streams one sample per clock without stalling and adapts cleanly to different transform sizes.</p>
  </div>

  <div class="card">
    <h3>Digital filter library</h3>
    <p>A family of configurable filters for conditioning radio signals, from simple anti-aliasing filters to multi-stage rate-changing chains. The generator leans on the FPGA's dedicated arithmetic blocks to keep every design lean.</p>
  </div>

  <div class="card">
    <h3>Convolutional decoder</h3>
    <p>A maximum-likelihood decoder for the codes used in nearly every wireless standard, from Wi-Fi to satellite links. An AI folded it down to a third of its logic while holding the full-speed clock, producing a menu of size-versus-speed points; the compact version runs inside the Wi-Fi receiver above, every mode bit-exact.</p>
    {% assign vpost = site.posts | where: "translation_id", "viterbi-resource-folding" | where: "lang", "en" | first %}
    <p class="meta"><a href="{{ vpost.url | relative_url }}">Read the full write-up</a></p>
  </div>

</div>

For the formal designs, validation, and measured results, see my
<a href="{{ site.google_scholar }}">publications</a> and
<a href="https://github.com/{{ site.github_username }}">open-source repositories</a>.
