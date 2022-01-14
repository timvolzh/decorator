from decorator import log_decorator_with_path

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None]
]


@log_decorator_with_path('Log.txt')
def flat_generator(list):
    cursor = 0
    inner_cursor = 0
    while len(list) != cursor and len(list[cursor]) != inner_cursor:
        yield list[cursor][inner_cursor]
        inner_cursor += 1
        if len(list[cursor]) == inner_cursor:
            cursor += 1
            inner_cursor = 0


for item in flat_generator(nested_list):
    print(item)
