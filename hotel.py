from flask import Flask, render_template
from flask import request
import csv
import datetime
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reviews', methods = ['GET'])
def reviews():

    reviews = readfile('static\\reviews.csv')

    return render_template('reviews.html', reviewlist = reviews)


@app.route('/guestReview', methods=['POST'])
def guestreview():
    # Read in existing rows
    reviews = readfile('static\\reviews.csv')

    # Create and add new review
    date = datetime.datetime.now().date().strftime("%x")
    name = request.form[('name')]
    rating = request.form[('rating')]
    comments = request.form[('comments')]

    newRow = [date, name, rating, comments]
    reviews.append(newRow)

    # Save new review list back to file
    writefile('static\\reviews.csv', reviews)

    # Reload page
    reviews = readfile('static\\reviews.csv')
    return render_template('reviews.html', reviewlist = reviews)


def readfile(filename):
    with open(filename, 'r') as inFile:
        reader = csv.reader(inFile)
        list = [row for row in reader]
    return list


def writefile(filename, list):
    with open(filename, 'w', newline='') as outFile:
        writer = csv.writer(outFile)
        writer.writerows(list)
    return


if __name__ == '__main__':
    app.run(debug = True)
