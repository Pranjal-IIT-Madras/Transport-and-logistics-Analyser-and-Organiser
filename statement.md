TripLog Analyzer – Project Statement
Problem Statement
Small transportation businesses—like local taxi services, bus routes, or delivery providers—often track their data in basic Excel sheets or manual logs. While this records the information, it doesn't make it easy to analyze.

Without a proper tool, these operators struggle to answer simple questions just by looking at rows of numbers. They often lack visibility on total mileage, vehicle utilization, or recurring delays. This project aims to solve that by providing a lightweight, Python-based tool that turns raw CSV logs into readable insights.

Project Scope
This project focuses on data processing and automation using a Command Line Interface (CLI). There is no graphical user interface (GUI); the priority is on logic, file handling, and data validation using only Python's standard libraries.

The system will:

Load and Sanitize Data: Read CSV files and validate the data to prevent errors from bad input.

Analyze: Perform calculations to summarize distances, counts, and delays.

Interact: Allow users to search, filter, and add data through a terminal menu.

Persist: Save any changes made during the session back to the file system.

Target Users
This tool is intended for:

Small logistics operators who need a quick way to check fleet performance.

Route coordinators managing schedules.

Students or developers looking for a reference on building data-driven Python applications without external dependencies.

Key Features
1. Data Loading & Validation The program reads trip records from a CSV file. It includes error-handling logic to validate numeric fields (like distance and delay) and safely skips corrupt or incomplete rows so the application remains stable.

2. Viewing & Filtering Users can view the data in a structured table. The tool includes options to:

Filter logs by specific Vehicle IDs.

Search for source or destination locations via text match.

Isolate delayed trips based on a user-defined time threshold.

3. Analytics & Summaries The core function of the tool is to generate statistics. It calculates:

Total trips and total distance covered.

Average trip distance.

Delay metrics (count and percentage of late trips).

A breakdown of trips per vehicle.

4. Trip Management Users can manually append new trip records via the terminal. The system automatically formats this input and saves it to the existing CSV file, ensuring the dataset is always up to date.

5. User Interface The program uses a straightforward, menu-driven text interface. It is designed to be intuitive, guiding the user through options for loading, viewing, and analyzing data.