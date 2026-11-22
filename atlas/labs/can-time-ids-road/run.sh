#!/bin/sh
# Reproduce from the repository root: sh atlas/labs/can-time-ids-road/run.sh
# Caps: CPU time 3600 s (ulimit -t), wall clock 3600 s per step (perl alarm),
# max user processes = current user count + 64 (ulimit -u is per user on macOS), BLAS/OpenMP threads 1. macOS does not
# enforce ulimit -v, so memory is measured (/usr/bin/time -l), not capped.
set -e
L=atlas/labs/can-time-ids-road
PY=.cache/venv-can-ids/bin/python
ROAD=.cache/data/road/road
SRC=.cache/src/can-time-ids-e0c862d
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
ulimit -t 3600
ulimit -u $(( $(ps -U $(id -u) | wc -l) + 64 ))  # macOS counts all of the user's processes
W="perl -e alarm(shift);exec(@ARGV) 3600"
mkdir -p $L/raw
$W /usr/bin/time -l $PY -I $L/equivalence_check.py $SRC $ROAD $L/raw/equivalence.json > $L/raw/equivalence.stdout 2> $L/raw/equivalence.time
$W /usr/bin/time -l $PY -I $L/run_experiment.py $ROAD $L/raw --seed 0 > $L/raw/run_seed0.stdout 2> $L/raw/run_seed0.time
$W /usr/bin/time -l $PY -I $L/run_experiment.py $ROAD $L/raw --seed 1 --r0-only > $L/raw/run_seed1.stdout 2> $L/raw/run_seed1.time
