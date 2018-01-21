import sys, csv, random


class DataWriter:
    def __init__(self, employees=300, skills=30, rating=5):
        try:
            self.employees = int(employees)
            self.skills = int(skills)
            self.rating = int(rating)
        except Exception:
            sys.exit('Please enter correct values for employees, skills and rating.')

    def create_csv(self):
        """Create csv with pseudo-ratings for employees"""
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            for employee in range(self.employees):
                record = [employee+1]
                record += [random.choice(range(1, self.rating+1)) for skill in range(self.skills)]
                writer.writerow(record)


data = DataWriter(*sys.argv[1:])
data.create_csv()
