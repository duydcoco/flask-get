#coding:utf-8

from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def hello():
    user = {'name':"flask"}
    title = "myflask-project"
    posts = [
        {"author":{"name":"jack"},
         "body":"beautiful ady in portland"
        },
        {
            "author":{"name":"nick"},
            "body":"a nice week"
        }
    ]
    return render_template("index.html",user=user,posts=posts,title=title)