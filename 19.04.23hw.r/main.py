from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

def create_post_route():
    def decorator(func):
        def wrapper():
            if request.method == 'POST':
                title = request.form['title']
                content = request.form['content']
                post = Post(title, content)
                posts.append(post)
                return redirect('/')
            return func()
        return wrapper
    return decorator

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/create_post', methods=['GET', 'POST'])
@create_post_route()
def create_post():
    return render_template('create_post.html')

if __name__ == '__main__':
    app.run()
