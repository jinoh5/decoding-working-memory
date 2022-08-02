#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('cd', 'C:\\Users\\MooreLab\\spatial memory')


# In[ ]:


import numpy as np
import random
import scipy.stats as stats


# In[1]:


def preprocess_neurons_by_creating_new_index_list(pos): 
    ## Preprocessing (Making sure each stimulus position has the same number of trials for every neuron)
    ## note that we only need to look at stimulus position (pos) because the indices are the same for every neuron
    # new total index list will always change due to sampling 
    
    # 1. Find the number of trials per each stimulus position  
    indices = [np.where(pos==i) for i in range(1,9)] 
    new_indices = [list(indices[array][0]) for array in range(len(indices))]

    # 2. Find the min of trials across different stimulus position and keep track of which stimulus position has more trials
    length_comparison = [len(new_indices[element]) for element in range(len(new_indices))]
    min_value = min(length_comparison)
    working_indices = []
    for count, value in enumerate(length_comparison):
        if value > min_value:
            working_indices.append(count)

    # 3. Do the sampling among the selected stimulus position trials so that the min number of trials is selected
        # (but each trial should not be selected twice in each sampling)
    new_total_index_list = []
    for index in working_indices:
        example_list = random.sample(new_indices[index], min_value)
        new_total_index_list = example_list + new_total_index_list

    # 5. Put the selected trials back into the original correct index to create 'corresponding neurons' (maybe just check with the index that was selected after this process and discard those that are not part of the final index)
    original_indices = [i for i in range(len(new_indices))]

    missing_indicies = []
    for i in range(len(working_indices)):
        if working_indices[i] != original_indices[i]:
            missing_indicies.append(i) 
            if len(missing_indicies) == 1:
                new_total_index_list = new_indices[missing_indicies[0]] + new_total_index_list
            else:  # in case, this has to generalize 
                for k in range(len(missing_indicies)):
                    new_total_index_list = new_indices[missing_indicies[k]] + new_total_index_list
    new_total_index_list.sort()
    
    return new_total_index_list

