---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Dirichlet-Form Loop Measure"
  - "Constr - The Periodised Kernel"
  - "Constr - Standard-Form Representative and the Fundamental Strip"
  - "Def - Centraliser and Coset Enumeration of a Conjugacy Class"
tags: [paper, probability, hyperbolic-geometry, loop-measures]
---

# Notation

- $\Gamma\subset\mathrm{PSL}(2,\mathbb{R})$ — a torsion-free Fuchsian group; $X=\Gamma\backslash\mathbb{H}^2$; $\pi:\mathbb{H}^2\to X$
- $(\mathcal{E},\mathcal{F})$ — a $\Gamma$-invariant regular symmetric Dirichlet form on $L^2(\mathbb{H}^2,\rho)$ with kernel $p^{\mathcal{E}}_{\mathbb{H}^2}$ satisfying $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,w)=p^{\mathcal{E}}_{\mathbb{H}^2}(t,hz,hw)$ for $h\in\Gamma$
- $p^{\mathcal{E}}_X$ — the [[Constr - The Periodised Kernel|periodisation]] (11); $\mu^{\mathcal{E}}_X$ the associated loop measure
- $\gamma\in\mathcal{P}_X$ — a primitive closed geodesic of length $\ell_\gamma$; $\tau : z\mapsto e^{\ell_\gamma}z$ its [[Constr - Standard-Form Representative and the Fundamental Strip|standard-form]] representative
- $F_\tau=\{z\in\mathbb{H}^2 : 1\leq\operatorname{Im}(z)<e^{\ell_\gamma}\}$ — the fundamental strip; $F\subset\mathbb{H}^2$ a fundamental region for all of $\Gamma$
- $[\tau^m]_{\mathrm{conj}}$ — the conjugacy class of $\tau^m$; $\Gamma/\langle\tau\rangle$ its indexing cosets
- $W^{t,\mathcal{E}}_{z\to z,X}$, $W^{t,\mathcal{E}}_{\tilde z\to h\tilde z,\mathbb{H}^2}$ — bridge measures downstairs and upstairs; $\pi_*$ the pushforward
- $\rho_{\mathbb{H}^2}$, $\rho_X$ — hyperbolic area upstairs and downstairs

---

# Type card

> [!abstract] Type card — Theorem 3.2 (general homotopy class decomposition)
> **Given.** A $\Gamma$-invariant regular symmetric [[Def - Dirichlet Form and the Hunt Process Correspondence|Dirichlet form]] whose kernel [[Constr - The Periodised Kernel|periodises]]; a [[Def - Primitive Hyperbolic Element and Translation Length|primitive closed geodesic]] $\gamma\in\mathcal{P}_X$ with [[Constr - Standard-Form Representative and the Fundamental Strip|standard-form representative]] $\tau : z\mapsto e^{\ell_\gamma}z$ and fundamental strip $F_\tau$; a winding number $m\geq1$. For jump processes, the left-hand side is read through [[Constr - Loop Mass in a Homotopy Class for Jump Processes|Remark 3.1]].
>
> **Produces.** An identity between two numbers in $[0,\infty]$: the mass of the [[Constr - The Dirichlet-Form Loop Measure|Dirichlet-form loop measure]] in the free homotopy class $\mathcal{C}_X(\gamma^m)$ equals an explicit double integral over $(0,\infty)\times F_\tau$ of the *upstairs* kernel evaluated against a *single* group element $\tau^m$.
>
> **Lets you.** Compute a homotopy-class mass entirely on $\mathbb{H}^2$, against one group element, over an explicit horizontal band. Both the sum over $\Gamma$ and the quotient geometry of $X$ have been eliminated; what remains is a two-variable integral that an explicit heat kernel can discharge.

---

# Statement

> **Theorem 3.2 (general homotopy class decomposition for hyperbolic surfaces).** Let $\gamma\in\mathcal{P}_X$ be a primitive closed geodesic with hyperbolic representative $\tau$ as in (9) and winding number $m\geq1$. The mass of the Dirichlet form loop measure in the free homotopy class is
> $$\mu^{\mathcal{E}}_X\big(\mathcal{C}_X(\gamma^m)\big) = \int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,\tau^m z)\,\mathrm{d}\rho_{\mathbb{H}^2}(z).\tag{14}$$

---

# Why it is true

Two things collapse against each other, and the result is (14).

