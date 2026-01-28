# Sistema de Gerenciamento Bancário para Pequenas Empresas – POO & Data Analysis
Este é um sistema simples de gerenciamento bancário pensado para pequenas empresas utilizando Python. O projeto simula operações que ocorrem dentro de uma empresa, permitindo o gerenciamento de transações com base em diferentes níveis de permissão entre funcionários e administradores.

## 🛠️ Tecnologias utilizadas:
- **Linguagem**: 3.13.5
- **Manipulação de Dados**: Pandas (Leitura e escrita de arquivos CSV)
- **Estrutura**: Programação Orientada a Objetos (POO)
- **Bibliotecas Adicionais**: 'random', 'time', 'datetime', 'os', 'platform' (consiltar requirements.txt)

## 💻 Funcionalidades Principais
* **Sistema de Login (RBAC):** Controle de acesso baseado em funções (Administrador vs. Operador).
* **Persistência de Dados:** Todas as transações e usuários são salvos em arquivos `.csv`, garantindo que os dados não sejam perdidos ao fechar o programa.
* **Gerenciamento de Transações:** Registro automático de saques e depósitos com data, hora e ID do usuário.
* **Visão Administrativa:** O Administrador possui métodos exclusivos para visualizar o histórico geral da empresa e a lista completa de usuários.
* **Interface CLI Dinâmica:** Menus adaptativos que mudam conforme o cargo do usuário logado.

## 🏛️ Arquitetura (POO)
O projeto aplica conceitos fundamentais de Orientação a Objetos:
- **Herança:** A classe `Funcionario` serve como uma classe pai (base) para `Operador` e `Adm`, que herdam métodos dessa classe.
- **Encapsulamento:** Uso de atributos protegidos (`_saldo`) e propriedades.
- **Polimorfismo:** Métodos de visualização de extrato que se comportam de forma diferente dependendo da classe.



## 📂 Estrutura de Arquivos
- `main.py`: Ponto de entrada da aplicação e lógica dos loops de menu.
- `usuarios.csv`: Base de dados de credenciais e cargos.
- `transacoes.csv`: Histórico completo de transações financeiras.
- `funcionario.py`: Módulo contendo a lógica da classe pai 'funcionario', que é herdada pelas classes 'adm' e 'operador'.
- `operador.py`: Módulo contendo a lógica da classe filha 'operador'.
- `adm.py`: Módulo contendo a lógica da classe filha 'adm'.

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/giovanni-pirolla/bank-management-system.git

2. Baixe as dependências especificadas em requirements.txt:
   ```bash
   pip install -r requirements.txt

3. Execute o programa:
   ```bash
   python main.py

Desenvolvido por Giovanni Perazzoli Silva Pirolla.
