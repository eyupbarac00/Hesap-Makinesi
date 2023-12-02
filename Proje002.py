import  time

while True:

    sayi1 = float(input("ilk sayıyı girin\n= "))
    sayi2 = float(input("ikinci sayıyı girin\n= "))

    islem = input("yapmak istediğiniz işlemi belirtin lütfen\ntoplama +\nçıkarma -\nçarpma *\nbölme /\n= ")
    if islem == "+":
        print(sayi1 + sayi2)
    elif islem == "-":
        print(sayi1 - sayi2)
    elif islem == "*":
        print(sayi1 * sayi2)
    elif islem == "/":
        print(sayi1 / sayi2)
    else:
        print("Hatalı tuşlama!")
        time.sleep(3)
        exit()