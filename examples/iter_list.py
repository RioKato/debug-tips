import gdb


def iter_list(value: gdb.Value):
    print(value)

    # next = value->next OR next = value.next
    next = value['next']
    if next == 0:
        return

    iter_list(next)


iter_list(gdb.parse_and_eval('list'))
