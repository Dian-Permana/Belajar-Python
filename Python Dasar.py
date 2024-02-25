# ☆☆☆ Alur dan Cara Kerja Python ☆☆☆
import time
start_time = time.time()

print("Hello")
print("World")
print("Hello World")

print("Hello Chikal")
# ini adalah comment
a = 10 # ini adalah comment juga
"""ini adalah comment multi line
karena bisa membuat comment dalam baris yang banyak"""
print(a)
print(time.time() - start_time, "detik")
# kita bisa mengcompile python ke yang namanya bytecode
""" cara mengcompile, buka terminal dan tuliskan python -m py_compile Main.py """

# ☆☆☆ Variabel ☆☆☆
# Variabel adalah tempat menyimpan data

# Menaruh / menyimpan data
a = 10
x = 5
panjang = 1000

# Pemanggilan pertama
print("Nilai a = ", a)
print("Nilai x = ", x)
print("Nilai panjang = ", panjang)

# Penamaan Variabel
nilai_y = 15 # dengan menggunakan underscore
juta10 = 1000000000 # ini boleh
nilaiZ = 17.5 # ini boleh
# Menggunakan - tidak boleh
# Menggunakan angka didepan string tidak boleh

# Pemanggilan kedua
print("Nilai a = ", a)
a = 7
print("Nilai a = ", a)

# Assignment Indirect
b = a 
print("Nilai b = ", b)

# ☆☆☆ Tipe Data ☆☆☆
# a = 10, a adalah variabel dengan nilai 10

# Tipe data : Angka satuan yang gak ada komanya (integer)
data_integer = 1
print("data : ", data_integer)
print("- bertipe : ", type(data_integer))

# Tipe data : Angka dengan koma (float)
data_float = 1.5
print("data : ", data_float)
print("- bertipe : ", type(data_float))

# Tipe data : Kumpulan karakter (string)
data_string = "Ucup"
print("data : ", data_string)
print("- bertipe : ", type(data_string))

# Tipe data : Biner True / False (Boolean)
data_bool = True
print("data : ", data_bool)
print("- bertipe : ", type(data_bool))

## Tipe Data Khusus

# Bilangan Kompleks
data_complex = complex(5,6)
print("data : ", data_complex)
print("- bertipe : ", type(data_complex))

# Kita bisa menggunakan Tipe Data dari Bahasa C 
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double)
print("- bertipe : ", type(data_c_double))

# ☆☆☆ Casting Tipe Data ☆☆☆
# Kita belajar Casting Tipe Data
# Merubah dari suatu tipe data ke tipe lain
# Tipe Data = int, float, str, bool

## INTEGER
print("====INTEGER====")
data_int = 9
print("data = ", data_int, ",type =", type(data_int))

data_float = float(data_int) # akan menjadi bilangan koma, nilai 9 menjadi 9.0
data_str = str(data_int) # akan berubah menjadi string
data_bool = bool(data_int) # akan false jika nilai int = 0
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))

## FLOAT
print("====FLOAT====")
data_float = 9.5
print("data = ", data_float, ",type =", type(data_float))

data_int = int(data_float) # akan dibulatkan kebawah, walaupun nilai 9.9 menjadi 9
data_str = str(data_float) # akan berubah menjadi string
data_bool = bool(data_float) # akan false jika nilai float = 0
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))

## BOOLEAN
print("====BOOLEAN====")
data_bool = True
print("data = ", data_bool, ",type =", type(data_bool))

data_int = int(data_bool) # True = 1 False = 0
data_float = float(data_bool) #True= 1.0 False= 0.0
data_str = str(data_bool) # akan berubah menjadi string
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_str, ",type =", type(data_str))

## STRING
print("====STRING====")
data_str = "Ucup"
print("data = ", data_str, ",type =", type(data_str))

data_int = int(data_str) # string harus angka
data_float = float(data_str) # string harus angka
data_bool = bool(data_str) # akan false jika nilai string kosong
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_bool, ",type =", type(data_bool))

# ☆☆☆ Input dari User ☆☆☆
# Episode Input User

# Data yang dimasukkan pasti string
data = input("Masukkan data: ")
print("data = ",data,",type=",type(data))

# Jika kita ingin mengambil int atau float, maka 
angka = int(input("Masukkan angka: "))
angka = float(input("Masukkan angka: "))
print("data = ",angka,",type=",type(angka))

#Bagaimana dengan Boolean ???
biner = bool(int(input("Masukkan nilai boolean: ")))
print("data = ",biner,",type =",type(biner))

# ☆☆☆ Operasi Aritmatika ☆☆☆
# Operasi Aritmatika

a = 10
b = 3

# Operasi penjumlahan +
hasil = a + b
print(a,"+",b,"=",hasil)

# Operasi pengurangan -
hasil = a - b
print(a,"-",b,"=",hasil)

# Operasi perkalian *
hasil = a * b
print(a,"*",b,"=",hasil)

# Operasi pembagian /
hasil = a / b
print(a,"/",b,"=",hasil)

# Operasi eksponen (pangkat) **
hasil = a ** b
print(a,"**",b,"=",hasil)

# Operasi modulus (sisa pembagian) %
hasil = a % b
print(a,"%",b,"=",hasil)

# Operasi floor division (dibulatkan kebawah) //
hasil = a // b
print(a,"//",b,"=",hasil)

# Prioritas operasi (Operational presedence)
""" 1. Tanda kurung ( )
    2. Eksponen **
    3. Perkalian dan teman-teman * / % //
    4. Penjumlahan dan Pengurangan + - """

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x 
print(x,"**",y,"*",z,"+",x,"/",y,"-",y,"%",z,"//",x,"=",hasil)

hasil = x + y * z
print(x,"+",y,"*",z,"=",hasil)
hasil = (x + y) * z
print("(",x,"+",y,") *",z,"=",hasil)


# ☆☆☆ Latihan Program Perhitungan Sederhana ☆☆☆
# Latihan Konversi Satuan Temperature

# Program Konversi Celsius ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATURE\n")

celcius = float(input("Masukkan suhu dalam celcius:"))
print("suhu adalah",celcius,"°Celcius")

# Reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur,"°Reamur")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah",fahrenheit,"°Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah",kelvin,"°Kelvin")

# Program Konversi Reamur ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATURE\n")

reamur = float(input("Masukkan suhu dalam reamur:"))
print("suhu adalah",reamur,"°Reamur")

# Celcius
celcius = (5/4) * reamur
print("suhu dalam celcius adalah",celcius,"°Celcius")

# Fahrenheit
fahrenheit = ((9/4) * reamur) + 32
print("suhu dalam fahrenheit adalah",fahrenheit,"°Fahrenheit")

# Kelvin
kelvin = ((5/4) * reamur) + 273
print("suhu dalam kelvin adalah",kelvin,"°Kelvin")

# Program Konversi Fahrenheit ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATURE\n")

fahrenheit = float(input("Masukkan suhu dalam fahrenheit:"))
print("suhu adalah",fahrenheit,"°Fahrenheit")

# Reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah",reamur,"°Reamur")

# Celcius
celcius= ((5/9) * (fahrenheit - 32))
print("suhu dalam celcius adalah",celcius,"°Celcius")

# Kelvin
kelvin = ((5/9) * (fahrenheit - 32)) + 273
print("suhu dalam kelvin adalah",kelvin,"°Kelvin")

# Program Konversi Kelvin ke satuan lain
print("\nPROGRAM KONVERSI TEMPERATURE\n")

kelvin = float(input("Masukkan suhu dalam kelvin:"))
print("suhu adalah",kelvin,"°Kelvin")

# Reamur
reamur = ((4/5) * (kelvin - 273))
print("suhu dalam reamur adalah",reamur,"°Reamur")

# Fahrenheit
fahrenheit = ((9/5) * (kelvin - 273)) + 32
print("suhu dalam fahrenheit adalah",fahrenheit,"°Fahrenheit")

# Celcius
celcius = kelvin - 273
print("suhu dalam celcius adalah",celcius,"°Celcius")

# ☆☆☆ Operasi Komparasi ☆☆☆
# Operasi Komparasi

# Setiap hasil dari operasi komparasi adalah boolean (True / False)

# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2
# Lebih besar dari (>)
print("==== Lebih besar dari (>) ====")
hasil = a > 3
print(a,">",3,"=",hasil)
hasil = b > 3
print(b,">",3,"=",hasil)
hasil = b > 2
print(b,">",2,"=",hasil)

# Lebih kecil dari (<)
print("==== Lebih kecil dari (<) ====")
hasil = a < 3
print(a,"<",3,"=",hasil)
hasil = b < 3
print(b,"<",3,"=",hasil)
hasil = b < 2
print(b,"<",2,"=",hasil)

# Lebih besar dari sama dengan (>=)
print("==== Lebih besar dari sama dengan (>=) ====")
hasil = a >= 3
print(a,">=",3,"=",hasil)
hasil = b >= 3
print(b,">=",3,"=",hasil)
hasil = b >= 2
print(b,">=",2,"=",hasil)

# Lebih kecil dari sama dengan (<=)
print("==== Lebih kecil dari sama dengan (<=) ====")
hasil = a <= 3
print(a,"<=",3,"=",hasil)
hasil = b <= 3
print(b,"<=",3,"=",hasil)
hasil = b <= 2
print(b,"<=",2,"=",hasil)

# Sama dengan (==)
print("==== Sama dengan (==) ====")
hasil = a == 4
print(a,"==",4,"=",hasil)
hasil = b == 4
print(b,"==",4,"=",hasil)

# Tidak sama dengan (!=)
print("==== Tidak sama dengan (!=) ====")
hasil = a != 4
print(a,"!=",4,"=",hasil)
hasil = b != 4
print(b,"!=",4,"=",hasil)

