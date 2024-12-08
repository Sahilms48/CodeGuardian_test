import secrets
import bcrypt
from flask import Flask, request, render_template_string, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
        # Here you would typically save the username and hashed_password to a database
        session['username'] = form.username.data
        return f"Registration successful for {session['username']}"
    
    return render_template_string('''
        <form method="POST">
            {{ form.hidden_tag() }}
            <div>{{ form.username.label }}: {{ form.username() }}</div>
            <div>{{ form.password.label }}: {{ form.password() }}</div>
            <div>{{ form.confirm_password.label }}: {{ form.confirm_password() }}</div>
            <div>{{ form.submit() }}</div>
        </form>
    ''', form=form)

if __name__ == '__main__':
    app.run(debug=False)
