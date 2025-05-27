def hitung_fpb(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Contoh penggunaan fungsi
bilangan1 = 48
bilangan2 = 18

fpb = hitung_fpb(bilangan1, bilangan2)
print(f"FPB dari {bilangan1} dan {bilangan2} adalah {fpb}")