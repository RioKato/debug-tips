import gdb

rax = gdb.selected_frame().read_register('rax')
print(rax)
