from flask import Flask, render_template, request, redirect, url_for
import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

@app.route('/')
def index():
        nome = request.args.get('nome')
        idade = request.args.get('idade')

        if nome and idade:
             return render_template('resultado.html', nome = nome, idade = idade)
        else:
             return render_template('index.html')


@app.route('/calcular_idade', methods=['GET', 'POST'])
def calcular_idade():
    if request.method == 'POST':

        nome = request.form['nome']
        data_nascimento = datetime.datetime.strptime(request.form['data_nascimento'], '%Y-%M-%d')

        idade = datetime.datetime.now().year - data_nascimento.year
        #idade_real = relativedelta(datetime.datetime.now(), data_nascimento)

        return redirect(url_for('index', idade = idade, nome=nome))


if __name__ == '__main__':
    app.run(debug=True)