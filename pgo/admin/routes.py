from flask import Flask, render_template, redirect, url_for, Blueprint

from pgo.admin.game import games_F

radmin = Blueprint('radmin', __name__)


@radmin.route("/admin")
def home():
    return render_template("admin/dashboard.html")


@radmin.route("/admin/member")
def member():
    return render_template("admin/member.html")


@radmin.route("/admin/games", methods=['GET', 'POST'])
def games():
    formgame = games_F()
    if formgame.validate_on_submit():
        return redirect(url_for('radmin.games'))
    return render_template("admin/game.html",  form=formgame)
