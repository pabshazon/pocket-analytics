# Write a Python script that reads this file line by line and calculates the total usage amount per user. Print the results as:
# user_id,total_usage

# events are user_id,timestamp,usage_amount
import csv


def total_usage_amount_per_user():
    pass


if __name__ == '__main__':
    csv_path = '../events.csv'
    totals_by_user = {}

    with open(csv_path, 'r', newline='') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            user_id      = row['user_id']
            usage_amount = row['usage_amount']
            timestamp    = row['timestamp']
            if user_id not in totals_by_user: totals_by_user[user_id] = 0.0
#             if ~totals_by_user[user_id]: totals_by_user[user_id] = 0
            totals_by_user[user_id] += float(usage_amount)

    print(totals_by_user)




#     with open(csv_path) as file:
#         print(file.read())
# print(file.closed)
