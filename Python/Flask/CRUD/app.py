from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    #posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime)

    def __init__(self, username, email, about_me):
        self.username = username
        self.email = email
        self.about_me = about_me
    

@app.route('/')
@app.route('/index')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            users = User(request.form['username'], request.form['email'], request.form['about_me'])
            db.session.add(users)
            db.session.commit()
        except:
            print('Falha ao gravar os dados')
            render_template('add.html') 
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    users = User.query.get(id)
    if request.method == 'POST':
        try:
            users.username = request.form['username']
            users.email = request.form['email']
            users.about_me = request.form['about_me']
            db.session.commit()
        except:
            print('Não foi possível editar o usuário.')
            return render_template('edit.html', users=users)        
        return redirect(url_for('index'))
    return render_template('edit.html', users=users)

@app.route('/delete/<int:id>')
def delete(id):
    try:
        users = User.query.get(id)
        db.session.delete(users)
        db.session.commit()
    except:
        print('Não foi possível excluir os dados.')
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

