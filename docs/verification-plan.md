# Verification Plan

## Golden Model

The Python implementation is the golden model. Every later RTL, HLS, C++, or vectorized kernel
should match it on deterministic fixtures before performance is discussed. This keeps correctness
ahead of optimization.

## Test Classes

1. Shape tests for empty, small, aligned, and unaligned inputs.
2. Boundary tests for saturation, zero-size cases, bank imbalance, and invalid dimensions.
3. Equivalence tests comparing optimized outputs to the Python reference model.
4. Stress tests that sweep tile sizes, lane counts, and buffer capacities.
5. Regression tests for every arithmetic bug or mismatch found during optimization.

## Signoff Evidence

A stronger future version should include CI for the reference model, a generated fixture set, a
hardware-interface sketch, and a report showing correctness before speed. For FPGA-oriented work,
timing, utilization, and board measurements should only be reported after the appropriate toolchain
artifacts exist.

## Review Standard

The repository should be judged on disciplined decomposition: clear model, explicit datapath,
bounded assumptions, deterministic tests, and honest separation between public prototype and
hardware implementation.
