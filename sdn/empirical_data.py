"""Empirical evaluation dataset from the Master's Thesis:
'Otimização Aplicada ao Problema de Engenharia de Tráfego em Redes Definidas por Software'
Author: João Paulo Versiani Ladeia (Unimontes, 2018)

Data obtained from the real SDN testbed:
Mininet + Floodlight Controller (OpenFlow) + D-ITG (Distributed Internet Traffic Generator).
Five independent experimental runs per network configuration.
"""

import pandas as pd
import numpy as np

# Per-application results (Quadro 6 and Quadro 7 from dissertation)
APPLICATIONS_DATA = [
    # app_id, type, orig, dest, target_thr_kbps, opt_thr_kbps, dj_thr_kbps, opt_loss_pct, dj_loss_pct, target_delay_s, opt_delay_s, dj_delay_s, opt_jitter_s, dj_jitter_s
    [1,  'Data',  0,  49, 256.0,  250.31, 222.56, 0.0000, 0.00,   1.000, 0.0539,  5.4526, 0.0154, 0.0292],
    [2,  'Data',  1,  33, 256.0,  250.37, 251.86, 0.0000, 0.00,   1.000, 0.0537,  0.0427, 0.0154, 0.0167],
    [3,  'Video', 2,  51, 1744.0, 1405.01, 1440.20, 0.0000, 0.00, 0.150, 0.0546,  0.0644, 0.0012, 0.0012],
    [4,  'Video', 3,  50, 1256.0, 1072.53, 822.81,  0.0000, 0.00, 0.150, 0.1354,  7.1648, 0.0049, 0.0085],
    [5,  'Data',  4,  37, 256.0,  250.33, 251.77, 0.0000, 0.00,   1.000, 0.2057,  0.1021, 0.0205, 0.0196],
    [6,  'Data',  31, 36, 256.0,  250.25, 251.87, 0.0000, 0.00,   1.000, 0.1354,  0.1544, 0.0209, 0.0204],
    [7,  'Data',  32, 46, 256.0,  250.18, 251.83, 0.0000, 0.00,   1.000, 0.0881,  0.1040, 0.0031, 0.0017],
    [8,  'Voice', 5,  48, 512.0,  482.21, 465.14, 0.0000, 3.38,   0.150, 0.0345,  3.5509, 0.0019, 0.0049],
    [9,  'Voice', 6,  47, 512.0,  482.73, 401.26, 0.0000, 0.00,   0.150, 0.1128,  5.7557, 0.0107, 0.0164],
    [10, 'Data',  7,  34, 256.0,  249.85, 251.88, 0.1054, 0.00,   1.000, 0.5306,  0.1244, 0.0038, 0.0019],
    [11, 'Video', 8,  44, 1256.0, 1066.53, 688.52, 0.0865, 36.63, 0.150, 0.4724,  4.4476, 0.0021, 0.0017],
    [12, 'Video', 9,  43, 1256.0, 1070.25, 707.21, 0.0000, 34.44, 0.150, 0.1534,  4.4079, 0.0023, 0.0018],
    [13, 'Voice', 11, 41, 512.0,  482.45, 306.19, 0.0000, 36.26, 0.150, 0.0747,  4.3821, 0.0019, 0.0024],
    [14, 'Data',  10, 42, 256.0,  249.66, 10.71,  0.0000, 0.07,   1.000, 0.6078, 61.7454, 0.0206, 0.6113],
    [15, 'Voice', 12, 40, 512.0,  482.15, 21.31,  0.0000, 0.00,   0.150, 0.1876, 49.9390, 0.0107, 0.2819],
    [16, 'Data',  13, 39, 256.0,  249.55, 161.43, 0.0935, 34.97,  1.000, 0.4927,  4.2379, 0.0032, 0.0027],
    [17, 'Data',  30, 45, 256.0,  250.28, 34.38,  0.0000, 0.02,   1.000, 0.1652,  1.7584, 0.0049, 0.0076],
]

COLUMNS = [
    'app_id', 'type', 'orig', 'dest', 'target_thr_kbps',
    'opt_thr_kbps', 'dj_thr_kbps', 'opt_loss_pct', 'dj_loss_pct',
    'target_delay_s', 'opt_delay_s', 'dj_delay_s',
    'opt_jitter_s', 'dj_jitter_s'
]

def get_empirical_dataframe():
    return pd.DataFrame(APPLICATIONS_DATA, columns=COLUMNS)

SUMMARY_TABLE_14 = {
    'metric': [
        'Average Throughput (kbps)',
        'Average End-to-End Delay (s)',
        'Average Jitter (s)',
        'Packet Loss Ratio (%)'
    ],
    'optimized': [517.3307, 0.2109, 0.0093, 0.0168],
    'dijkstra': [384.7603, 10.7962, 0.0697, 8.5747],
    'gain': [
        '+34.45%',
        '51.19x lower',
        '7.49x lower',
        '510.4x lower'
    ]
}

def get_summary_dataframe():
    return pd.DataFrame(SUMMARY_TABLE_14)
