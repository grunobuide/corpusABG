## Processo Final de Limpeza do Corpus: IBORUNA

## Corpora

iboruna = open('Palavras_Iboruna_semilimpas.txt', 'r')
pal_iboruna = (iboruna.read().split())
iboruna.close()

##Limpeza: falta apenas " e -, os demais já foram excluídos

lixo = '-;"&'
iboruna_limpa = [x.lower().strip(lixo) for x in pal_iboruna]
print len(iboruna_limpa)

def mono (corpus):
    mono = []
    vogais = ['a', 'e', 'i', 'o', 'u']
    for palavra in corpus:
        if len(palavra) <= 2:
           mono.append(palavra)
    return mono

d = mono(iboruna_limpa)
print set(d)
           
           

## Gravar Arquivo

corpus_iboruna = open("Palavras_Iboruna_Final.txt", 'w')
corpus_iboruna.write("\n")
for palavra in iboruna_limpa:
    corpus_iboruna.write(palavra + "\n")
corpus_iboruna.close()

###### Comparar
##
##ibor = open("Palavras_Iboruna_Final.txt", 'r')
##pal_ibo = ibor.read().split()
##ibor.close()
##
##sp = open("Palavras_Projeto_SP.txt", 'r')
##pal_sp = set(sp.read().split())
##sp.close()
##
##
##def comparar(corpus, corpora):
##    diferentes = []
##    for palavra in corpus:
##        if palavra not in corpora:
##            diferentes.append(palavra)
##    return diferentes
##
##marc = set(comparar(pal_ibo, pal_sp))
##print len(set(marc))
##
##
#### Gravar diferentes - TEMPORÁRIO - TESTE PARA LIMPEZA
##
##corpus_iboruna2 = open("Palavras_Iboruna_tem.txt", 'w')
##corpus_iboruna2.write("\n")
##for palavra in marc:
##    corpus_iboruna2.write(palavra + "\n")
##corpus_iboruna2.close()

