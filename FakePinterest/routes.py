#Criar rotas no nosso site(os links)
from flask import render_template, url_for
from FakePinterest import app
from flask_login import login_required
from FakePinterest.forms import FormLogin, FormCriarConta

@app.route("/", methods=["GET", "POST"])
def homepage():
    formlogin = FormLogin()
    return render_template("homepage.html", form=formlogin)

@app.route("/criarconta", methods=["GET", "POST"])
def criarconta():
    formcriarconta = FormCriarConta()
    return render_template("criarconta.html", form=formcriarconta)


@app.route("/perfil/<usuario>")
@login_required
def Perfil(usuario):
    return render_template("perfil.html", usuario=usuario)
