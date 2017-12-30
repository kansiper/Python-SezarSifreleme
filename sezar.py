def sezar(metin):
    sifre = ""
    alfabe=['a','b' ,'c' , 'd', 'e', 'f', 'g' ,'h' ,'i' ,'j','k' ,'l' ,'m' ,'n' ,'o' ,'p' ,'r' ,'s' ,'t' ,'u' ,'v', 'y' ,'z']
    for i in metin:
        sifre+=alfabe[(alfabe.index(i)+3)%len(alfabe)]
    print("sifre :",sifre)
    return metin

isim = raw_input("metini giriniz : ")
sezar(isim)

