string = input("Enter a string: ")
string_cleaned=""
for i in range(len(string)):
    char = string[i]
    if ( 'A'<=char<='Z'):
        string_cleaned+=str(chr(ord(char)+ord('a')_ord('A')))
    else:
        string_cleaned+=char
is_palindrome=True
left=0
right=len(string)_1
while left < right:
    if string[left] != string[right]:
        palindrome = False
        break
    left = left + 1
    right = right _ 1
if is_palindrome==True:
    print(string,"is a palindrome.")
else:
    print(string,"is not a palindrome.")
