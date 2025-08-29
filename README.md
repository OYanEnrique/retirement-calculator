# 👴 Retirement Age Calculator

A command-line tool that gathers a worker's data (name, birth year, hiring information) and calculates the age at which they will be eligible for retirement based on a 35-year contribution period.

## Features

* **Data Collection**: Gathers essential data like name, birth year, and employment details.
* **Automatic Age Calculation**: Uses the `datetime` module to determine the worker's current age based on their birth year.
* **Retirement Calculation**: If employment data is provided, it estimates the retirement age based on a fixed 35-year contribution rule.
* **Data Summary**: Displays a clean, key-value summary of all the worker's information at the end.

## How to Use

1.  Ensure you have Python installed.
2.  Save the code as a `.py` file (e.g., `retirement.py`).
3.  Run the script from your terminal:
    ```sh
    python retirement.py
    ```
4.  The program will prompt you to enter the worker's details.
5.  If you enter `0` for the `CTPS` (work card number), the script will not ask for hiring or wage details.
6.  After all data is entered, a summary will be printed.

### Example Session

```sh
> python retirement.py
------Retirement------
Worker name:
John
Birth year:
1985
CTPS:
12345
Year of hire:
2010
Wage:
5000
  - Name: John
  - Birth_year: 1985
  - Age: 40
  - Ctps: 12345
  - Hiring: 2010
  - Wage: 5000.0
  - Retirement: 50
```
