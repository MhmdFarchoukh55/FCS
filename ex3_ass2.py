def reverseString(phrase):
    char=""
    for i in range(1,len(phrase)):
        char=char+phrase[-i]
    return char
print(reverseString("hello world"))