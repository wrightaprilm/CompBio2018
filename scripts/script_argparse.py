import pandas as pd
import os
import sys
import argparse

def one_year_csv_writer(this_year, all_data, outdir):
    """
    Writes a csv file for data from a given year.

    this_year --- year for which data is extracted
    all_data --- DataFrame with multi-year data
    """
      
    # Select data for the year
    surveys_year = all_data[all_data.year == this_year]

    # Write the new DataFrame to a csv file
    filename = outdir + str(this_year) + '.csv'
    surveys_year.to_csv(filename)


def out_check(test_dir):
    test_strip = test_dir.split('/')
    checkout = test_strip[0] + '/' + test_strip[1]
    if test_strip[2] in os.listdir(checkout):
       print('Processed directory exists')
    else:
       writeout = test_strip[0] + '/' + test_strip[1] + '/' + test_strip[2]
       os.mkdir(writeout)
       print('Processed directory created')
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Path to input data in CSV format")
    parser.add_argument("--output", help="Path to where you want to write output, ending in output prefix.")
    parser.add_argument("--year", help="What year do you want data for?")
    
    args = parser.parse_args()
    if args.input:
         filename = args.input
    if args.output:
         outdir = args.output
    if args.year:
        this_year = args.year
    
    surveys_df = pd.read_csv(filename)
    out_check(outdir)   
    one_year_csv_writer(int(this_year), surveys_df, outdir)    