from IPython.display import clear_output
import random
import time
import winsound

pista = 120
cavalos = 6
pos = [0 for cavalo in range(cavalos)]

def atualiza(pos,pista):
    while True:
        yield pos
        pos[random.randint(0,len(pos)-1)] += random.randint(0,3)

def exibe(pos,pista):
    fundo = 41
    for y in range(len(pos)):
        if pos[y] == max(pos): cor = 30
        else: cor = 38
        print("\033[1;%s;%sm%s\033[0m" % (cor,fundo,str(' ' * (pista+3))))
        print("\033[1;%s;%sm%s\033[0m" % (cor,fundo,str(y+1) +  (' ' * pos[y]) +"0o"+  (' ' * (pista-pos[y]))))
        print("\033[1;%s;%sm%s\033[0m" % (cor,fundo,str(' ' * (pista+3))))
        fundo += 1

corrida = atualiza(pos,pista)

#winsound.PlaySound('C:\_kopp\Dropbox\Filipe\_github\FGV_Programming_Languages\Python\horse.wav', winsound.SND_FILENAME)

while max(pos) < pista:
    exibe(pos,pista)
    next(corrida)
    clear_output(True)
    time.sleep(0.03)
    winsound.PlaySound('C:\_kopp\Dropbox\Filipe\_github\FGV_Programming_Languages\Python\horse-gallop.wav', winsound.SND_FILENAME | winsound.SND_ASYNC)


winsound.PlaySound(None, winsound.SND_FILENAME)
