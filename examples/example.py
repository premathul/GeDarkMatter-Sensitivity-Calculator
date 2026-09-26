import numpy as np
from gedm_sensitivity.core import asimov_discovery_significance

signal=np.array([2.0,3.0,1.0])
background=np.array([10.0,12.0,8.0])
print("Asimov significance:",asimov_discovery_significance(signal,background))
