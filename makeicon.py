# -*- coding: utf-8 -*-
import os
import argparse
import json
from PIL import Image


iphonedic = {'29': ['2', '3'],
             '40': ['2', '3'],
             '60': ['2', '3']
             }

ipadic = {'29': ['1', '2'],
          '40': ['1', '2'],
          '76': ['1', '2']
          }

universaldic = {'29': ['1', '2', '3'],
                '40': ['1', '2', '3'],
                '60': ['2', '3'],
                '76': ['1', '2']
                }


def get_options():
    parser = argparse.ArgumentParser(
        description="make iOS app icon Images.xcassets."
    )
    parser.add_argument('-m', metavar='model', default='iPhone', type=str,
                        help='support device model,eg:iPhone, iPad,Universal')
    parser.add_argument('-b', metavar='path', type=file,
                        required=True, help='png file')
    args = parser.parse_args()
    return args


def makeicon(path, width, scale):
    img = Image.open(path, 'r')
    size = int(width) * int(scale), int(width) * int(scale)
    img.thumbnail(size, Image.ANTIALIAS)
    icondir = os.path.dirname(path) + '/AppIcon.appiconset'
    if not os.path.exists(icondir):
        os.mkdir(icondir)
    filename = ''
    if scale == '1':
        filename = '/Appicon%sx%s.png' % width
    else:
        filename = '/Appicon%sx%s@%sx.png' % (width, width, scale)
    img.save(icondir+filename, 'PNG')


def makeicons(path, model):
    dic = {}
    if model == 'iPhone':
        dic = iphonedic
    elif model == 'iPad':
        dic = ipadic
    else:
        dic = universaldic

    for width, scales in dic.items():
        for scale in scales:
            makeicon(path, width, scale)
    return


class ImageModel(object):
    def __init__(self, size, idiom, filename, scale):
        self.size = size
        self.idiom = idiom
        self.filename = filename
        self.scale = scale


def makecontentjsonitem(model, width, scale):
    filename = ''
    if scale == '1':
        filename = 'Appicon%sx%s.png' % width
    else:
        filename = 'Appicon%sx%s@%sx.png' % (width, width, scale)

    return ImageModel("%sx%s" % (width, width),
                      model,
                      filename,
                      "%s" % scale)


def makeimagemodelist(paramsdic, model):
    images = []
    for width, scales in paramsdic.items():
        for scale in scales:
            m = makecontentjsonitem(model, width, scale)
            images.append(m.__dict__)
    return images


def makecontentjson(path, model):
    icondir = os.path.dirname(path) + '/AppIcon.appiconset'
    if not os.path.exists(icondir):
        os.mkdir(icondir)
    dic = []
    if model == 'iPhone':
        dic = iphonedic
    elif model == 'iPad':
        dic = ipadic
    else:
        dic = universaldic
    contentjson = {}
    contentjson['images'] = makeimagemodelist(dic, model)
    contentjson['info'] = {'version': 1,
                           'author': 'xcode'}
    jsons = json.dumps(contentjson)
    with open(icondir + '/Contents.json', 'w') as f:
        f.write(jsons)


if __name__ == "__main__":
    args = get_options()
    model = args.m
    filepath = os.path.abspath(args.b.name)
    makeicons(filepath, model)
    makecontentjson(filepath, model)
