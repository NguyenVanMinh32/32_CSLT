# # Dictionary của tần số của các nốt âm cho oktav thứ tư (C4 đến B4)
# tần_số_các_nốt = {
#     'C': 261.63,
#     'D': 293.66,
#     'E': 329.63,
#     'F': 349.23,
#     'G': 392.00,
#     'A': 440.00,
#     'B': 493.88
# }

# # Nhập tên của nốt âm từ người dùng
# nốt_âm = input('Nhập tên của nốt âm (Ví dụ: C4, D4, E4, vv.): ')[:2]

# # Trích xuất thông tin về nốt âm và oktav từ dữ liệu đầu vào
# tên_nốt_âm = nốt_âm[0]  # Trích xuất tên của nốt âm (Ví dụ: 'C')
# oktav = int(nốt_âm[1])  # Trích xuất số oktav (Ví dụ: 4)

# # Kiểm tra xem nốt âm có trong từ điển không
# if tên_nốt_âm in tần_số_các_nốt:
#     # Tính tần số bằng cách lấy tần số của nốt tương ứng ở oktav thứ tư
#     # và chia cho 2 ^ (4 _ oktav)
#     tần_số = tần_số_các_nốt[tên_nốt_âm] / (2 ** (4 _ oktav))
#     print(f'Tần số của {nốt_âm} là {tần_số} Hz.')
# else:
#     print('Nốt âm không tồn tại trong từ điển.')
string = "Hello"
char_at_index_1 = string[1]  
print(char_at_index_1)

