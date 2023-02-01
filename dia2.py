#01/02 exercicios do 59 ao

#59 - Crie uma funcao com tres parametros, sendo dois deles com dados/valores padrao, alterando o terceiro deles contornando o paradigmas da justaposicao de argumentos

def pessoa1(nome,idade = 18,funcao = 'desenvolvedor'):
    print(f'{nome} tem {idade} anos, e sua funcao e {funcao}')

p1 = pessoa1('Laercio', funcao = 'analista de dados')

#########################################--FIM--################################################

#60 - Crie uma funcao que pode conter dois ou mais parametros porem sem um numero definido e declarado de parametros:
def msg(*args):
    print(f'Os parametros sao:{args}')

ex = msg('Nome = Laercio','Idade = 23','Profissao = Engenheiro de Software/Dados')
#########################################--FIM--################################################

#61 - Crie uma funcao de numero de parametros indefinido, que realiza a soma dos numeros repassados com parameros independentemente da quantidade de numeros:
def soma(*args):
    num = 0
    for valordigitado in args:
        num += valordigitado
    print(f'A soma dos numeros repassados é: {num}') 

soma = soma(18,43,99,1) #para testes
#########################################--FIM--################################################

#62 - crie uma funcao que recebe parametros tanto por justaposicao (*args) quanto nomeados (**kwargs):
def identificacao(*args,**kwargs):
    for n in args:
        nome = n
        #print(f'{n}')
    
    for k, v in kwargs.items():
        idade = k
        sexo = v
        #print(f'{idade},{sexo}')

        print(f'Nome:{nome},{idade},{sexo}')

pessoa = identificacao('Laercio', idade = 23, sexo = 'M')
#########################################--FIM--################################################

#63 - Escreva um programa que retorna o numero de fibonacci: sendo o numero de fibonacci um valor iniciado em 0 ou em 1 onde cada termo subsequente corresponde a soma
#dos dois anteriores:

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input('Digite um numero para encontrar seu Fibonacci'))
resposta = fibonacci(num-1)
print(resposta)
#########################################--FIM--################################################ 

#64 - crie um programa modularizado onde em um arquivo teremos uma lista de medicos ficticios a serem consultados em outro arquivo teremos a estreutura principal do programa
# que por sua vez realiza o agendamento de uma consulta com base na interacao do usuario.

import medicos

menu = str(input('Deseja agendar uma consulta? (S ou N)')).upper()

if menu == 'S':
    paciente = input('Por favor, digite seu nome completo:')
    print(f'{paciente}, escolha qual medico deseja consultar:')
    print('1 - Grazielle Veiga')
    print('2 - Matheus Correa')
    medico = int(input('Qual medico deseja consultar?'))
    if medico == 1:
        print(f'Sua consulta com a Dr.a {medicos.medicos[0]} sera agendada.')
    if medico == 2:
        print(f'Sua consulta com a Dr. {medicos.medicos[1]} sera agendada.')
else:
    print('Agradecemos o seu contato')
#########################################--FIM--################################################ 

#65 - aprimore o exemplo anterior incluindo um modulo simulando o cadastro de varios usuarios em um plano de saude apenas permitindo o agendamento de consulta
#       caso o usuario que esta interagindo com o programa conste no cadastro:
import cadastro_plano_saude

usuario = str(input('Digite seu numero de usuario: '))
if usuario in cadastro_plano_saude.usuarios.keys():
    if usuario == '001':
        usuario = 'Fernando'
        print('Bem-vindo Fernando!!!')
       
    elif usuario == '002':
        usuario = 'Ana Clara'
        print('Bem-vindo Ana Clara!!!')
        
    else:
        print('Usuario desconhecido ou nao cadastrado.')
       

    menu = str(input('Deseja agendar uma consulta? (S ou N)')).upper()
    if menu == 'S':
        print('Escolha qual medico deseja consultar:')
        print('1 - Grazielle Veiga')
        print('2 - Matheus Correa')
        medico = int(input('Qual medico deseja consultar?'))
        if medico == 1:
            print(f'Sua consulta com a Dr.a {medicos.medicos[0]} sera agendada.')
        if medico == 2:
            print(f'Sua consulta com a Dr. {medicos.medicos[1]} sera agendada.')
    else:
        print('Agradecemos o seu contato')
       
else:
    print('Usuario desconhecido ou nao cadastrado.')
#########################################--FIM--################################################ 

