# The mirror the search index cannot see

Author: Jared Wilder. First public timestamp: 2026-09-11.

A 32,081-file tree excluded from this estate's search index by construction, so no search has ever
returned a result from it. It is described internally as a divergent mirror. This is what is in it.

## The map

| | files | share |
|---|---|---|
| a built Mathlib `.lake` cache for a reproduction container | **27,836** | 86.8% |
| everything else | 4,244 | 13.2% |

Of the 4,244 real files, hashed path-for-path against the main tree:

| | files | share |
|---|---|---|
| byte-identical to the main tree | 1,863 | **43.9%** |
| same path, drifted bytes | 219 | 5.2% |
| **present only here** | **2,162** | **50.9%** |

**Roughly 44% stale duplicate, 56% genuine divergence — but only about 700 files carry
mathematics.** The rest of the unique content is service scaffolding and per-task engineering
receipts. Against the whole tree, unique content is 6.7%.

---

## A thirty-three minute search for a one-line theorem

The tree's crown is a family of sequenceability certificates: a set `A` in `Z_p \ {0}` is
*sequenceable* if its elements can be ordered so all partial sums are distinct and every proper
partial sum is nonzero.

One certificate's **witness bytes** exist only here: `Z_73` at size 72, the full nonzero group. Its
generator found it by simulated annealing:

```
61,532 restarts        1,845,089,701 anneal steps        1,981,048 ms  =  33 minutes
```

**It is an instance of a one-line theorem.** For any prime `p` with primitive root `g`, the ordering

```
g^1, g^2, g^3, ..., g^(p-1)
```

sequences the whole of `Z_p \ {0}`. The partial sums are `s_k = g(g^k - 1)/(g - 1)`, which are
distinct exactly when the `g^k` are, and vanish only when `(p-1) | k` — that is, only at the end.

**Verified here for all 61 odd primes below 300: zero failures.** At `p = 73` the primitive root is
5, the ordering begins `5, 25, 52, 41, 59, 3, 15, 2, 10, 50, ...`, all 72 partial sums are distinct,
and none is zero before the last.

**So every size-`(p-1)` row across all nine certificates is redundant.** The shipped `Z_73` ordering
has 47 distinct consecutive ratios, so it is not geometric — the search genuinely did not know.

The main tree *does* know the trick; it is recorded there under its own name with a date six days
before the annealing run. The mirror's generator, written earlier, does not — **and neither does the
main tree's own note on this closure**, which records the annealed result without observing that the
size-`(p-1)` case falls out in one line.

> **Corrected after publication.** This section first said the `Z_73` closure "exists only here",
> flagged as unconfirmed because a hash search across the main tree had not finished. It has now
> finished, and it resolves against that claim: **the result is ledgered in the main tree**, in a
> dated note carrying the same certificate hash `16281c7b...` and both verifier verdicts, which
> points at the erdosfire path as its source of truth. A second main-tree file names the same
> directory and marks it out of scope to touch.
>
> The accurate statement is narrower: **the witness bytes live only in the mirror; the result does
> not.** The two mirror copies of the certificate are byte-identical to each other and to the hash
> the main tree records.
>
> The eight-prime cross-check certificate genuinely lists only `{29, 31, 37, 41, 43, 47, 59, 61}`;
> `Z_73` is closed by that separate later note instead. And the `Z_29` certificate hash appears in
> the main tree only inside a search index, which is not a record — so that one is indexed but not
> ledgered.
>
> The primitive-root observation is unaffected and is now sharper: **both** the mirror's generator
> and the main tree's note missed it.

---

## What the certificates do establish

Published general results cover subsets of size at most 20. These close explicit finite gaps above
that, and **I re-verified every row from scratch: zero invalid witnesses, zero duplicate orbits.**

| p | sizes | orbit representatives | subsets covered |
|---|---|---|---|
| **29** | 21–28 | 60,134 | 1,683,218 |
| **31** | 21–30 | 765,548 | **22,964,087** |
| 37 | 29–36 | 298,344 | 10,739,176 |
| 41 | 34–40 | 114,998 | 4,598,479 |
| 43 | 36–42 | 148,157 | 6,220,768 |
| 47 | 40–46 | 237,372 | 10,917,020 |
| 59 | 54–58 | 7,885 | 456,838 |
| 61 | 56–60 | 8,738 | 523,686 |

Every per-size count equals the exact binomial `C(p-1, k)`. For `Z_29` the coverage is
`1184040 / 376740 / 98280 / 20475 / 3276 / 378 / 28 / 1`; for `Z_31`,
`14307150 / 5852925 / 2035800 / 593775 / 142506 / 27405 / 4060 / 435 / 30 / 1`.

