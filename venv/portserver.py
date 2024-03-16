from flask import Flask, render_template, redirect, request

# name in this case is main.
# an instance of Flask app is initiated here
app = Flask(__name__)

# this is a decorator here 
# it gives you an API route
# whenever this route is called, this function is run
@app.route('/')
@app.route('/index.html')
def hello_world():
    return render_template('./index.html')

@app.route('/about.html')
def about():
    return render_template('./about.html')

@app.route('/works.html')
def works():
    return render_template('./works.html')

@app.route('/contact.html')
def contact():
    return render_template('./contact.html')

@app.route('/thankyou.html')
def thankyou():
    return render_template('./thankyou.html')

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return redirect('/thankyou.html')
    else:
        return "error"

if __name__ == '__main__':
    app.run(debug=True)
