#02/02 exercicios do 102 ao  145 ( NIVEL MEDIO )
#Hora de incio: 16:00

#102 - Crie um programa que recebe do usuario tres numeros diferentes, retornando para o mesmo qual destes numeros e o de maior valor
#       usar de funcoes aninhadas para realizar as devidas comparacoes entre os valores dos numeros:
x = int(input('Digite o primeiro numero: '))
y = int(input('Digite o segundo numero: '))
z = int(input('Digite o terceiro numero: '))

def maior_de_dois(x,y):
    if x > y:
        return x
    return y

def maior_de_tres(x,y,z):
    return maior_de_dois(x,maior_de_dois(y,z))

print(f'O maior numero entre {x},{y} e {z} e: {maior_de_tres(x,y,z)}')
#########################################--FIM--################################################

#103 - Crie um programa que atua como mecanismo controlador de um sistema direcional, registrando a direcao e o numero de passos executando, ao final do processo, exiba
# em telao numero de referencia para um plano cartesiano. Ex: se o usuario digitar CIMA 5, BAIXO 3 ESQUERDA 3 E DIREITA 2 o resultado sera a coordenada 2.

import math

posicao = [0,0] 

while True:
    coordenada = input('Digite a coordenada, seguido do numero de passos (usando CIMA, BAIXO, ESQUERDA ou DIREITA e um numero int) :')
    if not coordenada:
        break
    
    movimento = coordenada.split(',')
    direcao = movimento[0]
    passos = int(movimento[1])

    if direcao == 'CIMA':
        posicao[0] += passos
    
    elif direcao == 'BAIXO':
        posicao[1] -= passos
    
    elif direcao == 'ESQUERDA':
        posicao[1] -= passos
    
    elif direcao == 'DIREITA':
        posicao[1] += passos
    else:
        pass

print(int(round(math.sqrt(posicao[1] ** 2 + posicao[0] ** 2))))
print(posicao)
#########################################--FIM--################################################

#104 - Crie uma estrutua orientada a objetos hibrida, para cadastro de usuarios que permita ser instanciada por uma variavel de modo que a mesma pode ou nao
# repassar argumentos para seus objetos de classe na hora em que instancia tal classe para isso a classe deve conter atributos/objetos de classe padrao 
# e instanciaveis de fora da classe

class Usuario:
    nome = 'usuario'
    senha = 'padrao'

    def __init__(self, nome = None, senha = None):
        self.nome = nome
        self.senha = senha

usuario1 = Usuario('admin','12345')
print(f'Usuario registrado: {Usuario.nome}')
#########################################--FIM--################################################

#105 - grere uma lista com 50 elementos ordenados de forma crescente inicialmente usando do modo convencional (e do construtor de list padrao) 
    # posteriormente reescrevendo o codigo usando de list comprehension


lista1 = list()

for num in range(51):
    lista1.append(num)

print(lista1)

### list comprehension ###

lista2 = [num for num in range(51)]

print(lista2)   
#########################################--FIM--################################################

#106 - reescreva a estrutura abaixo de um simples programa que gera uma lista com as possiveis combinacoes entre duas outras llistas [1,2,3] e [4,5,6] reduzindo
# e otimizando a mesma via list comprehension

lista3 = []

for x in [1,2,3]:
    for y in [4,5,6]:
        if x!=y:
            lista3.append(x*y)

print(lista3)

### list comprehension ###

lista4 = [(x,y) for x in [1,2,3] for y in [4,5,6] if x!=y]

print(lista4)   
#########################################--FIM--################################################

#107 -  escreva um programa que cria um array de 5 elementos do tiupo int exiba em tela todos os elementos da array em seguida exiba individuialmente 
#os elementos pares da mesma de acordo com sua posicao de indice.

from array import *

numeros = array('i',[5,10,15,20,25])

for i in numeros:
    print(i)
    if i % 2 == 0:
        print(f'{i} e um numero par')
#########################################--FIM--################################################

#108 - crie uma array composta de 6 elementos alatorios porem com valores sequencias crescentes uma vez criada a array exiba em tela seu conteudo
# em seu formato original e em seu formato invertido
from array import *


