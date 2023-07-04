from flask import Flask, render_template, request

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = {'title': title, 'content': content}
        posts.append(post)
        return redirect('/')
    return render_template('create_post.html')

if __name__ == '__main__':
    app.run()
