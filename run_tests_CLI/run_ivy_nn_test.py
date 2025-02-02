import sys
from ivy_tests.test_ivy.helpers.available_frameworks import available_frameworks


run = int(sys.argv[1])
backends = available_frameworks
submodules = [
    "activations",
    "layers",
    "losses",
    "norms",
]

N = len(backends)
M = len(submodules)

num_tests = N * M
run = run % num_tests

i = run // M
j = run % M

backend = backends[i]
submodule = submodules[j]

with open("./fwsubmod.txt", "w") as outfile:
    outfile.write(f"{backend}-{submodule}")

with open("./backend.txt", "w") as f:
    f.write(f"{backend}")

with open("./submodule.txt", "w") as f:
    f.write(f"test_{submodule}")
