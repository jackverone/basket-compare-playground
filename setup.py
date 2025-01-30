from setuptools import setup, find_packages

setup(
    name="basket_compare_playground",
    version="0.1.0",
    url="https://github.com/jackverone/basket-compare-playground",
    author="Jacek Services",
    author_email="jacek.services@gmail.com",
    description="App enables basket comparison for selected products.",
    packages=find_packages(),
    install_requires=[
        "python-dotenv",
        "blinker==1.8.2",
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "click==8.1.7",
        "Flask==3.0.3",
        "gunicorn==20.1.0",
        "idna==3.7",
        "itsdangerous==2.2.0",
        "Jinja2==3.1.4",
        "MarkupSafe==2.1.5",
        "requests==2.31.0",
        "setuptools==68.2.2",
        "urllib3==2.2.1",
        "Werkzeug==3.0.3",
        "WTForms==3.1.2"
    ],
)
