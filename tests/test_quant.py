from quantized_ml_fpga_inference_lab.quant import dequantize_int8, quantize_int8

def test_quantize_int8_clamps_to_signed_range() -> None:
    assert quantize_int8([-20.0, 0.0, 20.0], scale=0.1) == [-128, 0, 127]

def test_dequantize_int8_restores_scaled_values() -> None:
    assert dequantize_int8([-2, 0, 3], scale=0.5) == [-1.0, 0.0, 1.5]
