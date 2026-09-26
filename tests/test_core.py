import numpy as np
from gedm_sensitivity.core import asimov_discovery_significance, scale_counts
from gedm_sensitivity.scan import signal_strength_scan

def test_zero_signal_zero_significance():
    assert np.isclose(asimov_discovery_significance([0,0],[10,10]),0)

def test_scaling():
    assert np.allclose(scale_counts([1,2],2.0,0.5),[1,2])

def test_scan_recovers_asimov_strength():
    s=np.array([2.,1.]); b=np.array([10.,10.]); n=b+s
    r=signal_strength_scan(n,s,b,np.linspace(0,2,101))
    assert abs(r["best_mu"]-1.0)<0.05
