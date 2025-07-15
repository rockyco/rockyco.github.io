---
layout: page
title: Projects
permalink: /projects/
---

# Research Projects & Open Source Contributions

## Open Source Projects

### 🏆 peakPicker - LLM-Aided FPGA Design Comparative Study
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/peakPicker) | ⭐ 8 stars | 🍴 3 forks

**First Quantitative LLM-FPGA Comparison Study**

Groundbreaking comparative study for 5G NR signal processing with systematic analysis of LLM-assisted vs. traditional FPGA design flows.

**Breakthrough Results:**
- **18x latency improvement** over baseline (6,035 → 336 cycles)
- **96% LUT reduction** (7,148 → 284 LUTs)
- **400 MHz clock frequency** achieved
- **Multiple LLM comparison**: Claude 3.7 Sonnet, Gemini 2.5 Pro, GitHub Copilot

**Innovation:** Complete open-source workflow with structured LLM prompting methodology and reproducible performance analysis.

---

### 🚀 pulseDetector - Signal Processing Automation
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/pulseDetector) | ⭐ 27 stars | 🍴 4 forks

**Automated MATLAB to FPGA Translation for DSP**

Demonstrates LLM-powered automation for signal processing applications with focus on cross-correlation and pulse detection algorithms.

**Key Results:**
- **304 MHz** operating frequency achieved
- **194 DSP blocks** utilization
- **Automated FIR IP integration** within HLS designs
- **Performance comparable to specialized HDL tools**

**Impact:** Foundation for 5G NR SSB detection and wireless signal processing applications.

---

### 🔧 llm-fpga-design - Multi-Agent Framework
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/llm-fpga-design) | ⭐ 15 stars | 🍴 5 forks

**AI-Agent Framework for FPGA Development**

Complete automation framework supporting multiple LLM providers (OpenAI, Google, Anthropic) with specialized agents for code generation, debugging, and optimization.

**Key Features:**
- **Multi-Agent Architecture**: Specialized agents for each development phase
- **60-70% development time reduction** achieved
- **Interactive CLI** with automated workflow orchestration
- **Multi-LLM Support**: GPT-4, Gemini, Claude compatibility

**Success:** Proven with 5G NR applications using FREE Gemini 2.5 Pro API.

---

### 📊 ImageProcessing - Sobel Filter Optimization
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/ImageProcessing) | ⭐ 14 stars | 🍴 2 forks

**LLM-Guided Memory and Latency Optimization**

Three HLS implementations showcasing dramatic improvements through Gemini 2.0 Flash optimization from memory-intensive baseline to highly optimized version.

### 📡 estFreqOffset - Wireless Communications
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/estFreqOffset) | ⭐ 8 stars | 🍴 5 forks

**Carrier Frequency Offset Estimation**

MATLAB to HLS automation for wireless communications with **75% development time reduction** and **90% resource savings** through optimized BRAM implementation.

### 🎓 LabTraining - Educational Resources
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/LabTraining) | ⭐ 10 stars | 🍴 1 fork

**Digital System Design Training Materials**

Comprehensive educational resources with step-by-step lessons and hands-on FPGA design projects for students.

---

## 🔬 Research & Proprietary Projects

### 🛰️ Space-Grade Hyperspectral Image Compression
**CCSDS 123.0-B-1 Implementation with LLM-Assisted Module Integration**

Five-module FPGA system for space applications achieving **41.7% LUT reduction** and **43.5% timing improvement** with perfect CCSDS standard fidelity.

### 🔄 Advanced Viterbi Decoder
**MATLAB-to-FPGA Automation**

Complete automation achieving **352 Mbps throughput** with ping-pong memory architecture and power-of-2 optimization. Pure combinational logic implementation reduces latency to 1 clock cycle.

### 🌐 Multi-User MIMO-OFDM Transceiver
**RFSoC System with Jamming Suppression**

Advanced wireless communication system with data flow feedback paths in HLS, single FFT IP core reuse, and Pareto-optimal hardware structures for 5G NR readiness.

### 🎯 MATLAB HDL Coder Timing Optimization
**Breaking the 250 MHz Barrier**

Revolutionary methodology achieving:
- **93.6% frequency improvement** (126.61 → 245.16 MHz)
- **98% timing slack recovery** (-3.898 → -0.079 ns)
- **52.2% critical path reduction** through LLM-guided pipelining

### 🔄 Asynchronous Stream Processing Framework
**Real-World Data Synchronization**

Solving multi-stream synchronization challenges from 5G NR to radar applications with **250 MHz performance** and **100% test success** rate.

### 🏭 Cross-Language Translation Platform
**Java-to-FPGA Implementation Bridge**

Pioneering cross-domain algorithm translation demonstrating LLM capabilities in bridging diverse programming paradigms for hardware implementation.

---

## 🌟 Real-World Deployments

### 🏗️ Complete USRP X310 Pipeline
Full LLM-assisted development pipeline from MATLAB prototyping to live hardware deployment for real-time 5G NR SSB detection from public cell towers.

### 📡 5G NR Signal Sensing Testbed  
2x2 MIMO system using OAIBox MAX + USRP X310 (gNB) and Quectel RM500Q-GL (UE) for environmental sensing applications including rainfall and water level detection.

### 🎯 Key Research Discoveries

**BRAM Mapping Critical Finding:** FIFO size ≥16 entries prevents BRAM mapping for entire designs, achieving **42× resource reduction** through optimization.

**Timing Closure Breakthrough:** LLM-guided methodology achieving **250 MHz operation** with 93.6% frequency improvement on Xilinx Kintex-7.

---

## Research Impact & Evolution

### 🎯 Innovation Areas
- **Automated Hardware Design**: Pioneering LLM-assisted FPGA development workflows
- **Performance Breakthroughs**: 18x latency improvements, 96% resource reductions, 250 MHz timing closure
- **Industry Applications**: Space-grade systems, 5G/6G communications, real-time deployments
- **Educational Impact**: Open-source methodologies and comprehensive training materials

### 💡 Development Journey
**Phase 1 (Dec 2024):** Proof of concept - *"Using LLMs for MATLAB to HLS conversion... results were amazing"*

**Phase 2 (2025):** Advanced optimization with one-shot translation and zero-iteration workflows using Claude 3.7 Sonnet and Gemini 2.0 Flash

**Phase 3:** Production deployment with complete USRP integration and multi-language support

### 🔍 Key Insights
**LLM Strengths:** Frame-to-stream transformation, constraint-driven prompting, progressive optimization achieving 18x improvements

**LLM Limitations:** Cannot interpret simulation waveforms - human expertise remains essential for complex debugging

**Hybrid Approach:** Combining AI automation with engineering expertise for optimal results

---

## GitHub Profile
[**github.com/rockyco**](https://github.com/rockyco) | 6+ repositories | 80+ stars | 2+ years LLM-FPGA research