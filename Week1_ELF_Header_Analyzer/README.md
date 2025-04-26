# Week 1: ELF Header Analyzer

This project provides a simple ELF Header Analyzer built in Python.

## Features
- Validates if a file is a valid ELF binary (checks magic bytes)
- Detects if the file is 32-bit or 64-bit
- Determines the file's endianness (Little Endian or Big Endian)
- Saves the first 64 bytes of the file to `header.bin`

## Usage
Run the script:

```bash
python3 elf_analyzer.py


When prompted, enter the path to an ELF file (for example, `/bin/ls`).

The script will:
- Validate if the file is a proper ELF binary
- Analyze and print the architecture and endianness
- Save the first 64 bytes of the file into a separate file called `header.bin`

## Requirements
- Python 3.x
- No external libraries are needed (uses only built-in modules)

## Notes
- If the file is not a valid ELF file, the script will print an error message.
- If any error occurs while reading or saving the file, an appropriate message will be shown.

