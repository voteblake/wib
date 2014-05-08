from flask import render_template, flash, redirect, url_for
from . import blog

@blog.route('/')
@blog.route('/posts')
def posts():
    posts = [p for p in flatpages]
    posts.sort(key=lambda item: item['date'], reverse=False)
    return render_template('posts.html', posts=posts)

@blog.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)
