#EXTRAIR SÍLABAS E FREQUÊNCIAS

import codecs

#Input é o corpus, output é uma tabela em csv em que cada linha é uma sílaba
# do corpus. O formato vai me permitir comparar tônicas e átonas, finais,
#iniciais e mediais.



#abrindo o menino
a = codecs.open('corpus.csv', 'r','latin1')
arquivo  = a.read().split(u'\n')
a.close()

#formatando
i = 0
for item in arquivo:
    arquivo[i] = item.split(';')
    arquivo[i][-1] = arquivo[i][-1].strip(u'\r')
    i += 1

arquivo.pop(0)

dic_sil_typ = {}
dic_sil_tok = {}

for item in arquivo:
    try:
        for silaba in item[4].split(u'-'):
            try:
                dic_sil_typ[silaba] += 1
                dic_sil_tok[silaba] += item[7]
            except:
                dic_sil_typ[silaba] = 1
                dic_sil_tok[silaba] = item[7]
    except:
        print item
destino = codecs.open('silabas_type.csv','w','utf8')

for item, value in dic_sil_typ.items() :
	uni = u''
	uni = unicode(item) + u',' + unicode(value)
	uni += u'\n'
	destino.write(uni)
	
destino.close()

destino2 = codecs.open('silabas_tok.csv','w','utf8')

for item, value in dic_sil_tok.items() :
	uni = u''
	uni = unicode(item) + u',' + unicode(value)
	uni += u'\n'
	destino2.write(uni)
	
destino2.close()
