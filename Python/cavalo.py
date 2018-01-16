from IPython.display import clear_output
import random
import time

import winsound


pista = 120
cavalos = 8
cor = 1
pos = [0 for x in range(cavalos)]
for y in range(cavalos):
    print("\033[1;%s;%sm%s\033[0m" % (cor,40+y,str(' ' * (pista+3))))
    print("\033[1;%s;%sm%s\033[0m" % (cor,40+y,str(y+1) +  (' ' * pos[y]) +"0o"+  (' ' * (pista-pos[y]))))
    print("\033[1;%s;%sm%s\033[0m" % (cor,40+y,str(' ' * (pista+3))))


winsound.PlaySound('C:\_kopp\Dropbox\Filipe\_github\FGV_Programming_Languages\Python\horse.wav', winsound.SND_FILENAME)


while max(pos)<pista:
    clear_output(True)
    pos[random.randint(0,cavalos-1)] += min(pista-3,random.randint(0,3))
    for y in range(cavalos):
        if pos[y]==max(pos):
            cor = 31
            ganhador = y+1
        else:
            cor = 32
        print("\033[1;%s;%sm%s\033[0m" % (cor,40+y,str(' ' * (pista+3))))
        print("\033[1;%s;%sm%s\033[0m" % (cor,40+y,str(y+1) +  (' ' * pos[y]) +"0o"+  (' ' * (pista-pos[y]))))
        print("\033[1;%s;%sm%s\033[0m" % (cor,40+y,str(' ' * (pista+3))))
    time.sleep(0.05)
   
    
print("o ganhador foi o cavalo " + str(ganhador))