Start from what the class mass *is*. The loop measure is an integral over durations and basepoints of diagonal bridge measures; the kernel downstairs is a $\Gamma$-indexed sum; and by the [[Def - Free Homotopy Class and Conjugacy Class Correspondence|correspondence]] the terms of that sum indexed by $[\tau^m]_{\mathrm{conj}}$ are precisely the loops in $\mathcal{C}_X(\gamma^m)$. So the class mass is an integral over a fundamental region for $\Gamma$ of a sum over a conjugacy class. Both of those are large objects, and neither can be computed.

But they are *complementary* large objects. The conjugacy class is enumerated, one term per coset, by $\Gamma/\langle\tau\rangle$; and a fundamental region for $\Gamma$, translated by all the coset representatives and reassembled, is a fundamental region for $\langle\tau\rangle$. So the sum over the class can be traded, term by term, for an enlargement of the region: each coset representative $r$ moves its term onto the translated region $r^{-1}F$, and $\bigsqcup_r r^{-1}F$ is a fundamental region for the cyclic group. **One sum-over-a-class times one $\Gamma$-region equals one term times one $\langle\tau\rangle$-region.**

The last step is free. The integrand $z\mapsto p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,\tau^m z)$ is $\langle\tau\rangle$-invariant, since $\tau$ commutes with $\tau^m$ and the kernel is $\Gamma$-invariant; so its integral over any fundamental region for $\langle\tau\rangle$ is the same, and one may as well use the horizontal band $F_\tau$, where the geometry is explicit.

**The mechanism in one line: the conjugacy-class sum is exactly as big as the gap between a fundamental region for $\Gamma$ and one for the cyclic centraliser $\langle\tau\rangle$, so the two cancel and leave a single term on a band.**

---

# Strategy

**Strategy.** Unfold the conjugacy-class sum over the left cosets of the cyclic centraliser $\langle\tau\rangle$, using $\Gamma$-invariance of the kernel to move each coset representative onto the integration region; then replace the reassembled fundamental region for $\langle\tau\rangle$ by the strip $F_\tau$, which is legal because the integrand is $\langle\tau\rangle$-invariant.

> [!note]- Proof (skippable)
> **Step 1 — isolating the conjugacy class.** For a continuous process, the lifting picture gives the bridge decomposition
> $$W^{t,\mathcal{E}}_{z\to z,X} = \sum_{h\in\Gamma}\pi_*W^{t,\mathcal{E}}_{\tilde z\to h\tilde z,\mathbb{H}^2},\tag{15}$$
> which decomposes loops rooted at $z$ according to the deck transformation recorded by their lifts. Restricting to loops in $\mathcal{C}_X(\gamma^m)$ therefore corresponds to restricting the sum in the periodisation (11), with $\tilde z=\tilde w$, to $h\in[\tau^m]_{\mathrm{conj}}$. For a jump process this restriction is instead the definition (13) of [[Constr - Loop Mass in a Homotopy Class for Jump Processes|Remark 3.1]]. Either way,
> $$\mu^{\mathcal{E}}_X\big(\mathcal{C}_X(\gamma^m)\big) = \int_0^\infty\frac{\mathrm{d}t}{t}\int_X\sum_{h\in[\tau^m]_{\mathrm{conj}}}p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z,h\tilde z)\,\mathrm{d}\rho_X(z).\tag{16}$$
>
> **Step 2 — unfolding to the fundamental strip.** Let $F\subset\mathbb{H}^2$ be a fundamental region for $\Gamma$. Since $\int_X(\cdot)\,\mathrm{d}\rho_X=\int_F(\cdot)\,\mathrm{d}\rho_{\mathbb{H}^2}$, the right-hand side of (16) becomes
> $$\int_0^\infty\frac{\mathrm{d}t}{t}\int_F\sum_{h\in[\tau^m]_{\mathrm{conj}}}p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,hz)\,\mathrm{d}\rho_{\mathbb{H}^2}(z).\tag{17}$$
>
> Now unfold the sum over the conjugacy class using the coset enumeration (10). For each coset representative $r\in\Gamma/\langle\tau\rangle$, $\Gamma$-invariance of the heat kernel gives
> $$p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,r\tau^m r^{-1}z) = p^{\mathcal{E}}_{\mathbb{H}^2}(t,r^{-1}z,\tau^m r^{-1}z),$$
> and the substitution $w=r^{-1}z$ — an isometry, so it preserves $\rho_{\mathbb{H}^2}$ — gives
> $$\int_F p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,r\tau^m r^{-1}z)\,\mathrm{d}\rho_{\mathbb{H}^2}(z) = \int_{r^{-1}F}p^{\mathcal{E}}_{\mathbb{H}^2}(t,w,\tau^m w)\,\mathrm{d}\rho_{\mathbb{H}^2}(w).$$
> Summing over the coset representatives,
> $$\sum_{r\in\Gamma/\langle\tau\rangle}\int_{r^{-1}F}p^{\mathcal{E}}_{\mathbb{H}^2}(t,w,\tau^m w)\,\mathrm{d}\rho_{\mathbb{H}^2}(w) = \int_{\bigsqcup_r r^{-1}F}p^{\mathcal{E}}_{\mathbb{H}^2}(t,w,\tau^m w)\,\mathrm{d}\rho_{\mathbb{H}^2}(w).\tag{18}$$
>
> Since $F$ is a fundamental region for $\Gamma$ and $\Gamma=\bigsqcup_r r\langle\tau\rangle r^{-1}$ in the relevant sense, the union $\bigsqcup_r r^{-1}F$ is a fundamental region for $\langle\tau\rangle$. Moreover $\tau$ commutes with $\tau^m$ and the kernel is $\Gamma$-invariant, so $z\mapsto p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,\tau^m z)$ is $\langle\tau\rangle$-invariant, and its integral over any fundamental region of $\langle\tau\rangle$ is the same. Replacing the union by the strip $F_\tau$ of (12) gives
> $$\mu^{\mathcal{E}}_X\big(\mathcal{C}_X(\gamma^m)\big) = \int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,\tau^m z)\,\mathrm{d}\rho_{\mathbb{H}^2}(z).\qquad\square$$

