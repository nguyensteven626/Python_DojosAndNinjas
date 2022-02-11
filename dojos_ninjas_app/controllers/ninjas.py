from flask import render_template, request, redirect, session 
from dojos_ninjas_app import app 
from dojos_ninjas_app.models import dojo, ninja
from dojos_ninjas_app.models.ninja import Ninja 

@app.route('/ninjas')
def ninja_form():

    return render_template('ninja.html', all_dojos = dojo.Dojo.get_dojo())

# @app.route('/add_ninja/ninjas', methods = ['POST'])
# def create_ninja():
#     data = {
#         'first_name':request.form['first_name'],
#         'last_name':request.form['last_name'],
#         'age':request.form['age'],
#         'dojo_id':request.form['dojo_id']
#     }
#     ninja.Ninja.save(data)
#     return redirect('/')


@app.route('/add_ninja/ninjas', methods = ['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    return redirect('/ninjas')

# @app.route('/add_ninja')
# def add_ninja():
#     data = {
#         'first_name':request.form['first_name'],
#         'last_name':request.form['last_name'],
#         'age':request.form['age']
#     }
#     one_ninja = Ninja.get_ninja(data)
#     return redirect('/show')

