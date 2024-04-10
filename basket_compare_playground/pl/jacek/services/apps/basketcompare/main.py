import logging

from flask import Flask, session, render_template, request

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.constants import (
    SELECTED_PRODUCTS_SESSION_KEY, BASKET_COMPARE_SESSION_KEY)

from basket_compare_playground.pl.jacek.services.apps.basketcompare.controller.product_controller import \
    ProductController
from basket_compare_playground.pl.jacek.services.apps.basketcompare.controller.basket_controller import BasketController
from basket_compare_playground.pl.jacek.services.apps.basketcompare.controller.BasketCompareController import \
    BasketCompareController

from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.ProductRepository import \
    ProductRepository
from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.BasketRepository import BasketRepository
from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.BasketCompareRepository import \
    BasketCompareRepository

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.service.BuyBoxService import \
    BuyBoxService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.product_service import ProductService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.basket_service import BasketService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.BasketCompareService import \
    BasketCompareService

app = Flask(__name__)
app.secret_key = 'your secret key'
app.debug = True

logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s in %(filename)s %(module)s %(funcName)s: %(message)s'
)

buybox_service = BuyBoxService()
product_repository = ProductRepository()
basket_repository = BasketRepository()
basket_compare_repository = BasketCompareRepository()

product_service = ProductService(product_repository, buybox_service)
basket_service = BasketService(basket_repository)
basket_compare_service = BasketCompareService(basket_compare_repository)

product_controller = ProductController(product_service, product_repository)
basket_controller = BasketController(basket_service)
basket_compare_controller = BasketCompareController(basket_compare_service)


@app.route('/')
def home():
    if SELECTED_PRODUCTS_SESSION_KEY not in session:
        session[SELECTED_PRODUCTS_SESSION_KEY] = {}

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
    # basket_compares = basket_compare_controller.get_basket_compare(
    #     "Alchemik", "Paulo+Coelho")
    products = session[SELECTED_PRODUCTS_SESSION_KEY]
    logging.info(f"get_basket_compares: {products}")
    return render_template('basket_compares.html', basket_compares=products)


@app.route('/basket_compares_buybox')
def get_basket_compares_buybox():
    # basket_compares = basket_compare_controller.get_all_basket_compares()
    basket_compares = basket_compare_controller.get_basket_compare(
        "Alchemik", "Paulo+Coelho")
    return render_template('basket_compares.html', basket_compares=basket_compares)


@app.route('/products/search')
def search_products_view():
    app.logger.info("search_products_view()")
    return render_template('product_search.html', products=None)


@app.route('/products/search', methods=['POST'])
def search_products_post():
    name = request.form['name']
    info = request.form['info']
    logging.info(f"search_products_post({name}, {info})")

    products = product_controller.search_product(name, info)
    # products = None

    return render_template('product_search.html', products=products)


@app.route('/products/add', methods=['POST'])
def add_product_to_basket():
    name = request.form['name']
    info = request.form['info']
    logging.info(f"Adding product with name: {name} and info: {info} to basket compare")

    product = product_controller.search_product(name, info)
    session[SELECTED_PRODUCTS_SESSION_KEY][product.space_id] = product

    return render_template('product_search.html', products=None)


if __name__ == '__main__':
    # app.run(debug=True, extra_dirs=['basket_compare_playground'])
    app.run(debug=True)
