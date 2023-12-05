from flask import Flask, render_template, request, url_for, flash, redirect
from flask_assets import Environment, Bundle
from pklbase import pickle_db
import random
app = Flask(__name__)

pdb = pickle_db("data/guests.pickle")


@app.route('/',methods=('GET', 'POST'))
def evite():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if not name:
            flash('Title is required!')
        elif not email:
            flash('Content is required!')
        else:
            rpic = random.randrange(1,24)
            pdb.insert({'name':name,"email":email,"pic":rpic})
            return redirect(url_for('guestlist'))
    return render_template('evite.html')

@app.route('/guestlist')
def guestlist():
    glist = pdb.getall()
    return render_template('guestlist.html',guests = glist,numguests = len(glist))

