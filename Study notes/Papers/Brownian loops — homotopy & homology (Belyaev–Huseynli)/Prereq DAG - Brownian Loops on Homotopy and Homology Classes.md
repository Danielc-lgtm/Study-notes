---
type: prereq-dag
paper: "BH26"
subject: brownian-loops
tags: [paper, dag, prerequisites]
---

> [!info] Companion to [[Map - Brownian Loops on Homotopy and Homology Classes]]

# Anchors this note-set backchains to

Nodes from `Study notes/Prerequisite DAG.md` with familiarity $\geq7$. Every leaf of the trees below is one of these, or is explicitly flagged as a gap.

| anchor | (fam, int) | what it covers here |
|---|---|---|
| 🟢 Advanced Probability / Measure-Theoretic | (7,9) | $\sigma$-finite measures, disintegration, Poisson point processes, Fourier inversion on $\mathbb{Z}^r$ |
| 🟢 Functional Analysis | (8,10) | self-adjoint operators, semigroups, trace class, spectral theorem, Mellin/analytic continuation |
| 🟢 Analysis of PDEs | — | heat equation, heat kernels, parabolic estimates |
| 🟢 SDEs | (7,10) | Brownian motion, bridges, Feynman–Kac, Markov potential theory |
| 🟢 Linear Algebra | (7,7) | $\det(I-M)$, $\mathrm{tr}(M^m)$, class functions |
| 🟢 ODEs | (8,8) | elementary integrals and asymptotics |

> [!warning] Two judgement calls, stated rather than hidden
> **(1) Riemannian geometry** is 🔵 in the DAG, but `CLAUDE.md` lists differential/Riemannian geometry among the owner's strong areas. It is treated as an **anchor** here: the metric, volume form, geodesics, and the upper half-plane/half-space models are used without backchaining.
> **(2) Complex analysis** is 🔵 (4,7) and is the anchor most worth double-checking. Used for: infinite products and their logarithms, meromorphic continuation, the principal branch of $\sqrt{\cdot}$, and (in §5) finite parts of analytic families. If any of these is unfamiliar, [[Def - Selberg Zeta Function]] and [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions]] are where to slow down.

---

# The backchain, by strand

## Strand 1 — the loop measure (§2)

```
Constr - The Brownian Loop Measure
├── Def - Unnormalised Bridge Measure by Disintegration
│   ├── Def - Transition Density and Heat Kernel
│   │   └── 🟢 Analysis of PDEs (heat kernel existence, short-time asymptotics)
│   └── 🟢 Advanced Probability (disintegration, regular conditional laws)
├── Def - The Space of Unrooted Unparametrised Loops
│   └── 🟢 Advanced Probability (path space, σ-algebras)
├── dt/t weight
│   └── Ext - Le Jan Shift-Invariance  →  🟢 Advanced Probability
└── 🟢 Riemannian Geometry (volume measure)                          [judgement call 1]

Constr - The Dirichlet-Form Loop Measure
├── Def - Regular Symmetric Dirichlet Form
│   └── 🟢 Functional Analysis (closed forms, semigroups)
└── Ext - Fukushima Correspondence                                   → 🟢 Functional Analysis + 🟢 SDEs
```

## Strand 2 — subordination (§2.3–2.4)

```
Constr - The Subordinate Brownian Loop Measure
├── Def - Bernstein Function
│   └── Ext - Lévy–Khintchine Representation for Bernstein Functions → 🟢 Advanced Probability
├── Def - Subordinator
│   └── 🟢 Advanced Probability (Lévy processes)
├── Constr - Assumption 2.3 (Strictly Increasing Subordinator)
├── Ext - Phillips Subordination of Semigroups and Dirichlet Forms   → 🟢 Functional Analysis
└── Constr - The Weighted Potential Measure Vϕ
    └── Thm - Collapsing the Time Integral into the Weighted Potential Measure
        └── 🟢 Advanced Probability (Fubini–Tonelli)
```

## Strand 3 — the geometry and the decomposition (§3)

