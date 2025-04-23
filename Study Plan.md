# 🐚 Low-Level Bug Bounty & Reversing – 6-Month Study Plan

Welcome to my low-level security journey! This repository documents my 6-month path to mastering reverse engineering, binary exploitation, and bug bounty hunting at the system level (non-web).

## 📌 Structure
Each week includes:
- 📘 Learning: recommended readings, videos, docs
- 🛠️ Practice: scripts, CTFs, reverse challenges
- 🧾 Writeup: summary in `Week-X/summary.md` with code and insights

---

## 📅 Month 1: Python for Low-Level Work
- **Week 1**: Binary Files – `open()`, `rb/wb`, hex/ASCII dump
- **Week 2**: `struct` module – packing/unpacking binary formats
- **Week 3**: `socket` – building TCP clients to send/receive binary data
- **Week 4**: `pwntools` – payload creation, `p32`, `cyclic`, GDB integration

## 🔐 Month 2: Crypto, Hashing & Digital Signatures
- **Week 5**: Hashing – `hashlib`, base64/hex encoding
- **Week 6**: AES Encryption – using `cryptography` library
- **Week 7**: Digital Signatures – RSA, ECDSA, signing/verifying files
- **Week 8**: Ghidra basics – reversing a password-check binary

## 📚 Month 3: Stack Overflow Exploitation
- **Week 9**: GDB intro – stack layout, memory view
- **Week 10**: Stack Overflow – Protostar Stack0–2
- **Week 11**: Shellcode injection – Protostar Stack3–5
- **Week 12**: ASLR + DEP – mitigation analysis

## 🔍 Month 4: Heap, Format Strings, Reversing Tools
- **Week 13**: Heap Overflow – Protostar Heap0–2
- **Week 14**: Format String Attacks – `%x`, `%n`, memory leak
- **Week 15**: IDA Free + AIDA – static reversing
- **Week 16**: Linux Privilege Escalation + Sysinternals (optional)

## 🧠 Month 5: Exploit Mitigations & Bypasses
- **Week 17**: Stack Canaries – detection and bypass
- **Week 18**: NX / DEP – ret2libc with `pwntools`
- **Week 19**: PIE + ASLR – leaking addresses and base calculation
- **Week 20**: Full Exploit Chain Practice

## 🚀 Month 6: Final Projects & Bug Bounty Entry
- **Week 21**: CrackMe + full writeup
- **Week 22**: Full exploit build using pwntools
- **Week 23**: GitHub portfolio – clean repo, structured docs
- **Week 24**: Submit to ZDI / HackerOne or apply to internships

---

> Follow my journey through the folders above. Every week includes code, notes, and real progress. Feel free to fork, learn, or contribute!
