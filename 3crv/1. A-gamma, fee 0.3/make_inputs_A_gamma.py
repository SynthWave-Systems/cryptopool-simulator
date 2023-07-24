import numpy as np
from math import log10
import json
import itertools
from copy import copy


X = np.logspace(log10(0.5), log10(500), 32)
Xname = "A"
Y = np.logspace(log10(1e-7), log10(1e-3), 32)
Yname = "gamma"

other_params = dict(
    D=50e6,
    adjustment_step=1e-7,
    fee_gamma=0.006,
    ma_half_time=600,
    mid_fee=0.003,
    out_fee=0.003,
    gas_fee=10,
    n=3,
    log=0,
    allowed_extra_profit=1e-10,
    ext_fee=0.001,
    gamma=1e-5,
    A=6.3)

config = {
    'configuration': [],
    'datafile': [
        "3crv-ethusdt-1m",
        "3crv-crvusdt-1m",
        "3crv-crveth-1m"],
    'debug': 0}

for x, y in itertools.product(X, Y):
    params = copy(other_params)
    params[Xname] = x
    params[Yname] = y
    config['configuration'].append(params)

with open('configuration.json', 'w') as f:
    json.dump(config, f)
