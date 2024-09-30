from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

maximum = 75000
# Test ft_tqdm
for elem in ft_tqdm(range(maximum)):
    sleep(0.005)
print()

# Test tqdm
for elem in tqdm(range(maximum)):
    sleep(0.005)
print()