from flask import Flask, render_template, redirect
from flask_login import LoginManager, current_user
from werkzeug.exceptions import HTTPException
import forms

app = Flask(__name__)
app.secret_key = 'asdfghjksdfghjsdfghj'

login_manager=LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
	return User.get(user_id)


@app.errorhandler(404)
def page_not_found(error):
	return render_template('404.html'), 404


@app.route('/')
def index():
	if current_user.is_authenticated:
		# Show user profile page
		pass
	else:
		return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
	login_form = forms.LoginForm()
	if login_form.validate_on_submit():
		# Show user profile page
		pass
	else:
		return render_template('login.html', login_form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
	register_form = forms.RegisterForm()
	if register_form.validate_on_submit():
		# Handle user registration
		pass
	else:
		return render_template('register.html', register_form=register_form)


if __name__ == '__main__':
	app.run(debug=True, host='127.0.0.1', port=8080)