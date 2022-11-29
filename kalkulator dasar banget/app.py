def add(a, b):
    answer = a + b 
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")
    
def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")
    
def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True: 
    print("a, penambahan")
    print("b, pengurangan")
    print("c, perkalian")
    print("d, pembagian")
    print("e, keluar") 

    choice = input("masukkan pilihan: ")   

    if choice == "a" or choice == "A":
        print("Penambahan")
        a = int(input("masukkan angka pertama disini:"))
        b = int(input("masukkan angka kedua disini:"))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Pengurangan")
        a = int(input("masukkan angka pertama disini:"))
        b = int(input("masukkan angka kedua disini:"))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Perkalian")
        a = int(input("masukkan angka pertama disini:"))
        b = int(input("masukkan angka kedua disini:"))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Pembagian")
        a = int(input("masukkan angka pertama disini:"))
        b = int(input("masukkan angka kedua disini:"))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("selesai")
        quit()