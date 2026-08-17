---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Periodised Kernel"
  - "Def - Free Homotopy Class and Conjugacy Class Correspondence"
  - "Def - Subordinator and Subordination of a Semigroup"
tags: [paper, probability, topology, loop-measures]
---

# Notation

- $\alpha\in(0,2)$, $\phi(\lambda)=\lambda^{\alpha/2}$ — the running example: the $\alpha$-stable subordination, a pure-jump process
- $Y_u = B_{S_u}$ — the subordinate process, with $B$ a Brownian motion and $S$ an independent subordinator
- $(B,S)$ — the **marked** pair; the marked loop space is where the monodromy class is measurable
- $[\tau^m]_{\mathrm{conj}}$ — the conjugacy class; $p^{\mathcal{E}}_{\mathbb{H}^2}$ the upstairs kernel; $\rho_X$ the area measure on $X$
- $B|_{[S_{u^-},S_u]}$ — the Brownian segment deleted at a jump time $u$

---

# In plain language

For a pure-jump process, **a sample loop has no free homotopy class**, and the paper is honest about this rather than papering over it.

The reason is a hypothesis in the covering-space dictionary that is easy to forget: unique path lifting requires the path to be *continuous*. A càdlàg loop jumps, so it does not lift, so it records no deck transformation, so it belongs to no free homotopy class. The set $\mathcal{C}_X(\gamma^m)$, which for a diffusion is a measurable set of loops with a mass, is for a jump process not a subset of the càdlàg loop space at all.

The paper's response is to **define** the class mass by the formula that would be a theorem in the continuous case: restrict the [[Constr - The Periodised Kernel|periodisation]] to the conjugacy class. This is not arbitrary, and the justification is worth understanding, because it says exactly how much meaning the definition carries.

**Where the definition comes from.** Work on the space carrying the *pair* $(B,S)$ rather than on the time-changed path $Y$ alone. Condition on $S_t=s$. Then the term indexed by $h$ in the periodisation corresponds upstairs to a Brownian bridge from some $\tilde w$ to $h\tilde w$, and the projection of the **full Brownian arc** $B|_{[0,s]}$ is a genuine continuous loop with monodromy $h$, whose conjugacy class does not depend on the lift. The subordinator's only job is to decide which portions of that arc are observed. At a jump time $u$ the segment $B|_{[S_{u^-},S_u]}$ is deleted — but its *endpoints*, and hence the accumulated deck transformation, are unchanged. So restricting the periodisation to $[\tau^m]_{\mathrm{conj}}$ selects exactly the marked loops whose underlying Brownian arc lies in $\mathcal{C}_X(\gamma^m)$.

**What genuinely fails, and the open question.** The class is not recoverable from the càdlàg path alone: the deleted segments can be filled in by continuous paths whose projections have different monodromies, so two marked loops with the same $Y$ can carry different classes. The paper says it would be interesting to see an intrinsic geometrisation of a càdlàg loop — assigning a canonical continuous interpolation to each jump — but conjectures that no such scheme would preserve the closed-form mass formulas. That is a concrete open problem and it is recorded as such on [[Map - Brownian Loops on Homotopy and Homology Classes]].

---

# The construction

> **Definition (Remark 3.1 — loop mass in a homotopy class for jump processes).** Let $\alpha\in(0,2)$ and $\phi(\lambda)=\lambda^{\alpha/2}$, so that the subordinate process is the $\alpha$-stable one. Because it is purely discontinuous, a sample loop is a càdlàg map into $X$; it does not have a free homotopy class and does not admit a canonical lift via the path-lifting theorem. For jump processes one therefore **defines**
> $$\mu^{\mathcal{E}}_X\big(\mathcal{C}_X(\gamma^m)\big) := \int_0^\infty\frac{\mathrm{d}t}{t}\int_X\sum_{h\in[\tau^m]_{\mathrm{conj}}}p^{\mathcal{E}}_{\mathbb{H}^2}(t,\tilde z, h\tilde z)\,\mathrm{d}\rho_X(z),\tag{13}$$
> the part of the loop measure obtained by restricting the periodisation (11) to the conjugacy class $[\tau^m]_{\mathrm{conj}}$.

