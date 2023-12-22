import json
from flask import Flask, request, jsonify

app = Flask(__name__)

tarefas = [
    {
        "id": 4,
        "responsável": "Vitor",
        "tarefa": "Lavar os pratos",
        "status": "em andamento"
    },
    {
        "id": 10,
        "responsável": "Adilson",
        "tarefa": "Varrer a casa",
        "status": "concluída"
    },
    {
        "id": 25,
        "responsável": "Ana",
        "tarefa": "Levar o cachorro para passear",
        "status": "a fazer"
    },
]


@app.route("/")
def hello():
    return "Olá mundo!"


@app.route("/tarefa/<int:id>/", methods=["GET", "PUT", "DELETE"])
def handle_tarefa(id):
    if request.method == "GET":
        tarefa = list(filter(lambda tarefa: tarefa["id"] == id, tarefas))
        return jsonify(tarefa[0])
    elif request.method == "PUT":
        dados = json.loads(request.data)
        for i, tarefa in enumerate(tarefas):
            if tarefa["id"] == id:
                tarefas[i]["status"] = dados["status"]
        return jsonify({"status": "sucesso", "mensagem": "Tarefa atualizada"})
    elif request.method == "DELETE":
        for i, tarefa in enumerate(tarefas):
            if tarefa["id"] == id:
                tarefas.pop(i)
        return jsonify({"status": "sucesso", "mensagem": "Tarefa excluída"})


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)


@app.route("/criartarefa", methods=["POST"])
def criar_tarefa():
    tarefa = json.loads(request.data)
    tarefas.append(tarefa)
    return jsonify({"status": "sucesso", "mensagem": "Tarefa cadastrada"})


if __name__ == '__main__':
    app.run(debug=True)
