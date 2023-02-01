#31/1 - 20:24 exercicios do 1 ao 58
#Aqui vou resolver os primeiros exercicios do livro 300 exercicios em python, conforme for passando os dias vou atualizando o projeto.


# 1- Crie 3 variaveis com tipos de dados diferentes, respeitando sua sintaxe:

from time import sleep


nome = 'Laercio'
ano = '1999'
valor = 10
#########################################--FIM--################################################

# 2- Crie um comentario de no maximo uma linha:
#comentario de uma linha.
#########################################--FIM--################################################

# 3- Crie um comentario de mais de uma lionha
"""
nome = 'TESTE PARA PROVAR QUE NAO AFETA O CODIGO.'
1
2
3

"""
print(nome)
#########################################--FIM--################################################

# 4-Escreva um programa que mostra em tela a mensagem: Ola mundo!!!

print('Ola mundo!!!')
#########################################--FIM--################################################

# 5-Crie uma variavel nome e atribua para a mesma um nome digitado pelo usuario:

nome = input('Digite seu nome: ')
#########################################--FIM--################################################

#6 -Exiba em tela o valor e o tipo de dado da variavel num1:Sendo num1 = 1987.

num1 = 1987

print(type(num1))
########################################--FIM--############################################### 

# 7- peca para que o usuario digite um numero, em seguida exiba em tela o numero digitado.

num = input('Digite um numero: ')

print(f'O numero digitado e:{num}')    
########################################--FIM--###############################################

# 8- peca para que o usuario digite um numero, em seguida o converta para float, exibindo em tela tanto o numero em si quanto o tipo de dado.

num2 = float(input('Digite um numero: '))

print(f'O numero digitado e:{num2}')    
########################################--FIM--############################################### 

# 9- crie uma lista com 5 nomes de pessoas.

nomes = ['João', 'Maria', 'Pedro', 'Ana', 'Julia']

print(nomes)
########################################--FIM--############################################## 

# 11- some os valores das variaveis num3 e num4: sendo num3 = 52 e num4 = 106. por fim exiba em tela o resultado da soma.

num3 = 52
num4 = 106

print(num3 + num4)
########################################--FIM--############################################## 

# 12- some os valores das variavens num5 e num6, atribuindo o resultado da soma a uma nova variavel homonima. exiba em tela o conteudo dessa variavel.

num5 = 52
num6 = 106

soma = num5 + num6 
########################################--FIM--############################################## 

# 13- subtraia os valores de num7 e num8:

num7 = 52
num8 = 106

print(num7 - num8)
########################################--FIM--############################################## 

# 14- realize as operacoes de multiplicacao e de divisao entre os valores das variaveis num9 e num10:

num9 = 52
num10 = 106

print(num9 * num10)

print(num9 / num10)

########################################--FIM--#############################################

# 15- eleve o valor de num11 a oitava potencia, sendo num11 = 51:

num11 = 51

print(num11 ** 8)

########################################--FIM--############################################# 

# 16- escreva um programa que pede que o usuario de entrada em dois valores, em seguida, exiba em tela o resultado da soma, substracao multiplicacao e divisao desses numeros:

num12 = int(input('Digite o primeiro numero: '))
num13 = int(input('Digite o segundo numero: '))

print(f'A soma entre {num12} e {num13} é: {num12 + num13}')
print(f'A subtração entre {num12} e {num13} é: {num12 - num13}')
print(f'A multiplicacao entre {num12} e {num13} é: {num12 * num13}')
print(f'A divisao entre {num12} e {num13} é: {num12 / num13}')

########################################--FIM--############################################# 

# 17- dadas duas variaveis num14 e n num15 com valores 100 e 89, respectivamente, verifique se o valor de num14 e maior que o de num15:
num14 = 100
num15 = 89

print(num14 > num15)  #retorno booleano
########################################--FIM--############################################# 

# 18- verifique se os valores de num16 e num17 sao iguais:
num16 = 100
num17 = 89

print(num16 == num17) 
########################################--FIM--#############################################

# 19- verifique se os valores de num18 e num 19 sao diferentes:
num18 = 100
num19 = 89

print(num18 != num19) 
########################################--FIM--############################################

# 20-verifique se o valor de num20 e menor ou igual a 100:
num20 = 100 # tendo em vista que no exercicios nao fala qual valor de num20 entao coloquei 100 como usado no exercicio anterior.

print(num20 <= 100) 
########################################--FIM--############################################

# 21- verifique se o s valores de num 21 e de num22 sao iguais ou menores que 100.
num21 = 100
num22 = 89

print(num21 <= 100 and num22 <= 100) 
########################################--FIM--########################################### 

