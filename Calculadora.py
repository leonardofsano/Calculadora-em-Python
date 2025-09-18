n1 = float(input('Escreva seu primeiro numero: '))
n2 = float(input('Escreva seu segundo numero: '))
operador = input('Escolha qual operador voce deseja fazer esta conta: [ /,*,+,- ]: ')
if operador == '/':
    print('Sua conta deu como resultado: {:.2f}'.format(n1 / n2))
elif operador == '*':
    print('Sua conta deu como resultado: {:.2f}'.format(n1 * n2))
elif operador == '+':
    print('Sua conta deu como resultado: {:.2f}'.format(n1 + n2))
elif operador == '-':
    print('Sua conta deu como resultado: {:.2f}'.format(n1 - n2))
else:
    print('Erro! Operador selecionado não existente')