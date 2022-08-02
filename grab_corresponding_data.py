#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[ ]:

# Using the index list, let's grab neurons from the total neurons (transformed into python)
def grab_corresponding_data(total_neurons, index_list):
    
    corresponding_neurons = np.zeros((total_neurons.shape[0], len(index_list), total_neurons.shape[2]))
    placeholder = np.zeros((len(index_list), total_neurons.shape[2]))

    for neuron_num in range(total_neurons.shape[0]):
        for index, trial_num in enumerate(index_list):
            placeholder[index,:] = total_neurons[neuron_num, trial_num, :]
            corresponding_neurons[neuron_num,:,:] = placeholder

    return corresponding_neurons


# In[ ]:

# Using the final total index list, let's grab corresponding data from total neurons
def grab_new_corresponding_data(total_neurons, corresponding_neurons, new_total_index_list):
    new_corresponding_neurons = np.zeros((total_neurons.shape[0], len(new_total_index_list), total_neurons.shape[2]))
    placeholder = np.zeros((len(new_total_index_list), total_neurons.shape[2]))

    for neuron_num in range(total_neurons.shape[0]):
        for index, trial_num in enumerate(new_total_index_list):
            placeholder[index,:] = corresponding_neurons[neuron_num, trial_num, :]
            new_corresponding_neurons[neuron_num,:,:] = placeholder
    return new_corresponding_neurons 

