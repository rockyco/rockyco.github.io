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

### 🚀 MATLAB2HLS: Self-Learning Algorithm-to-Hardware Framework v13.0
[![GitHub](https://img.shields.io/badge/GitHub-Production%20Framework-blue?logo=github)](https://github.com/rockyco/MATLAB2HLS) | **Self-Learning System** | **24+ Case Studies**

**Hierarchical LLM-Driven Framework for Automated MATLAB-to-FPGA Transformation**

A self-learning system that bridges the semantic gap between high-level MATLAB algorithms and optimized FPGA implementations. The hierarchical approach prevents LLM hallucinations through structured multi-stage transformation with validation gates at each phase.

**Core Architecture:**
- **7-Phase Pipeline**: Decomposition → Test Generation → Flatten → Optimize → HLS Generation → HLS Optimization → Integration
- **8 Specialized Agents**: Each phase managed by domain-specific LLM agents with defined inputs/outputs
- **Self-Learning Engine**: Continuously improves success rate (70% → 95%+) through pattern accumulation
- **Multi-Target Output**: Xilinx FPGA, Intel FPGA, ASIC via Verilog/VHDL

**Performance Results:**
- **157× error reduction** on complex algorithms (72.17% → 0.00%)
- **97.3% latency reduction** with streaming architecture optimization
- **360 MHz timing closure** exceeding 300 MHz targets
- **99.54% functional accuracy** verified through RTL co-simulation

**Case Studies (24+ Examples):**
- **Harris Corner Detection**: Zero-error implementation, <1% FPGA utilization
- **5G NR SSB Detection**: 5-module system at 292 MHz, 279 DSPs
- **Lagged Product**: 100% MATLAB equivalence, 360 MHz operation
- **WLAN Synchronization**: Filter detection, CFO estimation modules
- **ISAC Systems**: FFT implementations, adaptive subspace algorithms

**Key Innovations:**
- **Horizontal Decomposition**: Breaks complex algorithms into modular blocks
- **Vertical Refinement**: MATLAB → optimized MATLAB → HLS C++ → RTL
- **Stream-based Adaptation**: Batch processing to streaming architecture
- **Blocking Validation Gates**: 5 phase-aligned hooks ensure quality

**Technologies:** MATLAB, Vitis HLS 2024.2, Verilog/VHDL, Python, Multi-Agent Architecture, Xilinx UltraScale+

---

### 📡 RX_AP_UE: High-Performance 8×8 MIMO-OFDM Wireless Receiver
**Production-Ready** | **200 MHz** | **1.5 Gbps Throughput**

**FPGA-Based MIMO-OFDM Receiver for Access Point and User Equipment Applications**

A complete wireless communication receiver implementation supporting 8×8 MIMO-OFDM with advanced signal processing including Cholesky-based equalization, carrier frequency offset compensation, and multi-stage channel estimation optimized for Xilinx Vitis HLS.

**Signal Processing Pipeline:**
```
RF Input → CFO Compensation → FFT → Channel Estimation → Cholesky Decomposition → Two-Stage Equalization → Payload Recovery
```

**Core Modules:**
- **applyCFO**: CORDIC-based carrier frequency offset compensation
- **runFFT**: OFDM demodulation via streaming FFT
- **calcMatrixH**: 8×8 MIMO channel estimation using LTS
- **runCholesky**: Matrix factorization for optimal equalization
- **equalFirstStage/equalSecondStage**: Two-stage MMSE equalization
- **recoverPayLoad**: Multi-modulation support (QPSK, QAM16, QAM64, QAM256)

**Performance Metrics:**
- **Clock Frequency**: 200 MHz (5ns period)
- **Throughput**: 1.5 Gbps in 8×8 MIMO configuration
- **Latency**: ~800-1000 cycles total pipeline
- **Resources**: 987 DSPs, 234 BRAMs, 67K LUTs, 89K FFs

**Development Evolution:**
- **21 integration versions** showing progressive optimization
- **39% DSP utilization** with efficient Cholesky implementation
- **Co-simulation verified** against MATLAB golden reference

**Technologies:** Vitis HLS, Vitis Solver Library, MIMO-OFDM, Cholesky Decomposition, AXI-Stream, Zynq UltraScale+

---

### 🐍 Python2HLS: Python-to-Hardware Transformation Framework
**Sub-Agent Architecture** | **IP Library Integration** | **345 MHz Achieved**

**Automated Python Algorithm Transformation to Hardware-Efficient HLS C++**

Building on MATLAB2HLS architecture, this framework transforms Python algorithmic code (NumPy/SciPy) into optimized HLS implementations with automatic IP library detection and integration for maximum performance.

**Core Architecture:**
- **6 Specialized Agents**: Workflow Coordinator, Python Analysis, Implementation, Synthesis, Optimization, Failure Resolution
- **6 Quality Gates**: Python Validation → Architectural Feasibility → Functional Validation → Synthesis → Co-simulation → Implementation
- **IP Library Integration**: Automatic detection and utilization of optimized IP cores

**IP Library Performance:**
| Algorithm | Manual | With IP Library | Improvement |
|-----------|--------|-----------------|-------------|
| FIR Filter | 8200+ cycles | 1067 cycles | 87% faster |
| FFT | Variable | Fixed II=1 | 60-80% faster |
| Matrix Mult | O(n³) | Systolic | 40-70% faster |

**Python-Specific Features:**
- **NumPy Pattern Recognition**: `np.convolve()` → FIR IP, `np.fft.fft()` → FFT IP
- **Automatic Type Inference**: Float operations → optimal fixed-point
- **Generator Support**: Python generators map directly to HLS streams
- **SciPy Acceleration**: `scipy.signal.lfilter()` → IIR Filter IP

**Performance Results:**
- **345 MHz achieved** (72% above 200 MHz target)
- **87% latency reduction** through IP library utilization
- **25-50% resource savings** vs naive implementation
- **<15 minutes** total transformation time

**Technologies:** Python, NumPy, SciPy, Vitis HLS, IP Libraries (FIR, FFT, Matrix), Multi-Agent System

---

### 🔧 CPP2FPGA: C++ to FPGA Transformation Framework
**6-Phase Pipeline** | **JPEG-LS Demonstration** | **8-Gate Compliance**

**Systematic Transformation of Algorithmic C++ to Synthesizable HLS Code**

A comprehensive framework for converting standard C++ algorithms into hardware-efficient HLS implementations, demonstrated with JPEG-LS image compression (ITU-T T.87 standard).

**6-Phase Transformation Pipeline:**
```
Phase 1: Algorithm Analysis    → Identify HLS incompatibilities, propose modules
Phase 2: Code Restructuring    → Transform to modular HLS-compatible C++
Phase 3: Test Generation       → Create per-module test vectors with golden refs
Phase 4: HLS Transformation    → Convert to synthesizable HLS with pragmas
Phase 5: HLS Optimization      → Optimize latency, resources, timing
Phase 6: HLS Integration       → Integrate modules into complete system
```

**JPEG-LS Encoder Modules:**
- **module1_line_buffer**: Streaming line buffer management
- **module2_context_selector**: Context ID selection for prediction
- **module3_predictor**: MED (Median Edge Detection) prediction
- **module4_error_mapper**: Prediction error mapping
- **module5_context_modeler**: Adaptive context modeling
- **module6_golomb_encoder**: Golomb-Rice entropy coding

**8-Gate HLS Compliance System:**
| Gate | Requirement |
|------|-------------|
| G1 | Algorithmic computation (no hardcoded results) |
| G2 | Accuracy < 1e-05 vs golden reference |
| G3 | Single main processing loop |
| G4 | Fixed loop bounds (compile-time constants) |
| G5 | Fixed-size arrays only |
| G6 | Sequential access pattern preferred |
| G7 | Single input element per iteration |
| G8 | ≤2 BRAM accesses per cycle |

**Key Features:**
- **Per-module validation**: Independent testing before integration
- **Universal Makefile**: Standardized build system for all modules
- **Phase validation hooks**: Automated quality checks at each stage

**Technologies:** C++17, Vitis HLS 2024.2, JPEG-LS (ITU-T T.87), Multi-Agent Architecture, Zynq UltraScale+

---

### 📊 PAM4Receiver: AI-Driven Communication System Implementation
[![GitHub](https://img.shields.io/badge/GitHub-Communication%20Systems-blue?logo=github)](https://github.com/rockyco/PAM4Receiver) | **4 Stars** | **AI-Driven HDL**

**Advanced PAM4 Receiver Implementation with AI-Driven HDL Code Generation**

Sophisticated communication system implementation demonstrating AI-assisted development for high-speed digital communication, featuring comprehensive PAM4 signal processing with automated HDL generation and optimization.

**Technical Achievements:**
- **PAM4 Signal Processing**: Complete receiver implementation for high-speed communication
- **AI-Driven HDL Generation**: Automated code generation with optimization strategies
- **Communication System Design**: End-to-end signal processing pipeline
- **Performance Optimization**: Systematic approach to timing and resource optimization

**Advanced Features:**
- **Multi-Level Signaling**: PAM4 modulation scheme for increased data rates
- **Automated Code Generation**: AI-assisted HDL development workflow
- **System-Level Design**: Complete receiver architecture implementation
- **Verification Framework**: Comprehensive testing and validation methodology

**Technologies:** MATLAB, HDL Code Generation, PAM4 Modulation, Communication Systems, AI-Assisted Design

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
[![GitHub](https://img.shields.io/badge/GitHub-Computer%20Vision-blue?logo=github)](https://github.com/rockyco/HarrisCorner) | **8 Stars** | **Zero-Error Implementation** | **366.7 MHz Performance**

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
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/peakPicker) | ⭐ 8 Stars | 🍴 3 Forks

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
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/pulseDetector) | ⭐ 29 Stars | 🍴 4 Forks

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
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/llm-fpga-design) | ⭐ 17 Stars | 🍴 5 Forks

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
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/ImageProcessing) | ⭐ 14 Stars | 🍴 2 Forks

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
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/LabTraining) | ⭐ 10 Stars | 🍴 1 Fork

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
[![GitHub](https://img.shields.io/badge/GitHub-View%20Repository-blue?logo=github)](https://github.com/rockyco/estFreqOffset) | ⭐ 10 Stars | 🍴 5 Forks

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

### 🛰️ HSI_Compressor: CCSDS 123.0-B-1 Hyperspectral Image Compression

**LLM-Assisted Multi-Module HLS Integration for Space Applications**

A complete FPGA implementation of the CCSDS 123.0-B-1 lossless compression standard for hyperspectral imaging, demonstrating LLM-assisted integration of 6 specialized HLS modules into a cohesive dataflow pipeline.

**System Architecture (6 Integrated Modules):**
- **convertDataOrder**: Input data rearrangement for efficient processing
- **calcLocalDifference**: Local difference computation between neighboring pixels
- **calcPredictedSample**: Sample prediction based on spatial neighbors
- **calcMappedResidual**: Prediction residual mapping to positive integers
- **calcParameterKt**: Dynamic Golomb-Rice coding parameter optimization
- **codeMappedResidual**: Entropy coding for final compression output

**Technical Achievements:**
- **41.7% LUT reduction** for Golomb-Rice coding module
- **43.5% timing improvement** in post-route performance
- **Perfect CCSDS compliance** with standard reference validation
- **Stream-based dataflow** with `hls::stream` interfaces throughout

**LLM-Guided Integration Innovations:**
- **Centralized Definition Management**: `common_defs.hpp` for standardized dimensions/types
- **Type Adapter Functions**: Bridging different data types across module interfaces
- **Dataflow Pipeline Architecture**: Concurrent module execution with `#pragma HLS DATAFLOW`
- **Interface Standardization**: Consistent streaming patterns across all modules

**Integration Challenges Solved:**
- **Macro Redefinition Conflicts**: Unified dimension definitions across modules
- **Type Compatibility**: Automatic adapters between `data_t`, `datamv_t`, `mapVal_t`
- **Pipeline Synchronization**: Balanced stream depths for throughput optimization

**Technologies:** Vitis HLS, CCSDS 123.0-B-1, Stream-based Dataflow, Hyperspectral Imaging, Space-grade FPGA

### 📻 Multi-User Massive MIMO for Tactical Networks

**FPGA Implementation of Robust Interference Mitigation for Contested Environments**

Research implementation of multi-user massive MIMO technologies for wireless tactical ad-hoc networks operating in contested environments with jamming signals, featuring complete FPGA signal processing chain.

**Core Innovations:**
- **Time-Domain Spatial Filtering (TDSF)**: Novel approach to suppress broadband jamming before FFT
- **Frequency-Domain MMSE Equalization**: Decision feedback for narrowband interference mitigation
- **Complete FPGA Architecture**: Signal acquisition, synchronization, FFT, channel estimation, Cholesky decomposition

**Signal Processing Pipeline:**
- **Signal Acquisition**: Packet detection and timing synchronization
- **FFT Processing**: OFDM demodulation with frequency-domain output
- **Channel Estimation**: Pilot-based MIMO channel matrix estimation
- **Cholesky Decomposition**: Efficient matrix factorization for equalization
- **Forward/Backward Substitution**: Linear system solving for signal recovery

**System Capabilities:**
- **MIMO-OFDM with SDMA**: Spatial Division Multiple Access for multi-user support
- **Anti-Jamming**: Robust operation under intentional interference
- **Field-Validated**: Prototype tested in real tactical network scenarios

**Technologies:** Massive MIMO, OFDM, MMSE Equalization, Cholesky Decomposition, Anti-Jamming, FPGA Implementation

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

- **Total Stars**: 163+ across all repositories
- **Total Forks**: 31+ community contributions
- **Active Repositories**: 20 public projects
- **Primary Languages**: C++, MATLAB, Python, Verilog, VHDL
- **Last Updated**: January 12, 2026

## GitHub Profile

**Visit my complete GitHub profile**: [https://github.com/rockyco](https://github.com/rockyco)

**Total Public Repositories**: 35+ active projects
**Focus Areas**: LLM-Driven Hardware Design, FPGA Acceleration, 5G/MIMO Signal Processing, Algorithm-to-Hardware Translation
**Framework Portfolio**: MATLAB2HLS, Python2HLS, CPP2FPGA - Complete algorithm transformation ecosystem
**Development Timeline**: 3+ years of systematic LLM-FPGA research and deployment
**Research Output**: Academic publications, production frameworks, and real-world USRP/MIMO deployments
