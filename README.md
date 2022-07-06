# Scramble a Python Binary 

A tool to scramble Python scripts. The scrambling obfuscates the source code and strings making it difficult --but not impossible-- for an attacker to see the Python code. Otherwise the script runs like a regular Python executable. 

Scripts compiled this way can be safely made SUID root because there's no race condition when reading the Python code. 

## Use 

Install the package form this repository: 

```console 
$ pip install git+https://github.com/mike-matera/PyScramble.git
```

Scramble a Python file: 

```console 
$ echo "print('Hello World')" > myfile.py
$ pyscramble myfile.py 
$ ./myfile 
Hello World
```

## Caution 

**This protection only slows down attackers, it CANNOT stop them.** Consider the encryptor's dilemma: 

> In order to run the executable you must decrypt the executable with the key. Since these executables can be run by anyone, everyone has access to the key. 

It's easy for an attacker to disassemble the generated files and find the original source because the key is embedded in the executable. Also, since the original source is in process memory, stack dumps from exceptions will show bits of unobfuscated code, which may reveal your secrets. 

This tool is intended to foil attacks with `cat` and `strings`. It won't hold up to much else. 

## Limitations 

1. This is only tested and probably only works on Linux. 
1. Compiled binaries will only run on the Python interpreter that created them (they are in no way portable). 
1. The system must have the C compiler and Python headers installed. 