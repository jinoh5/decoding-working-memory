#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('cd', 'C:\\Users\\MooreLab\\spatial memory')


# In[ ]:


import numpy as np


# In[ ]:


def grab_corresponding_memang(stim_pos, index_list):
    
    # Get a vector of S.memang according to the new corresponding neurons
    new_stimulus_position = []
    for count, element in enumerate(index_list):
        for i in range(len(stim_pos)):
            if i == element:
                new_stimulus_position.append(stim_pos[i])
    
    return new_stimulus_position

