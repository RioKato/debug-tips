import gdb

ulp = gdb.lookup_type('unsigned long').pointer()
value = gdb.parse_and_eval('0xdeadbeef')
value = value.cast(ulp)
deref = value.dereference()
print(deref)
