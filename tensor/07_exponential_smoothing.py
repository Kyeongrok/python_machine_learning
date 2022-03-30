
def exponential_smoothing(lst_actual_v, lst_forcast_v, alpha):
    return alpha * lst_actual_v + (1-alpha) * lst_forcast_v

def es(lav, lfv, a):
    return a * lav + (1-a) * lfv