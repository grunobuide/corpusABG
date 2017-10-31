### Concatenando os corpora escritos em um único arquivo ###

import codecs


## Folha ##

folha = codecs.open("Palavras_Folha_limpa.txt",'rU','utf8')
pal_folha2 = folha.read().split(u'\n')
pal_folha = []
for item in pal_folha2:
    pal_folha.append(item.strip('\r'))
folha.close()

## EstadÃ£o ##

estadao = codecs.open("Palavras_Estadao_limpa.txt", 'rU','utf8')
pal_estadao2 = estadao.read().strip('\r').split(u'\n')
pal_estadao = []
for item in pal_estadao2:
    pal_estadao.append(item.strip('\r'))
estadao.close()

## Artigos ##

artigos = codecs.open("Palavras_Artigos_limpa.txt", 'rU','utf8')
pal_artigos2 = artigos.read().strip('\r').split(u'\n')
pal_artigos = []
for item in pal_artigos2:
    pal_artigos.append(item.strip('\r'))
artigos.close()

## Blogs ##

blog = codecs.open("Palavras_blog_limpa.txt", 'rU','utf8')
pal_blog2 = blog.read().strip('\r').split(u'\n')
pal_blog = []
for item in pal_blog2:
    pal_blog.append(item.strip('\r'))
blog.close()

## Variável com a concatenação de todo o corpus escrito ##

corpus_escrito = pal_folha + pal_estadao + pal_artigos + pal_blog

with codecs.open('Corpus_Escrito.txt', 'w','utf8') as arquivo:
    for item in corpus_escrito:
        uni = unicode(item) + '\n'
        arquivo.write(uni)


###Concatenando os arquivos dos corpora orais num único arquivo ###

import codecs


## C-oral ##

coral = codecs.open("Palavras_Coral_limpas.txt", 'rU','utf8')
pal_coral2 = coral.read().split(u'\n')
pal_coral = []
for item in pal_coral2:
    pal_coral.append(item.strip('\r'))
coral.close()

## Iboruna ##

iboruna = codecs.open("Palavras_Iboruna_Final.txt", 'rU','utf8')
pal_iboruna2 = iboruna.read().split(u'\n')
pal_iboruna = []
for item in pal_iboruna2:
    pal_iboruna.append(item.strip('\r'))
iboruna.close()


## ProjetoSP 2010 ##

projetosp = codecs.open("Palavras_Sem_Marcador_Projeto_SP.txt", 'rU','utf8')
pal_projetosp2 = projetosp.read().split(u'\n')
pal_projetosp = []
for item in pal_projetosp2:
    pal_projetosp.append(item.strip('\r'))
projetosp.close()

## Projeto SP 2 ##

projetosp2 = codecs.open("Palavras_ProjetoSP2_Final.txt", 'rU','utf8')
pal_projetosp3 = projetosp2.read().split(u'\n')
pal_projetosp2 = []
for item in pal_projetosp3:
    pal_projetosp2.append(item.strip('\r'))
projetosp2.close()

## Variável com a concatenação das listas de palavras do corpus oral ##

corpus_oral = pal_coral + pal_projetosp + pal_projetosp2 + pal_iboruna


with codecs.open('Corpus_Oral.txt', 'w','utf8') as arquivo:
    for item in corpus_oral:
        uni = unicode(item) + '\n'
        arquivo.write(uni)

###Concatenando os arquivos dos corpora num único arquivo ###

import codecs


## C-oral ##

coral = codecs.open("Palavras_Coral_limpas.txt", 'rU','utf8')
pal_coral2 = coral.read().split(u'\n')
pal_coral = []
for item in pal_coral2:
    pal_coral.append(item.strip('\r'))
coral.close()

## Iboruna ##

iboruna = codecs.open("Palavras_Iboruna_Final.txt", 'rU','utf8')
pal_iboruna2 = iboruna.read().split(u'\n')
pal_iboruna = []
for item in pal_iboruna2:
    pal_iboruna.append(item.strip('\r'))
iboruna.close()


## ProjetoSP 2010 ##

projetosp = codecs.open("Palavras_Sem_Marcador_Projeto_SP.txt", 'rU','utf8')
pal_projetosp2 = projetosp.read().split(u'\n')
pal_projetosp = []
for item in pal_projetosp2:
    pal_projetosp.append(item.strip('\r'))
projetosp.close()

## Projeto SP 2 ##

projetosp2 = codecs.open("Palavras_ProjetoSP2_Final.txt", 'rU','utf8')
pal_projetosp3 = projetosp2.read().split(u'\n')
pal_projetosp2 = []
for item in pal_projetosp3:
    pal_projetosp2.append(item.strip('\r'))
