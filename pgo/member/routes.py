from flask import Flask, render_template, redirect, url_for, Blueprint
from pgo.member.register import register_F

rmember = Blueprint('rmember', __name__)


@rmember.route("/")
def homeuser():
    return render_template("members/home.html")


@rmember.route("/register", methods=['GET', 'POST'])
def regis():
    form = register_F()
    if form.validate_on_submit():
        return redirect(url_for('rmember.regis'))
    return render_template("members/register.html", form=form)


@rmember.route("/login", methods=['GET', 'POST'])
def login():
    form = register_F()
    if form.validate_on_submit():
        return redirect(url_for('rmember.login'))
    return render_template("members/login.html", form=form)
