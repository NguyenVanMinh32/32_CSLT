def tim_uoc_chung_lon_nhat(a, b):
    while b:
        a, b = b, a % b
    return a

so_a = int(input("Nhập số a: "))
so_b = int(input("Nhập số b: "))

uoc_chung_lon_nhat = tim_uoc_chung_lon_nhat(so_a, so_b)

print(f"Số chia lớn nhất của {so_a} và {so_b} là: {uoc_chung_lon_nhat}")

