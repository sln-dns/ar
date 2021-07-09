from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired
from flask_login import current_user
from datetime import datetime



class BoardForm(FlaskForm):
    #board_id = HiddenField('Id доски', validators=[DataRequired()])
    adress = StringField(
        'Адрес доски', 
        validators=[DataRequired()], 
        render_kw={"class": "btn btn-primary"},
        )
    memorys = StringField(
        'Заметки', 
        validators=[DataRequired()], 
        render_kw={"class": "btn btn-primary"},
        )
    submit = SubmitField('Создать', render_kw={"class": "btn btn-primary"})