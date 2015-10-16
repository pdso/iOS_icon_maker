# iOS icon maker
Like [Icon Master](http://imageresier-agrastas.rhcloud.com) or [prepo](https://itunes.apple.com/tw/app/prepo/id476533227?mt=12).Make different size icon for iPhone and iPad by Python PIL.

# Requirements
Requires the Python Imaging Library (PIL) to be installed.

`pip install PIL`

# Usage

`usage: makeicon.py [-h] [-m model] -b path`

optional arguments:

```
-h, --help  show this help message and exit
-m model    support device model,eg: iPhone, iPad, Universal, defalut is iPhone
-b path     png file path, 1024x1024 is best.
```

>Then move the `AppIcon.appiocnset` folder to Xcode project Assets.xcassets directory.

![img](/res/xcassets.png)


# The MIT License (MIT)

Copyright (c) 2015 star