numeros = array('i',[1,2,3,4,8,16,32])

for i in numeros:
    print(i)

numeros.reverse()

for i in numeros:
    print(i)
#########################################--FIM--################################################

#109 - dada a seguinte lista simples de elementos [1,3,5,7,9,11,13,15,17,19,21], transforme a mesma e um objeto do tipo array em seguida exiba o tamanho do array
# em bytes e seu marcador de posicao alocada em memoria:

from array import *

lista = array('i',[1,3,5,7,9,11,13,15,17,19,21])

print(f'lista e composta de: {len(lista)} elementos')

print(f'lista possui um tamanho de:  {lista.itemsize} bytes')

print(f'lista esta alocada na memoria no endereco: {lista.buffer_info()[0]}')
#########################################--FIM--################################################

#110 - escreva um programa que usando puramente logica encontra todos os numeros que sao divisiiveis por 7 e multiplos de 5 dentro de um intervalo de 
#0  a 500 incluindo tais valores:
numeros = []

for numero in range(0,501):
    if(numero % 7 == 0) and (numero % 5 == 0):
        numeros.append(str(numero))

print(','.join(numeros))
#########################################--FIM--################################################

#111 - escreva um programa que gera um numero aleatorio entre 0 e 10, salvando esse numero em uma variavel onde o usuario e convidado a interagir tentando
#advinhar qual foi o numero gerado ate acertar, caso usuario acerte o numero, exiba uma mensagem parabenizando, tambem exibindo incorporado em uma mensagem o numero em si

import random

num_gerado, num_advinhado = random.randint(0,11), 0

while num_advinhado!= num_gerado:
    num_advinhado = int(input('Digite um numero entre 0 e 10: '))

print('Parabens, voce acertou o numero!!!')

print(f'O numero gerado foi: {num_gerado}')
#########################################--FIM--################################################

#112 - escreva um programa que executa um bloco de codigos situado dentro de um comentario.
codigo = """
num = int(input('Digite um numero'))
def eleva_ao_quadrado(num):
    return num ** 2
print(f'{num} elevado ao quadrado e: {eleva_ao_quadrado})')
"""

exec(codigo)
#########################################--FIM--################################################

#113 - escreva um programa que recebe uma palavra qualquer do usuario, aplicando sobre a mesma funcao formatacao de estilo retornando a mesma com marcadores
# para negrito e italiano e sublinhado as funcoes que aplicam os estilos devem ser separadas entri si porem executadas em conjunto via decoradores para uma funcao principal

def negrito(palavra):
    def transforma():
        return "<b>" + palavra() + "</b>"
    return transforma

def italico(palavra):
    def transforma():
        return "<i>" + palavra() + "</i>"
    return transforma

def sublinhado(palavra):
    def transforma():
        return "<u>" + palavra() + "</u>"
    return transforma

@negrito
@italico
@sublinhado

def aplica_estilo():
    palavra = input('Digite uma palavra: ')
    return palavra

print(aplica_estilo())

#########################################--FIM--################################################

#114 - escreva um programa que le uma palavra ou frase digitada pelo usuario retornando o numero de letras maiusculas e minusculas da mesma, usar apenas
#logica e de funcoes embutidas no sistema.:
texto = input('digite uma palavra: ')

maisculas = 0
minusculas = 0

for letra in texto:
    if(letra.islower()):
        minusculas += 1
    elif(letra.isupper()):
        maisculas += 1

print(f'no texto{texto} foram encontradas {minusculas} letras minusculas e {maisculas} letras maisculas')
#########################################--FIM--################################################

#115 - Escreva um programa que verifica se uma determinada palavra consta em um texto de origem texto "Python e uma excelente linguagem de programacao!!!"
texto = "Python e uma excelente linguagem de programacao!!!"

pesquisa = input('Digite uma palavra a ser pesquisada: ')

if(texto.find(pesquisa) == -1):
    print(f'A palavra {pesquisa} não foi encontrada')
else:
    print(f'A palavra {pesquisa} foi encontrada')
#########################################--FIM--################################################

