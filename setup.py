#!/usr/bin/env python
#
# Copyright (c) 2009 James Bowes <jbowes@dangerouslyinc.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


from setuptools import setup

long_description = ""
try:
    f = open('README.rst')
    long_description = f.read()
    f.close()
except Exception as e:
    print str(e)  # If there's an issue, don't worry.

setup(
    name="shellout",
    version="0.2",
    description="Make your shelled out calls look like genuine OO code",
    author="James Bowes",
    author_email="jbowes@dangerouslyinc.com",
    url="http://github.com/jbowes/shellout/",
    platforms=['any'],
    license="MIT",
    keywords=["cli", "exec", "shell", "subprocess"],

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
    ],

    py_modules=["shellout"],
)
