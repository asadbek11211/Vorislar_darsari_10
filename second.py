#Bugundan Python dasturlash tilini o'rganamiz
#print( ) konsolga malumot chiqarish un qollaniladi

print('Hello, World!')
print("Hello, World!")
print("""Hello, World!""")

print('Salom \n o\'quvch\nilar')
print("Hayr Humoyun o'quvchi")
print("""Hello, World!""")

#Arithmetic Operators
# +, -, *, /, //, %, **

# + qo'shish

a = 12
b = 8
c = a + b
print("c =", c)

# - ayirish
d = a - b
print("d =", d)

# * ko'paytirish
e = a * b
print("e =", e)

# / bo'lish
a = 13
b = 2
f = a / b   #oddiy bo'lish
g = a // b  #Butun qismini olish
h = a % b   #qoldiqni olish

print("f =", f)
print("g =", g)
print("h =", h)

#input() klavaturadan malumot kiritish un qollaniladi
ism = input("O'zingizning Ismingiz nima? ")
ism1 = input("Otangizning ismi nima?")
ism2 = input("Onangizning ismi nima?")
print("Salom Hurmatli ", ism, ism1, ism2) 