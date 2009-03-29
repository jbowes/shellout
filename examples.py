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

import shellout as so


def print_formatted(input):
    """
    Prints output in a specific format.

    :Parameters:
       - `input`: the input to print.
    """
    print("=============================================\n")
    print(input)
    print("\n")


if __name__ == '__main__':
    # examples!
    print_formatted(so.ls.l.si("/"))
    print_formatted(so.svn.help())
    print_formatted(so.ps.a.u.x())
    print_formatted(so.ls.color["always"]("/"))
    print_formatted(so.grep("model name", "/proc/cpuinfo"))
    print_formatted(so.echo('with "both" \'quotes\''))
