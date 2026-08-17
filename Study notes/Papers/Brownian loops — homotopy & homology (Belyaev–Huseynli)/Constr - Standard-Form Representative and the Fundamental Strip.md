---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Primitive Hyperbolic Element and Translation Length"
  - "Def - Centraliser and Coset Enumeration of a Conjugacy Class"
tags: [paper, hyperbolic-geometry]
---

# Notation

- $\gamma\in\mathcal{P}_X$ — a primitive oriented closed geodesic of length $\ell_\gamma$
- $\tau\in\Gamma$ — a representative of the corresponding primitive hyperbolic conjugacy class, normalised as below
- $F_\tau$ — the fundamental strip, a fundamental region for $\langle\tau\rangle$ acting on $\mathbb{H}^2$
- $\operatorname{Im}(z)$ — the imaginary part in the upper half-plane model $\mathbb{H}^2=\{z\in\mathbb{C} : \operatorname{Im}(z)>0\}$
- $L=m\ell_\gamma$ — so that $\tau^m z = e^{L}z$
- $\rho_{\mathbb{H}^2}$ — the hyperbolic area measure, $\mathrm{d}\rho_{\mathbb{H}^2}=\operatorname{Im}(z)^{-2}\,\mathrm{d}x\,\mathrm{d}y$ for $z=x+iy$

---

# In plain language

Two normalisations, taken together, that turn an unmanageable integral into an explicit one.

**The standard form** is a change of coordinates. Every hyperbolic element of $\mathrm{PSL}(2,\mathbb{R})$ is conjugate, within $\mathrm{PSL}(2,\mathbb{R})$, to the dilation $z\mapsto e^{\ell}z$; conjugating moves the axis to the imaginary half-line while preserving the translation length. So a representative $\tau$ of the conjugacy class may be *chosen* to be $z\mapsto e^{\ell_\gamma}z$, and thereafter $\tau^m z = e^{m\ell_\gamma}z$ is a multiplication rather than a Möbius transformation. Everything in §3.1 depends on being able to write $\tau^m z=e^Lz$ literally.

**The fundamental strip** is the region to integrate over. In standard form, $\tau$ multiplies the imaginary part by $e^{\ell_\gamma}$: $\operatorname{Im}(\tau z)=e^{\ell_\gamma}\operatorname{Im}(z)$. So each $\langle\tau\rangle$-orbit meets the horizontal band $\{1\leq\operatorname{Im}(z)<e^{\ell_\gamma}\}$ in exactly one point — the powers of $\tau$ just shift $\log\operatorname{Im}(z)$ by multiples of $\ell_\gamma$. That band is $F_\tau$, and it is a fundamental region for the infinite cyclic group $\langle\tau\rangle$.

**Why the pairing matters.** [[Def - Centraliser and Coset Enumeration of a Conjugacy Class|The coset enumeration]] turns a $\Gamma$-sized sum over a conjugacy class into a single term integrated over a fundamental region for $\langle\tau\rangle$ — but the region it produces is $\bigsqcup_r r^{-1}F$, an unmanageable union of translated copies of a fundamental region for $\Gamma$. The integrand is $\langle\tau\rangle$-invariant, so any fundamental region gives the same answer, and $F_\tau$ is the one where the geometry is a horizontal band. **That freedom to swap fundamental regions is the second half of the unfolding move, and it is where all the explicitness comes from.**

---

# The construction

> **Construction (equation (9) — standard form).** Let $\gamma\in\mathcal{P}_X$ correspond to a primitive hyperbolic conjugacy class in $\Gamma$ with translation length $\ell_\gamma$. Fixing a representative $\tau\in\Gamma$ and conjugating in $\mathrm{PSL}(2,\mathbb{R})$, one may place $\tau$ in the **standard form**
> $$\tau : z\longmapsto e^{\ell_\gamma}z,\tag{9}$$
> the hyperbolic isometry of $\mathbb{H}^2$ whose axis is the imaginary half-line and whose translation length along that axis is $\ell_\gamma$.

> **Construction (equation (12) — the fundamental strip).** In the standard form, $\operatorname{Im}(\tau z)=e^{\ell_\gamma}\operatorname{Im}(z)$, so $\tau$ rescales the imaginary part. Each orbit of $\langle\tau\rangle$ therefore meets the horizontal band $1\leq\operatorname{Im}(z)<e^{\ell_\gamma}$ in exactly one point, and the **fundamental strip**
> $$F_\tau := \big\{z\in\mathbb{H}^2 : 1\leq\operatorname{Im}(z)<e^{\ell_\gamma}\big\}\tag{12}$$
> is a fundamental region for $\langle\tau\rangle$ acting on $\mathbb{H}^2$.

The verification that each orbit meets $F_\tau$ once is immediate: the orbit of $z$ has imaginary parts $\{e^{k\ell_\gamma}\operatorname{Im}(z) : k\in\mathbb{Z}\}$, and exactly one of these lies in $[1,e^{\ell_\gamma})$, namely the one with $k=-\lfloor\log\operatorname{Im}(z)/\ell_\gamma\rfloor$.

