---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Differential k-Form on a Manifold"
  - "Def - Vector Bundle"
  - "Def - Determinant"
tags: [geometry, differential-geometry, integration, density]
---

# Notation

Throughout, $M$ is a smooth $n$-manifold ($n \geq 1$), *not necessarily orientable*. $V$ is a real $n$-dimensional vector space. The space of all multilinear functions $V^n \to \mathbb{R}$ is large; we will pick out specific subspaces by transformation rules under change of basis. Recall that for an $n$-covector $\omega \in \Lambda^n(V^*)$, the transformation under a linear map $A : V \to V$ is $\omega(Av_1, \ldots, Av_n) = (\det A)\,\omega(v_1, \ldots, v_n)$. The full notation registry is at [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

---

# Axiom Motivation

A top-degree form on an orientable manifold lets one integrate (top-forms, or functions multiplied by a volume form). But what if the manifold is *not* orientable — like the Möbius strip, $\mathbb{RP}^2$, or the Klein bottle? Then no top-form exists globally, and the form-based integration theory fails.

What goes wrong, precisely? At each point, the orientation line bundle $\Lambda^n(T^*M)$ has two "sides" (the two rays in the one-dimensional fiber); a globally consistent choice of side is what an orientation is, and on a non-orientable manifold no such choice exists. The local sides flip as one traverses certain loops — the holonomy that creates non-orientability.

The fix is to **forget the sides**. Instead of working with top-covectors $\omega$ (which transform by $\det A$ and so have signs that flip), work with the *absolute value* $|\omega|$ (which transforms by $|\det A|$, always positive). The absolute-value version has no sides — only magnitudes — and the holonomy that flipped signs in the orientable case simply has no effect on a quantity that does not carry a sign.

Concretely: define a **density** at a point $p$ to be a function $\mu_p : (T_pM)^n \to \mathbb{R}$ that is alternating (zero on linearly dependent tuples) and transforms by $\mu_p(Av_1, \ldots, Av_n) = |\det A|\,\mu_p(v_1, \ldots, v_n)$ under linear maps $A : T_pM \to T_pM$. This is *almost* an alternating multilinear form, except that the transformation rule has an absolute value, breaking strict linearity (a density is not linear in each input separately). A density carries the *magnitude* of "signed volume" but not the sign.

The space of densities at $p$ is one-dimensional (because by alternation, a density is determined by its value on one basis, and the transformation rule is consistent). The collection of one-dimensional density spaces at each $p$ assembles into a real line bundle $|\Lambda|^n(T^*M) \to M$, called the **density bundle**. A **density on $M$** is a section of this bundle.

**The key fact** that makes densities useful is that this bundle is *always trivial* — even when the orientation line bundle is not. The reason: the transition functions of the orientation line bundle are $\det(D\varphi_{\alpha\beta})$, which are real numbers with no constraint on sign; the transition functions of the density bundle are $|\det(D\varphi_{\alpha\beta})|$, always positive. Positive transition functions can always be trivialized (take logs, glue via partition of unity, exponentiate). So *every* smooth manifold admits a nowhere-vanishing density — even non-orientable ones.

This is the strategic content of densities: they trade the *sign* of integration (carried by orientation) for *existence* (carried by every manifold). On orientable manifolds you can have either — densities are absolute-value-of-top-forms, top-forms are oriented-densities. On non-orientable manifolds you can only have densities.

**Per-axiom failure analysis: what if we drop "alternating"?** Then we get a more general kind of "volume-like" object that does not vanish on degenerate inputs. This is too general — the volume of a parallelepiped *should* vanish when the vectors are linearly dependent. Alternation is essential.

**What if we drop the absolute value and use the signed determinant?** Then we get back top-forms, and the global existence is obstructed by orientability. This is fine on orientable manifolds; the point of densities is to handle the non-orientable case.

**What if we strengthen by demanding positivity, $\mu_p > 0$ for $\mu_p$ nonzero?** A density at $p$ is determined by its value on one basis, and that value can be positive or negative. The convention is that nonzero densities can be either positive or negative; *positive* densities form a convex cone. A "positive density" is sometimes called a **volume density** or **smooth measure**, and is the natural object for measure-theoretic constructions. The orientation-free analog of "positively-oriented volume form".

**What if we work over $\mathbb{C}$?** The complex analog is the **complex density bundle**, with transition functions $|\det|_{\mathbb{C}}^2 = \det\overline{\det}$. This is automatically trivial on every complex manifold. Most uses of densities are real, though.

---

# The Definition

Let $V$ be a real vector space of [[Def - Dimension|dimension]] $n \geq 1$.

**Density at a point (the algebraic version).** A **density** (of order 1) on $V$ is a function $\mu : V^n \to \mathbb{R}$ satisfying:
- (Alternation) $\mu(v_1, \ldots, v_n) = 0$ if $v_1, \ldots, v_n$ are linearly dependent.
- (Transformation rule) For any linear map $A : V \to V$,
$$\mu(Av_1, \ldots, Av_n) = |\det A|\,\mu(v_1, \ldots, v_n).$$

Denote the space of densities on $V$ by $|\Lambda|^n(V^*)$. It is a one-dimensional real vector space: given any basis $(e_1, \ldots, e_n)$, a density is determined by its value $\mu(e_1, \ldots, e_n) \in \mathbb{R}$, and this assignment is independent of the basis (different bases give consistent values via the transformation rule).

**Relation to top-forms.** Every nonzero top-covector $\omega \in \Lambda^n(V^*)$ determines a density $|\omega|$ by $|\omega|(v_1, \ldots, v_n) := |\omega(v_1, \ldots, v_n)|$. The map $\omega \mapsto |\omega|$ is two-to-one (since $|\omega| = |-\omega|$), with fibers being orientation-reversal pairs. On an oriented vector space, the map is a bijection between *positively-oriented* top-covectors and *positive* densities.

**Density bundle on a manifold.** The **density bundle** $|\Lambda|^n(T^*M) \to M$ is the real line bundle whose fiber over $p \in M$ is $|\Lambda|^n(T^*_pM)$. Its transition functions, in any smooth atlas, are $|\det D(\varphi_\beta\circ\varphi_\alpha^{-1})|$ — always positive. Consequently:

> The density bundle is **trivial** on every smooth manifold (orientable or not).

A **density on $M$** is a smooth section of $|\Lambda|^n(T^*M)$, i.e. a smooth map $\mu : M \to |\Lambda|^n(T^*M)$ assigning to each $p$ a density on $T_pM$, varying smoothly.

**Positive density / volume density.** A density $\mu$ on $M$ is **positive** if $\mu_p$ is a positive (i.e. positive on linearly-independent tuples) density on $T_pM$ for every $p$. Equivalently, $\mu$ takes positive values on every smooth local frame. Positive densities exist on every smooth manifold (use partition of unity to glue local Euclidean densities $|dx^1\wedge\cdots\wedge dx^n|$).

**Integral of a compactly supported density.** For a compactly supported density $\mu$ on a smooth $n$-manifold $M$ (orientable or not), the integral $\int_M\mu \in \mathbb{R}$ is defined chart-by-chart by the formula
$$\int_M\mu := \sum_i\int_{\varphi_i(U_i)} |a_i(x)|\,dx^1\cdots dx^n,$$
where $\{\psi_i\}$ is a partition of unity, $\psi_i\mu = a_i(x)\,|dx^1\wedge\cdots\wedge dx^n|$ in chart $(U_i, \varphi_i)$, and the right-hand side is the ordinary Riemann/Lebesgue integral. Well-definedness is automatic from the $|\det DF|$ transformation rule.

**Integration of functions.** Given a positive density $\mu$ on $M$ (which always exists), a compactly supported function $f \in C^\infty_c(M)$ is integrated via $\int_M f := \int_M f\mu$. This depends on $\mu$, but $\mu$ is canonical on a Riemannian manifold (the Riemannian density $|\omega_g|$).

---

# Categorical / Structural Definition

The density bundle $|\Lambda|^n(T^*M)$ is the **associated bundle** to the frame bundle $\mathrm{Fr}(M)$ via the homomorphism $\mathrm{GL}(n, \mathbb{R}) \to \mathbb{R}_{>0}$, $A \mapsto |\det A|$. This factors through $\mathrm{GL}(n, \mathbb{R})/\mathrm{GL}_+(n, \mathbb{R}) \cdot \mathrm{SL}(n, \mathbb{R})$, isomorphic to the positive reals, which is contractible — hence the associated bundle is trivial.

Compare with the orientation line bundle $\Lambda^n(T^*M)$, which is associated via $A \mapsto \det A$, factoring through $\det : \mathrm{GL}(n, \mathbb{R}) \to \mathbb{R}^*$ — and $\mathbb{R}^*$ has two connected components, giving the orientation $\mathbb{Z}/2$-obstruction.

**General densities of order $s \in \mathbb{R}$.** One can define $s$-densities by changing the transformation rule to $|\det A|^s$. The order-$1$ case is the integration-relevant one; order-$1/2$ densities appear in half-density quantization in mathematical physics; order-$0$ densities are just smooth functions (transformation by $|\det A|^0 = 1$).

---

# Relate to Other Fields / Compression

A density is the **orientation-blind version of a top-form** — the absolute-value version, transforming by $|\det DF|$ instead of $\det DF$. The compression: the top-form carries both magnitude and orientation; the density carries only magnitude. Throwing away orientation lets the density exist globally on every manifold, at the cost of losing the signed integration theory (no Stokes for densities, no oriented integration).

In **measure theory**, a positive density on $M$ induces a Borel measure $\mu_g(A) := \int_A\mu$, locally equivalent to Lebesgue measure (with Radon–Nikodým factor $\sqrt{\det g}$ in the Riemannian case). Densities are the differential-geometric formalism that makes "Lebesgue integration on a manifold" intrinsic.

In **mathematical physics**, half-densities ($s = 1/2$ densities) are the natural objects for *geometric quantization*: an "honest" wave function on a manifold is a half-density, because $\int_M|\psi|^2$ — the probability — needs an order-1 density, and $|\psi|^2$ is the square of a half-density. This is the orientation-free version of integration.

**True name:** A density is a section of the always-trivial density line bundle $|\Lambda|^n(T^*M)$ — equivalently, the absolute value of a top-form (on the orientable case) or its non-orientable generalization. This is the operational form: a density is "a top-form without signs".

---

# Examples / Corollaries

**Is an instance — $|dx^1\wedge\cdots\wedge dx^n|$ on $\mathbb{R}^n$.** The absolute value of the standard top-form. Integration against this density recovers the usual unsigned multiple Riemann integral. Equivalent to ordinary Lebesgue measure on $\mathbb{R}^n$.

**Is an instance — $|\omega_g|$ on a Riemannian manifold.** The Riemannian density: the absolute value of the Riemannian volume form. Always exists, on orientable or non-orientable Riemannian manifolds. Induces the natural Lebesgue-like Borel measure $\mu_g$ on $M$.

**Is an instance — densities on the Möbius strip.** The Möbius strip $E$ is non-orientable but admits a positive density: in any of its two chart covers, $|dx \wedge dy|$ is a density, and the transition $(x, y) \mapsto (x + 1, -y)$ has $|\det| = 1$, so the density glues consistently. The total density-integral $\int_E|dx\wedge dy|$ gives the area of the Möbius strip.

**Is an instance — densities on $\mathbb{RP}^n$ for $n$ even.** $\mathbb{RP}^{2k}$ is non-orientable but admits a positive density. With the round metric inherited from $S^{2k}$ via the antipodal quotient, the Riemannian density $|\omega_g|$ exists; its total integral is half the area of $S^{2k}$ (since $\mathbb{RP}^{2k}$ is a 2-to-1 quotient).

**Is an instance — Haar measure on a (not necessarily orientable) topological [[Def - Group|group]].** On any locally compact topological [[Def - Group|group]] $G$, the Haar measure is a left-invariant Radon measure unique up to scaling. For a Lie group with a left-invariant orientation, it is induced by the left-invariant volume form; in general, it is induced by a left-invariant *density*.

**Is NOT an instance — a top-form on the Möbius strip.** As established: no nowhere-vanishing 2-form exists on the Möbius strip, so no top-form integration. But the *density* $|dx\wedge dy|$ (the absolute value of a candidate top-form that would-fail-to-glue) does exist, because absolute values glue under sign-flipping transitions.

**Corollary — every smooth manifold admits a positive density.** Use partition of unity: each chart admits the standard density $|dx^1\wedge\cdots\wedge dx^n|$; multiply by $\psi_i$ and sum. The result is smooth, positive (on each chart, it is a positive combination of positives), and nowhere-vanishing.

**Corollary — a positive density induces a Borel measure.** For any positive density $\mu$ on a smooth manifold $M$, define $\mu(A) := \int_A\mu$ for measurable $A \subseteq M$. This is a regular Borel measure, locally finite, and locally equivalent to Lebesgue measure in any chart.

**Corollary — Stokes's theorem fails for densities.** Densities have no exterior derivative — there is no analog of $d$ on the density bundle that satisfies $\int_M d\mu = \int_{\partial M}\mu$. The reason: $d$ uses the signed structure of forms, which densities have discarded. So *one cannot do Stokes's theorem with densities*; this is the price of orientation-blindness.

**Calibration check.** Verify that the density bundle has positive transition functions $|\det DF|$ and is therefore trivial; that every smooth manifold admits a positive density via partition of unity; that the integral of a density depends on the choice of density (it is not intrinsic the way the integral of a top-form is — but it is well-defined for any *given* density); and that Stokes's theorem does not apply directly to densities. A complex structure canonically orients the underlying real manifold, but it does not select a density: a positive density requires additional data, such as a Hermitian metric.

---

# Unlocked by This

> [!tip] Integration on Non-Orientable Manifolds *(continued in this topic)*
> Densities allow integration of functions on non-orientable manifolds like the Möbius strip, $\mathbb{RP}^{2k}$, and the Klein bottle. The Riemannian density $|\omega_g|$ is the canonical choice on a Riemannian manifold of any orientability.

> [!tip] Half-Densities and Geometric Quantization *(from Mathematical Physics)*
> Half-densities (order-$1/2$, transforming by $|\det A|^{1/2}$) are the natural object for the inner product $\langle\psi, \phi\rangle = \int_M\overline\psi\phi$ in quantum mechanics on a manifold. This is the **geometric quantization** view: wave functions are sections of the half-density bundle, not just functions.

> [!tip] Haar Measure on a Locally Compact Group *(from Harmonic Analysis)*
> The Haar measure on a locally compact group $G$ is a left-invariant Radon measure. On a Lie group, it is induced by a left-invariant positive density (which always exists, even on non-orientable Lie groups, though those are rare).

> [!tip] Densities in Index Theory *(from Differential Geometry)*
> The Atiyah–Singer index theorem produces a density-valued local quantity on the manifold, integrated to give the index of an elliptic operator. The density structure is what makes the index a single number rather than something depending on orientation choices.
