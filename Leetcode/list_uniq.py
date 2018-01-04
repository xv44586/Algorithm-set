"""
__author__ = 'xumingming'
"""


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


if __name__ == '__main__':
    t = [1, 9, 4, 9, 0, 8, 7]
    a = [{'x': 1, 'y': 4}, {'x' : 2, 'y': 2}, {'x':3, 'y':2}]
    print(list(dedupe(t)))
    print(list(dedupe(a, key=lambda x: (x['x'], x['y']))))
