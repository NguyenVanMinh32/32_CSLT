# def tim_uoc_chung_lon_nhat(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# so_a = int(input("Nhập số a: "))
# so_b = int(input("Nhập số b: "))

# uoc_chung_lon_nhat = tim_uoc_chung_lon_nhat(so_a, so_b)

# print(f"Số chia lớn nhất của {so_a} và {so_b} là: {uoc_chung_lon_nhat}")
'''def chuyen_doi_nhi_phan_sang_thap_phan(nhi_phan_str):
    so_thap_phan = 0
    nhi_phan_str = nhi_phan_str[::-1]  # Đảo ngược chuỗi nhị phân để bắt đầu xử lý từ chữ số bên phải

    for i in range(len(nhi_phan_str)):
        if nhi_phan_str[i] == '1':
            so_thap_phan += 2 ** i

    return so_thap_phan

# Nhập số nhị phân từ người dùng
nhap_nhi_phan = input("Nhập số nhị phân: ")

# Kiểm tra xem đầu vào có phải là số nhị phân hợp lệ không
if set(nhap_nhi_phan) <= {'0', '1'}:
    ket_qua_thap_phan = chuyen_doi_nhi_phan_sang_thap_phan(nhap_nhi_phan)
    print(f"Số thập phân tương đương với {nhap_nhi_phan} là: {ket_qua_thap_phan}")
else:
    print("Lỗi: Vui lòng nhập một số nhị phân hợp lệ.")'''
def decimal_to_binary(decimal_num):
    binary_str = ''

    if decimal_num == 0:
        binary_str = '0'

    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_str = str(remainder) + binary_str
        decimal_num = decimal_num // 2

    return binary_str

# Nhập số thập phân từ người dùng
so_thap_phan = int(input("Nhập một số thập phân: "))

ket_qua_nhi_phan = decimal_to_binary(so_thap_phan)
print(f"Biểu diễn nhị phân của {so_thap_phan} là: {ket_qua_nhi_phan}")