#66 - crie uma funcao que recebe parametros tanto por justaposicao quanto nomeados a partir de uma lista de dicionarios desempacotando os elementos e reorganizando os mesmos:
numeros = (33,1987,2020)
dados = {'Nome':'Laercio','Profissao':'Desenvolvedor'}

def identificacao(*args, **kwargs):
    print(args)
    print(kwargs)

identificacao(*numeros, **dados)
#########################################--FIM--################################################ 

#67 - crie uma classe de nome carro de tres atributos: nome, ano e cor:
class Carro:
    def __init__(self, nome, ano, cor):
        self.nome = nome
        self.ano = ano
        self.cor = cor 
#########################################--FIM--################################################ 

#68 - crie uma classe Pessoa instancie a mesma por meio de uma variavel e crie alguns atributos de classe dando caracteristicas a essa pessoa, por fim exiba em tela algumas 
#mensagem que incorpore os atributos da classe criados:
class Pessoa:
   pass

pessoa1 = Pessoa()
pessoa1.nome = 'Laercio'
pessoa1.idade = 23
pessoa1.profissao = 'Desenvolvedor'
pessoa1.hobby = 'Drifting'
pessoa1.carro = 'Civic vti 95 Aliviado, Forjado e com 500HP '

print(f'{pessoa1.nome} tem {pessoa1.idade} anos, e um {pessoa1.profissao} e ama fazer {pessoa1.hobby} com seu {pessoa1.carro}')

#########################################--FIM--###############################################

#69 - crie uma classe que armazena algumas caracteristicas de um carro em seguida cria dois carros distintos de caracteristicas diferentes, usando da classe para
#construcao de seus objetos/variaveis:
class Carro:
    ano = 1995
    cor = 'preto'
    modelo = 'VTI HATCH'
    opcionais = '1.5KG TURBO'

carro1 = Carro()

carro2 = Carro()
carro2.ano = 2015
carro2.cor = 'preto'
carro2.modelo = 'civic si'
carro2.opcionais = 'Aliviado com Gaiola'

print(f'CAarro numero 1 : Ano = {carro1.ano}, Cor = {carro1.cor}, Modelo = {carro1.modelo}, Opcionais = {carro1.opcionais}')


print(f'CAarro numero 2 : Ano = {carro2.ano}, Cor = {carro2.cor}, Modelo = {carro2.modelo}, Opcionais = {carro2.opcionais}')
#########################################--FIM--################################################ 

#70 - crie uma classe pessoa com metodo inicializador e alguns objetos de classe vazios dentro da mesma que representem caracteristicas de uma pessoa:


class Pessoa:
    def __init__(self):
        self.nome = None
        self.idade = None
        self.altura = None
        self.peso = None
        self.sexo = None
#########################################--FIM--################################################ 

#71 -crie uma classe de nome Inventario com os atributos de classe pre-definidos item1 e item2 a serem cadastrados manualmente pelo usuario simulando um simples 
#carrinho de copmpras:
class Inventario:
    def __init__(self,item1,item2):
        self.item1 = item1
        self.item2 = item2

cliente1 = Inventario('Camisa Nike Tam GG','Tenis Jordan 4 Black Cat Tam 44')

print(cliente1.item1)
print(cliente1.item2)
#########################################--FIM--################################################

#72 - crie uma classe biblioteca que possui uma estrutura molde basica para cadastro de um livro de acordo com seu titulo porem que espera a inclusao de um numero 
#definido de titulos em seguida cadastre ao menos 5 livros nessa biblioteca:

class Biblioteca:
    def __init__(self,livro1,**kwargs):
        self.livro1 = livro1

prateleira1 = Biblioteca('livro teste')
prateleira1.livro2 = 'Estruturando Algoritmos'
prateleira1.livro3 = 'Clean code'
prateleira1.livro4 = 'Ciencia de dados com python'
prateleira1.livro5 = 'entendendo python'
prateleira1.livro6 = 'Sql para ciencia de dados'

print(prateleira1.livro2)
print(prateleira1.livro3)
#########################################--FIM--################################################

#74 mostre via terminal a string 'Bem vindo ao mundo da programacao' de tras pra frente usando indexacao:
var = 'Bem vindo ao mundo da programacao'

print(var[::-1])
#########################################--FIM--################################################

#75 - escreva um programa que encontre todos os numeros que sao divisiveis por 7, mas que sao multiplos de 5, entre 2000 e 2200(ambos incluidos).
# os numeros obtidos devem ser impressos em sequencia separados por virgula em uma unica linha:

lista =[]

for i in range(2000,2201):
    if (i % 7 == 0) and (i % 5 != 0):
        lista.append(str(i))

