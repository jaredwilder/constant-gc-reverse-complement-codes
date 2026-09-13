# Constant-GC reverse-complement DNA codes

**Author:** Jared Wilder  
**Public subject home:** 2026-09-13  
**Status:** exact finite coding-theory results + open frontier

This repository is the canonical public home for a coding-theory program that was previously buried inside a mixed divergent-mirror audit.

For words over `{A,C,G,T}^n`, fix GC-weight exactly `w`, require pairwise Hamming distance at least `d`, and also require distance at least `d` from every reverse complement, including a word's own reverse complement.

Write `A_RC^GC(n,d,w)` for the maximum size of such a code.

## Exact result

### `A_RC^GC(7,5,3) = 11`

The full admissible conflict graph was rebuilt from the definition.

- all length-7 words of GC-weight 3: **4,480**;
- words invalidated by being within distance `<5` of their own reverse complement: **576**;
- surviving graph vertices: **3,904**;
- conflict-graph edges in the recovered audit: **3,945,728**;
- density: approximately **0.5179**;
- exact optimum: **11**.

A verified 11-word code is

```text
AACCCAA
CCGTTTA
GCAAGAT
CGTTCAT
GAGTAGT
CACATCT
CTTCAGA
GATCTTG
GTATCCA
TGACACT
TATTGCC
```

Every word has length 7 and GC-weight 3. The minimum pairwise Hamming distance is 5 and the minimum distance from any codeword to the reverse complement of any codeword is also 5.

The recovered upper-bound computation used nine clique-solver shards over a nine-orbit decomposition under a symmetry group of order **12,288**, with orbit sizes

```text
1024, 768, 768, 384, 384, 384, 96, 48, 48
```

which sum to 3,904.

The historical packet described this as a reproduction by a faster route rather than a new discovery claim. This repository preserves that distinction.

## The length-8 frontier

A historical 28-word code for `(n,d,w)=(8,5,4)` was recovered from an archived web page and independently verified in the source campaign, establishing

```text
A_RC^GC(8,5,4) >= 28.
```

The reconstructed length-8 conflict graph has

- **13,792 vertices**;
- **72,209,664 edges**;
- density approximately **0.7593**.

A 29-word candidate was also found with **exactly one** reverse-complement violation. The offending pair was

```text
ACACACGA
TCGTGTGT
```

and these two words are exact reverse complements of one another. All other reported relations in that candidate were clean.

### Current frontier

**Whether the true value at `(8,5,4)` is 28 or 29 remains open in this estate.**

The source campaign records the following bounded negative evidence around the 28-word witness:

- zero free one-word extensions among all **13,764** outside candidates;
- a plateau walk visiting **45,702** distinct valid 28-codes to depth 6 with no zero-blocker extension;
- tabu search converging to conflict count 1 on four independent seeds and again at four times the iterations;
- complete single-swap repair failure;
- two-for-two repair covering **2,012,283** of roughly 94.7 million candidate pairs.

These searches are evidence about the local frontier, **not** an upper bound of 28.

## A useful implementation correction

A naive length-7 vertex generator gives 4,480 constant-GC words and therefore disagrees with the published graph size. The missing step is essential:

> A word whose distance to its **own** reverse complement is below `d` can never belong to the code and must be removed before the conflict graph is built.

For `(7,5,3)`, exactly 576 words fail this self-reverse-complement condition, leaving the correct 3,904 vertices.

## Reproducible material in this repository

`verify.py` independently checks the public 11-word witness and reconstructs the 4,480 -> 3,904 admissible-vertex count from the definition using only the Python standard library.

`provenance/divergent-mirror/` contains the exact small public mirror files from which this program was extracted.

## Provenance boundary

The small public mirror does **not** contain all original large solver outputs or every historical witness byte referenced by its audit. In particular, the full archived 28-word witness and the complete nine-shard upper-bound certificate are source-recovery obligations unless and until their original bytes are surfaced from the larger estate.

This repository therefore distinguishes:

- theorem/result statements that can be independently recomputed here;
- historical computations accurately reported by the recovered audit;
- certificate or witness bytes still awaiting canonical recovery.

No missing certificate is silently treated as present, and no bounded search is promoted into a proof of the 28-vs-29 frontier.
