#!/usr/bin/env python3
"""Public verifier for the constant-GC reverse-complement code release.

Standard library only.

Checks:
  * 4,480 length-7 words of GC-weight 3;
  * 576 fail the self-reverse-complement distance-5 gate;
  * 3,904 admissible vertices remain;
  * the published 11-word witness has the required parameters.

This intentionally does not claim to reproduce the historical clique-solver
upper-bound certificate or the recovered 28-word length-8 witness, whose
original bytes are separate source-recovery obligations.
"""

from itertools import product, combinations

ALPHABET = "ACGT"
COMP = str.maketrans("ACGT", "TGCA")
WITNESS_753 = [
    "AACCCAA",
    "CCGTTTA",
    "GCAAGAT",
    "CGTTCAT",
    "GAGTAGT",
    "CACATCT",
    "CTTCAGA",
    "GATCTTG",
    "GTATCCA",
    "TGACACT",
    "TATTGCC",
]


def reverse_complement(word: str) -> str:
    return word.translate(COMP)[::-1]


def hamming(a: str, b: str) -> int:
    return sum(x != y for x, y in zip(a, b))


def gc_weight(word: str) -> int:
    return sum(c in "GC" for c in word)


def constant_gc_words(n: int, w: int):
    for letters in product(ALPHABET, repeat=n):
        word = "".join(letters)
        if gc_weight(word) == w:
            yield word


def admissible_self(word: str, d: int) -> bool:
    return hamming(word, reverse_complement(word)) >= d


def check_witness(words, n: int, d: int, w: int):
    assert len(words) == len(set(words)), "witness contains duplicate words"
    assert all(len(x) == n for x in words), "wrong word length"
    assert all(gc_weight(x) == w for x in words), "wrong GC weight"
    assert all(admissible_self(x, d) for x in words), "self-RC violation"

    min_pair = min(hamming(a, b) for a, b in combinations(words, 2))
    min_rc = min(
        hamming(a, reverse_complement(b))
        for a in words
        for b in words
    )
    assert min_pair >= d, ("pairwise distance", min_pair)
    assert min_rc >= d, ("reverse-complement distance", min_rc)
    return min_pair, min_rc


def main():
    all_words = list(constant_gc_words(7, 3))
    inadmissible = [x for x in all_words if not admissible_self(x, 5)]
    admissible = [x for x in all_words if admissible_self(x, 5)]

    assert len(all_words) == 4480, len(all_words)
    assert len(inadmissible) == 576, len(inadmissible)
    assert len(admissible) == 3904, len(admissible)

    min_pair, min_rc = check_witness(WITNESS_753, 7, 5, 3)

    print("constant-GC reverse-complement verifier")
    print("length-7 GC-weight-3 words:", len(all_words))
    print("self-RC invalid words:", len(inadmissible))
    print("admissible graph vertices:", len(admissible))
    print("witness size:", len(WITNESS_753))
    print("minimum pairwise Hamming distance:", min_pair)
    print("minimum reverse-complement distance:", min_rc)
    print("PASS")


if __name__ == "__main__":
    main()
