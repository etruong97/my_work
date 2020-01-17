#!/usr/bin/python3

# This program determines which contests your solution is eligible for.
# If your solution takes *more than five minutes* to solve a board,
# or it gets an *incorrect solution*, then it is not eligible for that
# board's contest.

# Please run this before submitting your code to the contest.

import sys
import os
import csv

import a2

try:
    import a2_bonus
except ImportError:
    print("Assessing the performance of a2.py")
except SyntaxError:
    print("Assessing the performance of a2.py")
    raise SyntaxWarning("a2_bonus.py contains invalid syntax")
else:
    print("Assessing the performance of a2_bonus.py")
    a2 = a2_bonus

# Please do not be discouraged if your initial code cannot complete
# all of these tests.
test_dirs = []
for name in os.listdir('tests/'):
    if os.path.isdir('tests/'+name):
        test_dirs.append(name)
test_dirs.sort()

### Timeout code credit David Narayan, Thomas Ahle, and vmarquet
### https://stackoverflow.com/questions/2281850/timeout-function-if-it-takes-too-long-to-finish
### Timeout works on *nix only.

if sys.platform in ['linux', 'darwin']:
    import signal

    class timeout:
        def __init__(self, board=''):
            self.error_code = 'Board %s took over 2 minutes to solve.' % board
        def handle_timeout(self, signum, frame):
            raise TimeoutError(self.error_code)
        def __enter__(self):
            signal.signal(signal.SIGALRM, self.handle_timeout)
            signal.alarm(120)
        def __exit__(self, type, value, traceback):
            signal.alarm(0)
else:
    import time

    class timeout: # dummy timeout
        def __init__(self, board=''):
            self.error_code = 'Board %s took over 2 minutes to solve.' % board
        def __enter__(self):
            self.start_time = time.time()
        def __exit__(self, type, value, traceback):
            if time.time() - self.start_time > 120:
                raise TimeoutError(self.error_code)

# loads the solved board from the given file; assumes that file is well-formed
def loadSolution(filename):
    board = {}
    with open(filename) as csvFile:
        n = -1
        reader = csv.reader(csvFile)
        for row in reader:
            for index, item in enumerate(row):
                if not item == '':
                    board[(reader.line_num-1, index)] = int(item)
    return board


contests = []

for test_dir in test_dirs:
    tests = os.listdir('tests/'+test_dir)
    tests.sort()

    if test_dir != 'named-boards':
        print('-------------------------\nTesting: '+test_dir+'...')
        failed = False
    for test in tests:
        if test.endswith('.csv'): # valid test
            if test_dir == 'named-boards':
                print('-------------------------\nTesting: '+test+'...')
            try:
                with timeout('%s/%s' % (test_dir, test)):
                    s = a2.Solver()
                    board = a2.Board("tests/%s/%s" % (test_dir, test))
                    s.solve(board)
                    if board.board != loadSolution("solutions/%s/%s" % (test_dir, test)):
                        raise RuntimeError("Solution for %s/%s does not match." % (test_dir, test))
            except (TimeoutError, RuntimeError) as err:
                print('\nTest failed: %s' % str(err))
                if test_dir != 'named-boards':
                    failed = True
                    break
                else: continue
            if test_dir == 'named-boards':
                print('Success!')
                contests.append(test)
            else:
                print('.', end='', flush=True)
    if test_dir != 'named-boards' and not failed:
        print('\nSuccess!')
        contests.append(test_dir)

print('-------------------------\nYou are eligible to compete in the following contests:')
print(contests)
