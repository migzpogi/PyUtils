# Demo usage of TQDM
# More here: https://pypi.python.org/pypi/tqdm/4.19.5

import random
import time
from tqdm import tqdm

# Normal iteration
for i in range(0, 5):
    print i
    wait = random.randrange(0,5)
    time.sleep(wait)

# Iteration with TQDM
for i in tqdm(range(0,5)):
    wait = random.randrange(0,5)
    time.sleep(wait)

