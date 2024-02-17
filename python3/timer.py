from time import time

start = time()

for x in range(100000000):
    continue

end = time()

elapsed = end - start

print('Total time to run: {0:.2f} seconds\n'.format(elapsed))