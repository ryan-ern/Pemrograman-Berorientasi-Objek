import string
# Nama: Ryan Ernanda
# NIM: 120140154
# Kelas: PBO RA

# Membuat kelas VigenereCipher.
class VigenereCipher():
    # Konstruktor.
    def __init__(self):
        self.__key = input("Masukkan kunci (key): ").upper()
        self.__alpha = string.ascii_uppercase # dari import string, ascii [A-Z]
       

    # Menampilkan menu.
    def menu(self):
        print("\nVigenere cipher")
        print("1) Enkripsi plainteks")
        print("2) Dekripsi cipher")
        print("3) Ganti kunci (key)")
        print("4) Keluar program")

        # Menu.
        Pilihan = int(input("Masukan nomor input: "))
        if Pilihan == 1:
            self.encrypt()
        elif Pilihan == 2:
            self.decrypt()
        elif Pilihan == 3:
            self.update_key()
        elif Pilihan == 4:
            exit()
        else:
            print('\nPilihan tidak tersedia!')
        
        # Rekur
        self.menu()

    # Enkripsi string.
    def encrypt(self):
        # Input plain teks.
        plain_txt = input("\nMasukkan plainteks: ").upper()#mengubah semua karakter huruf kecil menjadi huruf besar

        # Jumlah Alphabet
        apbt = 26

        # Generate plain key.
        key_u = 0
        plain_key = ""
        for i in range(len(plain_txt)):
            karakter = plain_txt[i]
            if karakter != " ":
                plain_key += self.__key[key_u]
                key_u += 1
                if key_u >= len(self.__key):
                    key_u = 0
            else:
                plain_key += " "

        # Proses enkripsi text.
        encrypted = ""
        for i in range(len(plain_txt)):
            karakter_txt = plain_txt[i]
            karakter_key = plain_key[i]
            if karakter_txt != " ":
                idx_1 = self.__alpha.index(karakter_txt)
                idx_2 = self.__alpha.index(karakter_key)
                idx_hsl = (idx_1 + idx_2) % apbt
                karakter_hsl = self.__alpha[idx_hsl]
                encrypted += karakter_hsl
            else:
                encrypted += " "
        
        # Menampilkan hasil enkripsi.
        print("Hasil enkripsi: {}".format(encrypted))
                
    # Dekripsi string.
    def decrypt(self):
         # Input cipher teks.
        cipher_txt = input("\nMasukkan cipher: ").upper()
        
        # Jumlah Alphabet
        apbt = 26

        # Generate cipher key.
        cipher_key = ""
        key_u = 0
        for i in range(len(cipher_txt)):
            karakter = cipher_txt[i]
            if karakter != " ":
                cipher_key += self.__key[key_u]
                key_u += 1
                if key_u >= len(self.__key):
                    key_u = 0
            else:
                cipher_key += " "

        # Proses enkripsi text.
        decrypted = ""
        for i in range(len(cipher_txt)):
            karakter_txt = cipher_txt[i]
            karakter_key = cipher_key[i]
            if karakter_txt != " ":
                idx_1 = self.__alpha.index(karakter_txt)
                idx_2 = self.__alpha.index(karakter_key)
                idx_hsl = (idx_1 - idx_2) % apbt
                karakter_hsl = self.__alpha[idx_hsl]
                decrypted += karakter_hsl
            else:
                decrypted += " "
        
        # Menampilkan hasil enkripsi.
        print("Hasil dekripsi: {}".format(decrypted))

    # Update kunci (key).
    def update_key(self):
        key=self.__key
        key_n = input("\nUpdate kunci (key): ").upper()
        if key_n!=key:
            print("Kunci Berhasil Diubah!")
            key=key_n
        else:
            print("Kunci Masih Sama!")
        

# Inisialisasi kelas dan menjalankan objek.
VC = VigenereCipher() # Inisialisasi.
VC.menu() # Menampilkan daftar menu.