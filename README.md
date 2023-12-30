# KIDNEY-STONE-PREDICTION-USING-MACHINE-LEARNING

Data mining methods and machine learning play a major role in this aspect of biosciences. Chronic Kidney Disease (CKD) is a condition in which the kidneys are damaged and cannot filter blood as they always do. A family history of kidney diseases or failure, high blood pressure, type 2 diabetes may lead to CKD This is a lasting damage to the kidney and chances of getting worse by time is high. The very common problems that results due to a kidney failure are heart diseases, anaemia, bone diseases, high potassium and calcium. The worst-case situation leads to complete kidney failure and necessitates kidney transplant to live. An early detection of CKD can increase the quality of life to a greater extent. This calls for good prediction algorithm to predict CKD at an earlier stage. Literature shows a wide range of machine learning algorithms employed for the prediction of CKD. This paper uses data pre-processing, data transformation and various classifiers to predict CKD and also proposes best Prediction framework for CKD. The results of the framework show promising results of better prediction at an early stage of CKD.

- **Data Collection:**
  - 400 records from UCI Machine Learning Repository.
  - After cleaning, 220 records remained.
  - 25 attributes, including numerical (e.g., age, blood pressure) and nominal (e.g., specific gravity) attributes.
  - Class distribution: 63% CKD, 37% NOTCKD.

- **Data Preprocessing:**
  - 80% of time dedicated to data preparation.
  - Cleaning, removing missing values, and formatting for SVM compatibility.
  - Utilization of Data Mining (DM) tools for real-time data analysis.

- **Training and Testing Data:**
  - Model training and testing under varied SVM parameter conditions.
  - Aim for maximum accuracy.
  - 70:30 split for training and testing, respectively.
  - Provision for algorithm improvisation if needed.

- **Results and Analysis:**
  - Evaluation based on parameters:
    - **Precision:**
      - Fraction of retrieved data useful for the query.
    - **Recall:**
      - Fraction of relevant data effectively retrieved.
    - **F-measure:**
      - A measure combining precision and recall.
    - **Accuracy:**
      - Proximity of computation to true value.
      - Calculated using true positive, true negative, false positive, and false negative.

This plan outlines the data collection, preprocessing steps, training/testing procedures, and parameters used for evaluating the proposed model's results in terms of precision, recall, F-measure, and accuracy.

**ALGORITHM USED**
- **Decision Tree:**
  - Solves regression and classification problems.
  - Creates a model with decision rules derived from training data.
  - Tree structure with roots, branches, and leaves.
  - Easy to understand, user-friendly rules.
  - Effective association representation among dataset attributes.
  - Requires less computation compared to other algorithms.

- **Random Forest:**
  - Ensemble of decision trees for classification and regression.
  - Constructs multiple trees using random subsets of training data.
  - Higher accuracy due to a collection of decision trees.
  - Fast runtime, accommodates missing data.
  - Handles unbalanced data, robust against overfitting.

- **Support Vector Machine (SVM):**
  - Supervised learning model for classification and multivariate analysis.
  - Builds a model to assign examples to categories.
  - Non-probabilistic binary linear classifier.
  - Maps training examples to maximize the gap between categories.
  - Useful in detecting Chronic Kidney Disease (CKD).
  - Utilizes support-vector clustering for unlabeled data.

**Road Map**
Input: Chronic Kidney Disease Dataset

Output: High Accuracy prediction Framework

Step 1: Input data Step2: Pre-process the data 

Step 2.1: Convert Categorical values to numerical values

Step 2.2: Replace numerical missing values by Mean

Step2.3 Replace Categorical missing values by Mode

Step3: Construct Classifier Models

Step3.1: Construct Decision Tree Model Step3.2: Construct Random Forest Model

Step 3.3: Construct SVM model

Step 4: Check the accuracy of the constructed models using confusion matrix 

Step 5: Decide the best prediction model for CKD
