from interface import menu,escolher_opcao,apagarhistorico,historico
from calculos import soma,subtrair,dividir,multiplicar

from time import sleep
while True:
    menu('SOMAR','SUBTRAIR','DIVIDIR','MULTIPLICAR','HISTORICO DE CONTAS','APAGAR HISTORICO','ENCERRAR PROGRAMA')
    opc1 = escolher_opcao('Selecione a opção desejada: ')
    if opc1 == 1:
        soma()
    elif opc1 == 2:
        subtrair()
    elif opc1 == 3:
        dividir()
    elif opc1 == 4:
        multiplicar()
    elif opc1 == 5:
        historico()
    elif opc1 == 6:
        while True:
            opc2 = str(input('DESEJA APAGAR SEU HISTORICO [S/N]')).upper()
            if opc2 == 'S':
                apagarhistorico()
            elif opc2 == 'N':
                print(f'Retornando ao menu!')
                break
            else:
                print(f'DIGITE UMA OPÇÂO VALIDA [S/N]')
    elif opc1 == 7:
        print('FIM DO PROGRAMA')
        break
    else:
        print('Opção Invalida!')
    
    sleep(2)
        