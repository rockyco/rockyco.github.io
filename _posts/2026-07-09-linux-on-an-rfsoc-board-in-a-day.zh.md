---
layout: post
title: "一天，把 Linux 跑上一块 RFSoC 板子"
date: 2026-07-09
lang: zh
translation_id: linux-on-an-rfsoc-board-in-a-day
reading_time: 7
excerpt: "一块试用板到手，上面没有操作系统。这回没有花一周慢慢调，而是让 AI 从头操盘，一天跑到登录提示符。靠的是把板子的每一层先验过再往上搭，遇到问题读机器的真实状态，而不是靠猜。"
---

一块试用板到了我桌上，上面没有操作系统。这是一块定制板，围绕两颗大芯片搭起来：一颗 Zynq
UltraScale+ RFSoC，把四核 Arm 处理器、可编程逻辑和射频放在一起；旁边一颗 Kintex UltraScale
FPGA，用来扩逻辑。硬件很能打，但一片空白。

给这种板子跑起一个能用的 Linux，正常是一个人一周的细活：先把板上每一块都验过，确认能信了，再
编内核、打包、烧卡，一点点把它哄过启动。这回我给方向，让 AI 去做具体的动手活。一天就收尾了：
控制台停在登录提示符，另一台机器 ssh 也能登进来。

<figure>
  <a class="zoom" href="{{ '/assets/blog/linux-on-an-rfsoc-board-in-a-day/zh/bench.jpg' | relative_url }}">
    <img src="{{ '/assets/blog/linux-on-an-rfsoc-board-in-a-day/zh/bench.jpg' | relative_url }}" alt="桌上接好线的 RFSoC 板子，后面的显示器上是 Linux 启动日志，停在登录提示符。">
  </a>
  <figcaption>一片空白的板子，如今跑着 Linux，停在登录提示符，一天点亮。</figcaption>
</figure>

## 不急着装 Linux

最顺手的做法是直奔终点，把 Linux 装上，坏哪修哪。可在一块不熟的板子上，这是最慢的路：一旦出
问题，你分不清是刚加的东西坏了，还是它底下的地基本来就没通。

所以 AI 没有从 Linux 开始。它一格一格往上爬，每爬一格，先留下一份日志和一组读数，再往上走。

<figure>
  <a class="zoom" href="{{ '/assets/blog/linux-on-an-rfsoc-board-in-a-day/zh/ladder.png' | relative_url }}">
    <img src="{{ '/assets/blog/linux-on-an-rfsoc-board-in-a-day/zh/ladder.png' | relative_url }}" alt="分级点亮的阶梯：JTAG、处理器内存、千兆以太网、启动模式、逻辑侧内存、两颗芯片之间的高速链路、射频前端，最后才是跑到登录提示符的 Linux。">
  </a>
  <figcaption>每一格都验过、留下证据，才开始下一格。Linux 是最后一格，不是第一格。</figcaption>
</figure>

它先连上 JTAG，确认能下载、能读回。它把 4 GB 处理器内存整个扫了一遍，零错误。它在千兆链路上
跑吞吐测试，测到接近线速的 948 Mbps。它验了板子的三种启动方式、FPGA 侧的内存、把两颗芯片连起
来的高速链路，还有射频前端。地基都通了，才把 Linux 搭上去。

## 把系统搭出来

地基稳了，搭 Linux 就是照流程走。从板子的硬件描述文件出发，把整套系统编出来，打包成一个启动
镜像、一个内核镜像，加一个根文件系统，写进 SD 卡。把板子拨到从卡启动，上电，盯着控制台。

<figure>
  <a class="zoom" href="{{ '/assets/blog/linux-on-an-rfsoc-board-in-a-day/zh/petalinux.png' | relative_url }}">
    <img src="{{ '/assets/blog/linux-on-an-rfsoc-board-in-a-day/zh/petalinux.png' | relative_url }}" alt="搭建流程：硬件描述文件，编译整套系统内核 6.6.40，打包镜像，写 SD 卡，启动到登录提示符。">
  </a>
  <figcaption>从一份硬件描述文件，到一张能启动的 SD 卡，用 PetaLinux 和内核 6.6.40 编出来。</figcaption>
</figure>

它起来了。内核拉起，启动日志一行行滚过，停在登录提示符。登录进去，把网卡起来，ssh 从房间那头
连了进来。一片空白的板子，成了一个能远程登录的仪器。

<figure>
  <a class="zoom" href="{{ '/assets/blog/linux-on-an-rfsoc-board-in-a-day/zh/bootlog.png' | relative_url }}">
    <img src="{{ '/assets/blog/linux-on-an-rfsoc-board-in-a-day/zh/bootlog.png' | relative_url }}" alt="控制台启动日志，各项服务依次就绪，最后停在板子的登录提示符。">
  </a>
  <figcaption>启动日志一路到登录提示符。到这里，ssh 就能进来了。</figcaption>
</figure>

## 值得多说一句的地方

有意思的不是一路顺的那部分，是路上的坑，以及 AI 是怎么过去的。

它一次都没靠猜。拨码开关到底选中了哪个启动模式，看不清的时候，它没有照着标签赌一把，而是去读
芯片里记录启动模式的那个寄存器，读出来是什么就认什么。第一次启动挂上了错误的根文件系统，悄悄
把真正的根盖住了，它顺着查出实际挂载的是哪一个，再从正确的地方重新挂。

一天能成，靠的就是这个习惯：读机器的真实状态，别去假设。文档和标签讲的是"应该是什么"，寄存器
告诉你的是"真的是什么"。

## 为什么这件事重要

这里每一步单拎出来都不难。真正拉开差距的是顺序和纪律：每一层先验过，再往上搭；每个问题都靠读
机器来定，而不是靠猜。这种耐心、可核对、说起来简单做起来枯燥的活，恰好适合交给一个会真的一步
一步做下去、还把证据摆出来的 AI。

我给计划，AI 去连板子、跑测试、读寄存器、编内核、烧卡、看启动日志、修坏掉的地方，再来一遍。一
片空白的板子到登录提示符，一天。

## 备注

- 硬件：一块定制板，把一颗 AMD Zynq UltraScale+ RFSoC（XCZU67DR）和一颗 AMD Kintex UltraScale
  FPGA（XCKU115）配在一起，用八条高速串行链路相连。RFSoC 上带八路接收、八路发射的射频通道。
- Linux 跑在 RFSoC 的四核 Arm 处理系统上，用 PetaLinux 2024.2 编出（内核 6.6.40）。
- 文中的数字，4 GB 处理器内存的零错误扫描、千兆链路实测 948 Mbps，都是点亮过程中在板子上读到
  的读数。
