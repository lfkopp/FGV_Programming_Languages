def pali(y1,y2):
    maior=0
    for a in range(y1,y2,-1):
        for b in range(y1,a-1,-1):
            if str(a*b) == str(a*b)[::-1] and a*b > maior: cand1,cand2,maior = a,b,a*b 
            elif a*b < maior: break
    return cand1,cand2,maior     
print(pali(99999,10000))
            
