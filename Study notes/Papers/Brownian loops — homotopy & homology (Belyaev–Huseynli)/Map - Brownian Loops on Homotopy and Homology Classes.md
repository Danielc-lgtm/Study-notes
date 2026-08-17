---
type: map
paper: "BH26"
subject: brownian-loops
tags: [paper, map, loop-measures, zeta-functions]
---

# What this paper does

Belyaev–Huseynli, *A probability measure on homotopy & homology classes via Brownian loops*. The Brownian loop measure on a hyperbolic surface $X=\Gamma\backslash\mathbb{H}^2$ is decomposed over **free homotopy classes**; each class turns out to carry an explicit finite mass, the sum of these masses over all non-trivial classes is exactly $-\log Z_X(s)$ for the Selberg zeta function, and dividing by that sum gives a canonical probability measure on free homotopy classes whose moments are derivatives of $\log Z_X$. The same total mass is the regularised $\log\det\Delta_X$; grouping by **homology** instead and twisting by unitary characters produces Selberg $L$-functions and, via the loop soup, the exact law of the total homology of infinitely many Brownian loops. A final section reruns the construction on hyperbolic $3$-manifolds, where everything transfers except the zeta identity.

---

# Global signature

| symbol | type |
|---|---|
| $X$ | $=\Gamma\backslash\mathbb{H}^2$ geometrically finite hyperbolic surface (§7: $\Gamma\backslash\mathbb{H}^3$) |
| $\mathcal{P}_X$ | primitive **oriented** closed geodesics $\leftrightarrow$ primitive hyperbolic conjugacy classes |
| $\ell_\gamma$ | $\in(0,\infty)$ translation length; §7: $L_\gamma=\ell_\gamma+i\theta_\gamma\in\mathbb{C}$ |
| $\mathcal{C}_X(\gamma^m)$ | the free homotopy class of $\gamma^m$; $(\gamma,m)\in\mathcal{P}_X\times\mathbb{Z}_{\geq1}$, **unique** per class |
| $L$ | $=m\ell_\gamma$ throughout §3–§6 (real); $=mL_\gamma$ in §7 (complex) |
| $\mu_X$ | Brownian loop measure; $\mu^\kappa_X$ with killing $\kappa$; $\mu^\phi_X$ subordinate by $\phi$; $\mu^E_X$ Dirichlet-form |
| $\phi$ | a Bernstein function; $V_\phi$ its weighted potential measure on $(0,\infty)$ |
| $\kappa$ | killing rate, $\geq-\tfrac14$ |
| $s$ | spectral parameter, $=\tfrac12+\sqrt{\tfrac14+\kappa}$ $\iff$ $\kappa=s(s-1)$ |
| $\delta$ | $\in(0,1]$ critical exponent; $\delta=1\iff\mathrm{area}(X)<\infty$ |
| $Z_X,L_X(\cdot,\chi)$ | Selberg zeta and $L$-function, $\mathrm{Re}(s)>\delta$ |
| $\mathbb{P}_s$ | the probability measure on free homotopy classes |
| $\mathcal{L}_\lambda$ | the loop soup of intensity $\lambda$; $\beta(\lambda)$ its total homology |

> **Conventions.** $\Delta_X$ is the **positive** Laplacian. *Total mass* always means the sum over non-trivial non-peripheral classes. $s$ is the spectral parameter in §4–§6 and the **subordination time** in §2 and §7 — the sections do not overlap. Never a LaTeX symbol inside a wikilink.

---

# The one identity

Everything in §4–§6 is this, read in different directions:

$$\underbrace{\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac1m\cdot\frac{e^{(1-s)L}}{e^{L}-1}}_{\text{§3, one class}}\qquad\Longrightarrow\qquad\underbrace{\sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq1}\mu^\kappa_X\big(\mathcal{C}_X(\gamma^m)\big)=-\log Z_X(s)}_{\text{§4, all classes}}$$

