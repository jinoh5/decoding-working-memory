#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('cd', 'C:\\Users\\MooreLab\\spatial memory')


# In[ ]:


import numpy as np


# In[ ]:


def change_int_pos_to_float_memang(post_int_stimulus_position, float_stim_pos):
    int_stim_pos = np.unique(post_int_stimulus_position)
    
    # Create a dict that is comprised of both integer stimulus position and original float stimulus position 
    Dict = {int_stim_pos[0]: float_stim_pos[0], 
            int_stim_pos[1]: float_stim_pos[1], 
           int_stim_pos[2]: float_stim_pos[2], 
           int_stim_pos[3]: float_stim_pos[3], 
           int_stim_pos[4]: float_stim_pos[4], 
           int_stim_pos[5]: float_stim_pos[5], 
           int_stim_pos[6]: float_stim_pos[6], 
           int_stim_pos[7]: float_stim_pos[7]}
    stim_pos_to_float = []
    
    # Find the corresponding integer stimulus position and change to float stimulus position
    for index in range(len(post_int_stimulus_position)):
        for key, value in Dict.items():
            if post_int_stimulus_position[index] == key:
                stim_pos_to_float.append(value)
    return stim_pos_to_float

