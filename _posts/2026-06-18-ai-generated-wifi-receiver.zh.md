---
layout: post
title: "用 AI 自动生成一台 Wi-Fi 接收机，以及凭什么相信它"
date: 2026-06-18
lang: zh
translation_id: ai-generated-wifi-receiver
reading_time: 9
excerpt: "一整条 802.11a 接收链路，从 MATLAB 参考设计自动生成，没有人手写过一行硬件，却能把发来的图片一字节不差地收回来。真正有意思的不是 AI 写了代码，而是每一层都自己证明自己是对的。"
---

不久前我做了一件略微反常的事：一台完整的 Wi-Fi 接收机，硬件电路没有任何人手写过一行。AI 读懂了
MATLAB 的一套参考设计，把整条接收链路直接生成成数字电路。它跑在 ADALM-Pluto 上，一块 USB 供电、
FPGA 只有指甲盖大小的软件无线电。把 MATLAB 自己生成的标准 Wi-Fi 波形喂进去，它能把发送的图片逐字节
原样收回来。

最后这句话里藏着真正的问题。如果电路不是工程师写的，凭什么相信它是对的？一台"基本能用"的无线电毫无
价值，比特要么对、要么错。这篇文章讲的就是这个问题的答案：一种生成方法，让每一层都拿上一层来核对自己，
于是可信来自流程的结构，而不是来自谁的口头保证。

## 那套参考设计

MATLAB 自带一个参考例程，叫 *Image Transmission and Reception Using 802.11 Waveform and SDR*。
它是一条完整的 802.11a 链路：把一张图片切成数据包，调制成 Wi-Fi 波形发出去，接收端再同步、均衡、纠错，
直到把原图完整拼回来。

我一直想把这套接收机搬上 FPGA，好几年了。挡路的从来不是思路，而是工作量。对照 MATLAB 一行行翻成硬件
描述语言再去验证，繁琐到我总能给自己找到不动手的理由。于是这事一直搁着，直到我们的生成框架成熟到可以
换个办法：让 AI 从同一份参考出发，直接生成接收机。

几天之后，整条接收链路就以可综合硬件的形式存在了。

## 把硬件分层生成，逐层可核对

这套方法的全部价值，在于它不是生成一团看不透的代码，而是分三层生成，并且逐层机器核对。

<figure>
  <a class="zoom" href="{{ '/assets/blog/ai-wifi-receiver/zh/ai_pipeline.png' | relative_url }}">
    <img src="{{ '/assets/blog/ai-wifi-receiver/zh/ai_pipeline.png' | relative_url }}" alt="数学模型、周期级模型、RTL 三层生成与验证流程。">
  </a>
  <figcaption>每一层都由上一层生成，再自动与上一层核对。</figcaption>
</figure>

- 先生成**数学模型**：一份朴素的浮点参考。它的输出与 MATLAB 标准工具箱的波形完全吻合，等于把"什么叫对"
  这件事钉死。
- 再生成**周期级模型**：同一个算法，但换成芯片真正使用的低位宽定点，并补上逐拍的硬件时序。机器逐值核对它
  与数学模型一致。
- 最后生成**电路**，机器核对它与周期级模型零差异。

值得停下来强调一句：每相邻两层之间的一致，是机器自动核对的，不是人嘴上保证的。这里还有一个要老实交代的
细节：低位宽定点的芯片，本就不可能去比浮点的小数末位，那样比毫无意义。真正的考核更简单也更严格：喂进一个
标准信号，恢复出的每一个比特都必须正确。

## 接收机到底要做哪些事

送进接收机的并不是天线信号，而是已经被射频芯片数字化的一串基带采样。它要把这串采样解成干净的数据比特，
中间这条链路与 MATLAB 参考接收机一一对应。

<figure>
  <a class="zoom" href="{{ '/assets/blog/ai-wifi-receiver/zh/rx_architecture.png' | relative_url }}">
    <img src="{{ '/assets/blog/ai-wifi-receiver/zh/rx_architecture.png' | relative_url }}" alt="接收机框图：同步、FFT、均衡、Viterbi 译码。">
  </a>
  <figcaption>从找到数据包，到解出数据比特的完整链路。</figcaption>
</figure>

链路分四段：先锁定每个数据包的起点并校正频偏；去掉循环前缀，把每个符号变换成各个子载波；估计信道并均衡，
再把星座点解成每个比特的可信度；最后解交织、送进 Viterbi 译码器做最大似然纠错。整条链路自由流水，按固定
节拍接一个新采样，可以无限地跑下去。其中唯一快不起来的是 Viterbi 译码器，因为它是一个反馈环，所以被放进
一个独立的慢时钟域，再安全地把数据交给前面的电路。

## 一张图片，发出去再收回来

参考设计的压轴演示，是把一整张图片传过去。我保留了它那张经典测试图，只换掉一样东西：接收端现在是自动生成
的硬件。

