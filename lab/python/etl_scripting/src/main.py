"""
You have a log file sample.log with various lines, some of which contain “ERROR:”. Write a Python script that reads the file line by line and extracts only the error lines into a new file errors_only.log. Print how many errors were found.
"""



if __name__ == "__main__":
    error_counter = 0
    with open('../log.txt', 'r', newline='') as log, open('../errors_log.txt', 'w', newline='') as errors_log:
        for entry in log:
            print(entry)
            if "ERROR" in entry:
                errors_log.write(entry)
                error_counter += 1

    print(error_counter)


