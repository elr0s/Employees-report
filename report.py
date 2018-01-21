import sys, csv, math
from collections import OrderedDict

class Report:
    def __init__(self, filename, group_size=3):
        try:
            self.filename = filename
            self.group_size = int(group_size)
        except Exception:
            sys.exit('Please enter correct values for group size.')

    def _calculate_medians(self, data):
        medians = []
        for ratings in data.values():
            i = 0
            while len(ratings) > 0:
                if len(medians) < i+1: medians.append(0)
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

    def write_report(self):
        """Make report with average values and 
           difference between own and general for
           each skills group of each employee"""
        with open(self.filename, newline='') as datafile, open('report.csv', 'w', newline='') as reportfile:
            reader = csv.reader(datafile)

            data = OrderedDict()
            for row in reader:
                data[row[0]] = list(map(int, row[1:]))

            medians = self._calculate_medians(data)
            report = self._make_report(data, medians)

            writer = csv.writer(reportfile)

            titles = ['Code']
            for rating in range(len(medians)):
                titles.append('Skills group {0}'.format(rating+1))
            writer.writerow(titles)

            for code, ratings in report.items():
                writer.writerow([code] + ratings)


report = Report(*sys.argv[1:])
report.write_report()
