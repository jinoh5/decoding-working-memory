#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('cd', 'C:\\Users\\MooreLab\\spatial memory')


# In[ ]:


import numpy as np


# In[ ]:


def change_memang_to_int(clean_memang):
    unique_stimulus_position = np.unique(clean_memang)
    int_list = [0,1,2,3,4,5,6,7]
    
    # change the stimulus position to 1-8
    for seq in range(len(int_list)):
        clean_memang = np.where(clean_memang==unique_stimulus_position[seq], seq+1, clean_memang)
    pre_int_stimulus_position = clean_memang.astype(int)
    
    return unique_stimulus_position, pre_int_stimulus_position

