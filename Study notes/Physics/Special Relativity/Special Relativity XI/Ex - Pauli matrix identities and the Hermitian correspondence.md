---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Pauli Matrices and the Hermitian-Matrix Correspondence"
tags: [physics, special-relativity]
---

# Problem Statement

Work with the [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|Pauli matrices]] $\sigma_0 = I$, $\sigma_1, \sigma_2, \sigma_3$ and the correspondence $\underline X = x^\mu\sigma_\mu$.

1. Prove the multiplication law $\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$ directly from the matrices, and deduce the anticommutator $\{\sigma_i,\sigma_j\} = 2\delta_{ij}I$ and commutator $[\sigma_i,\sigma_j] = 2i\varepsilon_{ijk}\sigma_k$.
2. Deduce that for any Euclidean unit vector $\mathbf n$, $(\mathbf n\cdot\boldsymbol\sigma)^2 = I$, and more generally $(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma) = (\mathbf a\cdot\mathbf b)I + i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma$.
3. Verify that $\mathscr{H} : X \mapsto \underline X$ carries the Minkowski interval to the determinant, $\det\underline X = X\cdot X$ (mostly-minus), and that the inverse is $x^0 = \tfrac12\mathrm{tr}\,\underline X$, $x^i = \tfrac12\mathrm{tr}(\sigma_i\underline X)$.

**Recall:**