with $L=m\ell_\gamma$ and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$. The right-hand side is the logarithmic expansion of the Selberg Euler product, term for term. §5 says the same number is $\log\det\Delta_X$; §6.1 divides by it; §6.2–§6.3 twist it by characters; §7 shows dimension $3$ breaks its shape.

---

# Type index

Every result the paper states, with what it consumes and what it yields.

## §2 — construction

| result | Given | Produces |
|---|---|---|
| [[Constr - The Brownian Loop Measure]] | heat kernel, bridge measures, $\mathrm{d}t/t$, $\mathrm{d}\mathrm{vol}_g$ | a $\sigma$-finite measure on unrooted unparametrised loops |
| [[Constr - The Dirichlet-Form Loop Measure]] | a regular symmetric Dirichlet form | the same, for a general symmetric Markov process |
| [[Constr - The Subordinate Brownian Loop Measure]] | $\phi$ Bernstein, Assumption 2.3 | $\mu^\phi_X$, with a transition density |
| [[Thm - Collapsing the Time Integral into the Weighted Potential Measure]] | $h\geq0$ measurable, Assumption 2.3 | $\int_0^\infty\frac{\mathrm{d}t}{t}\int h\,\mathrm{d}\psi^\phi_t=\int h\,\mathrm{d}V_\phi$ — **Lemma 2.11** |

## §3 — decomposition

| result | Given | Produces |
|---|---|---|
| [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] | $\Gamma$ Fuchsian torsion-free, $\tau$ in standard form | $\mu^E_X(\mathcal{C}_X(\gamma^m))=\int\frac{\mathrm{d}t}{t}\int_{F_\tau}p^E_{\mathbb{H}^2}(t,w,\tau^mw)$ — **Thm 3.2** |
| [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] | Thm 3.2, (WX), Lemma 2.11 | $\mu^\phi_X(\mathcal{C}_X(\gamma^m))=\frac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)$ — **Thm 3.5**; killing case $\frac1m\frac{e^{(1-s)L}}{e^L-1}$ |
| [[Thm - Poissonian Structure of Homotopy Classes]] | the loop soup; disjointness of classes | Poisson counts, jointly independent — **Prop 3.8** |
| [[Thm - Loop Masses Determine the Marked Length Spectrum]] | the masses, all classes | $\ell_\gamma=\log(1+1/\mu_X(\mathcal{C}_X(\gamma)))$; monotone for $\kappa$ — **Prop 3.11** |
| [[Thm - Loop Masses Determine the Hyperbolic Surface]] | equal masses for two metrics | same point of Teichmüller space — **Cor 3.12** |

## §4 — zeta identities

| result | Given | Produces |
|---|---|---|
| [[Thm - Selberg Zeta Criterion]] | $\frac{L}{2\sinh(L/2)}I_\phi(L)=C\frac{e^{(1-s)L}}{e^L-1}$, $C,s$ free of $L$ | total mass $=-C\log Z_X(s)$ — **Lemma 4.2** |
| [[Thm - Selberg Zeta Identity (Killing Case)]] | $\kappa\geq-\tfrac14$, $s>\delta$ | $\sum_{\gamma,m}\mu^\kappa_X=-\log Z_X(s)$ — **Cor 4.3** |
| [[Thm - Twisted Ruelle Zeta Identity]] | $\rho$ finite-dimensional, $\mathrm{Re}(s)>\max(c_\rho,\tfrac12)$ | $-\log R_X(s,\rho)$ as a **difference** of two loop measures — **Cor 4.6** |
| [[Thm - Finiteness of the Total Mass]] | $s(\phi)>\delta$ | total mass finite; and divergent iff $s\leq\delta$ — **Cor 4.7** |

## §5 — determinants

| result | Given | Produces |
|---|---|---|
| [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]] | $X$ closed, Naud's formula | $\log{\det}_\zeta\Delta=\mathrm{Area}(X)E+\log Z_X'(1)$ — **Thm 5.1** |
| [[Thm - Polyakov's Formula via Brownian Loop Measure]] | $g=e^{2\sigma}g_{\mathrm{hyp}}$, (P) | the determinant for **every** metric in the conformal class — **Cor 5.4** |
| [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)]] | $n_C$ cusps, (BJP) | $\log\det_0\Delta_X=\log C_X+\log Z_X'(1)$ — **Thm 5.7** |

