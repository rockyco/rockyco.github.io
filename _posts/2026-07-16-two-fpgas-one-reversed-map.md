---
layout: post
title: "Two FPGAs, One Backwards Map: When Every Simulation Lies"
date: 2026-07-16
lang: en
translation_id: two-fpgas-one-reversed-map
reading_time: 8
excerpt: "A ten-gigabit link between two chips would not carry data one direction, while every simulation, every eye diagram, and every netlist said it was perfect. The fault was not in the circuit. It was one line in a wiring record, written backwards, that every simulation faithfully obeyed."
---

The board has two large chips on it: a Zynq UltraScale+ RFSoC and a Kintex UltraScale FPGA
beside it, tied together by eight high-speed serial lanes. In the last post an AI brought this
blank board up to a login prompt in a day. This post is the next step: turning the second chip
into an extension of the first, so a module can run over there and use the four gigabytes of
memory sitting next to it. An AI did the work under the Python2Verilog framework; I gave the
direction at a few key points.

It should have been routine. Instead it turned into the most stubborn kind of bug: everything
measured perfect, and the hardware did nothing.

## One direction that would not work

The link uses a standard serial encoding: the receiver watches for a run of well-formed markers
and, once it sees enough of them in a row, declares itself locked. One direction locked almost
immediately. The other direction never did. The lock detector just kept sliding, forever a hair
short.

So we chased it, and every step produced a clean result. The vendor's own example locked in
simulation. A loopback locked and matched a frame bit-for-bit. A cross-chip simulation wired to
the real connections locked in both directions and matched byte-for-byte. Four hundred thousand
bits pushed across a simulated wire showed the markers landing correctly at exactly one offset. A
post-layout comparison of the working and broken designs came back identical, pin for pin.

Five checks, all green. The hardware stayed exactly as broken as before. And the physical signal
was pristine: the eye diagram was wide open, roughly 78 percent horizontal and 94 percent
vertical. The signal quality was flawless, which is precisely why the signal quality was not the
problem. Every layer of the circuit had been checked and cleared. So what was actually running on
that wire?

## Catching the real bytes

Every observation so far had been a statistic: a lock rate, a validity percentage, a pass or a
fail. Statistics are the problem here, because a statistic answers yes or no and hides what the
signal actually is. So the AI added a one-shot grabber that read three raw words straight off the
wire while the link claimed to be locked. They came back like this:

    0x6666666666666666
    0x9999999999999999
    0x6666666666666666

That is not data. Real payload, once scrambled, should look like noise. This is `0011` repeating:
a plain square wave, a free-running clock with nothing riding on it.

<figure>
  <a class="zoom" href="{{ '/assets/blog/two-fpgas-one-reversed-map/en/fig1_square_wave.png' | relative_url }}">
    <img src="{{ '/assets/blog/two-fpgas-one-reversed-map/en/fig1_square_wave.png' | relative_url }}" alt="A square wave sliced into 66-bit frames. Because 66 leaves a remainder of 2 when divided by 4, every frame's two-bit sync header lands on 01 or 10, both of which are valid, so the lock detector, the eye check, and the validity meter are all satisfied while no data is present.">
  </a>
  <figcaption>Why a clock pattern passes every health check. Sliced into frames, its header always lands on a legal value, so lock, eye, and validity all read perfect. None of them look at the payload.</figcaption>
</figure>

The coincidence that makes this so convincing is small and mean. The frame is 66 bits, and 66
divided by 4 leaves a remainder of 2, so from one frame to the next the pattern shifts by exactly
two bits and the two-bit header always lands on either `01` or `10`. Both are the legal values a
real header can take. A pure clock pattern therefore satisfies lock, satisfies the eye, satisfies
the marker-validity meter, and carries no information at all.

<figure>
  <a class="zoom" href="{{ '/assets/blog/two-fpgas-one-reversed-map/en/fig5_wire_capture.png' | relative_url }}">
    <img src="{{ '/assets/blog/two-fpgas-one-reversed-map/en/fig5_wire_capture.png' | relative_url }}" alt="Two waveforms captured off the same wire with the same grabber. The top trace is the clean, perfectly periodic square wave seen on thirty separate snapshots. The bottom trace, taken later on the correct lane, is irregular real scrambled data that descrambles to a standard idle block.">
  </a>
  <figcaption>The same wire, the same grabber. Top: the square wave, identical on all thirty snapshots. Bottom: real scrambled traffic on the correct lane. One capture ruled out an entire category of guesses about the data path.</figcaption>
</figure>

That single capture was worth more than all the statistics before it. It closed off an entire
class of hypotheses in one shot: the data path was not mangling anything, because there was no
data on this wire to mangle. Something else was.

## The map was backwards

