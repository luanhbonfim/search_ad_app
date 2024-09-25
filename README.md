# 🔍 AD Computer Search - Consulta Computadores no Active Directory 🚀

Uma aplicação em Python para buscar computadores no Active Directory de forma simples, eficiente e segura! 💻

## ✨ Funcionalidades

- 🔑 **Autenticação segura**: Faça login com seu usuário e senha no formato `domínio\usuário`, com proteção da senha por asteriscos!
- 🖥️ **Busca por computadores**: Utilize filtros como `"NOT-*"` para listar todos os computadores correspondentes no AD.
- 📊 **Resultados instantâneos**: Veja os computadores encontrados diretamente no terminal.

## 🛠️ Como usar

1. Clone o repositório:
    ```bash
    git clone https://github.com/luanhbonfim/search_ad_app.git
    ```

2. Instale a biblioteca `ldap3`:
    ```bash
    pip install ldap3
    ```

3. Configure o endereço IP do servidor AD e a base de pesquisa no código:
    ```python
    ip_address = 'IP_DO_SEU_SERVIDOR'
    search_base = 'dc=dominio,dc=com'
    ```

4. Execute a aplicação:
    ```bash
    python ad_computer_search.py
    ```

5. Siga as instruções para login e busque os computadores usando filtros como `"NOT-*"`.

## 📌 Exemplo

Ao iniciar, você verá algo como:

Digite seu usuário: Luan <br>
Senha: ********** <br>
Digite o filtro de pesquisa (ex: NOT-), ou 'sair' para encerrar: <br>
NOT- Computadores encontrados: <br>
NOT-001 <br>
NOT-002 <br>
...

## 🛡️ Segurança

- Senhas são digitadas com proteção visual, aparecendo como asteriscos (`********`).
- A conexão ao AD é feita de maneira segura usando credenciais autenticadas.

## 🌟 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

👨‍💻 **Feito com Python**  
📬 Entre em contato: [Seu email](mailto:luanhenrique.dev@gmail.com)  
⭐ Se você gostou do projeto, não esqueça de dar uma estrela!

---

#Python #ActiveDirectory #Segurança #Automação



