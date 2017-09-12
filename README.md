# BrainFlump

A Turing Tarpit that uses a Dump and a Cell as its memory model, rather than a Stack, Tree, Heap, Queue or Tape.

What's a Dump? It's a big unordered blop of values that just spits out a random value when you pop from it. A Cell is a single numerical value.

Have fun!

## Running BrainFlump

BrainFlump is written in Python2 and designed for PyPy.

How to run: `python BrainFlump.py <mode> <code|filename>`

Mode: `-c` to run code directly, `-f` to run code from a file

## Using BrainFlump

```
    +   Increment the Cell
    -   Decrement the Cell
    :   Push the Cell's value to the Dump
    ;   Pop a random value from the Dump to the Cell
    (   Start a loop, BrainFuck style
    )   End a loop, BrainFuck style
    ,   Read 1 char from input, assign to the Cell's value
    .   Print the Cell's value modulo 127 as an ASCII char
```

All other chars are ignored (yo don't use spaces tho it'll fuck up the arguments)

