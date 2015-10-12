# -*- coding: utf-8 -*-
import sys
from PIL import Image
from itertools import izip


def makeIcon(size):
    img = Image.open('1024.png', 'r')
    img.thumbnail(size, Image.ANTIALIAS)
    img.save('icon_76.png', 'PNG')


def machineModel():
    """
    iPhone or Pad or Universal, defautl is iPhone
    """

    if len(sys.argv) == 1:
        return 'iPhone'

    params = sys.argv[1:-1]
    i = iter(params)
    paramsDic = dict(izip(i, i))
    # model list: iPhone,iPad or Universal device
    modelList = ['iPhone', 'iPad', 'Universal']
    if '-m' in paramsDic:
        if paramsDic['-m'] in modelList:
            return paramsDic['-m']
        else:
            sys.exit("please input correct device model,eg: iPhone, iPad, Universal")
    else:
        return 'iPhone'


def deploymentVersion():
    """
    iOS version
    """

    if len(sys.argv) == 1:
        return 7.0

    params = sys.argv[1:-1]
    i = iter(params)
    paramsDic = dict(izip(i, i))
    # support iOS version list: 7.0, 8.0, 9.0
    versionList = ['7.0', '8.0', '9.0']

    if '-v' in paramsDic:
        if paramsDic['-v'] in versionList:
            return float(paramsDic['-v'])
        else:
            sys.exit('please input correct iOS version,eg: 7.0, 8.0, 9.0')
    else:
        return 7.0

if __name__ == "__main__":
    print machineModel()
    print deploymentVersion()
