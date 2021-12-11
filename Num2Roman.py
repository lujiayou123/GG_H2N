def Num2Roman(num):
    v1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    v2 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    v3 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    v4 = ['', 'M', 'MM', 'MMM']
    try:
        num = 12
        num1 = v4[num // 1000] + v3[num % 1000 // 100] + v2[num % 100 // 10] + v1[num % 10]
        ret = " {} ".format(num1)
    except Exception as e:
        print("请输入正确的数字")
    return ret

if __name__ == '__main__':
    num = 13
    print(Num2Roman(num))