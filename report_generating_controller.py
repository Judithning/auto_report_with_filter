
# coding: utf-8

# In[3]:


import sys
import os
import datetime

#variable=sys.argv
path=os.getcwd()
def controller(argu):
    '''
    argu=''
    for x in variable:
        l = ' '+x
        argu+=l
    '''
    #argu = 'filename.py 10.1.1.202:3306-TEST VC,TR S,10.1.1.32, 10.1.1.40 2018-11-01,2018-11-23'
    with open(path+'\\'+'sys_para.txt','w') as f:
        f.write(argu)
    time_now = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y.%m.%d')
    os.system('jupyter nbconvert --execute generate_reports_with_filtering_V1.ipynb')
    #os.rename('generate reports with filtering-v1.html','数据指标自动生成报告'+'time_now'+'.html')


# In[4]:


path


# In[17]:


controller(sys.argv[1])


# In[11]:


'''
import os
import pandas as pd
import datetime
import os.path as osp
import sys


env=os.environ
env['IPYTHONARGV'] = '10.1.1.202:3306-TEST VC,TR S,10.1.1.32, 10.1.1.40 2018-11-01,2018-11-23'#sys.argv[1:]
file='generate reports with filtering-v1.ipynb'
os.execlpe('jupyter','jupyter','nbconvert','--execute',file,env)
time_now = (datetime.datetime.now()-datetime.timedelta(days=1)).strftime('%Y.%m.%d')
#argu = ' 10.1.1.202:3306-TEST VC,TR S,10.1.1.32, 10.1.1.40 2018-11-01,2018-11-23'
#os.system('jupyter nbconvert --execute generate reports with filtering-v1.ipynb')#+argu)
os.rename('generate reports with filtering-v1.html','数据指标自动生成报告'+'time_now'+'.html')
''';

