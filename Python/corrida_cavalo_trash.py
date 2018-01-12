from IPython.display import clear_output
import random


pos = [0 for x in range(10)]
#print(pos)

def espaca(x):
    caminho = '.'
    for i in range(x):
        caminho += '.'
    return caminho
    
while True:
    for y in range(10):
        print(espaca(pos[y]),y+1)
    pos[random.randint(0,9)] += 1
    if max(pos)>20: break
        
    clear_output(wait=1)

print(pos)
