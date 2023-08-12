import asyncio

class This:
    def __init__(self,omastek: str):
        self.omastek = omastek

def dec2(greeting, farewell):
    def dec2_decorator(func):
        def dec2_inner(*args, **kwargs):
            print(greeting)
            res = func(*args, **kwargs)
            print(farewell)
            return res
        return dec2_inner
    return dec2_decorator

def jsf(func):
    def wrapper(*args, **kwargs):
        return func(This("it works"),*args,**kwargs)
    return wrapper

def asyncexe(func):
    async def wrapper(*args,**kwargs):
        return await func(*args,**kwargs)
    return asyncio.run(wrapper())


@dec2("hi","farewell")
@jsf
def test(self):
    @asyncexe
    async def _test():
        print("before:",self.omastek)
        await asyncio.sleep(1)
        print("after:",self.omastek)


if __name__ == '__main__':
    test()


