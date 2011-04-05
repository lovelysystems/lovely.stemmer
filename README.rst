==============
Lovely Stemmer
==============

This package contains a pure python implementation of the snowball
stemmer for german as described under
http://snowball.tartarus.org/algorithms/german/stemmer.html

Here is an example on how to use the stemmer from python::

    >>> from lovely.stemmer import german
    >>> german.stem(u'kaufen')
    u'kauf'

Developement Setup
==================

Run bootstrap::

 python bootstrap.py --distribute

And run buildout::

 ./bin/buildout -N

Test the package::

 ./bin/test

These code check commands should return no output::

 ./bin/pep8
 ./bin/pyflakes

Commandline Usage
=================

There is a commandline script which takes a word per line from
stdin and outputs the stemmed version of the word. For example::

  echo kaufen | ./bin/porter_german

This script can be used to stemm complete (e.g. myspell) dictionary
files too, it strips of any trailing parts after non-word characters.

License
=======

This package is licensed under the terms of the BSD license.

Copyright (c) 2011 Lovely Systems and Contributors.
All Rights Reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

*   Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

*   Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED
TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
