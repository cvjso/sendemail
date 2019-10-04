from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    abort,
    url_for,
)
from sitehosp import forms
from sitehosp.forms import formularioLogin
from sitehosp import app
import send_email2 as sender


@app.route("/", methods=["GET", "POST"])
def home():
    form = formularioLogin()
    if request.method == "POST" and form.validate():
        sender.send_mail(form.email.data)
    return render_template("index.html", form=form)
