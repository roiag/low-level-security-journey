import struct

def load_file(self):
    try:
        with open(self.path, 'rb') as f:
            self.data=f.read(64)
    except Exception as e:
            print(e)

def parse_header(self):
   values=struct.unpack('<16sHHIQQQIHHHHHH', self.data)
   self.e_ident=values[0]
   self.e_type=values[1]
   self.e_machine=values[2]
   self.e_version=values[3]
   self.e_entry=values[4]
   self.e_phoff=values[5]
   self.e_shoff=values[6]
   self.e_flags=values[7]
   self.e_ehsize=values[8]
   self.e_phentsize=values[9]
   self.e_phnum=values[10]
   self.e_shentsize=values[11]
   self.e_shnum=values[12]
   self.e_shstrndx=values[13]


def print_header_info(self):
    print("\n=== ELF Header Information ===")
    print(f"Type:           {self.e_type}")
    print(f"Machine:        {self.e_machine}")
    print(f"Version:        {self.e_version}")
    print(f"Entry point:    {hex(self.e_entry)}")
    print(f"Program header offset: {self.e_phoff}")
    print(f"Section header offset: {self.e_shoff}")
    print(f"Flags:          {self.e_flags}")
    print(f"ELF header size: {self.e_ehsize}")
    print(f"Program header entry size: {self.e_phentsize}")
    print(f"Number of program headers: {self.e_phnum}")
    print(f"Section header entry size: {self.e_shentsize}")
    print(f"Number of section headers: {self.e_shnum}")
    print(f"Section header string table index: {self.e_shstrndx}")