## §6 — probability

| result | Given | Produces |
|---|---|---|
| [[Constr - The Probability Measure on Free Homotopy Classes]] | Cor 4.3 + Cor 4.7 | $\mathbb{P}_s$, normalising constant $-\log Z_X(s)$ |
| [[Thm - Moments of the Length via the Selberg Zeta Function]] | $\mathbb{P}_s$; $F=-\log Z_X$ | $\mathbb{E}_s[L^n]=(-1)^nF^{(n)}/F$; $\mathbb{E}_s[e^{-rL}]=\log Z_X(s+r)/\log Z_X(s)$ |
| [[Thm - Concentration on Systolic Classes]] | $s\to\infty$ | uniform on the $N_{\mathrm{sys}}$ systolic classes; $\ell_{\mathrm{sys}},N_{\mathrm{sys}}$ recoverable from $Z_X$ |
| [[Thm - Selberg L-Function Identity]] | $\chi$ unitary | $-\log L_X(s,\chi)=\sum_{\gamma,m}\chi([\gamma])^m\mu^\kappa_X$ — **Cor 6.4** |
| [[Thm - Fourier Expansion and Inversion by Homology Class]] | Cor 6.4, orthogonality | $\mu^\kappa_X(\beta)=\int_{\widehat{H_1}}(-\log L_X(s,\chi))\overline{\chi(\beta)}\,\mathrm{d}\chi$ — **Thm 6.5** |
| [[Thm - Distribution of the Total Homology of the Loop Soup]] | the soup, (EF), Cor 6.4 | $\mathbb{E}[\chi(\beta(\lambda))]=(Z_X/L_X)^\lambda$; the full law — **Prop 6.7** |

## §7 — dimension 3

| result | Given | Produces |
|---|---|---|
| [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds]] | $\Gamma$ Kleinian torsion-free | (85), the slab decomposition — **Thm 7.1** |
| [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity]] | the explicit $\mathbb{H}^3$ kernel | (88),(89), **proved here** not imported |
| [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds]] | (88), Lemma 2.11 | (90) — **Thm 7.2** |
| [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds]] | (90), (GI) at $a=1$ | $\mu_X(\mathcal{C}_X(\gamma^m))=\frac1m\lvert e^{mL_\gamma}-1\rvert^{-2}$ — **Cor 7.3** |

---

# Imported results

Full status on each `Ext -` page. Ranked by how much collapses without it.

| import | used at | genuine gap? |
|---|---|---|
| [[Ext - Wang–Xue Strip Identity\|(WX)]] | Thm 3.5 — hence everything | **yes** |
| [[Ext - Naud's Formula for the Log-Determinant\|(N)]] | all of §5.1 | **yes** |
| [[Ext - Borthwick–Judge–Perry Determinant Formula\|(BJP)]] | all of §5.2 | **yes** |
| [[Ext - Selberg Trace Formula (Heat Kernel Form)\|(STF)]] | (N) | **yes** |
| [[Ext - Prime Geodesic Theorem\|(PGT)]] | Cor 4.7, §5.1 | **yes** |
| [[Ext - Melrose Renormalised Trace Expansion\|(M)]] | $\det_0$ well-posed | **yes** (no DAG node at all) |
| [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions\|(MC)]] | §5's interpretation | **yes**, not load-bearing in §4 |
| [[Ext - Otal–Croke Marked Length Spectrum Rigidity\|(OC)]] | Cor 3.12 only | **yes** (no DAG node) |
| [[Ext - Uniformisation of Punctured Hyperbolic Surfaces]] | §3.4 | **yes** |
| [[Ext - Polyakov Conformal Anomaly Formula\|(P)]] | Cor 5.4 only | yes, shallow |
| [[Ext - Lawler–Werner Restriction and Conformal Invariance\|(LW)]] | §3.4 only | yes, shallow |
| [[Ext - Hodge Theorem and the Period Lattice\|(HT)]] | Remark 6.6 only | yes, decorative |
| [[Ext - Gaussian Reciprocal Integral Identity\|(GI)]] | **six** times, §3 and §7 | no |
| [[Ext - Feynman–Kac Formula\|(FK)]], [[Ext - Exponential Formula for Poisson Point Processes\|(EF)]], [[Ext - Orthogonality of Characters on a Compact Abelian Group\|(OC)]], [[Ext - Fukushima Correspondence]], [[Ext - Lévy–Khintchine Representation for Bernstein Functions]], [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms]], [[Ext - Le Jan Shift-Invariance of the Parametrised Loop Measure]], [[Ext - Explicit Heat Kernel on Hyperbolic 3-Space]] | throughout | no — inside anchors |

