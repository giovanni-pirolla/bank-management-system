import datetime as dt
import pandas as pd
import time 


def limpar_tela():
    import os
    import platform
  
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

class funcionario:
    def __init__(self, nome, user_id, cargo, saldo):
        self._nome = nome
        self._cargo = cargo
        self._user_id = user_id
        self._saldo = saldo
        
    @property
    def saldo(self):
        return f'Saldo do {self._cargo} {self._nome}: R$ {self._saldo:.2f}'
    
    def realizar_operacao(self, tipo, valor):
        nova_linha = {
            'Data' : dt.datetime.now().strftime('%d/%m/%Y'),
            'Horario': dt.datetime.now().strftime('%H:%M:%S'),
            'id_usuario': self._user_id,
            'Nome': self._nome,
            'Cargo': self._cargo,
            'Tipo_transação': tipo,
            'Valor_transação': round(float(valor), 2)
        }
        df_transacoes = pd.read_csv('transacoes.csv', sep=';')
        df_transacoes = pd.concat([df_transacoes, pd.DataFrame([nova_linha])], ignore_index=True)
        df_transacoes.to_csv('transacoes.csv', sep=';', index=False)
        
        if tipo == 'Depósito':
            self._saldo += valor
                
            df_users = pd.read_csv('usuarios.csv', sep=';')
            df_users.loc[df_users['id_usuario'] == self._user_id, 'Saldo'] = self._saldo
            df_users.to_csv('usuarios.csv', sep=';', index=False)
        elif tipo == 'Saque':
            if valor <= self._saldo:
                self._saldo -= valor
                    
                df_users = pd.read_csv('usuarios.csv', sep=';')
                df_users.loc[df_users['id_usuario'] == self._user_id, 'Saldo'] = self._saldo
                df_users.to_csv('usuarios.csv', sep=';', index=False)
            else:
                print(f'''
    ================================================================================================================
    Saldo insuficiente para realizar o saque de R$ {valor:.2f} na conta de {self._nome}.
    ================================================================================================================
    ''')
                time.sleep(4)
                limpar_tela()
                return
            
        print(f'''
    ================================================================================================================
    Operação de {tipo} de R$ {valor:.2f} realizada com sucesso!\nNovo saldo: R$ {self._saldo:.2f}
    ================================================================================================================
    ''')
        time.sleep(4)
        limpar_tela()

        
    def ver_historico(self):
        pass
