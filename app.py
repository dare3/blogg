"""Blogly application."""

from flask import Flask, redirect, render_template, request, url_for
from models import Post, connect_db, db, User
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secretkey'

toolbar = DebugToolbarExtension(app)

connect_db(app)

# Ensure the database tables are created within the application context
with app.app_context():
    db.create_all()

@app.route('/users/<int:user_id>/posts/new')
def new_post(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('new_post.html', user_id=user_id)

@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def add_post(user_id):
    title = request.form['title']
    content = request.form['content']

    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    return redirect(url_for('show_user', user_id=user_id))

@app.route('/posts/<int:post_id>')
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('detail_post.html', post=post)

@app.route('/posts/<int:post_id>/edit')
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('edit_post.html', post=post)

@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    post.title = request.form['title']
    post.content = request.form['content']

    db.session.commit()
    return redirect(url_for('show_post', post_id=post.id))

@app.route('/posts/<int:post_id>/delete', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    user_id = post.user_id
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('show_user', user_id=user_id))
