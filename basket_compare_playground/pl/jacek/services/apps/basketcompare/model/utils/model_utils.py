def sort_products_by_price(products):
    return sorted(products, key=lambda x: x.price)


def sort_baskets_by_total_price(baskets):
    return sorted(baskets, key=lambda x: x.total_price)
