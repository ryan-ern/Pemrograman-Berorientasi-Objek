'''
Nama: Ryan Ernanda
NIM: 120140154
Kelas: RA
'''
# variable publik.
nama_bank = "Bank jagoan neon"
daftar_pelanggan = {} # Temp data pelanggan.

# Membuat class.
class AkunBank:
    # Konstruktor.
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.list_pelanggan = daftar_pelanggan
        self.list_pelanggan[self.__no_pelanggan] = self

    # Mengambil nama pelanggan.
    def get_nama(self):
        return self.__nama_pelanggan

    # Menampilkan nevigasi menu.
    def menu(self):
        # Info menu.
        print(f"\nSelamat datang di {nama_bank}")
        print(f"Halo {self.__nama_pelanggan}, ingin melakukan apa?")
        print("1) Lihat saldo")
        print("2) Tarik tunai")
        print("3) Transfer saldo")
        print("4) Keluar")

        # Navigasi menu.
        choice = int(input("Masukan nomor input: "))
        if choice == 1:
            self.__lihat_saldo()
        elif choice == 2:
            self.__tarik_tunai()
        elif choice == 3:
            self.__transfer()
        elif choice == 4:
            self.__keluar()
            return
        else:
            print('\nPilihan tidak tersedia!')
        
        # Rekursif
        self.menu()

    # Menarik isi saldo.
    def __tarik_tunai(self):
        # Input nominal penarikan.
        nominal_penarikan = int(input("\nMasukkan jumlah nominal yang ingin ditarik: "))
        # Validasi ketersediaan saldo.
        if nominal_penarikan > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
            self.__tarik_tunai()
            return
        
        # Proses penrurangan saldo.
        self.__jumlah_saldo -= nominal_penarikan
        print("Saldo berhasil ditarik!")

    # Melihat isi saldo.
    def __lihat_saldo(self):
        print(f"\n{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}")

    # Menerima pengiriman saldo saldo.
    def tambah_saldo(self, nominal):
        self.__jumlah_saldo += nominal

    # Melakukan transfer saldo.
    def __transfer(self):
        # Input dan validasi nominal.
        nominal = int(input("Masukkan nominal yang ingin ditransfer: "))
        if nominal > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
            self.__transfer()
            return

        # Input dan validasi nomor rekening tujuan.
        no_rek = int(input("Masukkan no rekening tujuan: "))
        daftar_no_rek = self.list_pelanggan.keys()
        if not no_rek in daftar_no_rek:
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama...")
            return

        # Transaksi.
        target = self.list_pelanggan[no_rek]
        self.__jumlah_saldo -= nominal
        target.tambah_saldo(nominal)
        print(f"Transfer Rp {nominal} ke {target.get_nama()} sukses!")
    

    # Keluar dari program.
    def __keluar(self):
        print("\nTerimakasih telah menggunakan layanan kami!\n")
        return True


# Inisialisai akun.
akun1 = AkunBank(1234, "Ryan Ernanda", 5000000000)
akun2 = AkunBank(2345, "Ukraina", 6666666666)
akun3 = AkunBank(3456, "Elon Musk", 9999999999)

# Simulasi transaksi pada setiap akun.
akun1.menu()
akun2.menu()
akun3.menu()