import os
import msvcrt
from ldap3 import Server, Connection, ALL

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def getpass_with_asterisks(prompt='Senha: '):
    """
    Recebe a senha do usuário e exibe asteriscos enquanto digita.
    """
    print(prompt, end='', flush=True)
    password = ''
    while True:
        ch = msvcrt.getch()
        if ch in [b'\r', b'\n']: 
            break
        elif ch == b'\x08': 
            if password:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else:
            password += ch.decode('utf-8')
            print('*', end='', flush=True)
    print()  # Newline
    return password

def connectionServer(ip_address, user, password):
    try:
        server = Server(ip_address, get_info=ALL)
        conn = Connection(server, user=user, password=password, auto_bind=True)
        print("Login bem-sucedido!")
        return conn
    except Exception as e:
        print("Login incorreto. Tente novamente.")
        return None

def query_ad_computers(conn, search_base, user_filter):
    try:
        search_filter = f'(cn={user_filter})'
        print(f"Filtro LDAP: {search_filter}")

        conn.search(search_base, search_filter, attributes=['cn'])
        
        if conn.entries:
            print("Computadores encontrados:")
            for entry in conn.entries:
                print(entry.cn)
        else:
            print("Nenhum resultado encontrado.")
    
    except Exception as e:
        print(f"Erro ao consultar o Active Directory: {e}")

def main():
    ip_address = '' # ip do ad
    search_base = 'dc=,dc='  # hostname
    conn = None

    while conn is None:
        clear_terminal()
        userInput = input("Digite seu usuário: ")
        password = getpass_with_asterisks()  
        user = "\\" + userInput.strip()  # entre aspas coloque o dominio

        conn = connectionServer(ip_address, user, password)

    clear_terminal()

    while True:
        user_filter = input("Digite o filtro de pesquisa (ex: RACH*), ou 'sair' para encerrar: ").strip()

        if user_filter.lower() == 'sair':
            print("Encerrando a pesquisa.")
            break
        
        clear_terminal()
        query_ad_computers(conn, search_base, user_filter)

    # Desassocia a conexão após finalizar as pesquisas
    conn.unbind()

if __name__ == "__main__":
    main()
