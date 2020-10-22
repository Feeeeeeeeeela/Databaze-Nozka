from . import app
from flask import render_template


@app.route('/')
def index():
    pi=3.141519
    e=2.7
    title = 'Index'
    return render_template('base.html.j2', pi=pi, title=title)


@app.route('/info/')
def info():
    title = 'Info'
    return render_template('info.html.j2', title=title)

@app.route('/Květák')
def kvetak():
    title = 'Květák'
    return render_template('kvetak.html.j2', title=title)

@app.route('/Kapusta')
def kapusta():
    title = 'Kapusta'
    return render_template('kapusta.html.j2', title=title)

@app.route('/Banány')
def banany():
    title = 'Banány'
    return render_template('banany.html.j2', title=title)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html.j2')
