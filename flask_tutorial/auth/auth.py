from flask import Blueprint, redirect, render_template, flash, session, request


auth = Blueprint("auth", __name__, template_folder='templates')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'user' in session:
            flash(f'Already logged in, {session["user"]}')
            return redirect(url_for("show_name_page"))
        return render_template('login.html')
    else:
        username = request.form["username"]
        session.permanent = True         # before setting the session, set its permanence

        session["user"] = username

        found_user = User.query.filter_by(name=username).first()
        if found_user:
            session['email'] = found_user.email
        else:
            usr = User(username, "")
            db.session.add(usr)
            db.session.commit()
        flash(f'you have been logged in, {username}')

        return redirect(url_for('show_name_page'))


@auth.route('/logout')
def logout():
    session.pop('user')
    flash('You have been logged out')
    return redirect(url_for('login'))
