primitive, meaning that the call was not induced via recursion

`ncalls`
for the number of calls.

`tottime`
for the total time spent in the given function (and excluding time made in calls to sub-functions)

`percall`
is the quotient of tottime divided by ncalls

`cumtime`
is the cumulative time spent in this and all subfunctions (from invocation till exit). This figure is accurate even for recursive functions.

`percall`
is the quotient of cumtime divided by primitive calls

`filename:lineno(function)`
provides the respective data of each function