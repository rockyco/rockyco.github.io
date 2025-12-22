---
layout: page
title: Projects
permalink: /projects/
---

# Research Projects & Open Source Contributions

## Featured Projects

### 🎯 A2HCoder: LLM-Driven Algorithm-to-HDL Translation Framework
[![GitHub](https://img.shields.io/badge/GitHub-Research%20Repository-blue?logo=github)](https://github.com/rockyco/LLM4FPGA) | **Academic Research** | **UTS Publication**

**Hierarchical Algorithm-to-HDL Coding Agent Powered by Large Language Models**

A groundbreaking research framework that addresses the critical gap between MATLAB-based algorithm design and FPGA hardware deployment, specifically targeting 5G wireless communication systems with novel LLM-driven methodologies.

**Research Innovation:**
- **First hierarchical LLM-driven algorithm-to-hardware translation framework**
- **Three-stage processing pipeline**: Code Adaptation → Translation → Optimization & Refinement
- **Novel approach to mitigating LLM hallucinations** through structured refinement
- **Complete 5G SSB detection system** deployed on USRP X310 platform

**Performance Breakthroughs:**
- **98.1% LUT reduction** compared to direct translation approaches
- **74.7% additional LUT reduction** with refinement stage
- **16.2% latency improvement** through systematic optimization
- **292 MHz timing closure** achieved on Kintex-7 FPGA

**Academic Impact:**
- **Authors**: Jie Lei¹, Ruofan Jia², J. Andrew Zhang¹†, Hao Zhang¹
- **Affiliations**: ¹University of Technology Sydney, ²Xidian University
- **Complete research paper** with LaTeX source and comprehensive evaluation
- **Interactive web demonstration** with live implementation examples

**Technical Architecture:**
- **Horizontal Decomposition**: Breaking algorithms into modular functional blocks
- **Vertical Refinement**: MATLAB → optimized MATLAB → HLS C++ → HDL progression
- **Stream-based Adaptation**: Converting frame-based to streaming architectures
- **Agent-style Feedback Loops**: Iterative LLM revision based on synthesis results

**Real-World Validation:**
- **Five core 5G NR submodules**: pssCorrelator, calcThreshold, peakFinder, collectLocations, extractSSBsig
- **Complete USRP X310 deployment** with functional validation
- **RFNoC framework integration** for software-defined radio applications

**Technologies:** MATLAB, HLS C++, Vitis HLS, Xilinx toolchain, RFNoC, AXI4-Stream, USRP X310, LaTeX

---

### 🚀 MATLAB2HLS: Universal Algorithm Transformation Framework
[![GitHub](https://img.shields.io/badge/GitHub-Production%20Framework-blue?logo=github)](https://github.com/rockyco/MATLAB2HLS) | **Production Ready** | **Enterprise Grade**

**Universal MATLAB-to-HLS Transformation Framework with Agent-Based Automation**

The practical implementation evolution of the A2HCoder research, featuring a production-ready framework that bridges algorithm development and FPGA deployment through sophisticated agent orchestration and universal template libraries.

**Framework Innovation:**
- **Multi-Stage Progressive Enhancement**: Foundation → Advanced → Industrial progression
- **Universal Template Library**: 21+ foundation templates supporting any MATLAB algorithm
- **Agent-Based Automation System**: 6 specialized agents orchestrating complete workflow
- **Quality Assurance Framework**: Mandatory simulation gates ensuring MATLAB equivalence

**Performance Achievements:**
- **95% error reduction** through foundation templates
- **217 MHz timing closure** with advanced FSM architectures
- **256-cycle latency reduction** via industrial framework optimizations
- **17.7x speedup improvement** demonstrated in laggedProduct case study

**Production Features:**
- **Template-Driven Development**: 60% development time reduction
- **Algorithm-Agnostic Transformation**: Universal patterns for any MATLAB code
- **Enterprise CI/CD Integration**: Industrial-grade deployment capabilities
- **Comprehensive Validation**: Two-stage floating-point → fixed-point validation

**Case Study Results:**
**Case 1 - laggedProduct Complex Matrix Algorithm:**
- **94% latency reduction**: 147,767 → 8,333 cycles
- **Interface optimization**: AXI → BRAM transformation
- **Resource efficiency**: Systematic LUT and DSP optimization

**Case 2 - 5G NR PSS Correlator:**
- **High-throughput design**: 18.75 MSps processing rate
- **3 parallel correlators** for all PSS sequences
- **Fixed-point optimization** with careful bit-width analysis
- **Complete MATLAB golden reference validation**

**Agent Orchestration System:**
- **Analysis Agent**: Code structure and dependency analysis
- **Implementation Agent**: HLS C++ code generation with pragmas
- **Simulation Agent**: Comprehensive testbench validation
- **Synthesis Agent**: Automated Vitis HLS workflow management
- **Optimization Agent**: Performance and resource optimization
- **Validation Agent**: End-to-end verification and reporting

**Technologies:** MATLAB, C++/HLS, Python, Xilinx Vitis HLS, AXI Stream, Agent Architecture, CI/CD Pipeline

---

### 🤖 MATLAB2HDL: Production-Ready Multi-Agent Framework
[![GitHub](https://img.shields.io/badge/GitHub-Production%20Framework-blue?logo=github)](https://github.com/rockyco/MATLAB2HDL) | **Industrial Grade** | **Web-Based Interface**

**Sophisticated Multi-Agent Framework for Automated MATLAB-to-HDL Transformation**

The evolution of the A2HCoder research into a production-ready, industrial-grade framework featuring comprehensive automation, web-based monitoring, and exceptional performance metrics across diverse signal processing algorithms.

**Framework Excellence:**
- **>95% Task Success Rate** with <3 second agent load times across all algorithm types
- **Multi-Agent Orchestration**: Specialized agents for analysis, transformation, validation, and synthesis
- **RAG Architecture**: Intelligent knowledge management with automated pattern synthesis
- **Web Interface**: Interactive workflow management through GitHub Pages with real-time monitoring

**Outstanding Results - Case 7 (PAM4 Receiver):**
- **86% DSP Reduction** through intelligent architecture optimization
- **7.5x Frequency Improvement** via balanced pipeline design
- **97.58% Decision Accuracy** over 10,000 test vectors
- **9.38e-05 BER at SNR=30dB** (20x improvement over baseline)
- **Long-term Stability**: Indefinite operation vs. original algorithm failure

**Production Features:**
- **7 Comprehensive Case Studies**: From AGC to complete PAM4 communication systems
- **Time-Multiplexing Intelligence**: Automatic resource explosion detection and optimization
- **Synthesis-Aware Decisions**: IOB, DSP, and memory optimization
- **Template System**: Algorithm-adaptive optimization patterns
- **Industrial Validation**: Full Xilinx Vivado integration with comprehensive reports

**Technologies:** MATLAB, HDL Coder, Xilinx Vitis HLS, Node.js, GitHub Pages, Multi-Agent Systems, RAG Architecture

---

### 🔍 HarrisCorner: AI-Driven Computer Vision Acceleration
[![GitHub](https://img.shields.io/badge/GitHub-Computer%20Vision-blue?logo=github)](https://github.com/rockyco/HarrisCorner) | **Zero-Error Implementation** | **366.7 MHz Performance**

**Complete AI-Powered MATLAB-to-FPGA Transformation for Computer Vision**

Demonstrates breakthrough AI-assisted development achieving perfect functional accuracy through systematic debugging methodology, transforming Harris Corner Detection from MATLAB to production-ready FPGA implementation.

**Technical Achievements:**
- **366.7 MHz Frequency** (22% above 300 MHz target) with 0% error rate
- **Perfect Functional Accuracy**: Zero-error implementation through iterative AI refinement
- **Exceptional Resource Efficiency**: <2% FPGA utilization (3,775 LUTs, 39 DSPs)
- **1 Pixel/Cycle Throughput** with II=1 pipeline efficiency
- **14.162 μs Latency** for 64x64 image processing

**AI-Driven Development Breakthrough:**
- **1,500+ Lines of Code** generated by Claude with systematic debugging
- **Evolution from 2.73% → 0% Error** through intelligent iterative refinement
- **Modular 5-Stage Pipeline**: Sobel → Structure Tensor → Gaussian → Harris Response → Non-Maximum Suppression
- **Stream-based Architecture**: Minimal buffering with optimal dataflow design

**Engineering Excellence:**
- **Modular Design Philosophy**: Isolated testing and validation for each component
- **Comprehensive Documentation**: Technical reports and interactive GitHub Pages website
- **Professional Visualization**: Performance dashboards and detailed analysis reports
- **Production-Ready Quality**: Suitable for commercial computer vision applications

**Technologies:** MATLAB, Xilinx Vitis HLS, Zynq UltraScale+, Python/Matplotlib, GitHub Pages

---

### 📡 5G-Scanner: Real-Time NR Signal Detection Platform
[![GitHub](https://img.shields.io/badge/GitHub-5G%20Research-blue?logo=github)](https://github.com/rockyco/5G-Scanner) | **Production-Ready** | **Live Deployment**

**Sophisticated 5G NR SSB Signal Detection and Analysis Platform**

Production-grade application for real-time detection and analysis of 5G New Radio Synchronization Signal Blocks using NI USRP X310, with proven real-world signal detection capabilities and comprehensive web-based monitoring.

**Real-World Performance:**
- **4 Active 5G Frequencies Detected** in band n78 (3.5 GHz) with live signal capture
- **GSCN 7951**: 303 SSB blocks detected at 3650.88 MHz
- **Multi-Band Support**: n1, n3, n77, n78, n79 bands with 3GPP TS 38.104 compliance
- **Custom FPGA Implementation**: 15.9MB optimized bitstream for X310 hardware

**Advanced Architecture:**
- **Modular Design**: 2,400+ lines across separated components for maintainability
- **Real-Time Web Interface**: Live progress monitoring with color-coded logging
- **Production Features**: SystemD service integration, comprehensive error handling
- **Data Persistence**: Historical scan results with JSON/CSV export capabilities

**Hardware Integration:**
- **Custom RFNoC Application**: Compiled executable for direct FPGA control
- **FPGA Resource Usage**: 59.91% LUT, 48.31% register utilization on Kintex-7
- **Process Management**: Advanced subprocess handling with timeout and cleanup
- **Thread-Safe Operations**: Concurrent scanning with robust resource management

**Proven Deployment:**
- **Active Data Collection**: Recent captures showing live 5G network detection
- **Enterprise Ready**: Service automation and production deployment capabilities
- **Research Utility**: Long-duration signal capture for detailed analysis
- **Web-Based Control**: User-friendly interface for monitoring and configuration

**Technologies:** Python Flask, NI USRP X310, Xilinx Vivado, RFNoC, SystemD, Custom FPGA, 5G NR

---

### 🏆 peakPicker - LLM-Aided FPGA Design Comparative Study
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/peakPicker) | ⭐ 8 stars | 🍴 3 forks

**A Comprehensive Comparative Study of LLM-Aided FPGA Design Flow**

A groundbreaking open-source project that bridges the gap between algorithm development and hardware design for 5G NR signal processing, featuring the first quantitative LLM-FPGA comparison study.

**Key Achievements:**
- **18x latency improvement** over original implementation
- **96% LUT reduction** (from 7,148 to 284 LUTs)  
- **2x latency improvement** over traditional MATLAB HDL Coder
- **400 MHz clock frequency** with minimal resource usage
- **60-70% time reduction** in optimization cycles

**Methodology & Innovation:**
- Systematic comparison of multiple design paths: MATLAB → HLS C++ (LLM-assisted) vs. MATLAB → Direct HDL
- Progressive optimization strategy with multiple LLM services (Claude 3.7 Sonnet, Gemini 2.5 Pro, GitHub Copilot)
- Structured LLM prompting methodology for FPGA design
- Complete open-source workflow from MATLAB to FPGA deployment

**Real-World Impact:**
*"This project showcases how Claude 3.7 Sonnet, Gemini 2.5 Pro, and GitHub Copilot can dramatically accelerate hardware design workflows while enhancing performance metrics."* - From LinkedIn project announcement

**Technologies:** MATLAB, HLS C++, Vitis HLS, HTML, AI-assisted design, AMD University Program support

---

### 🚀 pulseDetector - LLM-Aided Signal Processing
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/pulseDetector) | ⭐ 27 stars | 🍴 4 forks

**LLM-Aided FPGA Design for Signal Processing Applications**

Revolutionary approach demonstrating how Large Language Models can bridge the gap between algorithmic conception and hardware implementation, making advanced FPGA design more accessible to software engineers without sacrificing performance.

**Key Features:**
- Automated translation from MATLAB to optimized HLS C++
- Seamless integration of FIR IP cores within HLS designs  
- AI-guided design space exploration for optimal resource utilization
- Automated resource usage visualization with data visualization

**Performance Highlights:**
- **304 MHz** maximum operating frequency
- **194 DSP blocks** utilization  
- **Resource efficiency comparable to specialized HDL tools**
- Significant development time reduction while maintaining hardware efficiency

**Development Journey:**
*"This repository demonstrates how Large Language Models can revolutionize FPGA development workflows, specifically for DSP applications like pulse detection."* - From project announcement

**Connection to 5G Research:**
*"The key algorithmic computations for identifying 5G NR SSB signals - cross-correlation and frequency offset estimation - align perfectly with my pulseDetector project, creating an excellent opportunity to implement real-time 5G NR SSB detection on FPGA hardware."*

**Technologies:** MATLAB, HLS C++, Vitis HLS, Python, LLM integration, Cross-correlation algorithms

---

### 🔧 llm-fpga-design - Automated Design Flow
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/llm-fpga-design) | ⭐ 15 stars | 🍴 5 forks

**LLM-Aided FPGA Design and Debug Flow**

Innovative framework from University of Technology Sydney that leverages LLM AI-Agents to revolutionize FPGA design workflows, representing a significant step toward democratizing FPGA development through AI assistance.

**Revolutionary Features:**
- **Multi-Agent Architecture**: Specialized LLM agents for code generation, debugging, optimization, and documentation
- **Model Flexibility**: Compatible with OpenAI (GPT-4), Google (Gemini), and Anthropic (Claude) models  
- **Automated Workflow**: End-to-end orchestration from algorithm to synthesis and implementation
- **Interactive CLI**: User-friendly command interface for controlling the design process

**AI-Powered Capabilities:**
- **Automated Code Generation**: MATLAB algorithm descriptions directly to optimized HLS C++
- **Intelligent Debug Assistant**: AI-powered debugging with automated error analysis and correction
- **Performance Optimization**: Automatically apply performance optimizations
- **Documentation Generation**: Comprehensive auto-generated documentation

**Impact & Benefits:**
- **Dramatically reduces development time from weeks to hours**
- **60-70% development time reduction** with maintained high-quality implementations  
- Makes FPGA design more accessible to software engineers
- Enables rapid prototyping of complex signal processing algorithms
- Preserves design knowledge through comprehensive documentation

**Real-World Success:**
*"The integration of LLM APIs has elevated FPGA design productivity to new heights... reduces development time by 60%-70% while maintaining high-quality implementations."* - From development blog

**Case Study:** 5G NR Peak Picker implementation with full automation pipeline using **FREE** Gemini 2.5 Pro API

**Technologies:** MATLAB, HLS C++, Vitis HLS, Python, Multi-LLM APIs, Automated Testing

---

### 📊 ImageProcessing - LLM-Guided Sobel Filter Optimization
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/ImageProcessing) | ⭐ 14 stars | 🍴 2 forks

**Multi-Implementation Sobel Filter Study with LLM-Based Optimization**

Comprehensive exploration demonstrating dramatic memory and latency improvements through AI-guided design, featuring three HLS implementations from memory-intensive baseline to highly optimized version.

**Optimization Results:**
- **Memory-intensive baseline** → **Highly optimized version** guided by Gemini 2.0 Flash
- **Dramatic memory usage reduction** through systematic LLM optimization
- **Significant latency improvements** across multiple implementation versions
- **Comparative study methodology** for future LLM-FPGA projects

**LLM Integration:**
- **Gemini 2.0 Flash guidance** for advanced optimization strategies
- **Automated testbench generation** with 100% accuracy
- **HLS C++ module generation** from reference implementations

**Technologies:** C, FPGA, HLS, Image Processing Algorithms, Gemini 2.0 Flash

---

### 🎓 LabTraining - Educational Resources
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/LabTraining) | ⭐ 10 stars | 🍴 1 fork

**Digital System Design: Training Lessons and Exercise Projects**

Comprehensive educational materials for teaching digital system design and FPGA development to students.

**Educational Content:**
- Step-by-step training lessons
- Hands-on exercise projects
- Practical FPGA design examples
- Student-friendly documentation

**Technologies:** Verilog, Digital Design, FPGA, Educational Resources

---

### 📡 estFreqOffset - Carrier Frequency Estimation
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/estFreqOffset) | ⭐ 8 stars | 🍴 5 forks

**LLM-Assisted FPGA Design for Carrier Frequency Offset Estimation**

Revolutionary approach leveraging Large Language Models to automate conversion from MATLAB algorithms to hardware-ready HLS C++ code for wireless communications.

**Key Innovations:**
- **75% reduction in development time** compared to manual translation
- **Up to 90% resource savings** with optimized block RAM implementation
- **Comprehensive comparison** of flip-flop, LUT, and BRAM approaches
- **Systematic design space exploration** revealing unexpected optimization opportunities

**Real-World Connection:**
*"The key algorithmic computations for identifying 5G NR SSB signals - cross-correlation and frequency offset estimation - align perfectly with my estFreqOffset project."*

**Technologies:** C++, Signal Processing, FPGA, Wireless Communications, MATLAB, LLM Automation

---

## 🔬 Research & Proprietary Projects

### 🛰️ Hyperspectral Image Compression - CCSDS 123.0-B-1 Implementation

**LLM-Assisted Integration of HLS Modules for FPGA Acceleration**

Developed a modular FPGA implementation of the CCSDS 123.0-B-1 standard for space-based hyperspectral imaging applications, featuring unprecedented LLM-assisted system-level design.

**Technical Achievements:**
- **41.7% reduction in FPGA LUT usage** for Golomb-Rice coding
- **43.5% improvement in post-route timing performance**  
- **Perfect functional fidelity** with CCSDS standard
- **Five integrated modules**: Local Difference Calculation, Prediction, Mapping, Parameter Optimization, Coding

**LLM-Guided Innovations:**
- **Centralized Definition Architecture**: Standardized sharing across complex HLS modules
- **Stream-Based Pipeline Design**: High-throughput dataflow with balanced stages
- **Type-Safe Module Integration**: Adapter functions for error-free communication
- **Variable Shift Decomposition**: Novel switch-based approach replacing resource-intensive barrel shifters

**Space Technology Impact:**
- **Critical for space-grade FPGAs** with tight resource constraints
- **Radiation hardening requirements** addressed through lean, robust designs
- **Size, Weight, and Power (SWaP) constraints** optimized for onboard applications

### 🔄 Advanced Viterbi Decoder Implementation

**AI-Powered Algorithm-to-Hardware Transformation**

Complete MATLAB to FPGA automation achieving exceptional performance through systematic LLM-aided design methodology.

**Performance Highlights:**
- **352 Mbps data throughput** achieved
- **Ping-pong memory architecture** with dual 42-deep blocks
- **Power-of-2 optimization** for address control efficiency
- **Pure combinational logic** implementation reducing latency to 1 clock cycle

**Development Evolution:**
- **Branch Metric Calculation**: Handles punctured hard decision data
- **Traceback Module**: Automated sequence storage and reverse reading
- **LUT Usage**: Exceeding Xilinx paid IP core by ~1000 LUTs (acceptable trade-off)

**LLM Integration Insights:**
*"Using an LLM to convert MATLAB code to HLS C++ code is highly feasible. However, achieving high-performance hardware structures requires optimizing the MATLAB code based on deep understanding of algorithm principles."*

### 🌐 Multi-User MIMO-OFDM Transceiver

**Advanced Wireless Communication System with Jamming Suppression**

Comprehensive implementation leveraging AI-assisted programming for rapid RFSoC FPGA deployment.

**System Features:**
- **Multi-user MIMO-OFDM** wireless communication transceiver
- **Jamming suppression capabilities** for robust communication  
- **Modular design methodology** for parameterization
- **Automated optimization** of fixed-point bit widths and computational parallelism

**Technical Innovations:**
- **Data flow with feedback paths** in HLS without manual Verilog/VHDL
- **Single FFT IP core reuse** for both FFT and IFFT pipeline processing
- **RTL IP integration** as black box within HLS design
- **Pareto-optimal hardware structures** identification

**5G NR Algorithm Readiness:**
*"This clears the way to confidently use HLS C/C++ for implementing 5G NR algorithms on RFSoC systems."*



### 🎯 MATLAB HDL Coder Timing Optimization Framework

**Breaking the 250 MHz Barrier with LLM-Driven Solutions**

Groundbreaking methodology achieving unprecedented timing closure improvements through systematic LLM-guided HDL optimization.

**Breakthrough Results:**
- **93.6% frequency improvement** (126.61 MHz → 245.16 MHz)
- **98% timing slack recovery** (-3.898 ns → -0.079 ns)  
- **52.2% critical path reduction** (7.77 ns → 3.716 ns)
- **13.5% LUT efficiency improvement** (468 → 405 LUTs)
- **Strategic register doubling** (255 → 510 registers)

**LLM-Driven Methodology:**
- **Baseline Analysis**: Automated critical path identification via timing reports
- **Strategic Pipelining**: LLM-guided insertion using 'coder.hdl.pipeline'
- **Configuration Optimization**: Systematic HDL Coder settings exploration
- **Iterative Refinement**: AI-assisted validation of timing and functionality

**Future Vision:**
*"Imagine LLMs that can detect timing bottlenecks automatically, recommend optimal pipeline strategies, generate and fine-tune HDL configurations while ensuring both timing closure and functional correctness."*

### 🔄 Asynchronous Stream Processing Framework

**LLMs Supercharging MATLAB HDL Coder for Complex Data Flows**

Revolutionary approach solving real-world challenges where data rarely arrives in perfect synchronization, from 5G NR to radar applications.

**Technical Challenges Solved:**
- **Multiple asynchronous input streams** handling
- **Independent sample counters** tracking and synchronization
- **Minimum available sample count** synchronization eliminating data loss
- **Frame-based to stream-based** processing transformation

**LLM Enhancement Capabilities:**
- **Pattern Recognition**: Robust buffer architectures (dual circular buffers, power-of-2 sizing)
- **Synchronization Logic**: Automated code generation for stream alignment
- **Pipeline-Ready Design**: Sample-by-sample processing with fixed-point conversion
- **Testbench Automation**: Comprehensive validation including edge cases

**Performance Achievements:**
- **100% test success** rate achieved
- **250 MHz performance** reached without months of manual refactoring
- **Real-time single-cycle logic** implementation
- **Hardware-efficient, timing-closure-friendly** designs

**Industry Impact:**
*"You get the best of both worlds: MATLAB's rapid prototyping and HLS's streaming flexibility... 250 MHz performance are within reach without months of manual refactoring."*

### 🏭 Cross-Language Algorithm Translation Platform

**Java to FPGA Implementation Bridge**

Pioneering cross-domain algorithm translation demonstrating LLM capabilities in bridging diverse programming paradigms for hardware implementation.

**Translation Workflow:**
- **Java Algorithm Understanding**: Step-debugging for core logic comprehension
- **Testbench Generation**: Golden reference outputs from Java execution
- **LLM-Powered HLS Development**: Automated C/C++ module and testbench generation
- **Hardware Debugging**: AI co-pilot for optimization and verification

**Breakthrough Capabilities:**
- **Language-Agnostic Translation**: Hardware designers without deep source language expertise
- **Automated Verification**: Golden output comparison for functional correctness
- **Performance Optimization**: LLM-guided exploration beyond conventional thinking

**Democratization Impact:**
*"LLMs aren't just tools for software—they're becoming enablers for hardware designers, expanding access to algorithmic domains and accelerating co-design workflows. The potential to democratize algorithm–hardware co-design is immense."*

---

## 🌟 Real-World Applications & Deployments

### 🏗️ Complete 5G NR Development & Deployment Pipeline

**From MATLAB Algorithm to Live Hardware Deployment**

Successfully established the **full LLM-Assisted development pipeline** from high-level algorithm prototyping in MATLAB, through HLS-based FPGA acceleration, all the way to deployment on USRP hardware for real-time 5G NR applications.

**Automated Development Capabilities:**
- **Multiple SSB signal processing** from over-the-air cellular transmissions using Claude 3.7 Sonnet
- **Rich visualization creation** of detected SSB signals without manual coding
- **Interactive zoomed-in plots** of correlation peaks
- **Comprehensive MIB data tables** (Master Information Block)
- **Efficient peak detection algorithms** implementation

**Live Hardware Deployment:**
- **5G NR SSB Detection**: Real-time extraction from public 5G cell towers
- **RFNoC Integration**: Custom blocks embedded in NI RFNoC toolchain  
- **Live Hardware Validation**: Both simulation and live USRP deployments
- **High Accuracy**: Low SNR detection capabilities in real-time

**Development Impact:**
*"Without writing a single line of code manually, I was able to process multiple SSB signals... create rich visualizations... generate interactive plots... build comprehensive data tables."*

### 📡 5G NR Signal Sensing Testbed
Built comprehensive **2x2 MIMO 5G NR wireless communication system** using:
- **OAIBox MAX + USRP X310** as base station (gNB)
- **Quectel RM500Q-GL** as user device (UE)  
- **Channel State Information (CSI)** extraction for environmental sensing
- **Applications**: Accurate sensing of rainfall and water levels

### 🎯 Key Research Discoveries & Breakthroughs

#### MATLAB HDL Coder Timing Optimization Breakthrough
- **93.6% frequency improvement** (126.61 MHz → 245.16 MHz)
- **98% timing slack recovery** (-3.898 ns → -0.079 ns)
- **52.2% critical path reduction** (7.77 ns → 3.716 ns)
- **250 MHz operation** achieved for 5G NR signal processing on Xilinx Kintex-7

#### Space-Grade Algorithm Optimization Discovery
- **41.7% reduction in FPGA LUT usage** for CCSDS 123.0-B-1 Golomb-Rice coding
- **43.5% improvement in post-route timing performance**
- **Perfect functional fidelity** with CCSDS standard for space applications

#### Critical BRAM Mapping Finding
- **Research discovery**: FIFO size ≥16 entries prevents BRAM mapping for ENTIRE designs
- **42× resource reduction** achieved by optimizing FIFO constraints
- **Open-source contribution** with reproducible methodology published on GitHub

---

## Research Impact & Innovation

My open-source projects demonstrate the cutting-edge integration of **Artificial Intelligence** and **FPGA design**, contributing to:

- **Automated Hardware Design**: Pioneering the use of LLMs in FPGA development workflows
- **Performance Optimization**: Achieving breakthrough improvements in latency, resource utilization, and frequency
- **Educational Resources**: Providing comprehensive materials for digital system design education  
- **Reproducible Research**: Establishing methodologies for AI-assisted hardware design
- **Industry Standards**: Contributing to space-grade FPGA implementations and wireless communication systems
- **Real-Time Deployment**: Bridging simulation to hardware with validated USRP implementations

---

## 💡 Research Evolution & Development Journey

**From Algorithm to Hardware: The LLM Journey**

My research demonstrates a systematic evolution in LLM-aided hardware design:

**Phase 1: Proof of Concept (Dec 2024)**
*"I've been thinking for a long time about how to create an EDA tool that can automatically convert MATLAB code into HLS C++ code... using LLMs for this kind of conversion. To my surprise, the results were amazing."*

**Phase 2: Advanced Optimization (2025)**
- **One-Shot Translation**: Claude 3.7 Sonnet generating perfect, implementation-ready code on first attempt
- **Zero Iterations**: Complete MATLAB to HLS C++ conversion without corrections needed
- **Automated Testbench Generation**: 100% correct testbench code from Gemini 2.0 Flash

**Phase 3: Production Deployment**
- **Complete USRP Integration**: Full pipeline from MATLAB to live hardware deployment
- **Multi-Language Support**: Java to FPGA implementation bridges
- **Industrial Applications**: Space-grade algorithms and wireless communication systems

### 🔬 Technical Breakthroughs & Methodologies

#### LLM-Guided Design Principles
- **Frame-to-Stream Transformation**: Automating conversion from typical frame-based to sample-by-sample processing
- **Asynchronous Stream Handling**: LLMs solving complex multi-stream synchronization challenges  
- **Constraint-Driven Prompting**: Translating latency/throughput requirements into specific LLM constraints
- **Progressive Optimization**: Iterative refinement achieving 18x performance improvements

#### Real-World Validation Insights
*"LLM-assisted design is promising, but the key to success lies in deep hardware knowledge and hands-on debugging experience."*

- **LLM Limitations**: Cannot interpret simulation waveforms for timing/synchronization bugs
- **Human Expertise**: Hardware engineers remain indispensable for complex debugging
- **Hybrid Approach**: Combining AI automation with engineering expertise for optimal results

### 🌐 Cross-Domain Applications

#### Multi-Language Algorithm Translation
- **Java → HLS C++**: Hyperspectral image compression algorithms  
- **MATLAB → HDL**: 5G NR signal processing implementations
- **Viterbi Decoder**: Complete MATLAB to FPGA automation achieving 352 Mbps throughput

#### Industry Impact Areas
- **5G/6G Wireless Communications**: Real-time signal processing and detection
- **Space Technology**: CCSDS standard implementations for satellite applications
- **Computer Vision**: AMD Xilinx Kria KV260 accelerator implementations
- **Software Radio**: USRP and RFNoC framework integrations

---


## 📊 Repository Statistics

- **Total Stars**: 158+ across all repositories
- **Total Forks**: 31+ community contributions
- **Active Repositories**: 20 public projects
- **Primary Languages**: MATLAB, C++, Python, Verilog, VHDL
- **Last Updated**: December 22, 2025

## GitHub Profile

**Visit my complete GitHub profile**: [https://github.com/rockyco](https://github.com/rockyco)

**Total Public Repositories**: 20 active projects  
**Focus Areas**: LLM-Driven Hardware Design, FPGA Acceleration, 5G Signal Processing, Algorithm-to-Hardware Translation  
**Community Impact**: 158+ total stars, active collaboration and knowledge sharing  
**Development Timeline**: 3+ years of systematic LLM-FPGA research and deployment  
**Research Output**: Academic publications, production frameworks, and real-world USRP deployments