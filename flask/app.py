from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample

app = Flask(__name__)
app.config['SECRET_KEY'] = "hibbidybibiddyboo"
debug = DebugToolbarExtension(app)   #same file name  /// won't appear unless template is used


#flask looks for app.py; if not in shell FLASK_APP=my_app.py flask run
# 'environment variable'
#another ' ' FLASK_ENV=development flask run (gives debug)
# export FLASK_ENV=development // permanent in venv for that session
#can update in bash profile for permanent
#in folder python3 -m venv venv
# source venv/bin/activate 

# ~~~~~~~~~~~~~~~~~~~~~adding routes~~~~~~~~~~~~~~~~~~~~
# /dogs /signin 

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/hello') #@ = decorator @classmethod -demands method or function directly after
def say_hello():
    return render_template('hello.html')

@app.route('/goodbye')
def say_by():
    return 'goOd bYe!'

#~~~~~~~~~~~~~~~~~~query strings~~~~~~~~~~~~~
#search?q=dogs&sort=top
# ImmutableMultiDict([('term', 'dog'), ('sort', 'top')])
# https://www.reddit.com/search/?q=dogs&sort=new
from flask import request

@app.route('/search')
def search():
    """Handle GET requests like /search?term=fun"""

    term = request.args["term"]
    #request.args is a dict-like obj of query param
    # use term to find db data that matches 'term'
    sort = request.args["sort"]
    return f"<h1>Search results for: {term}</h1> <p>Sorting by: {sort}</p>"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~post~~~~~~~~~~~~~~~~~~~
#can be mthod ['post','get']

# @app.route("/post", methods=["POST"])
# def post_demo():
#     return 'YOU MADE A POST REQUEST'


# @app.route("/post", methods=["GET"])
# def get_demo():
#     return 'YOU MADE A GET REQUEST'

@app.route('/add-comment')
def add_comment_form():
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type='text' placeholder='comment' name='comment'/>
                <input type='text' placeholder='username' name='username'/>
        <button>Submit</button>
    </form>
    """
#'name=' html attr used to store the value of input when sent to server

@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username = request.form['username']
    return f"""
        <h1>Saved your comment</h1>
        <ul>
            <li>Username: {username}</li>
            <li>Comment: {comment}</li>
        </ul>
    """

@app.route('/r/<subreddit>') #<> same argument name passed to view handler
def show_subreddit(subreddit):
    return f"<h1>Browsing the {subreddit} subreddit</h1>"

@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comments(subreddit, post_id):
    return f"<h1>Viewing comments for post with the id: {post_id} from the {subreddit} subreddit</h1>"

#USERS = {
#   "whiskey": "Whiskey the Dog",
    # "spike": "Spring the Porcupine"
# }

# @app.route('/user/<username>')
# def show_user_profile(username):
#     """Show user profile for user"""

#     name = USERS[username]
#     return f"<h1>Profile for {name}</h1>"

POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo",
    3: "Double Rainbows all the way",
    4: "YOLO OMG (kill me)"
}

@app.route('/posts/<int:id>') #<> route variable
def find_post(id):
    post = POSTS.get(id, "Post not found") #'Post not found' default msg
    return f"<p>{post}</p>"

#Query params vs URL params
#http://toys.com/shop/spinning-top?color=red
#/shop/<product>/<color>   //// quesry string cause subject spinning-top with qualifier

#URL PARAM - /shop/<toy> Feels more like 'subject of page'
# /r/AskReddit/search/?q=chickens&restrict_sr=1
# /r/<subreddit>/search
#Query PARAM /shop?toy=elmo feels more like 'extra info abt a page' often used w/ form
#  /r/AskReddit/comments/ei1m7x/what_sauce_do_you_prefer_to_dip_your_chicken?sort=new


#~~~~~~~~~~~~~~~~~~~~~~~~~templates/jinja~~~~~~~~~~~~~~~~~~~~

# views are function that return a string(of html) def xxx(): < view
# template - stand alone file produce html, can be dynamic, can inherit
# new folder templates must

COMPLIMENTS = ['cool','clever','tenacious','awesome','pythonic']

@app.route('/lucky')
def lucky_num():
    """Example of dynamic template"""
    num = randint(1,10)
    return render_template('lucky.html', lucky_num=num, msg='You are so lucky!')

@app.route('/form')
def show_form():
    return render_template('form.html')

@app.route('/form-2')
def show_form_2():
    return render_template('form_2.html')

@app.route('/greet')
def get_greeting():
    username = request.args['username']
    nice_thing = choice(COMPLIMENTS)
    return render_template('greet.html', username=username, compliment=nice_thing)

@app.route('/greet-2')
def get_greeting_2():
    username = request.args['username']
    wants = request.args.get('wants_compliments')
    nice_things = sample(COMPLIMENTS, 3)
    return render_template('greet_2.html', username=username, wants_compliments=wants, compliments=nice_things)

@app.route('/spell/<word>')
def spell_word(word):
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)

#~~~~~~~~~~~~~~~~~template inheritence~~~~~~~~~~~~~~~~~~

#link to style sheet in base template 