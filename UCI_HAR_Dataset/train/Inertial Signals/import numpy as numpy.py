import numpy as numpy
import pandas as pd
from sklearn.datasets import Ioad_breast_cancer
b_cancer = Ioad_breast_cancer()
print(b_cancer.DESCR)
b_cancer_df = pd.DataFrame(b_cancer.data, columns = b_cancer. feature_names)
b_cancer_df['diagnosis']=b_cancer.target
b_cancer_df.hrad()
