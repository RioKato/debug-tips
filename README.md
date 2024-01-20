# debug-tips

## gdb

- `set $var=val`
- `pipe gdb_command | less`
- `pipe gdb_command | tee output.txt`
- `!less output.txt`
- `call malloc(size)`
- `call free(addr)`
- `call getchar()`
- `dprintf addr, "format", args`
- `break addr if cond commands ... end`
- `python command`
- `python ... end`
- `add-symbol-file a.o`
- `ptype /o type`
- `dump binary memory dump.bin start end`
- `info threads`
- `thread number`
- `record`
- `record stop`
- `rn`
- `rs`
- `watch *(char [SIZE]*)ADDRESS`
- `rwatch ...`
- `awatch ...`
- `edit`
- `p $fs_base`
- `ignore bpnum count`
- `save breakpoints example.gdb`

## gcc

- `gcc -g -fno-eliminate-unused-debug-types -x c -c -o types.h`
- `gcc -Og -fno-inline -g -o out src.c`

## execution

- `echo 0 | sudo tee /proc/sys/kernel/randomize_va_space`
- `env LD_PRELOAD=/path/to/lib command`
- `ld.so --library-path /path/to/dir command`
- `setarch -R command`
  - `setarch -R ld.so --library-path /path/to/dir command`
  - `setarch -R env LD_PRELOD=/path/to/lib command`

## pwndbg

- `nextcall`
- `nextjmp`
- `nextret`
- `retaddr`
- `bins`
- `heap`
- `vis_heap_chunks`

## rr

- `rr record -o /path/to/dir command`
  - `rr record -v LD_PRELOAD=/path/to/lib command`
- `rr replay /path/to/dir`

## Routine

### Standard

- `b xxx` => `b if $reg == ?`
- `b xxx` => `b if $_caller_is("fun")`
- `b xxx` => `drpintf ,"%lx\n", $reg`

### Reverse

- `rr replay` => `segfault` => `watch address` => `rc`
- `rr replay` => `segfault` => `watch $reg` => `rc`
