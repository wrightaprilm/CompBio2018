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
    surveys_df = pd.read_csv(sys.argv[1])
    outdir = sys.argv[2]
    year = sys.argv[3]
    
    out_check(outdir)   
    one_year_csv_writer(int(year), surveys_df, outdir)    
    
print("Hello world")