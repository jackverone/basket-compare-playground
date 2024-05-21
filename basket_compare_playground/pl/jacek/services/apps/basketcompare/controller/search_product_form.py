from wtforms import Form, BooleanField, StringField, PasswordField, validators
from wtforms.fields.simple import SubmitField


class SearchProductForm(Form):
    name = StringField('Tytuł', validators=[validators.DataRequired("Wpisz tytuł książki.")])
    # info = StringField('Autor', validators=[validators.DataRequired()])
    submit = SubmitField('Szukaj')

    def __str__(self):
        return f"SearchProductForm(name={self.name}, info={self.info})"
