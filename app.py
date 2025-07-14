from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Irasas(db.Model):
    __tablename__ = "Post"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime)
    autorius = db.Column(db.String)
    pavadinimas = db.Column(db.String)
    tekstas = db.Column(db.Text)
    status = db.Column(db.String)

with app.app_context():
    db.create_all()

# data =[{
#     'data':'2020 01 01',
#     'autorius': 'Autorius 1',
#     'pavadinimas': 'Apie nieką',
#     'tekstas': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris.',
#     'status': 'published'
# },
# {
#     'data':'2020 02 01',
#     'autorius': 'KITAS AUTORIUS',
#     'pavadinimas': 'Apie zombius',
#     'tekstas': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris. ',
#     'status': 'unpublished'
# },
# {
#     'data':'2020 03 01',
#     'autorius': 'Dar kažkas',
#     'pavadinimas': 'Braiiins!',
#     'tekstas': 'Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit​​, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris.',
#     'status': 'published'
# }]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/posts")
def posts():
    posts = Irasas.query.all()
    return render_template("posts.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == '__main__':
  app.run(debug=True)
