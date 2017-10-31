# Corpus ABG
Scripts em Python referentes ao processo de compilação do Corpus ABG.

Esse repositório contém os scripts utilizados no tratamento dos dados para a produção do Corpus ABG.

Além disso, uma versão final com a lista de palavras e suas informações relevantes também está contida aqui.

O formato da tabela final é o seguinte (colunas separadas por vírgulas):

[Índice da palavra, palavra ortográfica, categoria morfológica, lema, transcrição fonológica, transcrição fonológica acentuada, estrutura silábica, categoria acentual, frequência no corpus geral, frequência no corpus oral, frequência no corpus escrito, nível de frequência]

Os scripts disponíveis e suas respectivas funções são as seguintes: 

1- limpa_corpus.py - Remove acentuação, números e metadados.
2- compila_corpus.py - junta os arquivos de texto.
3- script_contagem_palavras- extrai as frequências das palavras
4- taggeadas.rar - pasta com notas de aplicação do etiquetador do e-dictor.
5- junta_tags_freqs.py - script que junta as informações morfossintáticas com frequências.
6- transcritor.rar -pasta com o transcritor desenvolvido para este trabalho, contém a chave de transcrição
7- acentuador.rar - pasta que representa a sílaba tônica substituindo o núcleo da sílaba por um símbolo de transcrição tônico. Inclui Silabificador para o Português.
8 - contasilabas.py -  script que extrai as frequências das sílabas no corpus.


NOTA: Os textos originais dos quais as palavras e suas contagens foram extraídas não estão disponíveis aqui e nem serão disponibilizados pelos autores.

Por fim, o corpus também pode ser encontrado nesta pasta, no arquivo:


*Corpus_ABG_Completo_Versao3.csv*



Bruno Guide e Aline Benevides, 2016.