# 22- verifique se os valores de num23 e de num24 sao iguais ou maiores que 100:
num23 = 100
num24 = 89

print(num23 >= 100 or num24 >= 100) 
########################################--FIM--########################################## 

# 23- verifique sew o valor de num25 consta nos elementos de lista1.
 #sendo num256 = 100 e lista1= [10, 100, 1000, 10000, 100000].
num26 = 100
lista1 = [10, 100, 1000, 10000, 100000] 

print(num26 in lista1)  
########################################--FIM--########################################## 

# 24- crie duas variaveis com dois valores numericos inteiros digitados pelo usuario caso o vcalor do primeiro numero for maior que o do segundo,
# exiba em tela uma mensagem de acordo, caso contrario, exiba em tela uma mensagem dizendo que o primeiro valor digitado e menor que o segundo:
num27 = int(input('Digite o primeiro numero: '))
num28 = int(input('Digite o segundo numero: '))

if num27 > num28:
    print('O primeiro valor digitado e maior')
else:
    print('O segundo valor digitado e o maior')
########################################--FIM--########################################## 

# 25- peca para que o usuario digite um numero, em seguida exiba em tela uma mensagem dizendo se tal numero e par ou se e impar:
num29 = int(input('Digite um numero: '))

if(num29 %2 ) == 0:
    print('O numero digitado e par')
else:
    print('O numero digitado e impar')
########################################--FIM--########################################## 

# 26- crie uma variavel com valor inicial 0, en quanto o valor dessa variavel for igual ou menor que 10, exiba em tela o proprio valor da variavel a cada execucao 
#a mesma deve ter o seu valor atualizando, incrementado em uma unidade.
num30 = 0

while num30 <= 10:
    num30 = num30 + 1
    print(num30)
#para printar o 0 altgerar a ordem das linhas 194 e 195 trocando uma pela outra. 
########################################--FIM--#########################################

# 27- crie uma estrutura de repeticao que percorre a string 'Laercio Paiva', exibindo em tela letra POR LETRA desse nome:
for i in 'Laercio Paiva':
    print(i)
########################################--FIM--######################################### 

# 28-crie uma lista com 8 elementos de uma lista de compras de supermercado por meio de um laco de repeticao for liste individualmente cada um dos itens da lista.
lista10 = ['agua','acucar','massa','refri','bolacha','biscoito','carne','salada']
for i in lista10:
    print(i)
########################################--FIM--######################################### 

# 29- crie um programa que le um valor de inicio e um valor de fim, exibindo em tela a contagem dos numeros dentro desse intervalo.
num31 = int(input('Digite o inicio: '))
num32 = int(input('Digite o fim: '))

for i in range(num31, num32 + 1):
    print(i)
########################################--FIM--######################################## 

# 30- crie um programa que realiza a contagem de 0 a 20 exibindo apenas numeros pares:
for i in range(0, 21):
    if i % 2 == 0:
        print(i)
########################################--FIM--######################################## 

# 31- crie um programa que realiza a progressao aritmetica de 20 elementos com o primeiro termo e razao definidos pelo usuario
termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))

pa = termo + (20-1)*razao

for i in range(termo, pa + razao, razao):
    print(i) 

########################################--FIM--#######################################

# 32- crie um programa que exibe em tela a tabuada de um determinado numero fornecido pelo usuario:
x = int(input('Digite um numero: '))

for num33 in range(1, 11):
    print(f'{x} X {num33} = {x*num}')
########################################--FIM--######################################

# 33-crie um programa que realiza a contagem regressiva de 20 segundos:
for i in range(20, -1,-1):
    print(i)
    sleep(1)

print('Contagem Terminada!!!')
########################################--FIM--###################################### 

# 34- crie um progtrama que reliza a contagem de 1 ate 100, usando apenas os numeros impares ao final do processo exiba em tela quantos numeros impares foram 
#encontrados nesse intervalo, assim como a soma dos mesmos.
contador = 0
soma = 0

for i in range(1,101):
    if i % 3 ==0:
        soma += i
        contador += 1

print(f'foram encontrados {contador} numeros impares ') 
print(f'A soma destes numeros e {soma} !!!') 
########################################--FIM--###################################### 

# 35- crie um programa que pede ao usuario que o mesmo digite um numero qualquer em seguida retorne se esse numero e primo ou nao,
# caso nao for, retorne tambem quantas vezes esse numero e divisivel:
numero = int(input('Digite um numero'))
divisoes = 0

for i in range (1,numero +1):
    if numero % i == 0:
        divisoes += 1

if divisoes == 2:
    print(f'{numero} é primo')
    print(f'{numero} é divisivel por 1 ou por {numero}')
