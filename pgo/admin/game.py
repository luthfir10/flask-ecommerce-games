from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class games_F(FlaskForm):
    kode_games = StringField('Kode Game', validators=[DataRequired()])
    judul = TextAreaField('Judul', validators=[DataRequired()])
    tag_games = StringField('Tag Game', validators=[DataRequired()])
    harga_beli = IntegerField('Harga Beli', validators=[DataRequired()])
    harga_jual = IntegerField('Harga Jual', validators=[DataRequired()])
    stok = IntegerField('Stok', validators=[DataRequired()])
    submit = SubmitField('Tambah')
