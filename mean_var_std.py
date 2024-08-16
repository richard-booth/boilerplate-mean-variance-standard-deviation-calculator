import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    #reshape list as a 3 x 3 matrix
    mat = np.array(list).reshape(3,3)

    #initialize dictionary to be returned
    calculations = {}

    #add values to dictionary:
    
    #mean
    calculations['mean'] = [mat.mean(axis=0).tolist(), mat.mean(axis=1).tolist(), mat.mean()]

    #variance
    calculations['variance'] = [np.var(mat,axis=0).tolist(), np.var(mat,axis=1).tolist(), np.var(mat)]
    
    #standard deviation
    calculations['standard deviation'] = [mat.std(axis=0).tolist(), mat.std(axis=1).tolist(), mat.std()]
    
    #maxima
    calculations['max'] = [mat.max(axis=0).tolist(), mat.max(axis=1).tolist(), mat.max()]
    
    #minima
    calculations['min'] = [mat.min(axis=0).tolist(), mat.min(axis=1).tolist(), mat.min()]
    
    #sums
    calculations['sum'] = [mat.sum(axis=0).tolist(), mat.sum(axis=1).tolist(), mat.sum()]

    return calculations
