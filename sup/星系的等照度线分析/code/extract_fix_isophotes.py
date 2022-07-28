import numpy as np
from photutils.isophote import EllipseGeometry
from photutils.isophote import EllipseSample
from photutils.isophote import Isophote, IsophoteList


def extract_fix_isophotes(image=None, xcen=None, ycen=None, initsma=None, eps=None, pa=None, step=None, 
                          linear_growth=False, minsma=None, maxsma=None, silent=False):
    """
    Function to extract surface brightness profile with fixed center, ellipticity, and position angle.
    """
    syntax = "syntax: results = extract_fix_isophotes(image=, xcen=, ycen=, initsma=, eps=, pa=, step=, linear_growth=False/True, minsma=None, maxsma=None, silent=False/True; minsma maxsma are optional)"
    if (None in [xcen, ycen, initsma, eps, pa, step]) or (image is None):
        print(syntax)
        return []
    print(syntax) if silent == False else print("")
    
    minsma = minsma if minsma is not None else 0.5
    maxsma = maxsma if maxsma is not None else max(np.shape(image))/2*1.3
    isophote_list = []

    geometry = EllipseGeometry(xcen, ycen, initsma, eps, pa, astep=step, linear_growth=False, 
                               fix_center=True, fix_pa=True, fix_eps=True)
    
    sma = initsma
    while True:
        sample = EllipseSample(image, sma, geometry=geometry)

        sample.update(geometry.fix)
        isophote = Isophote(sample, 0, True, stop_code=4)
        isophote_list.append(isophote)
        sma = isophote.sample.geometry.update_sma(step)
        if maxsma and sma >= maxsma:
            break

    first_isophote = isophote_list[0]
    sma, step = first_isophote.sample.geometry.reset_sma(step)

    while True:
        sample = EllipseSample(image, sma, geometry=geometry)

        sample.update(geometry.fix)
        isophote = Isophote(sample, 0, True, stop_code=4)
        isophote_list.append(isophote)
        sma = isophote.sample.geometry.update_sma(step)
        if minsma and sma <= max(minsma, 0.5):
            break

    isophote_list.sort()
    iso_fix = IsophoteList(isophote_list)
    
    return iso_fix