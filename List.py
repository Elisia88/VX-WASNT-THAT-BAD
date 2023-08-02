import csv

def get_class_job_category(name, index_file):
    """
    Get the ClassJobCategory for a given name from the index file.

    Parameters:
        name (str): The name to find in the index.
        index_file (str): The path to the index CSV file.

    Returns:
        str: The ClassJobCategory corresponding to the given name, or None if not found.
    """
    with open(index_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[1] == name:
                return row[0]
    return None

def get_data_file_path(class_job_category):
    """
    Get the path of the data file based on the ClassJobCategory.

    Parameters:
        class_job_category (str): The ClassJobCategory to find the data file for.

    Returns:
        str: The path of the data file.
    """
    if class_job_category == "BTN":
        return "BTN_data.csv"
    elif class_job_category == "Disciples of War or Magic":
        return "DOW_data.csv"
    elif class_job_category == "FSH":
        return "FSH_data.csv"
    elif class_job_category == "MIN":
        return "MIN_data.csv"
    else:
        return None

def sort_items_by_class_job_category(input_file, index_file, output_file, log_file):
    items_by_category = {}
    unprocessed_lines = []

    with open(input_file, 'r', encoding='utf-8') as infile:
        for line_num, line in enumerate(infile, start=1):
            line = line.strip()
            # Find the last occurrence of 'x' and split the line there
            x_index = line.rfind('x')
            if x_index != -1:
                num = line[:x_index].strip()
                name = line[x_index + 1 :].strip()
                if name:
                    class_job_category = get_class_job_category(name, index_file)
                    if class_job_category:
                        data_file = get_data_file_path(class_job_category)
                        if data_file:
                            if class_job_category not in items_by_category:
                                items_by_category[class_job_category] = []
                            items_by_category[class_job_category].append(f"{num}x {name}")
                            with open(log_file, 'a', encoding='utf-8') as logfile:
                                logfile.write(f"Line {line_num}: Processed - {num}x {name} -> ClassJobCategory: {class_job_category}\n")
                        else:
                            unprocessed_lines.append((line_num, line))
                            with open(log_file, 'a', encoding='utf-8') as logfile:
                                logfile.write(f"Line {line_num}: Unprocessed - {line}\n")
                    else:
                        unprocessed_lines.append((line_num, line))
                        with open(log_file, 'a', encoding='utf-8') as logfile:
                            logfile.write(f"Line {line_num}: Unprocessed - {line}\n")
                else:
                    unprocessed_lines.append((line_num, line))
                    with open(log_file, 'a', encoding='utf-8') as logfile:
                        logfile.write(f"Line {line_num}: Unprocessed - {line}\n")

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        for category, items in items_by_category.items():
            for item in items:
                writer.writerow([category, item])

    if unprocessed_lines:
        with open(log_file, 'a', encoding='utf-8') as logfile:
            logfile.write("Unprocessed lines:\n")
            for line_num, line in unprocessed_lines:
                logfile.write(f"Line {line_num}: {line}\n")

# Input files
input_list_file = 'input_list.txt'
index_csv_file = 'index.csv'
output_csv_file = 'output.csv'
log_file = 'log.txt'

# Clear log file before starting
with open(log_file, 'w', encoding='utf-8'):
    pass

# Sort the items by ClassJobCategory and write to the same output file
sort_items_by_class_job_category(input_list_file, index_csv_file, output_csv_file, log_file)
