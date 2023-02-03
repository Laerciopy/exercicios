#03/02 exercicios do 147 ao  200 ( NIVEL MEDIO FINALIZADO)
#Hora de incio: 08:00

#147 - a partir da lista lista=['a,'a','a','b','c','k','a',1,2,3,4,'j',1,'m'] gere uma nova lista porem sem elementos repetidos.

lista = ['a','a','a','b','c','k','a',1,2,3,4,'j',1,'m']

lista2 = []

for i in lista:
    if i not in lista2:
        lista2.append(i)

print(lista2)
#########################################--FIM--################################################

#148 - supondo que temos um  simples carrinho de compras, em formato de lista composta por alguns elementos onde cada elemento da mesma e um dicionario descrevendo
# um item, crie um mecanismo que retorna ao usuario o valor total do carrinho, seu item mais caro e tambem seu item mais barato.
lista_compras = [{'nome':'feijao','preco':'9.79'},
                {'nome':'arroz','preco':'3.45'},
                {'nome':'carne','preco':'20.93'},
                {'nome':'macarrao','preco':'2.99'}]

soma = sum([produto['preco'] for produto in lista_compras])

print(f'A cesta de produtos custa: R$ {soma:.2f}')

produto_max = max(lista_compras,key = lambda produto: produto['preco'])
produto_min = min(lista_compras,key = lambda produto: produto['preco'])

print(f"O produto mais caro: {produto_max['nome'].title()} - R$ {produto_max['preco']:.2f}")
print(f"O produto mais barato: {produto_min['nome'].title()} - R$ {produto_min['preco']:.2f}")
#########################################--FIM--################################################

#149 - uma vez apresentada a lista x = [10,12,35] apresente ao meenos 5 formas de retornar ao usuario a soma dos elementos dessa lista.

x = [10,12,35]

#metodo 1
num =x[0] + x[1] + x[2]

print(num)

#metodo 2
num = sum([i for i in x ])

print(num)

#metodo 3
num = sum(x)

print(num)

#metodo 4
def soma(x):
    total = 0
    for i in x:
        total += i
        print(total)
        return total
num = soma(x)

#metodo 5
n1,n2,n3 = x
num = n1 + n2 + n3

print(num)
#########################################--FIM--################################################

#150 - uma pratica comum e para certor contextos gerar listas, dicionarios ou qualquer outro tipo de conteiner de dados com algum valor padrao ou gerados a partir 
#de algum criterio nessa linha de raciocinio crie um gerador de dicionario que com um dado inteiro n fornecido pelo usuario retorna um dicionario
#composto por todos numeros antecessores ao numero n e seus valores elevados ao quadrado.

n = int(input('Digite um numero: '))

d = dict()

for i in range(1,n+1):
    d[i] = i * i
print(d)
#########################################--FIM--################################################

#151 - crie um diretorio chamado backups dentro desse diretorio crie uma pasta numerada para mes do ano por exemplo mes_03 antes de criar a pasta backup verifique
# se a mesma ja existe no diretorio raiz do projeto.
import os

if not os.path.exists('backups'):
    os.mkdir('backups')

    dir = [f'mes_{str(i).zfill(2)}' for i in range(1,13)]

    for i in dir:
        path = os.path.join('backups',i)
        os.mkdir(path)

    print(sorted(os.listdir('backups')))

else:
    print('backups já existe')
#########################################--FIM--################################################

#153 -crie um template de mala direta contendo uma mensagem envie a mensagem para 5 pessoas listadas em uma simples base de dados aqui representada pela lista nomes
#['ana','paulo','maria','rafael','patricia'] de modo que a mensagem seja personalizada a cada um dos nomes da lista.
from string import Template

nomes = ['ana','paulo','maria','rafael','patricia']

email = """Ola $name,
seja muito bem vindo ao curso de python
abracos !!!"""

template = Template(email)

for i in nomes:
    print(template.substitute(name = i))
    print('-' * 42)
#########################################--FIM--################################################

#154 -crie um simples mecanismo que le um determinado texto nesse caso "python 3.9" retornando ao usuario a quantidade de numeros encontrados no texto e que 
#   numeros sao estes ordenados em ordem posicional na exata ordem em que foram identificados no texto
import re

texto = "python 3.9"

numeros = re.findall(pattern=r"\d", string=texto)

print(f'Foram encontrados {len(numeros)} numeros no texto "{texto}".')
print(f'Os numeros sao {numeros[0]} e {numeros[1]}, respectivamente.')

#########################################--FIM--################################################

