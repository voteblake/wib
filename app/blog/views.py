from flask import render_template, url_for
from . import blog

from app import pages

@blog.route('/')
@blog.route('/posts')
def posts():
    posts = (p for p in pages)
    latest = sorted(posts, reverse=True, key=lambda p: p.meta['date'])
    return render_template('blog/posts.html', posts=latest)

@blog.route('/<path:path>/')
def post(path):
    post = pages.get_or_404(path)
    return render_template('blog/post.html', post=post)
