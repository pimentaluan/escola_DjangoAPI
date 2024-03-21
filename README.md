# Projeto Escola API Django 🎓🐍

Este projeto é uma API desenvolvida em Django com base no curso de API Django da Alura. A API tem como objetivo gerenciar informações relacionadas a alunos, matrículas e cursos em uma escola.
  </br></br>
  ## Tecnologias usadas
  <div style="display:flex">
    <img aling="center" alt="python" src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white">
    <img aling="center" alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"> 
    <img aling="center" alt="django_rest" src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray">
    <img aling="center" alt="postman" src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white">
  </div>
  
## Funcionalidades Principais 📝🔍

- **Cadastro de Alunos:** Permite criar, visualizar, atualizar e excluir informações sobre os alunos da escola.
- **Cadastro de Matrículas:** Permite gerenciar as matrículas dos alunos em cursos específicos, incluindo criação, visualização, atualização e exclusão.
- **Cadastro de Cursos:** Permite o gerenciamento das disciplinas oferecidas pela escola, incluindo a criação, visualização, atualização e exclusão das mesmas.
- **Associação de Alunos e Matrículas:** Permite associar alunos às matrículas em cursos que estão realizando.
- **Autenticação:** Utiliza autenticação básica para restringir o acesso à API apenas a usuários autenticados.

## Instalação e Configuração ⚙️🔧

1. **Clonar o repositório:**
    ```
    https://github.com/pimentaluan/escola_DjangoAPI.git
    ```

2. **Instalar dependências:**
    ```
    cd escola_DjangoAPI
    pip install -r requirements.txt
    ```

3. **Configurar o banco de dados:**
    Certifique-se de configurar as configurações do banco de dados no arquivo `settings.py`, e execute as migrações:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Executar o servidor:**
    ```
    python manage.py runserver
    ```

A API estará disponível em `http://localhost:8000/`.
