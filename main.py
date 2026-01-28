from operador import operador
from adm import adm
from funcionario import limpar_tela
import pandas as pd
import random
import time 



def gerar_id():
    df_users = pd.read_csv('usuarios.csv', sep=';')
    ids_existentes = df_users['id_usuario'].to_list()
    
    while True:
        novo_id = random.randint(1000, 9999)
        if novo_id not in ids_existentes:
            return novo_id
        
def criar_conta():  
    cargos = ['adm', 'operador']
    
    try:
        nome = str(input('Digite o nome completo: '))
    except ValueError:
        print('Nome de usuário inválido')
        return
    
    user_id = gerar_id()
    senha = str(input('Defina a senha desejada: '))  
    cargo = input('Digite o cargo do usuário: ').strip().lower()
    if cargo not in cargos:
        print('''
=========================================              
Cargo inválido. Escolha uma opção válida.
=========================================
''')
        time.sleep(2)
        limpar_tela()
        return
    
    try:
        saldo = float(input('Digite o saldo atual do usuário: '))
    except ValueError:
        print('''
=======================
Valor de saldo inválido
=======================
''')
        time.sleep(2)
        limpar_tela()
        return

    nova_linha = {
        'Nome' : nome,
        'id_usuario' : user_id,
        'Senha' : senha,
        'Cargo' : cargo,
        'Saldo' : saldo
    }
    
    df_users = pd.read_csv('usuarios.csv', sep=';')
    df_users = pd.concat([df_users, pd.DataFrame([nova_linha])], ignore_index=True)
    df_users.to_csv('usuarios.csv', sep=';', index=False)
    
    print(f'''
===============================================
Usuário criado com sucesso! Seu ID é: {user_id}
===============================================
''')
    time.sleep(3.5)
    limpar_tela()
    
def realizar_login():
    df_users = pd.read_csv('usuarios.csv', sep=';')
    
    if not df_users.empty:
        try:    
            user_id = int(input('Digite o seu ID: '))
            senha = str(input('Digite sua senha: '))
                    
            usuario_valido = df_users[(df_users['id_usuario'] == user_id) & (df_users['Senha'].astype(str) == str(senha))]
            
            if not usuario_valido.empty:
                dados = usuario_valido.iloc[0]
                nome = dados['Nome']
                cargo = dados['Cargo']
                saldo = dados['Saldo']
                
                if cargo == 'adm':
                    print(f'''
    ===============================================================================
    Acesso de {nome} como Administrador efetuado com sucesso!
    ===============================================================================
    ''')
                    time.sleep(2.5)
                    limpar_tela()
                    return adm(nome, user_id, cargo, saldo)
                elif cargo == 'operador':
                    print(f'''
    ===============================================================================
    Acesso de {nome} como Operador efetuado com sucesso!
    ===============================================================================
    ''')
                    time.sleep(2.5)
                    limpar_tela()
                    return operador(nome, user_id, cargo, saldo)
            else:
                print('''
    =============================================
    Acesso negado! Usuário e/ou senha inválido(s)
    =============================================
    ''')
                time.sleep(2)
                limpar_tela()
        except ValueError:
            print('''
    ========================================
    ID de usuário inválido. Tente novamente.
    ========================================
    ''')
            time.sleep(2)
            limpar_tela()
    
    else:
        print('''
=====================================
Nenhum usuário cadastrado no sistema.
Por favor, crie uma conta primeiro.
=====================================       
              ''')
        time.sleep(3)
        limpar_tela()

while True:
    print('''
=====SISTEMA DE ACESSO BANCÁRIO DA EMPRESA=====
          
Você deseja:''')
    
    escolha = int(input('''
Criar uma conta [1]
Realizar seu login [2]
Sair do programa [0]
'''))
    
    if escolha == 1:
        criar_conta()
        
    elif escolha == 2:
        usuario_logado = realizar_login()
        
        if usuario_logado:
            while True:
                print(f'''
=============================================================================================================                   
SEJA BEM VINDO(A) {usuario_logado._nome.upper()}! Quais os seus planos para hoje?
=============================================================================================================
''')
                
                
                opcao = int(input(f'''
Ver seu saldo atual [1]
Realizar um saque [2]
Realizar um depósito [3]
Ver {'seu histórico de transações' if usuario_logado._cargo == 'operador' else 'o histórico de transações da empresa'} [4]{'\nVer a lista de usuários [5]' if usuario_logado._cargo == 'adm' else ''}
Voltar[0]
'''))
                if opcao == 1:
                    print(usuario_logado.saldo)
                    time.sleep(4)
                    limpar_tela()
                
                elif opcao == 2:
                    try:
                        valor = float(input('Digite o valor a ser sacado: '))
                        usuario_logado.realizar_operacao('Saque', valor)
                    except ValueError:
                        print('''
=================================================
Utilize apenas números para o valor da transação.
=================================================
''')
                        time.sleep(2)
                        limpar_tela()
                
                elif opcao == 3:
                    try:
                        valor = float(input('Digite o valor a ser depositado: '))
                        usuario_logado.realizar_operacao('Depósito', valor)
                    except ValueError:
                        print('''
=================================================
Utilize apenas números para o valor da transação.
=================================================
''')
                        time.sleep(2)
                        limpar_tela()
                    
                elif opcao == 4:
                    usuario_logado.ver_historico()
                    
                elif opcao == 5:
                    usuario_logado.ver_usuarios()

                elif opcao == 0:
                    print('''
===============================
Voltando para o menu inicial...
===============================''')
                    time.sleep(2)
                    limpar_tela()
                    break
                        
                else:
                    print('''
===============================
Opção inválida. Tente novamente
===============================
''')
                    time.sleep(2)
                    limpar_tela()
            
    
    elif escolha == 0:
        print('''
=====================
Saindo do programa...
=====================
''')
        time.sleep(2)
        limpar_tela()
        break
    
    else:
        print('''
==================================
Escolha inválida. Tente novamente.
==================================
''')
        time.sleep(2)
        limpar_tela()