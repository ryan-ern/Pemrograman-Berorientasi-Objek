# metaclass
class MultiBases(type):
	# overriding __new__ method
	def __new__(cls, clsname, bases, clsdict):
		# jika tidak ada kelas dasar yang lebih besar dari 1
		# raise error
		if len(bases)>1:
			raise TypeError("Mewarisi beberapa kelas dasar!")
		
		# metode __new__ dari kelas super.
		# Panggil __init__ dari tipe kelas
		return super().__new__(cls, clsname, bases, clsdict)

# metaclass dapat ditentukan dengan argumen kata kunci 'metaclass'
# sekarang kelas MultiBase digunakan untuk membuat kelas
# base ini disebar ke semua subclass dari Base
class Base(metaclass=MultiBases):
	pass
# bukan raise error
class A(Base):
	pass
# bukan raise error
class B(Base):
	pass
# ini raise error!
class C(A, B):
	pass
