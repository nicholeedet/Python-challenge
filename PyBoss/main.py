# -*- coding: utf-8 -*-

import os 
import csv
import pandas as pd

# Declare file location through csvpath
csvpath = os.path.join( 'Resources', 'employee_data.csv')
print(csvpath)

# Define list to represent data variable
full_name = []
first_name = []
last_name = []
date_of_birth = []
d_o_b = []
ssn = []
ssn_private = []
abbrev = []
employee_id = []


# List the states names as keys and abb as values in a dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


# Open csv with Improved Reading using CSV module
with open(csvpath,newline="", encoding='utf-8') as employee_data:
    csvreader = csv.reader(employee_data,delimiter=",") 

    # we are going to skip the header 
    header = next(csvreader)     
    
    for row in csvreader:

        employee_id.append(row[0])


        # Split full name to first name and last name 
        full_name = row[1].split(" ")   
        first_name.append(full_name[0])
        last_name.append(full_name[1])

        # Split date of birth using "-", 
        date_of_birth = row[2].split("-")
        d_o_b.append(date_of_birth[1] + "/" + date_of_birth[2] + "/" + date_of_birth[0])
        

        # Split the SSN using "-" 
        ssn = row[3].split("-")
        ssn_private.append("***-**-" + ssn[2])

     #Matching the list to the dictionary
        abbrev.append(us_state_abbrev[row[4]])

# we are going to create Data Frame using pandas library
# Keys replace orignal headers, values are the lists created 
new_df = pd.DataFrame({"Employee Id": employee_id, "First Name": first_name, "Last Name": last_name, "DOB": d_o_b, "SSN":ssn_private, "State": abbrev})

# Export new_df to csv,employee_new_data.csv
new_df.to_csv(os.path.join( 'employee_new_data.csv'), index=False, header=True)

# Print sample data 
print(new_df.head())    

















