# ASSOCIATION RULE LEARNING (BİRLİKTELİK KURALI ÖĞRENİMİ)

# 1. Data Preprocessing
# 2. Preparing the ARL Data Structure (Invoice-Product Matrix)
# 3. Deriving Association Rules
# 4. Preparing the Script for the Study
# 5. Making Product Recommendations to Users at the Cart Stage


# 1. Data Preprocessing
# !pip install mlxtend
import pandas as pd
pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
# çıktının tek bir satırda olmasını sağlar
pd.set_option('display.expand_frame_repr', False)
from mlxtend.frequent_patterns import apriori, association_rules

# https://archive.ics.uci.edu/ml/datasets/Online+Retail+II

df_ = pd.read_excel("datasets/online_retail_II.xlsx",
                    sheet_name="Year 2010-2011")
df = df_.copy()

df.head()

df.describe().T
df.info()
df.isnull().sum()