from collections import OrderedDict
import cv2

class cvTypes():
    """docstring for ClassName"""
    def __init__(self):
        pass
        
    thresholdTypes=['Simple', 'Adaptive']
    thresholdChannels=['All','0','1','2']
    blurTypes=['Convolution','Blur','BoxFilter','GaussianBlur','MedianBlur','BilateralFilter']
    morpTypes=['Erosion','Dilation','Opening','Closing','Morphological Gradient','Top Hat','Black Hat']
    gradientTypes=['Sobel','Laplacian']
    gradientDirection=['x','y', 'Both']
    houghTypes=['Simple','Probabilistic']
    colorCodes=['RGB','RGBA','BGR','BGRA','GRAY','HSV','HLS']

    colorCodesMap = {
        'RGB2GRAY' : cv2.COLOR_RGB2GRAY,
        'RGB2RGBA' : cv2.COLOR_RGB2RGBA,
        'RGB2BGR' : cv2.COLOR_RGB2BGR,
        'RGB2BGRA' : cv2.COLOR_RGB2BGRA,
        'RGB2HSV' : cv2.COLOR_RGB2HSV,
        'RGB2HLS' : cv2.COLOR_RGB2HLS,
        'RGBA2GRAY' : cv2.COLOR_RGBA2GRAY,
        'RGBA2RGB' : cv2.COLOR_RGBA2RGB,
        'RGBA2BGR' : cv2.COLOR_RGBA2BGR,
        'RGBA2BGRA' : cv2.COLOR_RGBA2BGRA,
        'BGR2GRAY' : cv2.COLOR_BGR2GRAY,
        'BGR2BGRA' : cv2.COLOR_BGR2BGRA,
        'BGR2RGB' : cv2.COLOR_BGR2RGB,
        'BGR2RGBA' : cv2.COLOR_BGR2RGBA,
        'BGR2HSV' : cv2.COLOR_BGR2HSV,
        'BGR2HLS' : cv2.COLOR_BGR2HLS,
        'BGRA2GRAY' : cv2.COLOR_BGRA2GRAY,
        'BGRA2BGR' : cv2.COLOR_BGRA2BGR,
        'BGRA2RGB' : cv2.COLOR_BGRA2RGB,       
        'BGRA2RGBA' : cv2.COLOR_BGRA2RGBA,
        'GRAY2BGR' : cv2.COLOR_GRAY2BGR,
        'GRAY2BGRA' : cv2.COLOR_GRAY2BGRA,
        'GRAY2RGB' : cv2.COLOR_GRAY2RGB,
        'GRAY2RGBA' : cv2.COLOR_GRAY2RGBA,
        'HSV2BGR' : cv2.COLOR_HSV2BGR,
        'HSV2RGB' : cv2.COLOR_HSV2RGB,
        'HLS2BGR' : cv2.COLOR_HLS2BGR,
        'HLS2RGB' : cv2.COLOR_HLS2RGB
    }

    simpleThresholdMethods = OrderedDict([
        ('THRESH_BINARY',cv2.THRESH_BINARY),
        ('THRESH_BINARY_INV',cv2.THRESH_BINARY_INV),
        ('THRESH_TRUNC',cv2.THRESH_TRUNC),
        ('THRESH_TOZERO',cv2.THRESH_TOZERO),
        ('THRESH_TOZERO_INV',cv2.THRESH_TOZERO_INV)
    ])

    adaptiveThresholdMethods = {
        'ADAPTIVE_THRESH_MEAN': cv2.ADAPTIVE_THRESH_MEAN_C,
        'ADAPTIVE_THRESH_GAUSSIAN': cv2.ADAPTIVE_THRESH_GAUSSIAN_C
    }

    def getMethods(self, type):
        if type == 'Adaptive':
            return self.simpleThresholdMethods.keys()[:2]
        return self.simpleThresholdMethods.keys()