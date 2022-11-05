# Rice Classification: Cammeo vs Osmancik

The present problem has been dealt with in the article written by Cinar and Koklu [1]. Here they highlight the importance of rice classification for its subsequent separation and break down the problem into 5 steps:
1. **Image acquisition**. They emulated the industrial mechanism.
2. **Image processing**. The images were converted to binary.
3. **Extraction of morphological characteristics**. They obtain morphological characteristics that, together with the class of rice, make up the dataset [2].
4. **Classification**. Models were created using: Logistic Regression (LR), Multiplayer Perceptron (MLP), Support Vector Machine (SVM), Decision Tree (DT), Random Forest (RF), Naive Bayes (NB), and K-Nearest Neighbor (KNN).
5. **Performance Evaluation**. Metrics used: Accuracy, Sensivity, Specificity, Precision F1-Score, Negative Predictive Value, False Positive Rate, False Discovery Rate, False Negative Rate.

This project aims to partially reproduce the study (points 4 and 5), using the metrics, methods and techniques seen so far in this course [3]. To this end, the following steps will be followed:
1. **Exploratory data analysis (EDA)**: The basic characteristics of the information will be extracted. An Extensive EDA will check which would be the apparently most important morphological characteristics.
2. **Model training**: The following methods will be used: LR, DT, and RF. In addition, cross validation will be used in all of them, being k = 4, and the division of the dataset: 25% for the test and 75% for the training.
3. **Evaluation**: Since the classification only has two classes, it can be treated binary. Therefore we will use the Area Under the Curve (AUC) as a metric.

The method with the best performance will be the one used for deployment.

## How to Deploy

### Virtual environment

```sh
# Create a virtual environment
python3.9 -m venv .venv 

# Activate venv for GNU/Linux
source .venv/bin/activate
# Activate venv for  Windows PowerShell
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r ./requirements.txt
```

### Local deployment using Docker

```sh
# Build docker image
docker build -t rice-prediction .

# Launch local container
docker run -it -p 9696:9696 rice-prediction:latest
```

With the venv activated, you can test the local deployment using `predict-test.py`

```sh
python predict-test.py
```

## References

**[1]** Cinar, I. and Koklu, M. (2019). Classification of Rice Varieties Using Artificial Intelligence Methods. International Journal of Intelligent Systems and Applications in Engineering,  vol.7, no.3 (Sep. 2019), pp.188-194. https://doi.org/10.18201/ijisae.2019355381. 

**[2]** https://www.muratkoklu.com/datasets/

**[3]** https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp