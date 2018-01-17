import numpy 
from numpy.random import randint as rand
import matplotlib.pyplot as plt

def maze(width=81, height=81):
    shape = ((height // 2) * 2 + 1, (width // 2) * 2 + 1)
    complexity, density = int(shape[0] + shape[1]) , int(shape[0] // 2) * (shape[1] // 2)
    Z = numpy.zeros(shape , dtype=int)
    Z[0, :] = Z[-1, :] =  Z[:, 0] = Z[:, -1] = 200
    for i in range(density):
        x, y = rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
        Z[y, x] = 200
        for j in range(complexity):
            neighbours = []
            if x > 1:             neighbours.append((y, x - 2))
            if x < shape[1] - 2:  neighbours.append((y, x + 2))
            if y > 1:             neighbours.append((y - 2, x))
            if y < shape[0] - 2:  neighbours.append((y + 2, x))
            if len(neighbours):
                a,b = neighbours[rand(0, len(neighbours) - 1)]
                if Z[a, b] == 0:
                    Z[a, b] = Z[a + (y - a) // 2, b + (x - b) // 2] = 200
                    x, y = b, a
    return Z

m = maze(17,17)

while m.any() != 98:
    a,b = rand(0, m.shape[1]), rand(0, m.shape[0] )
    if m[a,b] == 0:
        m[a,b] = 98
        break

while m.any() != 99:
    c,d = rand(0, m.shape[1]), rand(0, m.shape[0] )
    if m[c,d] == 0:
        m[c,d] = 99
        break

mm = m.copy()

def vizinho(m,a,b):
    return [m[a-1,b],m[a,b-1],m[a,b+1],m[a+1,b]]

itc = 10000
def move(m,a,b,resposta=[]):
    global itc
    global resposta_fim
    if itc > 0:
        itc -= 1
        resposta.append([a,b])
    else:
        return m,resposta
    if 99 in vizinho(m,a,b):
        print("solução encontrada")
        #print(resposta)
        resposta_fim = resposta
        return m,resposta
    else:
        minimo = min(vizinho(m,a,b))
        proximo = vizinho(m,a,b).index(minimo)
        #print(vizinho(m,a,b),minimo,proximo)
        if minimo < 98:
            if proximo == 0:
                m[a-1,b] = max(40,m[a-1,b]+1)
                move(m,a-1,b)
            if proximo == 1:
                m[a,b-1] = max(40,m[a,b-1]+1)
                move(m,a,b-1)
            if proximo == 2:
                m[a,b+1] = max(40,m[a,b+1]+1)
                move(m,a,b+1)
            if proximo == 3:
                m[a+1,b] = max(40,m[a+1,b]+1)
                move(m,a+1,b)

            
            
m2 = move(m,a,b)


fig, ax = plt.subplots(figsize = (10,10))
ax.matshow(m, cmap=plt.cm.Blues)
#ax.grid(color='b', linestyle='-', linewidth=1)
plt.xticks([]), plt.yticks([])
plt.show()


for casa in range(len(resposta_fim)):
    for visita in range(len(resposta_fim)-1,casa,-1):
        if resposta_fim[casa] == resposta_fim[visita]:
            resposta_fim = resposta_fim[:casa] + resposta_fim[visita:]
            break

for x in resposta_fim:
    mm[x[0],x[1]]=50

fig, ax = plt.subplots(figsize = (10,10))
ax.matshow(mm, cmap=plt.cm.Blues)
#ax.grid(color='b', linestyle='-', linewidth=1)
plt.xticks([]), plt.yticks([])
plt.show()
