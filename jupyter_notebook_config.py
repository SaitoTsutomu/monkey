c = get_config()
c.InteractiveShellApp.exec_lines = [
    'from MonkeyBench import *',
    'import pandas as pd, numpy as np, matplotlib.pyplot as plt',
    'plt.rcParams["font.family"] = "IPAexGothic"',
]
