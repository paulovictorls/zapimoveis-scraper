#!/usr/bin/env python

# Copyright (c) 2009-2018, Geovany Rodrigues
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice,this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

from os import chdir
from os.path import abspath, join, split

# Make sure we are standing in the correct directory.
# Old versions of distutils didn't take care of this.
here = split(abspath(__file__))[0]
chdir(here)

# Package metadata.
metadata = dict(
    name='zapimoveis_scraper',
    provides=['zapimoveis_scraper'],
    requires=['beautifulsoup4'],
    packages=['zapimoveis_scraper'],
    scripts=[join('scripts', 'zapimoveis')],
    version="0.3.1",
    description="zapimoveis-scraper is a Python package that works as a crawler and scraper using beautifulsoup4 to get data from zap imoveis",
    author="Geovany Rodrigues",
    author_email="geovanyscv@gmail.com",
    url='https://github.com/GeovRodri/zapimoveis-scraper',
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Environment :: Console",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
     ],
)

# Prefer setuptools over the old distutils.
# If setuptools is available, use install_requires.
try:
    from setuptools import setup
    metadata['install_requires'] = metadata['requires']
except ImportError:
    from distutils.core import setup

# Get the long description from the readme file.
try:
    metadata['long_description'] = open(join(here, 'README.md'), 'r').read()
except Exception:
    pass

# Run the setup script.
setup(**metadata)
