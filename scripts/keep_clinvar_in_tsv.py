import csv
counter = 0
with open('E:/dbNSFP4.0a_variant.chr4', 'r', 262144) as f:
    with open('chr4.tsv', 'w') as o:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            o.write('\t'.join(list(row.keys())) + '\n')
            break
        for row in reader:
            if row['clinvar_id'] != '.':
                d = row.values()
                o.write('\t'.join(list(d)) + '\n')
            counter += 1
            print(counter)