from IPython.display import clear_output
import random
import time


pista = 50
cavalos = 8
pos = [0 for x in range(cavalos)]

def espaca(x):
    caminho = ' '
    for i in range(x):
        caminho += ' '
    return caminho
    
while max(pos)<pista:
    pos[random.randint(0,cavalos-1)] += 1
    for y in range(cavalos):
        if pos[y]==max(pos):
            cor = 31
            ganhador = y+1
        else:
            cor = 32
        print("\033[1;%s;%sm%s\033[0m" % (cor,40+y,str(y+1) + k + espaca(pos[y])+"0o"+ espaca(pista-pos[y])))
    time.sleep(0.05)
    clear_output(True)
    
print("o ganhador foi o cavalo " + str(ganhador))
