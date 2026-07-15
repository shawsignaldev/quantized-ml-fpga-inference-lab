def quantize_int8(values: list[float], scale: float) -> list[int]:
    if scale <= 0:
        raise ValueError("scale must be positive")
    return [max(-128, min(127, round(value / scale))) for value in values]

def dequantize_int8(values: list[int], scale: float) -> list[float]:
    if scale <= 0:
        raise ValueError("scale must be positive")
    return [round(value * scale, 6) for value in values]