**60,134 Lean witness theorems, kernel-checked, exist only in this mirror.** 470 shards, Lean 4.29.1
against a pinned Mathlib revision. Checked against the receipt rule: **all 470 shards return code 0,
every `stderr_tail` empty, and zero occurrences of `sorry` or `admit` in any shard.** 50,311 CPU
seconds. Cross-checked against the certificate: 60,134 member definitions, 60,134 orderings, 60,134
validity theorems, key sets identical, zero disagreements.

The mirror labels its own scope honestly: the Lean layer checks the witnesses, while orbit coverage
is checked outside Lean, and it records `terminalMathWin: false`.

### An exact stabilizer classification

Computed here, and not recorded anywhere in the tree. Orbit-size histograms under the `Z_p^x` action:

```
p=29   {28: 60098,  14: 33,  7: 1,  4: 1,  1: 1}
p=47   {46: 237282, 23: 89,  1: 1}
p=61   {60: 8720,   30: 15,  20: 1, 15: 1, 1: 1}
```

The structure is clean: a subset has stabilizer `H` exactly when its complement is a union of
`H`-cosets. The unique `p=61`, `|A|=56` representative with stabilizer of order 4 has complement
`{1, 11, 50, 60}`, which **is** the order-4 subgroup. The `|A|=57` one with stabilizer of order 3 has
complement `{14, 48, 60} = 14 · {1, 13, 47}`.

---

## A second mathematical line with no counterpart in the main tree

DNA codes: the largest code over `{A,C,G,T}^n` with GC-weight exactly `w`, pairwise Hamming distance
at least `d`, and distance at least `d` to every reverse complement including its own.

**An exact value, with the graph rebuilt from the definition.** For `(n,d,w) = (7,5,3)` the value is
**11**. Rebuilding the conflict graph from scratch: **3,904 vertices**, an exact match to the published
table, with 3,945,728 edges at density 0.5179.

The vertex count carries a filter worth stating, because a first re-implementation here got 4,480
and disagreed. There are 4,480 words of length 7 with GC-weight 3, but **576 of them sit within
distance 5 of their own reverse complement**, so they can never appear in any such code and are not
vertices at all. `4480 - 576 = 3904`. The 11-word witness verified: minimum pairwise
Hamming distance exactly 5, minimum distance to any reverse complement exactly 5, zero violations.

```
AACCCAA  CCGTTTA  GCAAGAT  CGTTCAT  GAGTAGT  CACATCT
CTTCAGA  GATCTTG  GTATCCA  TGACACT  TATTGCC
```

The upper bound comes from nine clique-solver shards over a nine-orbit decomposition under an
independently re-derived symmetry group of order 12,288 — orbit sizes
`1024, 768, 768, 384, 384, 384, 96, 48, 48`, summing to 3,904, each orbit times its stabilizer giving
12,288. The packet correctly calls this a reproduction by a faster route, not a discovery.

**A witness recovered from a dead web page.** `A(8,5,4) >= 28`, pulled from a Wayback snapshot of the
original author's page. Verified independently: 28 distinct words, all length 8, all GC-weight 4,
minimum pairwise Hamming 5, minimum reverse-complement distance 5, zero violations. The `n=8` graph
rebuilt here has **13,792 vertices and 72,209,664 edges, density 0.7593** — the edge count appears
nowhere in the packet.

**A 29-word near-miss with the obstruction pinned exactly.** Verified: 29 words, all weight 4, all
pairwise Hamming distances at least 5, and **exactly one violating pair** — `ACACACGA` and
`TCGTGTGT`, at reverse-complement distance 0, because they are exact reverse complements of each
other. Every one of the other 405 relations is clean.

The supporting negatives are bounded and labelled as such: zero free extensions from the historical
witness across all 13,764 outside candidates; a plateau walk visiting 45,702 distinct valid 28-codes
to depth 6 with no zero-blocker extension; tabu search converging to conflict-count 1 on four
independent seeds and again at four times the iterations; single-swap repair exhausting all
candidates; two-for-two repair covering 2,012,283 of roughly 94.7 million pairs.

**Whether the true value is 28 or 29 is open.**

---

## The most valuable negative in the tree

A symmetry-breaking constraint in a constraint solver reported **`provenOptimal, size = 14`** for a
case whose true optimum is **16**, already known.

It is unsound because it demands that a *different* group element canonicalize each clique vertex
independently, while the valid argument only supplies one group translate of the whole clique.

It was caught by contradiction with a known value, reverted, and written into the packet as a
standing rule: symmetry breaking may restrict only the outermost branch variable. Cold-start solver
runs are recorded as failures too — 900 seconds per shard producing bests of
`25, 25, 24, 24, 22, 23, 23`, all below the known 28.

A recorded unsoundness with the repair rule attached is worth more than the run that produced it.

## A cost model that breaks in both directions

