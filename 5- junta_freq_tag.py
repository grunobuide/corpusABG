### JUNTANDO AS INFORMAÇÕES DE FREQUÊNCIA COM O POS-TAGGING ###

import codecs

#Abrindo o arquivo com as palavras taggeadas
arquivo = codecs.open('Corpus_Total_limpo.txt','r','utf8')

corpus_tag = arquivo.read().split(u'\r')
corpus_taggeado = []
for item in corpus_tag:
    corpus_taggeado.append(item.split(u'\t'))

arquivo.close()
#Lista de listas, cada item é uma linha do corpus, no formato:

    # Palavra, Categoria, Lema



#Abrindo o arquivo com as frequências

arquivo2 = codecs.open('Contagem_palavras.txt','r','utf8')

contagem = arquivo2.read().split(u'\n')
corpus_freq = []
for item in contagem:
    corpus_freq.append(item.split(u'\t'))

arquivo2.close()
#Lista de listas, cada item é uma linha do corpus, no formato:

    # Palavra, Frequencia

#Abrindo o arquivo com as frequências orais

arquivo3 = codecs.open('Contagem_palavras_Oral.txt','r','utf8')

contagem_oral = arquivo3.read().split(u'\n')
corpus_freq_oral = []
for item in contagem_oral:
    corpus_freq_oral.append(item.split(u'\t'))

arquivo3.close()

#Abrindo o arquivo com as frequências escritas
arquivo4 = codecs.open('Contagem_palavras_Escrita.txt','r','utf8')

contagem_escrita = arquivo4.read().split(u'\n')
corpus_freq_escrita = []
for item in contagem_escrita:
    corpus_freq_escrita.append(item.split(u'\t'))

arquivo4.close()


#Vou transformar tudo em dicionário e organizar assim

dic_tag = {}
for item in corpus_taggeado:
    dic_tag[item[0]] = item[1:]
# palavra : [categoria, lema]

dic_freq = {}
for item in corpus_freq:
    if len(item) < 2:
        pass
    else:
        dic_freq[item[0]] = item[1]
# palavra: [frequencia geral]

dic_freq_oral = {}
for item in corpus_freq_oral:
    if len(item) < 2:
        pass
    else:
        dic_freq_oral[item[0]] = item[1]
# palavra: [frequencia oral]

dic_freq_escrita = {}
for item in corpus_freq_escrita:
    if len(item) < 2:
        pass
    else:
        dic_freq_escrita[item[0]] = item[1]
# palavra: [frequencia escrita]

## ARQUIVO DE DESTINO, PARTINDO DE UM DICIONARIO DESTINO, INFOS SALVAS DO SEGUINTE MODO

    #palavra: [categoria, lema, freq_geral, freq_oral, freq_escrita]

dic_destino ={}
with codecs.open('Corpus_Tag_Freq.txt','w','utf8') as destino:
    for item in dic_tag.keys():
        #começa como uma cópia do dicionário tag
        dic_destino[item] = dic_tag[item]
        if dic_freq.has_key(item): #se o item tiver uma frequencia geral, copia
            dic_destino[item].append(dic_freq[item])
        else: #senão, preenche com 0g
            dic_destino[item].append('0g')
        if dic_freq_oral.has_key(item):#se tiver freq oral, copia
            dic_destino[item].append(dic_freq_oral[item])
        else:
            dic_destino[item].append('0o')
        if dic_freq_escrita.has_key(item):
            dic_destino[item].append(dic_freq_escrita[item])
        else:
            dic_destino[item].append('0e')
            
    for item in dic_destino.keys():
        uni = unicode(item) + u'\t'
        for freq in dic_destino[item]:
            uni += unicode(freq) + u'\t'
        uni += '\n'
        destino.write(uni)