#155 - crie um simples mecanismo validador que recebe do usuario um texto qualquer e retorna ao mesmo se tal texto pertence ou nao a uma frase pre definida
# nesse caso: 'Python e uma excelente linguagem de programacao!!!'
texto = 'Python e uma excelente linguagem de programacao!!!'

pesquisa = input('Digite uma palavra a ser pesquisada:')

if(texto.find(pesquisa) == -1):
    print(f'A palavra "{pesquisa}" não foi encontrada no texto.')
else:
    print(f'A palavra "{pesquisa}" foi encontrada no texto.')
#########################################--FIM--################################################

#156 - escreva uma funcao que recebe do usuario um numero loongo qualquer o convertendo para notacao numerica computacional numero original considerado como bytes
# convertido de acordo com seu trabalho para kilobytes megabytes gigabytes etc e retornando em forma legivel ao usuario.

def conv_bytes(bytes):
    sufixo = 'B'
    
    for i in['','k','M','G','P','E','Z']:
        if abs(bytes) < 1024.0:
            return '%3.1f%s%s' % (bytes,i,sufixo)
        bytes /= 1024.0

    return '%.1f%s%s' % (bytes,'Y',sufixo)

num = int(input('Digite um numero: '))

numc = conv_bytes(num)

print(numc)
#########################################--FIM--################################################

#157 - escreva um programa que recebe do usuario um intervalo de tempo em anos, retornando a partir desta informacao o numero de ocorrencias de um dia especifico(
# nesse caso as segundas-feiras) dentro de um dia espefico do mes ( nesse caso no primeiro) em um intercalo de tempo previamente definido
from datetime  import datetime

segundas = 0
meses = range(1,13)

ano_inicio = int(input('Digite o ano inicial: '))
ano_fim = int(input('Digite o ano final: '))

intervalo = []
intervalo.append(ano_inicio)
intervalo.append(ano_fim)

for ano in range(intervalo[0], intervalo[1]+1):
    for mes in meses:
        if datetime(ano, mes, 1).weekday() == 0:
            segundas +=1

print(f'Entre {intervalo[0]} e {intervalo[1]}, existem {segundas} segundas-feiras no primeiro dia do mes.')
#########################################--FIM--################################################

#158 - crie uma pasta chamada imagens, entre na pasta e retorne seu caminho completo para uma variavel. exibe em tela o caminho completo da pasta imagens.
import os

os.mkdir('Imagens')
os.chdir('Imagens')

caminho = os.getcwd()

print(caminho)
#########################################--FIM--################################################

#159 - crie uma mecanismo otimizado de multipla escolha que recebe do usuario um determinado numero em sua forma numerica e retorna para o mesmo o numero escrito por extenso:

def conversor(num):
    match num:
        case 0: return 'Zero'
        case 1: return 'Um'
        case 2: return 'Dois'
        case 3: return 'Três'
        case 4: return 'Quatro'
        case 5: return 'Cinco'

numero = int(input('Digite um numero de 0 a 5: '))

print(conversor(numero))
#########################################--FIM--################################################

#160 - crie uma simples funcao que soma dois numeros fornecidos pelo usuario, retornando o resultado de tal operacao matematica. para a funcao soma()
#crie  uma docuimenmtacao acessivel pelo usuario diretamente via codigo orientando o mesmo a respeito do funcionamento da funcao, simulando que tal (  
# funcao e modularizada ou que de alguma forma seu codigo nao e explicito!!!)
from soma import soma

num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))

soma_numeros = soma(num1,num2)

print(f'A soma entre {num1} e {num2} é {soma_numeros}.')

print(f'Documentacao do mudolo soma: \n {soma.__doc__}')

#para acessar a domcumentacao use o comando help(soma)
#########################################--FIM--################################################

#161 - implemente um sistema de carrinho com insercao e remocao de elementos via comando, da forma mais reduzida possivel porem sem fazer uso de compression
# de lista ou funcao vazias, apenas estruturas condicionais simples, o sistema deve manter vivo ate quue o usuario digite um comando para sair:

carrinho = []

print('Digite o nome e pressione ENTER para inserir no carrinho.')
print('Digite CORRIGE para remover o ultimo item inserido')
print('Digite SAIR para fechar o carrrinho de compars.')

while(obj:=input('Digite um objeto: ')) != 'sair':
    carrinho.append(obj); print(carrinho)

    if obj =='corrigir':
        del(carrinho[-2]);del(carrinho[-1]);print(carrinho)

print(f'Lista de compras final:\n{carrinho}')
#########################################--FIM--################################################

#162 - escreva um simples modulo pacote que inspeciona uma determinada pasta retornando o nome de todos os arquivos de imagem contidos na pasta se houver:
import os

