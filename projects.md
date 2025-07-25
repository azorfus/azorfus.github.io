---
layout: default
title: Projects
permalink: /projects/
---

## [Tag](https://www.github.com/azorfus/Tag) (UnderDev) — 2025  
Tag is a statically-typed, imperative programming language implemented in Rust, featuring a custom lexer, parser, and AST generator. The project is designed for integration with LLVM for code generation and optimization. Tag supports modularity, control flow, and function definitions, and is structured for maintainability and extensibility. <br><br>

## [QTTP](https://www.github.com/azorfus/QTTP) (UnderDev) — 2025

QTTP is a clean-room, zero-dependency implementation of a full HTTP/3 client over QUIC, written entirely in C. It establishes a QUIC connection via raw UDP sockets, performs the full TLS 1.3 handshake (including AEAD encryption and key derivation), and communicates with real-world HTTP/3 servers like Google and Cloudflare — all without using any external libraries for networking, TLS, or HTTP. Every protocol layer — QUIC transport, TLS crypto, HTTP/3 framing, and stream multiplexing — is hand-rolled from the RFCs. QTTP is designed as a deep systems project to explore and expose the internals of modern internet protocols through raw, low-level control.<br><br>

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
