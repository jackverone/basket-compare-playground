class ProductMetaData:
    def __init__(self, status, space_id, tracking_url, sort_type, use_css, use_tabs, default_tab, lead_color,
                 show_product, shop_style, version, language, show_prices, send_ga_client_id, button_label, row_count,
                 statistics, name, info, image, shop_name: str = ""):
        self.status = status
        self.space_id = space_id
        self.tracking_url = tracking_url
        self.sort_type = sort_type
        self.use_css = use_css
        self.use_tabs = use_tabs
        self.default_tab = default_tab
        self.lead_color = lead_color
        self.show_product = show_product
        self.shop_style = shop_style
        self.version = version
        self.language = language
        self.show_prices = show_prices
        self.send_ga_client_id = send_ga_client_id
        self.button_label = button_label
        self.row_count = row_count
        self.statistics = statistics
        self.name = name
        self.info = info
        self.image = image
        self.shop_name = shop_name

    def __str__(self):
        return (f"ProductMetaData(status={self.status}, space_id={self.space_id}, tracking_url={self.tracking_url}, "
                f"sort_type={self.sort_type}, use_css={self.use_css}, use_tabs={self.use_tabs}, default_tab={self.default_tab}, "
                f"lead_color={self.lead_color}, show_product={self.show_product}, shop_style={self.shop_style}, "
                f"version={self.version}, language={self.language}, show_prices={self.show_prices}, "
                f"send_ga_client_id={self.send_ga_client_id}, button_label={self.button_label}, row_count={self.row_count}, "
                f"statistics={str(self.statistics)}, name={self.name}, info={self.info}, image={self.image}, "
                f"shop_name={self.shop_name})")

    def __repr__(self):
        return self.__str__()
