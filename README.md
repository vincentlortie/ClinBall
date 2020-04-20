[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1Ahv6rKT_1iJg3o93t9_sews-yafoBAsF#scrollTo=KmOp5bSsLvO1)

# ClinBall

The goal of this project is to predict ClinVar predictions on variants that lack existing ClinVar data. 

---
# Report Draft 
TODO:
 - add details about mutation count: how using J's suggestion we tried to incorporate genomic context
 - add presentation-ready sentences 

## Introduction & motivation
* Clinvar is big and helps bring context to variants, but not all variants *edit further* 
* In-silico predictors exist that predict pathogenicity, they are reasonably good see results
* We are interested in this project to help our users increase the context when making their decisions: this means
that we are interested in feature extraction as well as accurate predictions. 
* Calling variants results in hundreds of potential clinically improtant mutations, even after filtering. We need to reduce the number of false positives, so precision is more important than recall: the need is to have a small number of highly recommended mutations, where if the critical variant is not found then we are easily able to relax the thresholds. (this might not be clearly written but is an important point for guiding our decisions) 

## Results
* Experimental table of > 20 experiments: ( Notebook naming is as follows: id.featureset.chromosomes.model (ex: 1.1.234.svm))

| **Notebook number:**                         | **Input data: total # of examples** | **Model: details**       | **Evaluation: baseline/primary class = 1**    | **Evaluation: Accuracy** | **Evaluation: Precision** | **Evaluation: Recall ** | **Evaluation: F1** | **Evaluation: AUC** |
| -------------------------------------------- | ----------------------------------- | ------------------------ | --------------------------------------------- | ------------------------ | ------------------------- | ----------------------- | ------------------ | ------------------- |
| **1.1.2\_4.svm**                             | 13767                               | SVM (rbf)                | 0.71                                          | 0.74                     | 0.64                      | 0.16                    | 0.25               | 0.64                |
| **2.1.2\_4.RF**                              | 13767                               | RF (n=10)                | 0.71                                          | 0.80                     | 0.64                      | 0.65                    | 0.64               | 0.85                |
| **3.1.2\_4.nn TORERUN**                      | 13767                               | 3 hidden layers          | 0.71                                          | 0.73                     | 0.36                      | 0.5                     | 0.42               |                     |
| 3.1.2\_4.nn<br>**MK ran monday (disc)**      |                                     |                          | 0.71 (but 0.68 in test set of 3442 examples ) | 0.68                     | 0.0                       | 0.0                     | nan                |                     |
| 4.2.2\_4.svm                                 | 13767                               | SVM (rbf)                | 0.71                                          | 0.74                     | 0.65                      | 0.21                    | 0.32               | 0.62                |
| 5.2.2\_4.RF                                  | 13767                               | RF(n=10)                 | 0.71                                          | 0.80                     | 0.64                      | 0.63                    | 0.68               | 0.84                |
| 6.2.2\_4.NN                                  |                                     |                          | 0.71 (but 0.72 in test set of 3434 examples)  | 0.72\*                   | 0.0                       | 0.0                     | nan                |                     |
| 7.3.2\_4.svm                                 | 13767                               | SVM (rbf)                | 0.71                                          | 0.74                     | 0.68                      | 0.18                    | 0.0.28             | 0.70                |
| 8.3.2\_4.RF                                  | 13767                               | RF(n=10)                 | 0.71                                          | 0.81                     | 0.64                      | 0.68                    | 0.66               | 0.85                |
| 9.3.2\_4.nn                                  |                                     |                          | 0.71 (but 0.68 in test set of 3442 examples ) | 0.68                     |                           |                         |                    |                     |
| 10.4.2\_4.svm                                | 13767                               | SVM (rbf)                | 0.71                                          | 0.75                     | 0.76                      | 0.16                    | 0.27               | 0.69                |
| 11.4.2\_4.RF                                 | 13767                               | RF(n=10)                 | 0.71                                          | 0.86                     | 0.75                      | 0.74                    | 0.74               | 0.90                |
| 12.4.2\_4.nn                                 | 13767                               | 3 hidden layers          | 0.71                                          | 0.72                     | 0                         | 0                       | nan                |                     |
| 13.1.2\_4u.svm                               | 40905                               | svm(rbf), balanced class | see below                                     | 0.39                     | 0.80                      | 0.26                    | 0.39               |                     |
| 14.1.2\_4u.RF                                | 40905                               | RF(n=10) balanced class  | see below                                     | 0.67                     | 0.76                      | 0.77                    | 0.77               |                     |
| 15.4.2\_4.nn<br>**TO RERUN WITH SPLIT SETS** |                                     | Balanced dataloader      |                                               | 0.66                     | 0.47                      | 0.59                    | 0.56               |                     |
| 16.4.2\_4.GB (compare with 11)               |                                     | Gradient Boost (n=10)    |                                               | 0.82                     | 0.82                      | 0.47                    | 0.59               |                     |
| 17.5.2\_4.svm                                | 13767                               | svm(rbf)                 | 0.71                                          | 0.75                     | 0.76                      | 0.16                    | 0.27               | 0.69                |
| 18.5.2\_4.RF                                 | 13767                               | RF(n=10)                 | 0.71                                          | 0.87                     | 0.79                      | 0.73                    | 0.76               | 0.93                |
| 19.5.2\_4u.RF                                | 40905                               | RF(n=10) balanced        |                                               | 0.73                     | 0.77                      | 0.86                    | 0.81               |                     |
| 20.6.2\_4.RF                                 | 40905                               | RF(n=10) balanced        |                                               | 0.74                     | 0.78                      | 0.88                    | 0.82               |                     |
| 21.7.2\_4.RF                                 | 40905                               | RF(n=100)                |                                               | 0.75                     | 0.89                      | 0.78                    | 0.83               |                     |
| 22.8.5\_7.RF                                 | 40905                               | RF(n=100)                |                                               | 0.76                     | 0.77                      | 0.91                    | 0.84               |                     |



* *I think we should add the in-silico scores and binning results as well* 

## Methodology 
* Models: Test three different model architechtures with increasing hyperparameter adjustments and increased data.
* Input data:
  - Labeled output: Begin with binary class prediction, expand to include unknown labels so as to harness as much information from ClinVar as possible. Description of class distribution is below, models were trained with balanced by proportion of class label. 
  - Features: largely taken from dbNSFP which is a aggregation of >350 features including in-silico predictors, other high-level aggregated metrics, and low level information about chemistry and biological annotations at the position of interest. Feature selection is critical for our project because we seek to learn which features are most informative.

## Discussion of Results
* Based this on the table, highlight only the experiments that are most informative to compare. 
* Can include here how we used the results of earlier experiments to inform the subsequent model setup.

## Discussion of Future Directions and Limitations 
* We are bound by the assumption, biases, and data of ClinVar. With the constraints that we faced, we preferentially set our efforts to selecting the best features + model combination possible, using conventional trainings, validation, and testings splits of the labeled clinvar data. We would explore alternative sources of pathogenically labeled variants to evaluate the geerailzability of our findings. For example, Human Mandelian Genomic Database *check name and link to* or manually curated clinical findings would show how well the model trained on clinvar would preform on other datasets. The attempts in this direction were meaningful, but being the strict requirement of disjoint data to avoid biases was beyond the scope of what we could finish. 
* There was a preliminary efforts to evaluate variants using the model from experiment 19 on unlabeled data, with the required features fro mset 5. A handful of variants preidcted by the model to be pathogenic were manual evaulated to be consistent with the prediction. These can be found in the supplemental notes below. 
* giving a finer resolution to dgi if it seems to be informative.
* Better handling of unknown label, exploration of methods such as `out-of-distribtuion detection` were not easily incorporated, though we suspect would likely improve the accuracy.




--- 
# Supplemental notes

## Distribution of labels in the data:
* Not sure the best way to show this, feed back most welcome. 
* Early experiments were run with a subset of all genomic examples: using chromosomse 2, 3, 4. Initially, only examples with pathogenic (including likely-pathogenic) and benign (including likely-benign) were selected. These were at a balance of 71% pathogenic. 
* Later experiments allowed for multi-class classification, which included the `unknown clinical significance` class. The distributions of the classes, for chromosomes 2, 3, 4 were the following: 
PROPORTION OF LABELS: 
0: unknown       0.663440 
1: Pathogenic    0.240068
2: Benign        0.096492
* Models used balanced classes from experiment *13 onward* without a large increase in accuracy. 

## Predicting on unlabeled data using model 19: 

1. Generate the dataframe that has the 9 features of feature set 5 for chromosome 2, 3, 4 for pathogentic, benign, and unknown. data_processing/Dataprocessing_2-4u_featureset5.ipynb. pickle the dataframe → 

2. Use the picked dataframe to train a model, 19.5.2_4u.RF.ipynb, pickle the model → pickled_models/19.5.2_4u.RF.pkl

3. Generate dataframe that has 9 features of feature set 5 for unlabeled data from chromosome 1,2,3,4: → store in pickled/chr1-4_nolabels.pkl

4. Use the trained model on different data: chromosomes 1, 2, 3, 4 with no clinvar labels. model_predictions/dbNSFP_chr1_4_nolabels.ipynb
