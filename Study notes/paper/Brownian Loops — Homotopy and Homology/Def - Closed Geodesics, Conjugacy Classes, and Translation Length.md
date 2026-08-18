---
type: definition
subject: geometry
prereqs:
  - "Def - Fuchsian Group and the Hyperbolic Quotient Surface"
tags: [geometry, hyperbolic-geometry, group-theory, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$X=\Gamma\backslash\mathbb{H}^2$ a hyperbolic surface with torsion-free [[Def - Fuchsian Group and the Hyperbolic Quotient Surface|Fuchsian group]] $\Gamma$; $\pi:\mathbb{H}^2\to X$ the covering. A **free homotopy class** of an oriented closed curve is the set of oriented closed curves deformable into one another (with no fixed basepoint). $[h]_{\mathrm{conj}}=\{ghg^{-1}:g\in\Gamma\}$ the conjugacy class of $h\in\Gamma$; $C_\Gamma(h)=\{g:gh=hg\}$ its centraliser.

---

# Axiom Motivation

The paper sorts loops by *which hole they wind around and how many times* — their free homotopy class. To compute with these classes one needs a bookkeeping device, and hyperbolic geometry supplies a perfect one: **free homotopy classes of oriented closed curves on $X$ correspond exactly to conjugacy classes in $\Gamma$**, and each nontrivial class contains a **unique closed geodesic** whose length is a group-theoretic invariant (the translation length). This dictionary is what turns a topological/geometric question ("mass of loops winding around this handle") into an algebraic one ("sum over a conjugacy class"), which §3 then evaluates.

Two facts make the dictionary work. First, a loop upstairs lifts to an *arc* whose two endpoints differ by a deck transformation $h\in\Gamma$ (the "monodromy"): $h=\mathrm{id}$ exactly when the loop is contractible, and changing the basepoint conjugates $h$, so the *conjugacy class* $[h]_{\mathrm{conj}}$ (not $h$ itself) is the basepoint-free invariant — hence free homotopy classes $\leftrightarrow$ conjugacy classes. Second, a nontrivial, non-peripheral class corresponds to a **hyperbolic** element $\tau$, which translates along a unique geodesic axis by a definite distance $\ell_\gamma$; that axis projects to the unique closed geodesic in the class, of length $\ell_\gamma$. The paper needs to *enumerate* a conjugacy class without repetition, which is where the centraliser and cosets come in.

---

# The Definition

> **Definition (free homotopy ↔ conjugacy; closed geodesic; translation length).** Fix $x\in X$, $\tilde x\in\pi^{-1}(x)$, giving an isomorphism $\pi_1(X,x)\cong\Gamma$. A loop $\omega$ rooted at $x$ lifts uniquely to an arc $\tilde\omega$ from $\tilde x$ to $h_\omega\tilde x$ for a unique $h_\omega\in\Gamma$ (the **monodromy** / recorded deck transformation), with $h_\omega=\mathrm{id}$ iff $\omega$ is contractible. Changing the basepoint replaces $h_\omega$ by a conjugate, so:
> $$\{\text{free homotopy classes of oriented closed curves on }X\}\ \longleftrightarrow\ \{\text{conjugacy classes in }\Gamma\}.$$
> A class is **non-trivial** if its loops are not null-homotopic and **non-peripheral** if they are not freely homotopic into a cusp or a boundary/funnel. A non-trivial non-peripheral class corresponds to a **primitive hyperbolic** conjugacy class; its representative $\tau\in\Gamma$ can be conjugated to the **standard form** $\tau:z\mapsto e^{\ell_\gamma}z$, with **translation length** $\ell_\gamma>0$, and the class contains a unique **closed geodesic** $\gamma$ of length $\ell_\gamma$ (the projection of the axis of $\tau$, the imaginary half-line). Write $\mathcal P_X$ for the set of **primitive** oriented closed geodesics; the class winding $m\ge1$ times around $\gamma$ is $C_X(\gamma^m)$, corresponding to $[\tau^m]_{\mathrm{conj}}$, with geodesic length $m\ell_\gamma$.

> **Definition (centraliser and coset enumeration).** Since $\Gamma$ is torsion-free and $\tau$ primitive hyperbolic, everything commuting with $\tau^m$ preserves the axis of $\tau$, and the axis-preserving elements form the infinite cyclic **centraliser**
> $$C_\Gamma(\tau^m)=\langle\tau\rangle=\{\tau^k:k\in\mathbb{Z}\}.$$
> Two conjugates coincide, $g_1\tau^m g_1^{-1}=g_2\tau^m g_2^{-1}$, iff $g_1^{-1}g_2\in\langle\tau\rangle$, i.e. iff $g_1,g_2$ lie in the same left coset of $\langle\tau\rangle$. Hence the conjugacy class is enumerated *without repetition* by cosets:
> $$[\tau^m]_{\mathrm{conj}}=\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^m r^{-1}\},\qquad\text{one distinct conjugate per coset.}$$

