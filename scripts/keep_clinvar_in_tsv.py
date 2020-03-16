import csv
counter = 0
with open('E:/dbNSFP4.0a_variant.chr1', 'r', 262144) as f:
    with open('out.tsv', 'w') as o:
        reader = csv.DictReader(f, delimiter='\t')
        csvwriter = csv.writer(o)
        for row in reader:
            if row['clinvar_id'] != '.':
                d = row.values()
                o.write('\t'.join(list(d)) + '\n')
            counter += 1
            print(counter)