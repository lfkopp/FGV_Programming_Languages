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

m = maze(51,31)  # tamanho do maze

while m.any() != 98:
    a,b = rand(1, m.shape[0]-1), rand(1, m.shape[1]-1)
    if m[a,b] == 0:
        m[a,b] = 98
        break
        
while m.any() != 99:
    c,d = rand(1, m.shape[0]-1), rand(1, m.shape[1]-1)
    if m[c,d] == 0:
        m[c,d] = 99
        break
        
def vizinho(m,a,b):
    return [m[a-1,b],m[a,b-1],m[a,b+1],m[a+1,b]]

def zeros(l):
    result = []
    for index, item in enumerate(l):
        if item == 0: result.append(index)
    return result

resposta_fim = []

def move(m,a,b,resultado):
    global itc
    itc = 100000
    global resposta_fim
    if itc > 0:
        if 99 in vizinho(m,a,b):
            if resposta_fim == [] or len(resultado)<len(resposta_fim):
                resposta_fim = resultado.copy()
                #print(resultado)
                return m,resposta_fim
        else:
            proximo = zeros(vizinho(m,a,b))
            itc -= 1
            if len(proximo) > 0:
                if 0 in proximo:
                    mm = m.copy()
                    mm[a-1,b] = max(40,m[a-1,b]+1)
                    r = resultado.copy()
                    r.append([a-1,b])
                    if len(resposta_fim) == 0 or len(r) < len(resposta_fim): move(mm,a-1,b,r)
                if 1 in proximo:
                    mm = m.copy()
                    mm[a,b-1] = max(40,m[a,b-1]+1)
                    r = resultado.copy()
                    r.append([a,b-1])
                    if len(resposta_fim) == 0 or len(r) < len(resposta_fim): move(mm,a,b-1,r)
                if 2 in proximo:
                    mm = m.copy()
                    mm[a,b+1] = max(40,mm[a,b+1]+1)
                    r = resultado.copy()
                    r.append([a,b+1])
                    if len(resposta_fim) == 0 or len(r) < len(resposta_fim): move(mm,a,b+1,r)
                if 3 in proximo:
                    mm = m.copy()
                    mm[a+1,b] = max(40,mm[a+1,b]+1)
                    r = resultado.copy()
                    r.append([a+1,b])
                    if len(resposta_fim) == 0 or len(r) < len(resposta_fim): move(mm,a+1,b,r)

move(m,a,b,[])

if len(resposta_fim)>0:
    for c in resposta_fim:
        m[c[0]][c[1]] = 40
else:
    print("não encontrada solução com " + str(itc) + " iterações")

fig, ax = plt.subplots(figsize = (15,10))
ax.matshow(m, cmap=plt.cm.Blues)
plt.xticks([]), plt.yticks([])
plt.show()
