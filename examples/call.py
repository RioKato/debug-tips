import gdb

# call malloc(0x10)

malloc = gdb.parse_and_eval('malloc')
ret = malloc(0x10)
print(ret)
