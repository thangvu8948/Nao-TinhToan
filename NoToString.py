
def docChuSo(p):
    number = p
    if(number==1):
        return "1"
    elif (number ==2):
        return "2"
    elif (number==3):
        return "3"
    elif (number == 4):
        return "4"
    elif (number == 5):
        return "5"
    elif (number == 6):
        return "6"
    elif (number == 7):
        return "7"
    elif (number == 8):
        return "8"
    elif  (number == 9):
        return "9"
    elif (number == 0):
        return "0"
    return

def docSo( p ):
    strNum =''
    soLuong = len(p)
    soDao = 0
    number = int(p)
    if (number<0):
        strNum+="A"
        number = -number
        soLuong-=1
    while(number!=0):
        soDao = soDao * 10 + number % 10
        number = int(number / 10)
    if (soDao == 0):
        strNum+="0"
    while(soDao!=0):
        if ((soDao%10) == 1  and int(soDao%10)%10 == 0 and soLuong%3 == 2):
            strNum+="M"
            soLuong-=1
            soDao = int(soDao / 10)
        else:
            if ((soDao % 10) == 1 and soLuong % 3 == 2):
                strNum += "M"
                soLuong -= 1
                soDao = int(soDao / 10)
            if (soLuong %3 ==0):
                strNum += docChuSo(soDao % 10)
                strNum+="T"
            if (soLuong % 3 == 2 and soDao%10 != 0):
                strNum += docChuSo(soDao % 10)
                strNum+= "M"
            elif (soLuong % 3 == 2 and soDao % 10 == 0 and int(soDao/10)%10 == 0):
                strNum += ""
            elif(soLuong%3==2 and soDao%10==0):
                strNum+="L"
            if (soLuong % 3 == 1 and soDao%10 !=0):
                strNum+=docChuSo(soDao%10)
        if (soLuong == 10):
            strNum += "B"
        if (soLuong == 7):
            strNum += "M"
        if (soLuong == 4):
            strNum += "N"
        soLuong=soLuong-1
        soDao = int(soDao/10)
    return strNum

def docSoFull(p):
    number = float(p)
    nguyen = int(float(p))
    strNum = ''
    if (nguyen == number):
        strNum+=docSo(p)
        return strNum
    else:
        strNum+=docSo(str(nguyen))
        strNum+="P"
        temp = number - nguyen
        if (temp<0):
            temp = -temp
        temp = round(temp,3)
        while (temp!=int(temp)):
            temp = temp*10
        strNum+=docSo(str(int(temp)))
    return strNum


number = str(input("number: "))
print(docSoFull(number))