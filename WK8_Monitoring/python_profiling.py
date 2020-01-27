import cProfile
import re

function_to_run = 're.compile("foo|bar")'
cProfile.run(function_to_run)

cProfile.run(function_to_run, 'restats')

import pstats
from pstats import SortKey
p = pstats.Stats('restats')
# The strip_dirs() method removed the extraneous path from all the module names.

p.strip_dirs().sort_stats(-1).print_stats()