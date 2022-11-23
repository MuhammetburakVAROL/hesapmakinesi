print("Hesap makinesini kapatmak için x tuşuna basınız.")

while True:
    sayi = int(input("Birinci sayıyı giriniz: "))
    sayi2 =int(input("İkinci sayıyı giriniz: "))
    islemSecim = input("Bir İslem Seciniz (+ - / .): ")

    if islemSecim == '+':
        print(sayi, '+',sayi2,"=",sayi+sayi2)

    elif islemSecim == '-':
        print(sayi,'-',sayi2,"=",sayi-sayi2)

    elif islemSecim == '/':
        print(sayi,'/',sayi2,"=",sayi/sayi2)

    elif islemSecim == '.':
        print(sayi,'.',sayi2,"=",sayi*sayi2)

    else:
        print("Yanlış Tuşlama Yaptınız !!!")
    kapat = input("Hesap makinesini kapatmak için x tuşuna devam etmek için d tuşuna basınız.")
    if kapat == "x":
        print("Hesap makinesi kapanıyor..." )
        break

