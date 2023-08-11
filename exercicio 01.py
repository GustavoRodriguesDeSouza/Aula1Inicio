# Exercicio 01
nome = input('Digite o seu nome: ')
print('Seja bem vindo',nome)


# Exercicio 02
nome1 = input('Digite o seu nome: ')
dia = input('Digite o dia de seu nascimento: ')
mes = input('Digite o mês de seu nascimento: ')
ano = input('Digite o ano de seu nascimento: ')
print('O usuário',nome1,'nasceu em',dia,'/',mes,'/',ano)


# Exercicio 03

def bhaskara(a,b,c):
  delta = (b**2) - (4*a*c)
  x1 = (((-1)*b) + (delta**0.5))/(2*a)
  x2 = (((-1)*b) - (delta**0.5))/(2*a)
  if delta == 0:
    print()
    print("Equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta = 0, há um único valor de raiz (X1 = x2): ",x1)
  elif delta > 0:
    print()
    print("Equação do 2º Grau: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta > 0, temos dois valores distintos de raízes: ",x1,"e",x2)
  else:
    print()
    print("Resultado da equação: ",a,".x²",b,".x",c,"= 0")
    print("Como Delta < 0, não possui raízes reais!")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
bhaskara(a,b,c)


