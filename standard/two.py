import asyncio
import collections as cl
nt = cl.namedtuple('Class', ('hosam', '4A'))
print(nt)

id = 0
async def get_id():
    for i in range(int(1e10)):
        id = i
    return  id


