# Run this script AFTER running extract.sh and BEFORE doing running MDS/Kriging scripts
# New Testament is made of: 
# the Acts (b.ACT.)
# the Pauline epistles (b.ROM., b.1CO., b.2CO., b.GAL., b.EPH., b.PHI., b.COL., b.1TH., b.2TH., b.1TI., b.2TI., b.TIT., b.PHM., b.HEB.)
# Book of Revelation (b.REV.)
# other epistles (b.JAM., b.1PE., b.2PE., b.1JO., b.2JO.,b.3JO.,b.JUD.)
# and the Gospels (b.MAT., b.MAR., b.LUK., b.JOH.)

# Single out the NT and plot that only 

import csv
import pandas as pd

# List all NT books
NTbooks = ("b.ACT.", "b.ROM.", "b.1CO.", "b.2CO.", "b.GAL.", "b.EPH.", "b.PHI.", "b.COL.", "b.1TH.", "b.2TH.", "b.1TI.", "b.2TI.", "b.TIT.", "b.PHM.", "b.HEB.", "b.JAM.", "b.1PE.", "b.2PE.", "b.1JO.", "b.2JO.", "b.3JO.", "b.JUD.", "b.MAT.", "b.MAR.", "b.LUK.", "b.JOH.")

# Change path accordingly
with open("./model2-LC-NP/_TARGETWORDS_/when-while.csv", 'r') as csv_file, open('./model2-LC-NP/_TARGETWORDS_/NTonly.csv', 'w') as fi:
    csv_NT = csv.reader(csv_file, delimiter=',')
    csv_writer = csv.writer(fi)
    csv_writer.writerow(next(csv_NT))
    NTonly = []
    for row in csv_NT:
        sent_id = row[0]
        for name in NTbooks:
            if name in sent_id:
                csv_writer.writerow(row)

# Remove heb and amh because they only have Old Testament, and gla as it only has Mark
data = pd.read_csv('NTonly.csv', keep_default_na=False, na_values=['_'])
data.drop('heb', inplace=True, axis=1)
data.drop('amh', inplace=True, axis=1)
data.drop('gla', inplace=True, axis=1)
data.to_csv('NTonly.csv', index=False)
