import random

hraci = ['mane 90','salah 90','firminho 88','wijnaldum 85','henderson 85','fabinho 86','robertson 86','vandijk 91','gomez 82',
'trent 85','alisson 90','keita 82','shaq 81','williams 64','van_den_berg 66','minamino 77','lallana 78','lovren 80','origi 78',
'adrian 76','matip 83','oxlade 80','milner 81','glatzel 60','larouci 60','jones 65','kelleher 61','clyne 76','lewis 60',
'chirivella 66','lonergan 65','hoever 62','elliot 64']

vladko = []
adam = []
vladko_res = []
adam_res = []

def the_sorter(value: tuple):
    return value[1]

c = 1
d = 1
while len(hraci) > 0:
    a = random.choice(hraci)
    if len(vladko) < len(adam):
        vladko.append(a)
    else:
        adam.append(a)
    
    hraci.remove(a)

for ind in vladko:
    vladko_res.append(ind.split(' '))

for inx in adam:
    adam_res.append(inx.split(' '))
    
y = sorted(vladko_res, key=the_sorter, reverse = True)
z = sorted(adam_res, key=the_sorter, reverse = True)

print('VLADKO')
for vl in y:
    print('{}. hráč je: '.format(c),vl[0],'-',vl[1])
    c += 1
    
print()
    
print('ADAM')
for ad in z:
    print('{}. hráč je: '.format(d),ad[0],'-',ad[1])
    d += 1
