import asyncio
import time


async def do_somethine(s):
    print("运行中... {}".format(s))

    # await asyncio.sleep(s)
    await asyncio.sleep(s)

    print("haha")

def done(futu):
    print(futu)
    print("运行完了")

loop = asyncio.get_event_loop()

do1 = asyncio.ensure_future(do_somethine(1))
do2 = asyncio.ensure_future(do_somethine(2))
do3 = asyncio.ensure_future(do_somethine(3))

works = [do1, do2, do3]

do1.add_done_callback(done)
do2.add_done_callback(done)
do3.add_done_callback(done)

loop.run_until_complete(asyncio.gather(*works))


