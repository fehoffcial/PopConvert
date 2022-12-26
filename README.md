# PopConvert
# ***  1-) Primeiro Exército da Prova Seletivo:
# Você é dado duas listas ligadas não-vazias representando dois números inteiros não-negativos. Os dígitos são armazenados em ordem reverse, e há somente um dígito em cada posição das listas. Adicione os dois números e retorne a soma como uma lista ligada.
# Você pode assumir que os dois números não contém zeros na frente (ex: 001), exceto o número 0 em si.
# Precisamos que o código tenha uma função implementando o algoritmo faça o que é pedido no teste. Não se faz necessário chamar a função no código, chamaremos essa função ao testar o código com diferentes valores e deve funcionar para todos os valores possíveis descritos no teste.
# Exemplos:
    # 1-) Exercio:
        # Input: l1 = [2,4,3], l2 = [5,6,4]
        # Output: [7,0,8]
    # 2-) Exercio:
        # Explanation: 342 + 465 = 807.
    # 3-) Exercio:
        # Input: l1 = [0], l2 = [0]
        # Output: [0]
    # 4-) Exercio:
        # Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
        # Output: [8,9,9,9,0,0,0,1]
# Resultados:
    x = int(input("Digite o valor de l1: ")) #* O Valor de l1 para depois fazer a soma com l2
    y = int(input("Digite o valor de l2: ")) 
    xy = x+y #*  A Soma de x e y
    xy = str(xy) #* Convertendo INT para STR para ser utilizado na lista 
    xl = list(xy) #* Criando a LISTA com os VALORES
    xr = list(xy)
    xl.reverse() #! REALIZANDO REVERSE NA LISTA PARA EXIBIR COM SUCESSO
    print("Vamos exibir como que é feito o Processo do Exercio:")
    print("1-) Primeiramente fazemos a soma do valores {0} e {1} que o resultado é: {2} e realizando o reverse: {3}".format(x,y,xr,xl ))
# ***  2-) Primeiro Exército da Prova Seletivo:
#    A-) Projeto de Análise de Dados: A Função Verdadeira ( IF ).
#        1) Primeiro importar a biblioteca Time e Random para o arquivo, a ser utilizado no projeto para obter o tempo de cada função.
#        2) Adicionamos uma função que é o dicionário para armazenar todos os tipos de valores exemplo: Numero da Function ,Random e Time.
#        3) A partir daí, a função entra no loop, para selecionar F99.
#        4) Iniciar função tempo tempo uma função.
#        5) Iniciando o gerador de números aleatórios.
#        6) Verificar se a função number_random é maior que 0,5, se for, salvará esses dados na função db_dict.
#        7) Após o IF é verdadeiro, a function_number Number será salva na função db_dict.
#        8) A função Timer é feita para calcular quantos milissegundos demorou para ser verdadeiro.
#        9) Esta função db_dict salva todos os valores que são verdadeiros.
#        10) Após você verifica quantas foi Keys no db_dict, se for até 99 Keys, depois execute break para parar a o Loop.
#        11) Imprimir todos os Values de db_dict.
#    B-) Projeto de Análise de Dados: A Função Falso ( Else ).
#        1) Verificar se a função number_random é menor que 0,5, se for, salvará esses dados na função db_dict_all.
#        2) Após o IF é verdadeiro, a function_number Number será salva na função db_dict_all.
#        3) A função Timer é feita para calcular quantos milissegundos demorou para ser verdadeiro.
#        4) Mostra quantas vez foi preciso para fechar o Loop e Time.

# Exemplos:
    async function f(A, B) { 
    const X = Math.random()
    if (X >= 0.5) {
	A.register(f, X)

    } else {
	B.register(f, X)
    
    }
    return new Promise(resolve => {
	    setTimeout(() => resolve(X), 500)
        })
       }
    Input:
    async function f1(A, B) {
      A.register(f1, 4)
      return 4
    }
    async function f2(A, B) {
      B.register(f2, 5)
      return 5
    }
    async function f3(A, B) {
      A.register(f3, 20)
      return 20
    }
    minimum = 5
    callbackDelayPairs = [
      [f1, 100],
      [f2, 0],
      [f3, 5000],
    ]
    Output:
    {
      all: [[f1, 4], [f2, 5], [f3, 20]],
      filtered: [[f3, 20], [f2, 5]],
    }
    

# Resultados:
    import time,random # Importar a biblioteca Time e Random
    times_now = time.time() # Tempo Inicial dos Programa
    db_dict = {} # Dicionário para armazenar todos os valores exemplo: Número da Function ,Random e Time.
    db = {} # Dicionário para armazenar todos os tipos de valores exemplo: Número da Function ,Random e Time.
    function_number = 0 # Número da Function.
    init_random = 0 # Número da Function init_random.
    while True: # Ativando o Loop.
        time_function = time.time() # Time da Function.
        number_random = random.random() # Random Number Generator.
        if(str(number_random)[0:3]>"0.5"): # Verificação das funcão Number_random se for maior 0.5.
            function_number = function_number + 1 # A function_number Number será salva na função db_dict.
            times = time_function - times_now # Timer é feita para calcular quantos milissegundos demorou para ser verdadeiro.
            db_dict[f"f{function_number}"] = [f"[ RANDOM ] {number_random}",f"[ MS ] {str(times)[4:]}"] # Esta função db_dict salva todos os valores que são verdadeiros.
            if (99==len(db_dict.keys())): # Após você verifica quantas foi Keys no db_dict, se for até 99 Keys.
                user = input("Gostaria de exibir os valores db_dict [ Y ] ou [ N ]:")
                if user.upper()=="Y":
                    for functions in db_dict.items():
                        init_random+=1
                        print(functions) # Empremir os Values
                        if init_random==99: # Checking 
                            break # Finalizar o Loop
                    break # Finalizar o Loop
                if user.upper()=="N":
                    print(f"Quantas vez que foi preciso para fechar o [ Loop ] {len(db_dict.keys())} || Quantos Tempo que Demorou [ S ] {times_now}")  # Mostra quantas vez foi preciso para fechar o Loop.
        else:
            continue
        """
            function_number = function_number + 1  # A function_number Number será salva na função db_dict_all.
            times = time_function - times_now  # Timer é feita para calcular quantos milissegundos demorou para ser verdadeiro.
            db[f"f{function_number}"] = [f"[ RANDOM ] {number_random}",f"[ MS ] {str(times)[4:]}"]  # Esta função db_dict_all salva todos os valores que são verdadeiros.
        """
