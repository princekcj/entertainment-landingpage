from flask import render_template, request
from CSElandingpage import app, db
from CSElandingpage.csemodels import Emails

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_email = request.form['email']
        add_email = Emails(email=new_email)
        db.session.add(add_email)
        db.session.commit()
    return render_template('index.html')
