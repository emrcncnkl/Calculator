print('''
 ___  ___  _______   ________  ________  ________        _____ ______   ________  ___  __    ___  ________   _______   ________  ___     
|\  \|\  \|\  ___ \ |\   ____\|\   __  \|\   __  \      |\   _ \  _   \|\   __  \|\  \|\  \ |\  \|\   ___  \|\  ___ \ |\   ____\|\  \    
\ \  \\\  \ \   __/|\ \  \___|\ \  \|\  \ \  \|\  \     \ \  \\\__\ \  \ \  \|\  \ \  \/  /|\ \  \ \  \\ \  \ \   __/|\ \  \___|\ \  \   
 \ \   __  \ \  \_|/_\ \_____  \ \   __  \ \   ____\     \ \  \\|__| \  \ \   __  \ \   ___  \ \  \ \  \\ \  \ \  \_|/_\ \_____  \ \  \  
  \ \  \ \  \ \  \_|\ \|____|\  \ \  \ \  \ \  \___|      \ \  \    \ \  \ \  \ \  \ \  \\ \  \ \  \ \  \\ \  \ \  \_|\ \|____|\  \ \  \ 
   \ \__\ \__\ \_______\____\_\  \ \__\ \__\ \__\          \ \__\    \ \__\ \__\ \__\ \__\\ \__\ \__\ \__\\ \__\ \_______\____\_\  \ \__\
    \|__|\|__|\|_______|\_________\|__|\|__|\|__|           \|__|     \|__|\|__|\|__|\|__| \|__|\|__|\|__| \|__|\|_______|\_________\|__|
                       \|_________|                                                                                      \|_________|    
                                                                                                                                         
                                                                                                                                         
''')

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    return x / y

hesaplamaya_devam = "e"

while hesaplamaya_devam == "e":
    num1 = int(input("Birinci sayıyı girin: "))
    num2 = int(input("İkinci sayıyı girin: "))
    islem = input("Yapmak istediğiniz işlemi girin (+, -, *, /): ")

    if islem == '+':
        sonuc = toplama(num1, num2)
    elif islem == '-':
        sonuc = cikarma(num1, num2)
    elif islem == '*':
        sonuc = carpma(num1, num2)
    elif islem == '/':
        sonuc = bolme(num1, num2)

    print("Sonuç: ", sonuc)

    hesaplamaya_devam = input("Başka bir hesaplama yapmak ister misiniz? (e/h): ")
    hesaplamaya_devam = hesaplamaya_devam.lower()