**The strip is unbounded horizontally.** $F_\tau$ ranges over all real parts; it is a band of finite "height" in the $\log\operatorname{Im}$ coordinate and infinite extent in the real direction. Its hyperbolic area is infinite. This is not a problem, because the integrand $p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,\tau^m z)$ decays as $z$ moves away from the axis — the displacement $d(z,\tau^m z)$ grows — and the resulting integral is exactly what [[Thm - The Wang–Xue Fundamental-Strip Identity|Lemma 3.4]] evaluates.

---

# Type card

> [!abstract] Type card — standard form and the fundamental strip
> **Given.** A primitive hyperbolic conjugacy class in $\Gamma$ with translation length $\ell_\gamma>0$; the freedom to conjugate within $\mathrm{PSL}(2,\mathbb{R})$ (not merely within $\Gamma$).
>
> **Produces.** A representative $\tau : z\mapsto e^{\ell_\gamma}z$, an element of $\mathrm{PSL}(2,\mathbb{R})$ acting by multiplication; and the region $F_\tau=\{1\leq\operatorname{Im}(z)<e^{\ell_\gamma}\}\subset\mathbb{H}^2$, a fundamental region for $\langle\tau\rangle$, of infinite hyperbolic area.
>
> **Lets you.** Turn the integral over an unmanageable fundamental region for $\Gamma$, with a conjugacy-class sum inside it, into an explicit integral over a horizontal band with a single term inside it — after which the hyperbolic heat kernel can be integrated in closed form.

---

# Properties relied on later

**$\tau^m z = e^{L}z$ with $L=m\ell_\gamma$.** The reason [[Thm - The Wang–Xue Fundamental-Strip Identity|Lemma 3.4]] can be stated as an identity about $\int_{F_\tau}p_{\mathbb{H}^2}(s,z,e^Lz)\,\mathrm{d}\rho_{\mathbb{H}^2}(z)$ — a formula in one real parameter $L$ — rather than as a statement about a group element.

**$\langle\tau\rangle$-invariance of the integrand.** Since $\tau$ commutes with $\tau^m$ and the kernel is $\Gamma$-invariant, $z\mapsto p^{\mathcal{E}}_{\mathbb{H}^2}(t,z,\tau^m z)$ is $\langle\tau\rangle$-invariant, so its integral over *any* fundamental region for $\langle\tau\rangle$ is the same. This is what licenses replacing $\bigsqcup_r r^{-1}F$ by $F_\tau$ in Step 2 of Theorem 3.2, and it is the single step that makes the theorem's right-hand side computable.

**Conjugation is in $\mathrm{PSL}(2,\mathbb{R})$, not in $\Gamma$.** Worth stating explicitly: the normalisation moves $\Gamma$ itself to a conjugate group, and that is harmless because every quantity computed is conjugation-invariant. But the coset enumeration of [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]] takes place inside $\Gamma$ (or its conjugate), and the two normalisations must be applied consistently.

**The three-dimensional analogue.** In §7 the same two constructions are carried out with $\mathrm{PSL}(2,\mathbb{C})$: $\tau:(z,y)\mapsto(e^{L_\gamma}z, e^{\ell_\gamma}y)$ and $F_\tau=\{1\leq y<e^{\ell_\gamma}\}$. The key observation there is that only the *height* is scaled — the holonomy rotation $\theta_\gamma$ acts within each slab and does not affect which slab a point lies in — so the same one-point-per-orbit argument goes through. See [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]].

---

# Consumed by

- [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]] — assumed as a hypothesis; $F_\tau$ is the region on the right-hand side of the conclusion
- [[Thm - The Wang–Xue Fundamental-Strip Identity|Lemma 3.4]] — the identity is stated for exactly this region and this $\tau$
- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]] — inherits the hypothesis through Theorem 3.2 and Lemma 3.4
- [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab]] — the three-dimensional analogue, built on the same principle
- [[Def - Fuchsian Group and the Quotient Surface]] — the hyperbolic cylinder example there is exactly $\langle\tau\rangle\backslash\mathbb{H}^2$ with $F_\tau$ as fundamental region

---

# Where this sits in my DAG

Reduces to [[Def - Primitive Hyperbolic Element and Translation Length]] for the existence of the axis and the translation length, and to [[Def - Centraliser and Coset Enumeration of a Conjugacy Class]] for the identification of $\langle\tau\rangle$ as the relevant cyclic group. Below those, anchors: the hyperbolic plane, its isometry group, and the fact that every hyperbolic element is $\mathrm{PSL}(2,\mathbb{R})$-conjugate to a dilation — all standard, all covered by the Riemannian-geometry strand and [[Def - The Hyperbolic Space H^n]].

The conjugacy normalisation is a one-line matrix computation: $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ with $|a+d|>2$ has two real eigenvalues $e^{\pm\ell/2}$, and conjugating by the matrix of eigenvectors diagonalises it to $\begin{pmatrix}e^{\ell/2}&0\\0&e^{-\ell/2}\end{pmatrix}$, which acts as $z\mapsto e^\ell z$.
