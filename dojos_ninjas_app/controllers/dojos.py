from flask import render_template, redirect, request, session
from dojos_ninjas_app import app 
from dojos_ninjas_app.models.dojo import Dojo
from dojos_ninjas_app.models.ninja import Ninja 

@app.route('/')
def index():
    all_dojos = Dojo.get_dojo()
    return render_template('index.html', all_dojos = all_dojos)

@app.route('/add_dojo', methods = ['POST'])
def add_dojo():
    data = {
        'name':request.form['name']
    }
    Dojo.create_dojo(data)
    return redirect('/')
    
@app.route('/dojos/<int:id>')
def show_dojo(id):
    data = {
        'id':id
    }
    return render_template('show.html', display_dojo = Dojo.get_one_with_ninjas(data))




