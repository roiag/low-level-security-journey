# Week 3: Binary Socket Communication

This project demonstrates basic binary communication between a client and a server using TCP sockets in Python.

## Features
- A simple TCP server (`server.py`) that listens for incoming connections.
- A client (`client.py`) that sends a binary command using `struct.pack`.
- Support for two operations:
  - Opcode 1: Multiply the given value by 3
  - Opcode 2: Add the value to itself
- The server parses the received binary data using `struct.unpack` and processes it accordingly.
- Basic error handling for invalid opcodes and connection issues.

## Usage

### Start the server
```bash
python3 server.py
