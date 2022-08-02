#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('cd', 'C:\\Users\\MooreLab\\spatial memory')


# In[ ]:


import numpy as np
import pandas as pd
import scipy.io


# In[ ]:


def grab_data(filename):
    ## 1. Grab trials, timepoints, cells 
    mat = scipy.io.loadmat(filename)
    neurons = mat.get("cells")
    total_neurons = np.zeros((len(neurons['cellNo'][0]),len(neurons['FR'][0][0]),len(neurons['FR'][0][0][0,:]))) #change to generalize (135, 1287, 200)
    for i in range(len(neurons['FR'][0][0])):               #number of trials - 1287
        for j in range(len(neurons['FR'][0][0][0,:])):      #number of timepoints - 200
            for d in range(len(neurons['cellNo'][0])):      #number of cells - 135
                total_neurons[d,i,j]=neurons['FR'][0][d][i,j]
    
    ## 2. From 'S', grab block_cond and experiment result 
    S = mat.get("S")
    
    block_cond = []
    for index in range(len(S['esetup_block_cond'][0][0])):
        block_cond.append(S['esetup_block_cond'][0][0][index][0][0])
    
    exp_result = []
    for index in range(len(S['edata_error_code'][0][0])):
        exp_result.append(S['edata_error_code'][0][0][index][0][0])
    
    # Combine block_cond (different tasks) and result ('correct or incorrect') together
    task_and_result = np.vstack((block_cond, exp_result))
    
    ## 3. Grab S.memang (circular stimulus positions)
    memang=S['memang'][0][0]
    
    return total_neurons, task_and_result, memang

