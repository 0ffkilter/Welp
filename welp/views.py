from flask import render_template

from welp import welp

@welp.route('/')
def index():
    return render_template('index.html')
