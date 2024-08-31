from flask import Flask, jsonify, request


app = Flask(__name__)

bandas = [
    {
        'id': 1,
        'banda': 'System Of A Down',
        'genero': 'NU metal'
    },
    {
        'id': 2,
        'banda': 'Ghost',
        'genero': 'Heavy metal'
    },
    {
        'id': 3,
        'banda': 'Slipknot',
        'genero': 'Groove metal'
    },
    {
        'id': 4,
        'banda': 'Limp Bizkit',
        'genero': 'NU metal'
    },
    {
        'id': 5,
        'banda': 'Avatar',
        'genero': 'Heavy Metal'
    },
]

#consultar(todos)
@app.route('/bandas', methods=['GET'])
def obter_bandas():
    return jsonify(bandas)

#consultar por id
@app.route('/bandas/<int:id>', methods=['GET'])
def buscar_id(id):
    for banda in bandas:
       if banda.get('id') == id:
           return jsonify(banda)

#editar
@app.route('/bandas/<int:id>', methods=['PUT'])
def editar_banda_por_id(id):
    alteracao = request.get_json()
    for indice,banda in enumerate(bandas):
        if banda.get('id') == id:
            bandas[indice].update(alteracao)
            return jsonify(bandas[indice])
        
#criar
@app.route('/bandas/<int:id>', methods=['POST'])
def incluir_banda():
    nova_banda = request.get_json()
    bandas.append(nova_banda)

    return jsonify(bandas)

#excluir
@app.route('/bandas/<int:id>', methods=['DELETE'])
def exluir_banda(id):
    for indice, banda in enumerate(bandas):
        if banda.get('id') == id:
            del bandas[indice]

    return jsonify(bandas)

app.run(port=5000, host='localhost', debug=True)