<figure>
  <a class="zoom" href="{{ '/assets/blog/ai-wifi-receiver/zh/image_flow.png' | relative_url }}">
    <img src="{{ '/assets/blog/ai-wifi-receiver/zh/image_flow.png' | relative_url }}" alt="端到端图片链路：分包、调制、信道、接收、重组。">
  </a>
  <figcaption>图片被切成数据包、调制、穿过带噪信道，再由恢复出的比特重新拼起。</figcaption>
</figure>

在干净信道下，收回的图片与原图逐字节一致。为了让系统在受压时也表现得诚实，我故意把其中一个数据包的信号
电平压得很低。这一包的校验没通过、被丢弃，恢复出的图上于是留下一条灰带，其余部分照常恢复。这正是参考设计
演示的丢包行为，只不过这次跑在一台没人手写过的电路上。

<figure>
  <a class="zoom" href="{{ '/assets/blog/ai-wifi-receiver/zh/image_recovery.png' | relative_url }}">
    <img src="{{ '/assets/blog/ai-wifi-receiver/zh/image_recovery.png' | relative_url }}" alt="原图与恢复图逐字节一致，仅丢失一个数据包。">
  </a>
  <figcaption>发送与恢复对照。唯一那条灰带，是我故意饿掉信号的那一包。</figcaption>
</figure>

## 拿独立的标准来对照

演示很有说服力，但最硬的核对要用一个外部权威。在无线通信里，这个权威就是 MATLAB 的 WLAN 工具箱，它直接
实现了 802.11 标准。对照分两层，而且关键在于把两层分开。

<figure>
  <a class="zoom" href="{{ '/assets/blog/ai-wifi-receiver/zh/xval_flow.png' | relative_url }}">
    <img src="{{ '/assets/blog/ai-wifi-receiver/zh/xval_flow.png' | relative_url }}" alt="两层对照：算法层对标准，硬件层对 MATLAB 发出的信号。">
  </a>
  <figcaption>算法层对照标准；硬件层对照一个独立工具发出的信号。</figcaption>
</figure>

**算法层**，是把生成的浮点参考与标准工具箱的波形逐个采样去比，两者完全吻合，说明这份参考模型就是标准本身。
**硬件层**，则让 MATLAB 当发射方：它生成标准波形，按真实接收机会看到的方式量化，再灌进定点电路。结果是
一个比特都不差。这一步最有说服力，恰恰因为发射方是一个完全独立、严格符合标准的工具，不是我写的。

## 信号本身长什么样

也值得看看信号本身。下面这些都不是示意图，而是把真实波形跑过定点接收链路测出来的。

<figure>
  <a class="zoom" href="{{ '/assets/blog/ai-wifi-receiver/zh/spectrum.png' | relative_url }}">
    <img src="{{ '/assets/blog/ai-wifi-receiver/zh/spectrum.png' | relative_url }}" alt="发射 OFDM 频谱，中间是标准要求的直流置零。">
  </a>
  <figcaption>发射频谱，端坐在信道里，中间那个小凹口是标准规定的直流置零。</figcaption>
</figure>

星座图展示了接收机在各种调制下的表现：从能扛住最弱信号的稳健方式，到每个符号塞最多比特、对信道最挑剔的
密集方式。

<figure>
  <a class="zoom" href="{{ '/assets/blog/ai-wifi-receiver/zh/constellations.png' | relative_url }}">
    <img src="{{ '/assets/blog/ai-wifi-receiver/zh/constellations.png' | relative_url }}" alt="四种调制的接收星座图。">
  </a>
  <figcaption>恢复出的星座图。越密的星座装的比特越多，但需要越强的信号。</figcaption>
</figure>

把信号质量系统地扫一遍，就画出那条熟悉的误码率曲线：稳健的调制在很低的信号电平下就清零，密集的则要高得多。
两者一起，给出这台接收机能可靠工作的真实边界。

<figure>
  <a class="zoom" href="{{ '/assets/blog/ai-wifi-receiver/zh/ber_waterfall.png' | relative_url }}">
    <img src="{{ '/assets/blog/ai-wifi-receiver/zh/ber_waterfall.png' | relative_url }}" alt="四种调制的误码率随信号质量变化曲线。">
  </a>
  <figcaption>误码率随信号质量变化，就是接收机真实的工作边界。</figcaption>
</figure>

标准里的每一种调制编码组合都能一路解到数据比特、逐字节正确，包括恶劣的多径信道，而这一切都跑在一块单手就能
握住的开发板上。

## 为什么这件事可以复用

我做的是一台 Wi-Fi 接收机，但整个方法里没有一处是 Wi-Fi 专属的。从数学定义，到带时序的定点模型，再到生成
的电路，每一层都与上一层可证等价，而且这个等价由机器核对，不是人嘴上保证。这台接收机恰好由十个这样的模块
组成，每个都被独立验证。

真正可复用的，不是这一台无线电，而是它底下那条纪律：一种让每一层都清楚知道自己该和谁对照的生成方式。当年
我躲了好几年没动手的手写移植，AI 几天就做完了，而 MATLAB 发来的信号被一个比特不差地收了回来。值得留下的，
是这一部分。
