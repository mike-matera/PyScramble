import sys

if sys.version_info < (3, 10):
    program = sys.argv[0]
    args = sys.argv[1:]
else:
    program = sys.orig_argv[0]
    args = sys.argv

print("program:", program)
print("args:", args)
