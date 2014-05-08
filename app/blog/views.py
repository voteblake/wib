from flask import render_template, url_for
from . import blog

@blog.route('/')
@blog.route('/posts')
def posts():
    posts = (p for p in flatpages if 'date' in p.meta)
    latest = sorted(posts, reverse=True, key=lambda p: p.meta['date'])
    return render_template('posts.html', posts=latest)

@blog.route('/posts/<name>/')
def post(name):
    path = '{}/{}'.format(POST_DIR, name)
    post = flatpages.get_or_404(path)
    return render_template('post.html', post=post)
