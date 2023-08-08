from flask import Flask, render_template, request

app = Flask(__name__)
coach_seats= [
            [1, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 0, 1, 1],[1, 1, 1, 0, 1, 1, 1],[0, 0, 1, 0, 0, 1, 1],[1, 1, 1, 1, 1, 1, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 0, 1, 1],[1, 1, 1, 0, 1, 1, 1],[0, 0, 0],
        ]


def book_seats(seats, num_seats):
    rows = len(seats)
    cols = len(seats[0])
    booked_seats = []

    for row in range(rows):
        consecutive_available_seats = 0
        start_seat = -1

        for col in range(cols):
            if seats[row][col] == 0:
                if consecutive_available_seats == 0:
                    start_seat = col
                consecutive_available_seats += 1
            else:
                consecutive_available_seats = 0

            if consecutive_available_seats == num_seats:
                for i in range(num_seats):
                    seats[row][start_seat + i] = 1
                    booked_seats.append((row + 1, start_seat + i + 1))
                break

        if len(booked_seats) == num_seats:
            break

    return booked_seats

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        booked_seat=[]
        num_seats = int(request.form['num_seats'])
        booked_seat=book_seats(coach_seats, num_seats)
        return render_template('seats.html',booked_seat=booked_seat)
    return render_template('seats.html',coach_seats=coach_seats)
if __name__ == '__main__':
    app.run(debug=True)
