TripLog Analyzer
A Python-Based Transportation Data Processing & Analysis Tool

Project Title
TripLog Analyzer – Transportation Trip Data Processing System

What is this Project?
Think of TripLog Analyzer as a handy digital assistant for anyone managing transportation data. It is a straightforward Python program designed to read, tidy up, and make sense of trip records stored in simple CSV files.

Whether you are running a small cab company, managing a few bus routes, or overseeing a delivery service, this tool helps you see the bigger picture behind your daily logs. Instead of staring at rows of spreadsheets, the program calculates and displays:

The total number of trips taken.

How far your fleet has traveled (total and average distance).

Which trips were delayed.

A breakdown of trips by specific vehicles.

The best part? It runs right in your terminal using standard Python. It’s lightweight, portable, and doesn't require complex installations.

What Can It Do?
Here is a look at the specific features packed into this tool:

✔ Reads Your Data: Loads trip information directly from a CSV file.

✔ Keeps It Clean: Automatically validates records to ensure the data is usable.

✔ visualizes the Logs: Displays all your trips in a neat, organized tabular layout.

✔ Filters by Vehicle: Lets you isolate data to see performance for a specific bus or car.

✔ Smart Search: Allows you to search for routes using text (like "CityCenter").

✔ Spots Delays: Identifies late trips based on a delay threshold you choose.

✔ Manual Entry: Lets you add new trips manually through the menu.

✔ Auto-Save: Automatically saves any new data back to your CSV file so you never lose work.

✔ The Big Picture: Generates a complete summary including total distance and delay stats.

✔ User-Friendly: Uses a simple menu system that is great for beginners.

Under the Hood (Tech Stack)
We kept things simple and reliable.

Language: Python 3.x

Libraries: We only used Python's standard library, so you don't need to install anything extra.

csv → Used for reading and writing the data files.

os → Used to check if files exist and handle paths.

Interface: Command-line Interface (CLI).

▶  How to Get Up and Running
Follow these steps to get the tool working on your machine:

1. Install Python First, make sure you have Python 3.x installed. You can check this by typing the following into your terminal: python --version

2. Download the Files You will need two main files in the same folder:

main.py (The actual program code)

trips.csv (Your dataset)

3. Check Your Data Ensure your CSV file is formatted correctly. A standard row should look like this: 1,2025-11-20,BUS01,Campus,CityCenter,15.5,40,5

4. Run the Program Open your terminal, navigate to the project folder, and type: python main.py

Once you hit enter, the main menu will pop up, inviting you to load data, view trips, or analyze stats.

How to Test Drive It (and Try to Break It)
To really see if the system is robust, try running these scenarios. It’s like a quality assurance checklist:

1. File Loading Tests

Happy Path: Keep a valid trips.csv file and watch it load successfully.

Missing File: Rename or delete the file. The system should handle it gracefully (showing 0 trips) rather than crashing.

Bad Data: Add some "garbage" rows to the CSV. The program should be smart enough to skip them.

2. Adding Trips

Valid Entry: Add a standard trip with a positive distance.

Invalid Entry: Try to enter a negative distance or zero. The system should reject it.

Wrong Formats: Type letters where numbers should be. The program should show an error message.

3. Viewing & Filtering

View All: Check if the table looks correct.

Vehicle Filter: Search for a vehicle ID that exists, and then one that doesn't.

Text Search: Search for a source or destination. It should find matches regardless of capitalization (case-insensitive).

Delay Check: Filter for delayed trips using different thresholds (e.g., 0, 5, or 10 minutes).

4. checking the Math (Summary) Verify that the summary screen accurately calculates:

Total trips.

Total and Average distance.

The count of delayed trips.

The distribution of trips per vehicle.

5. Saving & Loading

Add a new trip manually.

Close the program and run it again.

Check if that new trip is still there (it should load automatically).

Project Structure
Here is how your folder should look to keep things organized:

Plaintext

TripLog-Analyzer/
│
├── main.py          # The brain of the operation
├── trips.csv        # The data
├── README.md        # This file
└── screenshots/     # (Optional visuals)
✅ Conclusion
TripLog Analyzer is designed to be a lightweight, transparent, and easy-to-use tool for handling transportation logs.

Beyond just being a useful utility, it demonstrates practical programming skills, including:

File Handling: Reading and writing data.

Data Validation: Ensuring data integrity.

Logic: Filtering and summarizing complex information.

Design: Keeping code modular and clean.

It is a solid project for Python beginners and a great example of how to apply computational thinking to solve real-world data problems.