"""
bus.py
-------
This module handles all bus-related data and core reservation logic
for the Bus Ticket Reservation System.

It stores the list of available buses (as a dictionary), and provides
functions to search buses, book seats, cancel seats, and display
booking details.
"""

# Dictionary storing bus data.
# Key   -> Bus ID
# Value -> dictionary with route, departure time, price, total seats,
#          and a list representing seat availability (True = available)
buses = {
    "B101": {
        "route": "Kuala Lumpur -> Penang",
        "time": "08:00 AM",
        "price": 45.00,
        "total_seats": 10,
        "seats": [True] * 10
    },
    "B102": {
        "route": "Kuala Lumpur -> Johor Bahru",
        "time": "10:30 AM",
        "price": 35.00,
        "total_seats": 10,
        "seats": [True] * 10
    },
    "B103": {
        "route": "Kuala Lumpur -> Ipoh",
        "time": "02:00 PM",
        "price": 25.00,
        "total_seats": 10,
        "seats": [True] * 10
    }
}

# List to keep a record of all bookings made in this session
booking_history = []


def display_all_buses():
    """Display every available bus, its route, time, price and
    how many seats are still free. Uses a loop to go through the
    buses dictionary."""
    print("\n===================== AVAILABLE BUSES =====================")
    print(f"{'ID':<6}{'Route':<28}{'Time':<12}{'Price (RM)':<12}{'Seats Left'}")
    print("-------------------------------------------------------------")
    for bus_id, info in buses.items():
        seats_left = info["seats"].count(True)
        print(f"{bus_id:<6}{info['route']:<28}{info['time']:<12}"
              f"{info['price']:<12.2f}{seats_left}/{info['total_seats']}")
    print("=============================================================")


def display_seat_map(bus_id):
    """Display a simple seat map for a given bus.
    True (O) = available, False (X) = booked."""
    bus = buses[bus_id]
    print(f"\nSeat map for {bus_id} ({bus['route']}):")
    for i, seat_available in enumerate(bus["seats"], start=1):
        status = "O" if seat_available else "X"
        print(f"Seat {i:2}: {status}", end="   ")
        if i % 5 == 0:  # new line after every 5 seats
            print()
    print("\n(O = Available, X = Booked)")


def book_seat(bus_id, seat_number, passenger_name):
    """
    Attempt to book a seat for a passenger.
    Returns True and prints a confirmation if successful,
    otherwise returns False with an explanation.
    """
    bus = buses[bus_id]

    # Basic validation (error handling)
    if seat_number < 1 or seat_number > bus["total_seats"]:
        print(f"Invalid seat number. Please choose between 1 and {bus['total_seats']}.")
        return False

    index = seat_number - 1
    if not bus["seats"][index]:
        print(f"Seat {seat_number} is already booked. Please choose another seat.")
        return False

    # Mark seat as booked
    bus["seats"][index] = False

    booking = {
        "passenger": passenger_name,
        "bus_id": bus_id,
        "route": bus["route"],
        "seat": seat_number,
        "price": bus["price"]
    }
    booking_history.append(booking)

    print(f"\nBooking successful! {passenger_name} booked seat {seat_number} "
          f"on {bus_id} ({bus['route']}) for RM{bus['price']:.2f}.")
    return True


def cancel_seat(bus_id, seat_number):
    """Cancel a previously booked seat, freeing it up again."""
    bus = buses[bus_id]

    if seat_number < 1 or seat_number > bus["total_seats"]:
        print("Invalid seat number.")
        return False

    index = seat_number - 1
    if bus["seats"][index]:
        print(f"Seat {seat_number} on {bus_id} is not currently booked.")
        return False

    bus["seats"][index] = True

    # Remove matching booking from history if it exists
    for record in booking_history:
        if record["bus_id"] == bus_id and record["seat"] == seat_number:
            booking_history.remove(record)
            break

    print(f"Seat {seat_number} on {bus_id} has been cancelled successfully.")
    return True


def display_booking_history():
    """Display every booking made so far in this session."""
    print("\n===================== BOOKING HISTORY ======================")
    if not booking_history:
        print("No bookings have been made yet.")
    else:
        for idx, record in enumerate(booking_history, start=1):
            print(f"{idx}. {record['passenger']} | {record['bus_id']} "
                  f"({record['route']}) | Seat {record['seat']} | "
                  f"RM{record['price']:.2f}")
    print("=============================================================")