**Concrete unpacking.** On the hyperbolic cylinder $\Gamma=\langle\tau\rangle$, $\tau:z\mapsto e^\ell z$: the axis is the imaginary half-line, projecting to the core geodesic of length $\ell$; the class $C_X(\gamma^m)$ is "wind $m$ times around the cylinder", corresponding to $\tau^m:z\mapsto e^{m\ell}z$, geodesic length $m\ell$. Here $\Gamma/\langle\tau\rangle$ is a single coset, so the conjugacy class is the single element $\tau^m$ (an abelian group has singleton conjugacy classes) — the coset sum has one term, matching the strip being a full fundamental region.

**Standard names.** **Free homotopy class**, **conjugacy class**, **primitive hyperbolic element**, **translation/displacement length**, **closed geodesic**, **centraliser**, **primitive geodesic**. The correspondence "free homotopy classes ↔ conjugacy classes of $\pi_1$, with a unique geodesic per class in negative curvature" is classical (Cartan; do Carmo, *Riemannian Geometry*, Ch. 12).

---

# Examples and Non-Examples

**Is an instance.** On a genus-2 surface, each of the $2g=4$ standard generators is a primitive hyperbolic element with its own closed geodesic; their conjugacy classes are distinct free homotopy classes. $\tau^m$ ($m\ge2$) is non-primitive: it wraps the primitive geodesic $m$ times, length $m\ell_\gamma$.

**Is NOT an instance.** A **parabolic** element (fixing one boundary point, $|\operatorname{tr}|=2$) has *no* axis and no closed geodesic — its class is **peripheral** (winds into a cusp) and is excluded. Its "class" has zero translation length, so the mass formulas (which divide by $\sinh(\ell/2)$) do not apply.

**Calibration check.** (1) Verify $h_\omega$ changes to $q h_\omega q^{-1}$ when the lift's start moves from $\tilde x$ to $q\tilde x$. (2) Check $C_\Gamma(\tau^m)=\langle\tau\rangle$ for $\Gamma=\langle\tau\rangle$ trivially, and see why torsion-freeness is needed in general (no finite-order element can preserve the axis). (3) Confirm the class $[\tau^m]_{\mathrm{conj}}$ is in bijection with $\Gamma/\langle\tau\rangle$.

---

# Where the paper uses this

This is the algebraic engine of §3. Theorem 3.2's proof restricts the heat-kernel periodisation to the conjugacy class $[\tau^m]_{\mathrm{conj}}$, unfolds it over cosets $\Gamma/\langle\tau\rangle$ using the enumeration above, and reassembles the pieces into an integral over the fundamental strip. Translation length $\ell_\gamma$ (via $L=m\ell_\gamma$) is the sole geometric input to every mass formula. **[[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3]]**.

---

# Verified against

Katok, *Fuchsian Groups*, Ch. 2 (hyperbolic elements, axes, translation length, standard form $z\mapsto e^\ell z$); Buser, *Geometry and Spectra of Compact Riemann Surfaces*, Ch. 1 (free homotopy ↔ conjugacy classes, unique closed geodesic per class, primitive elements and centralisers). Standard.
