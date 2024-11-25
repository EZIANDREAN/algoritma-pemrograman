# Operasi yang dapat dilakukan dengan meringkas
# Operasi ditambah dengan assignment

a = 5 # assignment
print("nilai a = ", a)

a += 1 # artinya a = a + 1
print("nilai a += 1, nilai a menjadi = ", a)

a -= 1
print("nilai a -= 1, nilai a menjadi = ", a)
a *= 1
print("nilai a *= 1, nilai a menjadi = ", a)
a /= 1
print("nilai a /= 1, nilai a menjadi = ", a)

a %= 1 # modulus
print("nilai a %= 1, nilai a menjadi = ", a)

a //= 1 # floot
print("nilai a //= 1, nilai a menjadi = ", a)

# pangkat / exponen
# **=
a **= 10 # artinya a = a // 1
print("nilai a **= 5, nilai a menjadi = ", a)

# OR
c = True
print("nilai c = ", c)
c |= False
print("nilai c |= False, menjadi c = ", c)
c |= True
print("nilai c |= True, menjadi c = ", c)

# AND
c = True
print("nilai c = ", c)
c &= False  # Artinya c = c and False
print("nilai c &= False, menjadi c = ", c)
c |= True
print("nilai c &= True, menjadi c = ", c)
