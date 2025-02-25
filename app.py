from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db = SQLAlchemy(app)
#this is the database creration class
class todo(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    desc = db.Column(db.String(200),nullable=False)
    date = db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/")
def hello_world():
    return render_template('index.html')
    
@app.route("/menu")
def heya():
    return "this is the menu"

if __name__=="__main__":
    app.run(debug=True,port=8000)