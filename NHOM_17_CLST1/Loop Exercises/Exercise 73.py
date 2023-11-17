string = input("Enter a string: ")
string-cleaned=""
for i in range(len(string)):
    char = string[i]
    if ( 'A'<=char<='Z'):
        string-cleaned+=str(chr(ord(char)+ord('a')-ord('A')))
    else:
        string-cleaned+=char
is-palindrome=True
left=0
right=len(string)-1
while left < right:
    if string[left] != string[right]:
        palindrome = False
        break
    left = left + 1
    right = right - 1
if is-palindrome==True:
    print(string,"is a palindrome.")
else:
    print(string,"is not a palindrome.")
