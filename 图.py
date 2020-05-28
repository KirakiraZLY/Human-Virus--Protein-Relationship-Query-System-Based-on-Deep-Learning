#from pyecharts.charts import Bar
import xlrd
from wordcloud import WordCloud
#from scipy.misc import imread
import numpy as np
from PIL import Image
data = xlrd.open_workbook('VTP-PTV.xlsx')

table = data.sheets()[0]
table1 = data.sheets()[1]
#print(table.nrows)
for i in range(0, 33):
    name = table1.row_values(i)[0]
    print('{')
    print('name: ' + "'" + name + "'" + ',')
    print('des: ' + "'" + name + "'" + ',')
    print('symbolSize: 20,')
    print('category: 0,')
    print('},')

for i in range(0, 43):
    name = table1.row_values(i)[1]
    print('{')
    print('name: ' + "'" + name + "'" + ',')
    print('des: ' + "'" + name + "'" + ',')
    print('symbolSize: 30,')
    print('category: 1,')
    print('},')

for i in range(0, 19):   #包含头不含尾
  # print(table.row_values(i))
    name = table.row_values(i)[2]
    print('{')
    print('source: ' + "'" + name + "'" + ',')
    name1 = table.row_values(i)[1]
    print('target: ' + "'" + name1 + "'" + ',')
    name2 = table.row_values(i)[3]
    print('des: ' + "'" + name2 + "'" + ',')
    print('},')
for i in range(19, 63):   #包含头不含尾
  # print(table.row_values(i))
    name = table.row_values(i)[1]
    print('{')
    print('source:' + "'" + name + "'" + ',')
    name1 = table.row_values(i)[2]
    print('target:' + "'" + name1 + "'" + ',')
    name2 = table.row_values(i)[3]
    print('des:' + "'" + name2 + "'" + ',')
    print('},')

#柱状图
#bar = Bar()
#bar.add_xaxis(names)
#bar.add_yaxis('次数',times)
#bar.render('高频词可视化展示.html')

#词云图
