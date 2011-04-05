# -*- coding: utf-8 -*-

import sys
import re

VOWELS = u"aeiouyäöü"
SAVES_PAT = re.compile(u'(.*[%s])([u,y])([%s].*)' % (VOWELS, VOWELS), re.U)

S_END = u'bdfghklmnrt'
ST_END = u'bdfghklmnt'
E_SFX1 = [u'ern', u'em', u'en', u'er', u'es', u'e']
E_SFX2 = [u'en', u'er', u'est']

S_SFX = map(lambda x: x + u's', S_END)
ST_SFX = map(lambda x: x + u'st', ST_END)

SFX_1 = sorted(E_SFX1 + S_SFX, key=lambda x: -len(x))
SFX_2 = sorted(E_SFX2 + ST_SFX, key=lambda x: -len(x))
SFX_3 = [u'end', u'ung']
SFX_4 = [u'ig', u'ik', u'isch']
SFX_5 = [u'lich', u'heit']


def _save_yu(w):
    def _upper(m):
        return m.group(1) + m.group(2).upper() + m.group(3)
    while True:
        m = SAVES_PAT.sub(_upper, w)
        if w == m:
            return w
        w = m


def _get_r(s):
    last = None
    res = []
    for i, c in enumerate(s):
        if len(res) > 1:
            break
        if c not in VOWELS and last and last in VOWELS:
            if not res:
                i = max(2, i)
                res.append(s[i + 1:])
            else:
                res.append(s[i + 1:])
                return res
        last = c
    res = res + [u''] * (2 - len(res))
    return res


def stem(w):
    w = w.lower()
    w = _save_yu(w)
    w = w.replace(u'ß', u'ss')

    r1, r2 = _get_r(w)

    def _del(w, sfx):
        l = len(sfx)
        w = w[:-l]
        r1, r2 = _get_r(w)
        return w, r1, r2

    for sfx in SFX_1:
        if w.endswith(sfx):
            s = sfx in S_SFX
            if not s and sfx in r1:
                w, r1, r2 = _del(w, sfx)
            elif s and sfx[-1:] in r1:
                w, r1, r2 = _del(w, sfx[:-1])
            break

    for sfx in SFX_2:
        if w.endswith(sfx):
            if sfx in ST_SFX:
                if len(w) >= 6 and u'st' in r1:
                    w, r1, r2 = _del(w, sfx[-2:])
            elif sfx in r1:
                w, r1, r2 = _del(w, sfx)
            break

    done = False

    for sfx in SFX_3:
        if w.endswith(sfx) and sfx in r2:
            done = True
            w, r1, r2 = _del(w, sfx)
            if w.endswith(u'ig') and not w.endswith(u'eig') and u'ig' in r2:
                w, r1, r2 = _del(w, u'ig')
            break

    if not done:
        for sfx in SFX_4:
            if sfx in r2 and w.endswith(sfx) and not w.endswith(u'e' + sfx):
                w, r1, r2 = _del(w, sfx)
                done = True

    if not done:
        for sfx in SFX_5:
            if w.endswith(sfx) and sfx in r2:
                done = True
                w, r1, r2 = _del(w, sfx)
                for sfx in [u'en', u'er']:
                    if w.endswith(sfx) and sfx in r1:
                        w, r1, r2 = _del(w, sfx)

    sfx = u'keit'
    if not done and w.endswith(sfx):
        done = True
        if sfx in r2:
            w, r1, r2 = _del(w, sfx)
        for sfx in [u'lich', u'ig']:
            if w.endswith(sfx) and sfx in r2:
                w, r1, r2 = _del(w, sfx)

    w = w.lower()
    for uml, repl in [u'öo', u'äa', u'üu']:
        w = w.replace(uml, repl)

    return w

# split by any none word char
TOKEN_PAT = re.compile('[\W+_]', re.UNICODE)
NUM_PAT = re.compile(r'^[0-9\.]+$')


def main():
    stream = sys.stdin
    out = sys.stdout
    last = None
    for l in stream:
        l = l.strip()
        l = l.decode('utf-8')
        if '-' in l or NUM_PAT.match(l):
            continue
        for term in TOKEN_PAT.split(l, 1):
            s = stem(term).encode('utf-8')
            if s and len(s) > 2 and s != last:
                print >> out, s
                last = s
            break
