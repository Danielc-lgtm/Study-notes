---
type: theorem
subject: linear-algebra
prereqs:
  - "Def - Inner Product Space"
  - "Def - Norm Induced by an Inner Product"
tags: [algebra, linear-algebra]
---

# Notation

$V$ is an inner product space over $\mathbf{F}$. The notation registry is on the parent topic page [[Linear Algebra VI — §6 Inner Product Spaces]].

---

# Statement

> **Theorem (Parallelogram Law).** For any $u, v$ in an inner product space,
> $$\|u + v\|^2 + \|u - v\|^2 = 2(\|u\|^2 + \|v\|^2).$$

> **Theorem (Jordan-von Neumann Converse).** A norm $\|\cdot\|$ on a vector space $V$ over $\mathbf{F}$ comes from an inner product if and only if it satisfies the parallelogram law. In that case, the inner product is given by the **polarization identity** (see [[Ex - Inner product determined by norm via the polarization identity]]).

---

# Motivation

The parallelogram law is the precise algebraic statement that distinguishes inner-product norms from other norms. As a geometric identity it is striking: it asserts that in any parallelogram (with sides $u$ and $v$, hence diagonals $u + v$ and $u - v$), the sum of the squared diagonals equals the sum of the squared sides — a result that goes back to Euclid for $\mathbb{R}^2$. The remarkable fact is that this Euclidean identity holds in *any* inner product space, no matter how exotic — including function spaces, infinite-dimensional Hilbert spaces, and operator spaces.

Its central role is as the **characterisation** of inner-product norms. A general normed space $V$ has a notion of length and the four norm-axioms (non-negativity, definiteness, homogeneity, triangle inequality), but no notion of angle or perpendicularity. The Jordan-von Neumann theorem (1935) says: a norm comes from an inner product if and only if it satisfies the parallelogram law. This is a *complete* characterisation — no additional information is needed. Given the norm, you can recover the inner product via the polarization identity, provided the parallelogram law holds.

This characterisation is what tells you which Banach spaces are *actually* Hilbert spaces. The space $\ell^p$ is a Banach space for every $p \in [1, \infty]$, but the parallelogram law holds only for $p = 2$ — so $\ell^2$ is the unique $\ell^p$ that is a Hilbert space. The same applies to $L^p$ spaces and Sobolev spaces: $p = 2$ is the only case with Hilbert structure. This is *the* reason $L^2$ is the natural function space for Fourier analysis, quantum mechanics, and signal processing — the Hilbert-space structure is exactly what the parallelogram law guarantees.

The parallelogram law is also useful as a **computational identity** in its own right. It lets you trade information about $\|u + v\|$ for information about $\|u - v\|$ (or vice versa), express any one of the four quantities $\{\|u\|, \|v\|, \|u + v\|, \|u - v\|\}$ in terms of the other three. This is the workhorse of "Apollonius's identity" and a hundred Euclidean-geometry identities you may have proved in school by coordinate calculations.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is bare: any two vectors in an inner product space.

The first source is **a problem involving both $\|u + v\|$ and $\|u - v\|$**. Property $B$: the problem statement contains both the sum and difference norms. Bridge: the parallelogram law directly relates them, so the immediate move is to compute via the parallelogram law and see what cancellations or simplifications arise.

The second source is **proving a norm comes from an inner product**. Property $B$: you are given a normed space and asked whether the norm has Hilbert-space structure. Bridge: by Jordan-von Neumann, check the parallelogram law on any pair of vectors. If it fails for even one pair, the norm is *not* an inner-product norm. If it holds for all pairs, you can construct the inner product via the polarization identity.

The third source is **a classical Euclidean-geometry identity**. Property $B$: the problem is about parallelograms, triangles, or quadrilaterals, with constraints on side and diagonal lengths. Bridge: identify the vectors $u, v$ as sides emanating from a common vertex, then the parallelogram law gives the diagonal-side relation. **Apollonius's identity** for triangles ($a^2 + b^2 = \tfrac{1}{2}c^2 + 2m^2$ where $m$ is the median to side $c$) is the parallelogram law applied to the midpoint construction.

**Targets (Output Amplification)**

The conclusion is an *equality* (not an inequality), so its uses are different from those of Cauchy-Schwarz or the triangle inequality.

The first target is **the polarization identity** $\langle u, v\rangle = \tfrac{1}{4}(\|u + v\|^2 - \|u - v\|^2)$ over $\mathbb{R}$, or a four-term version over $\mathbb{C}$. Property $D$: subtract the two parallelogram-law instances $\|u + v\|^2 + \|u - v\|^2 = 2(\|u\|^2 + \|v\|^2)$ and a rearranged version, or expand each norm-squared explicitly. Combination: this recovers the inner product entirely from the norm, completing the bidirectional inner-product ⟷ norm correspondence. See [[Ex - Inner product determined by norm via the polarization identity]].

