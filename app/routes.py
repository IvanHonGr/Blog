from flask import render_template
from app import blog

@blog.route('/')
@blog.route('/index')
def index():
    user = {'username':'Ivan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@blog.route('/secret')
def secret():
    return "not so smart"