An infeasibility finding rules a search range unreachable, correctly: the largest run ever completed
handled 22,964,087 raw subsets, and the target sizes are 13 to 20 orders of magnitude beyond that.
The exact binomial table is carried in full, peaking at `C(72,36) = 442,512,540,276,836,779,204`.

It then self-reports its own cost model failing. Fitted on nine runs at density between 0.718 and
1.0, the law `ms_per_orbit = 4278.42 · density^37.8066` predicts **about zero minutes** for one size
covering `7.7 x 10^17` subsets, and **about 3,475 years** for another covering `1.8 x 10^18` — a
*larger* count taking, by the model, essentially no time.

A steep power law extrapolated out of band is arbitrary in both directions, and the file says so.

## Solvers built and never run

Two exact adapters exist only here with no stored output anywhere. Their mathematics, computed here:

**Maximum sum-free subset of `{1,...,n}`** (no `x + y = z`, with `x = y` allowed), for `n = 1..24`:

```
1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12      = ceil(n/2) throughout
```

witness at `n = 18` being `{10, ..., 18}`.

**Largest 3-uniform family on `[u]` with no sunflower** (three sets whose pairwise intersections are
all equal). Run to exhaustion:

| u | triples | forbidden triples | **maximum** |
|---|---|---|---|
| 3 | 1 | 0 | **1** |
| 4 | 4 | **0** | **4** |
| 5 | 10 | 10 | **6** |
| 6 | 20 | 60 | **10** |
| 7 | 35 | 315 | **12** |
| 8 | 56 | — | **12** |
| 9 | 84 | — | **14** |

The adapter's own hard cap is `u <= 6`, so `u = 7, 8, 9` are past anything its code computes. Values
through `u = 6` recomputed here; the rest come from the exhaustive run.

**At `u = 4` there are no forbidden triples at all** — all four 3-subsets of a 4-set coexist, because
no three of them have equal pairwise intersections.

**The sequence plateaus at 12 across `u = 7` and `u = 8`**, then rises by two at `u = 9`. The eighth
point buys nothing and the ninth buys two. The reason is visible in the witness: the optimal family
at `u = 8` **lives entirely on seven points**, so the eighth is unused.

```
u = 8   {136, 137, 145, 147, 156, 235, 237, 245, 246, 267, 356, 467}
        12 sets, 0 sunflower triples, ground set {1,...,7}

u = 9   {057, 058, 067, 068, 127, 128, 134, 138, 147, 234, 238, 247, 567, 568}
        14 sets, 0 sunflower triples, ground set {0,...,8}

u = 6   {014, 015, 023, 025, 034, 123, 124, 135, 245, 345}
```

Both larger witnesses re-verified here from the definition: zero sunflower triples in each.

The value is still climbing at `u = 9`, so the unbounded maximum exceeds 14. **No literature value is
asserted for it.**

## Kernel-checked residue theorems, confirmed

Admissible residues for the prime pattern `(r, r+2, r+6)`. All six recomputed and matching:

```
mod 3   {2}
mod 5   {1,2}
mod 7   {2,3,4,6}
mod 11  {1,2,3,4,6,7,8,10}
mod 13  {1,2,3,4,5,6,8,9,10,12}
mod 17  {1,2,3,4,5,6,7,8,9,10,12,13,14,16}
```

Proved by `decide` in the kernel rather than by compiler-trusted decision, with `#print axioms` for
each — the stronger of the two available forms. The combined sieve leaves 8,960 surviving classes
modulo 255,255, density 0.0351.

## A finished paper that exists only here

A complete LaTeX source with compiled PDF, presenting the `Z_29` certificate with its symmetry lemma,
orbit table and dual-verifier argument. Its novelty audit is unusually disciplined: it states the
boundary of the prior computational literature, records the exact search queries it ran with their
date, and **explicitly refuses to convert a search failure into a priority claim.**

## Is it worth returning here

Once more, for the DNA-code line, which has no main-tree counterpart. That conclusion rests on the
path-level hash comparison rather than on a token search, so it is not affected by the `Z_73`
correction above.

The `Z_73` closure is **not** a reason to return: the result is already ledgered in the main tree,
and only its witness bytes sit here. After that the certificates are cross-checked into the main
ledger, and what remains is a 1.7 GB build cache plus a stale copy.

And the primitive-root observation is an action item, not a curiosity: it retires every size-`(p-1)`
row across all nine certificates.

## On absence

Statements here about what the main tree lacks rest on a byte-level path-mapped comparison and on
the main tree's own certificate enumerating eight primes.

The one claim flagged as unconfirmed on first publication — that the `Z_73` certificate was absent
from the main tree — **has since been resolved against itself** and is corrected above. That is the
intended behaviour of flagging it: an unfinished search was reported as unfinished rather than as an
absence, and when it completed it changed the claim.

## Verification

```bash
python verify.py
```

Standard library only.

## License

Apache-2.0.
