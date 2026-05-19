from rich import print
from rich.panel import Panel

def lin():
    print('-'*30)
    
def menu(*texto):
    
    ## EXIBIR OPÇÔES
    contador = 1
    msg = ''
    for i in texto:
        msg += f'{contador} - {i} \n'        
        contador += 1 
    print(Panel(msg,width=27,height=9, title= '[blue]CALCULADORA[/]'))
    
def escolher_opcao(msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print('DIGITE UMA OPÇÃO VALIDA')

def apagarhistorico():
    with open('calculadora/historico.log','w') as arq:
        print('HISTORICO APAGADO COM SUCESSO!')
        
def historico():
    
    with open('calculadora/historico.log','r') as arq:
        conteudo = arq.readlines()
        lin()
        if len(conteudo) > 0:   
            print(f'HISTORICO DE CONTAS DO USUARIO')
            for i in conteudo:
                items = i.split()
                print(f'{items[0]} {items[1]} {items[2]} {items[3]} {items[4]}')
            lin()
        else:
            print('NÃO EXISTE HISTORICO DE CONTAS!!')
        