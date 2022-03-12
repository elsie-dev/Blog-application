from flask import Flask,render_template
app = Flask(__name__)


posts= [
    {
        'author':'ELSIE ma',
        'title':'post one',
        'content':'health issues',
        'date_posted':'April 30,2020'

    },
    {
        'author':'ELSIE ma',
        'title':'post one',
        'content':'health issues',
        'date_posted':'April 30,2020'

    }
]
    


@app.route("/")
@app.route("/home")
def home():


@app.route("/about")
def about():
    return render_template('about.html',title='About')


if __name__ == '__main__':
    app.run(debug=True)