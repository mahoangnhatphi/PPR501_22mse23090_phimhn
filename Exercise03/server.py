from flask import Flask, flash, render_template, request

from Post import Post
from module.database import Database

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"
db = Database()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create', methods=['GET'])
def create():
    return render_template('create.html')


@app.route('/edit/<int:id>/', methods=['GET'])
def edit(id):
    post = db.get_post_by_id(id)
    return render_template('edit.html', post=post)


@app.route('/edit/<int:id>/', methods=['POST'])
def update_edit(id):
    form = request.form
    title = form.get('title')
    content = form.get('content')
    post = Post(id, title, content, None)
    if db.update(post):
        flash("A post has been updated")
    else:
        flash("A post can not be updated")
    post = db.get_post_by_id(id)
    return render_template('edit.html', post=post)


@app.route('/posts', methods=['GET'])
def posts():
    posts = db.get_posts()
    return render_template('post.html', posts=posts)


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    if db.delete(id):
        flash("A post has been deleted")
    else:
        flash("A post can not be deleted")
    return posts()


@app.route('/create', methods=['POST'])
def create_posts():
    form = request.form
    title = form.get('title')
    content = form.get('content')
    post = Post(None, title, content, None)
    if db.insert(post):
        flash("A post has been added")
    else:
        flash("A post can not be added")
    return posts()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')


if __name__ == '__main__':
    app.run(port=8181, host="0.0.0.0")