projetosp2.close()

## Variável com a concatenação das listas de palavras do corpus oral ##

corpus_oral = pal_coral + pal_projetosp + pal_projetosp2 + pal_iboruna


## Folha ##

folha = codecs.open("Palavras_Folha_limpa.txt",'rU','utf8')
pal_folha2 = folha.read().split(u'\n')
pal_folha = []
for item in pal_folha2:
    pal_folha.append(item.strip('\r'))
folha.close()

## EstadÃ£o ##

estadao = codecs.open("Palavras_Estadao_limpa.txt", 'rU','utf8')
pal_estadao2 = estadao.read().strip('\r').split(u'\n')
pal_estadao = []
for item in pal_estadao2:
    pal_estadao.append(item.strip('\r'))
estadao.close()

## Artigos ##

artigos = codecs.open("Palavras_Artigos_limpa.txt", 'rU','utf8')
pal_artigos2 = artigos.read().strip('\r').split(u'\n')
pal_artigos = []
for item in pal_artigos2:
    pal_artigos.append(item.strip('\r'))
artigos.close()

## Blogs ##

blog = codecs.open("Palavras_blog_limpa.txt", 'rU','utf8')
pal_blog2 = blog.read().strip('\r').split(u'\n')
pal_blog = []
for item in pal_blog2:
    pal_blog.append(item.strip('\r'))
blog.close()

## Variável com a concatenação de todo o corpus escrito ##

corpus_escrito = pal_folha + pal_estadao + pal_artigos + pal_blog

#Variável total

corpus_total = corpus_oral + corpus_escrito

with codecs.open('Corpus_Total.txt', 'w','utf8') as arquivo:
    for item in corpus_total:
        uni = unicode(item) + '\n'
        arquivo.write(uni)

with codecs.open('Corpus_Total_Sem_Repetições.txt', 'w','utf8') as arquivo:
    for item in set(corpus_total):
        uni = unicode(item) + '\n'
        arquivo.write(uni)


## Quantificação do Corpora por Corpus ##

### ESCRITOS ###

## Folha ##

folha = open("Palavras_Folha_limpa.txt",'r')
pal_folha = folha.read().split('\n')
folha.close()

## Estadão ##

estadao = open("Palavras_Estadao_limpa.txt", 'r')
pal_estadao = estadao.read().split('\n')
estadao.close()

## Artigos ##

artigos = open("Palavras_Artigos_limpa.txt", 'r')
pal_artigos = artigos.read().split('\n')
artigos.close()

## Blogs ##

blog = open("Palavras_blog_limpa.txt", 'r')
pal_blog = blog.read().split('\n')
blog.close()

###ORAIS###

## C-oral ##

coral = open("Palavras_Coral_limpas.txt", 'r')
pal_coral = coral.read().split('\n')
coral.close()

## Iboruna ##

iboruna = open("Palavras_Iboruna_Final.txt", 'r')
pal_iboruna = iboruna.read().split('\n')
iboruna.close()


## ProjetoSP 2010 ##

projetosp = open("Palavras_Sem_Marcador_Projeto_SP.txt", 'r')
pal_projetosp = projetosp.read().split('\n')
projetosp.close()

## Projeto SP 2 ##

projetosp2 = open("Palavras_ProjetoSP2_Final.txt", 'r')
pal_projetosp2 = projetosp2.read().split('\n')
projetosp2.close()


print "Ocorrências:\n\n"
print "Estadão = ", len(pal_estadao)
print "Artigos = ", len(pal_artigos)
print "Blogs = ", len(pal_blog)
print "Folha = ", len(pal_folha)
listao = pal_estadao + pal_artigos + pal_blog + pal_folha
total_escrito = len(listao)
set_total_escrito = len(set(listao))
print 'Total Escrito = ', total_escrito
print "Set Escrito= ", set_total_escrito

print '\n\n'

print 'C-oral = ', len(pal_coral)
print 'Iboruna = ', len(pal_iboruna)
print 'Projeto SP = ', len(pal_projetosp)
print 'SP2 = ', len(pal_projetosp2)
listao2 = pal_coral + pal_projetosp + pal_projetosp2 + pal_iboruna
total_oral = len(listao2)
print 'Total Oral = ', total_oral
set_total_oral = len(set(listao2))
print "Set Oral= ", set_total_oral


print 'Total: \n\n'

tokens = len(listao) + len(listao2)
print 'Tokens: ', tokens
types = len(set(listao + listao2))
print 'Types: ', types
