#!/usr/bin/python3


def weight_average(my_list=[]):
    if not my_list:
        return 0
    numerator = denominator = 0
    for score, weight in my_list:
        numerator += score * weight
        denominator += weight
    return numerator / denominator if denominator else 0
