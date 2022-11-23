class RakBuku:
    def __init__(self):
        self.size = 5
        self.data = [None] * self.size

    def getHash(self,key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum % self.size

    def probing(self,key):
        for index in range(self.size):
            probeHash = self.linearProbing(key, index)
            if (self.data[probeHash] is None) or (self.data[probeHash] == 'deleted'):
                return probeHash

    def linearProbing(self,jenisBuku,namaBuku):
        return (self.getHash(jenisBuku)+namaBuku) % self.size

    def tambahBuku(self, key, value):
        key_hash = self.getHash(key)
        key_value = [key, value]

        if self.data[key_hash] is None:
            self.data[key_hash] = list([key_value])
            return True
        else:
            key_hash = self.probing(key)
            if key_hash is None:
                print("Rak Buku anda sudah penuh")
                return False
            else:
                self.data[key_hash] = list([key_value])
                return True

    def lihatBuku(self, jenisBuku):
        key_hash = self.getHash(jenisBuku)
        if (self.data[key_hash] is not None) and (self.data[key_hash] != 'deleted'):
            for index in range(self.size):
                key_hash = self.linearProbing(jenisBuku, index)
                if(self.data[key_hash][0][0] == jenisBuku):
                    return self.data[key_hash][0][1]

        print("Key ", jenisBuku, " tidak ditemukan")
        return "None"  

    def ambilBuku(self, jenisBuku):
        key_hash = self.getHash(jenisBuku)
        if self.data[key_hash] is None:
            return False
        for index in range(self.size):
            key_hash = self.linearProbing(jenisBuku, index)
            if(self.data[key_hash][0][0] == jenisBuku):
                print("deleting ", jenisBuku)
                self.data[key_hash] = "deleted"
                return True

        print("Key ", jenisBuku, " tidak ditemukan")
        return False

    def printAll(self):
        print('='*20,'List Buku', '='*20)
        for data in self.data:
            if data is not None and data != 'deleted':
                print(f"Nama : {data[0][1]} <> Jenis : {data[0][0]}")
        print('='*51)

if __name__ == "__main__":
 rak1 = RakBuku()
 rak1.tambahBuku("History", "Mein Kampf (B01)")
 rak1.tambahBuku("Fantasy", "The Witcher (B02)")
 rak1.tambahBuku("Mystery", "Exile (B03)")
 rak1.tambahBuku("Sci Fi", "The Martian (B04)")
 rak1.tambahBuku("History", "World War (B05)")
 rak1.tambahBuku("Romance", "Twilight (B06)")
 
#  rak1.printAll()
 
 print(rak1.lihatBuku("History"))
 print(rak1.lihatBuku("Romance"))
 
 rak1.ambilBuku("Sci Fi")
 rak1.ambilBuku("Romance")

 rak1.printAll()