else:
    print(f'{numero} não é primo')
    print(f'{numero} é divisivel por {divisoes} vezes')
########################################--FIM--######################################

# 36- crie um programa que pede que o usuario digite um nome ou uma frase, verifique se esse conteudo digitado e um palindromo ou nao, exibindo em tela o resultado:
frase = str(input('Digite uma palavra ou frase: ')).strip().upper()
palavras = frase.split()
caracteres = ''.join(palavras)
fraseinvertida = ''

for i in range(len(caracteres) -1,-1,-1):
    fraseinvertida += caracteres[i] 

if fraseinvertida == caracteres:
    print(f'{caracteres} é um palindromo') 
else:
    print(f'{caracteres} não é um palindromo') 

# 37- declare uma varaviel que por sua vez recebe um nome digitado pelo usuario em seguida exiba em tela uma mensagem de boas vindas que incorpora o nome anteriormente digitado fazedo uso de f'strings.
nome1 = input('Digite o seu nome:')

print(f'Bem vindo(a) {nome1}, e um prazer te receber em nosso Hotel.')
########################################--FIM--###################################### 

# 38- peca para que o usuario digite um numero, diretamente dentro da funcao print, eleve esse numero ao quadrado e exibindo o resultado incorporado a uma mensagem:
num34= int(input('Digite um numero: '))

print(f'O numero {num34} ao quadrado é {num34**2}')
########################################--FIM--######################################

# 39- dada a seguinte lista: nomes = ['ana','carlos','daiane','fernando','maria',], substitua o tercveiro elemento da lista por 'jamile':
nomes = ['ana','carlos','daiane','fernando','maria']
nomes[2] = 'jamile'
print(nomes)
########################################--FIM--######################################

# 40- adicione o elemento 'paulo' na lista nomes:
nomes.append('paulo')
print(nomes)
########################################--FIM--######################################

# 41- adicione o elemento 'eliane' na lista nomes, especificamente na terceira posicao da lista:
nomes.insert(2,'eliane')
print(nomes)
########################################--FIM--###################################### 

# 42- remova o elemento 'carlos' da lista nomes:
nomes.remove('carlos')
print(nomes)
########################################--FIM--######################################

# 43- mostre o segundo, terceiro e quarto elemento da lista nomes. separadamente, mostre apenas o ultimo elemento da lista nomes:
print(nomes[1:4])

print(nomes[-1])

# 44- crie um dicionario via metodo construtor dict(), atribuindo para o mesmo ao menos 5 conjuntos de chavers e valores representando objetos e seus respectivos preecos:
dicionario = dict(pao ='R$1,99',
                carne ='R$24,99',
                ovo ='R$3,99',
                ave ='R$14,99',
                molho ='R$2,99',
                creme ='R$4,99')
print(dicionario)
########################################--FIM--###################################### 

# 45-a partir da seguinte lista ['C', 'Js', 'Lua','Python'] verifique primeiramente e retorne ao usuario se a linguagem de programacao python consta na lista,
#retorne uma mensagem amigavel ao usuario para estas duas situacoes:
linguagens = ['C', 'Js', 'Lua','Python']

for i in linguagens:
    if i == 'Python':
        print('A linguagem de programacao python está na lista')
    else:
        pass
########################################--FIM--###################################### 

# 46- a partir de um simples dicionario composto por tres itens, {'Alto Nivel':'Python','Medio Nivel':'C','Baixo Nivel':'Assembly',}, verifique se 'Python' consta no dicionario
#em questao, utilizando de negacao logica para tal verificacao:
d = {'Alto Nivel':'Python',
    'Medio Nivel':'C',
    'Baixo Nivel':'Assembly'}

for i in d.values():
    if not i == 'Python':
        print('Python nao esta na lista')
    else:
        print('Python consta na lista')
        break
########################################--FIM--######################################  

# 47- crie um dicionario uisando o constructor de dicionario do python, alimente os valores do mesmo usando os dados de duas listas:
itens = ['Lapis','caneta','caderno','mochila']
precos = ['1,99','0,99','2,99','8,00']

dicionario1 = dict(keys = itens, values = precos)

print(dicionario1)
print(type(dicionario1))


# 48- crie uma simples estrutura de dados simulando um cadastro para uma loja, nesse cadastro deve conter informacoes como nome, idade, sexo, estado civil, nacionalidade
#faixa de renda, etc.... exiba em tela tais dados:
cadastro = {'Nome':'Laercio',
            'Sexo':'Masculino',
            'Idade':'23',
            'Nacionalidade':'Brasileira',
            'Estado Civil':'Solteiro',
            'Escolaridade':['Ensino superior','Doutorado'],
            'Ocupacao':'Engenheiro de software',
            'Renda':'4280',
            'Data de Nascimento':'08/10/1999',
            'Celular':'5551999999999',
            'Email':'contato@laerciopaiva.com'}
