# def tim-uoc-chung-lon-nhat(a, b):
#     while b:
#         a, b = b, a % b
#     return a

# so-a = int(input("Nhập số a: "))
# so-b = int(input("Nhập số b: "))

# uoc-chung-lon-nhat = tim-uoc-chung-lon-nhat(so-a, so-b)

# print(f"Số chia lớn nhất của {so-a} và {so-b} là: {uoc-chung-lon-nhat}")
'''def chuyen-doi-nhi-phan-sang-thap-phan(nhi-phan-str):
    so-thap-phan = 0
    nhi-phan-str = nhi-phan-str[::-1]  # Đảo ngược chuỗi nhị phân để bắt đầu xử lý từ chữ số bên phải

    for i in range(len(nhi-phan-str)):
        if nhi-phan-str[i] == '1':
            so-thap-phan += 2 ** i

    return so-thap-phan

# Nhập số nhị phân từ người dùng
nhap-nhi-phan = input("Nhập số nhị phân: ")

# Kiểm tra xem đầu vào có phải là số nhị phân hợp lệ không
if set(nhap-nhi-phan) <= {'0', '1'}:
    ket-qua-thap-phan = chuyen-doi-nhi-phan-sang-thap-phan(nhap-nhi-phan)
    print(f"Số thập phân tương đương với {nhap-nhi-phan} là: {ket-qua-thap-phan}")
else:
    print("Lỗi: Vui lòng nhập một số nhị phân hợp lệ.")'''
# def decimal-to-binary(decimal-num):
#     binary-str = ''

#     if decimal-num == 0:
#         binary-str = '0'

#     while decimal-num > 0:
#         remainder = decimal-num % 2
#         binary-str = str(remainder) + binary-str
#         decimal-num = decimal-num // 2

#     return binary-str

# # Nhập số thập phân từ người dùng
# so-thap-phan = int(input("Nhập một số thập phân: "))

# ket-qua-nhi-phan = decimal-to-binary(so-thap-phan)
# print(f"Biểu diễn nhị phân của {so-thap-phan} là: {ket-qua-nhi-phan}")

'''import random
def coin-flip():
    # Generate a random number (0 or 1)
    result = random.randint(0, 1)
    
    # Return 'Heads' for 0, 'Tails' for 1
    return 'Heads' if result == 0 else 'Tails'

def simulate-coin-flips(num-flips):
    # Perform coin flips and count the occurrences of Heads and Tails
    heads-count = 0
    tails-count = 0
    
    for - in range(num-flips):
        result = coin-flip()
        if result == 'Heads':
            heads-count += 1
        else:
            tails-count += 1
    
    # Return the results
    return heads-count, tails-count
# Example: Simulate 100 coin flips
num-flips = 100
heads, tails = simulate-coin-flips(num-flips)
# Print the results
print(f"Heads: {heads}")
print(f"Tails: {tails}")
'''
# import random

# def simulate-coin-series():
#     consecutive-count = 0  # Count of consecutive heads or tails
#     flips-needed = 0       # Total flips needed to reach 3 consecutive outcomes

#     while consecutive-count < 3:
#         # Simulate a coin flip (0 for Heads, 1 for Tails)
#         result = random.randint(0, 1)
        
#         # Display the outcome
#         print('H' if result == 0 else 'T', end=' ')
        
#         # Update consecutive count
#         consecutive-count = consecutive-count + 1 if result == consecutive-result else 1

#         # Update the previous result for comparison
#         consecutive-result = result

#         # Increment total flips
#         flips-needed += 1

#     print(f"\nFlips needed to get 3 consecutive: {flips-needed}")
    
#     return flips-needed

# def main():
#     total-flips = 0
#     num-simulations = 10

#     for - in range(num-simulations):
#         total-flips += simulate-coin-series()

#     average-flips = total-flips / num-simulations
#     print(f"\nAverage number of flips needed: {average-flips:.2f}")

# if --name-- == "--main--":
#     main()
'''import random
def simulate-coin-series():
    consecutive-count = 0
    flips-needed = 0

    while consecutive-count < 3:
        result = random.choice(['H', 'T'])
        print(result, end=' ')
        
        if result == 'H':
            consecutive-count += 1
        else:
            consecutive-count = 0

        flips-needed += 1

    print(f"\nSố lần tung cần để có 3 liên tiếp: {flips-needed}")
    
    return flips-needed

def main():
    total-flips = 0
    num-simulations = 10

    for - in range(num-simulations):
        total-flips += simulate-coin-series()

    average-flips = total-flips / num-simulations
    print(f"\nSố lần tung trung bình cần: {average-flips:.2f}")

if --name-- == "--main--":
    main()'''
import random

def tim-gia-tri-lon-nhat():
    # Chọn một số nguyên ngẫu nhiên ban đầu từ 1 đến 100
    so-lon-nhat = random.randint(1, 100)
    cap-nhat = 0  # Đếm số lần cập nhật

    # Hiển thị số lớn nhất ban đầu
    print(f"Số Lớn Nhất Ban Đầu: {so-lon-nhat}")

    # Sinh thêm 99 số nguyên ngẫu nhiên
    for - in range(5):
        so-hien-tai = random.randint(1,100)

        # Kiểm tra nếu số hiện tại lớn hơn số lớn nhất đã gặp
        if so-hien-tai > so-lon-nhat:
            so-lon-nhat = so-hien-tai
            cap-nhat += 1
            print(f"{so-hien-tai} (Số Lớn Nhất Mới)")
        else:
            print(so-hien-tai)

    # Hiển thị số lớn nhất cuối cùng và số lần cập nhật
    print(f"\nSố Lớn Nhất Cuối Cùng: {so-lon-nhat}")
    print(f"Số Lần Cập Nhật: {cap-nhat}")

# Chạy chương trình
tim-gia-tri-lon-nhat()
