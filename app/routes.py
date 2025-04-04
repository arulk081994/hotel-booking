from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Booking

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        booking = Booking(
            guest_name=request.form['name'],
            room_type=request.form['room_type'],
            check_in=request.form['check_in'],
            check_out=request.form['check_out'],
            special_requests=request.form.get('requests', '')
        )
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('bookings'))
    return render_template('book.html')

@app.route('/bookings')
def bookings():
    all_bookings = Booking.query.all()
    return render_template('bookings.html', bookings=all_bookings)