The second target is the **Jordan-von Neumann characterisation theorem**: a norm on $V$ satisfies the parallelogram law if and only if it comes from an inner product. Property $D$: the polarization identity defines a candidate inner product, and the parallelogram law ensures the candidate is sesquilinear (a non-trivial check). Combination: gives a structural characterisation of Hilbert spaces among Banach spaces.

The third target is **Apollonius's identity** for triangles. Property $D$: take $u, v$ as the two sides emanating from one vertex of a triangle, and $w = (u + v)/2$ as the midpoint of the opposite side. Combination: $\|u\|^2 + \|v\|^2 = \tfrac{1}{2}\|u - v\|^2 + 2\|w\|^2$ — the sum of squared sides equals half the squared third side plus twice the squared median, a classical theorem of plane geometry that follows in two lines from the parallelogram law.

---

# Why Is It True

The intuition is the algebraic identity at the heart of inner-product expansion: **the cross-terms in $\|u + v\|^2$ and $\|u - v\|^2$ have opposite signs, so they cancel when you add the two**.

Expanding via sesquilinearity:
$$
\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2,
$$
$$
\|u - v\|^2 = \|u\|^2 - 2\operatorname{Re}\langle u, v\rangle + \|v\|^2.
$$
Adding these, the cross-terms $\pm 2\operatorname{Re}\langle u, v\rangle$ cancel exactly, leaving
$$
\|u + v\|^2 + \|u - v\|^2 = 2\|u\|^2 + 2\|v\|^2.
$$
**The one-liner mechanism: the cross-term $2\operatorname{Re}\langle u, v\rangle$ appears in $\|u + v\|^2$ with a plus sign and in $\|u - v\|^2$ with a minus sign, so summing kills it and leaves only $\|u\|^2 + \|v\|^2$ on each side.**

Geometrically, the parallelogram with sides $u, v$ has diagonals $u + v$ (the "long diagonal") and $u - v$ (the "short diagonal", in the typical drawing). The sum of squared diagonals depends on both the side lengths and the angle between them — but the angle contributes via the cross-term $\langle u, v\rangle$, which appears with opposite signs in the two diagonals. So the *sum* of squared diagonals is angle-independent, depending only on the side lengths. This is the geometric content: in a parallelogram, the sum of the squared lengths of the four sides (i.e., $2\|u\|^2 + 2\|v\|^2$, since each side is repeated) equals the sum of the squared lengths of the two diagonals.

The parallelogram law is therefore **the cancellation of the inner-product cross-term**, dressed up as a geometric identity about parallelograms. It is the simplest non-trivial consequence of sesquilinearity, and it is exactly the property that singles out inner-product norms among all norms — because it captures the "additivity-of-squared-length" that holds when length comes from a bilinear-form-squared, not from any other formula.

---

# What Makes This Hard

The forward direction of the parallelogram law is trivial — two lines of expansion and addition. The hard direction is the **Jordan-von Neumann converse**: given a norm satisfying the parallelogram law, construct an inner product from it. The construction (via the polarization identity) is mechanical, but verifying that the candidate inner product is actually sesquilinear — additive in each slot, homogeneous, conjugate-symmetric — requires a careful argument. Specifically, additivity $\langle u_1 + u_2, v\rangle = \langle u_1, v\rangle + \langle u_2, v\rangle$ is the non-trivial step, and it requires the parallelogram law applied to several specific vector combinations. The common error is to assume the polarization identity defines an inner product without verifying sesquilinearity.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Expand $\|u + v\|^2$ and $\|u - v\|^2$ using sesquilinearity. The cross-terms cancel when added.

**Subgoal decomposition:**

1. **Expand $\|u + v\|^2$.** Compute $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$.
   - *Hint:* sesquilinear expansion of $\langle u + v, u + v\rangle$.
   - *Why needed:* gives one of the two terms in the parallelogram-law sum.

2. **Expand $\|u - v\|^2$.** Compute $\|u - v\|^2 = \|u\|^2 - 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$.
   - *Hint:* same expansion as step 1, with sign changes on cross-terms.
   - *Why needed:* gives the other term, with the cross-term sign flipped.

3. **Add.** Cross-terms cancel: $\|u + v\|^2 + \|u - v\|^2 = 2\|u\|^2 + 2\|v\|^2$.
   - *Hint:* this is just arithmetic.
   - *Why needed:* this is the statement of the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: Expansion of $\|u + v\|^2$ and $\|u - v\|^2$