print(','.join(lista))
#########################################--FIM--################################################

#76 - Escreva um programa, uma calculadora, simples de 4 operacoes, onde o usuario escolhera entre uma das 4 operacoes, (soma, subtracao,multiplicacao, divisao) lembrando
# que o usuario digitara apos dois valores e escolhera apenas uma operacao matematica do menu:

print('----- CALCULADORA DE 4 OPERACOES -----')
print('+ -> soma')
print('- -> subtracao')
print('* -> multicacao')
print('/ -> divisao')

numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o primeiro numero: '))

operacao = input('Digite a operacao que deseja realizar (+, -, *, /): ')

if operacao == "+":
    soma = numero1 + numero2
    print(f'O resultado da soma e : {soma}')

elif operacao == "-":
    subtracao = numero1 - numero2
    print(f'O resultado da subtracao e : {subtracao}')

elif operacao == "*":
    multiplicacao = numero1 * numero2
    print(f'O resultado da multiplicacao e : {multiplicacao}')

elif operacao == "/":
    divisao = numero1 / numero2
    print(f'O resultado da divisao e : {divisao}')

else:
    print('Operacao invalida') 
#########################################--FIM--################################################

#77 - Crie uma funcao que recebe o numero e retorna o mesmo dividido em duas metades, sendo cada metade um elemento de uma lista:
def divide_pela_metade(n):
    return[n//2,n-n//2]

n = int(input('Digite um numero: '))
print(divide_pela_metade(n))
#########################################--FIM--################################################

#78 - crie um programa que gera um dicionario a partior de um valor digitado pelo usuario de modo que serao exibidos todos os valores antecessores a esta numero
# multiplicados por eles mesmos, supondo que o usuario tenha digitado 4 a saida deve ser {1:1,2:4,3:9,4:16}:
numero = int(input('Digite um numero: '))
dicionario = dict()

for i in range(1,numero +1):
    dicionario[i] = i * i

print(dicionario)
#########################################--FIM--################################################

#79 - Defina uma funcao que pode aceitar duas strings como entrada, exibindo em tela apenas a string de maior tamanho/comprimento, caso as duas strings tenham o mesmo tamanho
#exiba as duas :
def mostra_msg_maior(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 > len2:
        print(f'{s1} e a string de maior tamanho. ')
    elif len2 > len1:
        print(f'{s2} e a string de maior tamanho. ')
    else:
        print(f'{s1} e {s2} sao iguais. ')
        print(s1)
        print(s2)

mostra_msg_maior(s1='STRING1', s2='MAIORSTRING')
#########################################--FIM--################################################

#80 - escreva um programa que recebe um texto do usuario e o converte para codigo mosrse, exbibindo em tela o texto em formato morse, seguindo a padronizacao ".-":
def texto_p_morse(texto):
    d = {'A':'.-', 'B':'-...',
        'C':'-.-.','D':'-..', 'E':'.',
        'F':'..-.','G':'--.', 'H':'....',
        'I':'..','J':'.---', 'K':'-.-',
        'L':'.-..','M':'--', 'N':'-.',
        'O':'---','P':'.--.', 'Q':'--.-',
        'R':'.-.','S':'...', 'T':'-',
        'U':'..-','V':'...-', 'W':'.--',
        'X':'-..-','Y':'-.--', 'Z':'--..',
        '1':'.----','2':'..---', '3':'...--',
        '4':'....-','5':'.....', '6':'-....',
        '7':'--...','8':'---..', '9':'----.',
        '0':'-----',',':'--..--', '.':'.-.-.-',
        '?':'..--..','/':'-..-.', '-':'-...-',
        '(':'-.--.',')':'-.--.-', '!':'-.-.--',
        '':'','""':'.----.', ':':'---...'}

    return ''.join(d[i] for i in texto.upper())
texto = input('Digite o texto a ser convertido para codigo morse: ')

conversor = texto_p_morse(texto)

print(f'{texto} em codigo morse : {conversor}')
#########################################--FIM--################################################

#82 - crie uma funcao que recebe um nome e um sobrenome do usuario retornando os  mesmos no padrao americano, ou seja, sobrenome primeiro seguido do nome:
def inverte_nome(n):
    nome,snome = n.split()
    return ' '.join([snome,nome])

pessoa = input('Digite seu nome e sobrenome')

pessoa = inverte_nome(pessoa)

print(pessoa)
#########################################--FIM--################################################

#83 - crie um programa que gera uma senha aleatoria com um tamanho definido pelo usuario:
import random

tamanho = int(input('Digite o tamanho que deseja sua senha: '))

senha = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'

senha = "".join(random.sample(senha,tamanho))

print(senha)
#########################################--FIM--################################################

#84 - crie uma funcao que exibe em tela tanto o conteudo de uma variavel local quanto de uma variavel global sendo as variaveis do mesmo nome, porem uma nao substituindo
# a outra :
def msg():
    global mensagem
    print(mensagem)
    mensagem = "Usufrua das funcionalidades do sistema."
    print(mensagem)

mensagem = 'Ola, seja bem vindo!'

msg()
#########################################--FIM--################################################

#86 - crie um programa que mostra a data atual, formatada para dia-mes-ano, hora:minuto:segundo 
import datetime

agora = datetime.datetime.now()

print("Data e hora atual: ")
print(agora.strftime("%d-%m-%Y, %H:%M%S"))
#########################################--FIM--################################################

#87 - crie um programa que exibe a versao atual do python instalada no sistema:
import sys 
print('Versao do nucleo python :')
print(sys.version)

print("versao detalhada")
print(sys.version_info)
#########################################--FIM--################################################

#88 - a partir de uma lista composta apenas de dados numericos, gere outra lista usando de list comprehension usando como base a lista anterior compondo
# a nova com os valores dos elementos originais elevados ao cubo:

lista1 = [1,2,3,4,5,6,7,8,9,10]

lista2 = [i**3 for i in lista1]

print(lista1)
print(lista2)
#########################################--FIM--################################################

#89 - dada uma estrutura inicial de um carrinho de compras com 5 itens e seus respectivos valores, assim como uma funcao que soma os valores dos itens
#desse carrinho, retornando um valor toital, aprimore a funcao deste codigo usando um list comprehension:

#### ESTRUTURA INICIAL ####
carrinho = []

carrinho.append(('item1',10))
carrinho.append(('item2',20))
carrinho.append(('item3',30))
carrinho.append(('item4',40))
carrinho.append(('item5',50))

total = 0

for produto in carrinho:
    total = total + produto[1]

print(f'O valor total e : R${total}')


#### CODIGO OTIMIZADO ####

total2 = sum([y for x,y in carrinho])

print(f'O valor total e : R${total2}')
#########################################--FIM--################################################

#90 -escreva uma funcao que recebe do usuario um numero qualquer e retorna para o mesmo tal numero elevado ao quadrado, crie uma documentacao para essa funcao 
# que possa ser acessada pelo usuario diretamente via IDE 
def ao_quadrado(num):
    """
    Esta funcao recebe como parametro um numero,
    retornando ao usuario o resultado do 
    numero em questao elevado ao quadrado.
    Ex: ao_quadrados(16) retornara 256.
    """
    return num **2

print(ao_quadrado.__doc__)
#########################################--FIM--################################################

#91 -  escreva um programa que receve uma frase qualquer, mapeando a mesma e retornando ao usuario cada palavra com a frequencia que ela mesma 
#aparece na frase em questao:

frequencia = []
texto = 'Se alguma coisa pode dar errado, dara errado, e mais, dara errado da pior maneira, no pior momento, e de modo que cause o maior / pior dano possivel'

for palavra in texto.split():
    frequencia[palavra] = frequencia.get(palavra,0) +1

palavra = frequencia.keys()

for i in palavra:
    print(f'[i] = {frequencia[i]}')
#revisar
#########################################--FIM--################################################

#92 - crie um  programa que recebe do usuario uma sequencia de numeros aleatorios separados por virgula, armazene os numeros um a um, em formado de texto
# como elementos ordenados de uma lista, mostre em tela a lista com seus respectivos elementos apos ordenados
numero = input('Digite os numeros, separados por virgula: ')

lista = numero.split(",")
lista.sort()

print(lista)
#########################################--FIM--################################################

#93 - escvreva um programa da forma mais reduzida possivel, que recebe do usuario uma serie de nomes, separando os mesmos e os organizando em ordem alfabetica em seguida
#exiba em tela os nomes ja ordenados

nomes = [x for x in input('Digite os nomes, separados por virgula: ').split(',')]
nomes.sort()
print(','.join(nomes))
#########################################--FIM--################################################

#94 - escreva um simples programa que recebe do usuario um numero qualquer, retornando ao mesmo se este numero digitado e um numero perfeito.
x = int(input('Digite um numero'))

def num_perfeito(x):
    soma = 0
    for i in range(1,x):
        if x % i == 0:
            soma += i
    return soma == x
if num_perfeito(x):
    print(f'{x} e um numero perfeito')
else:
    print(f'{x} nao e um numero perfeito')
#########################################--FIM--################################################

#95 - escreva uma funcao que recebe uma lista de elementos totalmente aleatorios e os ordena de forma crescente de acordo com seu valor numerico:
def ordena_lista(lista):
    for i in range(1,len(lista)):
        valor = lista[i]
        indice = i -1
        while indice >= 0:
            if valor < lista[indice]:
                lista[indice+1], lista[indice] = lista[indice], lista[indice+1]
                indice -=1
            else:
                break
    return lista
lista1 = ordena_lista([9,0,3,5,1,6,7,2,8,4])


print(lista1)
#########################################--FIM--################################################

#96 - crie uma estrutura toda orientada a objetos que recebe do usuario uma string qualquer retornando a mesma com todas as suas letras convertidas
#para letras maiusculas os metodos de classe para cada funcionalidade devem ser independentes entre si porem trabalhar no escopo geral da classe:
class Conversor(object):
    def __init__(self):
        self.s = ""

    def recebe_string(self):
        self.s = input('Digite uma palavra ou frase:  ')
    
    def exibe_string(self):
        print(self.s.upper())

frase1 = Conversor()
frase1.recebe_string()
frase1.exibe_string()
########################################--FIM--################################################

#97 - escreva de forma reduzida um programa que recebe do usuario um nome e duas notas salvando tais dados como um elemento de uma lista. exiba em tela o conteudo
from operator import itemgetter

nomes = []

while True:
    dados = input('Digite seu nome, seguindo de duas notas de 0 a 10')
    if not dados:
        break
    nomes.append(tuple(dados.split(',')))
print(sorted(nomes,key = itemgetter(0,1,2)))
########################################--FIM--################################################

#98 -crie um programa que gera o valor de salario de funcionarios considerando horas trbalhadas e horas extras, sendo o valor fixo da hora trabalhada 
    #R$ 29,11 e da hora extra R$5,00. crie uma regra onde o funcionario so tem direito a receber horas extras a partir de 40 hrs trabalhadas de forma convencional
valor_hora = 29.11
valor_hora_extra = 5

horas = int(input('Digite o numero de horas trabalhadas: ')) * valor_hora
adicional = int(input('Digite o numero de horas extras: ')) * valor_hora_extra

if horas > 40:
    valor_final = horas + adicional
else:
    valor_final = horas 

print(f'Salario base: R$ {horas}')
print(f'Adicional de horas extras: R$ {adicional}')

print(f'Salario Total: R$ {valor_final}')
########################################--FIM--################################################

#99 - reescreva o codigo anterior do ex 98 adicionando um mecanismo simples de validacao que verifica se os dados inseridos pelo usuario sao do tipo numerico
# caso nao sejam que o precesso seja ecerrado.

valor_hora = 29.11
valor_hora_extra = 5

try:

    horas = int(input('Digite o numero de horas trabalhadas: ')) * valor_hora
    adicional = int(input('Digite o numero de horas extras: ')) * valor_hora_extra

    if horas > 40:
        valor_final = horas + adicional
    else:
        valor_final = horas
except:
    print('Digite apenas numeros..')
    quit()

print(f'Salario base: R$ {horas}')
print(f'Adicional de horas extras: R$ {adicional}')

print(f'Salario Total: R$ {valor_final}')
########################################--FIM--################################################

#100 - crie um programa que recebe uma nota entre 0 e 1.0 classificando de acordo com a nota se um  aluno ficticio esta aprovado ou em recuperacao de acordo com
#sua nota , a media para aprovacao deve ser 0.6 ou mais, e o programa deve realizar as devidas validacoes para caso o usuario digite a nota em um formato invalido:

def calcula_nota(nota):
    if nota < 0 or nota > 1.0:
        print('nota invalida')
        print('A nota deve ser um valor entre 0 e 1.0')
    elif nota == 1.0:
        print('Parabens voce gabaritou a prova!!!')
    elif nota >= 0.6:
        print('Parabens, voce esta aprovado(a)!!!!')
    elif nota < 0.6:
        print('Nota abaixo da media, voce esta em recuperacao!')
    else:
        print('Nao foi possivel computar sua nota')
try:
    nota = float(input('Digite a nota: '))
except:
    print('Valor invalido')
    print('Use somente numeros com casas decimais entre 0 e 1.0')
    quit()
print(calcula_nota(nota))

########################################--FIM--################################################