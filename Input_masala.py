import math
# # input operatoridan foydalanib Masala ishlash
# a = int(input("Istalgan son kiriting men uni kub ildizini aniqlab beraman : "))
# n =  a * a * a
# print("Siz kiritgan sonning kub ildizi : ", n)

# Kvadatning tomoni berilgan uning peremetrini aniqlash dasturini yozing

# k_tomoni = int(input("Kvadratning tomonini kiriting : "))

# p = k_tomoni * 4

# print("Kvadratning peremetri : P = ", p)

# Ikkita son a va b berilgan ularning orta arfimetikini aniqlash dasturini yarating

# a = int(input("Birinchi sonni kiriting : a = "))
# b = int(input("Ikkinchi sonni kiriting : b = "))

# o_arf = (a + b) / 2

# print("Orta arifmetigi : O = ", o_arf)

# Ikkita manfiy bo'lmagan a va b soni berilgan ularning  o'rta geometrikini  aniqlash dasturini yozing

# a = int(input("Birinchi manfiy bo'lmagan sonni kiriting : a = "))
# b = int(input("Ikkinchi manfiy bo'lmagan sonni kiriting : b = "))

# o_geom = math.sqrt(a * b)
# print("O'rta geometrigi : O_geometrik qiymati = ", o_geom)

# Nolga teng bolmagan ikkita son berilgan. Ularning Yigindisini, Kopaytmasini, Va modullarini aniqlash dasturini yarating 

birinchi_son = float(input("Nolga teng bo'lmagan ixtiyoriy son kiriting  son1 = "))
ikkinchi_son = float(input("Nolga teng bo'lmagan ixtiyoriy son kiriting  son2 = "))

yigindi = birinchi_son + ikkinchi_son
kopaytma = birinchi_son * ikkinchi_son
son1_modul = math.fabs(birinchi_son) 
son2_modul = math.fabs(ikkinchi_son)

print(f"Siz kiritgan sonlarning \n Yigindisi = {yigindi} \n Kopaytmasi = {kopaytma} \n Birinchi sonning moduli = {son1_modul} \n Ikkinchi sonning moduli = {son2_modul}")