#116 - escreva um programa que verifica se um endereco de site foi digitado corretamente validandso se tal endereco constam o prefixo 'www' e o sufixo '.com.br' pedindo
# que o usuario digite repetidas vezes o endereco ate que o mesmo for validado como correto

endereco = ''

while(endereco.startswith('www.') and endereco.endswith('.com.br'))!= True:
    endereco = input('digite um endereco: ')

print(f'{endereco} e um endereco Valido!!!')
#########################################--FIM--################################################

#117 - escreva um programa que recebe uma lista de elemebtos mistos trocando de posicao apenas o primeiro e o ultimo elemento da lista de referencia
listadereferencia = [11,22,33,44,55,66,77,88,'X']

print(f'Lista Original: {listadereferencia}')

temp = listadereferencia[0]
listadereferencia[0] = listadereferencia[-1]
listadereferencia[-1] = temp

print(f'Lista finalizado: {listadereferencia}')
#########################################--FIM--################################################

#118 - escreva um programa que realiza a valiodacao de uma senha digitada pelo usuario o mecanismo de validacao deve verificar se a senha digitada possui um tamanho 
#minimo  de 6 caracteres tamanho maximo de 16 caracteres ao menos uma letra entre a e z ao menos uma letra maiuscula e ao menos um simnolo especial
import re

senha = input('Digite sua nova senha: ')

x = True

while x:
    if(len(senha) < 6 or len (senha) > 16):
        print('A senha deve conter entre 6 e 16 caracteres!')
        break

    elif not re.search("[a-z]", senha):
        print('A senha deve conter ao menos uma letra minuscula!')
        break

    elif not re.search("[0-9]", senha):
        print('A senha deve conter ao menos um numero!')
        break

    elif not re.search("[A-Z]", senha):
        print('A senha deve conter ao menos uma letra maiuscula!')
        break 

    elif not re.search("[!@#$%^&*]", senha):
        print('A senha deve conter ao menos um simbolo especial!')
        break

    elif re.search("\s", senha):
        break
    else:
        print('A senha foi cadastrada com sucesso!!!')
        x = False
        break

if x:
    print('Senha invalida!')
#########################################--FIM--################################################

#119 - escreva um programa que realiza a contagem do numero de segundas feiras que caem no dia 1 de cada mes dentro de um intervalo do ano de 1999 ate 2023
from datetime import datetime

segundas = 0
meses = range(1,13)

for ano in range(1999, 2023):
    for mes in meses:
        if datetime(ano,mes,1).weekday() == 0:
            segundas += 1

print(f'Entre 1999 e 2023 existem {segundas} segundas-feiras no primeiro dia do mes.')

#########################################--FIM--################################################

#120 - escreva um programa que exibe uma mensagem em formato de contagem regressiva conmtando de 10 a 0 com o intervalo de 2 segundos entre uma mensagem e outra
import time
final = 0

total = 10

print('Contagem iniciada!')

while final <= 10:
    print(total)

    time.sleep(2)

    total -= 1
    
    final = total

    if total == -1:
        print('COntagem encerrada!!!')
        break
#########################################--FIM--################################################

#121 - escreva um programa que retorna a data e hora da ultima vez que um determinado arquivo foi modificado:
import os

import time

def ultima_mod(arquivo):
    status = os.stat(arquivo)
    data = time.localtime((status.st_mtime))
    
    ano = data[0]

    mes = data[1]

    dia = data[2]

    hora = data[3]

    minuto = data[4]

    segundo = data[5]

    str_ano = str(ano)[0:]

    if(mes <= 9):
        str_mes = '0' + str(mes)

    else:
        str_mes = str(mes)

    if(dia <= 9):
        str_dia = '0' + str(dia)
    
    else:
        str_dia = str(dia)

    return(str_dia + str_mes + str_ano + str_mes + str_ano + '/' +str(hora) + ':' + str(minuto) + ':' + str(segundo))
print('Ultima modificacao realizada em:', ultima_mod('testes.txt'))
#########################################--FIM--################################################

#123 -  crie uma funcao reduzida para separar elementos negativos e positivos de uma lista sem aplicar qualquier tipo de ordenacao sobre os mesmos:
lista01 =[-1,6,-9,-8,4,0,-3,2,7,1,8,-2]