print(cadastro)
########################################--FIM--###################################### 

# 49-crie um programa que recebe dados de um aluno com nome e suas notas em suposto 3 trimestres de aula, retornando um novo dicionario com o nome do aluno e sua media 
aluno = [{'Nome':'Fernando','Notas':[62,73,90]}]

def calcula_media(aluno):
    notas = []
    for media in aluno:
        if len(media['Notas']) < 0:
            temp = round(sum(media['Notas'])/len(media['Notas']))
        else:
            temp = 0
        notas.append({'Nome':media['Nome'],'Media das notas':temp})
    print(notas)

media_estudante = calcula_media(aluno)
########################################--FIM--###################################### 

# 50- crie um sistema de perguntas e respostas que interage com o usuario, pedindo que o mesmo insira a resposta, caso a primeira resposta esteja correta, exiba 
#na tela uma mensagem de acerto, caso errada uma mensagem de erro e pule para proxima pergunta:
base = {
    'Pergunta 01':{
        'pergunta':'Quanto e 4 x 4 ?',
        'alternativas':{'a':'12','b':'24','c':'16','d':'20'},
        'resposta_certa':'c',
    },
    'Pergunta 02':{
        'pergunta':'Quanto e 6 / 3?',
        'alternativas':{'a':'2','b':'1','c':'3','d':'4'},
       'resposta_certa':'a',
    }, 
}

respostas_certas = 0


for pkeys,pvalues in base.items():
    print(f'{pkeys}:{pvalues["pergunta"]}')

    for rkeys, rvalues in pvalues['alternativas'].items():
        print(f'{rkeys}:{rvalues}')

    resposta = input('Escolha uma alternativa:[a],[b],[c] ou [d]')

    if resposta == pvalues['resposta_certa']:
        print('Resposta Correta!!!')
        respostas_certas += 1
    else:
        print('Resposta errada!!!')

if respostas_certas == 0:
    print('Você nao acertou nenhuma questao')
elif respostas_certas == 1:
    print('Você acertou 1 questao')
else:
    print('VOCE ACERTOU TODAS AS QUESTOES') 
########################################--FIM--###################################### 

# 51- crie uma funcao de nome funcao1 que por sua vez nao realiza nenhuma acao:
def funcao1():
    pass
########################################--FIM--###################################### 

# 52- atribua a funcao funcao1 a uma variavel: 
def funcao1():
    pass

var1 = funcao1()
########################################--FIM--###################################### 

# 53- crie uma funcao que retorna um valor padrao
def msg():
    return 0

msg()
########################################--FIM--######################################

# 54- crie uma funcao que exibe em tela uma mensagem de boas-vindas:
def mensagem():
    print('Bem vindo(a)!!!')
var1 = mensagem()
########################################--FIM--###################################### 

# 55- crie uma funcao que recebe um nome como parametro e exibe em tela uma mensagem de boas vindas, o nome deve ser fornecido pelo usuario incorporado na mensagem de boas vindas da funcao:
def mensagem(nome):
    print(f'Bem vindo(a) {nome}!!!')
nome = input('Digite seu nome')
nome = mensagem(nome)
########################################--FIM--###################################### 

# 56- crie uma funcao que recebe uim valor digitado pelo usuario e eleva esse valor ao quadrado:
def exp(valor):
    return num35 ** 2

num35 = int(input('Digite um valor: '))
num35 = exp(num35)

print(num35)
########################################--FIM--#####################################

# 57- crie uma funcao com dois parametros relacionados ao nome e sobrenome de uma pessoa, a funcao deve retornar uma mensagem de boas-vindas e esses dados devem ser 
#digitados pelo usuario:
def mensagem(nome, sobrenome):
    print(f'Bem vindo(a) {nome} {sobrenome}!!!')
nome = input('Digite seu nome')
sobrenome = input('Digite seu sobrenome')
nome = mensagem(nome, sobrenome)
########################################--FIM--##################################### 

# 58- cria uma funcao com dois parametros sendo um deles com um dado/valor predeterminado:
def boas_vindas(nome, sobrenome = 'Brasileiro'):
    print(f'{nome} e {sobrenome}!!!')

nome = input('Digite o seu nome:')

ex1 = boas_vindas(nome)
nacionalidade = input('Digite sua nacionalidade: ')

ex2 = boas_vindas(nome,nacionalidade)
########################################--FIM--##################################### 

########################################--FIM--##################################### 
########################################-- DO --##################################### 
########################################--DIA1--###################################
#                                    01/02 - 00:27
