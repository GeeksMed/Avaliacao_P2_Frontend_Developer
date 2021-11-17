from application.model.entity.produto import Produto
import json

product_list = []


class ProdutoDao():
    def init(self):
        self.__product_list = product_list

    def dict_to_list(self, lista_prod):
        product_list = []
        for produto_item in lista_prod:
            produto = Produto()
            produto.set_id(produto_item['id'])
            produto.set_name(produto_item['name'])
            produto.set_image(produto_item['image'])
            produto.set_oldPrice(produto_item['oldPrice'])
            produto.set_price(produto_item['price'])
            produto.set_description(produto_item['description'])
            installments = produto_item['installments']
            produto.set_count(installments['count'])
            produto.set_value(installments['value'])
            product_list.append(produto)
        return product_list

    def product_list(self):
        product_list = []
        with open('application/controller/products.json', 'r') as file:
            produto_json = json.load(file)
            lista = self.dict_to_list(produto_json)
        return lista