import requests
import json

############# G1 ####################################
### https://falkor-cda.bastian.globo.com/feeds/b904b430-123a-4f93-8cf4-5365adf97892/posts/page/1
### https://comentarios.globo.com/comentarios/%40%40jornalismo%40%40g1%40%40sp%40%40sao-paulo/multi-content%40%40318d2ab0-78da-4152-9d6a-c519e29f3a07/https%3A%40%40%40%40g1.globo.com%40%40sp%40%40sao-paulo%40%40noticia%40%40pf-indicia-haddad-por-caixa-2-em-campanha-para-a-prefeitura-de-sp.ghtml/shorturl/PF%20indicia%20Haddad%20por%20usar%20caixa%202%20em%20campanha%20para%20a%20Prefeitura%20de%20S%C3%A3o%20Paulo/1.json
### facebook.com/profile.php?id=
### https://graph.facebook.com/v2.7/1507833879263297/picture
### https://graph.facebook.com/100000632217856/picture?type=large&redirect=false
### http://graph.facebook.com/100000632217856/picture?width=200&height=600


lista = []
for num in range(1,2):
    url = 'http://falkor-cda.bastian.globo.com/feeds/b904b430-123a-4f93-8cf4-5365adf97892/posts/page/'+str(num)
    pagina = requests.get(url)
    x = json.loads(pagina.text)
    #print(x['items'][0])
    for y in x['items']:
        try: data = str(y['publication'][:19]).replace("T"," ")
        except: data = ''
        try: link = str(y['content']['url'])
        except: link = ''
        try: imagem = str(y['content']['image']['url'])
        except: imagem = ''
        lista.append([data,link,imagem])

#for noti in lista:   
    #print(noti)
