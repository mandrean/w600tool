#!/usr/bin/env python
#-*- coding:utf-8 -*-


from setuptools import setup, find_packages          

setup(
    name = "w600tool",      
    version = "1.0.0",  
    keywords = ("pip", "SICA","featureextraction"),
    description = "An feature extraction algorithm",
    long_description = "An feature extraction algorithm, improve the FastICA",

    url = "https://github.com/wemos/w600tool",    
    author = "wemos",
    author_email = "support@wemos.cc",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = [
        "pyserial>=3.0",
        "argparse",
        "pyprind",
        "xmodem"，
    ]          
)

