# -*- coding: utf-8 -*-
from flask import Flask, request

from main import insertUsuario

app = Flask("API")

@app.route("/olamundo", methods=["GET"])
def olaMundo():
  return{"ola": "mundo"}

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():

  body = request.get_json()

  if("nome" not in body):
    return geraResponse(400, "O parâmetro 'nome' é obrigatório")  

  if("email" not in body):
    return geraResponse(400, "O parâmetro 'email' é obrigatório")

  if("senha" not in body):
    return geraResponse(400, "O parâmetro 'senha' é obrigatório")    


  usuario = insertUsuario(body["nome"], body["email"], body["senha"])

  return geraResponse(200, "Usuario criado", "user", usuario)

def geraResponse(status, mensagem, nome_conteudo = False, conteudo = False):
  response = {}
  response["status"] = status
  response["mensagem"] = mensagem
  
  if(nome_conteudo and conteudo):
    response[nome_conteudo] = conteudo

  return response   

app.run()