print(f'Lista original:: {lista01}')

lista02 = [x for x in lista01 if x < 0] + [x for x in lista01 if x >= 0]

print(f'Lista rearranjada: {lista02}')
#########################################--FIM--################################################

#124 - escreva um programa que retorna os 5 elementos mais comuns de um texto ( caracter individuais) exibindo em tela tanto os elementos em si quanto
# o numero de incidencias de tais elementos:
from collections import Counter

texto = 'A radiologia e a ciencia que estuda a anatomia por meio de radiacoes!'

a1,a2,a3,a4,a5,a6 = Counter(texto).most_common(6)

print(f'O elemento mais comum e : "{a2[0]}", repetido {a2[1]} vezes')
print(f'O elemento mais comum e : "{a3[0]}", repetido {a3[1]} vezes')
print(f'O elemento mais comum e : "{a4[0]}", repetido {a4[1]} vezes')
print(f'O elemento mais comum e : "{a5[0]}", repetido {a5[1]} vezes')
print(f'O elemento mais comum e : "{a6[0]}", repetido {a6[1]} vezes')
#########################################--FIM--################################################

#125 - escreva um programa que recebe tres conjuntos numericos de mesmos valores, o terceiro conjunto deve ser uma copia literal do segundo exiba em tela os 
# conteudos dos conjuntos seu identificador de memoria e se alguns destes conjuntos compartilham do mesmo identificador ( se internamente sao o mesmo objeto alocado
# em memoria)
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

#126 - crie uma ferramenta implementavel em qualquer codigo que reliza a contagem de numero de variaveis locais presentes em uma determinada funcao do codigo:
def minha_funcao():
    x = 1
    y = 2
    
    nome = "Laercio"

    lista = []

    print(f'{x},{y}')

    print(f'{nome}')

    print(f'{lista}')

print(minha_funcao())

var_locais = minha_funcao.__code__.co_nlocals

print(f'A funcao {minha_funcao} possui {var_locais} variaveis')
#########################################--FIM--################################################

#127- escreva um programa que recebe do usuario um nome e um telefone, verificando se o nome digitado consta em uma base de dados pre existente, caso nao conste
# cadastre esse novo nome e numero na base de dados.

clientes = {'Laercio':'51991805568',
            'Paiva':'5199189899'}

novo_clientes = input('Digite o nome do cliente')

if novo_clientes in clientes:
    print(f'O cliente {novo_clientes} já existe na base de dados')
    novo_clientes = input('Digite nome do cliente')
else:
    print(f'{novo_clientes} Nao esta cadastrado')
    print('Digite novamente o nome a ser cadastrado')
    nome = input('Digite o nome: ')
    telefone = str(input('Digite o telefone: '))
    clientes.__setitem__(nome, telefone)

print(clientes)
#########################################--FIM--################################################

#128 - crie uma calculadora de 7 operacoes ( soma, subtracao, multiplicacao, divisao, exponenciacao, divisao inteira e modulo de uma divisao) com toda sua estrutura 
#orientada a objetos.
class Calculadora():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return self.num1 + self.num2
    
    def subtracao(self):
        return self.num1 - self.num2
    
    def multiplicacao(self):
        return self.num1 * self.num2
    
    def divisao(self):
        return self.num1 / self.num2
    
    def exponenciacao(self):
        return self.num1 ** self.num2
    
    def divisao_inteira(self):
        return self.num1 // self.num2
    
    def modulo(self):
        return self.num1 % self.num2

num1 = int(input('Digite o primeiro numero'))
num2 = int(input('Digite o segundo numero'))

operacao = Calculadora(num1, num2)

print('Escolha 1 para SOMA')
print('Escolha 2 para SUBTRACAO')
print('Escolha 3 para MULTIPLICACAO')
print('Escolha 4 para DIVISAO')
print('Escolha 5 para EXPONENCIACAO')
print('Escolha 6 para DIVISAO INTEIRA')
print('Escolha 7 para MODULO')

escolha = int(input('Digite o numero da operacao: '))

