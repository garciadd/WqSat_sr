import numpy as np
from sklearn.decomposition import PCA
import warnings

from wqsat_sr import algorithms

def generate_panchromatic(PanBands):
    """
    Generate a pan-chromatic image from the given bands.
    :param PBands: List of bands to be used for generating the pan-chromatic image.
    :return: Pan-chromatic image.
    """
    if len(PanBands) == 0:
        warnings.warn("No valid panchromatic band found, using bicubic interpolation")
        return None
    elif len(PanBands) == 1:
        warnings.warn("Only one band provided, returning the same band as pan-chromatic image.")
        return PanBands[0]
    else:
        h,w = PanBands[0].shape
        x = np.stack([b.flatten() for b in PanBands], axis=1)
        pca = PCA(n_components=1)
        pc1 = pca.fit_transform(x).reshape(h, w)
        return pc1

def ResolutionEnhancer(bands, method='wavelet'):

    all_bands = {}

    # Extraer bandas por resolución
    bands_10 = bands.get('10', {})
    bands_20 = bands.get('20', {})
    bands_60 = bands.get('60', {})

    panchro = generate_panchromatic(list(bands_10.values()))
    for name, b in bands_10.items():
        all_bands[name] = b
    for name, b in {**bands_20, **bands_60}.items():
        if method == 'wavelet' and panchro is not None:
            enhanced = algorithms.sr_algorithms.wavelet_enhance(b, panchro)
        else:
            # Use bicubic interpolation as default
            enhanced = algorithms.sr_algorithms.resize_band(b, b.shape, list(bands_10.values())[0].shape)
        all_bands[name] = enhanced
        
    return all_bands