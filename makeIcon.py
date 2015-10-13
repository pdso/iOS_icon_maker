# -*- coding: utf-8 -*-
import os
import argparse
from PIL import Image


iphonedic = {'29': ['2', '3'],
             '40': ['2', '3'],
             '60': ['2', '3']
             }

ipadic = {'29': ['1', '2'],
          '40': ['1', '2'],
          '76': ['1', '2']
          }


def makeicon(path, width, scale):
    img = Image.open(path, 'r')
    size = int(width) * int(scale), int(width) * int(scale)
    img.thumbnail(size, Image.ANTIALIAS)
    icondir = os.path.dirname(path) + '/AppIcon.appiconset'
    if not os.path.exists(icondir):
        os.mkdir(icondir)
    filename = ''
    if scale == '1':
        filename = '/Appicon_%s.png' % width
    else:
        filename = '/Appicon_%s@%sx.png' % (width, scale)
    img.save(icondir+filename, 'PNG')


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


if __name__ == "__main__":
    args = get_options()
    model = args.m
    filepath = os.path.abspath(args.b.name)
    makeicon(filepath, '29', '2')
