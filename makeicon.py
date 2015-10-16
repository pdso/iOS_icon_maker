# -*- coding: utf-8 -*-
import os
import sys
import argparse
import json
from PIL import Image


iphonedic = {'29': ['2', '3'],
             '40': ['2', '3'],
             '60': ['2', '3']
             }

ipadic = {'29': ['1.0', '2.0'],
          '40': ['1.0', '2.0'],
          '76': ['1.0', '2.0']
          }

universaldic = {'29': ['1.0', '2', '2.0', '3'],
                '40': ['1.0', '2', '2.0', '3'],
                '60': ['2', '3'],
                '76': ['1.0', '2.0']
                }


def get_options():
    parser = argparse.ArgumentParser(
        description="make iOS app icon Images.xcassets."
    )
    parser.add_argument('-m', metavar='model',
                        default='iPhone', type=str,
                        help='support device model,'
                             'eg: iPhone, iPad, Universal, defalut is iPhone')
    try:
        parser.add_argument('-b', metavar='path', type=file,
                            required=True,
                            help='png file path, 1024x1024 is best.')
        args = parser.parse_args()
    except IOError, e:
        if e.errno == 2:
            sys.exit('IOError: No such file or directory')
    else:
        return args


def makeicon(path, width, scale):
    img = Image.open(path, 'r')
    size = int(width) * int(scale[0]), int(width) * int(scale[0])
    img.thumbnail(size, Image.ANTIALIAS)
    icondir = os.path.dirname(path) + '/AppIcon.appiconset'
    if not os.path.exists(icondir):
        os.mkdir(icondir)
    filename = ''
    if len(scale) == 3:
        if scale == '1.0':
            filename = '/Appicon%sx%s~ipad.png' % (width, width)
        else:
            filename = '/Appicon%sx%s@%sx~ipad.png' % (width, width, scale[0])
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


def makecontentjsonitem(model, width, scale):
    filename = ''
    if len(scale) == 3:
        model = 'iPad'
        if scale == '1.0':
            filename = 'Appicon%sx%s~ipad.png' % (width, width)
        else:
            filename = 'Appicon%sx%s@%sx~ipad.png' % (width, width, scale[0])
    else:
        model = 'iPhone'
        filename = 'Appicon%sx%s@%sx.png' % (width, width, scale)
    return {'size': "%sx%s" % (width, width),
            'idiom': model.lower(),
            'filename': filename,
            'scale': "%sx" % scale[0]}


def makeimagemodelist(paramsdic, model):
    images = []
    for width, scales in paramsdic.items():
        for scale in scales:
            m = makecontentjsonitem(model, width, scale)
            images.append(m)
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
    jsons = json.dumps(contentjson, indent=4)
    with open(icondir + '/Contents.json', 'w') as f:
        f.write(jsons)


if __name__ == "__main__":
    args = get_options()
    model = args.m
    if model not in ['iPhone', 'iPad', 'Universal']:
        sys.exit('Error: -m,model should be iPhone, iPad or Universal')
    filepath = os.path.abspath(args.b.name)
    makeicons(filepath, model)
    makecontentjson(filepath, model)
    print os.path.dirname(filepath) + '/AppIcon.appiconset'
