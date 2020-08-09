from functools import partial


def read_from(filename, block_size=1024*8):
    with open(filename, 'r') as f:
        for truck in iter(partial(f.read, block_size), ''):
            yield truck



