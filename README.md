# Constant-GC reverse-complement DNA codes

For words over `{A,C,G,T}^n`, fix GC-weight `w`, require pairwise Hamming distance at least `d`, and require the same distance from every reverse complement, including a word's own reverse complement.

Write `A_RC^GC(n,d,w)` for the maximum code size.

## Exact result: `A_RC^GC(7,5,3)=11`

The admissible conflict graph has:

- 4,480 length-7 words of GC-weight 3;
- 576 words excluded by the self-reverse-complement distance condition;
- **3,904 admissible vertices**;
- 3,945,728 conflict edges;
- exact independence number **11**.

One optimal code is

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

Every word has GC-weight 3. The minimum pairwise Hamming distance is 5, and the minimum distance from any codeword to the reverse complement of any codeword is also 5.

The upper-bound computation decomposes the graph into nine symmetry orbits of sizes

```text
1024, 768, 768, 384, 384, 384, 96, 48, 48
```

and solves the resulting exact clique subproblems.

## Length 8 frontier

A verified historical code gives

\[
A_{RC}^{GC}(8,5,4)\ge 28.
\]

The reconstructed conflict graph has 13,792 vertices and 72,209,664 edges.

A 29-word candidate was found with exactly one violation, the reverse-complement pair

```text
ACACACGA
TCGTGTGT
```

so the current unresolved question in this package is whether the exact value is 28 or 29.

Searches around the 28-word code found:

- no direct one-word extension among 13,764 outside candidates;
- 45,702 distinct valid 28-codes visited to depth 6 without an extension;
- repeated tabu searches reaching conflict count 1;
- no single-swap repair.

These are finite search results, not an upper bound of 28.

## Implementation detail

The self-reverse-complement filter is essential. Starting from all 4,480 constant-GC words and omitting this step gives the wrong graph. For `(7,5,3)`, exactly 576 words fail the self-distance requirement, leaving 3,904 valid vertices.

## Reproduce

[`verify.py`](verify.py) checks the public 11-word code and reconstructs the `4480 -> 3904` admissible-vertex count from the definition using only the Python standard library.

```bash
python verify.py
```

The complete historical nine-shard upper-bound outputs and the archived 28-word witness are not all present in the small recovered source mirror; the exact result statements above are separated from those still-missing archival bytes.

Author: Jared Wilder.
