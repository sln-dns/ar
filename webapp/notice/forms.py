from flask_wtf import FlaskForm
from wtforms import HiddenField, StringField, SubmitField
from wtforms.validators import DataRequired



class NoticeForm(FlaskForm):
    #notice_id = HiddenField('Id объявления', validators=[DataRequired()])
    notice_title = StringField('Заголовок объявления', validators=[DataRequired()], render_kw={"class": "btn btn-secondary"})
    notice_text = StringField('Текст объявления', validators=[DataRequired()], render_kw={"class": "btn btn-secondary"})
    submit = SubmitField('Опубликовать', render_kw={"class": "btn btn-secondary"})