---

# What this assumes, and where to climb

Four hypotheses, and it is worth walking them because each fails differently.

**A loop measure to take the mass of** — [[Constr - The Dirichlet-Form Loop Measure]]. Without $\sigma$-finiteness there is no measure; without the shift-invariance of the rooted measure there is no pushforward to $\mathcal{C}_X$.

**The periodisation, with $\Gamma$-invariance** — [[Constr - The Periodised Kernel]]. This does two separate jobs and both are essential. It makes the downstairs kernel a $\Gamma$-indexed sum, so that a topological restriction is available at all. And in Step 2 it supplies $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,r\tau^m r^{-1}z)=p^{\mathcal{E}}_{\mathbb{H}^2}(t,r^{-1}z,\tau^m r^{-1}z)$, without which no coset representative can be moved onto the region and the unfolding does not start.

**The coset enumeration** — [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]]. The conjugacy class must be listed **without repetition**, and the enumeration must be by $\Gamma/\langle\tau\rangle$ with $\tau$ *primitive*. Listing by $\Gamma/\langle\tau^m\rangle$ instead would over-count by a factor $m$ and destroy the $1/m$ that later becomes a logarithm and hence the Selberg zeta function.

**The standard form and the strip** — [[Constr - Standard-Form Representative and the Fundamental Strip]]. Not needed for correctness of the unfolding, only for the *explicitness* of the answer: the theorem would be true with any fundamental region for $\langle\tau\rangle$, but only $F_\tau$ makes the next step, [[Thm - The Wang–Xue Fundamental-Strip Identity|Lemma 3.4]], possible.

**And for jump processes**, the left-hand side is [[Constr - Loop Mass in a Homotopy Class for Jump Processes|a definition]], not a measured mass. Step 1 branches here: for a diffusion the identity (16) is derived from the bridge decomposition (15); for a jump process it *is* (13).

---

# What consumes this

- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] — starts from (14) with $p^{\mathcal{E}}_{\mathbb{H}^2}=p^\phi_{\mathbb{H}^2}$, expands via (6), and discharges the two integrals in turn
- [[§3 Decomposition over Homotopy Classes]] — the section's central result
- [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds|Theorem 7.1]] — the proof is described in the paper as "identical in structure", with the loxodromic standard form (82) in place of (9); reading this proof is reading that one

---

# Reading it against the rest of the paper

This is one of the three proofs worth reading in full, and the reason is that the unfolding move is the *only* structural argument in the paper. Everything else is either an explicit integral, a substitution into a known formula, or a citation. If you internalise the exchange "conjugacy-class sum $\leftrightarrow$ enlargement of the fundamental region", you have the geometric content of both §3 and §7.

The move is not specific to loop measures. It is the standard device by which a sum over a conjugacy class in the [[Def - Critical Exponent and the Prime Geodesic Theorem|Selberg trace formula]] is turned into an integral over a cylinder — the same unfolding, applied to $\int_X p_X(t,z,z)\,\mathrm{d}\rho_X$ rather than to a single class. Seeing Theorem 3.2 as one term of the trace formula's geometric side, isolated, is the right way to place it: §5 will need the whole trace formula, and this theorem is what one term of it looks like.
