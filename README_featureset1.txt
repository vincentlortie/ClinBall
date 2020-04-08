# Feature set 1: 

## Inspired by the list VL and MK chose, in order (columns number precedes name):
12	aapos
-25	APPRIS
27	TSL
31	codonpos
-33	Ancestral_allele
116	HUVEC_fitCons_score
348	clinvar_clnsig:
-356	Interpro_domain
419	ExAC_cnv.score
421	GDI
433	LoFtool_score
434	SORVA_LOF_MAF0.005_HetOrHom
-443	Essential_gene_CRISPR

--> Note that those with - are not numeric and are therefore excluded for simplicity 
from feature set 1. 

### select features from set1 from chromosomes 2,3,4 on April 8th:
$ for i in 2 3 4; do python3 keep_relevant_headers.py ../data/chr2-4_with_gene/chr$i\_gene.tsv ../data/chr2-4_with_gene/chr$i.out_set1.tsv --cols chr,pos,ref,alt,aapos,TSL,codonpos,HUVEC_fitCons_score,clinvar_clnsig,ExAC_cnv.score,GDI,LoFtool_score,SORVA_LOF_MAF0.005_HetOrHom; done


### data processing to get df:
* processed with `dataprocessing_chr2,3,4_featureset1`: 
* pickled_dfset1_chr234.pkl, to give df of shape: (11724, 9)