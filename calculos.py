from rich.panel import Panel
from rich import print
def perguntar_num():
    while True:
        try:
            return float(input('Digite o valor desejado: ').replace(',','.'))
        except ValueError:
            print('DIGITE UM NUMERO VALIDO')

def soma():
    num1 = perguntar_num()
    num2 = perguntar_num() 
    resnum = num1 + num2 
    linha = f'{num1} + {num2} = {resnum} \n'
    with open('calculadora/historico.log','at') as arq:
    
        arq.write(linha)
        
    print(Panel(f'A soma entre os valores [blue]{num1}[/] e [blue]{num2}[/] é de: [red]{resnum}[/]',width=54))
    
def subtrair():
    num1 = perguntar_num()
    num2 = perguntar_num() 
    resnum = num1 - num2
    linha = f'{num1} - {num2} = {resnum}\n'
    with open('calculadora/historico.log','at') as arq:
    
        arq.write(linha)
    print(Panel(f'A subtração entre os valores [blue]{num1}[/] e [blue]{num2}[/] é de: [red]{resnum}[/]',width=54))
    
def dividir():
    while True:
        try:
            num1 = perguntar_num()
            num2 = perguntar_num() 
            resnum = num1 / num2
            linha = f'{num1} / {num2} = {resnum} \n'
            with open('calculadora/historico.log','at') as arq:
            
                arq.write(linha)
            print(Panel(f'A divisão entre os valores [blue]{num1}[/] e [blue]{num2}[/] é de: [red]{resnum}[/]',width=54))
            break
        
        except ZeroDivisionError:
            print('NÂO É POSSIVEL DIVIDIR POR ZERO')

def multiplicar():
    num1 = perguntar_num()
    num2 = perguntar_num() 
    resnum = num1 * num2
    linha = f'{num1} * {num2} = {resnum }\n'
    with open('calculadora/historico.log','at') as arq:
    
        arq.write(linha)
    print(Panel(f'A multiplicação entre os valores [blue]{num1}[/] e [blue]{num2}[/] é de: [red]{resnum}[/]',width=54))

