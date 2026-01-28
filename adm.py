from funcionario import funcionario
from funcionario import limpar_tela 
import pandas as pd
        
class adm(funcionario):
    def __init__(self, nome, user_id, cargo, saldo):
        super().__init__(nome, user_id, cargo, saldo)

    def ver_historico(self):
        df_transacoes = pd.read_csv('transacoes.csv', sep=';')
        print(f'''
=======================================================================================================================================
{df_transacoes}
=======================================================================================================================================
''')
        input('Pressione Enter para continuar...')
        limpar_tela()
        
        
    def ver_usuarios(self):
        df_users = pd.read_csv('usuarios.csv', sep=';')
        print(f'''
=======================================================================================================================================
{df_users}
=======================================================================================================================================
''')
        input('Pressione Enter para continuar...')
        limpar_tela()