"""
Note : Komparasi >,<,>=,<=,==,!= semuanya dapat bekerja pada syntax literal.
Contoh : a == 4
Penjelasan : 
a -> ada nilainya -> memakan memory
4 -> literal karena gak ada variable, tidak memakan memory

"is" membandingkan komparasi antara nilai yang memakan memory / object

Contoh syntax salah : a is 4 (SALAH)
Contoh syntax benar : a = 4
                      b = 4
                      a is b (BENAR)
"""
# "is" sebagai komparasi object identity
print("==== Object identity is ====")
x = 5 # ini adalah assignment membuat object
y = 5
print("nilai x =",x,"id =",hex(id(x)))
print("nilai y =",y,"id =",hex(id(y)))
hasil = x is y
print("x is y =",hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print("nilai x =",x,"id =",hex(id(x)))
print("nilai y =",y,"id =",hex(id(y)))
hasil = x is y
print("x is y =",hasil)

# "is not" sebagai komparasi object identity
print("==== Object identity is not ====")
x = 5 # ini adalah assignment membuat object
y = 5
print("nilai x =",x,"id =",hex(id(x)))
print("nilai y =",y,"id =",hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print("nilai x =",x,"id =",hex(id(x)))
print("nilai y =",y,"id =",hex(id(y)))
hasil = x is not y
print("x is not y =",hasil)

# ☆☆☆ Operasi Logika atau Boolean ☆☆☆
# Operasi Logika atau Boolean

# not, or, and, xor

# NOT
print ("===== NOT =====")
a = True
c = not a 
print("a = True" )
print("c = not a")
print("data a =",a)
print("-------NOT")
print("data c =",c)

# OR (Jika salah satu True, maka hasilnya adalah True)
print ("===== OR =====")
a = False
b = False
c = a or b
print(a,"OR",b,"=",c)
a = False
b = True
c = a or b
print(a,"OR",b,"=",c)
a = True
b = False
c = a or b
print(a," OR",b,"=",c)
a = True
b = True
c = a or b
print(a," OR",b,"=",c)

# AND (Jika dua buah nilai adalah True, maka hasilnya True)
print ("===== AND =====")
a = False
b = False
c = a and b
print(a,"AND",b,"=",c)
a = False
b = True
c = a and b
print(a,"AND",b,"=",c)
a = True
b = False
c = a and b
print(a," AND",b,"=",c)
a = True
b = True
c = a and b
print(a," AND",b,"=",c)

# XOR (Jika salah satu True, maka hasilnya adalah True, sisanya False)
print ("===== XOR =====")
a = False
b = False
c = a ^ b
print(a,"XOR",b,"=",c)
a = False
b = True
c = a ^ b
print(a,"XOR",b,"=",c)
a = True
b = False
c = a ^ b
print(a," XOR",b,"=",c)
a = True
b = True
c = a ^ b
print(a," XOR",b,"=",c)

# ☆☆☆ Latihan Komparasi dan Logika ☆☆☆
# Latihan Komparasi dan Logika

# Membuat gabungan area rentang dari angka

# ++++++2---------10++++++
inputUser = float(input("Masukkan angka yang bernilai kurang dari 3 atau lebih besar dari 10:"))

# ++++++2------
# Memeriksa angka kurang dari 3------
isKurangDari = inputUser < 3
print("Kurang dari 3 =",isKurangDari)


# Memeriksa angka lebih dari 10++++++
isLebihDari = inputUser > 10
print("Lebih dari 10 =",isLebihDari)

isCorrect = isKurangDari or isLebihDari
print("Angka kurang dari 3 atau lebih dari 10 =",isCorrect)

# ------3+++++++++10------ (Kasus Irisan)
inputUser = float(input("Masukkan angka yang bernilai lebih besar sama dengan 3 atau lebih kecil sama dengan 10:"))

# ------3++++++
# Memeriksa angka lebih dari sama dengan 3++++
isLebihDariSamaDengan = inputUser >= 3
print("Lebih dari sama dengan 3 =",isLebihDariSamaDengan)

# Memeriksa angka lebih dari 10------
isKurangDariSamaDengan = inputUser <= 10
print("Lebih kecil sama dengan 10 =",isKurangDariSamaDengan)

isCorrect = isLebihDariSamaDengan or isKurangDariSamaDengan
print("Angka lebih dari sama dengan 3 dan kurang dari sama dengan 10 =",isCorrect)

# PR Latihan Komparasi dan Logika
# 1. -----0+++++5-----8+++++11-----
inputUser = float(input("Masukkan angka yang memenuhi persyaratan berikut.\nAngka > 0 < 5 atau > 8 < 11:"))

#Memeriksa angka hasil Input User
Logika_1 = (inputUser > 0) and (inputUser < 5)
Logika_2 = (inputUser > 8) and (inputUser < 11)
print("Angka > 0 dan < 5 =",Logika_1)
print("Angka > 8 dan < 11 =",Logika_2)
isCorrect = Logika_1 or Logika_2
print("Angka yang Anda masukkan =", isCorrect)

# 2. +++++0-----5+++++8-----11+++++
inputUser = float(input("Masukkan angka yang memenuhi persyaratan berikut.\nAngka < 0 > 5 dan < 8 > 11:"))

#Memeriksa angka hasil Input User
Logika_1 = (inputUser < 0) or ((inputUser > 5 and inputUser < 8))
Logika_2 = ((inputUser > 5) and (inputUser < 8)) or (inputUser > 11)
print("Angka < 0 dan > 5 =",Logika_1)
print("Angka < 8 dan > 11 =",Logika_2)
isCorrect = Logika_1 and Logika_2
print("Angka yang Anda masukkan =", isCorrect)

# Operator Bitwise, operasi biner (binary)
# Bitwise = Operasi masing-masing bit

a = 9
b = 5

# Bitwise OR ( | )
print("==== OR ====")
c = a | b 

print("Nilai a =",a)
print("Nilai b =",b)
print("Nilai",a,", binary :",format(a,"08b"))
print("Nilai",b,", binary :",format(b,"08b"))
print("=========================== (|)","Bitwise OR")
print("Nilai",c,", binary :",format(c,"08b"))


# Bitwise AND ( & )
print("==== AND ====")
c = a & b 

print("Nilai a =",a)
print("Nilai b =",b)
print("Nilai",a,", binary :",format(a,"08b"))
print("Nilai",b,", binary :",format(b,"08b"))
print("=========================== (&)","Bitwise AND")
print("Nilai",c,", binary :",format(c,"08b"))


# Bitwise XOR ( ^ )
print("==== XOR ====")
c = a ^ b 

print("Nilai a =",a)
print("Nilai b =",b)
print("Nilai",a,", binary :",format(a,"08b"))
print("Nilai",b,", binary :",format(b,"08b"))
print("=========================== (^)","Bitwise XOR")
print("Nilai",c,", binary :",format(c,"08b"))

# Bitwise NOT (~)
print("==== NOT ====")
c = ~a
print("Nilai",a,", binary :",format(a,"08b"))
print("=========================== (~)","Bitwise NOT")
print("Nilai",c,", binary :",format(b,"08b"))
print("=========================== (^)","Bitwise XOR")
d = 0b0000001001
e = 0b1111111111
print("Nilai :",e^d,", binary",format(e^d,"08b"))

# Shifting (Shift register)
print("==== Shift Right ====")
# Shift right (>>)
c = a >> 2
print("=========================== (>>)","Bitwise Shift Right")# Bitwise Shift Right ( >> )
print("Nilai",a,", binary :",format(a,"08b"))
print("=========================== (>>)","Bitwise Shift Right 2x")# Bitwise Shift Right ( >> )
print("Nilai",c,", binary :",format(c,"08b"))

print("==== Shift Left ====")
# Shift left (<<)
c = a << 2
print("=========================== (<<)","Bitwise Shift Left")# Bitwise Shift Left ( << )
print("Nilai",a,", binary :",format(a,"08b"))
print("=========================== (<<)","Bitwise Shift Left 2x")# Bitwise Shift Leftt ( << )
print("Nilai",c,", binary :",format(c,"08b"))

# Operasi yang dapat dilakukan dengan penyingkatan
# Operasi ditambah dengan assignment

a = 5 # ini adalah assignment
print("Nilai a adalah =",a)

a += 1 # Artinya adalah a = a + 1
print("Nilai a += 1, nilai a menjadi",a)

a -= 2 # Artinya adalah a = a - 2
print("Nilai a -= 2, nilai a menjadi",a)

a *= 5 # Artinya adalah a = a * 5
print("Nilai a *= 5, nilai a menjadi",a)

a /= 2 # Artinya adalah a = a / 2
print("Nilai a /= 2, nilai a menjadi",a)

# Modulus
b = 10
print("\nNilai b =",b)

b %= 3 # Artinya adalah b = b % 3
print("Nilai b %= 3, nilai b menjadi",b)

# Floor Division
b = 10
print("\nNilai b =",b)

b //= 3 # Artinya adalah b = b // 3
print("Nilai b //= 3, nilai b menjadi",b)

# Pangkat / Eksponen
a = 5
print("Nilai a =",a)
a **= 3 # Artinya adalah a = a ** 3
print("Nilai a **= 3, nilai a menjadi",a)

# Operasi Bitwise
# OR
c = True
print("\nNilai c =",c)
c |= False # Artinya adalah c = c OR False
print("Nilai c |= False, nilai c menjadi",c)
c = False
print("\nNilai c =",c)
c |= False # Artinya adalah c = c OR False
print("Nilai c |= False, nilai c menjadi",c)

# AND
c = True
print("\nNilai c =",c)
c &= False # Artinya adalah c = c AND False
print("Nilai c &= False, nilai c menjadi",c)
c = True
print("\nNilai c =",c)
c &= True # Artinya adalah c = c AND True
print("Nilai c &= True, nilai c menjadi",c)

# XOR
c = True
print("\nNilai c =",c)
c ^= False # Artinya adalah c = c XOR False
print("Nilai c ^= False, nilai c menjadi",c)
c = True
print("\nNilai c =",c)
c ^= True # Artinya adalah c = c XOR True
print("Nilai c ^= True, nilai c menjadi",c)

# Shift Register
# Shift Right (Menggeser bit ke kanan)
d = 0b0100
print("\nNilai d =",format(d,"04b"))
d >>= 2 # Artinya adalah d = shift right 2x ke kanan
print("Nilai d >>= 2, nilai d menjadi",format(d,"04b"))

# Shift Left
d <<= 1 # Artinya adalah d = shift left 1x ke kiri
print("Nilai d <<= 1, nilai d menjadi",format(d,"04b"))

# ☆☆☆ Pengenalan String ☆☆☆
data = "ini adalah string"
print(data)
print(type(data))

# 1.Cara Membuat String
'''
# 1. Dengan menggunakan single quote '...'
  2. Dengan menggunakan double quote "..."
'''

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Hallo, apa kabar?"')
print("'Hallo, apa kabar?'")
print("Ini adalah hari Jum'at")

'''
# 2.Menggunakan tanda \
# Membuat tanda ' menjadi string
'''
print('Mari kita shalat Jum\'at')
print('g\'day, isn\'t it?')

'# Backlash (Agar tanda backlash bisa di print maka diketik 2x)'
print("C:\\User\\ChikaL")

'# Tab'
print("Anna Elsa,berdekatan")
print("Anna\tElsa,agak jauhan")
print("Anna\t\t\tElsa,semakin jauhan")

'# Backspace'
print("Ucup \bOtong")
print("Ucup  \bOtong")

'# Newline'
print("baris pertama.\nbaris kedua.") # LF -> Line Feed -> Unix, Linux, Max Os
print("baris pertama.\rbaris kedua.") # CR -> Carriage Return -> Commodore, Acorn, Lisp
print("baris pertama.\r\nbaris kedua.") # Dipakai oleh Windows

'''
# 3. String Literal / raw_input
'''

# Hati-hati
print("C:\new folder") #  akan salah path nya

# Menggunakan raw string 
print(r"C:\new folder")
'''Note : Jika menggunakan format raw string , maka semua karakter yang ditulis akan dianggap string semua '''
# Perhatikan contoh dibawah ini :
print(r"C:User\New Folder\n \b\r\File Baru")
# Karakter akan di print semua

# Multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# Multiline literal string dan raw
print(r"""
Nama : Ucup
Kelas : 3 SD\NEW NORMAL
Website : www.ucup.com/newID
""")

# Operasi dan Manipulasi String

# 1.Menyambung string (concatenate)
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

print("\n")

# 2.Menghitung panjang string (len)
panjang = len(nama_lengkap)
print("panjang dari "+ nama_lengkap + " = " + str(panjang))

print("\n")

# 3.Operator untuk string
""" Mengecek apakah ada komponen char atau string di string
"""

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "D"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

print("\n")

# Mengulang string
print("wk"*10)
print(15*"wk")

print("\n")

# Indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-6 : " + nama_lengkap[6])
print("index ke- (-1) : " + nama_lengkap[-1])
print("index ke- (-2) : " + nama_lengkap[-2])
print("index ke- [0:3] : " + nama_lengkap[0:4])
print("index ke- [3:7] : " + nama_lengkap[3:8])
print("index ke- [0,2,4,6,8,10] : " + nama_lengkap[0:11:2])

print("\n")

# Item paling kecil
print("paling kecil :" + min(nama_lengkap))
print("paling besar :" + max(nama_lengkap))

print("\n")

# ASCII CODE
ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

print("\n")

# Operator dalam method
data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah o pada " + data + " = ",str(jumlah))

print("\n")
# Cara membalikkan urutan dalam string
#Perhatikan contoh berikut :
# Syntax nya = nama_variabel_data[-1: : -1] # (index start,stop,step)
data = "Purwakarta"
data_terbalik = data[-1: :-1] #(start,stop,step)
print(f"data awal = {data}")
print(f"data setelah direverse = {data_terbalik}")

# Operator dalam bentuk methods

## Merubah case dari string

# Merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam.upper())

# Merubah semua ke lower case
alay = "aKu KeCe AbieezZZZzzZZZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## Pengecekan dengan isX methods

# Contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower()
print(salam + " is lower = "+ str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = "+ str(apakah_upper))

# isalpha() --> untuk mengecek semuanya huruf
# isalnum() --> huruf dan angka
# isdecimal () --> angka saja
# isspace() --> spasi, tab, newline \n
# istitle() --> semua kata dimulai dengan huruf besar

judul = "It Is Okay Not To Be Okay"
cek_judul = judul.istitle() # hasil bool
print(judul + " is title = " + str(cek_judul))

## Mengecek komponen startswith() endswitch() --> keren

cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppa".endswith("Oppa")
print("end = " + str(cek_end))

## Penggabungan komponen join() split()
pisah = ["aku","sayang","kamu"]
gabung = ",".join(pisah)
print(gabung)

gabungan = " ".join(pisah)
print(gabungan)

gabungan = " ehm ".join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split("ehm"))

# Alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(10)
print("'"+tengah+"'")

aneh = "aneh".center(20,"=")
print("'"+aneh+"'")

# Kebalikannya --> strip()
aneh = aneh.strip("=") # menghilangkan tanda =
print("'"+aneh+"'")

print("manual")
print(5*"=" + "data" + "="*5)

# Format string

# Contoh generic
# String
nama = "Ucup"
format_str = f"hello {nama}"
print(format_str)

# Boolean
boolean = True
format_str = f"boolean = {boolean}"
print(format_str)

# Angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# Bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# Bilangan dengan ordo ribuan
angka = 2000
format_str = f"jutaan = {angka:,}"
print(format_str)

# Bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print(format_str)

# Menampilkan leading zero
angka = 2005.54321
format_str = f"jutaan = {angka:09.3f}"
print(format_str)

# Menampilkan tanda + atau -
angka_minus = -10
angka_plus = +10
format_minus = f"minus = {angka_minus}"
format_plus = f"plus = {angka_plus}"
print(format_minus)
print(format_plus)

# Memformat Persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# Melakukan Operasi Matematika di dalam Placeholder
harga = 10000
jumlah = 5 
format_str = f"harga total = Rp. {harga*jumlah:,}"
print(format_str)

# Format Angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hexadecimal= f"hexadecimal = {hex(angka)}"
print("Angka = ",angka)
print("Format",format_binary)
print("Format",format_octal)
print("Format",format_hexadecimal)

# Width and Multiline

# Data
data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 165.1
data_nomor_sepatu = 41

# String standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggu = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# Mengatur lebar
data_nama = "Ucup"
data_string = f"""
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggu = {data_tinggi:>5}
sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# Date and Time (Latihan)

import datetime as dt
print("Silahkan masukkan tanggal,\nbulan dan tahun lahir Anda")
tanggal = int(input("Tanggal \t:"))
bulan = int(input("Bulan \t\t:"))
tahun = int(input("Tahun \t\t:"))
hari_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir Anda adalah :{hari_lahir}")
print(f"Hari lahir Anda adalah :{hari_lahir:%A}")

hari_ini = dt.date.today()
print(f"Hari ini tanggal: {hari_ini}")
umur_hari = hari_ini - hari_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30
print(f"Umur Anda adalah: {umur_hari}")
print(f"Umur Anda adalah: {umur_tahun} tahun, {umur_bulan_sisa} bulan")

# If dan Else Statement

# 1. if nya
# 2. kondisinya
# 3. aksinya

nama = input("Siapa nama Anda? ")

# program sebelumnya
# if kondisi: aksi
# program selanjutnya

# 1.Program if inline
if nama == "Ucup" : print("Kamu ganteng AbiezzZZZ!!!!!!")
print(f"Terima kasih {nama}")

# 2.Program if indentation
if nama == "Ucup":
        print("Kamu ganteng abiezzz")
        print("Kamu juga keren banget")
print(f"Terima kasih {nama}")

# 3.Else Statement
if nama == "Otong":
         print("Hai Otong, si Kereeen....!!!")
else:
         print("Ah kamu bukan Otong, kamu gak keren! :(")
print("Akhir dari program")

#Elif = Else If Statement

nama = input("Nama Anda siapa? ")

"""
# Rumusnya seperti dibawah ini
if kondisi:
    aksi True
elif kondisi:
    aksi True
else
    aksi False
"""

if nama == "Ucup": #Kondisi 1
   print("Hai ganteng beuds...!!") #Aksi True 1
elif nama == "Otong": #Kondisi 2
   print("Hai si kece bangets!!!") #Aksi True 2
elif nama == "Mario": #Kondisi 3
   print("Hai Humoris!!!") #Aksi True 3
else:
   print("Au ah gak kenal !!!")
print("Ini adalah akhir program")

# Latihan Percabangan
# Kalkulator sederhana
print(20*"=")
print("Kalkulator Sederhana")
print(20*"=" + "\n")

angka_1 = float(input("masukan angka 1 = "))
operator = input("operator (+,-,x,/) : ")
angka_2 = float(input("masukan angka 2 = "))

# percabangannya

if operator == "+":
	hasil = angka_1 + angka_2
	print(f"hasilnya adalah {hasil}")
elif operator == "-":
	hasil = angka_1 - angka_2
	print(f"hasilnya adalah {hasil}")
elif operator == "x" or operator == "*":
	hasil = angka_1 * angka_2
	print(f"hasilnya adalah {hasil}")
elif operator == "/":
	hasil = angka_1 / angka_2
	print(f"hasilnya adalah {hasil}")
else:
	print("masukan yang bener dong!, aku pusying")

print("Akhir dari program, terima gajih!")

# Perulangan (Loop)

"""
Syntaxnya seperti dibawah ini :
for i in data:
  aksi
  
Note: For Loop akan melihat kondisi data terakhir maka eksekusi akan berakhir (selesai)
"""

# Ini dengan list
angka_list = [0,1,2,3,4] # ini adalah list
print(angka_list)
for i in angka_list:
  print(f"i sekarang -> {i}")
print("Akhir dari program 1\n")

# Ini dengan range
angka_range = range(5)
for i in angka_range:
  print(f"i sekarang -> {i}")
print("Akhir dari program 2\n")

angka_range = range(1,10)
for i in angka_range:
  print(f"i sekarang -> {i}")
  #print("Aku pasti bisa...!!!")
print("Akhir dari program 3\n")

# Menggunakan string
data_str = "Aku dari Purwakarta"
for huruf in data_str:
    print(huruf)
print("Akhir dari program 4")

# While Loop
"""
Syntaxnya seperti dibawah ini :
while kondisi:
      aksi ini
      aksi itu
akhir dari program
Note: While Loop kondisi False maka akan keluar dari Perulangan (Loop)
"""

angka = 0
print(f"Angka sekarang -> {angka}")
while angka < 5:
  angka += 1
  print(f"Angka sekarang -> {angka}")
  print(f"Ini adalah contoh While Loop")
  
print("Kondisi While Loop tidak sesuai, program berakhir")

# continue,pass, dan break

# pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0
while angka < 5:
  angka += 1
  if angka == 3:
    pass # ini tidak akan dieksekusi
  
  print(angka)
  
# continue
angka = 0
print(f"Angka sekarang -> {angka}")
while angka < 5:
  angka += 1
  
  print(f"Angka sekarang -> {angka}") # Aksi 1
  
  if angka == 3:
    print("Nice...!")
    continue # Akan membuat loop meloncat ke step selanjutnya
  
  print("What's Up...!!") # Aksi 2
print("Finish...!!!")

# Break

# Contoh ke 1
angka = 0
while angka < 5:
  angka += 1
  
  print(f"Angka sekarang = {angka}")
  
  if angka == 3:
    print("Nice...!")
    break 
  
  print("Whats's Up")
print("Finish")

# Contoh ke 2
data_int = int(input("Hitung sampai berapa = "))
angka = 0
while True:
  angka += 1
  print(f"Count = {angka}")
  
  if angka == data_int:
    print("Nice...!")
    break 
  
  print("Whats's Up")
print("Finish")

# Latihan Loop Membuat Segitiga

sisi = 10

# 1. Menggunakan For Loop
# dummy variable
print("Menggunakan For Loop")
count = 1

for i in range(sisi):
  print("*"*count)
  count += 1
  
print("Akhir For Loop\n")
  
# 2. Menggunakan While Loop
print("Menggunakan While Loop")
count = 1

while True:
  print("*"*count)
  count += 1
  
  if count > sisi:
    break
  
print("Akhir While Loop\n")


# 3. Hanya ganjil saja
print("Menggunakan While Loop Hanya Ganjil")
count = 1
while True:
  
  if count % 2:
    # Print jika ganjil
    print("*"*count)
    count += 1
    
  else:
    # Hanya count up jika genap
    count += 1
    continue
   # Akan break jika count melebihi sisi
  if count > sisi:
    break
  
  print("Akhir While Loop Ganjil")
    
# 4. Menggunakan While Loop Secara Simetris
print("Menggunakan While Loop Secara Simetris")
count = 1
spasi = int(sisi/2)
while True:
  
  if count % 2:
    # Print jika ganjil
    print(" "*spasi, "+"*count)
    count += 1
    spasi -= 1
    
  else:
    # Hanya count up jika genap
    count += 1
    continue
   # Akan break jika count melebihi sisi
  if count > sisi:
    break
  
# Latihan Loop Membuat Segitiga

sisi = 10

# 1. Menggunakan For Loop
# dummy variable
print("Menggunakan For Loop")
count = 1

for i in range(sisi):
  print("*"*count)
  count += 1
  
print("Akhir For Loop\n")
  
# 2. Menggunakan While Loop
print("Menggunakan While Loop")
count = 1

while True:
  print("*"*count)
  count += 1
  
  if count > sisi:
    break
  
print("Akhir While Loop\n")


# 3. Hanya ganjil saja
print("Menggunakan While Loop Hanya Ganjil")
count = 1
while True:
  
  if count % 2:
    # Print jika ganjil
    print("*"*count)
    count += 1
    
  else:
    # Hanya count up jika genap
    count += 1
    continue
   # Akan break jika count melebihi sisi
  if count > sisi:
    break
  
  print("Akhir While Loop Ganjil")
    
# 4. Menggunakan While Loop Secara Simetris
print("Menggunakan While Loop Secara Simetris")
count = 1
spasi = int(sisi/2)
while True:
  
  if count % 2:
    # Print jika ganjil
    print(" "*spasi, "+"*count)
    count += 1
    spasi -= 1
    
  else:
    # Hanya count up jika genap
    count += 1
    continue
   # Akan break jika count melebihi sisi
  if count > sisi:
    break
  
while True:
  
  if count % 2:
    # Print jika ganjil
    count -= 1
  else:
    # Hanya count down jika genap
    count -= 1
    spasi += 1
    print(" "*spasi,"+"*count)
    continue
   # Akan break jika count lebih kecil dari sisi
  if count < 1:
    break
print("Akhir While Loop Secara Simetris")

# ===== LIST =====

# Kumpulan data numbers
data_angka = [1,2,3,4,5]
print(data_angka)

# Kumpulan data string 
data_string = ["Dian","Andri","Riska"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, False]
print(data_boolean)

# Kumpulan data campuran
data_campuran = [1,"Bala-bala",2,"Cireng",3,"Ucup",True,"Otong",False]
print(data_campuran)

# Cara alternatif membuat list
data_range = range(0,10,2) # range (start,stop,step)
print(data_range)
data_list = list(data_range)
print(data_list)

# Membuat list dengan for loop, list comprehension
list_pake_for = [i for i in range(0,10)]
print(list_pake_for)

# Membuat list pake for dan if
list_pake_for_if = [i**2 for i in range(0,10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i%2 != 0]
print(list_pake_for_if)

# Operasi list

# index   0      1        2   (Jika dihitung dari depan)
data = ["Ucup","Otong","Dudung"]
# index  -3     -2       -1   (Jika dihitung dari belakang)

# Mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir (index -1) = {data_terakhir}")

data_Ucup = data[-3]
print(f"data pertama (index -3) = {data_Ucup}")

# Mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"Panjang data pada list data = {panjang_data}\n")

# Manipulasi data list
# Menambahkan item pada list sesuai posisi
print(f"Data sebelum ditambah = \n{data}")

data.insert(1,"Asep")
print(f"Data sesudah ditambah = \n{data}")

# Menambah data di akhir list
data.append("Jajang")
print(f"Data ditambah lagi = \n{data}")

# Menambahkan list dengan list
data_baru =["Ujang","Usep","Dadang"]
data.extend(data_baru)
print(f"Data setelah ditambah dengan data baru = \n{data}")

# Merubah data list
# Kita ubah data index ke-2 menjadi Bogég
data[2] = "Bogég"
print(f"Data setelah edit index ke-2 = \n{data}")

# Me remove data list
data.remove("Ujang")
print(f"Data setelah remove = \n{data}")
# data.remove("usep") # Akan error karena huruf harus sesuai dengan data di list, yaitu "Usep"

# Me remove data paling belakang
data.pop()
print(f"Data akhir = {data}")


# Mengecek data yang dibuang dengan cara print (variable = data.pop())

data_angka = [1,5,1,4,3,2,4,3,2,3,7,8,9,0]
print(f"data_angka = {data_angka}")

# Count data (Menghitung data)
jumlah_data_angka_4 = data_angka.count(4)
jumlah_data_angka_3 = data_angka.count(3)
print(f"Jumlah angka 4 pada data sebanyak = {jumlah_data_angka_4}")
print(f"Jumlah angka 3 pada data sebanyak = {jumlah_data_angka_3}")

# Mengambil posisi data (index)
data = ["Ucup","Otong","Dudung","Ujang"]
print(f"data ={data}")
index_Dudung = data.index("Dudung")
index_Ujang = data.index("Ujang")

print(f"Posisi index Dudung pada data = index ke-{index_Dudung}")
print(f"Posisi index Ujang pada data = index ke-{index_Ujang}")

# Mengurutkan list
print(f"Data angka sebelum sort = \n{data_angka}")

data_angka.sort()
print(f"Data angka setelah sort = \n{data_angka}")

print(f"data = {data}")
data.sort()
print(f"data sort = {data}")

# Cara membalik data list
data_angka.reverse()
data.reverse()

print(f"Data angka setelah sort lalu di reverse = \n{data_angka}")
print(f"Data setelah sort lalu di reverse = \n{data}")

# Teknik Menduplikat List

a = ["Ucup","Otong","Dudung"]
print(f"a = {a}")

b = a # Ini namanya pass by reference
print(f"b = {b}")

# Kita akan merubah member dari list a 

# Ini akan merubah kedua list
a[1] = "Michael"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# Address dari kedua list a dan b 
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# Menduplikat List dengan copy
print(f"Membuat list c dengan a.copy")
c = a.copy() # Ini full duplicate / data baru
print(f"c = {c}")

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(f"Kita ubah data index [0] pada list c")
c[0] = "Dadang"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

print(f"Kita ubah data index [1] pada list a")
a[1] = "Otong"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")

data_0 = [1,2]
data_1 = [3,4]
data_list_biasa = [1,2,3,4]
print(f"List biasa = {data_list_biasa}")

list_2D = [data_0,data_1,6,7]
print(f"list_2D = {list_2D}")

# Contoh penggunaan

peserta_a = ["Ucup",25,"Laki-laki"]
peserta_b = ["Otong",10,"Laki-laki"]
peserta_c = ["Agnes",32,"Wanita"]

print("\n")

list_peserta = [peserta_a,peserta_b,peserta_c]
print(f"list_peserta = {list_peserta}")

print("\n")

for peserta in list_peserta:
  print(f"nama\t: {peserta[0]}")
  print(f"umur\t: {peserta[1]}")
  print(f"gender\t: {peserta[2]}\n")
  
# Dengan reference
list_copy = list_peserta.copy()
print(f"list_peserta.copy = {list_copy}\n")
peserta_a[0] = "Michael"
print(f"list_peserta.copy = {list_copy}\n")
print(f"list_peserta = {list_peserta}")

data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1]
data_2D_copy = data_2D.copy()
print(f"data = {data_2D}")

# Mengambil data dari Nested List 
data = data_2D[0]
print(f"data = {data}")

data =data_2D[0][0]
print(f"data = {data}")

data = data_2D[1]
print(f"data = {data}")

data = data_2D[1][0]
print(f"data = {data}")

# Address data
print(f"Address asli = {hex(id(data_2D))}")
print(f"Address copy = {hex(id(data_2D_copy))}")

print(f"Address dari member ke-1")
print(f"Address asli = {hex(id(data_2D[0]))}")
print(f"Address copy = {hex(id(data_2D_copy[0]))}")

#===== Note =====#
"""
methode list.copy() ini adalah copy shallow = meng-copy dangkal, address nama list saja yang berbeda tetapi address member pada list masih sama. Untuk member diluar list bisa dicopy.
"""

# Untuk melakukan copy secara mendalam, kita bisa gunakan methode deep copy

# Cara menggunakan deepcopy
from copy import deepcopy

data_2D = [data_0,data_1]
data_2D_deepcopy = deepcopy(data_2D)

print(f"Address asli = {hex(id(data_2D))}")
print(f"Address deepcopy = {hex(id(data_2D_deepcopy))}")

print(f"Address dari member ke-1")
print(f"Address asli = {hex(id(data_2D[0]))}")
print(f"Address deepcopy = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][0]= 30
print(f"data = {data_2D}")
print(f"data copy= {data_2D_copy}")
print(f"data deepcopy= {data_2D_deepcopy}")

# Ini adalah looping dari list

# for loop
print("For Loop")
kumpulan_angka = [4,3,2,5,6,1]

for angka in kumpulan_angka:
  print(f"Angka = {angka}")
  
print("\n")
  
peserta = ["Ucup","Otong","Dadang","Diding","Dudung"]
  
for nama in peserta:
  print(f"Nama peserta = {nama}")
 
  
print("\n") 

# for loop dan range
print("For Loop dan Range")
kumpulan_angka = [10,5,4,2,6]
  
panjang = len(kumpulan_angka)
for i in range(panjang):
  print(f"Angka = {kumpulan_angka[i]}")
  
print("\n")
  
# while loop
print("While Loop")
kumpulan_angka = [10,5,4,2,6]
  
panjang = len(kumpulan_angka)
i = 0
while i < panjang:
  print(f"Angka = {kumpulan_angka[i]}")
  i += 1
  
print("\n")

# Menggunakan List Comprehension
print("List Comprehension")
data = ["Ucup",1,2,3,"Otong"]
[print(f"data = {i}") for i in data]

print("\n")

angka = [10,5,4,2,6]
angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

print("\n")

# enumerate
print("Enumerate")

data_list = ["Ucup",1,2,3,"Otong"]

for index,data in enumerate(data_list):
  print(f"index = {index}, data = {data}")
  
# Program List Buku

list_buku = []
while True:
  print("\nMasukkan data buku")
  judul = input("Judul buku\t: ")
  penulis = input("Nama Penulis\t: ")
  buku_baru =[judul,penulis]
  list_buku.append(buku_baru)
  
  print("\n\n","="*10,"Data Buku","="*10)
  for index,buku in enumerate(list_buku):
    print(f"{index+1} | {buku[0]} | {buku[1]}")
    
  print("\n\n","="*20)
  isLanjut = input("Apakah dilanjutkan ? (Y/N) = ")
  
  if isLanjut == "N":
    break

print("PROGRAM SELESAI")

# list
# Menggunakan kurung siku [ ]
data_list = [10,2,4,3,4,8]
print(data_list)

# tuples
# Menggunakan kurung biasa ( )
# Data tuples tidak bisa kita rubah isinya
# Contoh Syntax Error seperti dibawah ini :
# data_tuples[1] = "Ucup" x
# data_tuples.append(1) x

data_tuples = (7,8,9,10)
print(data_tuples)
print(data_tuples[1])

# sets
# Sebuah collection yang tidak punya index
# Hanya berupa himpunan data
# Hanya indexing yang tidak bisa dilakukan
# Untuk menghitung, append dan lainnya bisa dilakukan
data_sets = {10,4,3,2,4,7,6,5}
print(data_sets)

# list -> array, mengakses data dengan menggunakan index
data_list = ["Ucup","Otong","Dudung"]
print(data_list[0])

# dictionary (dict) -> associative array
# identifier -> key

data_dict = {
  "key1":"value1",
  "key2":"value2",
  "cp":"Ucup",
  "tg":"Otong",
  "dg":"Dudung",
  "number":100,
  "list":data_list,
}

print(data_dict["tg"])
print(data_dict["number"])
print(data_dict["list"])

# Operator dictionary
data_dict = {
  "cup":"Ucup Surucup",
  "tong":"Otong Surotong",
  "dung":"Dudung Surudung"
}

# Panjang dictionary
LENDICT = len(data_dict)
print(f"Panjang dictionary = {LENDICT}")

# Mengecek key exist atau tidak
KEY = "cup"
CHECKKEY = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict : {CHECKKEY}")

# Mengakses value (read) dengan get
print(data_dict["cup"])
print(data_dict.get("cup"))
print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan message tidak ditemukan
# Jika mengakses dictionary tanpa get, ketika key tidak ada maka akan muncul error

# Mengupdate data
data_dict["cup"] = "Ucup si Ganteng"
print(data_dict)
data_dict["sep"] = "Asep si Kasep"
print(data_dict)

data_dict.update({"cup":"Ucup Surucup"}) # Kalo key ada maka data diupdate
print(data_dict)

data_dict.update({"dian":"Dian si Chikal"}) # Kalo key gak ada maka data di add za
print(data_dict)

# Delete data pada dictionary
del data_dict["dian"]
print(data_dict)

# Looping Dictionary
teman_teman = {
  "cup":"Ucup Surucup",
  "tong":"Otong Surotong",
  "dung":"Dudung Surudung",
  "sep":"Asep si Kasep",
  "cuy":"Ucuy Surucuy"
}

# Looping First Try (Yang keluar adalah key nya)
for teman in teman_teman:
  print(teman)
  
# Operator untuk mengambil item / iterables
keys = teman_teman.keys()
print(keys) # ini keluar dictionary hanya key saja

for key in teman_teman.keys():
    print(key) # ini yang keluar hanya key saja
    
for key in teman_teman.keys():
    print(teman_teman.get(key)) # ini yang keluar hanya value saja
    
values = teman_teman.values()
print(values) # ini keluar dictionary hanya values saja

for value in teman_teman.values():
    print(value)
    
items = teman_teman.items()
print(items) # ini keluar dictionary items

for item in teman_teman.items():
    print(item) # ini keluar tuples items
    
for key,value in teman_teman.items():
    print(f"key = {key}, value = {value}")
    
# Copy Dictionary

teman_teman = {
  "cup":"Ucup Surucup",
  "tong":"Otong Surotong",
  "dung":"Dudung Surudung",
  "sep":"Asep si Kasep",
  "cuy":"Ucuy Surucuy"
}

friends = teman_teman.copy()
print(f"teman_teman = {teman_teman}\n")
print(f"friends = {friends}\n")

teman_teman["cup"]= "Ucup si Keren"
print(f"teman_teman = {teman_teman}\n")
print(f"friends = {friends}\n")

"""
Note : Jika variabel B = variabel A, maka akan ke reference yang sama . Jika menggunakan .copy() seperti ini -> variabel B = variabel A.copy() maka akan menjadi 2 hal yang berbeda. Jika variabel A dirubah, maka variabel B tidak akan ikut berubah
"""

# pop Dictionary (diambil berdassrkan key)
dataAsep = friends.pop("sep")
print(f"data Asep = {dataAsep}\n")
print(f"friends = {friends}\n")

#popitem Dictionary (diambil yang terakhir za)
dataTerakhir = friends.popitem()
print(f"dataTerakhir = {dataTerakhir}\n")
print(f"friends = {friends}\n")

import datetime

mahasiswa1 ={
  "nama" : "Ucup Surucup",
  "nim":"19022021",
  "sks_lulus":130,
  "beasiswa":False,
  "lahir":datetime.datetime(2001,4,10) #datetime(tahun,bulan,tanggal)
}

mahasiswa2 ={
  "nama" : "Otong Surotong",
  "nim":"19022022",
  "sks_lulus":140,
  "beasiswa":True,
  "lahir":datetime.datetime(2002,10,10) #datetime(tahun,bulan,tanggal)
}

mahasiswa3 ={
  "nama" : "Asep si Kasep",
  "nim":"19022023",
  "sks_lulus":125,
  "beasiswa":False,
  "lahir":datetime.datetime(2000,2,29) #datetime(tahun,bulan,tanggal)
}

data_mahasiswa = {
  "MAH001":mahasiswa1,
  "MAH002":mahasiswa2,
  "MAH003":mahasiswa3
}
print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*50)
"""
Note: Trick pada format sting,perhatikan contoh print dibawah ini
print(f"{'KEY':<6} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")

Tanda <6 artinya rata kiri dengan 6 karakter
Tanda >5 artinya rata kanan dengan 5 karakter
Tanda ^8 artinya rata tengah / center dengan 8 karakter

Angka yang mengikuti tanda artinya jumlah karakter yg disetting.
"""
for mahasiswa in data_mahasiswa:
  KEY = mahasiswa
  NAMA = data_mahasiswa[KEY]["nama"]
  NIM = data_mahasiswa[KEY]["nim"]
  SKS = data_mahasiswa[KEY]["sks_lulus"]
  BEASISWA = data_mahasiswa[KEY]["beasiswa"]
  LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")
  
  print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")

import datetime
import os

# template dict mahasiswa
mahasiswa_template = {
  "nama":"nama",
  "nim":"00000000",
  "sks_lulus":0,
  "lahir":datetime.datetime(1111,1,11)
}

data_mahasiswa ={}

os.system("cls") # Untuk Windows
os.system("clear") # Untuk Mac
# Note : Fungsi os.system -> Untuk menghapus tulisan yang diatas. Sehingga ketika program di RUN layar bersih hanya menampilkan program saja
print(f"{'SELAMAT DATANG':^20}")
print(f"{'DATA MAHASISWA':^20}")
print("-"*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
mahasiswa["nama"] = input("Nama Mahasiswa: ")
mahasiswa["nim"] = input("NIM Mahasiswa: ")
mahasiswa["sks_lulus"] = int(input("SKS Lulus: "))
TAHUN_LAHIR = int(input("Tahun Lahir (YYYY): " ))
BULAN_LAHIR = int(input("Bulan Lahir (MM): "))
TANGGAL_LAHIR = int(input("Tanggal Lahir (DD): "))
mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
print(mahasiswa)

import datetime
import os
import string 
import random 

# template dict mahasiswa
mahasiswa_template = {
  "nama":"nama",
  "nim":"00000000",
  "sks_lulus":0,
  "lahir":datetime.datetime(1111,1,11)
}

data_mahasiswa ={}

while True:
  os.system("cls") # Untuk Windows
  os.system("clear") # Untuk Mac
  # Note : Fungsi os.system -> Untuk menghapus tulisan yang diatas. Sehingga ketika program di RUN layar bersih hanya menampilkan program saja
  print(f"{'SELAMAT DATANG':^20}")
  print(f"{'DATA MAHASISWA':^20}")
  print("-"*20)
  
  mahasiswa = dict.fromkeys(mahasiswa_template.keys())
  mahasiswa["nama"] = input("Nama Mahasiswa: ")
  mahasiswa["nim"] = input("NIM Mahasiswa: ")
  mahasiswa["sks_lulus"] = int(input("SKS Lulus: "))
  TAHUN_LAHIR = int(input("Tahun Lahir (YYYY): " ))
  BULAN_LAHIR = int(input("Bulan Lahir (MM): "))
  TANGGAL_LAHIR = int(input("Tanggal Lahir (DD): "))
  mahasiswa["lahir"] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)
  
  KEY = "".join((random.choice(string.ascii_uppercase) for i in range(6)))
  data_mahasiswa.update({KEY:mahasiswa})
  
  print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
  print("-"*60)
  for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]["nama"]
    NIM = data_mahasiswa[KEY]["nim"]
    SKS = data_mahasiswa[KEY]["sks_lulus"]
    LAHIR = data_mahasiswa[KEY]["lahir"].strftime("%x")
    
    print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")
    
  print("\n")
  is_done = input("Apakah akan isi data lagi (Y/N) ?: ")
  if is_done == "N":
      break
    
print("Akhir dari program,terima kasih ^_^")

"""
# Fungsi -> Function
         -> Method 
         -> Sub routine / routine
         
  Di pemograman jangan mengulang menulis code program yang sudah kita lakukan. 
  Maka dari itu,muncul paradigma Don't repeat code, do it once. Maka muncullah fungsi, untuk mempermudah kita untuk melakukan hal yang sama berulang-ulang.
  Fungsi harus didefinisikan sebelum kita panggil.
"""

"""Membuat Fungsi"""

def hello_world():
  print("Hello World") # Fungsi menampilkan Hello World
  print("Di dalam fungsi bisa diisi banyak code")
  print("Contohnya seperti ini")
  
hello_world()
hello_world()

def fungsi():
    print("Ini adalah fungsi")
    
fungsi()

""" Fungsi dengan Argument (input)"""

# Template Fungsi
# def nama_fungsi(argument):
#   badan fungsi
   
# Note : argument/parameter/input akan masuk ke badan fungsi
# Isi badan fungsi bisa macam², mau string, number, boolean,list, terserah kalian


def hello_world(nama):
  """ Fungsi hello world menggunakan input dengan variabel nama """
  print(f"Selamat pagi dunia wahai {nama}")

hello_world("Ucup")
hello_world("Asep")

# Contoh 1
def tambah(angka1,angka2):
  """ Fungsi Tambah """
  hasil = angka1 + angka2
  print(f"{angka1} + {angka2} = {hasil}")

tambah(1,5)
tambah(100000,1)

def say_hi(list_peserta):
  """ Fungsi say hi """
  data_peserta = list_peserta.copy()
  for peserta in data_peserta:
    print(f"Yang terhormat {peserta}")
  
  
anggota_boyband = ["Ucup","Otong","Dudung"]
say_hi(anggota_boyband)

"""
Penjelasan Fungsi say_hi
▪︎Kita mempunyai data anggota boyband diluar fungsi. 
▪︎Saat dia masuk ke fungsi say_hi, variabelnya dirubah menjadi list_peserta.
list_peserta = anggota_boyband
▪︎Apapun yang kita masukkan ke fungsi say_hi akan berubah menjadi list_peserta
"""

""" Fungsi dengan kembalian (return value) """

# Template fungsi dengan kembalian
#def nama_fungsi(argument):
#        badan fungsi
#        return output

# Fungsi Kuadrat
def kuadrat(input_angka):
  output_kuadrat = input_angka ** 2
  return output_kuadrat
	
x = kuadrat(5)
print(x)
	
print(kuadrat(6))

z = 10 + kuadrat(7)
print(z)

# Fungsi Tambah
def fungsi_tambah(angka_1,angka_2):
  """Fungsi return dengan multi input"""
  return angka_1 + angka_2
  
a = fungsi_tambah(10,8)
print(a)

# Fungsi dengan return banyak
def operasi_matematika(angka_1,angka_2):
  tambah = angka_1 + angka_2
  kurang = angka_1 - angka_2
  kali = angka_1 * angka_2
  bagi = angka_1 / angka_2
  
  return tambah,kurang,kali,bagi
  
k,l,m,n = operasi_matematika(9,5)
print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")

"""Default Argument"""

# def fungsi(argument):
# def fungsi(argument = nilai defaultnya):

# Contoh 1

def say_hello(nama = "Ganteng"):
  """Fungsi dengan default argument"""
  print(f"Hallo {nama}")
  
say_hello("Ucup")

# Note : default argument berfungsi untuk mengisi value default ketika sebuah fungsi dipanggil tetapi tidak diisi dengan argument

# Perhatikan contoh pemanggilan fungsi dibawah ini, ketika fungsi dipanggil tanpa argument, maka nilai default argument yang akan keluar adalah "Ganteng" karena pada default argument diisi dengan value "Ganteng"
say_hello()

# Contoh 2

def sapa_dia(nama, pesan = "Apa kabar"):
  """Fungsi dengan satu input biasa, dan satu default argument""" 
  print(f"Hai {nama}, {pesan}")
  
sapa_dia("Dudung","Hai ganteng")
sapa_dia("Otong")

# Contoh 3

def hitung_pangkat(angka, pangkat=2):
	hasil = angka ** pangkat
	return hasil

print(hitung_pangkat(2,4))

hasil = hitung_pangkat(pangkat=3, angka=5)
print(hasil)

# Contoh 4

def fungsi(input1=1,input2=2,input3=3,input4=4):
	hasil = input1 + input2 + input3 + input4
	return hasil
	
print(fungsi())
print(fungsi(input3 = 10))

# Note : Jika argument pada fungsi diisi , maka argument yang dieksekusi sesuai data, tidak berdasarkan argument defaultnya

"""Latihan Fungsi"""

import os 

#Program menghitung luas dan keliling persegi panjang

#Membuat header program 
#os.system("clear")
#os.system("cls")
#print(f'{"PROGRAM MENGHITUNG LUAS":^40}')
#print(f'{"DAN KELILING PERSEGI PANJANG":^40}')
#print(f'{"-"*40:^40}')

 #Mengambil input user
#LEBAR = int(input("Masukkan nilai lebar: "))
#PANJANG = int(input("Masukkan nilai panjang: "))

# Program menghitung luas 
#LUAS = PANJANG * LEBAR 
#KELILING = 2 * (PANJANG + LEBAR)

 #Tampilkan hasilnya
#print(f"Hasil perhitungan luas = {LUAS}")
#print(f"Hasil perhitungan keliling = {KELILING}")

def header():
  os.system("clear")
  #os.system("cls")
  print(f'{"PROGRAM MENGHITUNG LUAS":^40}')
  print(f'{"DAN KELILING PERSEGI PANJANG":^40}')
  print(f'{"-"*40:^40}')

def input_user():
   """Fungsi Input User"""
   lebar = int(input("Masukkan nilai lebar: "))
   panjang = int(input("Masukkan nilai panjang: "))
   return lebar,panjang
   
def hitung_luas(lebar,panjang):
	"""Fungsi Luas"""
	return lebar * panjang
	
def hitung_keliling(lebar,panjang):
	"""Fungsi Keliling"""
	return 2*(lebar+panjang)

def display(message,value):
	"""Fungsi Display"""
	print(f"Hasil perhitungan {message} = {value}")
	
# Program utamanya
while True:
    header()
    LEBAR,PANJANG = input_user()
    LUAS = hitung_luas(LEBAR,PANJANG)
    KELILING = hitung_keliling(LEBAR,PANJANG)
    
    display("luas", LUAS)
    display("keliling", KELILING)
    
    isContinue = input("Apakah akan dilanjutkan (Y/N? : ")
    if isContinue == "N":
      break
      
print("Program selesai, terima kasih")

""" Type Hints Untuk Fungsi"""

# Bentuk standard fungsi yang sudah kita pelajari

"""
Ini adalah study kasus
def fungsi(argument):
  hasil = argument**2
  print(hasil)
  
fungsi(1)
fungsi("Ucup")
fungsi(True)
"""

# Penggunaan Tupe Hints
import string
def fungsi_dengan_hints(argument:int) ->int:
  """Fungsi dengan Hints"""
  output = 10**argument
  return output
  
HASIL = fungsi_dengan_hints(2)
print(HASIL)

def display(argument:string):
  print(argument)
  
display("Ucup")

import os 
hasil = os.system("clear")

"""
Note : Type hints berfungsi untuk memberitahukan rekan kerja tentang suatu fungsi itu INPUT nya apa?? OUTPUTNYA apa??? Apakah Integer, Float, String, Boolean dll"""

""" *args """

# Memasukkan data/argument

def fungsi(nama,tinggi,berat):
  print(f"{nama} punya tinggi {tinggi}cm dan berat {berat}kg")
  
fungsi("Ucup",170,48)

def fungsi(data_list):
  data = data_list.copy()
  nama = data[0]
  tinggi = data[1]
  berat = data[2]
  print(f"{nama} punya tinggi {tinggi}cm dan berat {berat}kg")
  
fungsi(["Otong",150,55])

# Kenalan dengan *args
def fungsi(*args):
  nama = args[0]
  tinggi = args[1]
  berat = args[2]
  print(f"{nama} punya tinggi {tinggi}cm dan berat {berat}kg")
  
fungsi("Dudung",175,45)

# Study kasus

def tambah(*data):
  # data type nya adalah tuple dan bisa diiterasi
  output = 0
  for angka in data:
    output += angka
    
  return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"Hasil = {hasil}")

hasil = tambah(10,5,15)
print(f"Hasil = {hasil}")
  
"""**kwargs"""

def fungsi(nama,tinggi,berat):
  """fungsi biasa"""
  print(f"{nama} punya tinggi {tinggi}cm dan berat {berat}kg")

fungsi("Ucup",187,79)

def fungsi(**kwargs):
  """fungsi kwargs"""
  nama = kwargs["nama"]
  tinggi = kwargs["tinggi"]
  berat = kwargs["berat"]
  print(f"{nama} punya tinggi {tinggi}cm dan berat {berat}kg")
  
fungsi(nama="Ucup",tinggi=187,berat=79)

# Study Kasus

def math(*args,**kwargs):
  output = 0
  if kwargs["option"] == "tambah":
    for angka in args:
      output += angka
  elif kwargs["option"] == "kali":
    output = 1
    for angka in args:
      output *= angka
  else:
    print("Tidak ada operasi")
    
  return output
  
  
hasil = math(1,2,3,4,option = "tambah")
print(f"Hasil jumlah = {hasil}")

hasil = math(1,2,3,4,option = "kali")
print(f"Hasil kali = {hasil}")

# Lambda Function

def fungsi_kuadrat(angka):
  return angka**2
  
print(f"Hasil fungsi kuadrat = {fungsi_kuadrat(3)}")

# Kita coba dengan lambda
# Output = lambda argument: expression

kuadrat = lambda angka : angka**2
print(f"Hasil dari lambda kuadrat = {kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"Hasil lambda pangkat = {pangkat(4,2)}")

# Kegunaannya apa Bang?

# Sorting untuk list biasa
data_list = ["Otong","Ucup","Dudung"]
data_list.sort()
print(f"sorted list = {data_list}")

# Sorting dia pakai panjang
def panjang_nama(nama):
  return len(nama)
  
data_list.sort(key=panjang_nama)
print(f"sorted list by panjang_nama = {data_list}")

# Sort menggunakan lambda
data_list = ["Otong","Ucup","Dudung"]
data_list.sort(key=lambda nama:len(nama))
print(f"sorted list by lambda = {data_list}")

# filter
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]
def kurang_dari_lima(angka):
  return angka < 5
  
data_angka_baru = list(filter(kurang_dari_lima,data_angka))
data_angka_baru = list(filter(lambda x:x<7,data_angka))
print(data_angka_baru)

# Kasus genap
data_genap = list(filter(lambda x:(x % 2==0),data_angka))
print(data_genap)

# Kasus ganjil
data_ganjil = list(filter(lambda x:(x % 2!=0),data_angka))
print(data_ganjil)

# Kelipatan 3
data_3 = list(filter(lambda x:(x % 3==0),data_angka))
print(data_3)

# Anonymous Function
# currying <- Haskell currying

def pangkat(angka,n):
  hasil = angka**n 
  return hasil
  
data_hasil = pangkat(5,2)
print(f"Fungsi biasa = {data_hasil}")

# Dengan currying
def pangkat(n):
  return lambda angka:angka**n 
  
pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")
  
pangkat3 = pangkat(3)
print(f"pangkat 3 = {pangkat3(3)}")
print(f"pangkat bebas = {pangkat(4)(5)}")

## Global dan Local Scope

nama_global = "Otong" # <- ini adalah variabel global

# Akses variabel global dalam fungai
def fungsi():
  print(f"fungsi menampilkan {nama_global}")

fungsi()

# Akses variabel global dalam loop
for i in range (0,5):
  print(f"Loop ke {i} - {nama_global}")

# Akses variabel global dalam percabangan
if True:
  print(f"if menampilkan {nama_global}")
  
## Variabel Local Scope

def fungsi2():
  nama_local = "Ucup" # <- ini adalah variabel local scope
  
fungsi2()
# print(nama_local) # ini tidak bisa dilakukan boss

## Contoh 1 : Penggunaan Variabel

def say_otong():
  print(f"Hello {nama}")
 
nama = "Otong" 
say_otong()

## Contoh 2 : Akses Variabel
angka = 0
name = "Ucup"

def ubah(nilai_baru,nama_baru):
  global angka # fungsi ini mendapat akses merubah variabel angka
  global name # fungsi ini mendapat akses merubah variabel name
  angka = nilai_baru
  name = nama_baru
"""
Note: Jika kita akan merubah variabel global di dalam fungsi, maka harus menggunakan global (spasi) nama variabel seperti contoh diatas
"""
print(f"Before {angka,name}")
ubah(10,"Otong")
print(f"After {angka,name}")

## Contoh 3 :
angka = 0 

for i in range(0,5):
  angka += i
  angka_dummy = 0
  
print(angka)
print(angka_dummy)

if True:
  angka = 10
  angka_dummy = 10
  
print(angka)
print(angka_dummy)

