import struct

class ELFHeaderAnalyzer:
    def __init__(self, path):
        self.path = path
        self.data = None
        self.bits = None
        self.endian = None

    def load_file(self):
        try:
            with open(self.path, "rb") as f:
                self.data = f.read(64)
        except Exception as e:
            print(f"An exception occurred while loading the file: {e}")

    def validate_elf(self):
        if self.data[:4] == b'\x7fELF':
            self.analyze_header()
        else:
            print("Invalid ELF file.")

    def analyze_header(self):
        self.bits = "32-bit" if self.data[4] == 1 else "64-bit"
        self.endian = "Little Endian" if self.data[5] == 1 else "Big Endian"

    def save_header(self):
        try:
            with open("header.bin", "wb") as f:
                f.write(self.data)
        except Exception as e:
            print(f"An exception occurred while saving the header: {e}")

    def display_info(self):
        print("\nELF File Analysis:")
        print(f"Architecture: {self.bits}")
        print(f"Endianness: {self.endian}")

def main():
    path = input("Enter the path to the ELF file: ").strip()
    analyzer = ELFHeaderAnalyzer(path)
    analyzer.load_file()
    analyzer.validate_elf()
    analyzer.display_info()
    analyzer.save_header()

if __name__ == "__main__":
    main()
