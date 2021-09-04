# Python programs manual

## Install python3 on your machine

Download file from address: https://www.python.org/downloads/mac-osx/

Install file

Check install using command: 

% python3 --version

Check pip install (if not installed, install it)

% pip --version

Install pip:

% curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
% python3 get-pip.py

## Install pandas library

Install pandas via command:

% pip install pandas

Check if installed:

% pip list

## Run python program

Go to folder where python.py file is located

Run file via command in terminal:

% python3 fileName.py

If successful, you will see a reply (note that it will depend due to the amount of data)

This will create test.cvs file

## Modify python file (if needed)

Open .py file with your text editor (MS VScode is very good)

edit path where ps.read_csv field is.

Note that you need to have a correct files for it to work

datan_kasittely_ohjelma.py uses files: Alkuperainen_OY_kaikki.csv and Member_last_activited.csv

toinen_datan_kasittely_ohjelma.py uses files: Oskarin_potet_2021.csv and Member_last_activited.csv

Note that the file names must be exact

## Import csv file to excel

Open blank excel sheet

Select Data tab --> then From Text --> select csv file --> Get Data
--> Next --> select semicolon --> Next --> --> choose formatting if needed --> Finish --> keep the position --> ok

## Run All_clientaccounts_with_auto_invest.py file

Change path if needed (files must be exact).

Make .csv file if needed. Excel --> file --> save as --> save as csv
