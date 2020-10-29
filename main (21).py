import random
hraci = ['mane 90','salah 90','firminho 88','wijnaldum 85','henderson 85','fabinho 86','robertson 86','vandijk 91','gomez 82',
'trent 85','alisson 90','keita 82','shaq 81','williams 64','van den berg 66','minamino 77','lallana 78','lovren 80','origi 78',
'adrian 76','matip 83','oxlade 80','milner 81','glatzel 60','larouci 60','jones 65','kelleher 61','clyne 76','lewis 60',
'chirivella 66','lonergan 65','hoever 62','elliot 64']
vladko = []
adam = []
c = 1
d = 1
while len(hraci) > 0:
    a = random.choice(hraci)
    if len(vladko) < len(adam):
        vladko.append(a)
    else:
        adam.append(a)
    
    hraci.remove(a)

print('VLADKO')    
for _ in vladko:
    print('{}. hrac: '.format(c),_)
    c += 1

print()    

print('ADAM')
for _ in adam:
    print('{}. hrac: '.format(d),_)
    d += 1