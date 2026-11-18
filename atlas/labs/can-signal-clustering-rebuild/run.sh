#!/bin/sh
# Independent rebuild (not ORNL code). Run from the repository root:
#   sh atlas/labs/can-signal-clustering-rebuild/run.sh <step> [step ...]
# steps: env dups prep r0 r0check sens a3 q1 q2g q2p q2pi q2pc0 q2pc1 q3g q3p diag
# Caps per step: wall 1800 s (perl alarm, plus SIGALRM inside Python),
# CPU 1800 s (ulimit -t), memory 8 GiB (watchdog on peak RSS inside Python,
# exit 97; macOS does not enforce RLIMIT_AS), processes = user count + 16,
# BLAS/OpenMP threads 1. /usr/bin/time -l records wall time and peak RSS.
set -e
L=atlas/labs/can-signal-clustering-rebuild
PY=.cache/venv-clusim/bin/python
SE=.cache/data/road/road/signal_extractions
W=.cache/data/road/work-clusim
export OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1
ulimit -t 1800
ulimit -u $(( $(ps -U $(id -u) | wc -l) + 16 ))
mkdir -p $L/raw $W
cap() { name=$1; shift; perl -e 'alarm(shift); exec(@ARGV)' 1800 /usr/bin/time -l "$@" > $L/raw/$name.stdout 2> $L/raw/$name.time; }
for step in "$@"; do
  date -u +"%FT%TZ start $step" >> $L/raw/run_log.txt
  case $step in
    env)
      { date -u +%FT%TZ; sw_vers; uname -mr; sysctl -n machdep.cpu.brand_string; echo "mem_bytes: $(sysctl -n hw.memsize)";
        $PY -VV; echo "road.zip md5: $(md5 -q .cache/data/road/road.zip)"; echo '--- uv pip freeze';
        uv pip freeze --python $PY; } > $L/raw/environment.txt 2>&1 ;;
    dups) cap dups $PY -I $L/check_dups.py $SE $L/raw/duplicate_check.json ;;
    prep) cap prep $PY -I $L/prep.py $SE $W $L/raw/prep_stats.json ;;
    r0)   cap r0   $PY -I $L/run_r0.py $W $L/raw/prep_stats.json $L/raw/r0.json ;;
    r0check) cap r0check $PY -I $L/run_r0.py $W $L/raw/prep_stats.json $L/raw/r0_final_code.json ;;
    sens) cap sens $PY -I $L/run_r0.py $W $L/raw/prep_stats.json $L/raw/sens.json --sensitivity ;;
    a3)   cap a3   $PY -I $L/run_r0.py $W $L/raw/prep_stats.json $L/raw/a3.json --a3 ;;
    q1)   cap q1   $PY -I $L/run_q.py q1 $W $SE $L/raw/q1.json --r0 $L/raw/r0.json --sens $L/raw/sens.json --a3 $L/raw/a3.json ;;
    q2g)  cap q2_global $PY -I $L/run_q.py q2 $W $SE $L/raw/q2_global.json --mode global --reps 20 --seed 0 ;;
    q2p)  cap q2_pairwise_fixed $PY -I $L/run_q.py q2 $W $SE $L/raw/q2_pairwise_fixed.json --mode pairwise --parts full,pre_injection ;;
    q2pi) cap q2_pairwise_injection $PY -I $L/run_q.py q2 $W $SE $L/raw/q2_pairwise_injection.json --mode pairwise --parts injection_only ;;
    q2pc0) cap q2_pairwise_crops_s0 $PY -I $L/run_q.py q2 $W $SE $L/raw/q2_pairwise_crops_s0.json --mode pairwise --parts crops --reps 4 --seed 0 ;;
    q2pc1) cap q2_pairwise_crops_s1 $PY -I $L/run_q.py q2 $W $SE $L/raw/q2_pairwise_crops_s1.json --mode pairwise --parts crops --reps 4 --seed 1 ;;
    q3g)  cap q3_global $PY -I $L/run_q.py q3 $W $SE $L/raw/q3_global.json --mode global ;;
    q3p)  cap q3_pairwise $PY -I $L/run_q.py q3 $W $SE $L/raw/q3_pairwise.json --mode pairwise ;;
    diag) cap diag_pairN $PY -I $L/diag_pairN.py $W $L/raw/a3.json $L/raw/r0.json $L/raw/diag_pairN.json ;;
    *) echo "unknown step $step"; exit 2 ;;
  esac
  date -u +"%FT%TZ end $step" >> $L/raw/run_log.txt
done
