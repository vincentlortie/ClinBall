from flask import Flask, render_template, redirect, url_for

from .forms import VariantSubmitForm
app = Flask(__name__)

import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/', methods=["GET"])
def predict():
    form = VariantSubmitForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run()
