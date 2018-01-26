## Requirements:
Python 3 or higher.

## create_data.py

The script creates csv file with pseudo-data of employees and their ratings.
The script takes one necessary argument with datafile name and three unnecessary keyword:
  -e or --employees - count of employees in datafile,
  -s or --skills - count of skills for each employee,
  -r or --rating - maximum of rating value.
Default values are 300 employees, 30 skills for each employee and ratings from 1 to 5.
Key -h or --help will open help menu.

###### Usage example
```
python3 create_data.py data -e 500
```
Create datafile data.csv with 30 skills and ratings from 1 to 5 for 500 employees.


## report.py

The script builts report in report.csv file and logs errors.
The script takes one necessary argument with datafile name and one unnecessary keyword:
  -g or --group_size - count of skills in skills group.
Default value of group size is 3.
Key -h or --help will open help menu.

###### Usage example
```
python3 report.py data.csv
```
Create file report.csv with reports and file log.txt with errors.


