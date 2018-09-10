import pandas as pd
import os
import sys
import argparse

def one_year_csv_writer(this_year, all_data, output):
    """
    Writes a csv file for data from a given year.

    this_year --- year for which data is extracted
    all_data --- DataFrame with multi-year data
    """
        
    # Select data for the year
    surveys_year = all_data[all_data.year == this_year]

    # Write the new DataFrame to a csv file
    filename = output + str(this_year) + '.csv'
    surveys_year.to_csv(filename)

def output_test(test_dir):
    """
    Check to see if an output directory exists.
    If it exists, tell us.
    If it doesn't, create one, and tell us.
    """
    test_split = test_dir.split('/')
    check_directory = test_split[0] + '/' + test_split[1] + '/'
    if test_split[2] in os.listdir(check_directory):
       print('Processed directory exists')
    else:
#       output_directory = '/'.join(test_split[0:-1])
       output_directory = test_split[0] + '/' + test_split[1] + '/' + test_split[2]
       print(output_directory)
       os.mkdir(output_directory)
       print('Processed directory created')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.addArgument("--dataset", help = "CSV containing data for multiple years.")
    parser.addArgument("--output", help = "Where do you want to write output?")
    parser.addArgument("--year", help = "Which year do you want to analyze?")
    args = parser.parse_args()
    if args.dataset:
        surveys_df = args.dataset
    if args.output:
        test_dir = args.output
    if args.year:
        this_year = args.year
    surveys_df = pd.read_csv(surveys_df)
    output_test(test_dir)
    one_year_csv_writer(all_data = surveys_df, this_year = data_year, output = test_dir)    
    print("Victory.")