ext = ('.jpg', '.pjeg', '.png', '.bmp', '.gif')

arquivos = sorted([i for i in os.listdir() if i.endswith(ext)])

print(arquivos)
#########################################--FIM--################################################

#163 - crie um simples mecanismo que valida a ionsercao de um elemento em um dicionario verificando se o elemento a ser adicionado ao mesmo ja existe no dicionario atual

clientes = {'Laercio':'424214241',
            'Maria':'41114241',
            'Joao':'42224241',
            'Pedro':'123214241'}

novo_cliente = input('Digite o nome do cliente: ')

if novo_cliente in clientes.keys():
    print(f'{novo_cliente} já existe no dicionario.')
    novo_cliente = input('Digite o nome do cliente')
    if novo_cliente not in clientes.keys():
        print(f'para inserir {novo_cliente} a base de dados, digite um telefone.')
        clientes.__setitem__(novo_cliente,str(input('Digite o telefone: ')))

print(clientes)
#########################################--FIM--################################################

#164-  uma vez que temos dois conjuntos numericos iniciais c1 = (2,4,6,8,10) e c2 = (2,4,6,8,10) e um terceiro conjunto nomeado c3 gerado a partir do conteudo de c2
# equiparando os 3 conjuntos verifique se os mesmo possuem mesmo conteudo identiuficador de memoria
import collections

c1 = (2,4,6,8,10)

dq1 = collections.deque(c1)

c2 = (2,4,6,8,10)

dq2 = collections.deque(c2)

dq3 = dq2

print(f'Conjunto 1: {dq1}')
print(f'O endereco do Conjunto 1: {id(dq1)}')

print(f'Conjunto 2: {dq2}')
print(f'O endereco do Conjunto 2: {id(dq2)}')

print(f'Conjunto 1: {dq3}')
print(f'O endereco do Conjunto 1: {id(dq3)}')

if(dq1 == dq2)  and (id(dq1) == id(dq2)):
    print(f'conjunto 1 e 2 possuem os mesmo elementos e sao o mesmo objeto alocado em memoria')
if(dq1 == dq3)  and (id(dq1) == id(dq3)):
    print(f'conjunto 1 e 3 possuem os mesmo elementos e sao o mesmo objeto alocado em memoria')
if(dq2 == dq3)  and (id(dq2) == id(dq3)):
    print(f'conjunto 2 e 3 possuem os mesmo elementos e sao o mesmo objeto alocado em memoria')

if(dq1 == dq2)  and (id(dq1) != id(dq2)):
    print(f'conjunto 1 e 2 possuem os mesmo elementos, porem sao diferentes alocados em memoria')

if(dq1 == dq3)  and (id(dq1) != id(dq3)):
    print(f'conjunto 1 e 3 possuem os mesmo elementos, porem sao diferentes alocados em memoria')

if(dq2 == dq3)  and (id(dq2) != id(dq3)):
    print(f'conjunto 2 e 3 possuem os mesmo elementos, porem sao diferentes alocados em memoria')
#########################################--FIM--################################################

#165 - escreva um programa que procuira um certo dado / valor a partir de multiplos dicionarios, conforme dado inserido pelo usuario os dicionarios em questao
# devem possuiir itens domesticos representados com nome e preco retorne ao usuario o item consultado de qual dicionario foi extraido e seu valor em reais

from collections import ChainMap

cozinha = {
    'fogao': 631,
    'geladeira': 3000,
    'forno eletrico': 300}

sala = {
    'sofa': 631,
    'tv': 3000,
    'estante': 300}

quarto = {
    'cama': 631,
    'roupeiro': 3000,
    'secador eletrico': 300}

banheiro = {
    'pia': 631,
    'vaso': 230,
    'banheira': 3020}

x = ChainMap(cozinha,sala,quarto,banheiro)
y = input('Digite o item a ser buscado:')

if y in cozinha.keys():
    print(f'informacao extraida a partir do dicionario cozinha:')
    print(f'o valor de {y} e R$ {x[y]},00')
if y in sala.keys():
    print(f'informacao extraida a partir do dicionario sala:')
    print(f'o valor de {y} e R$ {x[y]},00')
if y in quarto.keys():
    print(f'informacao extraida a partir do dicionario quarto:')
    print(f'o valor de {y} e R$ {x[y]},00')
if y in banheiro.keys():
    print(f'informacao extraida a partir do dicionario banheiro:')
    print(f'o valor de {y} e R$ {x[y]},00')
else:
    print(f'o dado solicitado nao consta em nenhum dicionario:')
#########################################--FIM--################################################

