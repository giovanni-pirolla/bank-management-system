from funcionario import funcionario 
from funcionario import limpar_tela 
import pandas as pd


class operador(funcionario):
    def __init__(self, nome, user_id, cargo, saldo):
        super().__init__(nome, user_id, cargo, saldo)
    
    def ver_historico(self):
        df_transacoes = pd.read_csv('transacoes.csv', sep=';')
        df_transacoes= df_transacoes[df_transacoes['id_usuario'] == self._user_id]
        print(f'''
=======================================================================================================================================
{df_transacoes}
=======================================================================================================================================
''')
        input('Pressione Enter para continuar...')
        limpar_tela()
