import numpy as np

def poisson_log_likelihood(observed, expected):
    n=np.asarray(observed,float)
    mu=np.asarray(expected,float)
    if n.shape!=mu.shape or np.any(n<0) or np.any(mu<=0):
        raise ValueError("invalid Poisson inputs")
    return float(np.sum(n*np.log(mu)-mu))

def asimov_discovery_significance(signal, background):
    s=np.asarray(signal,float); b=np.asarray(background,float)
    if s.shape!=b.shape or np.any(s<0) or np.any(b<=0):
        raise ValueError("invalid signal/background")
    q=2*np.sum((s+b)*np.log1p(s/b)-s)
    return float(np.sqrt(max(q,0.0)))

def gaussian_background_significance(signal, background):
    s=np.asarray(signal,float); b=np.asarray(background,float)
    if s.shape!=b.shape or np.any(s<0) or np.any(b<=0):
        raise ValueError("invalid signal/background")
    return float(np.sum(s)/np.sqrt(np.sum(b)))

def scale_counts(reference_counts, exposure_scale=1.0, efficiency=1.0):
    x=np.asarray(reference_counts,float)
    e=np.asarray(efficiency,float)
    if exposure_scale<0 or np.any((e<0)|(e>1)):
        raise ValueError("invalid exposure scale or efficiency")
    return x*exposure_scale*e
