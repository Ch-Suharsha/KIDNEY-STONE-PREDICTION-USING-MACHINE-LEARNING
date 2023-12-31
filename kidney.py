# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_curve, auc, confusion_matrix, classification_report, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

# Reading the dataset
kidney = pd.read_csv("/content/kidney_disease dataset.csv")
kidney.head()

# Information about the dataset
kidney.info()

# Description of the dataset
kidney.describe()

# To see what are the column names in our dataset
print(kidney.columns)

# Mapping the text to 1/0 and cleaning the dataset
kidney[['htn', 'dm', 'cad', 'pe', 'ane']] = kidney[['htn', 'dm', 'cad', 'pe', 'ane']].replace(to_replace={'yes': 1, 'no': 0})
kidney[['rbc', 'pc']] = kidney[['rbc', 'pc']].replace(to_replace={'abnormal': 1, 'normal': 0})
kidney[['pcc', 'ba']] = kidney[['pcc', 'ba']].replace(to_replace={'present': 1, 'notpresent': 0})
kidney[['appet']] = kidney[['appet']].replace(to_replace={'good': 1, 'poor': 0, 'no': np.nan})
kidney['class'] = kidney['class'].replace(to_replace={'ckd': 1.0, 'ckd\t': 1.0, 'notckd': 0.0, 'no': 0.0})
kidney['pe'] = kidney['pe'].replace(to_replace='good', value=0)  # Not having pedal edema is good
kidney['appet'] = kidney['appet'].replace(to_replace='no', value=0)
kidney['cad'] = kidney['cad'].replace(to_replace='\tno', value=0)
kidney['dm'] = kidney['dm'].replace(to_replace={'\tno': 0, '\tyes': 1, ' yes': 1, '': np.nan})
kidney.drop('id', axis=1, inplace=True)
kidney.head()

# This helps us to count how many NaN are there in each column
len(kidney) - kidney.count()

# This shows the number of rows with missing data
kidney.isnull().sum(axis=1)

# This is a visualization of missing data in the dataset
sns.heatmap(kidney.isnull(), yticklabels=False, cbar=False, cmap='viridis')

# This shows the number of complete cases and also removes all the rows with NaN
kidney2 = kidney.dropna()
print(kidney2.shape)

# Now our dataset is clean
sns.heatmap(kidney2.isnull(), yticklabels=False, cbar=False, cmap='viridis')
sns.heatmap(kidney2.corr())

# Counting the number of normal vs. abnormal red blood cells of people having chronic kidney disease
print(kidney2.groupby('rbc').rbc.count().plot(kind="bar"))

# This plot shows the patient's sugar level compared to their ages
kidney2.plot(kind='scatter', x='age', y='su')
plt.show()

# Shows the maximum blood pressure having chronic kidney disease
print(kidney2.groupby('class').bp.max())
print(kidney2['dm'].value_counts(dropna=False))

X_train, X_test, y_train, y_test = train_test_split(kidney2.iloc[:, :-1], kidney2['class'], test_size=0.33,
                                                    random_state=44, stratify=kidney2['class'])
print(X_train.shape)
y_train.value_counts()

rfc = RandomForestClassifier(random_state=22)
rfc_fit = rfc.fit(X_train, y_train)
rfc_pred = rfc_fit.predict(X_test)
print(confusion_matrix(y_test, rfc_pred))
print(classification_report(y_test, rfc_pred))
accuracy_score(y_test, rfc_pred)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
pred = knn.predict(X_test)
print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
accuracy_score(y_test, pred)

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
accuracy_score(y_test, predictions)

feature_importances = pd.DataFrame(rfc.fit(X_train, y_train).feature_importances_,
                                   index=X_train.columns, columns=['importance']).sort_values('importance', ascending=False)
print(feature_importances)

kidney3 = kidney.drop(columns=['rbc', 'pc', 'sod', 'pot', 'pcv', 'wc', 'rc'])
kidney3.shape
kidney3.head()
kidney3.isnull().sum()
kidney3.mode()

# Fill in the NaNs with the mode for each column.
kidney3_imp = kidney3.apply(lambda x: x.fillna(x.value_counts().index[0]))
X_train, X_test, y_train, y_test = train_test_split(kidney3_imp.iloc[:, :-1], kidney3_imp['class'],
                                                    test_size=0.33, random_state=44, stratify=kidney3_imp['class'])
y_train.value_counts()

rfc = RandomForestClassifier(random_state=22)
rfc_fit = rfc.fit(X_train, y_train)
rfc_pred = rfc_fit.predict(X_test)
print(confusion_matrix(y_test, rfc_pred))
print(classification_report(y_test, rfc_pred))
accuracy_score(y_test, rfc_pred)

logmodel = LogisticRegression()
logmodel.fit(X_train, y_train)
predictions = logmodel.predict(X_test)
print(classification_report(y_test, predictions))
print(confusion_matrix(y_test, predictions))
accuracy_score(y_test, predictions)

dtree = DecisionTreeClassifier()
dtree.fit(X_train, y_train)
predictions = dtree.predict(X_test)
print(classification_report(y_test, predictions))

# Rest of the code for decision tree visualization, random forest, and k-neighbors classifier is unchanged.
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
import graphviz
from IPython.display import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

# Assume you have already defined X_train, y_train, X_test, y_test, and kidney3

# Decision Tree Visualization
features = list(kidney3.columns[1:])
target = 'class'

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

dot_data = export_graphviz(dt, out_file=None,
                           feature_names=features,
                           class_names=['negative', 'positive'],
                           filled=True, rounded=True,
                           special_characters=True)

graph = graphviz.Source(dot_data)
graph.render("decision_tree")  # Saves the decision tree to a file
Image("decision_tree.png")  # Displays the decision tree in Jupyter notebook

# Random Forest Classifier
rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(X_train, y_train)
rfc_pred = rfc.predict(X_test)

print(confusion_matrix(y_test, rfc_pred))
print(classification_report(y_test, rfc_pred))
print(accuracy_score(y_test, rfc_pred))

# Choosing a K Value using the Elbow Method
error_rate = []

for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10, 6))
plt.plot(range(1, 40), error_rate, color='blue', linestyle='dashed', marker='o',
         markerfacecolor='red', markersize=10)
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')

# K-Nearest Neighbors Classifier
knn = KNeighborsClassifier(n_neighbors=1)
pred = knn.predict(X_test)

print(confusion_matrix(y_test, pred))
print(classification_report(y_test, pred))
print(accuracy_score(y_test, pred))
