
# coding: utf-8

# In[1]:

def factorial(minimum,maximum):
    #Because we are mutliplying you need to set this value to 1
    total=1
    #for every value in some range.....
    for n in range(minimum,maximum+1):
        #....take the "total" that you started with and multiply this times the maximum value and each 
        #value below that maximum until you reach the minimum value.
        #Remember that the maximum is exclusive, so you need to add one to this. 
        total=total*n
    return total



# In[2]:

#Test your function with some random numbers 
eight_factorial=factorial(6,8)
print(eight_factorial)


# In[3]:

#Calculate the bionomial coeffecient based on the equations given in class. 
def bionom_coeff(number_trials_n,successes_k):
    #Use the factorial function from above to calculate the top and bottom of the equation usnig the number of trials as the max
    #and the number of successes k as the minimum.
    top=factorial(1,number_trials_n)
    bottom=(factorial(1,number_trials_n-successes_k)*(factorial(1,successes_k)))
    #divide the top by the bottom to complete the equation
    coeff = top/bottom
    return coeff


# In[4]:

five_choose_2=bionom_coeff(5,2)
print(five_choose_2)


# In[5]:

def bionom_coeff_easy(number_trials_n,successes_k):
    bi_co_n=1
    for n in range (number_trials_n,number_trials_n-successes_k+1,-1):
        bi_co_n=bi_co_n*n
    bi_co_k=1
    for k in range(successes_k,0,-1):
        bi_co_k=bi_co_k*k
    bi_co_nk=(bi_co_n)/(bi_co_k)
    return bi_co_nk


# In[6]:

eleven_choose_3=bionom_coeff(11,3)
print(eleven_choose_3)


# In[7]:

#Calculate the entire PMF using this equation, plus the function used to calculate the binomial coefficient above.
def binom_PMF(number_trials_n,successes_k,probability):
    bi_co=bionom_coeff(number_trials_n,successes_k)
    prob_success=pow(probability,successes_k)
    prob_no_success=pow(1-probability,number_trials_n-successes_k)
    bi_co_pmf=bi_co*prob_success*prob_no_success
    return bi_co_pmf


# In[8]:

five_choose_2_probability_zero_point_three=binom_PMF(5,2,0.5)
print(five_choose_2_probability_zero_point_three)


# In[9]:

import random
def arb_disc_distrib_sample(events,p_vals):
    #For each value in a list of events, choose one of them randomly.
    for character in events:
        random_choice=random.choice(events)
        #For each of the randomly chosen events, you need to link it to a p-value. 
        for choice in random_choice:
            p_values=(p_vals[events.index(choice)])
    #Return the associated p-value
    return p_values

random_events=['a','b','c','d']
random_values=['0.2','0.1','0.3','0.4']
pick_an_event=arb_disc_distrib_sample(random_events,random_values)
print(pick_an_event)


# In[10]:

#Based upon the psuedo code provided...
def climbTheHill(probability,successes_k,number_trials_n):
    # pick starting p
    pCurr=probability 
    # set starting diff (make it coarse to start - maybe 0.1)
    diff=0.1
    # Let's keep trying to find a better solution until our diff is sufficiently small
    while (diff>0.001):
        #Calculate the likelihood for the current probability, and then for
        #a point higher and lower than that probability by diff
        pCurrLike=binom_PMF(number_trials_n,successes_k,pCurr)
        pRightLike=binom_PMF(number_trials_n,successes_k,pCurr+diff)
        pLeftLike=binom_PMF(number_trials_n,successes_k,pCurr-diff)
        while (pRightLike>pCurrLike):
            #If the likelihood to the right of the current one is higher,
            #update the current probability, and then change the current likelihood as well as the 
            #points that are to the right and left of that 
            pCurr=pCurr+diff
            pCurrLike=binom_PMF(number_trials_n,successes_k,pCurr)
            pRightLike=binom_PMF(number_trials_n,successes_k,pCurr+diff)
            pLeftLike=binom_PMF(number_trials_n,successes_k,pCurr-diff)
        while (pLeftLike>pCurrLike):
            #If the likelihood to the left of the current one is higher,
            #update the current probability, and then change the current likelihood as well as the 
            #points that are to the right and left of that 
            pCurr=pCurr-diff
            pCurrLike=binom_PMF(number_trials_n,successes_k,pCurr)
            pRightLike=binom_PMF(number_trials_n,successes_k,pCurr+diff)
            pLeftLike=binom_PMF(number_trials_n,successes_k,pCurr-diff)
        diff=diff*0.5
    return pCurr
    
hill=climbTheHill(0.3,4,20)
print(hill)


# In[11]:

import random
def LRCut(probability,number_trials_n,successes_k,simulations):
    #Choose a chosen number of successes randomly and store in a list  
    random_choice_k=[random.randint(1,number_trials_n) for x in range (simulations+1)]
    #I will need this variable later, but I will fill it later in a loop
    max_likelihoods=[]
    #I will need this variable later, but I will fill it later in a loop
    LR_ratio=[]
    #I will need this variable later, but I will fill it later in a loop
    LR_ratio_top=[]
    #For each randomly chosen number of successes....
    for character in random_choice_k:
        if number_trials_n==character:
            #Otherwise you get a weird error....
            max_likelihoods.append(1)
        elif character==0:
            #Otherwise you get a weird error....
            max_likelihoods.append(0)
        else:
            #....calculate the likelihood based on the "climb the hill" function previously generated
            max_likelihoods.append(climbTheHill(probability,character,number_trials_n))
    for m in range(0,simulations+1):
        #Calculate the likelihood ratio of the calculated likelihoods versus the current p-value
        LR_ratio.append(binom_PMF(number_trials_n,random_choice_k[m],max_likelihoods[m])/(binom_PMF(number_trials_n,random_choice_k[m],probability)))
        #Sort the list from lowest to highest
        LR_ratio.sort()
        #Return the top 5% of the LR ratios 
        LR_ratio_top=LR_ratio[int(0.95*simulations):simulations+1]
    return LR_ratio_top
random_n=LRCut(0.7,20,5,100)
print(random_n)
        

