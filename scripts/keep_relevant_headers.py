import csv
KEEP_HEADERS = ['chr', 'pos(1-based)', 'ref', 'alt', 'SIFT_pred', 'FATHMM_pred', 'PROVEAN_pred', 'clinvar_clnsig']

counter = 0
with open('temp.tsv', 'r', 262144) as f:
    with open('final.tsv', 'w') as o:
        reader = csv.DictReader(f, delimiter='\t')
        csvwriter = csv.writer(o)
        for row in reader:
            new_row = []
            for key, val in row.items():
                if key and key.strip() in KEEP_HEADERS:
                    new_row.append(val)
            o.write('\t'.join(new_row) + '\n')
            counter += 1
            print(counter)
