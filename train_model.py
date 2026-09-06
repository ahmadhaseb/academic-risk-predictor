import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report,accuracy_score


#dataset loading
df = pd.read_csv('C:\AI_SocialMedia_Imapct\AI_SocialMedia_Student_Health_Dataset_clean.csv')

#Seprate Features(X) and Target (Y)
x = df.drop(columns=['Student_ID','Academic_Failure_Risk'])
y = df['Academic_Failure_Risk']

#Columns Grouping
numericl_cols = ['Age', 'Daily_Social_Media_Hours', 'Daily_AI_Tool_Usage_Hours',
    'Sleep_Hours', 'Physical_Activity_Hours', 'Mental_Health_Score',
    'Physical_Health_Score', 'Social_Isolation_Score', 'Academic_Performance_Score']

ordinal_columns = ['Burnout_Level', 'Education_Level']
nominal_coumns = ['Gender']

#Catogrize Ordinal Columns
burnout_order = ['Low', 'Moderate', 'High', 'Severe']
Education_order = ['High School', 'College', 'University']

#Preprocessor Setup
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numericl_cols),
        ('ord', OrdinalEncoder(categories=[burnout_order,Education_order]),ordinal_columns),
        ('nom', OneHotEncoder(handle_unknown='ignore',sparse_output=False), nominal_coumns)
    ]
)

#Class Weight Handling
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier(n_estimators=100,class_weight='balanced',random_state=42))
])

#Train Test Split(80% Train,20% Test)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)

#Model Training
model_pipeline.fit(x_train,y_train)

#Model Evaluation
y_pred = model_pipeline.predict(x_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

#Modle Saving
joblib.dump(model_pipeline, 'AI_Student_Impact.pkl')
print("Model saved successfully in local PyCharm environment!")

import sklearn
print(sklearn.__version__)