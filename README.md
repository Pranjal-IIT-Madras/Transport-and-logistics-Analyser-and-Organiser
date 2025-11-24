TripLog Analyzer
A Python CLI tool designed to parse, clean, and analyze transportation trip data from CSV files. This project calculates total trips, distance metrics, delays, and vehicle utilization statistics without requiring external dependencies.

Overview
This script provides a menu-driven interface to process raw transportation logs. It handles data validation, error checking, and generates statistical reports suitable for fleet management or logistics analysis.

Key Capabilities:

Data Ingestion: Loads and validates CSV records.

Aggregates: Calculates total distance and average trip metrics.

Categorization: Groups trip data by vehicle ID.

Performance Metrics: Analyzes delay frequency and percentage.

Zero Dependencies: Built entirely using the Python Standard Library.

Data Format
The application expects a CSV file (default: trips.csv) containing raw trip records.

Header Structure: trip_id, date, vehicle_id, source, destination, distance_km, travel_time_min, delay_min

Sample Record:

Code snippet

1,2025-11-20,BUS01,Campus,CityCenter,15.5,40,5
Installation and Usage
Prerequisites: Python 3.x

Setup: Clone the repository or download the source files.

Execution: Navigate to the src directory and run the entry point:

Bash

python main.py
Operation: Follow the on-screen prompts to load your data file. Once loaded, you can generate the following reports:

Basic Summary: Aggregate totals and averages.

Vehicle Report: Trip counts per vehicle.

Delay Stats: Analysis of schedule adherence.

Output Examples
Basic Summary

Plaintext

Total trips                : 25
Total distance (km)        : 312.40
Average distance (km/trip) : 12.49
Vehicle Report

Plaintext

BUS01 : 12 trips
VAN02 : 8 trips
TAXI5 : 5 trips
Delay Statistics

Plaintext

Total trips        : 25
Delayed trips      : 7
Percentage delayed : 28.00%
Project Structure
The codebase is modular to facilitate maintenance and extension:

main.py: CLI entry point and menu logic.

data_loader.py: File I/O, parsing, and data cleaning.

analytics.py: Core logic for statistical calculations.

reports.py: Formatting and display of analysis results.

Developers can extend analytics.py to include additional metrics such as route popularity, average speed calculation, or export functionality.