```
Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces
├── Def - Fuchsian Group and the Quotient Surface
│   └── Def - Free and Properly Discontinuous Action
│       └── 🔵 Algebraic Topology (1,10) — covering spaces          [GAP, shallow]
├── Def - Deck Transformations and the Lift of a Rooted Loop
│   └── 🔵 Algebraic Topology — regular coverings, Galois correspondence  [GAP, shallow]
├── Def - Free Homotopy Class and Conjugacy Class Correspondence
├── Def - Centraliser and Coset Enumeration of a Conjugacy Class
│   └── 🔵 Abstract Algebra (3,8) — conjugacy, centralisers, cosets  [GAP, shallow]
├── Def - Fundamental Region  (clauses D1,D2; identities U, I, R)
├── Constr - The Periodised Kernel
└── Constr - Standard-Form Representative and the Fundamental Strip

Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces
├── Thm 3.2 (above)
├── Ext - Wang–Xue Strip Identity                                    [GAP — quoted]
├── Constr - The Weighted Heat-Kernel Integral Iϕ
└── Ext - Gaussian Reciprocal Integral Identity                      → 🟢 ODEs / elementary
```

## Strand 4 — zeta functions (§4)

```
Thm - Selberg Zeta Identity (Killing Case)
├── Thm - Selberg Zeta Criterion
│   └── Thm 3.5 (Strand 3)
├── Def - Selberg Zeta Function
│   ├── 🔵 Complex Analysis (4,7) — infinite products, logarithms   [judgement call 2]
│   └── Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions  [GAP]
└── Def - Critical Exponent
    └── 🔵 Automorphic Forms / Selberg Trace Formula                 [GAP]

Thm - Finiteness of the Total Mass
├── Ext - Prime Geodesic Theorem                                     [GAP]
├── Def - Systole
└── Thm - Selberg Zeta Criterion
```

## Strand 5 — determinants (§5)

```
Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)
├── Def - Zeta-Regularised Determinant of the Laplacian
│   └── 🟢 Functional Analysis (trace class, Mellin, continuation)
├── Ext - Selberg Trace Formula (Heat Kernel Form)                   [GAP]
├── Ext - Naud's Formula for the Log-Determinant                     [GAP — deepest of §5.1]
└── Ext - Prime Geodesic Theorem (refined form)                      [GAP]

Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)
├── Def - Eisenstein Series and the Continuous Spectrum
├── Def - Renormalised Integral and the 0-Trace
│   └── Ext - Melrose Renormalised Trace Expansion                   [GAP — no DAG node at all]
└── Ext - Borthwick–Judge–Perry Determinant Formula                  [GAP — deepest of §5.2]

Thm - Polyakov's Formula via Brownian Loop Measure
└── Ext - Polyakov Conformal Anomaly Formula                         [GAP, shallow]
```

## Strand 6 — probability and homology (§6)

```
Constr - The Probability Measure on Free Homotopy Classes
└── Thm - Selberg Zeta Identity (Killing Case) + Thm - Finiteness of the Total Mass

Thm - Fourier Expansion and Inversion by Homology Class
├── Def - Character Torus and the Pontryagin Dual
│   ├── 🔵 Algebraic Topology — Hurewicz, H₁ = π₁ᵃᵇ                  [GAP, shallow]
│   └── 🟢 Functional Analysis — Pontryagin duality, Haar measure
├── Def - Selberg L-Function  →  Thm - Selberg L-Function Identity
├── Constr - The Mass in a Homology Class
└── Ext - Orthogonality of Characters on a Compact Abelian Group     → 🟢 (not a gap)

Thm - Distribution of the Total Homology of the Loop Soup
├── Constr - The Loop Soup  →  Thm - Poissonian Structure of Homotopy Classes
└── Ext - Exponential Formula for Poisson Point Processes            → 🟢 Advanced Probability

Remark 6.6 only:
Def - The Jacobian as a Principally Polarised Abelian Variety
└── Ext - Hodge Theorem and the Period Lattice                       [GAP — decorative]
```

## Strand 7 — dimension 3 (§7)

```
Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds
├── Def - Kleinian Group and Loxodromic Complex Length               (Strand 3, verbatim)
├── Constr - Loxodromic Standard Form and the H3 Fundamental Slab
├── Thm - The H3 Fundamental-Slab Heat-Kernel Identity
│   └── Ext - Explicit Heat Kernel on Hyperbolic 3-Space             → 🟢 Analysis of PDEs
├── Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds
└── Ext - Gaussian Reciprocal Integral Identity (at a = 1)
```

---

# The gaps, ranked

Results imported without proof and with no anchor closing them. Each has an `Ext -` page giving preconditions, conclusion, and status, so all are usable on blind faith.

