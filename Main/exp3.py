import csv
import os

TRAINS_FILE = "../Data/trains.csv"
PASSENGERS_FILE = "../Data/passengers.csv"
FARE_FILE = "../Data/fare.csv"
OUTPUT_DIR = "../Outputs/output_exp3"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def load_trains():
    trains = {}
    with open(TRAINS_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            trains[row['Train ID']] = {
                'Train Name': row['Train Name'],
                'Source': row['Source Station'],
                'Destination': row['Destination Station'],
                'Total Seats': int(row['Total Seats'])
            }
    return trains


def load_fares():
    fares = {}
    with open(FARE_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            train_id = row['Train ID']
            train_class = row['Class']
            fare_amount = int(row['Fare'])
            fares[(train_id, train_class)] = fare_amount
    return fares


def load_passengers():
    passengers = []
    with open(PASSENGERS_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            passengers.append({
                'Name': row['Name'],
                'Train ID': row['Train ID'],
                'Class': row['Class'],
                'Tickets': int(row['Number of Tickets'])
            })
    return passengers


def book_tickets(trains, fares, passengers):
    revenue = {}
    passenger_costs = []

    for p in passengers:
        name = p['Name']
        train_id = p['Train ID']
        t_class = p['Class']
        tickets = p['Tickets']

        if train_id not in trains:
            print(f"Error: Invalid Train ID '{train_id}' for passenger {name}")
            continue

        if (train_id, t_class) not in fares:
            print(
                f"Error: Fare for Train {train_id} Class {t_class} not found for {name}"
            )
            continue

        available = trains[train_id]['Total Seats']
        if tickets > available:
            print(f"Error: Not enough seats for {name} on train {train_id}")
            continue

        trains[train_id]['Total Seats'] -= tickets
        booking_fare = tickets * fares[(train_id, t_class)]
        revenue[train_id] = revenue.get(train_id, 0) + booking_fare
        passenger_costs.append(
            (name, train_id, t_class, tickets, booking_fare))
        print(
            f"Booking confirmed for {name} on {trains[train_id]['Train Name']} ({t_class}) - Fare: ₹{booking_fare}"
        )

    return revenue, passenger_costs

def generate_reports(trains, revenue, passenger_costs):
    with open(f"{OUTPUT_DIR}/report1_trains.csv", 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["Train ID", "Train Name", "Source", "Destination", "Seats Available"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for tid, details in trains.items():
            writer.writerow({
                "Train ID": tid,
                "Train Name": details['Train Name'],
                "Source": details['Source'],
                "Destination": details['Destination'],
                "Seats Available": details['Total Seats']
            })


    with open(f"{OUTPUT_DIR}/report2_revenue.csv", 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["Train ID", "Total Revenue"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for tid, rev in revenue.items():
            writer.writerow({
                "Train ID": tid,
                "Total Revenue": rev
            })

    with open(f"{OUTPUT_DIR}/passenger_costs.csv", 'w', newline='', encoding='utf-8') as f:
        fieldnames = ["Passenger Name", "Train ID", "Class", "Tickets", "Total Fare"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for name, tid, t_class, tickets, fare in passenger_costs:
            writer.writerow({
                "Passenger Name": name,
                "Train ID": tid,
                "Class": t_class,
                "Tickets": tickets,
                "Total Fare": fare
            })


def main():
    trains = load_trains()
    # print(trains)
    fares = load_fares()
    passengers = load_passengers()
    revenue, passenger_costs = book_tickets(trains, fares, passengers)
    generate_reports(trains, revenue, passenger_costs)
    print("Reports generated successfully.")


if __name__ == "__main__":
    main()