if escolha == 1:
    print(f'A soma de {num1} e {num2} é {operacao.soma()}')
elif escolha == 2:
    print(f'A subtracao de {num1} e {num2} é {operacao.subtracao()}')
elif escolha == 3:
    print(f'A multiplicacao de {num1} e {num2} é {operacao.multiplicacao()}')
elif escolha == 4:
    print(f'A divisao de {num1} e {num2} é {operacao.divisao()}')
elif escolha == 5:
    print(f'A exponenciacao de {num1} e {num2} é {operacao.exponenciacao()}')
elif escolha == 6:
    print(f'A divisao inteira de {num1} e {num2} é {operacao.divisao_inteira()}')
elif escolha == 7:
    print(f'A modulo de {num1} e {num2} é {operacao.modulo()}')
else:
    print('Opção inválida')
#########################################--FIM--################################################

#129 - escreva um programa que recebe uma fila composta de valores referente a idade de pessoas extraindo os 3 elementos de maior idade para uma ouutra fila prioritaria
# sem que os elementos prioritarios sejam rearranjados!
import heapq as hq

fila_original = [23,45,60,19,23,50,18,82,46,77]

fila_normal = hq.nsmallest(7, fila_original)

fila_prioritaria = list(set(fila_original) - set(fila_normal))

print(f'fila normal: {fila_normal}')

print(f'fila prioritaria: {fila_prioritaria}')
#########################################--FIM--################################################

#130 - na frase "A radiologia e a ciencia que estuda a anatomia por meio de exames de imagem" realize a contagem de carcteres de sua composicao retornando quais 
#6 caracteres mais recorrentes e quantas vezes os mesmos aparecem na frase acima!
from collections import Counter

texto = 'A radiologia e a ciencia que estuda a anatomia por meio de exames de imagem'

a1, a2, a3, a4, a5, a6 = Counter(texto).most_common(6)

print(f'A letra mais recorrente e "{a2}[0]", repetida {a2}[1] vezes')
print(f'A letra mais recorrente e "{a3}[0]", repetida {a3}[1] vezes')
print(f'A letra mais recorrente e "{a4}[0]", repetida {a4}[1] vezes')
print(f'A letra mais recorrente e "{a5}[0]", repetida {a5}[1] vezes')
print(f'A letra mais recorrente e "{a6}[0]", repetida {a6}[1] vezes')
#########################################--FIM--################################################

#132 - uma vez que temos a lista [...FRUTAS..] busque extrair o segundo e o quarto
#elementos da lista de forma ainda mais reduzida e otimizada que quando utilizamos list comprehension

frutas = ["Maca","banana","laranja","acabate","pessego"]

from operator import itemgetter

n_citricas = list(itemgetter(1,3(frutas)))

print(n_citricas)
#########################################--FIM--################################################

#133 - crie uma estrutura de codigo de validacao de uma senhaa digitada pelo usuario
import re

senha = input('Digite sua nova senha: ')

x = True

while x:
    if(len(senha) < 6 or len (senha) > 16):
        print('A senha deve conter entre 6 e 16 caracteres!')
        break

    elif not re.search("[a-z]", senha):
        print('A senha deve conter ao menos uma letra minuscula!')
        break

    elif not re.search("[0-9]", senha):
        print('A senha deve conter ao menos um numero!')
        break

    elif not re.search("[A-Z]", senha):
        print('A senha deve conter ao menos uma letra maiuscula!')
        break 

    elif not re.search("[!@#$%^&*]", senha):
        print('A senha deve conter ao menos um simbolo especial!')
        break

    elif re.search("\s", senha):
        break
    else:
        print('A senha foi cadastrada com sucesso!!!')
        x = False
        break

if x:
    print('Senha invalida!')
#########################################--FIM--################################################

#134 - reorganize os elementos da lista [-1,6,-9,-8,4,0,-3,2,7,1,8,-2] em ordem crescente e a partir da mesma gere duas novas listas uma contendo apenas os elementos
# negativos e outra contendo apenas os elementos positivos por fim exiba em tela o conteudo da lista original e das 3 novas listas
lista1 =  [-1,6,-9,-8,4,0,-3,2,7,1,8,-2]
print(f'Lista original: {lista1}')

