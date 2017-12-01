from flask import Flask, render_template
from flask import request
import csv
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booking')
def booking():
    
    bookings = readfile('static\\bookings.csv')

    return render_template('booking.html', bookinglist = bookings)

    
@app.route('/reviews', methods = ['GET'])
def reviews():

    reviews = readfile('static\\reviews.csv')

    return render_template('reviews.html', reviewlist = reviews)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

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

@app.route('/guestBooking', methods=['POST'])
def guestbooking():
    # Read in existing rows
    bookings = readfile('static\\bookings.csv')

    # Create and add new review
    date = datetime.datetime.now().date().strftime("%x")
    name = request.form[('name')]
    email = request.form[('email')]
    arrival = request.form[('arrival')]
    departure = request.form[('departure')]
    confirmed = "no"

    newRow = [date, name, email, arrival, departure]
    bookings.append(newRow)

    # Save new booking list back to file
    writefile('static\\bookings.csv', bookings)

    # Reload page
    #print(bookings[0])
    #for row in bookings:
    #    print(row)
    #    for index in row:
    #        print(row[index])
	#
    row = 0
    index = 1
    print(bookings[row[index]])
    return render_template('booking.html', bookinglist = bookings)


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
