import csv

def filter_data(input_file, output_file, class_job_category):
    """
    Filter data based on ClassJobCategory and write to the output file.

    Parameters:
        input_file (str): The name of the input CSV file.
        output_file (str): The name of the output CSV file.
        class_job_category (str): The ClassJobCategory to filter data for.
    """
    filtered_data = []

    with open(input_file, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')  # Explicitly set the delimiter to a comma
        headers = next(reader)  # Read and store the headers

        for row in reader:
            if row[2] == class_job_category and row[14]:  # Check the class and task columns
                filtered_data.append(row)

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile, delimiter=',')  # Explicitly set the delimiter to a comma
        writer.writerow(headers)  # Write the headers to the output file
        writer.writerows(filtered_data)

def create_index_file(input_file, output_file):
    """
    Create an index file containing ClassJobCategory and Task values.

    Parameters:
        input_file (str): The name of the input CSV file.
        output_file (str): The name of the output CSV file for the index.
    """
    index_data = []

    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Read and store the headers

        for row in reader:
            if len(row) >= 15 and row[2] and row[14]:  # Check the class and task columns
                index_data.append([row[2], row[14]])

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(headers[:3])  # Write only ClassJobCategory and Task headers to the output file
        writer.writerows(index_data)

# Input CSV file
input_csv_file = 'RetainerTask.csv'

# Creating index.csv
create_index_file(input_csv_file, 'index.csv')

# Creating separate files for each ClassJobCategory and Task combination
filter_data(input_csv_file, 'BTN_data.csv', 'BTN')
filter_data(input_csv_file, 'MIN_data.csv', 'MIN')
filter_data(input_csv_file, 'FSH_data.csv', 'FSH')
filter_data(input_csv_file, 'DOW_data.csv', 'Disciples of War or Magic')
