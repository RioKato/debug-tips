import gdb

# dprintf malloc, "%d", $rdi
# dprintf *(malloc+0x100), "%d", $rax


class MallocFinishTrace(gdb.FinishBreakpoint):
    def stop(self):
        rax = gdb.selected_frame().read_register('rax')
        print(rax)
        return False


class MallocTrace(gdb.Breakpoint):
    def __init__(self):
        self.fb = None
        super().__init__('malloc')

    def stop(self):
        rdi = gdb.selected_frame().read_register('rdi')
        print(rdi)
        MallocFinishTrace()
        return False


mt = MallocTrace()
