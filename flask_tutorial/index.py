from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from auth import auth
# from platform import platform

# app setup
app = Flask(__name__)
app.secret_key = '39a03067f85a9b39c0c94ca50b5d445b7df18a04.zip'
app.permanent_session_lifetime = timedelta(days=4)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(auth.auth, url_prefix="")
# db setup
db = SQLAlchemy(app)


class User(db.Model):
    _id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route('/admin')
def admin_page():
    return redirect(url_for('show_name_page', name='Baba yaga!'))


@app.route('/views')
def views():
    return render_template('view.html', values=User.query.all())


@app.route('/')
def home():
    return render_template('index.html', content='You can\'t show me nothing')


@app.route('/user', methods=['GET', 'POST'])
def show_name_page():
    if "user" in session:
        if request.method == 'GET':
            return render_template('user.html', email=session['email'])
        else:
            email = request.form['email']
            session['email'] = email
            found_user = User.query.filter_by(name=session['user']).first()
            found_user.email = email
            db.session.commit()
            return render_template('user.html', email=session['email'])
    return redirect(url_for('login'))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
