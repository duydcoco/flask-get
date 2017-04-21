#coding:utf-8

from app import app
from flask import render_template
from forms import LoginForm
from flask import flash
from flask import redirect


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


@app.route("/login",methods=['get','post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
                           title = 'Sign In',
                           form = form,
                           providers = app.config['OPENID_PROVIDERS'])

