import configparser

# Create a ConfigParser object
config = configparser.ConfigParser()

# Read the properties file
config.read('basket_compare_playground/pl/jacek/services/apps/basketcompare/config/application.properties')

# Initialize constants from properties file
BUYBOX_API_URL = config.get('BuyBoxApi', 'BUYBOX_API_URL')
BUYBOX_API_ID = config.get('BuyBoxApi', 'BUYBOX_API_ID')

SELECTED_PRODUCTS_SESSION_KEY = config.get('AppSessionProperties', 'SELECTED_PRODUCTS_SESSION_KEY')
BASKET_COMPARE_SESSION_KEY = config.get('AppSessionProperties', 'BASKET_COMPARE_SESSION_KEY')
BASKET_SESSION_KEY = config.get('AppSessionProperties', 'BASKET_SESSION_KEY')
