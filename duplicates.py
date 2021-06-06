import io
from collections import defaultdict

test1 = io.StringIO('''4
4 3 2 1
3''')


test2 = io.StringIO('''8
1 1 2 3 1 4 3 1
2''')


test3 = io.StringIO('''8
1 1 2 3 1 4 3 1
3''')


def get_jedi_idx(str_buffer: io.StringIO) -> int:
    next(str_buffer)
    jedi_lst = []
    jedi_fist_positions_dict = {}
    counter = defaultdict(int)
    for idx, current in enumerate(next(str_buffer).strip().split(), start=1):
        current = int(current)
        jedi_lst.append(current)
        counter[current] += 1
        if current not in jedi_fist_positions_dict:
            jedi_fist_positions_dict[current] = idx
    search_idx = int(next(str_buffer)) - 1
    modified_jedi = []
    for current in jedi_lst:
        if counter[current] == 1:
            modified_jedi.append(current)
    if search_idx < 0 or search_idx > len(modified_jedi) - 1:
        return 0
    else:
        jedi_to_enter = modified_jedi[search_idx]
        answer = jedi_fist_positions_dict[jedi_to_enter]
        return answer


assert get_jedi_idx(test1) == 3
assert get_jedi_idx(test2) == 6
assert get_jedi_idx(test3) == 0
