import csv
import os

DATA_FILE = "trips.csv"

TRIP_FIELDS = [
    "trip_id",
    "date",
    "vehicle_id",
    "source",
    "destination",
    "distance_km",
    "travel_time_min",
    "delay_min",
]


def load_trips():
    """Load trips from CSV file into a list of dictionaries."""
    trips = []
    if not os.path.exists(DATA_FILE):
        return trips

    try:
        with open(DATA_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    trip = {
                        "trip_id": int(row["trip_id"]),
                        "date": row["date"],
                        "vehicle_id": row["vehicle_id"],
                        "source": row["source"],
                        "destination": row["destination"],
                        "distance_km": float(row["distance_km"]),
                        "travel_time_min": int(row["travel_time_min"]),
                        "delay_min": int(row["delay_min"]),
                    }
                    # Basic validation: ignore non-positive distance
                    if trip["distance_km"] <= 0:
                        continue
                    trips.append(trip)
                except (KeyError, ValueError):
                    # Skip bad rows
                    continue
    except Exception as e:
        print(f"[ERROR] Could not load trips: {e}")

    return trips


def save_trips(trips):
    """Save trips back to CSV file."""
    try:
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=TRIP_FIELDS)
            writer.writeheader()
            for t in trips:
                writer.writerow(t)
    except Exception as e:
        print(f"[ERROR] Could not save trips: {e}")


def print_trips_list(trips):
    if not trips:
        print("No trips to show.\n")
        return

    print("\nIndex | Trip ID | Date       | Vehicle | From -> To            | Dist(km) | Time(min) | Delay(min)")
    print("-" * 95)
    for i, t in enumerate(trips, start=1):
        route = f"{t['source']} -> {t['destination']}"
        print(
            f"{i:5} | {t['trip_id']:7} | {t['date']:<10} | {t['vehicle_id']:<7} | "
            f"{route:<20} | {t['distance_km']:8.2f} | {t['travel_time_min']:9} | {t['delay_min']:10}"
        )
    print("")


def view_trips(trips):
    while True:
        print("\nView Trips")
        print("1. View all trips")
        print("2. View trips by vehicle")
        print("3. View delayed trips")
        print("4. Search by source/destination")
        print("5. Back to main menu")
        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            print_trips_list(trips)

        elif choice == "2":
            vid = input("Enter vehicle ID: ").strip()
            filtered = [t for t in trips if t["vehicle_id"].lower() == vid.lower()]
            print_trips_list(filtered)

        elif choice == "3":
            try:
                threshold = int(input("Minimum delay in minutes (default 0): ").strip() or "0")
            except ValueError:
                threshold = 0
            delayed = [t for t in trips if t["delay_min"] > threshold]
            print_trips_list(delayed)

        elif choice == "4":
            q = input("Search text (in source/destination): ").strip().lower()
            if not q:
                print("Empty search.\n")
                continue
            filtered = [
                t for t in trips
                if q in t["source"].lower() or q in t["destination"].lower()
            ]
            print_trips_list(filtered)

        elif choice == "5":
            break
        else:
            print("Invalid choice, try again.\n")


def add_trip_flow(trips):
    while True:
        print("\nAdd New Trip (or type 'b' at any prompt to go back)")
        trip_id_input = input("Trip ID: ").strip()
        if trip_id_input.lower() == "b":
            return
        try:
            trip_id = int(trip_id_input)
        except ValueError:
            print("Invalid Trip ID. Please enter a number.\n")
            continue

        date = input("Date (e.g., 2025-11-24): ").strip()
        if date.lower() == "b":
            return

        vehicle_id = input("Vehicle ID: ").strip()
        if vehicle_id.lower() == "b":
            return

        source = input("Source: ").strip()
        if source.lower() == "b":
            return

        destination = input("Destination: ").strip()
        if destination.lower() == "b":
            return

        distance_input = input("Distance (km): ").strip()
        if distance_input.lower() == "b":
            return

        time_input = input("Travel time (minutes): ").strip()
        if time_input.lower() == "b":
            return

        delay_input = input("Delay (minutes, 0 if on time): ").strip()
        if delay_input.lower() == "b":
            return

        try:
            distance_km = float(distance_input)
            travel_time_min = int(time_input)
            delay_min = int(delay_input)
        except ValueError:
            print("Invalid numeric value. Please try again.\n")
            continue

        if distance_km <= 0:
            print("Distance must be positive. Trip not added.\n")
            continue

        trips.append({
            "trip_id": trip_id,
            "date": date,
            "vehicle_id": vehicle_id,
            "source": source,
            "destination": destination,
            "distance_km": distance_km,
            "travel_time_min": travel_time_min,
            "delay_min": delay_min,
        })

        save_trips(trips)
        print("Trip saved.\n")

        again = input("Add another trip? (y/n): ").strip().lower()
        if again != "y":
            break


def print_summary(trips):
    print("\n=== Trip Summary ===")
    if not trips:
        print("No trips available.\n")
        return

    total_trips = len(trips)
    total_distance = sum(t["distance_km"] for t in trips)
    avg_distance = total_distance / total_trips if total_trips > 0 else 0.0

    # trips per vehicle
    trips_per_vehicle = {}
    for t in trips:
        vid = t["vehicle_id"]
        trips_per_vehicle[vid] = trips_per_vehicle.get(vid, 0) + 1

    delayed_trips = sum(1 for t in trips if t["delay_min"] > 0)
    delayed_percent = (delayed_trips / total_trips) * 100 if total_trips > 0 else 0.0

    print(f"Total trips              : {total_trips}")
    print(f"Total distance (km)      : {total_distance:.2f}")
    print(f"Average distance (km)    : {avg_distance:.2f}")
    print(f"Delayed trips            : {delayed_trips}")
    print(f"Percentage delayed trips : {delayed_percent:.2f}%\n")

    print("--- Trips per Vehicle ---")
    for vid, count in trips_per_vehicle.items():
        print(f"{vid}: {count} trips")
    print("")


def main():
    trips = load_trips()
    print("TripLog Analyzer (CSV-based Trip Manager)")
    print(f"Loaded {len(trips)} existing trips from '{DATA_FILE}'.\n")

    while True:
        print("Main Menu")
        print("1. Add new trip")
        print("2. View trips")
        print("3. Summary")
        print("4. Quit")
        choice = input("Choose (1-4): ").strip()

        if choice == "1":
            add_trip_flow(trips)
        elif choice == "2":
            view_trips(trips)
        elif choice == "3":
            print_summary(trips)
        elif choice == "4":
            print_summary(trips)
            print(f"All data saved to '{DATA_FILE}'.")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
