import numpy as np
from scipy.stats import entropy

def kl_divergence(target_list,reference_list):
  target_list=target_list/np.sum(target_list)
  reference_list=reference_list/np.sum(reference_list)
  return entropy(target_list,reference_list)
    

def place_holder(input_list):
    '''Returns the place holder (?, ?, .....) as string'''
    return f"({', '.join('?' * len(input_list))})"

def confidence_interval(m,N,delta):
    return np.sqrt((1/(2*m))*((1-(m-1)/N)*(2*np.log(np.log(m))+np.log(((np.pi)*(np.pi))/(3*delta)))))

def reset_index(tables):
    for i,table in enumerate(tables):
        tables[i]=table.reset_index(drop=True)
    return tables