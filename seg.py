import ks

def findSeg(seq, probFunc):
    opt = [None for s in seq]
    p = [0. for s in seq]

    for i in range(len(seq) - 1, -1, -1):
        for j in range(i, len(seq)):
            ss = seq[i : j + 1]
            p_ss = probFunc(ss) * p[i - len(ss)]
            if p_ss > p[i]:
                p[i] = p_ss
                opt[i] = ss

    segs = [s for s in opt if s is not None]
    return segs, p[0]
