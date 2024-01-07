from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))  # Remove nullable=False
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user:
            print(f"Entered password: {password}")
            print(f"Stored hashed password: {user.password}")

            if check_password_hash(user.password, password):
                session['user_id'] = user.id
                flash('Login successful!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Login unsuccessful. Please check your username and password.', 'danger')
        else:
            flash('User not found. Please check your username.', 'danger')

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        posts = Post.query.all()  # Fetch all posts
        return render_template('dashboard.html', user=user, posts=posts)
    else:
        flash('You need to log in first.', 'warning')
        return redirect(url_for('login'))

@app.route('/create_post', methods=['POST'])
def create_post():
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        title = request.form['title']
        content = request.form['content']

        new_post = Post(title=title, content=content, user=user)
        db.session.add(new_post)
        db.session.commit()
        flash('Post created successfully.', 'success')

    return redirect(url_for('dashboard'))

@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        post = Post.query.get(post_id)

        if post and (user.id == post.user.id):
            db.session.delete(post)
            db.session.commit()
            flash('Post deleted successfully.', 'success')
        else:
            flash('Unable to delete the post.', 'danger')

    return redirect(url_for('dashboard'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = generate_password_hash(password)

        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
