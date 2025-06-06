from flask import render_template, redirect, url_for, request
from app import app

users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        hobby = request.form['hobby']
        if name:
            users.append({'name': name, 'age': age, 'city': city, 'hobby': hobby})
            return redirect(url_for('index'))
    return render_template('user_data.html', users=users)