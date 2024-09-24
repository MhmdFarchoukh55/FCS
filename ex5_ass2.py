def strongPass(char):
    for i in char:
        if (len(char)>8):
            if(i in "1234567890"):
                if (i in "?!#$"):
                    return "strong pass"
        return "weak pass"
print(strongPass("uiaebnfie0?"))