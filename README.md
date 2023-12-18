<h1 align="center">Bloco de notas</h1>

Este é um projeto de um site de bloco de notas. Ele permite que os usuários salvem, vizualizem, editem e excluam suas notas.

<h3>Como instalar?</h3>

- Clone o repositório: 
```python 
#Requisição http:
git clone https://github.com/IslanP1/bloco-de-notas.git

#Via chave ssh:
git clone git@github.com:IslanP1/bloco-de-notas.git
```

- Crie um ambiente virtual:
```python
#Windows:
py -m venv venv

#Linux
python3 -m venv .venv
```

- Ative o ambiente virtual:
```python
#Windows - cmd:
.\venv\Scripts\activate

#Windows - powershell:
.\venv\Scripts\activate.ps1

#Linux
. .venv/bin/activate
```

- Instale as dependências a partir do requirements.txt:
```python
pip install -r requirements.txt
```

- Rode o projeto:
```python
#Windows
py manage.py runserver

#Linux
python3 manage.py runserver
```
