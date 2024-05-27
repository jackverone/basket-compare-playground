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
from basket_compare_playground.pl.jacek.services.apps.basketcompare.controller.search_product_form import \
    SearchProductForm
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.constants import PRODUCT_SEARCH_SESSION_KEY

app = Flask(__name__)
app.secret_key = "your another secret key"
app.debug = True

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s in %(filename)s %(module)s %(funcName)s: %(message)s"
)

buybox_service = BuyBoxService()
product_repository = ProductRepository()
basket_repository = BasketRepository()
basket_compare_repository = BasketCompareRepository()

product_service = ProductService(product_repository, buybox_service)
basket_service = BasketService(product_service, basket_repository)
basket_compare_service = BasketCompareService(basket_compare_repository)

product_controller = ProductController(product_service, product_repository)
basket_controller = BasketController(basket_service)
basket_compare_controller = BasketCompareController(basket_compare_service)


@app.errorhandler(404)
def page_not_found(e):
    logging.error(f"Page not found: {e}")
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    logging.error(f"Internal server error: {e}")
    return render_template("500.html"), 500


@app.route("/")
def home():
    logging.info(f"home()")
    basket_repository.clear_all_products()
    session.clear()

    if PRODUCT_SEARCH_SESSION_KEY not in session:
        session[PRODUCT_SEARCH_SESSION_KEY] = False

    logging.info(f"Session: {session}")
    return render_template("dashboard.html")


@app.route("/products")
def get_products():
    # products = product_controller.get_all_products()
    products = {}
    return render_template("products.html", products=products)


@app.route("/baskets")
def get_baskets():
    # baskets = basket_controller.get_all_baskets()
    baskets = {}
    return render_template("baskets.html", baskets=baskets)


@app.route("/basket_compare")
def get_basket_compare():
    app.logger.info(f"get_basket_compare()")

    products = basket_controller.get_all_products()
    basket_compare = basket_controller.create_basket_compare(products)

    return render_template("basket_compare.html", basket_compare=basket_compare)


@app.route("/products/search")
def search_products_view():
    app.logger.info("search_products_view()")
    form = SearchProductForm()
    return render_template("product_search.html", product_meta_data=None, form=form)


@app.route("/products/search", methods=["POST"])
def search_products_post():
    logging.info("search_products_post()")
    form = SearchProductForm(request.form)
    logging.info(f"Form: {form}")

    if form.validate():
        name = form.name.data
        info = form.info.data
        logging.info(f"search_products_post({name}, {info})")

        product_meta_data = product_controller.search_product_meta_data(name, info)

        return render_template("product_search.html", product_meta_data=product_meta_data, form=SearchProductForm())
    return render_template("product_search.html", form=form)


@app.route("/products/add", methods=["POST"])
def add_product_to_basket():
    name = request.form["name"]
    info = request.form["info"]
    logging.info(f"Adding product with name: {name} and info: {info} to basket compare")

    added_product: Product = basket_controller.search_and_add_product(name, info)
    logging.info(f"Added product: added_product")

    session[PRODUCT_SEARCH_SESSION_KEY] = True
    logging.info(f"Session: {session}")

    return render_template("product_search.html", product_meta_data=None, form=SearchProductForm())


if __name__ == "__main__":
    app.run(debug=True)
