from flask import Flask, render_template, url_for

app = Flask(__name__)
post=[
    {
        'author':'Arnav Kamboj',
        'title':'Blog post 1',
        'content':'Hi just doing something op',
        'date_posted':'May 4 2005'
    },
    {
         'author':'Arnav Kamboj',
        'title':'Blog post 2',
        'content':'Hi just doing something op',
        'date_posted':'May 4 2006'

    }
]

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template("home.html",posts=post)

@app.route("/about")
def about():
    return render_template("about.html",title="About page")


if __name__=='__main__':
    app.run(debug=True)