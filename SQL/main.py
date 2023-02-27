from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/',method=['GET', 'POST'])
def home():

    return render_template('index.html')


@app.route("/add", method=['GET', 'POST'])
def add():
    if request.methods == 'POST':
        book_name = request.form['Book Name']
        print(book_name)
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