---

# Reading orders

**Fastest path to the main theorem (≈8 pages).**
[[Constr - The Brownian Loop Measure]] → [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces]] → [[Ext - Wang–Xue Strip Identity]] (accept) → [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] → [[Def - Selberg Zeta Function]] → [[Thm - Selberg Zeta Criterion]] → [[Thm - Selberg Zeta Identity (Killing Case)]] → [[Constr - The Probability Measure on Free Homotopy Classes]].

**Typecheck path (verify every step).** Read the sections in order: [[§2.1–2.2 Loop Measures — Brownian and Dirichlet Form]] → [[§2.3–2.4 Subordination and the Weighted Potential Measure]] → [[§3 Decomposition over Homotopy Classes]] → [[§4 Zeta Identities and Finiteness of the Total Mass]] → [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] → [[§6 Probability Measures on Homotopy and Homology Classes]] → [[§7 Brownian Loops on Hyperbolic 3-Manifolds]]. Each section page ends with numbered **Exports** (E1)…(En) that are the only things later sections use.

**Probabilist's path.** §2 → §3 → [[§3.3 The Loop Soup and its Poissonian Structure]] → §6. Skip §4.2, §5 entirely; accept $\sum_{\gamma,m}\mu^\kappa_X=-\log Z_X(s)$ as a definition of $Z_X$.

**Spectral geometer's path.** [[Def - Schwinger Proper-Time Representation]] → [[Def - Selberg Zeta Function]] → §4 → §5. §3 is then just "where the mass formula comes from".

**Skippable without loss.** [[§3.2 Euclidean Quantum Mechanics and the Path Integral]] (a digression, cited by nothing), [[Thm - Twisted Ruelle Zeta Identity]] (stated, then abandoned), [[Def - The Jacobian as a Principally Polarised Abelian Variety]] (Remark 6.6 only).

---

# Open questions the paper leaves

1. **Dimension 3 has no zeta identity.** $\frac1m\lvert e^{mL_\gamma}-1\rvert^{-2}$ is not of the shape [[Thm - Selberg Zeta Criterion|Lemma 4.2]] requires — squared modulus, complex length. No total mass, no probability measure, no determinant formula in §7. A holonomy-twisted Selberg zeta for Kleinian groups is the natural candidate and is not pursued. **The most concrete gap.**
2. **Which mass functions arise?** [[Thm - Loop Masses Determine the Hyperbolic Surface|Cor 3.12]] shows $\mathcal{T}(X)\to\{$mass functions$\}$ is injective; its image is not characterised.
3. **Geodesic intersections.** The stated motivation for $\mathbb{P}_s$ — computing intersection probabilities of random classes — is not carried out.
4. **General Bernstein $\phi$.** Only four $\phi$ satisfy the criterion (33). For a general one the total mass is simply not a zeta value, and nothing is said about what it is.
5. **Non-compact Jacobian analogue.** Remark 6.6 needs closedness; partial analogues are said to exist and are not invoked.

---

# Also here

- [[Prereq DAG - Brownian Loops on Homotopy and Homology Classes]] — the backchain to anchors, the gap ranking, and a suggested repair order.
