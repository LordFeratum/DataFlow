from itertools import tee


async def async_map(transform, data):
    res = []
    for datum in data:
        res.append(await transform(datum))

    return res


async def async_filter(fnx, data):
    res = []
    for datum in data:
        if await fnx(datum):
            res.append(datum)

    return res


async def async_reduce(fnx, data, start):
    acc = start
    for datum in data:
        acc = await fnx(acc, datum)
    return acc


async def async_dropwhile(fnx, data):
    data, data_copy = tee(data)
    idx = 0
    for datum in data_copy:
        if not await fnx(datum):
            break
        idx += 1

    res = []
    for _idx, datum in enumerate(data):
        if _idx <= idx:
            continue

        res.append(datum)

    return res


async def async_takewhile(fnx, data):
    res = []
    for datum in data:
        if await fnx(datum):
            res.append(datum)
        else:
            break

    return res