lista2 = [x for x in lista1 if x < 0] + [x for x in lista1 if x >= 0]
lista3 = [x for x in lista1 if x < 0]
lista4 = [x for x in lista1 if x >= 0]

print(f'Lista rearranjada: {lista2}')
print(f'elementos negativos: {lista3}')
print(f'elementos positivos: {lista4}')\
#########################################--FIM--################################################

#137 - supondo que tenhamos uma lista composta por elementos em forma de dicionario, elementos estes aleatorios descrevendo em suas chaves e valores alguns carros
# com seus respectivos HP's, reorganize os elementos dessa lista de acordo com um criterio pre estabelecido, nesse cano, Potencia do motor

def f(crit):
    return crit['HP']

carros = [
    {'carro':'Celta','HP':'12'},
    {'carro':'Uno','HP':'12'},
    {'carro':'Prisma','HP':'0'},
    {'carro':'Golf','HP':'21'},
    {'carro':'Gol G3','HP':'80'},
    {'carro':'Gol quadrado','HP':'200'},
    {'carro':'Civic VTI','HP':'549'},
    {'carro':'Projetinho','HP':'999'},
]

carros.sort(key=f)

print(carros)
########################################--FIM--################################################

#141 - crie um metodo de classe com parametros nomeados justapostros, com valor padrao tipo de dado definidos na declaracao o que retorna um tipo de dado obrigatorio
# e especifico no retorno da funcao nesta ordem como referencia o metodo convencional def inventario(item, localizacao, quantidade, preco, categoria) deve ser
#transformado para um metodo para um metodo discriminado onde cada tipo de parametro possui uma identidade e caracteristicas proprias
"""def inventario(item, localizacao, quantidade, preco, categoria):
    pass
#metodo discriminado
def inventario(item,
    localizacao = 'estoque',
    quantidade = 0,
    preco:float = 0.01,
    categoria:list['perifericos',
                    'acessorios',
                    'Outros'],
    **kwargs)-> np.ndarray:
    pass""" #Rever depois!
########################################--FIM--################################################

#142 - crie uma classe composta por atributos "Somente leitura", da forma mais reduzida possivel:
from dataclasses import dataclass

@dataclass(frozen=True)
class Cachorro:
    cor:str
    idade: int

pet1  = Cachorro('Preto e branco',6)

print(pet1.cor)
########################################--FIM--################################################

#144 - crie uma estrutura de codigo que simula o sistema de depenmdencia de uma blockchain em um cluster de processamento nesse processo e permitido usar de alguma
# estrutura de repetricao, e cluster inicial deve conmter ao menos 4 blocos de origem
def executa(base_dir,no_dir,chain):
    caminhos = []
    base = base_dir
    no = no_dir
    chain = chain
    caminhos.append[0](base)
    caminhos.append[1](no)
    caminhos.append[2](chain)
    return caminhos

class Cluster:
    def __init__(self,bloco,params,configs):
        self.bloco = bloco
        self.params = params
        self.configs = configs
        self.nodes = ['bloco_01','bloco_02','bloco_03','bloco_04']
        self.cria_bloco = {node: executa(caminho = caminhos,
                            bloco = self.bloco,
                            params = self.params,
                            configs = self.configs)for node in self.nodes}
########################################--FIM--################################################

#145 - escreva um program que a partir de uma lista de elementos retorne o tipo de dado de cada elemento a lista em questao e 
# lista = [(1,),[1,2,3],(1),{4,5},{'nome':'A','value':2},10,[],1+3j,1.2,True,False,None,'Hello World!'].
lista = [(1,),
        [1,2,3],
        (1),
        {4,5},
        {'nome':'A','value':2},
        10,
        [],
        1+3j,
        1.2,
        True,
        False,
        None,
        "Hello World!",
        ]
for elemento in lista:
    print(elemento,type(elemento))
########################################--FIM--##################################### 
########################################-- DO --##################################### 
########################################--DIA3--###################################
#                                    02/02 - 20:00