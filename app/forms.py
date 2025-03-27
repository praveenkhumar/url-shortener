# Form validation and handling

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class URLForm(FlaskForm):
    original_url = StringField('URL', 
        validators=[DataRequired(), URL(message='Invalid URL')],
        render_kw={"placeholder": "Enter your long URL here"}
    )
    submit = SubmitField('Shorten')