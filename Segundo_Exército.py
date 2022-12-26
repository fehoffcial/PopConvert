"""
    A-) Projeto de Análise de Dados: A Função Verdadeira ( IF ).
        1) Primeiro importar a biblioteca Time e Random para o arquivo, a ser utilizado no projeto para obter o tempo de cada função.
        2) Adicionamos uma função que é o dicionário para armazenar todos os tipos de valores exemplo: Numero da Function ,Random e Time.
        3) A partir daí, a função entra no loop, para selecionar F99.
        4) Iniciar função tempo tempo uma função.
        5) Iniciando o gerador de números aleatórios.
        6) Verificar se a função number_random é maior que 0,5, se for, salvará esses dados na função db_dict.
        7) Após o IF é verdadeiro, a function_number Number será salva na função db_dict.
        8) A função Timer é feita para calcular quantos milissegundos demorou para ser verdadeiro.
        9) Esta função db_dict salva todos os valores que são verdadeiros.
        10) Após você verifica quantas foi Keys no db_dict, se for até 99 Keys, depois execute break para parar a o Loop.
        11) Imprimir todos os Values de db_dict.
    B-) Projeto de Análise de Dados: A Função Falso ( Else ).
        1) Verificar se a função number_random é menor que 0,5, se for, salvará esses dados na função db_dict_all.
        2) Após o IF é verdadeiro, a function_number Number será salva na função db_dict_all.
        3) A função Timer é feita para calcular quantos milissegundos demorou para ser verdadeiro.
        4) Mostra quantas vez foi preciso para fechar o Loop e Time.
"""
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