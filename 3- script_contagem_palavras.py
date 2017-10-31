# -*- coding: utf-8 -*-

#Contando as palavras no corpus geral
import codecs
from ftfy import fix_text
from collections import Counter

##Script para contar as palavras, atribuindo a frequencia no corpus geral,
##no corpus escrito e no corpus falado

#Abrindo os arquivos todos, gerando uma variável chamada tokens, que é uma
#lista contendo todos as palavras do corpus com split.

#Abrindo o corpus escrito
escrito = codecs.open('Corpus_Escrito.txt','r','utf-8')
corpus_escrito = escrito.readlines()
escrito.close()

#Abrindo o corpus oral
oral = codecs.open('Corpus_Oral.txt','r','utf-8')
corpus_oral = oral.readlines()
oral.close()

#Variavel com o corpus inteiro
tokens =  corpus_escrito + corpus_oral

#Estocando os types

types = set(tokens)
print len (types)


#Fazendo um contador que não seja estúpido

with codecs.open('Contagem_palavras.txt','w','utf8') as arquivo:
    histograma = Counter(tokens).most_common(len(types))
    for item in histograma:
        uni =(unicode(item[0].strip('\n')) + u'\t' + unicode(item[1]) + u'\n')
        arquivo.write((uni))


with codecs.open('Contagem_palavras_Escrita.txt','w','utf8') as arquivo:
    histograma = Counter(corpus_escrito).most_common(len(types))
    for item in histograma:
        uni =(unicode(item[0].strip('\n')) + u'\t' + unicode(item[1]) + u'\n')
        arquivo.write((uni))


with codecs.open('Contagem_palavras_Oral.txt','w','utf8') as arquivo:
    histograma = Counter(corpus_oral).most_common(len(types))
    for item in histograma:
        uni =(unicode(item[0].strip('\n')) + u'\t' + unicode(item[1]) + u'\n')
        arquivo.write((uni))
