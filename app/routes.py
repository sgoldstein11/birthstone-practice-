from flask import render_template, request, redirect
from app import app
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['GET', 'POST'])
def results ():
    #return "breakfast" 
    if request.method == 'GET':
        return breakfast 
    else:
        userdata = formopener.dict_from(request.form)
        #userdata = request.form
        print (userdata)
        #month = userdata['month']
        return render_template('results.html')


    
