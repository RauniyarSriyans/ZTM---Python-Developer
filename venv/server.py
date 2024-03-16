from flask import Flask, render_template

# name in this case is main.
# an instance of Flask app is initiated here
app = Flask(__name__)

# this is a decorator here 
# it gives you an API route
# whenever this route is called, this function is run
@app.route('/')
def hello_world():
    return render_template('./learning.html')

@app.route('/blog')
def blog():
    return 'These are my thoughts on the blog'

# using parameter in the URL, here name is a variable in the JINJA template in html.
@app.route('/<username>')
def hello_world_withname(username=None):
    return render_template('./index.html', name=username)

if __name__ == '__main__':
    app.run(debug=True)