#166 - crie tres classes representando tres funcionarios de uma empresa, descreva como atributo de classe primario o cargo e como atributos secundarios seus respectivos
#   nomes e salarios estres dados devem ser imutaveis insira os registros destes fuincionarios em uma lista e exiba em tela o conteuido da lista de funcionarios

from collections import namedtuple

funcionarios = namedtuple('ID', "Cargo Detalhes")
funcionarios = []

func001 = funcionarios('Gerente',{'Nome':'Anna', 'Salario':'R$ 2930,32'})
func002 = funcionarios('Fiscal',{'Nome':'Bento DI SA', 'Salario':'R$ 1330,32'})
func003 = funcionarios('Fiscal',{'Nome':'Carlos G', 'Salario':'R$ 1530,32'})

print(f'{func001} \n{func002} \n {func003}')

funcionarios.append(func001)
funcionarios.append(func002)
funcionarios.append(func003)
print(funcionarios)
#########################################--FIM--################################################

#167 - a partir de uma base simples de dados em uma lista composta por ['1001','1002','1003','1004','1005','1006',None,'1008','1009'] gere uma nova base
# de dados a partir desta contendo apenas dados validos retorne ao usuario uma mensagem informando a posicao de indice do dado invalido da base de dado original

base = ['1001','1002','1003','1004','1005','1006',None,'1008','1009']
lista = []
inv = 0

for i in base:
    if i is not None:
        lista.append(i)
    else:
        inv = base.index(None)
    
print(f'Nova lista: {lista}')
print(f'Existe um dado invalido no indice {inv} da lista original')
#########################################--FIM--################################################

#168 - supondo que temos uma lista composta por ['Terca','Quarta','Quinta','Sexta','Sabado','Domingo','Segunda'] reordene os elementos da lista de modo a obter a sequencia
# ['Segunda','Terca','Quarta','Quinta','Sexta','Sabado','Domingo'].
from collections import deque

semana = deque(['Terca','Quarta','Quinta','Sexta','Sabado','Domingo','Segunda'])
semana.rotate(1)

print(semana)
#########################################--FIM--################################################

#169 - uma vez que temos uma lista contendo como elemento proprio uma serie de tuplas compostas por uma categoria e por um tipo de exame de imagem, reconstrua 
#essa base de dados em um dicionario unificando as categorias de exames e agrupando seus subtipos:
data = [('Raio-X','Raios-X'),
        ('Magnetismo','Ressonancia Magnetica'),
        ('Física','Ressonancia Física'),
        ('Bioquímica','Ressonancia Bioquímica'),
        ('Raio-X','Ressonancia Eletroquímica'),
        ('Física','Ressonancia Mecânica'),
        ('Raio-X','Ressonancia Matemática')]

data_dict = []

for i,j in data:
    data_dict.setdefault(i,[]).append(j)

print(data_dict)
#########################################--FIM--################################################

#170 - otimize o codigo anterior fazendo uso de defaultdict() realize a comparacao do tempo de processamente nmecessario para ambos os metodos
from collections import defaultdict
data = [('Raio-X','Raios-X'),
        ('Magnetismo','Ressonancia Magnetica'),
        ('Física','Ressonancia Física'),
        ('Bioquímica','Ressonancia Bioquímica'),
        ('Raio-X','Ressonancia Eletroquímica'),
        ('Física','Ressonancia Mecânica'),
        ('Raio-X','Ressonancia Matemática')]

def_dict = defaultdict(list)
for i,j in data:
    def_dict[i].append(j)

print(def_dict)
#########################################--FIM--################################################

#171 - supondo que temos um dicionario representando usuarios de um sistema onde cada item do dicionnario e um usuario descrito por seu id
#   nome, sobrenome, e-mail, exiba em tela de forma estruturada exatamente como escrita no corpo do codigo o conteuido desse dicionario
from pprint import pprint 

data = {"usuarios":[
            {"Id":1,
            "Nome":"Rafael",
            "Sobrenome":"Morais",
            "email":"rmorais@gmail.com"},
            {"Id":2,
            "Nome":"Rafael",
            "Sobrenome":"aasd",
            "email":"rmorai3s@gmail.com"},
            {"Id":3,
            "Nome":"Rafael",
            "Sobrenome":"jr",
            "email":"rmowwrais@gmail.com"}]}

pprint(data)

print(data)
#########################################--FIM--################################################

#172 - Crie um mecanismo que gera um  numero pseudorrandomico, no intervalo entre 0 e 1, exibindo tal numero com 5 casal decimais apos a virgula.

import random

random.seed(42)

var = random.random()

print(f'{var:.5}')
#########################################--FIM--################################################

