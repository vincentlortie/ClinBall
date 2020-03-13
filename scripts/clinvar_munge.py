import pysam
import sys
import pandas as pd

"""
Input: ClinVar vcf data
Output: 3 csv files, one for each clinical significance: uncertain, begign, pathogenic

"""

clinvar_vcf = pysam.VariantFile(sys.argv[1])

df = pd.DataFrame()
column_labels = ['ALLELEID', 'CLNDISDB', 'CLNDN', 'CLNHGVS', 'CLNREVSTAT', 'CLNSIG', 'CLNVC', 'CLNVCSO', 'GENEINFO', 'MC', 'ORIGIN', 'alt', 'chrom', 'pos', 'ref', 'AF_ESP', 'AF_EXAC', 'AF_TGP', 'RS', 'CLNVI', 'CLNSIGCONF']

row_list = []  # faster than appending to df in each row

for rec in clinvar_vcf.fetch():
     rec_dict = {}
     for info in rec.info:
         if type(rec.info[info]) is tuple:
             rec_dict[info] = rec.info[info][0]
         else:
             rec_dict[info] = rec.info[info]

     # Fill in cpra, to be used as idientifier
     rec_dict['chrom'] = rec.chrom
     rec_dict['pos'] = rec.pos
     rec_dict['ref'] = rec.ref
     
     # error if no alt (not typical, ex: chr1:5875102, id: 167375)
     try:
         rec_dict['alt'] = rec.alts[0]
     except:
         continue
     rec_dict['id'] = rec.id
     row_list.append(rec_dict)

df = pd.DataFrame(row_list, columns = column_labels)

benign_df = df[df['CLNSIG'].isin(['Likely_benign', 'Benign'])]
benign_df.to_csv('benign.csv', index=False)

pathogenic_df = df[df['CLNSIG'].isin(['Likely_pathogenic', 'Pathogenic'])]
pathogenic_df.to_csv('pathogenic.csv', index=False)

unk_df = df[df['CLNSIG'].isin(['Uncertain_significance'])]
unk_df.to_csv('Uncertain_significance.csv', index=False)


