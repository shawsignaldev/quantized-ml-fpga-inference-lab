# Hardware Architecture

        ## Intent

        Quantized ML FPGA Inference Lab is a public reference model for a hardware-oriented accelerator concept. The Python code
        gives deterministic arithmetic that can be inspected in CI. This architecture note describes the
        hardware/software boundary that a deeper prototype should implement.

        ## Datapath

        The target datapath is to quantize model inputs, run int8-style inference primitives, dequantize outputs, and compare scale sensitivity. The important design choice is to keep the data movement
        explicit. A fast arithmetic block is not useful if host transfers, bank conflicts, or buffering
        decisions dominate the end-to-end path.

        ## Resource Model

        - `int8 multiply lanes`
- `scale registers`
- `activation buffers`
- `saturation counters`

        Each resource should be tracked separately in a future hardware build. The public prototype avoids
        claiming deployed hardware results, but it does establish the counters and dimensions that would be needed
        to compare designs responsibly.

        ## Integration Boundary

        A production-oriented implementation should expose a narrow host API, deterministic fixtures, and
        a reference-output comparison path. The accelerator kernel should not own experiment tracking,
        dashboard rendering, or trading decisions. Those belong to the orchestration layer.