#173 - data a lista ['python','java','php','c++','c#','javaScript','kotlin','r'], retorne duas novas listas geradas a partir da lista inicial, com seus elementos
#reordenando de forma aleatoria porem reproduzivel.
import random

random.seed(32)
linguagens = ['python','java','php','c++','c#','javaScript','kotlin','r']
random.shuffle(linguagens)
print(linguagens)

random.seed(42)
random.shuffle(linguagens)
print(linguagens)
#########################################--FIM--################################################

#174 - supondo que a lista data = [30.28,34.26,39.47,33.54,29.46,36.54,31.54,27.58,32.55,20.15,30.40,36.15,20.40,22.42] e o  retorno dos ultimos 20 registros de um sensor
#qualquer  retorne a media simples, a media harmonica e a media geometrica destes valores. os resultados devem conter a precisao de 5 casas decimais.
import statistics
import numpy as np

data = [30.28,34.26,39.47,33.54,29.46,36.54,31.54,27.58,32.55,20.15,30.40,36.15,20.40,22.42]

print(f'Media simples: {round(statistics.mean(data),5)}')
print(f'Media Harmonica: {round(statistics.harmonic_mean(data),5)}')


data = np.array(data)

media_geom = round(data.prod()**(1.0/len(data)),5)

print(f'Media geometrica: {media_geom}')
#########################################--FIM--################################################    

#175 - supondo que para um determinado proposito temos uma classe de nome menu, que quando instanciada recebe um dado / valor que deve obrigatoriamente ser de tipo
#numerico para criacao de seui respectivo objeto / atributo de classe. a validacao por sua vez deve ocorrer a partir do metodo constructor da classe.

import numbers

class Menu:
    def __init__(self,n):
        if isinstance(n,numbers.Number) and n > 0:
            self.n = n
        
        else:
            raise TypeError("Valor deve ser numerico e maior que zero")
        
maquina1 = Menu(5)

maquina2 = Menu('cinco')
#########################################--FIM--################################################    

#176 - como bem sabemos, operacoes matematicas em python realizadas a partir de valores numericos muitos proximos tendem a gerar numeros com casas decimais 
# valores em casas decimais normalmente, arredondados por questoes de performance porem em computacao cientifica que pode ser necessario numeros com grande numero de casa
#decimais pois estes valores quanto mais extensos simbolizam maior precisao realize a simples soma de dois valores, 0.1 e 0.2 retornando um terceiro numero de no minimo
# 20 casas decimais
import decimal as d

resultado = d.Decimal(0.1) + d.Decimal(0.2)

print(resultado)
#########################################--FIM--################################################    

#177 - uma vez que temos as fraccoes 1/4 e 5/8 realize a soma desses fracoes exibindo em tela detalhadamente seus numeradores denominadores e o proprio resultado da soma
from fractions import Fraction

frac1 = Fraction(1,4)
print(f'Fracao: {frac1}')
print(f'Fracao: {frac1.numerator}')
print(f'Fracao: {frac1.denominator}')

frac2 = Fraction(5,8)
print(f'Fracao: {frac2}')
print(f'Fracao: {frac2.numerator}')
print(f'Fracao: {frac2.denominator}')

frac3 = Fraction(frac1) + Fraction(frac2)
print(f'Fracao: {frac3}')
print(f'Fracao: {frac3.numerator}')
print(f'Fracao: {frac3.denominator}')

print(f'Soma das Fracoes: {frac3}')
#########################################--FIM--################################################    

#178 - Crie um mecanismo de desempactotamento de dados, capaz de reduzir listas aninhadas para uma so lista comum sem alterar o comportamento de seus elementos
#a lista a ser usada de referencia e : [[1,2,[3,4,5,6,7,8]],[9,10,11,12]]
from pydash import py_

lista = [[1,2,[3,4,5,6,7,8]],[9,10,11,12]]

lista2 = py_.flatten_deep(lista)

print(lista2)
#########################################--FIM--################################################    

#179 - implemente dois mecanismos de extracao de dados a partir de dicionarios aninhados sendo ao menos um deles o metodo convencion al utilizando da notacao padrao
#de extracao de dados a partir das chaves de um dicionario.

item = {"TV":{'Mostruario':{'LG':'14p',
                    'SOny':'29p',
                    'Philipps':'32p'},
                    'Estoque':{'Sony':'29p',
                    'LG':'32p'}}}

print(item['TV']['Estoque']['LG'])

print(py_.get(item,'TV.Estoque.LG'))
########################################--FIM--##################################### 
########################################-- DO --##################################### 
########################################--DIA4--###################################
#                                    03/02 - 14:40
#                        - DANDO INICIO AOS EXERCICIOS COM BIBLIOTECAS -