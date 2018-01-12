from bs4 import BeautifulSoup
import requests, string
from collections import Counter
import operator

urls = ['http://www.oglobo.com.br', 'http://www.estadao.com.br', 'http://www.odia.com.br', 'https://www.folha.uol.com.br/']
limpo2 = []

for url in urls:
    pagina = requests.get(url)
    texto = pagina.text
    soup = BeautifulSoup(texto, 'lxml')
    limpo = soup.get_text()
    limpo = limpo.replace('\n',' ').replace('\t',' ').split()
    limpo = [x.strip(string.punctuation) for x in limpo if len(x)>3]
    limpo2 = limpo2 + limpo
dic = Counter(limpo2)
sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
sorted_dic
