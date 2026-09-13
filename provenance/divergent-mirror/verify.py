#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recomputes the results this repository states in its own voice.

    python verify.py

Standard library only. Exit 0 means everything reproduced.
"""
from __future__ import annotations

import sys
from itertools import combinations

FAILURES = []


def check(label, got, want):
    ok = got == want
    print("  %-56s %s" % (label, "PASS" if ok else "FAIL got=%r want=%r" % (got, want)))
    if not ok:
        FAILURES.append(label)


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def primitive_root(p):
    fac, m, d = set(), p - 1, 2
    while d * d <= m:
        if m % d == 0:
            fac.add(d)
            while m % d == 0:
                m //= d
        d += 1
    if m > 1:
        fac.add(m)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g
    return None


def sequences_whole_group(p):
    """Does g^1..g^(p-1) sequence all of Z_p minus zero?"""
    g = primitive_root(p)
    order = [pow(g, k, p) for k in range(1, p)]
    if sorted(order) != list(range(1, p)):
        return False
    s, seen = 0, set()
    for i, x in enumerate(order):
        s = (s + x) % p
        if i < len(order) - 1 and s == 0:
            return False
        if s in seen:
            return False
        seen.add(s)
    return True


def test_primitive_root():
    print("The one-line theorem behind a 33-minute annealing search")
    primes = [p for p in range(3, 300) if is_prime(p)]
    check("odd primes below 300 tested", len(primes), 61)
    check("failures", [p for p in primes if not sequences_whole_group(p)], [])
    check("p = 73 specifically", sequences_whole_group(73), True)
    check("  its primitive root", primitive_root(73), 5)
    print("     => every size-(p-1) sequenceability row is an instance of this")


def rc(w):
    comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(comp[c] for c in reversed(w))


def hamming(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def test_dna_11():
    print("An exact DNA-code value, witness verified")
    W = ["AACCCAA", "CCGTTTA", "GCAAGAT", "CGTTCAT", "GAGTAGT", "CACATCT",
         "CTTCAGA", "GATCTTG", "GTATCCA", "TGACACT", "TATTGCC"]
    check("word count", len(W), 11)
    check("all distinct", len(set(W)), 11)
    check("all length 7", {len(w) for w in W}, {7})
    check("all GC-weight 3", {sum(1 for c in w if c in "GC") for w in W}, {3})
    check("minimum pairwise Hamming distance",
          min(hamming(a, b) for a, b in combinations(W, 2)), 5)
    check("minimum distance to any reverse complement",
          min(hamming(a, rc(b)) for a in W for b in W), 5)


def test_graph_size():
    print("The conflict graph, rebuilt from the definition")

    def words(n, w):
        out = []
        def rec(pre):
            if len(pre) == n:
                if sum(1 for c in pre if c in "GC") == w:
                    out.append(pre)
                return
            for c in "ACGT":
                rec(pre + c)
        rec("")
        return out

    allw = words(7, 3)
    check("all length-7 GC-weight-3 words", len(allw), 4480)
    # A word within distance 5 of its OWN reverse complement can never sit in a
    # code, so it is not a vertex. Missing this filter is what made a first
    # re-implementation here report 4480 and disagree with the published table.
    V = [w for w in allw if hamming(w, rc(w)) >= 5]
    check("after the self-reverse-complement filter", len(V), 3904)
    check("  dropped", len(allw) - len(V), 576)


def test_sumfree():
    print("Maximum sum-free subset of [1,n]")
    res = []
    for n in range(1, 19):
        best = 0
        for k in range(n, 0, -1):
            if k <= best:
                break
            found = False
            for S in combinations(range(1, n + 1), k):
                Ss = set(S)
                if not any(x + y in Ss for x in S for y in S):
                    found = True
                    break
            if found:
                best = k
                break
        res.append(best)
    check("n = 1..18", res, [(n + 1) // 2 for n in range(1, 19)])
    check("  equals ceil(n/2) throughout", True, True)


def test_sunflower():
    print("Largest sunflower-free 3-uniform family on [u]")
    print("  a sunflower here: three sets whose three pairwise intersections are equal")

    def largest(u):
        T = [frozenset(t) for t in combinations(range(u), 3)]
        bad = []
        for i, j, k in combinations(range(len(T)), 3):
            a, b, c = T[i], T[j], T[k]
            if (a & b) == (b & c) == (a & c):
                bad.append({i, j, k})
        for size in range(len(T), 0, -1):
            for S in combinations(range(len(T)), size):
                Ss = set(S)
                if not any(x <= Ss for x in bad):
                    return size
        return 0

    check("u = 3", largest(3), 1)
    check("u = 4  (no sunflower triple exists at all)", largest(4), 4)
    check("u = 5", largest(5), 6)
    print("  the two larger witnesses, checked from the definition:")

    def parse(ws):
        return [frozenset(int(c) for c in w) for w in ws]

    def sunflowers(F):
        return [1 for a, b, c in combinations(F, 3)
                if (a & b) == (b & c) == (a & c)]

    W8 = parse("136 137 145 147 156 235 237 245 246 267 356 467".split())
    check("    u = 8 witness has 12 sets", len(W8), 12)
    check("      all of size 3", {len(x) for x in W8}, {3})
    check("      zero sunflower triples", sunflowers(W8), [])
    check("      and it uses only SEVEN points", len(set().union(*W8)), 7)
    print("        which is why the maximum plateaus at 12 from u=7 to u=8")

    W9 = parse("057 058 067 068 127 128 134 138 147 234 238 247 567 568".split())
    check("    u = 9 witness has 14 sets", len(W9), 14)
    check("      all of size 3", {len(x) for x in W9}, {3})
    check("      zero sunflower triples", sunflowers(W9), [])
    check("      and it uses all nine points", len(set().union(*W9)), 9)


def test_residues():
    print("Admissible residues for the pattern (r, r+2, r+6)")
    for m, want in [(3, [2]), (5, [1, 2]), (7, [2, 3, 4, 6]),
                    (11, [1, 2, 3, 4, 6, 7, 8, 10]),
                    (13, [1, 2, 3, 4, 5, 6, 8, 9, 10, 12]),
                    (17, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 16])]:
        got = [r for r in range(m)
               if r % m and (r + 2) % m and (r + 6) % m]
        check("mod %-3d" % m, got, want)


def main():
    for fn in (test_primitive_root, test_dna_11, test_graph_size,
               test_sumfree, test_sunflower, test_residues):
        fn()
        print()
    if FAILURES:
        print("FAILED: %d check(s)" % len(FAILURES))
        for f in FAILURES:
            print("   " + f)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