![[Def - Pauli Matrices and the Hermitian-Matrix Correspondence#The Definition]]

The Levi-Civita symbol $\varepsilon_{ijk}$ is totally antisymmetric with $\varepsilon_{123} = +1$; $\delta_{ij}$ is the Kronecker delta; $\mathbf a\cdot\boldsymbol\sigma = a^i\sigma_i$; the trace $\mathrm{tr}$ of a $2\times 2$ matrix is the sum of its diagonal entries. The signature is mostly-minus, $X\cdot X = (x^0)^2 - (x^1)^2 - (x^2)^2 - (x^3)^2$.

---

# Convergent Strategy

**Problem class.** A *foundational identity-verification* drill: establish, by direct matrix computation, the algebraic facts that the rest of the chapter takes for granted. The [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map#Problem-Solving Strategy|topic strategy]] says the Pauli multiplication law is the engine behind every later computation, so this exercise builds the engine.

**Assumption pattern.** The only inputs are the four explicit matrices and the definitions of trace and determinant. Everything follows by multiplying $2\times 2$ matrices and matching entries; there is no theorem to invoke, only careful bookkeeping. The signpost that this is a "compute directly" problem is that the objects are given as concrete matrices.

**Theorem routing.** No external theorem is needed — this exercise *is* the proof of facts that other pages cite. Part 1 establishes the multiplication law that [[Thm - The Spinor Map SU(2) to SO(3)]] and [[Def - Lie Algebra sl(2,C) and the Exponential Map]] use; part 2's $(\mathbf n\cdot\boldsymbol\sigma)^2 = I$ is what makes every Pauli exponential collapse; part 3 is the interval-as-determinant fact at the foundation of [[Def - The Spinor Map and SL(2,C)|the spinor map]].

**Key decision point.** The one genuine choice is how to organise the case-checking in part 1: rather than computing all nine products $\sigma_i\sigma_j$ separately, exploit the symmetry — the diagonal cases $i = j$ give $\sigma_i^2 = I$, and the off-diagonal cases reduce to the single computation $\sigma_1\sigma_2 = i\sigma_3$ plus cyclic permutation. Recognising the cyclic structure turns nine computations into two.

---

# Legal Operations Used

1. **Use the Pauli multiplication law to collapse a product** (operation 3 from the topic page): this exercise *derives* the law, then immediately applies it in part 2 to compute $(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma)$ by expanding $a^i b^j\sigma_i\sigma_j$ and substituting $\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$.

2. **Recast a four-vector as a Hermitian matrix** (operation 1 from the topic page): part 3 writes $\underline X = x^\mu\sigma_\mu$ explicitly as $\begin{pmatrix}t+z & x-iy\\x+iy & t-z\end{pmatrix}$ and takes its determinant.

---

# Hints

> [!note]- Hint 1
> For part 1, you only need to compute $\sigma_1^2$ (and note $\sigma_2^2, \sigma_3^2$ are identical by the same computation) and the single product $\sigma_1\sigma_2$; the rest follow by the cyclic symmetry $1 \to 2 \to 3 \to 1$ and by taking adjoints. Recall $\sigma_2\sigma_1 = -\sigma_1\sigma_2$ from antisymmetry.

> [!note]- Hint 2
> For part 2, write $(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma) = a^i b^j\sigma_i\sigma_j$ and substitute the multiplication law. The symmetric part $a^i b^j\delta_{ij} = \mathbf a\cdot\mathbf b$; the antisymmetric part $i\,a^i b^j\varepsilon_{ijk}\sigma_k = i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma$.

> [!note]- Hint 3
> For part 3, the determinant of $\begin{pmatrix}t+z & x-iy\\x+iy & t-z\end{pmatrix}$ is $(t+z)(t-z) - (x-iy)(x+iy) = t^2 - z^2 - (x^2 + y^2)$. For the inverse, $\mathrm{tr}\,\sigma_0 = 2$ and $\mathrm{tr}\,\sigma_i = 0$, while $\mathrm{tr}(\sigma_i\sigma_j) = 2\delta_{ij}$.

---

# Solution

The three parts are independent computations, all reducing to multiplying $2\times 2$ matrices and reading off entries. Part 1 establishes the multiplication law from two base computations plus cyclic symmetry; part 2 expands a product using that law; part 3 takes a determinant and uses trace orthogonality of the Pauli basis.

**Step 1: The multiplication law $\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$.**

> [!note]- Derivation
> Compute the squares: $\sigma_1^2 = \begin{pmatrix}0&1\\1&0\end{pmatrix}^2 = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I$, and identically $\sigma_2^2 = \begin{pmatrix}0&-i\\i&0\end{pmatrix}^2 = \begin{pmatrix}1&0\\0&1\end{pmatrix} = I$, $\sigma_3^2 = \begin{pmatrix}1&0\\0&-1\end{pmatrix}^2 = I$. So $\sigma_i^2 = I = \delta_{ii}I$ (no sum), confirming the diagonal case.
>
> Compute the key product: $\sigma_1\sigma_2 = \begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}0&-i\\i&0\end{pmatrix} = \begin{pmatrix}i&0\\0&-i\end{pmatrix} = i\sigma_3$. By cyclic permutation $1\to2\to3\to1$ (or direct computation), $\sigma_2\sigma_3 = i\sigma_1$ and $\sigma_3\sigma_1 = i\sigma_2$. Taking the products in the opposite order: $\sigma_2\sigma_1 = \begin{pmatrix}0&-i\\i&0\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix} = \begin{pmatrix}-i&0\\0&i\end{pmatrix} = -i\sigma_3$, so $\sigma_2\sigma_1 = -\sigma_1\sigma_2$.
>
> Collecting: for $i\neq j$, $\sigma_i\sigma_j = i\varepsilon_{ijk}\sigma_k$ (the sign tracking the cyclic order), and for $i = j$, $\sigma_i\sigma_j = I$. Both cases are summarised by
> $$\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k.$$
> Adding $\sigma_i\sigma_j + \sigma_j\sigma_i$: the $\varepsilon$ terms cancel (antisymmetric), giving $\{\sigma_i,\sigma_j\} = 2\delta_{ij}I$. Subtracting: the $\delta$ terms cancel, giving $[\sigma_i,\sigma_j] = 2i\varepsilon_{ijk}\sigma_k$.

**Step 2: $(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma) = (\mathbf a\cdot\mathbf b)I + i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma$, hence $(\mathbf n\cdot\boldsymbol\sigma)^2 = I$.**

> [!note]- Derivation
> Expand using the bilinearity and the law from Step 1:
> $$(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma) = a^i b^j\,\sigma_i\sigma_j = a^i b^j(\delta_{ij}I + i\varepsilon_{ijk}\sigma_k) = (a^i b^i)I + i\,\varepsilon_{ijk}a^i b^j\sigma_k.$$
> The first term is $(\mathbf a\cdot\mathbf b)I$. In the second, $\varepsilon_{ijk}a^i b^j = (\mathbf a\times\mathbf b)_k$ is the $k$-th component of the cross product, so the term is $i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma$. Hence
> $$(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma) = (\mathbf a\cdot\mathbf b)I + i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma.$$
> Setting $\mathbf a = \mathbf b = \mathbf n$ with $|\mathbf n| = 1$: $\mathbf n\cdot\mathbf n = 1$ and $\mathbf n\times\mathbf n = 0$, so $(\mathbf n\cdot\boldsymbol\sigma)^2 = I$. This is the identity that makes every Pauli exponential close into $\cos/\sin$ or $\cosh/\sinh$.

**Step 3: $\det\underline X = X\cdot X$ and the trace inverse.**

> [!note]- Derivation
> The Hermitian matrix is
> $$\underline X = x^0\sigma_0 + x^1\sigma_1 + x^2\sigma_2 + x^3\sigma_3 = \begin{pmatrix}x^0 + x^3 & x^1 - ix^2 \\ x^1 + ix^2 & x^0 - x^3\end{pmatrix}.$$
> Its determinant is
> $$\det\underline X = (x^0 + x^3)(x^0 - x^3) - (x^1 - ix^2)(x^1 + ix^2) = (x^0)^2 - (x^3)^2 - \big((x^1)^2 + (x^2)^2\big),$$
> which equals $(x^0)^2 - (x^1)^2 - (x^2)^2 - (x^3)^2 = X\cdot X$ in mostly-minus signature.
>
> For the inverse, $\mathrm{tr}\,\underline X = (x^0 + x^3) + (x^0 - x^3) = 2x^0$, so $x^0 = \tfrac12\mathrm{tr}\,\underline X$. For the spatial components, use $\mathrm{tr}(\sigma_i\sigma_j) = 2\delta_{ij}$ (immediate from Step 1, since $\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$ has trace $2\delta_{ij}$ as $\mathrm{tr}\,\sigma_k = 0$) and $\mathrm{tr}(\sigma_i\sigma_0) = \mathrm{tr}\,\sigma_i = 0$. Then $\mathrm{tr}(\sigma_i\underline X) = x^\mu\mathrm{tr}(\sigma_i\sigma_\mu) = x^j\cdot 2\delta_{ij} = 2x^i$, so $x^i = \tfrac12\mathrm{tr}(\sigma_i\underline X)$.

> [!note]- Complete formal solution
> **(1)** Direct multiplication gives $\sigma_i^2 = I$ for each $i$ and $\sigma_1\sigma_2 = i\sigma_3$, $\sigma_2\sigma_3 = i\sigma_1$, $\sigma_3\sigma_1 = i\sigma_2$, with $\sigma_j\sigma_i = -\sigma_i\sigma_j$ for $i\neq j$; combining, $\sigma_i\sigma_j = \delta_{ij}I + i\varepsilon_{ijk}\sigma_k$. The symmetric and antisymmetric parts are $\{\sigma_i,\sigma_j\} = 2\delta_{ij}I$ and $[\sigma_i,\sigma_j] = 2i\varepsilon_{ijk}\sigma_k$.
>
> **(2)** $(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma) = a^i b^j\sigma_i\sigma_j = (\mathbf a\cdot\mathbf b)I + i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma$; at $\mathbf a = \mathbf b = \mathbf n$ (unit), $(\mathbf n\cdot\boldsymbol\sigma)^2 = I$.
>
> **(3)** $\underline X = \begin{pmatrix}x^0+x^3 & x^1-ix^2\\x^1+ix^2 & x^0-x^3\end{pmatrix}$ has $\det\underline X = (x^0)^2 - (x^1)^2 - (x^2)^2 - (x^3)^2 = X\cdot X$; using $\mathrm{tr}\,\sigma_0 = 2$, $\mathrm{tr}\,\sigma_i = 0$, $\mathrm{tr}(\sigma_i\sigma_j) = 2\delta_{ij}$ gives the inverse $x^0 = \tfrac12\mathrm{tr}\,\underline X$, $x^i = \tfrac12\mathrm{tr}(\sigma_i\underline X)$. $\blacksquare$

---

# Key Takeaways

**The entire Pauli algebra reduces to two base computations plus cyclic symmetry.** The nine products $\sigma_i\sigma_j$ are not nine independent facts: the three diagonal ones are all $I$ (one computation, $\sigma_1^2 = I$, repeated), and the six off-diagonal ones come from $\sigma_1\sigma_2 = i\sigma_3$ by cyclic permutation and sign-reversal under transposition. Recognising this structure — that a totally antisymmetric object on three indices is determined by one component — is the reusable skill, and it recurs everywhere $\varepsilon_{ijk}$ appears (cross products, angular momentum, the structure constants of $\mathfrak{so}(3)$). When you meet a quantity indexed by $i,j,k$ with a cyclic pattern, compute one representative and propagate by symmetry rather than grinding through all cases. The trigger is any totally antisymmetric or cyclically symmetric three-index object.

**$(\mathbf n\cdot\boldsymbol\sigma)^2 = I$ is the single fact that makes the whole chapter's exponentials computable.** Because a unit Pauli combination squares to the identity, $\exp(z\,\mathbf n\cdot\boldsymbol\sigma)$ splits into even powers (all $I$) and odd powers (all $\mathbf n\cdot\boldsymbol\sigma$), summing to $\cosh z\,I + \sinh z\,\mathbf n\cdot\boldsymbol\sigma$ (or with $z$ imaginary, $\cos$ and $\sin$). This is Euler's formula for an object that squares to $\pm I$, and it is why rotations and boosts in $SL(2,\mathbb{C})$ have closed-form $2\times 2$ matrices rather than infinite series. The transferable principle: any matrix $M$ with $M^2 = I$ (an involution) or $M^2 = -I$ has a one-line exponential, and recognising such an $M$ is the first thing to check when an exponential appears. The same trick computes $\exp$ of a reflection, of $i$ times a Hermitian projector, and of the gamma matrices in the Dirac theory.

**Interval-as-determinant is the structural reason $SL(2,\mathbb{C})$ acts on spacetime.** The computation $\det\underline X = X\cdot X$ looks like a coincidence of $2\times 2$ algebra, but it is the load-bearing fact of the chapter: it is *why* a determinant-preserving congruence is an interval-preserving Lorentz transformation. The trace inverse $x^\mu = \tfrac12\mathrm{tr}(\sigma_\mu\underline X)$ (with $\sigma_0$ contributing the factor differently) is the practical tool for reading components back out of a Hermitian matrix, used every time you compute the Lorentz matrix $\Lambda_A$ from $A$. The deeper lesson, drawn out on the [[Def - Pauli Matrices and the Hermitian-Matrix Correspondence|definition page]], is that this works only because the determinant form on $2\times 2$ Hermitian matrices has signature exactly $(1,3)$ — an accident of four dimensions that makes spinor methods uniquely powerful here and nowhere else.
