from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__ (self, warna, harga):
        self_warna = warna
        self_harga = harga

    def klakson(self):
        print("Tinnn!")

    @abstractmethod
    def maju(self):
        print("Maju")
    
    @abstractmethod
    def berhenti(self):
        print("Berhenti")

    @abstractmethod
    def ngebut(self):
        print("Ngebut")