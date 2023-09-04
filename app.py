from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Récupération des variables d'environnement
pg_user = os.environ.get('PG_USER', 'default_user')
pg_password = os.environ.get('PG_PASSWORD', 'default_password')
pg_db = os.environ.get('PG_DB', 'default_db')
pg_host = os.environ.get('PG_HOST', 'localhost')

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{pg_user}:{pg_password}@{pg_host}/{pg_db}'
db = SQLAlchemy(app)

# Modèle simple pour une table 'users'
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
# Modèle simple pour une table 'mydatabase'
class Mydatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mydatabase = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return f'<Mydatabase {self.mydatabase}>'
    


@app.route('/')
def hello():
    users = User.query.all()
    # Affiche les utilisateurs sur la page d'accueil
    return '<br>'.join([user.username for user in users])

@app.route('/add_user/<username>')
def add_user(username):
    new_user = User(username=username)
    db.session.add(new_user)
    db.session.commit()
    return f'User {username} added'



if __name__ == '__main__':
    db.create_all()  # Crée les tables si elles n'existent pas
    new_user = User(username='admin')
    # Ajoute l'utilisateur 'admin' si il n'existe pas
    if not User.query.filter_by(username='admin').first():
        db.session.add(new_user)    

    db.session.commit()
    app.run(host='0.0.0.0', port=80)

