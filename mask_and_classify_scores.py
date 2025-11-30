import numpy as np

def mask_and_classify_scores(arr):
    
    #check if arr is numpy array
    #check if arr is 2D and square (nxn)
    #check if arr is at least 4x4
    if not isinstance(arr, np.ndarray) or arr.ndim != 2 or arr.shape[0] != arr.shape[1] or arr.shape[0] < 4:    
        #if not, return None
        return None
    
    
    #Part A, cleaning scores
    #create a copy called cleaned
    cleaned = arr.copy()
    
    #check for n<0, then change them into n=0 in cleaned
    #check for n>100, then change them into n=100 in cleaned
    cleaned[cleaned < 0] = 0
    cleaned[cleaned > 100] = 100

    
    #Part B, classifying scores
    #create a new array called levels with same shape (hint: create a placeholder array)
    #check each index in cleaned, for each <40, 40<=i<70, and >=70, 
    #set 0, 1, 2 accordingly in levels
    
    
    #Part B Alternative (might be easier?)
    #straight up copy cleaned and call it levels
    levels = cleaned.copy()
    
    #change <40 to 0, 40<=i<70 to 1 and >=70 to 2 in levels
    levels[levels < 40] = 0
    levels[(levels >= 40) & (levels < 70)] = 1
    levels[levels >= 70] = 2

    
    #Part C, count passing per row
    #create an empty array row_pass_counts, again, use placeholder array (np.zero) for the length of n
    n = arr.shape[0]
    row_pass_counts = np.zeros(n, dtype=int)
    
    #use loop to count how many i>=50 in cleaned
    for i in range(n):
        count = 0
        for value in cleaned[i]:
            if value >= 50:
                count += 1
        #assign count into row_pass_counts
        row_pass_counts[i] = count
    
    #return cleaned, levels, row_pass_counts
    return cleaned, levels, row_pass_counts
    
    
    
    
