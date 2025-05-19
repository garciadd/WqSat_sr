import numpy as np
import cv2
from typing import Dict, Literal, Tuple
import pywt

class sr_algorithms:
    """
    Class containing various super-resolution algorithms.
    """

    def wavelet_enhance(band_lr: np.ndarray, band_hr: np.ndarray) -> np.ndarray:

        h, w = band_hr.shape
        coeffs_lr = pywt.wavedec2(band_lr, 'db4', level=2)
        coeffs_hr = pywt.wavedec2(band_hr, 'db4', level=2)
        new_coeffs = list(coeffs_lr)
        new_coeffs[1:] = coeffs_hr[1:]  # reemplazar detalles
        enhanced = pywt.waverec2(new_coeffs, 'db4')
        return cv2.resize(enhanced, (w, h), interpolation=cv2.INTER_CUBIC)

    def resize_band(self, band: np.ndarray, target_shape: Tuple[int, int]) -> np.ndarray:
        return cv2.resize(band, (target_shape[1], target_shape[0]), interpolation=cv2.INTER_CUBIC)