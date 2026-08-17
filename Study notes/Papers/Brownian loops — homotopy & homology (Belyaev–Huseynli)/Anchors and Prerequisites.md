---
type: prereq-dag
paper: "BH26"
subject: brownian-loops
tags: [paper, prereqs, anchors, self-contained]
---

> [!info] Optional reference. The section pages are self-contained: every term is expanded down to the anchor set below, on the page. This page names that anchor set explicitly (so it can be sanity-checked), and — for a reader who wants to *close* the gaps rather than assume them — gives the backchain and a repair order. Part of [[Map - Brownian Loops on Homotopy and Homology Classes]].

# The anchor set — what the section pages assume you own

These come from the vault's `Study notes/Prerequisite DAG.md` (🟢 nodes, familiarity $\ge7$) and the owner's background in `CLAUDE.md`. Anything on this list is used on the section pages **without** expansion; everything else is expanded inline.

| anchor | what it covers here |
|---|---|
| 🟢 Advanced / measure-theoretic probability (7,9) | $\sigma$-finite measures, disintegration, Poisson point processes and the exponential formula, Fourier inversion on $\mathbb Z^r$ |
| 🟢 Functional analysis (8,10) | self-adjoint operators, semigroups, trace class, spectral theorem, Mellin/Laplace transforms, meromorphic continuation, abscissa of convergence, Pontryagin duality / Haar measure |
| 🟢 Analysis of PDEs | heat equation, heat kernels, short-time asymptotics |
| 🟢 SDEs / stochastic analysis (7,10) | Brownian motion, bridges, Feynman–Kac, Markov potential theory |
| 🟢 Linear algebra (7,7) | $\det(I-M)$, $\operatorname{tr}(M^m)$, class functions |
| 🟢 Complex analysis basics | infinite products, $-\log(1-x)=\sum x^m/m$, geometric series, principal $\sqrt{\cdot}$ |

> [!warning] Two calibration calls, stated not hidden
> **(1) Riemannian-geometry basics** are treated as an anchor (metric, geodesics, volume form, the $\mathbb H^2$/$\mathbb H^3$ models) on the strength of `CLAUDE.md`, though the DAG node is 🔵. **(2) Complex analysis** is 🔵 (4,7) and is the anchor most worth double-checking; if infinite products, meromorphic continuation, or finite parts of analytic families are unfamiliar, §4 and §5 are where to slow down. A wrongly-assumed anchor is the exact failure the self-contained design exists to prevent — if you hit an unexpanded term you don't know, it is a bug, report it.

---

# Backchain — every non-anchor term, and where it bottoms out

Each term below is expanded in full on the section page cited; here is only the reduction, so you can see the floor.

**§2.** loop measure → unnormalised bridge measure ($|W^t_{x\to y}|=p(t,x,y)$) → 🟢 heat kernel · $\mathrm dt/t$ shift-invariance → 🟢 probability · regular symmetric Dirichlet form → Markovian + closed + core → 🟢 functional analysis, via Fukushima (import) · Bernstein function / subordinator → Lévy–Khintchine triple → 🟢 probability · $V_\phi$, Lemma 2.11 → 🟢 Tonelli.

**§3.** covering-space unfolding → free + properly discontinuous action → 🔵 covering spaces (shallow; expanded inline) · centraliser $C_\Gamma(\tau^m)=\langle\tau\rangle$ → axis-preserving elements of a discrete torsion-free group → 🔵 abstract algebra (shallow; expanded inline) · fundamental region, standard form → elementary · **Wang–Xue strip identity** → **gap** (import 1) · $I_\phi$ evaluation → Gaussian reciprocal integral → 🟢 elementary · polar set → hitting probability zero → 🟢 potential theory · marked length spectrum, rigidity → **Otal–Croke** (gap, import 7).

**§4.** $\delta$ critical exponent → Poincaré-series abscissa → 🟢 abscissa of convergence; its geodesic-growth reading → **prime geodesic theorem** (gap, import 5) · $Z_X$, the $-\log Z_X$ expansion → 🟢 Euler products + geometric series · the criterion, killing verification → §3 mass + Gaussian reciprocal → 🟢.

**§5.** $\det_\zeta$ → $-\zeta_X'(0)$, Mellin, heat-trace short-time → 🟢 functional analysis · Selberg trace formula, Naud's formula → **gaps** (imports 4, 2) · Polyakov anomaly → **gap** (import 10) · continuous spectrum / Eisenstein series → 🟢 spectral theory · renormalised $0$-trace → **Melrose** (gap, import 8) · Borthwick–Judge–Perry → **gap** (import 3).

**§6.** $\mathbb P_s$, moments → 🟢 (derivatives of $\log Z_X$) · homology $H_1=\pi_1^{\mathrm{ab}}$ → 🔵 Hurewicz (shallow; expanded inline) · character torus, Selberg $L$ → 🟢 Pontryagin duality + the §4 machinery · Fourier inversion → 🟢 orthogonality of characters · loop-soup total homology → 🟢 exponential formula · Jacobian → **Hodge** (gap, import 12, decorative).

**§7.** Kleinian group, loxodromic complex length → 🔵 (expanded inline; the §3 geometry with a rotation) · $\mathbb H^3$ heat kernel → 🟢 classical (elementary in odd dimension) · slab identity → **derived**, no import · mass formula → Gaussian reciprocal at $a=1$ → 🟢.

---

# Suggested repair order (to close gaps rather than assume them)

1. **🔵 Algebraic topology** (covering spaces, Hurewicz) — shallow, unlocks §3 and §6.2 outright; highest-interest node (1,10). Already mostly expanded inline; a node would make it rigorous.
2. **🔵 Abstract algebra** (conjugacy, centralisers, cosets) — shallow, same §3 strand.
3. **🔵 Complex analysis** — closes calibration call (2); needed throughout §4–§6.
4. **🔵 Automorphic forms / Selberg trace formula** — the single highest-leverage node: closes imports **4, 5**, and half of **6** at once, hence most of §4–§5. Prereqs: modular forms, harmonic analysis, spectral theory, representation theory, Riemann surfaces.
5. **🔵 Spectral geometry** — closes Naud (2), Polyakov (10), and half of Borthwick–Judge–Perry (3).
6. **🔵 Riemann surfaces / Hodge theory** — closes uniformisation (11) and the Jacobian remark (12).

Everything else is one-result-deep and can be left as an honest import (see [[External Inputs and Gaps]]).

---

# What this paper unlocks downstream

| DAG node | what §-content feeds it |
|---|---|
| 🔵 GFF isomorphism theorems / loop soups | §3.3, §6.3 — the loop soup, its Poisson structure, the exponential formula |
| 🔵 Automorphic forms / Selberg trace formula | §4–§5 — every identity is a trace-formula consequence read probabilistically |
| 🔵 Spectral geometry | §5 — $\det_\zeta$, $\det_0$, Polyakov |
| 🔵 Algebraic topology | §3, §6.2 — covering spaces, free homotopy, $H_1$, in concrete use |
| 🔵 Random conformal geometry | §3.4 — restriction and conformal invariance of the loop measure |
