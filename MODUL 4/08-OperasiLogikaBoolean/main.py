# Operasi Logika Dan Boolean

# not, or ,and

# NOT
print("===NOT===")
a = False
c = not a
print("data a = ", a)
print("------------------ , NOT")
print("data c = ", c)

# OR (jika salah satu true, hasilnya akan true)
print("===OR===")
a = False
b = False
c = a or b
print(a, "OR", b, "=", c)
print("===OR===")
a = True
b = False
c = a or b
print(a, "OR", b, "=", c)
print("===OR===")
a = False
b = True
c = a or b
print(a, "OR", b, "=", c)
print("===OR===")
a = True
b = True
c = a or b
print(a, "OR", b, "=", c)

# AND (jika salah satu false, hasilnya akan false)
print("===AND===")
a = True
b = True
c = a and b
print(a, "AND", b, "=", c)
print("===AND===")
a = False
b = True
c = a and b
print(a, "AND", b, "=", c)
print("===AND===")
a = True
b = False
c = a and b
print(a, "AND", b, "=", c)
print("===AND===")
a = False
b = False
c = a and b
print(a, "AND", b, "=", c)






