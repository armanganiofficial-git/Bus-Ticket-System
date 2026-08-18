"""
main.py
--------
Entry point of the Bus Ticket Reservation System.
Handles the menu-driven console interface and user input.
Uses functions imported from bus.py (modular programming).
"""

import bus  # import our custom module


def get_valid_int(prompt):
    """
    Helper function to safely get an integer input from the user.
    Keeps asking until a valid integer is entered (error handling).
    """
    while True:
        value = input(prompt)
        try:
            return int(value)
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_bus_id():
    """Helper function to make sure the user enters a Bus ID that exists."""
    while True:
        bus_id = input("Enter Bus ID (e.g., B101): ").strip().upper()
        if bus_id in bus.buses:
            return bus_id
        print("Bus ID not found. Please check the bus list and try again.")


def main():
    print("=============================================================")
    print("           WELCOME TO BUS TICKET RESERVATION SYSTEM")
    print("=============================================================")

    running = True
    while running:
        print("\n----------------------- MAIN MENU --------------------------")
        print("1. Display All Buses")
        print("2. View Seat Map")
        print("3. Book a Ticket")
        print("4. Cancel a Ticket")
        print("5. View Booking History")
        print("6. Exit")
        print("--------------------------------------------------------------")

        choice = get_valid_int("Enter your choice (1-6): ")

        if choice == 1:
            bus.display_all_buses()

        elif choice == 2:
            bus_id = get_valid_bus_id()
            bus.display_seat_map(bus_id)

        elif choice == 3:
            bus.display_all_buses()
            bus_id = get_valid_bus_id()
            bus.display_seat_map(bus_id)
            passenger_name = input("Enter passenger name: ").strip()

            # Basic validation: name should not be empty
            if passenger_name == "":
                print("Passenger name cannot be empty. Booking cancelled.")
            else:
                seat_number = get_valid_int("Enter seat number to book: ")
                bus.book_seat(bus_id, seat_number, passenger_name)

        elif choice == 4:
            bus_id = get_valid_bus_id()
            bus.display_seat_map(bus_id)
            seat_number = get_valid_int("Enter seat number to cancel: ")
            bus.cancel_seat(bus_id, seat_number)

        elif choice == 5:
            bus.display_booking_history()

        elif choice == 6:
            running = False
            print("\nThank you for using the Bus Ticket Reservation System. Goodbye!")

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()