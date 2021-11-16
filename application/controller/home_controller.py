from application import app
from flask import Flask, render_template, request, url_for, jsonify

#product_list = ProductDAO()


@app.route('/')
def index():
    return render_template("home.html")


@app.route("/busca")
def busca():
    return render_template("home.html")
