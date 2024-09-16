'''Create a script that processes a CSV file containing student grades and calculates the average grade for each student.'''

import csv

def calculate_averages(input_file, output_file):
    student_averages = {}
    
    # Read the CSV file
    with open(input_file, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            name = row['Student Name']
            grades = [float(value) for key, value in row.items() if key != 'Student Name' and value]
            
            if grades:  # Check if there are any grades
                average = sum(grades) / len(grades)
                student_averages[name] = average

    # Write the averages to a new CSV file
    with open(output_file, mode='w', newline='') as csvfile:
        fieldnames = ['Student Name', 'Average Grade']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for name, average in student_averages.items():
            writer.writerow({'Student Name': name, 'Average Grade': average})
    
    print(f"Average grades have been written to {output_file}")

# Main program
input_filename = input("Enter the input CSV file name: ")
output_filename = input("Enter the output CSV file name: ")

calculate_averages(input_filename, output_filename)
