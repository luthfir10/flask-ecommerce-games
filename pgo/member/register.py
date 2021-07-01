from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class register_F(FlaskForm):
    nopengenal = IntegerField('Nomor Pengenal', validators=[DataRequired()])
    nama = StringField('Nama', validators=[DataRequired()])
    alamat = TextAreaField('Alamat')
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
        DataRequired(), Length(min=6, max=25)])
    pas_konfi = PasswordField('Konfirmasi Password', validators=[
        DataRequired(), EqualTo('password')])
    submit = SubmitField('Tambah')
