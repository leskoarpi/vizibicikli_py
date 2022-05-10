import math
#2
class Kolcsonzes:
    #3
    def __init__(self,sor):
        nev,jazon,eora,eperc,vora,vperc = sor.strip().split(';')
        self.nev  =  str(nev)
        self.jazon  = str(jazon)
        self.eora  =  int(eora)
        self.eperc  =  int(eperc)
        self.vora  =  int(vora)
        self.vperc  =  int(vperc)
        
#4
with open('kolcsonzesek.txt', encoding=('utf-8')) as f:
    fejlec = f.readline()
    lista = [Kolcsonzes(sor) for sor in f]
#5
print(f'5. feladat: Napi kölcsönzések száma: {len(lista)}')
#6
nevbe = input('6. feladat: Kérek egy nevet: ')
volt=False
print(f'\t{nevbe} kölcsönzései:')
for sor in lista:
    if sor.nev == nevbe:
        print(f'\t{sor.eora}:{sor.eperc}-{sor.vora}:{sor.vperc}')
        volt= True
if volt == False:
    print(f'Nem volt ilyen nevü kölcsönző!')

#7
idobe = input('7. feladat: Adjon meg egy időpontot óra:perc alakban: ')
fuu = idobe.strip().split(':')
print(f'\t A vizen lévő Járművek:')
for sor in lista:
    el = (sor.eora * 60) + sor.eperc
    vissza = (sor.vora * 60) + sor.vperc
    bekert = (int(fuu[0]) * 60) + int(fuu[1])
    
    if el <= bekert and vissza >= bekert:
        print(f'\t {"{:02d}".format(sor.eora)}:{"{:02d}".format(sor.eperc)}-{"{:02d}".format(sor.vora)}:{"{:02d}".format(sor.vperc)} : {sor.nev}')

#8
bevetel = 0
for sor in lista:
    ossz = (sor.vora-sor.eora)*60 + (sor.vperc-sor.eperc)
    bevetel += math.ceil(ossz/30) * 2400

print(f'8. feladat: A napi bevétel: {bevetel} Ft')

#9
with open('F.txt', 'w' , encoding='utf-8')as w:
    for sor in lista:
        if sor.jazon == 'F':
            w.write(f'{"{:02d}".format(sor.eora)}:{"{:02d}".format(sor.eperc)}-{"{:02d}".format(sor.vora)}:{"{:02d}".format(sor.vperc)} : {sor.nev}\n')
#10

szotar = {}
for i in lista:
    szotar[i.jazon]=szotar.get(i.jazon,0)+1

szotar_items = szotar.items()
rendezett = sorted(szotar_items)
for i in rendezett:
    print(f'{i[0]} - {i[1]}')