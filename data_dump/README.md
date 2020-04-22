## All Chromosomes data extracted from dbNSFP

### To decompress:
```
cat *00* > massive.zip.gz
gunzip massive.zip.gz
unzip massive.zip
```

### To use in the data proessing notebooks, select the headers to keep

```
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 M X Y; \
    do python3 keep_relevant_headers.py \
    ../data_dump/chr$i\_gene.tsv ../data_dump/chr$i.out_set5.tsv \
    --cols chr,pos,ref,alt,aapos,codonpos,Polyphen2_HVAR_pred,GenoCanyon_score,LINSIGHT,clinvar_clnsig,RVIS_ExAC,ExAC_cnv.score,SORVA_LOF_MAF0.005_HetOrHom; done
```

## Then run the data processing notebook to create the pickled dataframe:

/notebooks/data_processing/Dataprocessing_2-16_featureset5_mc.ipynb
* concatenates the data chromosomes 2-26, inclusive
* add the mutation counts columns
* pickles the dataframe to `pickled/chr2-16_set5_mc.pkl`


## Run the model: 
run 39.5.2_16.RF.lococv 

