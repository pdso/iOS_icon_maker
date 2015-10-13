# -*- coding: utf-8 -*-
import os
import argparse
from PIL import Image


def makeicon(size):
    img = Image.open('1024.png', 'r')
    img.thumbnail(size, Image.ANTIALIAS)
    img.save('icon_76.png', 'PNG')

    
def get_options():
    parser = argparse.ArgumentParser(description='make iOS app icon Images.xcassets.')
    parser.add_argument('-m',  metavar='model', default='iPhone', type=str,
                    help='support device model,eg:iPhone, iPad,Universal')
    parser.add_argument('-b', metavar='path', type=file,
                    required=True, help='png file')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_options()
    model = args.m
    filepath = os.path.abspath(args.b.name)
    print model, filepath
