import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)


# funcionalidades
@app.route('/')
def homepage():
    return 'A API está no ar'


@app.route('/pegarvendas')
def pegarvendas():
    tabela = pd.read_csv('advertising.csv')
    tabela_vendas = tabela['Vendas'].sum()
    resposta = {'total vendas': tabela_vendas}
    return jsonify(resposta)


# rodar a api
if __name__ == "__main__":
    app.run(host='0.0.0.0')