For a **continuous** process this is not a definition but a consequence: the lifting picture gives the bridge decomposition $W^{t,\mathcal{E}}_{z\to z,X}=\sum_{h\in\Gamma}\pi_*W^{t,\mathcal{E}}_{\tilde z\to h\tilde z,\mathbb{H}^2}$, which decomposes loops rooted at $z$ by the deck transformation their lifts record, so restricting to $\mathcal{C}_X(\gamma^m)$ *is* restricting the sum to $h\in[\tau^m]_{\mathrm{conj}}$. The content of (13) is that the same right-hand side is adopted as the left-hand side's meaning when the left-hand side has none.

---

# Type card

> [!abstract] Type card — Remark 3.1 (jump-process convention)
> **Given.** A pure-jump subordinate process on $X=\Gamma\backslash\mathbb{H}^2$, whose sample loops are càdlàg maps with no free homotopy class and no canonical lift; the periodised kernel (11); a primitive geodesic $\gamma$ with representative $\tau$ and a winding number $m\geq1$.
>
> **Produces.** A *definition* (13) of the number $\mu^{\mathcal{E}}_X(\mathcal{C}_X(\gamma^m))\in[0,\infty]$, agreeing with the measured quantity whenever the process is continuous.
>
> **Lets you.** State [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] and [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]] uniformly across diffusions and jump processes — at the explicit price that in the jump case the left-hand side is a definition, not a measured quantity.

---

# Properties relied on later

**Consistency with the continuous case.** For $\phi(\lambda)=\lambda$ and $\phi(\lambda)=\lambda+\kappa$ the process is a diffusion (with killing, which does not change the paths), so (13) is a theorem and not a convention. **Only the two stable cases are affected.** This is worth remembering when reading §3.1.3 and §3.1.4: the identity $\mu^\alpha_X=\tfrac\alpha2\mu_X$ is an identity between one measured quantity and one defined quantity.

**The marked-space interpretation.** Every statement about $\mu^\alpha_X(\mathcal{C}_X(\gamma^m))$ can be read as a statement about the process on the space carrying $(B,S)$, on which the monodromy class *is* measurable. This is what makes the convention meaningful rather than merely formal, and it is inherited by [[Thm - Poissonian Structure of Homotopy Classes|Proposition 3.8]]: when the process has jumps, the loop soup is taken to be the Poisson point process of **marked** loops, with the same intensity $c\,\mu^\phi_X(\mathcal{C}_X(\gamma^m))$ for the class.

**The failure is genuine, not technical.** The deleted segments can be filled by continuous paths of differing monodromy, so no amount of care recovers the class from $Y$. The paper's conjecture is that any canonical interpolation scheme would break the closed-form mass formulas (90) — that is, the tractability and the intrinsic geometrisation are in tension.

---

# Consumed by

- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]] — the theorem's statement covers jump processes by reading the left-hand side through (13); Step 1 of its proof branches on continuity, with the continuous branch using the bridge decomposition and the jump branch using (13) directly
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] — the $\alpha$-stable and shifted $\alpha$-stable instances are read through this convention
- [[Thm - Poissonian Structure of Homotopy Classes|Proposition 3.8]] — the marked loop soup
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1(iii)]] — the $\alpha$-stable determinant formula uses $\mu^\alpha_X=(\alpha/2)\mu_X$ on each homotopy-class term, which is an identity between a defined and a measured quantity
- [[Thm - Mass of the Subordinate Brownian Loop Measure on 3-Manifolds|Theorem 7.2]] — the same convention in three dimensions

---

# Where this sits in my DAG

Sits above [[Constr - The Periodised Kernel]] and [[Def - Free Homotopy Class and Conjugacy Class Correspondence]], and its whole content is the failure of one hypothesis on [[Def - Deck Transformations and the Lift of a Rooted Loop]] — namely that **unique path lifting requires continuity**. Tracing the dependency backwards is the cleanest way to see why the convention is needed: covering-space theory ([[Def - Covering Space]]) supplies path lifting for continuous paths only, and no version of it applies to càdlàg maps.

The probabilistic side — writing $Y_u=B_{S_u}$ on the space carrying the pair, and the fact that deleting a segment leaves its endpoints unchanged — reduces to [[Def - Subordinator and Subordination of a Semigroup]] and thence to anchors in *Advanced Probability* (🟢) and *SDEs* (🟢).
