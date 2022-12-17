#!/usr/bin/python3
#!coding=utf-8

# NORMALIZATION METHODS

from statistical_tools import *

import math

def normalize_m1(list_):
    """ Y' = (list_[i] - Min) / (Max - Min) """
    normalized_list=[]
    Max = max(list_)
    Min = min(list_)
    for i in list_:
        normalized_list.append( (i - Min) / (Max - Min) )
    return normalized_list


def normalize_m2(list_):
    """ Y' = (list_[i] - mu) / sd """
    normalized_list=[]
    mu = arithmetic_mean(list_)
    sd = standard_deviation(list_)
    for i in list_:
        normalized_list.append( (i - mu ) / sd )
    return normalized_list

def normalize_m3(list_):
    """ Y' = (list_[i] - mu) / variance """
    normalized_list=[]
    mu = arithmetic_mean(list_)
    var = sample_variance(list_)
    for i in list_:
        normalized_list.append( (i - mu ) / var )
    return normalized_list

def normalize_m4(list_):
    """ Y' = (list_[i] - mean) / (Max - Min) """
    normalized_list=[]
    Max = max(list_)
    Min = min(list_)
    mu=arithmetic_mean(list_)
    for i in list_:
        normalized_list.append( (i - mu ) / (Max - Min) )
    return normalized_list

def normalize_m5(list_):
    """ Y' = ( 1 / (1 + e**(-i)) ) """
    normalized_list=[]
    e = 2.71828
    Min = min(list_)
    for i in list_:
        normalized_list.append( 1 / (1 + e**(-i)) )
    return normalized_list

def normalize_m6(list_):
    """ Y' = ( 1 / (1 + e**(-i)) ) """
    normalized_list=[]
    e = 2.71828
    for i in list_:
        normalized_list.append( math.log(i,e) / (1 - math.log(i,e) ))
    return normalized_list
