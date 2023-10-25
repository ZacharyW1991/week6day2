from phonebook import app
from flask import render_template, url_for, redirect
from phonebook.forms import SubmitForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['get', 'post'])
def submission():
    form=SubmitForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        first_name=form.first_name.data
        last_name=form.last_name.data
        phone=form.phone.data
        address=form.address.data
        print(first_name, last_name, address, phone)
        return redirect(url_for('index'))
    return render_template('submit.html', form=form)
