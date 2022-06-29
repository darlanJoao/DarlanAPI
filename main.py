from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<clube>')
def clubes(clube):
    times = ['flamengo', 'gremio', 'internacional', 'palmeiras', 'corinthians', 'são paulo', 'santos', 'cruzeiro']
    titu = [
        ['1 Mundial, 2 Libertadores,7 Brasileirao,  3 Copa do Brasil, 37 Estaduais'],
        ['1 Mundial, 3 Libertadores, 2 Brasileirao, 5 Copa do Brasil, 41 Estaduais'],
        ['1 Mundial, 2 Libertadores, 3 Brasileirao, 1 Copa do brasil, 45 Estaduais'],
        ['51 eh pinga, 3 Libertadores, 10 Brasileirao, 4 Copa do Brasil, 24 Estaduais'],
        ['2 Mundial e 1 Libertadores kkkkkkkkkkkk, 7 Brasileirão, 3 Copa do Brasil, 30 Estaduais'],
        ['3 Mundial, 3 Libertadores, 6 Brasileirao, 0 Copa do Brasil, 21 Estaduais'],
        ['2 Mundial, 3 Libertadores, 8 Brasileirao, 1 Copa do Brasil, 22 Estaduais'],
        ['0 Mundial, 2 Libertadores, 4 Brasileirao, 6 Copa do Brasil, 38 Estaduais']
    ]

    for i in times:
        if clube == i:
            opcao = titu[times.index(i)]
            break
    return jsonify({'Titulos': opcao})


app.run(host='0.0.0.0')

