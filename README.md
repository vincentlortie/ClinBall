# ClinBall ![alt text](https://a.slack-edge.com/production-standard-emoji-assets/10.2/apple-medium/1f63b@2x.png)


The goal of this project is to predict ClinVar predictions on variants that lack existing ClinVar data. 

Final Model Presented can be found [here](https://github.com/vincentlortie/ClinBall/blob/master/notebooks/experiments/AIGenomics_Model_Quickstart.ipynb) or at `notebooks/experiments/AIGenomics_Model_Quickstart.ipynb`. For quick start to run, please see `notebooks/QuickStart.txt` or clone and run `notebooks/experiments/AIGenomics_Model_Quickstart.ipynb` directly. 

---
# Report

## Introduction & motivation
* ClinVar is an aggregation of various sources that provide clincal data for variants
* In-silico predictors exist that predict pathogenicity, they are reasonably good see results
* We are interested in this project to help our users make informed decisions: this means
that we are interested in feature extraction as well as accurate predictions
* Our usage would not be to select variants of pathogenicity, but to prioritze them. This is a critical distriction because it means that a False Positive is worse than other clinical applications, and a False Negative is not as bad (we are not removing variants on the basis of this prediction).
* Calling variants results in hundreds of potential clinically improtant mutations, even after filtering. We need to reduce the number of false positives, so precision is more important than recall: the need is to have a small number of highly recommended mutations, where if the critical variant is not found then we are easily able to relax the thresholds. 

## Results
* Experimental table of > 20 experiments: ( Notebook naming is as follows: id.featureset.chromosomes.model (ex: 1.1.234.svm))

| **Notebook number:**      | **Input data: total # of examples** | **Model: details**       | **Evaluation: baseline/primary class = 1**    | **Evaluation: Accuracy** | **Evaluation: Precision** | **Evaluation: Recall ** | **Evaluation: F1** | **Evaluation: AUC** |
| ------------------------- | ----------------------------------- | ------------------------ | --------------------------------------------- | ------------------------ | ------------------------- | ----------------------- | ------------------ | ------------------- |
| **1.1.2\_4.svm**          | 13767                               | SVM (rbf)                | 0.71                                          | 0.74                     | 0.64                      | 0.16                    | 0.25               | 0.64                |
| **2.1.2\_4.RF**           | 13767                               | RF (n=10)                | 0.71                                          | 0.80                     | 0.64                      | 0.65                    | 0.64               | 0.85                |
| **3.1.2\_4.nn**           | 13767                               | 3 hidden layers          | 0.71                                          | 0.73                     | 0.36                      | 0.5                     | 0.42               |                     |
| 3.1.2\_4.nn<br>           | 13767                               | MPL                      | 0.71 (but 0.68 in test set of 3442 examples ) | 0.68                     | 0.0                       | 0.0                     | nan                |                     |
| 4.2.2\_4.svm              | 13767                               | SVM (rbf)                | 0.71                                          | 0.74                     | 0.65                      | 0.21                    | 0.32               | 0.62                |
| 5.2.2\_4.RF               | 13767                               | RF(n=10)                 | 0.71                                          | 0.80                     | 0.64                      | 0.63                    | 0.68               | 0.84                |
| 6.2.2\_4.NN               | 13767                               | MPL                      | 0.71 (but 0.72 in test set of 3434 examples)  | 0.72\*                   | 0.0                       | 0.0                     | nan                |                     |
| 7.3.2\_4.svm              | 13767                               | SVM (rbf)                | 0.71                                          | 0.74                     | 0.68                      | 0.18                    | 0.0.28             | 0.70                |
| 8.3.2\_4.RF               | 13767                               | RF(n=10)                 | 0.71                                          | 0.81                     | 0.64                      | 0.68                    | 0.66               | 0.85                |
| 9.3.2\_4.nn               | 13767                               | MLP                      | 0.71 (but 0.68 in test set of 3442 examples ) | 0.68                     | 0.0                       | 0.0                     | nan                |                     |
| 10.4.2\_4.svm             | 13767                               | SVM (rbf)                | 0.71                                          | 0.75                     | 0.76                      | 0.16                    | 0.27               | 0.69                |
| 11.4.2\_4.RF              | 13767                               | RF(n=10)                 | 0.71                                          | 0.86                     | 0.75                      | 0.74                    | 0.74               | 0.90                |
| 12.4.2\_4.nn              | 13767                               | 3 hidden layers          | 0.71                                          | 0.72                     | 0                         | 0                       | nan                |                     |
| 13.1.2\_4u.svm            | 40905                               | svm(rbf), balanced class | 0.66u                                         | 0.39                     | 0.80                      | 0.26                    | 0.39               |                     |
| 14.1.2\_4u.RF             | 40905                               | RF(n=10) balanced class  | 0.66u                                         | 0.67                     | 0.76                      | 0.77                    | 0.77               |                     |
| 15.4.2\_4.nn              | 40905                               | Balanced dataloader      | 0.66u                                         | 0.62                     | 0.44                      | 0.68                    | 0.53               |                     |
| 16.4.2\_4.GB              | 40905                               | Gradient Boost (n=10)    | 0.71                                          | 0.82                     | 0.82                      | 0.47                    | 0.59               |                     |
| 17.5.2\_4.svm             | 13767                               | svm(rbf)                 | 0.71                                          | 0.75                     | 0.76                      | 0.16                    | 0.27               | 0.69                |
| 18.5.2\_4.RF              | 13767                               | RF(n=1000)<br>balanced   | 0.71                                          | 0.87                     | 0.79                      | 0.73                    | 0.76               | 0.93                |
| 19.5.2\_4u.RF             | 40905                               | RF(n=1000) balanced      | 0.66u                                         | 0.73                     | 0.77                      | 0.86                    | 0.81               |                     |
| 20.6.2\_4u.RF             | 40905                               | RF(n=100) balanced       | 0.66u                                         | 0.74                     | 0.78                      | 0.88                    | 0.82               |                     |
| 21.7.2\_4u.RF             | 40905                               | RF(n=100)                | 0.66u                                         | 0.75                     | 0.89                      | 0.78                    | 0.83               |                     |
| 22.8.5\_7u.RF             | 40905                               | RF(n=100)                | 0.66u                                         | 0.76                     | 0.77                      | 0.91                    | 0.84               |                     |
| 23.8.5\_7uc.RF            | 40905                               | RF(n=100)                | 0.66u                                         | 0.75                     | 0.77                      | 0.91                    | 0.84               |                     |
| 24.8.5\_7c.RF             | 13767                               | RF(n=100)                | 0.66u                                         | 0.84                     | 0.74                      | 0.80                    | 0.77               |                     |
| 25.5.2\_4.RFunk           | 13820, then 17808 (unk)             | unk boosted RF(n=1000)   | 0.71, then 0.57                               | 0.88                     | 0.84                      | 0.76                    | 0.80               |                     |
| 26.4.2\_4.LR<br>          | 13820                               | Logistic Regression      | 0.71                                          | 0.71                     | 0.49                      | 0.76                    | 0.60               |                     |
| 27.5.2\_4u.KNN            | 13820                               | Nearest Neighbour (n=3)  | 0.66u                                         | 0.67                     | 0.72                      | 0.84                    | 0.80               |                     |
| 28.5.5\_7.RF              | 13820                               | RF(n=100)                | 0.70                                          | 0.87                     | 0.68                      | 0.78                    | 0.73               | 0.92                |
| 29.5.8\_10.RF             | 9472                                | RF(n=100)                | 0.69                                          | 0.85                     | 0.70                      | 0.81                    | 0.75               | 0.92                |
| 30.5.11\_14.RF            | 7836                                | RF(n=100)                | 0.75                                          | 0.87                     | 0.80                      | 0.67                    | 0.73               | 0.91                |
| 31.5.15\_19.RF            | 17361                               | RF(n=100)                | 0.75                                          | 0.88                     | 0.80                      | 0.69                    | 0.74               | 0.92                |
| 32.5.20\_Y.RF             | 10154                               | RF(n=100)                | 0.78                                          | 0.87                     | 0.78                      | 0.62                    | 0.69               | 0.91                |
| 33.5.2\_4.GB              | 13767                               | RF(n=100)                | 0.71                                          | 0.87                     | 0.80                      | 0.74                    | 0.77               | 0.93                |
| 34.polyphen.2\_4.RF       | 13825                               | RF(n=100)                | 0.71                                          | 0.76                     | 0.73                      | 0.25                    | 0.38               | 0.66                |
| 35.genocanyon.2\_4.RF     | 13825                               | RF(n=100)                | 0.71                                          | 0.71                     | 0.46                      | 0.27                    | 0.34               | 0.57                |
| 36.fathmm.2\_4.RF         | 13825                               | RF(n=100)                | 0.71                                          | 0.79                     | 0.65                      | 0.54                    | 0.59               | 0.79                |
| 37.mutationtaster.2\_4.RF | 13825                               | RF(n=100)                | 0.71                                          | 0.77                     | 0.68                      | 0.34                    | 0.45               | 0.71                |
| 38.metasvm.2\_4.RF        | 13825                               | RF(n=100)                | 0.71                                          | 0.86                     | 0.76                      | 0.71                    | 0.74               | 0.90                |
| 39.7.2\_4.RF              | 13825                               | RF(n=100)                | 0.71                                          | 0.88                     | 0.90                      | 0.94                    | 0.92               | 0.94                |
| 40.8.2\_4.RF              | 13825                               | RF(n=100)                | 0.71                                          | 0.89                     | 0.90                      | 0.94                    | 0.92               | 0.94                |
| 41.5.2\_4.RF              | 13825                               | RF(n=1000)               | 0.71                                          | 0.87                     | 0.80                      | 0.73                    | 0.76               | 0.93                |
| 42.5.1\_22.RF             | 65424                               | RF(n=1000)               | 0.722                                         | 0.81 ±0.1                | 0.80±0.08                 | 0.5±0.11                | 0.60±0.1           |                     |



## Methodology 
* Models: Test three different model architectures with increasing hyperparameter adjustments and increased data.
* Input data:
  - Labeled output: Begin with binary class prediction, expand to include unknown labels so as to harness as much information from ClinVar as possible. Description of class distribution is below, models were trained with balanced by proportion of class label. 
  - Features: largely taken from dbNSFP which is a aggregation of >350 features including in-silico predictors, other high-level aggregated metrics, and low level information about chemistry and biological annotations at the position of interest. Feature selection is critical for our project because we seek to learn which features are most informative.
* Novel feature: in order to incorporate a measure of genomic context, we sought to use the position of the variant to assess the variants nearby. Intially, a convolution was applied but to use it successfully with other features, we decided to simplify and count mutations at various Kb distances from the variant in question. This is added in a seperate data processing step.

## Discussion of Results
* Ran various models to test which would work best for our data. Selected Random Forest as it preformed favorably. 
* Experimented with various feature sets that would work well together. Selected Feature set 5 as trade off between preformance and easily interpretable features. 
* Fixing model (RF) and features (set 5), we fine tuned the parameters of the model.
* Cross validation is a work in progress.
* Unknonw labels were complex to work with as it is not quite its own class, using these examples is a work in progress.

## Discussion of Future Directions and Limitations 
* We are bound by the assumption, biases, and data of ClinVar. With the constraints that we faced, we preferentially set our efforts to selecting the best features + model combination possible, using conventional trainings, validation, and testings splits of the labeled clinvar data. We would explore alternative sources of pathogenically labeled variants to evaluate the geerailzability of our findings. For example, Human Mandelian Genomic Database *check name and link to* or manually curated clinical findings would show how well the model trained on clinvar would preform on other datasets. The attempts in this direction were meaningful, but being the strict requirement of disjoint data to avoid biases was beyond the scope of what we could finish. 
* There was a preliminary efforts to evaluate variants using the model from experiment 19 on unlabeled data, with the required features fro mset 5. A handful of variants preidcted by the model to be pathogenic were manual evaulated to be consistent with the prediction. These can be found in the supplemental notes below. 
* giving a finer resolution to dgi if it seems to be informative.
* Better handling of unknown label, exploration of methods such as `out-of-distribtuion detection` were not easily incorporated, though we suspect would likely improve the accuracy.



---
# Supplemental notes

## Distribution of labels in the data:
* Early experiments were run with a subset of all genomic examples: using chromosomse 2, 3, 4. Initially, only examples with pathogenic (including likely-pathogenic) and benign (including likely-benign) were selected. These were at a balance of 71% pathogenic. 
* Models used balanced classes from experiment *13 onward* without a large increase in accuracy. 
* Later experiments allowed for multi-class classification, which included the `unknown clinical significance` class. The distributions of the classes:

### Chr2-4:
TOTAL SUM OF LABELS: 1    9863
2    3957
PERCENT OF LABELS: 
1    0.713676
2    0.286324
TOTAL: 13820


### Chr2-4U:
TOTAL SUM OF LABELS: 0    27177
1     9863
2     3957

PERCENT OF LABELS: 
0    0.662902
1    0.240579
2    0.096519

TOTAL: 40997

### Chr1_22:
TOTAL SUM OF LABELS: 1    47278
0    18146
PERCENT OF LABELS: 
1    0.72264
0    0.27736
TOTAL: 65424



## WIP: Predicting on unlabeled data using model 19 (exp 25): 

1. Generate the dataframe that has the 9 features of feature set 5 for chromosome 2, 3, 4 for pathogentic, benign, and unknown. data_processing/Dataprocessing_2-4u_featureset5.ipynb. pickle the dataframe → 
2. Use the picked dataframe to train a model, 19.5.2_4u.RF.ipynb, pickle the model → pickled_models/19.5.2_4u.RF.pkl
3. Generate dataframe that has 9 features of feature set 5 for unlabeled data from chromosome 1,2,3,4: → store in pickled/chr1-4_nolabels.pkl
4. Use the trained model on different data: chromosomes 1, 2, 3, 4 with no clinvar labels. model_predictions/dbNSFP_chr1_4_nolabels.ipynb

## Dead ends

* Using features from well-preforming in-silico predictors was very challenging: the publications do not release the data used for the creation of the model. Some features were well described, while others were quite obscur; of those that were available through other sources, few were ready-to-use and would require significant data preprocessing. 
* Integrating pharma db with our dataset -> gene - drug associations did not perform adequately in the model. Getting more depth did not help either.
* Manually curating the training data did not help either. We selected the data points with the most complete data and the results did not vary.
*  lncRNA multiple databases exist. However, the data format was incompatible with ours. Reliable standards have not emerged yet to the point where we can use the data.
