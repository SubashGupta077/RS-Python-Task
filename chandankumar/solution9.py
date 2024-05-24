import numpy as np
import pandas as pd
!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!kaggle datasets download -d arshid/iris-flower-dataset
import zipfile
zip_ref = zipfile.ZipFile('/content/iris-flower-dataset.zip', 'r')
zip_ref.extractall('/content')
zip_ref.close()
df=pd.read_csv('/content/IRIS.csv')
df.shape
df.head()
df['sepal_length'].sum()
df['sepal_length'].max()
df['sepal_length'].min()
