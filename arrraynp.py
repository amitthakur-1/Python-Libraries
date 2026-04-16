import numpy as np
import pandas as pd

data=np.array([[1,"varun",23],[2,"aman",23],[3,"dhir",23]])
df=pd.DataFrame(data,columns=["id","name","age"])
print(df)