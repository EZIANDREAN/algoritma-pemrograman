#Mambuat Program menghitung luas lingkaran


# Menghitung luas lingkaran
import math

# Nilai jari-jari
r = 10

# Rumus luas lingkaran
luas = math.pi * r * r

# Menampilkan hasil
print("Luas lingkaran dengan jari-jari", r, "adalah", luas)



# Konversi suhu dari Fahrenheit ke Celsius
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    return celsius

# Suhu dalam Fahrenheit
f = 130

# Mengonversi ke Celsius
c = fahrenheit_to_celsius(f)

print(f"Suhu {f}°F adalah {c:.2f}°C")


# Fungsi untuk menghitung luas segitiga
def luas_segitiga(a, t):
    luas = 0.5 * a * t
    return luas

# Input dari pengguna
a = float(input("Masukkan panjang alas segitiga (a): "))
t = float(input("Masukkan tinggi segitiga (t): "))

# Menghitung luas segitiga
luas = luas_segitiga(a, t)

# Menampilkan hasil
print(f"Luas segitiga dengan alas {a} dan tinggi {t} adalah {luas:.2f}")

