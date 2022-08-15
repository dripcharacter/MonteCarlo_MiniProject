import math
import random

simple_sampling_list=list()
importance_sampling_list=list()

def sigma_func(radius):
    return 1 / math.sqrt(1 - radius)
# p(r)=1/sqrt(1-r^2)에 대한 importance_sampling이다
def importance_sampling(sample_num):
    sample_list=list()
    sampled_num=0
    while sampled_num < sample_num:
        r_num_from_uniform=random.uniform(0, 1)
        r_num_from_inverse_cdf=1-(r_num_from_uniform-1)**2
        r_num_result=random.uniform(0, r_num_from_inverse_cdf)
        if r_num_result <= 1 / (math.sqrt(1-r_num_from_uniform**2)*math.asin(1)):
            print("Success: Since", r_num_result, "is smaller than", 1 / (math.sqrt(1-r_num_from_uniform**2)*math.asin(1)))
            sample_list.append(r_num_result)
            sampled_num+=1
        else:
            print("Failure: Since", r_num_result, "is bigger than", 1 / math.sqrt(1 - r_num_from_uniform ** 2))
    return sample_list

def simple_method(sample_num):
    for i in range(sample_num):
        radius = random.uniform(0, 1)
        simple_sampling_list.append(sigma_func(radius))
    simple_mean=sum(simple_sampling_list)/len(simple_sampling_list)
    simple_variance=0
    for sample in simple_sampling_list:
        simple_variance+=(sample-simple_mean)**2
    simple_variance/=len(simple_sampling_list)
    return simple_mean, simple_variance

def importance_method(sample_num):
    sample_list=importance_sampling(sample_num)
    for sample in sample_list:
        importance_sampling_list.append((math.sqrt(1-sample**2)*(math.asin(1))**2)/(2*(1-sample)))
    importance_mean=sum(importance_sampling_list)/len(importance_sampling_list)
    importance_variance=0
    for sample in importance_sampling_list:
        importance_variance+=(sample-importance_mean)**2
    importance_variance/=len(importance_sampling_list)
    return importance_mean, importance_variance


importance_mean, importance_variance=importance_method(100000)
print("importance_mean:", importance_mean, "importance_variance:", importance_variance)
simple_mean, simple_variance=simple_method(100000)
print("simple_mean:", simple_mean, "simple_variance:", simple_variance)