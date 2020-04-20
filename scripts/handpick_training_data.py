import argparse
import sys
import csv

"""
This script handpicks training data according to certain criteria.
The main criteria is divided by coding and non-coding variant
"""
CODING_COLUMNS = ['fathmm-XF_coding_score']
NON_CODING_COLUMNS = ['LINSIGHT', 'GenoCanyon_score']


def main(inp, out):
    with open(inp, 'r', 262144) as f:
        with open(out, 'w') as o:
            reader = csv.DictReader(f, delimiter='\t')
            kept = 0
            for i, row in enumerate(reader):
                counter = 0
                if i == 0:
                    o.write('\t'.join(row) + '\n')
                # Check if we are in a coding or non-coding variant
                if False:
                    print("Non coding Variant:")
                    for nc_col in NON_CODING_COLUMNS:
                        if row[nc_col] != '.':
                            print("NC variant has ", nc_col)
                            counter += 2
                else:
                    for c_col in CODING_COLUMNS:
                        if row[c_col] != '.':
                            pass
                            # print("C variant has ", c_col)
                            # counter += 2
                for key, val in row.items():
                    if val is None:
                        val = '.'
                    if val != '.':
                        counter += 1
                        # print('Variant has ', key)
                print('variant has {0}/{1} features'.format(counter, len(row.keys())))

                if counter > 14:
                    # print("Keeping Variant, score above 15")
                    o.write('\t'.join(row.values())+ '\n')
                    kept += 1
            print("kept a total of {0} / {1}".format(kept, i))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
    Takes a dbnsfp file and only keeps the specified columns
    """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('inp', help='input dbnsfp file')
    parser.add_argument('out', help='VCF containing fixed rows')
    args = parser.parse_args()
    sys.exit(main(inp=args.inp, out=args.out))

