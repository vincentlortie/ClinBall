import csv
counter = 0
# Here we specify the input and output files.
# The output file will have all the input rows which have a valid clinvar entry
with open('E:/dbNSFP4.0a_variant.chr', 'r', 262144) as f:
    with open('chrY.tsv', 'w') as o:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            o.write('\t'.join(list(row.keys())) + '\n')
            break
        for row in reader:
            if row['clinvar_id'] != '.':
                d = row.values()
                if None in d:
                    continue
                o.write('\t'.join(list(d)) + '\n')
            counter += 1
            print(counter)