# Comecando com Numpy -- ARRAYS --

# criando uma array do tipo Numpy contendo 15 elementos de valor zero:
import numpy as np

array = np.zeros(15)

print(array)
print(len(array))

#array de formato 4x4 preenchida com elementos de valor inicial zero, tais elementos devem ser do tipo inteiro.

array = np.zeros(shape = (4,4),
                dtype= 'int')

print(array)
print(type(array))
print(type(array[0,0]))

#criando um array com numpy composta de elementos, todos de valor 5:
array = np.ones(10) * 5

print(array)

#array composta de numeros inteiros, dentro do intervalo de 10 a 40:
array = np.arange(10, 41)

print(array)

#array composta apenas de elementos de valores pares dentro do intervalo de 10 a 50:
array = np.arange(10, 51, 2)

print(array)

#array de formato 3x3 composto de elementos de valores inteiros entre 0 e 8:
array = np.arange(9)
array =  array.reshape(3,3)

print(array)

#array de formato 10x10 preenchida com valores 128 sendo cada elemento do tipo float:
array = np.full(shape =(10,10),
                fill_value = 128,
                dtype = 'float')
print(array)
print(type(array[0,0]))

#array composto por apenas um elemento numerico de valor entre 0 e 1 :
array = np.random.rand(1)

print(array)

#array composto por 25 numeros naturais gerados aleatoriamente 
array = np.random.randn(25)

print(array)

#array composto por 50 elementos de valores simetricamente separados(linear espacados, escalonados entre 0 e 1:)
array = np.linspace(0, 1, 50)

print(array)

#dada uma matriz inicial 5x5 composta de elementos numericos seeuenciais entre 20 e 45 gere um array numpy contendo elementos a partir da terceira linha e segunda coluna da matriz origem:

a = np.array([[20,21,22,23,24],
            [25,26,27,28,29],
            [30,31,32,33,34],
            [35,36,37,38,39],
            [40,41,42,43,44]])

array = a[2:,1:]

print(array)

#reduzindo o codigo anterior utilizando metodo de geradores de arrays:
arr = np.arange(20,45).reshape(5,5)

array = arr[2:,1:]

print(array)

#array inicial 5x5 com elementos aleatoriam ente gerados dentro do intervalo de 20 a 44 exibindo em tela o array em si a soma de todos seus elementos e o desbio padrao dos mesmos:
arr = np.arange(20,45).reshape(5,5)
array10_soma = arr.sum()
array10_desvio = arr.std()

print(arr)
print(f'a soma de todos os elementos: {array10_soma}')
print(f'valor do desvio padrao: {array10_desvio}')

#a partir de um array 5x5 composto por elementos de valor nmumerico entre 20 e 44 exibindo em tela o resultado da soma de todos elementos da primeiro coluna, da quarta coluna
arr = np.arange(20,45).reshape(5,5)
soma_linhas = arr.sum(axis = 1)
soma_colunas = arr.std(axis = 0)

print(arr)
print(f'soma dos elementos da primeira linha: {soma_linhas[0]}')
print(f'soma dos elementos da primeira coluna: {soma_colunas[0]}')

print(f'soma dos elementos da quarta linha: {soma_linhas[3]}')
print(f'soma dos elementos da quarta coluna: {soma_colunas[3]}')

#array com formato 10x10 composto de 100 elementos de valores escalonados entre 0 e 1
array = np.arange(1,101).reshape(10,10) / 100

print(array)

#fornecidas 4 matriz diferentres cada uma composta de diversos elementos de valores proprios verifique se o retorno padrao gerado por cada matris e o valor logico True:
A = np.array([[3,2,1,4],
            [5,2,1,6]])

B = np.array([[0,1,2,3,4],
            [5,6,7,8,9]])

C = np.array([[True,False,False],
            [True,True,True]])

D = np.array([0.1,0.3])

for i,j in zip(list('ABCD'), [A,B,C,D]):
    print(f'Array {i}: {np.all(j)}')

#array composto por alguns elementos proprios retornando true para cada elemento que nao for do tipo numerico:
A = np.array([[3,2,1,np.nan],
                [3,2,1,np.nan]])

print(np.isnan(A))

#array com matriz transversa / matriz de identidade,  contendo 10 elementos de valor 1 na diagonal todos os tipo inteiro;
array = np.eye(N = 10,
                dtype = 'int')

print(array)

#nos moldes do anterior criando uma matriz dessa vez diagonal composta por 10 elementos em sua diagonal:
array = np.diag(np.arange(10))

print(array)

