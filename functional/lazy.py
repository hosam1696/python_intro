# Lazy Evaluation

"""
some operations are cost

strict vs lazy
syncronous vs asyncronous
"""
#@lru_cache(maxsize=1)
# tools for lazy operations
import time
for i in range(10):
    print('{}'.format(i))
    time.sleep(1)