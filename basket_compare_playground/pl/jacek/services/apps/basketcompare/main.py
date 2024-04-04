import logging

from flask import Flask, session, render_template, request

from basket_compare_playground.pl.jacek.services.apps.basketcompare.controller.ProductController import \
    ProductController
from basket_compare_playground.pl.jacek.services.apps.basketcompare.controller.BasketController import BasketController
from basket_compare_playground.pl.jacek.services.apps.basketcompare.controller.BasketCompareController import \
    BasketCompareController

from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.ProductRepository import \
    ProductRepository
from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.BasketRepository import BasketRepository
from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.BasketCompareRepository import \
    BasketCompareRepository

from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.ProductService import ProductService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.BasketService import BasketService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.BasketCompareService import \
    BasketCompareService

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

product_repository = ProductRepository()
basket_repository = BasketRepository()
basket_compare_repository = BasketCompareRepository()

product_service = ProductService(product_repository)
basket_service = BasketService(basket_repository)
basket_compare_service = BasketCompareService(basket_compare_repository)

product_controller = ProductController(product_service)
basket_controller = BasketController(basket_service)
basket_compare_controller = BasketCompareController(basket_compare_service)


@app.route('/')
def home():
    return render_template('dashboard.html')


@app.route('/products')
def get_products():
    # products = product_controller.get_all_products()
    products = {}
    return render_template('products.html', products=products)


@app.route('/baskets')
def get_baskets():
    # baskets = basket_controller.get_all_baskets()
    baskets = {}
    return render_template('baskets.html', baskets=baskets)


@app.route('/basket_compares')
def get_basket_compares():
    # basket_compares = basket_compare_controller.get_all_basket_compares()
    basket_compares = basket_compare_controller.get_basket_compare(
        "Alchemik", "Paulo+Coelho")
    return render_template('basket_compares.html', basket_compares=basket_compares)


@app.route('/products/search')
def search_products():
    return render_template('product_search.html', products=None)


@app.route('/products/search', methods=['POST'])
def search_products_post():
    name = request.form['name']
    info = request.form['info']
    logging.info(f"Searching for products with name: {name} and info: {info}")

    products = basket_compare_controller.get_basket_compare(name, info)
    # products = None

    return render_template('product_search.html', products=products)


@app.route('/products/add', methods=['POST'])
def add_product_to_basket_compare():
    name = request.form['name']
    info = request.form['info']
    logging.info(f"Adding product with name: {name} and info: {info} to basket compare")

    # basket_compare_controller.create_basket_compare(name, info)

    return render_template('product_search.html', products=None)


if __name__ == '__main__':
    app.run(debug=True, extra_dirs=['basket_compare_playground'])
