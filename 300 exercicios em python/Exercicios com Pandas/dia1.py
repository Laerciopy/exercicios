import pandas as pd

#lista composta de 5 nomes / elementos em forma de string, criando uma serie a partir dessa lista exibindo em tela seu tipo de dado e conteudo!

nomes = ['João', 'Maria', 'Pedro', 'Ana', 'Julia']
pdnomes = pd.Series(data = nomes)
print(pdnomes)
print(type(pdnomes))

#a partir de um dicionario composto por seus respectivos itens de chave:valor, crie uma Serie, exibindo em tela seui conteudo: refatorando utilizando dataframe
estoque = {'Cel Xiaomi redmi Note  11': 1699,
          'Cel samsung taltal  12': 2567,
          'Cel motorola redmi Note  13': 1356,
          'Cel Xiaomi redmi Note  14': 2333}

pdestoque = pd.Series(data = estoque)
pdestoque = pd.DataFrame(pdestoque,columns=['Preco'])

print(pdestoque)
print(type(pdestoque.info()))
#print(type(pdestoque.describe()))   #             -utilizando describe


#a partir do dataframe criando para os exercicios anteriores, separe somante a coluna referente aos nomes dos itens exibindo em tela a lista de todos estes itens

estoque = {'Cel Xiaomi redmi Note  11': 1699,
          'Cel samsung taltal  12': 2567,
          'Cel motorola redmi Note  13': 1356,
          'Cel Xiaomi redmi Note  14': 2333}

pdestoque = pd.Series(data = estoque)
pdestoque = pd.DataFrame(pdestoque).reset_index()
pdestoque.columns = ['Item', 'Preco']

itens = pdestoque['Item']


print(itens)

#crie um datetimeindex referente ao mes de maio de 2022 cada elemento deste objeto deve ser um dos dias do mes de maio
maio = pd.date_range(start = '2022-05-01',
                    periods= 31)

print(maio)

#crie um dataframe composto de todas as suas segunas-feiras desde o inicio do ano de 2020 ate a metade do ano 2022, cada elemento do dataframe deve estar na notacao
#ano mes dia exiba em tela o conteudo  do dataframe:
segundas = pd.date_range(start ='2020-01-01',
                        end = '2022-06-01',
                        freq = 'W-MON')

print(segundas)
print(f'Entre 01/2020 e 06/2022 existem {len(segundas)} segundas feiras')

##Fim do modulo Pandas com dados staticos e iniciando ideia de projeto com tratamento de dados com pandas incorporando em um dashboard...