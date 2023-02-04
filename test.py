import pandas as pd
Education= [['B.Tech','CSE','2017','ICET','7.09 CGPA'],['12th','Electronics','2013','THSS-Muttom', '78%'],['10th','CBSE','2011','Vimala Public School','78%']]
df = pd.DataFrame(Education, columns=['Institution', 'Stream','Year','Institution','%Passing'])
print(df)