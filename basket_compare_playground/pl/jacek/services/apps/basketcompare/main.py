import logging

from flask import Flask, render_template, request, session

from basket_compare_playground.pl.jacek.services.apps.basketcompare.controller.product_controller import \
    ProductController
from basket_compare_playground.pl.jacek.services.apps.basketcompare.controller.basket_controller import BasketController
from basket_compare_playground.pl.jacek.services.apps.basketcompare.controller.basket_compare_controller import \
    BasketCompareController

from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.ProductRepository import \
    ProductRepository
from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.basket_repository import BasketRepository
from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.BasketCompareRepository import \
    BasketCompareRepository

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.service.BuyBoxService import \
    BuyBoxService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.product_service import ProductService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.basket_service import BasketService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.basket_compare_service import \
    BasketCompareService

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product

app = Flask(__name__)
app.secret_key = 'your another secret key'
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
    session.clear()

    # if SELECTED_PRODUCTS_SESSION_KEY not in session:
    #     logging.info(f"Creating session for {SELECTED_PRODUCTS_SESSION_KEY}")
    #     session[SELECTED_PRODUCTS_SESSION_KEY] = {}
    #
    # if BASKET_COMPARE_SESSION_KEY not in session:
    #     logging.info(f"Creating session for {BASKET_COMPARE_SESSION_KEY}")
    #     session[BASKET_COMPARE_SESSION_KEY] = {}
    #
    # logging.info(f"Session: {session}")

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


@app.route('/basket_compare')
def get_basket_compare():
    app.logger.info(f"get_basket_compare()")

    products = basket_controller.get_all_products()
    basket_compare = basket_controller.create_basket_compare(products)
    app.logger.info(f"get_basket_compare() = {compares}")
    # for k, v in basket_compare.items():
    #     logging.info(f"create_basket_compare: k={k}, v={v} \n")
    #     for product in v:
    #         logging.info(f"create_basket_compare: product={product} \n")

    return render_template('basket_compare.html', basket_compare=basket_compare)


# @app.route('/basket_compares_buybox')
# def get_basket_compares_buybox():
#     # basket_compares = basket_compare_controller.get_all_basket_compares()
#     basket_compares = basket_compare_controller.get_basket_compare(
#         "Alchemik", "Paulo+Coelho")
#     return render_template('basket_compare.html', basket_compares=basket_compares)


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
    basket_controller.add_product(product)

    return render_template('product_search.html', products=None)


if __name__ == '__main__':
    app.run(debug=True)
