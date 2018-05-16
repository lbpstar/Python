import asyncio

@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    yield from asyncio.sleep(5)
    print("Hello again!")
    yield from asyncio.sleep(5)
    print("Hello 3!")
# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()