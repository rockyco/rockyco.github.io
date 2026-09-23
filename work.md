---
layout: page
title: Work
permalink: /work/
---

Communications hardware I have designed, from error-correction and signal-processing cores to complete wireless physical layers. Everything below was generated and verified with the same AI-assisted method: a design is built
as a math reference, then a hardware-timed model, then the circuit, and each layer is
machine-checked against the one above it, so correctness rests on evidence rather than
assumption. These are described in plain terms, as methods and capabilities rather than
benchmark figures.

<div class="cards">

  <div class="card">
    <h3>Python2Verilog, the framework</h3>
    <p>The evidence-governed flow behind every design on this page. It takes an executable algorithm through a math reference, a hardware-timed model, the circuit, implementation and board deployment, with a gate at every step. AI proposes candidates; standard tools execute them; independent checks decide acceptance, and those checks are themselves proven to catch planted faults before their verdicts count. Accepted designs become reusable families, and the output ships as modular kits, from portable RTL through board bring-up, embedded Linux and interconnect up to a working application.</p>
    <p class="meta"><a href="https://github.com/{{ site.github_username }}">Code on GitHub</a></p>
  </div>

  <div class="card">
    <h3>Quantum error-correction decoder</h3>
    <p>The real-time classical decoder a fault-tolerant quantum computer cannot run without, rebuilt from first principles for IBM's gross code and generated from a model checked against the mathematics at every step. The work traced where such a decoder's speed limit comes from - the wiring of the code's graph rather than its logic - which makes the useful lever algorithmic: stop a stuck decoding attempt early.</p>
    {% assign qpost = site.posts | where: "translation_id", "ibm-relay-bp-quantum-ldpc" | where: "lang", "en" | first %}
    <p class="meta"><a href="{{ qpost.url | relative_url }}">Read the full write-up</a></p>
  </div>

  <div class="card">
    <h3>802.11a Wi-Fi receiver</h3>
    <p>A complete Wi-Fi receiver, generated without anyone hand-writing the hardware, that decodes standard signals end to end and runs on a pocket-sized, USB-powered radio. Fed a standard waveform from MATLAB's own toolbox, it recovers the transmitted image bit-for-bit across every supported modulation.</p>
    <p class="meta"><a href="{{ '/blog/' | relative_url }}">Read the full write-up</a></p>
  </div>

  <div class="card">
    <h3>5G error-correction decoder</h3>
    <p>The forward-error-correction engine at the heart of a 5G base station, generated across a wide range of code configurations, each matching the standard's reference exactly. Timing work on the flagship configuration shows how to close a deep, wiring-dominated decoder pipeline: find where the delay really sits, then cut it with registers placed where they help.</p>
    {% assign lpost = site.posts | where: "translation_id", "ldpc-clock-past-commercial-ip" | where: "lang", "en" | first %}
    <p class="meta"><a href="{{ lpost.url | relative_url }}">Read the full write-up</a></p>
  </div>

  <div class="card">
    <h3>Deep-space decoder</h3>
    <p>An error-correction decoder for the codes that protect deep-space and satellite links, where a signal must survive extreme noise. One design covers every code size and rate of the standard, switching between them on the fly. It is validated on real silicon and sold as a licensed core with its own datasheet and user guide.</p>
  </div>

  <div class="card">
    <h3>Wi-Fi transceiver on a custom RFSoC board</h3>
    <p>A complete Wi-Fi transmitter, receiver and link layer, running three generations of the standard from a single design that switches between them at runtime, with LDPC error-correction coding. On a custom radio board, with Linux on the chip's processors driving it, it carries live video over a real radio link.</p>
    {% assign rpost = site.posts | where: "translation_id", "linux-on-an-rfsoc-board-in-a-day" | where: "lang", "en" | first %}
    <p class="meta"><a href="{{ rpost.url | relative_url }}">How the board was brought up</a></p>
  </div>

  <div class="card">
    <h3>4G base-station physical layer</h3>
    <p>The full physical layer of an LTE base station, both directions: random access, uplink data and control, turbo decoding and the downlink signal chain, serving many users from one shared datapath. It is checked against a MATLAB reference end to end, closed as a single implementation on one RFSoC chip, and its turbo decoder runs on real silicon.</p>
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
    <p>A maximum-likelihood decoder for the codes used in nearly every wireless standard, from Wi-Fi to satellite links. Folding the decoder trades logic against throughput while holding the clock, giving a menu of size-versus-speed points; a compact version runs inside the Wi-Fi receiver above, every mode bit-exact.</p>
    {% assign vpost = site.posts | where: "translation_id", "viterbi-resource-folding" | where: "lang", "en" | first %}
    <p class="meta"><a href="{{ vpost.url | relative_url }}">Read the full write-up</a></p>
  </div>

</div>

For the formal designs, validation, and measured results, see my
<a href="{{ site.google_scholar }}">publications</a> and
<a href="https://github.com/{{ site.github_username }}">open-source repositories</a>.
