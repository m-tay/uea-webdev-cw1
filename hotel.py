from flask import Flask, render_template, request, redirect
import csv
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/booking')
def booking():
    
    bookings = readfile('static\\bookings.csv')
    earliestdate = datetime.datetime.now().date().strftime("%Y-%m-%d")
    
    return render_template('booking.html', mindate = earliestdate, bookinglist = bookings)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')
    
@app.route('/reviews', methods = ['GET'])
def reviews():

    reviews = readfile('static\\reviews.csv')

    return render_template('reviews.html', reviewlist = reviews)


@app.route('/guestReview', methods=['POST'])
def guestreview():
    # Read in existing rows
    reviews = readfile('static\\reviews.csv')

    # Create and add new review
    date = datetime.datetime.now().date().strftime("%d/%m/%Y")
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
    room = request.form[('room')]
    arrival = request.form[('arrival')]
    departure = request.form[('departure')]
    confirmed = 'no'

    newRow = [date, name, email, room, arrival, departure, confirmed]
    arrivalDate = datetime.datetime.strptime(arrival, "%Y-%m-%d").date()
    print(arrivalDate)
    #Make sure dates are logical
    if (departure <= arrival):
        return render_template('booking.html', bookinglist = bookings, errorMessage = "Departure/Arrival dates not valid")
    elif arrivalDate < datetime.datetime.now().date():
        return render_template('booking.html', bookinglist = bookings, errorMessage = "Can't enter a departure/arrival date in the past")        	
    else:
        bookings.append(newRow)
        print('New Booking Request: ',newRow)
    
    # Save new booking list back to file
    writefile('static\\bookings.csv', bookings)
    
    
    return render_template('conformation.html', details = newRow)
    

@app.route('/guestBooking', methods=['POST'])
def bookingconformation():
    
    
    return redirect("/booking", code=302)

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
