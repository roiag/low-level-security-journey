# Week 2: ELF Header Parser

This project provides a simple ELF Header Parser built in Python using the `struct` module.

## Features
- Reads the first 64 bytes of an ELF binary.
- Parses the ELF header fields using `struct.unpack`.
- Extracts and displays important fields such as:
  - File type (`e_type`)
  - Machine architecture (`e_machine`)
  - Entry point address (`e_entry`)
  - Program and section header offsets
  - Number of program and section headers
- Prints all parsed information in a clean and organized format.

## Usage
Run the script:

```bash
python3 elf_parser.py
