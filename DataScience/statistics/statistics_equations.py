#!/usr/bin/python3
#!coding=utf-8

def arithmetic_mean(list_):
    """
    :param list_: insert a list of value (floats or integers)
    :return: the arithmetic mean

    formula  ->  A = 1/n * sum(list_)

    """
    n = len(list_)
    list_sum = 0
    for i in range(len(list_)):
        list_sum += list_[i]

    A = list_sum / n
    return A


def geometric_mean(list_):
    """
    :param list_: insert a list of value (floats or integers)
    :return: the geometric mean

    n=len(list) it's the grade of the root
    the product of each element of the list is the base of the root

    formula -> G = root(x1*x2*...xn, n)

    """
    product = production(list_)
    n = len(list_)
    geom_mean = root(product,n)
    return geom_mean


def root(base, index):
    """
    Return the mathematical root of index grade
    I don't use math.sqrt() because it is just for roots with index=2
    :param base: the base of the root
    :param index: the index of the root
    """
    result = base ** (1 / float(index))
    return result


def summation(list_):
    """
    :param list_: list of int or float
    :return: the sum of each element
    """
    result=0
    for i in list_:
        result+=i
    return result


def production(list_):
    """
    like summation but with the * instead of +
    """
    result = 1
    # start with 1 and not 0 because I don't want to null the production

    for i in list_:
        result = result * i
    return result


def mean_squared_error(list_):
    """
    formula ->  mse = 1/N * summation( ( X_i - X_mean )**2 )
    """
    mean = arithmetic_mean(list_)
    n = len(list_)
    list_quadratic_error=quadratic_error(list_)
    mse = 1/n * summation(list_quadratic_error)
    return mse


def quadratic_error(list_):
    """
    :param list_: list of int or float
    :return: list of quadratic error

    list of  ( X_i - X_mean) ** 2

    """
    quadratic_error_list=[]
    mean=arithmetic_mean(list_)
    for i in list_:
        quadratic_error_list.append((i-mean)**2)
    return quadratic_error_list


def standard_deviation(list_):
    """
    -> formula SD= root( (1/len(list_) * summation(quadratic_error(list_)))  )
    """
    quadratic_error_list = []
    quadratic_error_list = quadratic_error(list_)
    n = len(list_)
    sd = root(1/n * summation(quadratic_error_list), 2)
    return sd


def sample_variance(list_):
    """
    Unbiased estimator of the population variance

    :param list_: list of int or float

    -> formula SD = ( 1/len(list_-1) * summation( (X_i - X_mean)**2 )

    """
    quadratic_error_list = []
    quadratic_error_list = quadratic_error(list_)
    n = len(list_)-1
    variance = 1/n * summation(quadratic_error_list)
    return variance
