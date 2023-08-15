"""
deque의 `maxlen` 키워드인자를 사용하여 크기를 유지한 채 자동으로 push back과 pop front를 이루어지게 만들었다. 

`islice`는 이터레이터를 위한 슬라이싱 함수로, 굳이 리스트가 아니어도 순회 가능한 모든 객체를 슬라이싱 할 수 있다는 개쩌는 장점이 있다. 아쉽게도 음수 인덱싱은 안된다.

아래 코드는 itertools-recipes의 코드를 훔쳐온 것이다. 머리 속에 넣어놓고 필요할 때 꺼내어 써먹자.
"""
import collections
from itertools import islice


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


"""
만약 이터레이터를 쓰지 않고 당장 리스트를 가지고 슬라이딩을 하고 싶다면 반복문과 슬라이싱 문법을 활용하면 된다.
"""


def sliding_window_list(ls, n):
    for i in range(len(ls) - n + 1):
        yield ls[i : i + n]
