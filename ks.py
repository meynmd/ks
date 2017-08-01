from math import *

MajorKeyProfile = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88]
MinorKeyProfile = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17]
MajorKeyAvg = float(sum(MajorKeyProfile)) / len(MajorKeyProfile)
MinorKeyAvg = float(sum(MinorKeyProfile)) / len(MinorKeyProfile)

"""
KS Key Profile evaluation function

in:
    pitchClassDurations     list    indexed by pitch class, where C -> 0, etc.
                                    values: total duration of each pitch class
                            
    testKey                 int     hypothetical key for which to find KS score
    
    isMajor                 bool    major -> True, minor -> False
    
out:
    score                   float   KS score for this key
"""
def score(pitchClassDurations, testKey, isMajor):
    # define xs and ys
    x = pitchClassDurations
    x_avg = float(sum(pitchClassDurations)) / len(pitchClassDurations)
    if isMajor:
        y = MajorKeyProfile
        y_avg = MajorKeyAvg
    else:
        y = MinorKeyProfile
        y_avg = MinorKeyAvg

    # do the summations
    sum_xy, sum_difx2, sum_dify2 = 0., 0., 0.
    for k in range(len(pitchClassDurations)):
        i = (k - testKey + 12) % 12
        sum_xy += (x[k] - x_avg) * (y[i] - y_avg)
        sum_difx2 += (x[k] - x_avg)**2
        sum_dify2 += (y[i] - y_avg)**2

    return sum_xy / sqrt(sum_difx2 * sum_dify2)
