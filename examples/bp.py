import gdb


class BP(gdb.Breakpoint):
    def __init__(self):
        super().__init__('*0xdeadbeef')

    def stop(self):
        i = gdb.parse_and_eval('i')
        if i == 0x10:
            return True
        else:
            return False


bp = BP()