#array composto de 20 elementos de valores gerados aleatoriamente a array deve ter a capacidade de ser replicada por seu metodo gerador produzindo os mesmos valores
# de seu elemento idependente do numero de execucoes:
np.random.seed(10)
array = np.random.rand(20)

print(array)

#array composta de alguns elementos de valores proprios exibida em tela cada um dos elementos do array separadamente respeitando sua ordem:
array = np.array([[1,4,3,7],
                [5,2,6,8]])

for i in np.nditer(array):
    print(i)

#simulando o resultado do sorteio de uma loteria e gerando um array composto de 6 elementos aleatorios de valores entre 1 e 50 sem que tais numeros se repitam
np.random.seed(2042)
array = np.random.choice(range(1,50),
                        size = 6,
                        replace = False)
print(array)

#array formato 5x5 composto de numeros sequenciais a partir do numero 20 salvando esta array em um arquivo nomeado array.npy carregue a array contida no arquivo 
#para uma variavel e exiba em tela o conteudo dessa array:

A = np.arange(20,45).reshape(5,5)
np.save('array.npy', A)

B = np.load('array.npy')

print(B)

#array de 3 linhas e 4 colunas composto por numeros sequenciais ate 12 salvando esse array em um arquivo txt simples nomeando como array.txt e exibido em tela:
A = np.arange(12,dtype = 'int').reshape(-1,4)
np.savetxt(fname = 'array.txt',
           X = A,
           fmt = '%0.2f')

B = np.load('array.txt')

print(B)

#arrayh 4x4 inicialmente composta de elementos de valor 1 insirindo umas nova linha acima e abaixo assim como uma coluna a esquerda e uma a direita da matriz inicial
A = np.ones(shape=(4,4))

print(A)

print(np.pad(A,pad_width=1,
        constant_values=0))

#duas arrays, uma composta por elementos numericos sequenciais entre 0 e 8 distribuidos em formato 4x4 e uma segunda de mesmo formato composta por elementos numericos 
#aleatorios exibidindo em tela elementos comuns nas duas arrays
A = np.arange(8).reshape(-1,4)
B = np.array([[9,10,11,3],
                [2,8,0,8]])

print(A)
print(B)
print(np.intersect1d(A, B))

#array no formato 3x3 composto de um elemento numerico aleatorios extraindo os mesmos para uma lista ordenando os em forma numerica crescente:
A = np.random.randint(low = 1,
                        high = 10,
                        size = (2,3))

print(A)
print(np.unique(A))

#array no formato 3x3 composto por elementos de valor numerico decimais exibindo em tela a posicaso de indice de cada linha onmde consta o elemento de maior valor:
A = np.array([[0.4,0.3,0.1],
            [0.1,0.1,0.8],
            [0.2,0.2,0.5]])

print(np.argmax(A, axis=1))

#array de formato 6x6 que representa uma matriz de base triangular :
array = np.tri(N = 6)

print(array)

#imagem ruido de tamanho 800 x 600p a partir de uma array numpy
import numpy as np

imagem = np.random.randint(low = 0,
                            high = 256,
                            size = (800, 600),
                            dtype = np.uint8)
print(imagem)

#imagem ruido de tamanho 200x300p em 3 canais de cor, com valores de pixel aleatorios entre 0 e 255 a partir de um array numpy imagem reproduzivel
np.random.seed(42)
imagem = np.random.randint(low = 0,
                            high = 256,
                            size = (200, 300,3),
                            dtype = np.uint8)
print(imagem)

#array 2x2 composto de valores de 0 a 4 gerados via arrange revertendo a posicao de todos os elementos usando apenas notacao de fatiamento de listas:
array = np.arange(4, dtype ='int').reshape(-1,2)
print(array)

array = array[::-1, ::-1]
print(array)

#array formato 10 por 6 com valores aleatorios distribuidos entre 0 e 1 contabilize o numero de elementos de valor 1 e exiba em tela o resultado: a array deve ser reproduzivel:
np.random.seed(42)
array = np.random.randint(low = 0,
                            high = 2,
                            size = (10,6))

print(array)
print(f'Numeros UM encontrados {np.count_nonzero(array)}')

#array com 10 linhas 4 colunas composta por elementos de valores aleatorios defina o numero de casas decimais como 5 para cada um dos elementos:
array = np.random.randint(10,4)
np.set_printoptions(precision = 5)

print(array)

#arrayu [1.2e-6,1.7e-7] exiba em tela os valores desta array sem a notacao cientifica e com 8 casas decimais:
array = np.array([1.2e-6,1.7e-7])
np.set_printoptions(seprres = True,
                        precision = 8)

#MAIS EXERCICIOS DE ARRAY USANDO NUMPY NO LIVRO, PG 470