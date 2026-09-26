"""Poisson counting sensitivity for a user-supplied signal template; no halo model."""
import argparse
import math

def poisson_cdf(k, mean):
    if k < 0 or mean < 0: raise ValueError("Nonnegative counts and mean required")
    if mean == 0: return 1.
    # Stable recurrence starting from the term at k, descending.
    term = math.exp(-mean + k*math.log(mean) - math.lgamma(k+1))
    total = term
    for j in range(k,0,-1):
        term *= j/mean
        total += term
    return min(1.,total)

def upper_signal(observed, background, alpha=0.1):
    if observed < 0 or background < 0 or not 0 < alpha < 1:
        raise ValueError("Invalid count, background or tail probability")
    lo,hi=0.,1.
    while poisson_cdf(observed,background+hi)>alpha: hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if poisson_cdf(observed,background+mid)>alpha: lo=mid
        else: hi=mid
    return (lo+hi)/2

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--observed",type=int,default=0)
    p.add_argument("--background",type=float,default=0.)
    p.add_argument("--exposure-kg-day",type=float,default=100.)
    p.add_argument("--efficiency",type=float,default=0.8)
    args=p.parse_args()
    if args.exposure_kg_day <= 0 or not 0 < args.efficiency <= 1: raise ValueError("Invalid exposure/efficiency")
    s=upper_signal(args.observed,args.background)
    print(f"signal_upper_counts_90={s:.8g}")
    print(f"rate_upper_counts_per_kg_day_90={s/(args.exposure_kg_day*args.efficiency):.8g}")
    print("Method: P(N <= observed | background + signal_upper) = 0.1.")
if __name__=="__main__": main()
