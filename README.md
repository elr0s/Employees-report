## Requirements:
Python 3 or higher.

## datawriter.py

The script creates a csv file with pseudo-data of employees and their ratings.
The script takes one mandatory argument with datafile name and three optional arguments:
  -e or --employees - count of employees in datafile,
  -s or --skills - count of skills for each employee,
  -r or --rating - maximum of rating value.
Default values are 300 employees, 30 skills for each employee and ratings from 1 to 5.
Key -h or --help will open help menu.

###### Usage example
```
python3 datawriter.py data -e 500
```
Creates datafile data.csv with 30 skills and ratings from 1 to 5 for 500 employees.


## report.py

The script generates a report and saves it to the report.csv file. It also logs occurred errors to the log.txt file.
The script takes one mandatory argument with datafile name and one optional argument:
  -g or --group_size - count of skills in skills group.
Default value of group size is 3.
Key -h or --help will open help menu.

###### Usage example
```
python3 report.py data.csv
```
Creates file report.csv with reports and file log.txt with errors.


