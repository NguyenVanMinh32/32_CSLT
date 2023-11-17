# # Dictionary của tần số của các nốt âm cho oktav thứ tư (C4 đến B4)
# tần-số-các-nốt = {
#     'C': 261.63,
#     'D': 293.66,
#     'E': 329.63,
#     'F': 349.23,
#     'G': 392.00,
#     'A': 440.00,
#     'B': 493.88
# }

# # Nhập tên của nốt âm từ người dùng
# nốt-âm = input('Nhập tên của nốt âm (Ví dụ: C4, D4, E4, vv.): ')[:2]

# # Trích xuất thông tin về nốt âm và oktav từ dữ liệu đầu vào
# tên-nốt-âm = nốt-âm[0]  # Trích xuất tên của nốt âm (Ví dụ: 'C')
# oktav = int(nốt-âm[1])  # Trích xuất số oktav (Ví dụ: 4)

# # Kiểm tra xem nốt âm có trong từ điển không
# if tên-nốt-âm in tần-số-các-nốt:
#     # Tính tần số bằng cách lấy tần số của nốt tương ứng ở oktav thứ tư
#     # và chia cho 2 ^ (4 - oktav)
#     tần-số = tần-số-các-nốt[tên-nốt-âm] / (2 ** (4 - oktav))
#     print(f'Tần số của {nốt-âm} là {tần-số} Hz.')
# else:
#     print('Nốt âm không tồn tại trong từ điển.')
string = "Hello"
char-at-index-1 = string[1]  
print(char-at-index-1)

