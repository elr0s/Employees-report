#!/usr/bin/python3
import os
import csv
import sys
import argparse
from collections import OrderedDict


class Report:
    def __init__(self, filename, group_size=3):
            self.filename = filename
            self.group_size = group_size

    def _calculate_medians(self, data):
        medians = []
        for ratings in data.values():
            i = 0
            while len(ratings) > 0:
                if len(medians) < i + 1:
                    medians.append(0)
                medians[i] += sum(ratings[:self.group_size])
                ratings = ratings[self.group_size:]
                i += 1
        medians = list(map(lambda x: round(x / len(data), 2), medians))
        return medians

    def _make_report(self, data, medians):
        for code, ratings in data.items():
            groups = []
            i = 0
            while len(ratings) > 0:
                group = sum(ratings[:self.group_size])
                average = round(group / self.group_size, 2)
                difference = round(group - medians[i], 2)
                groups.append('{0} {1}'.format(average, difference))
                ratings = ratings[self.group_size:]
                i += 1
            data[code] = groups
        return data

    def _check_data(self):
        if not os.path.exists(self.filename):
            print('Data file with that name doesn\'t exists.')
            sys.exit()

    def write_report(self):
        """
        Make report with average values and
        difference between own and general for
        each skills group of each employee.
        """
        self._check_data()
        with open(self.filename, newline='') as datafile,\
                open('report.csv', 'w', newline='') as reportfile,\
                open('log.txt', 'w') as log:
            reader = csv.reader(datafile)

            data = OrderedDict()
            errors = 0
            for row in reader:
                try:
                    data[row[0]] = list(map(float, row[1:]))
                except Exception:
                    log.write('Data of employee with code {0} is invalid.'.format(row[0]))
                    errors += 1

            medians = self._calculate_medians(data)
            report = self._make_report(data, medians)

            writer = csv.writer(reportfile)

            titles = ['Code']
            for rating in range(len(medians)):
                titles.append('Skills group {0}'.format(rating + 1))
            writer.writerow(titles)

            for code, ratings in report.items():
                writer.writerow([code] + ratings)

            print('Work is over. The reports are built for {0} employees.\nErrors: {1}.'.format(len(data), errors))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="name of file with employees data")
    parser.add_argument("-g", "--group_size", type=int, help="count of skills in skills group")
    args = parser.parse_args()
    defined = {k: v for k, v in vars(args).items() if v is not None}

    report = Report(**defined)
    report.write_report()
