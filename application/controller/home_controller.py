from application import app
from application.model.dao.produtoDAO import ProdutoDao
from application.model.entity.produto import Produto
from flask import Flask, render_template, request, url_for, jsonify

product_dao = ProdutoDao()
product_list = product_dao.product_list()
print(product_list)


@app.route('/')
def index():
    return render_template("home.html")


@app.route("/produtos")
def produtos():
    return render_template("products.html", product_list=product_list[0:4])