> **Statement:** For $u, v$ in an inner product space,
> $$\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2, \qquad \|u - v\|^2 = \|u\|^2 - 2\operatorname{Re}\langle u, v\rangle + \|v\|^2.$$
>
> **Hint:** Sesquilinear expansion of $\langle u + v, u + v\rangle$ and $\langle u - v, u - v\rangle$; use $\langle v, u\rangle = \overline{\langle u, v\rangle}$, so the cross-terms sum to $\pm 2\operatorname{Re}\langle u, v\rangle$.
>
> **Why needed:** These two expansions are the ingredients of the parallelogram law; their sum eliminates the cross-term.
>
> > [!note]- Full proof
> > Computing $\|u + v\|^2 = \langle u + v, u + v\rangle = \langle u, u\rangle + \langle u, v\rangle + \langle v, u\rangle + \langle v, v\rangle$. By conjugate symmetry $\langle v, u\rangle = \overline{\langle u, v\rangle}$, so $\langle u, v\rangle + \langle v, u\rangle = 2\operatorname{Re}\langle u, v\rangle$. Hence $\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$.
> >
> > For $\|u - v\|^2 = \langle u - v, u - v\rangle = \langle u, u\rangle - \langle u, v\rangle - \langle v, u\rangle + \langle v, v\rangle = \|u\|^2 - 2\operatorname{Re}\langle u, v\rangle + \|v\|^2$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** $\|u + v\|^2 + \|u - v\|^2 = 2(\|u\|^2 + \|v\|^2)$ for any $u, v$ in an inner product space.
>
> *Proof.* By sesquilinear expansion (see Lemma 1),
> $$\|u + v\|^2 = \|u\|^2 + 2\operatorname{Re}\langle u, v\rangle + \|v\|^2,$$
> $$\|u - v\|^2 = \|u\|^2 - 2\operatorname{Re}\langle u, v\rangle + \|v\|^2.$$
> Adding:
> $$\|u + v\|^2 + \|u - v\|^2 = 2\|u\|^2 + 2\|v\|^2,$$
> as desired. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Geometry: Apollonius's identity.** In any triangle with sides $a, b, c$ and median $m$ to side $c$, $a^2 + b^2 = \tfrac{1}{2}c^2 + 2m^2$. Apply the parallelogram law to the two vectors from the midpoint of side $c$ to the two endpoints of that side; the diagonals of the resulting parallelogram are sides of the triangle.

**Functional analysis: identifying Hilbert spaces.** To determine whether a given Banach space is a Hilbert space, check the parallelogram law on a specific pair of vectors. For $\ell^p(\mathbb{R}^2)$ with $p \neq 2$: take $u = (1, 0)$, $v = (0, 1)$. Then $\|u + v\|_p = 2^{1/p}$, $\|u - v\|_p = 2^{1/p}$ (since $\||\pm 1| + |\pm 1|^p|^{1/p} = 2^{1/p}$), and $\|u\|_p = \|v\|_p = 1$. The parallelogram law would require $2^{2/p} + 2^{2/p} = 4$, i.e., $2^{2/p + 1} = 4$, i.e., $2/p + 1 = 2$, i.e., $p = 2$. So $\ell^p$ for $p \neq 2$ is not a Hilbert space.

**Probability: variance of a sum and difference.** For random variables $X, Y$ (in the inner-product space of mean-zero finite-variance random variables), the parallelogram law gives
$$E[(X + Y)^2] + E[(X - Y)^2] = 2(E[X^2] + E[Y^2]),$$
which simplifies to $\operatorname{Var}(X + Y) + \operatorname{Var}(X - Y) = 2(\operatorname{Var}(X) + \operatorname{Var}(Y))$. This identity is a useful diagnostic in statistics: deviation from the parallelogram law signals departure from the $L^2$-norm structure of the underlying $\sigma$-algebra.

---

# Bridges

- **Polarization Identity** *(see [[Ex - Inner product determined by norm via the polarization identity]])* — the parallelogram law is the algebraic identity that *implies* the polarization identity, and conversely the polarization identity (together with non-negativity of $\langle v, v\rangle$) implies the parallelogram law. The two are complementary: the parallelogram law shows the norm is constrained by the inner product, while polarization shows the inner product can be recovered from the norm. Together they make norm and inner product interconvertible data.

- **[[Thm - Pythagorean Theorem|Pythagorean Theorem]]** — the parallelogram law specialises to the Pythagorean theorem when $\langle u, v\rangle = 0$: setting cross-terms to zero gives $\|u + v\|^2 = \|u\|^2 + \|v\|^2$. So the parallelogram law is the *generalisation* of the Pythagorean theorem to non-orthogonal pairs, with the correction $-2\operatorname{Re}\langle u, v\rangle$ accounting for the non-perpendicularity.

- **Jordan-von Neumann Characterisation** *(Functional Analysis)* — the parallelogram law characterises inner-product norms among all norms on a vector space (Jordan and von Neumann, 1935). The converse direction — constructing the inner product from a parallelogram-law-satisfying norm via the polarization identity — is the structural theorem that pins down "Hilbert space" as a property of the norm alone.

- **$L^p$ structure and the unique role of $L^2$** *(Analysis)* — the $L^p$ norm satisfies the parallelogram law if and only if $p = 2$. This is *the* mathematical reason $L^2$ is special: it is the unique $L^p$ that is a Hilbert space, hence the unique $L^p$ in which orthogonality, projections, Fourier expansions, and all the inner-product machinery work. Without the parallelogram law, $L^p$ for $p \neq 2$ has only the Banach-space structure — useful for many things, but missing the geometric richness.
