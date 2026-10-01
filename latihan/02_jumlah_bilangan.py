print("=== PROGRAM JUMLAH BILANGAN BERURUTAN ===")
n = int(input("Masukkan nilai n: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Jumlah dari 1 sampai {n} adalah: {total}")