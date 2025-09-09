---
layout: default
title: Projects
permalink: /projects/
---

## [Tag](https://www.github.com/azorfus/Tag) 2025  
Tag is a dead parser. <br><br>

## [QTTP](https://www.github.com/azorfus/QTTP) (UnderDev) — 2025

QTTP is a low-level QUIC and HTTP/3 client being developed in C, using raw Linux syscalls without reliance on external HTTP or socket libraries. It aims to implement full TLS 1.3 handshake support via picotls, and will manually construct and parse QUIC packets in accordance with RFC 9000, RFC 9001, and RFC 9114.

The project is intended for developers, researchers, and systems engineers who require precise control over protocol behavior and visibility into QUIC transport dynamics. It is being designed with a modular architecture to support experimentation, analysis, and diagnostic workflows.

Planned Features

Manual Frame Construction and Injection
The client will allow injection and mutation of individual QUIC frames (e.g., STREAM, PING) to test protocol edge cases, compliance, and fault tolerance.

Live Transport Metrics Collection
It will provide real-time visibility into transport metrics such as RTT, congestion window size, packet loss, and retransmissions.

TLS and QUIC Fingerprinting
The tool will support extraction of connection metadata including cipher suites, TLS extensions, ALPN negotiation, transport parameters, and connection ID formats for interoperability research.

Packet-level QUIC Proxy
A bidirectional UDP-based proxy is planned to enable passive forwarding and inspection of encrypted QUIC traffic, supporting debugging and testing scenarios.

Raw Syscall-Based UDP Stack
All networking operations will use sendmsg, recvmsg, and epoll, without external abstractions or high-level libraries.

Optional QLOG and Keylog Export
Support will be added to export session logs and TLS key material for use with external analysis tools like Wireshark and qvis.<br><br>

## RL-Sandbox  
A personal research environment for studying reinforcement learning.

RL-Sandbox includes hand-built RL engines and algorithm implementations in Python. It’s designed to support foundational learning and experimentation. The project includes:

- Custom RL engines (e.g., 15-puzzle, gridworld, gambler’s problem)
- Implementations of Value Iteration, Policy Iteration, Q-Learning, SARSA
- Instrumentation for step-by-step debugging and performance tracking
- Tools for visualizing agent behavior and learning progress

The project serves as a base for writing devlogs, studying algorithm behavior, and experimenting with variations of classic reinforcement problems.<br><br>


## Tetris OS (Queued) (2025)
A custom simple Tetris OS written in Zerl.<br><br>

---

<br>
# Miscellaneous. 

## Server - Client chat system (2023)
A simple server - client IRC chat system I wrote for my school project, It contains a very shaky file transfer feature which doesn't have much use :P.
[Repository.](https://github.com/azorfus/PyChatServer)

## StringLib (2021)
A simple string library with basic memory management written in C. You can find the code [here](https://github.com/azorfus/StringLib).

## LeD (2021)
A simple line editor inspired by edlin I wrote back in the day to understand string manipulation in C which led me to write the not very efficient [string library](https://github.com/azorfus/StringLib). You can find the code [here](https://github.com/azorfus/Led).
