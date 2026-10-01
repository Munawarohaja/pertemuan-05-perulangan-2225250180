print("=== PROGRAM KUIS 2: DERET ARITMETIKA ===")
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))
n = int(input("Banyak suku n: "))
while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))
total = 0
print("\n--- Hasil Suku Deret ---")
for i in range(n):
    suku = a + (i * d)
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")
print("-" * 25)
print(f"Jumlah seluruh suku (Total): {total:.2f}")