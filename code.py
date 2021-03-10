Coding:

def class1(str1): 
    ip=int(str1[0])
    if (ip >=1 and ip <= 126):
        return 'Class A'
    elif (ip >= 128 and ip <= 191):
        return 'Class B'
    elif (ip >= 192 and ip <= 223):
        return 'Class C'
    elif (ip >= 224 and ip <= 239):
        return 'Class D'
    else:
        return 'Class E'
str1 = list(input().split('.'))
print(class1(str1))
