import sys, csv, random, argparse


class DataWriter:
    def __init__(self, filename, employees=300, skills=30, rating=5):
        self.filename = filename
        self.employees = employees
        self.skills = skills
        self.rating = rating

    def create_csv(self):
        """Create csv with pseudo-ratings for employees"""
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for employee in range(self.employees):
                record = [employee+1]
                record += [random.choice(range(1, self.rating+1)) for skill in range(self.skills)]
                writer.writerow(record)


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="name of file to write data")
    parser.add_argument("-e", "--employees", type=int, help="count of employees with ratings in datafile")
    parser.add_argument("-s", "--skills", type=int, help="count of skills for each employee")
    parser.add_argument("-r", "--rating", type=int, help="maximum of rating value")
    args = parser.parse_args()
    defined = {k: v for k, v in vars(args).items() if v is not None}

    return defined


if __name__ == "__main__":
    data = DataWriter(**cli())
    data.create_csv()
