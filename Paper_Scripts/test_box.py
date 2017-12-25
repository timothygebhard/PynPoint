import os
import sys
module_path = os.path.abspath(os.path.join('../'))
if module_path not in sys.path:
    sys.path.append(module_path)
from PynPoint import Pypeline
from PynPoint.processing_modules import WaveletTimeDenoisingModule, CwtWaveletConfiguration

pipeline = Pypeline("/scratch/user/mbonse/FastPca",
                    "/scratch/user/mbonse/FastPca",
                    "/scratch/user/mbonse/FastPca")

from PynPoint.processing_modules import StackAndSubsetModule

stack = StackAndSubsetModule(name_in="stacking",
                             image_in_tag="psf_normalized",
                             image_out_tag="10_stacked",
                             stacking=10)

pipeline.add_module(stack)
pipeline.run_module("stacking")


'''
wv = CwtWaveletConfiguration(wavelet="dog",
                             wavelet_order=2,
                             keep_mean=False,
                             resolution=0.5)

time_denoising = WaveletTimeDenoisingModule(wv,
                                            name_in="time_denoising",
                                            image_in_tag="10_stacked",
                                            image_out_tag="star_arr_denoised",
                                            denoising_threshold=1.0,
                                            padding="zero",
                                            median_filter=True,
                                            threshold_function="soft")

pipeline.add_module(time_denoising)

pipeline.run_module("time_denoising")'''

from PynPoint.processing_modules import PSFSubtractionPCAmulit

psf_subtraction = PSFSubtractionPCAmulit(range(10),
                                         name_in="PSF_subtraction",
                                         images_in_tag="10_stacked",
                                         reference_in_tag="10_stacked")
pipeline.add_module(psf_subtraction)

pipeline.run_module("PSF_subtraction")
