import numpy as np
from .core import poisson_log_likelihood

def signal_strength_scan(observed, signal_template, background, mu_grid):
    n=np.asarray(observed,float)
    s=np.asarray(signal_template,float)
    b=np.asarray(background,float)
    mus=np.asarray(mu_grid,float)
    if n.shape!=s.shape or n.shape!=b.shape:
        raise ValueError("shape mismatch")
    if np.any(mus<0):
        raise ValueError("signal strengths must be nonnegative")
    ll=[]
    for mu in mus:
        expected=b+mu*s
        if np.any(expected<=0):
            ll.append(-np.inf)
        else:
            ll.append(poisson_log_likelihood(n,expected))
    ll=np.asarray(ll)
    best=int(np.argmax(ll))
    return {"mu_grid":mus,"log_likelihood":ll,"best_mu":float(mus[best]),"best_log_likelihood":float(ll[best])}

def delta_log_likelihood(scan_result):
    ll=np.asarray(scan_result["log_likelihood"],float)
    return ll-np.max(ll)
