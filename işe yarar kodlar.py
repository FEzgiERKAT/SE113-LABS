#KOD-1 bu kodda verilen iki basamaklı sayının okunuşunu yazıyorsun.

birler=["","Bir","iki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar=["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
def okunus(sayi):
    birlericin=sayi%10
    onlaricin=sayi//10
    return onlar[onlaricin]+ " " + birler[birlericin]

sayi=int(input("iki basamaklı bir sayı giriniz..."))
print(okunus(sayi))


#KOD-2  pisgor üçgenlerini bulma kodu
def pisagor_bulma() :
    liste=list()
    for a in range(1,101):
        for b in range(1,101):
            c=((a**2)+(b**2))**(1/2)
            if c==int(c):
                liste.append((a,b,int(c)))
    return liste

for i in pisagor_bulma():
    print(i)


#KOD-3