| gap | depth | DAG node that would close it | consequence if removed |
|---|---|---|---|
| [[Ext - Naud's Formula for the Log-Determinant\|(N)]] | deepest of §5.1 | 🔵 Automorphic Forms + 🔵 Spectral Geometry | all of §5.1 |
| [[Ext - Borthwick–Judge–Perry Determinant Formula\|(BJP)]] | deepest of §5.2 | 🔵 Spectral Geometry + microlocal | all of §5.2 |
| [[Ext - Melrose Renormalised Trace Expansion\|(M)]] | technical | **none exists** (b-calculus) | $\det_0$ ill-posed |
| [[Ext - Selberg Trace Formula (Heat Kernel Form)\|(STF)]] | structural | 🔵 Automorphic Forms / Selberg Trace Formula | (N), hence §5.1 |
| [[Ext - Prime Geodesic Theorem\|(PGT)]] | moderate | 🔵 Automorphic Forms / Selberg Trace Formula | Cor 4.7, hence §6's existence |
| [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions\|(MC)]] | moderate | 🔵 Automorphic Forms + 🔵 Spectral Geometry | §5's interpretation; **not** §4's identities |
| [[Ext - Wang–Xue Strip Identity\|(WX)]] | moderate | 🔵 Spectral Geometry / hyperbolic analysis | Thm 3.5, hence everything |
| [[Ext - Otal–Croke Marked Length Spectrum Rigidity\|(OC)]] | deep | **none exists** (Teichmüller theory) | Cor 3.12 only |
| [[Ext - Uniformisation of Punctured Hyperbolic Surfaces]] | moderate | 🔵 Riemann Surfaces | §3.4's length-spectrum identity |
| [[Ext - Hodge Theorem and the Period Lattice\|(HT)]] | shallow | 🔵 Hodge Theory, 🔵 Riemann Surfaces | Remark 6.6 only |
| [[Ext - Polyakov Conformal Anomaly Formula\|(P)]] | shallow | 🔵 Spectral Geometry / conformal geometry | Cor 5.4 only |
| [[Ext - Lawler–Werner Restriction and Conformal Invariance\|(LW)]] | shallow | 🔵 Random Conformal Geometry | §3.4 only |

**Not gaps** (inside an anchor, listed as `Ext -` only for interface clarity): [[Ext - Gaussian Reciprocal Integral Identity|(GI)]], [[Ext - Feynman–Kac Formula|(FK)]], [[Ext - Exponential Formula for Poisson Point Processes|(EF)]], [[Ext - Orthogonality of Characters on a Compact Abelian Group|(OC)]], [[Ext - Fukushima Correspondence]], [[Ext - Lévy–Khintchine Representation for Bernstein Functions]], [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms]], [[Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure]], [[Ext - Explicit Heat Kernel on Hyperbolic 3-Space]].

---

# What this paper unlocks downstream

| DAG node | what §-content feeds it |
|---|---|
| 🔵 GFF Isomorphism Theorems / Loop Soups | §3.3, §6.3 — the loop soup, its Poisson structure, the exponential formula |
| 🔵 Automorphic Forms / Selberg Trace Formula | §4–§5 — every identity is a trace-formula consequence read probabilistically |
| 🔵 Spectral Geometry | §5 — $\det_\zeta$, $\det_0$, Polyakov |
| 🔵 Algebraic Topology | §3, §6.2 — covering spaces, free homotopy, $H_1$, Hurewicz, in concrete use |
| 🔵 Riemann Surfaces / 🔵 Hodge Theory | §6.2 — Jacobian, period lattice |
| 🔵 Random Conformal Geometry | §3.4 — restriction and conformal invariance of the loop measure |
| 🔵 Abstract Algebra | §3 — conjugacy classes, centralisers, cosets, used non-trivially |

---

# Suggested repair order

If closing gaps rather than reading on faith:

1. **🔵 Algebraic Topology** (covering spaces, Hurewicz) — shallow, unlocks §3 and §6.2 outright, and is the highest-interest node (1,10).
2. **🔵 Abstract Algebra** (conjugacy, centralisers) — shallow, same strand.
3. **🔵 Complex Analysis** — closes judgement call 2, needed everywhere in §4–§6.
4. **🔵 Automorphic Forms / Selberg Trace Formula** — the single node that closes (STF), (PGT), (MC) at once, hence most of §4–§5.
5. **🔵 Spectral Geometry** — closes (N), (P), and half of (BJP).
6. Everything else is one-result-deep and can be left quoted.
