from flask import Flask

app = Flask(__name__)

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
    html = """
    <html>
        <body>
            <h1>Home Page</h1>
            <p>Welcome to my simple app (I'm doin it bitches)</p>
            <a href='/hello'>Go to Hello Page</a>
        </body>
    </html>
    """
    return html

@app.route('/hello') #@ = decorator @classmethod -demands method or function directly after
def say_hello():
    html = """
    <html>
        <body>
            <h1>HELLO!</h1>
            <p>This is the Hello Page</p>
        </body>
    </html>
    """
    return html

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