If the wire carries a free-running clock, then nothing is driving it. The AI went back and
measured the lane connections directly, trusting only the physical names printed on both chips,
not the tool's internal numbering, and sending a distinct coded marker down each lane so it could
tell them apart. Three rounds resolved all eight. The result was the exact reverse of the record
everyone had been trusting.

<figure>
  <a class="zoom" href="{{ '/assets/blog/two-fpgas-one-reversed-map/en/fig2_lane_map.png' | relative_url }}">
    <img src="{{ '/assets/blog/two-fpgas-one-reversed-map/en/fig2_lane_map.png' | relative_url }}" alt="Two panels. The recorded map, in orange, shows lanes connecting straight across, lane i to lane i. The measured map, in green, shows them crossing over, lane i to lane 7 minus i. The listener the design watched was actually wired to a lane that was never configured, which free-ran the square wave.">
  </a>
  <figcaption>Left, the record everyone trusted: lanes straight across. Right, the measured truth: lanes reversed. The transmitter was sending correct data to a lane no one was listening to; the listener was wired to a lane never configured, which free-ran the clock.</figcaption>
</figure>

Here is the trap that let it survive so long. The transmitter really was sending correct data.
It was just sending it to a lane nobody was listening on, while the input everyone watched was
connected to a lane that had never been configured and so oscillated on its own. Every simulation
had wired itself from that same record. The record was internally consistent, so every simulation
reproduced the same wrong connection and passed. Five layers of verification agreed with each
other because they all read from one shared, wrong assumption.

Someone reasonable will ask: the eight lanes had a bit-error-rate test, and seven came back with
zero errors. How did that miss a swap? Because that test sends the same pattern down every lane,
so no matter how they are connected, each receiver locks and reads zero errors. It is blind by
design to which lane connects to which. Every strand of copper was genuinely fine. What was wrong
was the table that said which strand went where.

The honest, uncomfortable detail: that record even carried a note saying it had been "verified on
silicon". The note was real, but the verification behind it was the accidental lock of the very
first lane. No one had gone back to the schematic, because a result stamped "measured" feels safer
than seventy-five pages of PDF drawings, and tracing eight differential pairs by hand across those
pages is exactly the kind of thing that goes wrong. The answer had been sitting on the schematic
the whole time. Rewired to the two correct lanes, the link came up on the first try and matched
byte for byte.

## The second chip becomes an extension

With the link honest, the rest fell into place. There was a second machine-reading job on the way:
the four gigabytes of memory next to the second chip had no usable pinout file, only the same
seventy-five-page schematic. The AI turned that into a geometry problem, pairing each pin number
with its net name by position on the page and refusing to accept anything that did not match up
twice. Every net resolved with zero conflicts, and the memory passed its calibration on the first
power-up.

From there the second chip became three things to the first: a ten-gigabit pipe, a place to run
compute, and a block of remote memory. Each was proven on the real hardware, not in simulation. A
quarter-megabyte round trip came back byte-for-byte. A decoder ran on the second chip, took its
soft input across the link and handed the hard result back, and matched the reference model with
zero errors, twice in a row without a reset in between. A write to the far memory and a read back
matched exactly, at one address and then at another deep in the range.

There was one loose end worth keeping. During the earlier bring-up, one of the eight lanes had
shown a few bit errors. Before closing out, the AI soaked that lane alone for ten minutes:
six trillion bits, zero errors, an eye as open as the other seven. The earlier errors never came
back. The quiet punchline is that this was the same lane the reversed link had been using.

## What survives this

Three rules went back into the framework as required checks, and they generalize past this one
board:

Lock is not data. A signal can satisfy every health metric a link exposes, lock, eye, validity,
all of it, and still carry nothing. A link is not proven until you decode a real payload and check
it byte for byte.

Trust the measurement, not the record. Read the connection by its physical name, drive each lane
with a signal that can only have come from that lane, and treat the tool's numbering as a
convenience, not a fact.

Trust the machine, not the transcription. A pinout hand-copied from a drawing is a source of
quiet errors. Extract it by geometry, demand zero conflicts, and let a downstream check referee it.

The most expensive lesson is the general one. When every layer of the circuit has been checked and
cleared, the thing left to doubt is the measurement itself. That backwards record survived a full
day of work for one reason: every simulation was faithfully obeying it. The circuit was never
lying. The map was.

## Notes

- Hardware: a custom board pairing an AMD Zynq UltraScale+ RFSoC (XCZU67DR) with an AMD Kintex
  UltraScale FPGA (XCKU115), linked by eight high-speed serial lanes.
- The link, remote-compute, and remote-memory logic, and all of the debugging, were done by an AI
  under the Python2Verilog framework. Numbers cited are readings taken on the board and outputs
  from tool reports in the same session.
- This is a follow-on to "Bringing Up Linux on an RFSoC Board in a Day".
