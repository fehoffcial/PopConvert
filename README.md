# PopConvert
""" Selection process of PopConvert company """
"""
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
"""
