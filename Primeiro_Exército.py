x = int(input("Digite o valor de l1: ")) #* O Valor de l1 para depois fazer a soma com l2
y = int(input("Digite o valor de l2: ")) 
xy = x+y #*  A Soma de x e y
xy = str(xy) #* Convertendo INT para STR para ser utilizado na lista 
xl = list(xy) #* Criando a LISTA com os VALORES
xr = list(xy)
xl.reverse() #! REALIZANDO REVERSE NA LISTA PARA EXIBIR COM SUCESSO
print("Vamos exibir como que é feito o Processo do Exercio:")
print("1-) Primeiramente fazemos a soma do valores {0} e {1} que o resultado é: {2} e realizando o reverse: {3}".format(x,y,xr,xl ))
