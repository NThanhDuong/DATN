import os 
import pandas as pd
import tqdm

product_data_path = 'C:/D/Doan/data-platform/data/dataRaw'
list_cate = os.listdir(product_data_path)
merge_table=pd.read_csv('C:/D/Doan/data-platform/data/dataRaw/action-camera-4879.csv')
df = pd.DataFrame(list_cate)
print(len(list_cate))
# for tbl in df[0][55:59]:
#     # print(tbl)
#     df_table = pd.read_csv(f'C:/D/Doan/data-platform/data/dataRaw/{tbl}')
#     merge_table = pd.concat([merge_table,df_table])
# merge_table.to_csv("C:/D/Doan/data-platform/data/Products3.csv")

# df_table = pd.read_csv('./data/dataRaw/action-camera-4879.csv')
# print(df_table)
