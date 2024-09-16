'''Develop a program that handles multiple types of exceptions (e.g., FileNotFoundError, ValueError) and logs errors to a file.'''


import logging

logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def process_file(filename):
    try:
        
        with open(filename, 'r') as file:
            data = file.read()
         
            value = int(data)  
            print(f"Processed value: {value}")
    
    except FileNotFoundError as e:
        logging.error(f"FileNotFoundError: {e}")
        print("Error: The file was not found. Check the filename and try again.")
    
    except ValueError as e:
        logging.error(f"ValueError: {e}")
        print("Error: Invalid data format. Ensure the file contains valid data.")
    
    except Exception as e:
        logging.error(f"Exception: {e}")
        print("An unexpected error occurred. Check the log file for details.")

# Main 
input_filename = input("Enter the filename to process: ")
process_file(input_filename)
