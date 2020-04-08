
import argparse
import sys


import csv


def main(inp, out, cols):
    if cols:
        KEEP_HEADERS = cols.split(',')
    else:
        KEEP_HEADERS = ['chr', 'pos(1-based)', 'ref', 'alt', 'SIFT_pred', 'FATHMM_pred', 'PROVEAN_pred', 'clinvar_clnsig']


    with open(inp, 'r', 262144) as f:
        with open(out, 'w') as o:
            reader = csv.DictReader(f, delimiter='\t')
            for header in KEEP_HEADERS:
                if header not in reader.fieldnames:
                    raise Exception('header %s is not specified header list' % header)
            o.write('\t'.join(KEEP_HEADERS) + '\n')
            for row in reader:
                new_row = []
                for key, val in row.items():
                    if key and key.strip() in KEEP_HEADERS:
                        if ';' in val:
                            preds_arr = val.split(';')
                            val = max(set(preds_arr), key=preds_arr.count)
                        new_row.append(val)
                o.write('\t'.join(new_row) + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
    Takes a dbnsfp file and only keeps the specified columns
    """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('inp', help='input dbnsfp file')
    parser.add_argument('out', help='VCF containing fixed rows')
    parser.add_argument('--cols', required=False, help='The columns we wish to keep(comma separated, with no spaces)')
    args = parser.parse_args()
    sys.exit(main(inp=args.inp, out=args.out, cols=args.cols))

