import argparse
import sys
import csv

def main(inp, gene, out):
    genes = {}

    with open(gene, 'r', 262144) as g:
        reader = csv.DictReader(g, delimiter='\t')
        headers_to_add = reader.fieldnames
        for row in reader:
            gene_attrs = [val for key, val in row.items() if key != 'chr']
            genes[row['Gene_name']] = gene_attrs
        headers_to_add.pop(headers_to_add.index('chr'))

    with open(inp, 'r', 262144) as f:
        with open(out, 'w') as o:
            reader = csv.DictReader(f, delimiter='\t')
            o.write('\t'.join(reader.fieldnames + headers_to_add) + '\n')
            for row in reader:
                genename = row['genename']
                if ';' in genename:
                    genes_arr = genename.split(';')
                    genename = max(set(genes_arr), key=genes_arr.count)
                new_row = []
                try:
                    gene_row = genes[genename]
                except:
                    gene_row = []
                o.write('\t'.join(list(row.values()) + list(gene_row)) + '\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
    Takes a dbnsfp file chromosome file, gets its gene name and add the correct
    dnNSFP gene information
    """, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('inp', help='input dbnsfp chr file')
    parser.add_argument('gene', help='input dbnsfp gene file')
    parser.add_argument('out', help='TSV containing rows gene and variant rows')
    args = parser.parse_args()
    sys.exit(main(inp=args.inp, gene=args.gene, out=args.out))