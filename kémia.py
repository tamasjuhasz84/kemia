#Év;Elem;Vegyjel;Rendszám;Felfedező
# 0   1     2      3           4
#Ókor;Arany;Au;79;Ismeretlen

with open ("felfedezesek.csv", 'r', encoding='latin2') as f:
    fejléc = f.readline()
    matrix = list()
    for i in f:
        matrix.append( i.strip().split(';') )

print(f' 3. feladat: Elemek száma: {len(matrix)}')

i = 0
for sor in matrix:
    if sor[0] == 'Ókor':
        i += 1
print(f' 4. feladat: Felfedezések száma az ókorban: {i}')

def betü(x):
    return 'a' <= x <= 'z' or 'A' <= x <= 'Z'

while True:
    a = input('Kérek egy vegyjelet:')
    if len(a) == 1:
        if betü(a):
            break
    elif len(a) == 2:
        if betü(a[0]) and betü(a[1]):
            break


    
        
        
    
    


