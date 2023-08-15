from typing import List


def find_biggest_name(names: List[str]) -> str:
    # raise NotImplementedError
    bigger_name = ''
    for name in names:
        if len(name) > len(bigger_name):
            bigger_name = name
    return bigger_name
