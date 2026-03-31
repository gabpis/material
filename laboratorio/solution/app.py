from flask import Flask, render_template

app = Flask(__name__)

posts_list = [
    {
        "username": "@alberto",
        "publication_date": "1 day ago",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec tristique lobortis molestie.",
        "profimg": "images/user.jpg",
        "postimg": "images/img1.jpg"
    },

    {
        "username": "@luigi",
        "publication_date": "4 days ago",
        "text": "Nunc condimentum tincidunt mollis. Curabitur gravida aliquam urna, ac vulputate felis condimentum at.",
        "profimg": "images/user.jpg",
        "postimg": "images/img2.jpg"
    },
    {
        "username": "@juan",
        "publication_date": "1 week ago",
        "text": "Sed sapien lectus, aliquam ac ornare sed, dapibus pulvinar ligula. Ut ultrices a nibh eget eleifend.",
        "profimg": "images/user.jpg",
        "postimg": "images/img3.jpg"
    }
]

@app.route('/')
def home():
    return render_template('indexlab.html', plist = posts_list)

@app.route('/about')
def about():
    return render_template('about.html')



