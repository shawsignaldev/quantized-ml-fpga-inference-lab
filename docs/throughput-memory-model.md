# Throughput And Memory Model

## Primary Constraint

poor scale selection can saturate activations or lose signal resolution before the accelerator sees the data. The model should therefore track both compute cycles and memory movement. A single
throughput number is not enough; reviewers need to see whether the design is compute-bound,
memory-bound, or transfer-bound.

## Measurements To Track

- Input elements per batch
- Output elements per batch
- Bytes read and written per decision
- Estimated compute cycles
- Buffer occupancy and tile utilization
- Host transfer overhead when applicable

## Roofline Framing

The first-order analysis should compare arithmetic intensity against available bandwidth. If the
design has low arithmetic intensity, optimization should focus on layout, tiling, reuse, and transfer
batching before adding more compute lanes. If arithmetic intensity is high, utilization and pipeline
occupancy become the main questions.

## Reporting Rule

Future benchmark reports should separate model-estimated cycles from measured hardware results.
Simulated estimates are useful for design review, but they must remain clearly labeled until a real
toolchain, board, clock constraint, and repeatable benchmark harness are present.
