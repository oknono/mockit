from flask import Flask, render_template, url_for, redirect, request
from mockit import *

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/randompost', methods=['POST'])
def randompost():
    subreddit = request.form['subreddit']
    title = generate_post_title(subreddit)

    if not subreddit:
        return redirect(url_for('index'))

    return render_template('randompost.html', title=title, post="Work in Progess", subreddit=subreddit)

if __name__ == '__main__':
    app.run()
