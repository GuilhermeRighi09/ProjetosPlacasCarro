from flask import jsonify, render_template, redirect, url_for, request, Flask

from controllers.veiculo_controller import (
    buscar_veiculos_controller,
    salvar_veiculo_controller,
    deletar_veiculo_controller,
    buscar_veiculo_por_id_controller,
    atualizar_veiculo_controller
)

app = Flask(__name__)


@app.route('/')
def index():
    dados_veiculo = {
        "nome": "Aguardando Leitura...",
        "curso": "-",
        "placa": "------",
        "status": "-"
    }
    return render_template('index.html', dados=dados_veiculo)



@app.route('/admin', methods=['GET'])
def listar_veiculos():
    try:
        veiculos = buscar_veiculos_controller()
        return render_template("admin.html", veiculos=veiculos)
    except Exception as ex:
        print('Erro na lista de veículos:', str(ex))
        return jsonify({'message': 'Erro ao buscar dados'}), 500



@app.route("/novo", methods=["GET", "POST"])
def novo_veiculo():
    try:
        if request.method == 'POST':
            dados = request.form.to_dict()
            salvar_veiculo_controller(dados)
            return redirect(url_for("listar_veiculos"))

        return render_template("novo_veiculo.html")
    except Exception as ex:
        print("Erro ao salvar o veículo:", str(ex))
        return jsonify({"message": "Erro interno no Servidor"}), 500



@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_veiculo(id):
    try:
        deletar_veiculo_controller(id)
        return redirect(url_for("listar_veiculos"))
    except Exception as ex:
        print('Erro ao deletar:', str(ex))
        return jsonify({"message": "Erro interno no Servidor"}), 500



@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_veiculo(id):
    try:
        if request.method == 'POST':
            dados = request.form.to_dict()

            atualizar_veiculo_controller(id, dados)

            return redirect(url_for('listar_veiculos'))

        veiculo = buscar_veiculo_por_id_controller(id)
        if veiculo:
            return render_template('editar_veiculo.html', veiculo=veiculo)

        return "Veículo não encontrado", 404

    except Exception as ex:
        print('Erro ao editar:', str(ex))
        return jsonify({"message": "Erro interno no Servidor"}), 500


if __name__ == '__main__':
    app.run(debug=True)
