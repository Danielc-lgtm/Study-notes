---
type: theorem
subject: special-relativity
prereqs:
  - "Def - The Hodge Star"
  - "Def - Alternate Forms and the Exterior Product"
  - "Thm - Hodge Star and the Exterior Product"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$, $\eta = \mathrm{diag}(1,-1,-1,-1)$. $\mathscr{A}_2(E)$ is the six-dimensional space of [[Def - Alternate Forms and the Exterior Product|2-forms]] on [[Def - Minkowski Space and the Metric|Minkowski space]]; $\star$ is the [[Def - The Hodge Star|Hodge star]] (with $\star^2 = -1$ on $2$-forms, from [[Thm - Hodge Star and the Exterior Product]]). For a unit timelike vector $\vec u$ ($\vec u\cdot\vec u = +1$), $u^\flat = g(\vec u, \cdot)$ is its [[Def - Metric Duality and Index Manipulation|metric-dual]] one-form. For a $2$-form $A$ and an observer with four-velocity $\vec u$, the electric and magnetic parts relative to $\vec u$ are the vectors $\mathbf e = A(\cdot, \vec u)^\sharp$ and $\mathbf b = \star A(\cdot, \vec u)^\sharp$ in the [[Def - Observer and Local Rest Space|local rest space]] $\vec u^\perp$. The complexification is $\mathscr{A}_2(E)_\mathbb{C} = \mathscr{A}_2(E)\otimes\mathbb{C}$. Full registry on [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality]].

---

# Statement

> **Theorem (observer decomposition of a $2$-form).** Let $A \in \mathscr{A}_2(E)$ be a $2$-form and $\vec u$ a unit timelike vector. There exist a unique one-form $q$ and a unique vector $\vec b$, both orthogonal to $\vec u$ ($\langle q, \vec u\rangle = 0$ and $\vec u\cdot\vec b = 0$), such that
> $$\boxed{\ A = u^\flat\wedge q + \star\big(u^\flat\wedge b^\flat\big)\ },$$
> with $q = A(\cdot, \vec u)$ obtained directly from $A$ and $\vec b = \star A(\vec u, \cdot)^\sharp$ obtained from the Hodge dual, equivalently in components $b^\alpha = -\tfrac12\varepsilon^{\alpha\mu\nu}{}_\rho A_{\mu\nu}u^\rho$. The vector $\vec q^\sharp$ is the **electric part** and $\vec b$ the **magnetic part** of $A$ relative to $\vec u$.

> **Theorem (self-dual / anti-self-dual decomposition).** Since $\star^2 = -1$ on $\mathscr{A}_2(E)$, the Hodge star has no real eigenvalues, but on the complexification $\mathscr{A}_2(E)_\mathbb{C}$ it has eigenvalues $\pm i$, giving an $\star$-invariant orthogonal direct-sum decomposition
> $$\mathscr{A}_2(E)_\mathbb{C} = \mathscr{A}_2^+ \oplus \mathscr{A}_2^-, \qquad \mathscr{A}_2^\pm = \{F : \star F = \pm i\,F\}, \qquad \dim_\mathbb{C}\mathscr{A}_2^\pm = 3,$$
> the **self-dual** ($+i$) and **anti-self-dual** ($-i$) $2$-forms. The projections of any real $2$-form $A$ are $A^\pm = \tfrac12(A \mp i\star A)$. Relative to an observer, $A^\pm$ are built from the complex combinations $\mathbf e \pm i\mathbf b$ of the electric and magnetic parts.

---

# Motivation

A $2$-form on Minkowski space has six components — and "six" is the dimension of the [[Def - Lie Algebra of the Lorentz Group|Lorentz algebra]], the dimension of the space of electromagnetic field configurations $(\mathbf E, \mathbf B)$ at a point, and twice the dimension of space. This coincidence is not accidental, and the two decompositions in the statement are the two ways of splitting those six components into physically meaningful threes. The first split is **observer-relative**: pick an observer (a unit timelike $\vec u$) and the $2$-form falls apart into an electric three-vector and a magnetic three-vector in that observer's rest space — exactly how the single field $F$ presents itself to a laboratory as $(\mathbf E, \mathbf B)$. The second split is **observer-independent and complex**: the Hodge star, which mixes electric and magnetic, has eigenvalues $\pm i$, and the six real components reorganise into three complex self-dual and three complex anti-self-dual components — the chirality of the field.

The first decomposition is the relativistic statement that "electric" and "magnetic" are not intrinsic but depend on who is looking. The same $2$-form $A$, decomposed against two different four-velocities $\vec u$ and $\vec u'$, yields different electric and magnetic parts — which is the abstract source of the transformation law $\mathbf E, \mathbf B \to \mathbf E', \mathbf B'$ under a boost. The theorem makes precise that the *only* invariant content is the $2$-form itself; the $(\mathbf E, \mathbf B)$ split is a coordinate, not a fact.

The second decomposition is the deeper one, and it is the reason the chapter exists. The bare statement "$\star^2 = -1$ on $2$-forms" sounds like a sign convention, but it forces a profound restructuring: an operator with $\star^2 = -1$ is a **complex structure**, and the natural variables are not the real field $A$ but the complex combinations $A \mp i\star A$. For electromagnetism these are $\mathbf E \pm i\mathbf B$, the Riemann-Silberstein vector, and the self-dual/anti-self-dual split is the decomposition of the photon into its two helicities. Moreover this split is exactly the $(1,0)\oplus(0,1)$ decomposition of the field strength under the [[Def - The Lorentz Group|Lorentz group]]: the self-dual part transforms in the $(1,0)$ representation, the anti-self-dual in $(0,1)$, matching the complexification $\mathfrak{so}(1,3)_\mathbb{C}\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$ of [[Special Relativity X — The Lorentz Group as a Lie Group]]. The Hodge star on $2$-forms and the complexification of the Lorentz algebra are the *same* $\pm i$ splitting, seen once on forms and once on the algebra. This is the machinery that makes the electromagnetic chapters clean, and it is why a chapter on Hodge duality belongs in a relativity course.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a $2$-form, plus (for the first decomposition) a unit timelike vector."

A first disguised source is **"an antisymmetric type-$(0,2)$ tensor."** Any antisymmetric $T_{\mu\nu}$ is a $2$-form, so the theorem applies to the field strength $F$, the angular-momentum tensor $J_{\mu\nu}$, the spin tensor $S_{\mu\nu}$, and the [[Def - Local Frame and Four-Rotation|four-rotation]] $\Omega_{\mu\nu}$ of an observer's frame. The bridge is recognising antisymmetry. *Example problem:* decompose the angular-momentum $2$-form $J_C$ relative to an observer to extract the [[Def - Spin Four-Vector|angular-momentum vector]] $\boldsymbol\sigma_C = \star J_C(\vec u_0, \cdot)$ — Gourgoulhon's Example 14.11, which is exactly the magnetic-part construction.

A second disguised source is **"an observer is given."** Whenever a problem names a four-velocity — a particle's, a laboratory's, an instantaneous rest frame's — that supplies the $\vec u$ for the first decomposition, and any $2$-form in sight can be split into its electric and magnetic parts relative to that observer. The bridge is "four-velocity = unit timelike vector." *Example problem:* the electric and magnetic fields measured by a moving charge are the parts of $F$ relative to the charge's four-velocity.

A third disguised source is **"a parity-definite or helicity-definite field."** A field with $\star F = \pm iF$ is already self-dual or anti-self-dual; a circularly polarised wave, or one helicity of radiation, is such a field. The bridge is the eigenvalue condition. *Example problem:* show that a positive-helicity plane wave has $\mathbf E + i\mathbf B$ pointing in a fixed complex direction (self-dual), so the wave is annihilated by the anti-self-dual projector.

**Targets (Output Amplification)**

The conclusion is the pair of decompositions.

Combine the observer decomposition with **a change of observer**. Decomposing the *same* $A$ against $\vec u$ and against a boosted $\vec u'$ yields two different $(\mathbf e, \mathbf b)$ pairs, related by the boost. The further result is the transformation law of electric and magnetic fields, $\mathbf E_\parallel' = \mathbf E_\parallel$, $\mathbf E_\perp' = \gamma(\mathbf E + \mathbf v\times\mathbf B)_\perp$, etc. The combination is useful because it derives the field transformations from a single invariant object; see [[Special Relativity XXI — The Electromagnetic Field]].

Combine the self-dual decomposition with **the field invariants**. The two Lorentz invariants of a $2$-form are $A_{\mu\nu}A^{\mu\nu} \propto \mathbf b^2 - \mathbf e^2$ and $\star A_{\mu\nu}A^{\mu\nu} \propto \mathbf e\cdot\mathbf b$; together they form the single complex invariant $(\mathbf e + i\mathbf b)^2 = \mathbf e^2 - \mathbf b^2 + 2i\,\mathbf e\cdot\mathbf b$, which is the squared length of the self-dual part. The further result: the field is classified (electric-dominated, magnetic-dominated, or null) by one complex number. The combination is nonobvious because two real invariants are really one complex invariant of the self-dual part.

Combine the self-dual decomposition with **the Lorentz group action**. The self-dual and anti-self-dual subspaces are each Lorentz-invariant, and they carry the irreducible $(1,0)$ and $(0,1)$ representations. The further result is the representation-theoretic classification of the field strength and the statement that a parity-symmetric theory must treat the two chiralities symmetrically. The combination connects the Hodge star to [[Special Relativity X — The Lorentz Group as a Lie Group|the (A,B) representation theory]] — the same $\pm i$ on both sides.

---

# Why Is It True

The observer decomposition is, at heart, the statement that a unit timelike $\vec u$ splits spacetime into "time" (the $\vec u$ direction) and "space" (the orthogonal rest space $\vec u^\perp$), and a $2$-form splits accordingly. A $2$-form eats two vectors; feed one slot the time direction $\vec u$ and you get a one-form on the rest space (the **electric** part, $q = A(\cdot, \vec u)$); the part of $A$ that lives entirely in the rest space is a $2$-form on a three-space, which by three-dimensional [[Def - The Hodge Star|Hodge duality]] is a vector (the **magnetic** part $\vec b$). That every $2$-form decomposes this way, uniquely, is the four-dimensional content of [[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms|the orthogonal decomposition of antisymmetric bilinear forms]] proved for observers — here re-expressed compactly using the wedge and the Hodge star.

**The one-line mechanism for the observer split: a $2$-form contracted once with the time direction $\vec u$ gives the electric one-form; what is left, being a $2$-form purely in the three-dimensional rest space, is dual to the magnetic vector.**

The self-dual decomposition is pure linear algebra of an operator with $\star^2 = -1$. Over the reals such an operator cannot be diagonalised — its minimal polynomial is $x^2 + 1$, irreducible over $\mathbb{R}$. But over $\mathbb{C}$, $x^2 + 1 = (x-i)(x+i)$ splits, so $\star$ is diagonalisable with eigenvalues $\pm i$, and the complexified space is the direct sum of the two eigenspaces. The projectors onto them are $P^\pm = \tfrac12(1 \mp i\star)$ (check: $\star P^\pm = \tfrac12(\star \mp i\star^2) = \tfrac12(\star \pm i) = \pm i\cdot\tfrac12(1 \mp i\star) = \pm i P^\pm$). Each eigenspace has complex dimension $3$ because the six-dimensional real space, complexified to six complex dimensions, splits evenly (the two eigenspaces are complex conjugates of each other, so equal-dimensional). That the eigenvalues are $\pm i$ rather than $\pm 1$ is the whole story: $\pm 1$ (the Riemannian case) would give a *real* decomposition, but $\pm i$ forces complexification, and the complex structure is the helicity structure of the field.

**The one-line mechanism for the chiral split: $\star^2 = -1$ means $\star$ is "multiplication by $i$," so the natural eigen-objects are complex, $A \mp i\star A$, and these are the two helicities $\mathbf e \pm i\mathbf b$.**

---

# What Makes This Hard

The first decomposition is conceptually easy but notationally treacherous: one must keep straight which slot of $A$ is fed $\vec u$, that the magnetic part comes from $\star A$ rather than $A$, and the orthogonality conditions $\langle q, \vec u\rangle = 0$, $\vec u\cdot\vec b = 0$. The second decomposition trips people on the *necessity* of complexification — the instinct is to look for real eigenvectors of $\star$ and fail, missing that the right move is to complexify; and on the *interpretation* — recognising that the abstract $\pm i$ eigenspaces are concretely $\mathbf E \pm i\mathbf B$, and that this matches the $(1,0)\oplus(0,1)$ of the Lorentz algebra rather than being a separate accident. The single most common error is to compute $\star^2 = +1$ (the Euclidean sign), which collapses the complex decomposition into a spurious real one.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For the observer split, define $q = A(\cdot, \vec u)$ and verify (using [[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms|the antisymmetric-bilinear-form decomposition]] and the wedge formula $\star(a\wedge b) = \varepsilon(\vec a, \vec b, \cdot)$) that $A - u^\flat\wedge q$ is the Hodge dual of $u^\flat\wedge b^\flat$. For the chiral split, observe $\star^2 = -1$, complexify, and build the eigenprojectors $P^\pm = \tfrac12(1\mp i\star)$.

**Subgoal decomposition:**

1. **Extract the electric part.** Set $q := A(\cdot, \vec u)$; show $\langle q, \vec u\rangle = 0$ by antisymmetry of $A$.
   - *Hint:* $\langle q, \vec u\rangle = A(\vec u, \vec u) = 0$ since $A$ is alternating.
   - *Why needed:* It is the first term and fixes the electric one-form.

2. **Identify the remainder as a Hodge dual.** Show $B := A - u^\flat\wedge q$ is a $2$-form annihilated by $\vec u$ in one slot, hence (in the rest space) dual to a vector $\vec b$, giving $B = \star(u^\flat\wedge b^\flat)$.
   - *Hint:* Use [[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms]] (eq 3.37); the wedge formula identifies the $\varepsilon(\vec u, \vec b, \cdot, \cdot)$ term as $\star(u^\flat\wedge b^\flat)$.
   - *Why needed:* It is the second term and fixes the magnetic vector.

3. **Recover $\vec b$ from $\star A$.** Take the Hodge star of the decomposition; using $\star^2 = -1$, show $\star A(\vec u, \cdot) = b^\flat$, i.e. $\vec b = \star A(\vec u, \cdot)^\sharp$.
   - *Hint:* $\star A = \varepsilon(\vec u, \vec q^\sharp, \cdot, \cdot) - u^\flat\wedge b^\flat$; set the first argument to $\vec u$ and use $\vec u\cdot\vec u = 1$.
   - *Why needed:* It gives the operational formula $b^\alpha = -\tfrac12\varepsilon^{\alpha\mu\nu}{}_\rho A_{\mu\nu}u^\rho$.

4. **Complexify and diagonalise $\star$.** From $\star^2 = -1$, form $P^\pm = \tfrac12(1\mp i\star)$ and verify they are complementary projectors onto the $\pm i$ eigenspaces.
   - *Hint:* Check $P^+ + P^- = 1$, $P^\pm{}^2 = P^\pm$, $\star P^\pm = \pm iP^\pm$ using $\star^2 = -1$.
   - *Why needed:* It produces the self-dual/anti-self-dual decomposition.

---

# Lemma Decomposition

> [!note]- Lemma 1: The electric one-form is orthogonal to the observer
> **Statement:** For $q := A(\cdot, \vec u)$ with $A$ a $2$-form, $\langle q, \vec u\rangle = 0$.
>
> **Hint:** Evaluate $q$ on $\vec u$ and use antisymmetry.
>
> **Why needed:** It certifies that the electric part lives in the rest space, as required.
>
> > [!note]- Full proof
> > $\langle q, \vec u\rangle = q(\vec u) = A(\vec u, \vec u)$. Since $A$ is a [[Def - Alternate Forms and the Exterior Product|2-form]], $A(\vec u, \vec u) = -A(\vec u, \vec u)$, so $A(\vec u, \vec u) = 0$. Hence $\langle q, \vec u\rangle = 0$. $\blacksquare$

> [!note]- Lemma 2: The Hodge star is a complex structure on 2-forms
> **Statement:** On $\mathscr{A}_2(E)$, $\star^2 = -\mathrm{id}$, so $\star$ has minimal polynomial $x^2 + 1$, no real eigenvalues, and over $\mathbb{C}$ eigenvalues exactly $\pm i$.
>
> **Hint:** This is the $p = 2$ case of $\star\star = (-1)^{p+1}$.
>
> **Why needed:** It is the entire basis of the self-dual/anti-self-dual decomposition.
>
> > [!note]- Full proof
> > By [[Thm - Hodge Star and the Exterior Product]], $\star\star A = (-1)^{p+1}A$, and for $p = 2$ this is $\star\star A = -A$, i.e. $\star^2 = -\mathrm{id}$. The minimal polynomial divides $x^2 + 1$; since $\star \neq \pm i\,\mathrm{id}$ over $\mathbb{R}$ (it has no real eigenvalues at all, as $x^2 + 1$ is irreducible over $\mathbb{R}$), the minimal polynomial is exactly $x^2 + 1$. Over $\mathbb{C}$ this factors as $(x - i)(x + i)$ with distinct roots, so $\star$ is diagonalisable on $\mathscr{A}_2(E)_\mathbb{C}$ with eigenvalues $\pm i$. $\blacksquare$

> [!note]- Lemma 3: The eigenprojectors and equal dimensions
> **Statement:** $P^\pm = \tfrac12(\mathrm{id} \mp i\star)$ are complementary projectors with $\star P^\pm = \pm iP^\pm$, and the eigenspaces $\mathscr{A}_2^\pm = P^\pm(\mathscr{A}_2(E)_\mathbb{C})$ each have complex dimension $3$.
>
> **Hint:** Verify the projector identities algebraically; the equal dimensions follow because $\mathscr{A}_2^-$ is the complex conjugate of $\mathscr{A}_2^+$.
>
> **Why needed:** It exhibits the decomposition explicitly and fixes the $3 + 3$ dimension count.
>
> > [!note]- Full proof
> > Using $\star^2 = -1$: $P^+ + P^- = \tfrac12(1 - i\star) + \tfrac12(1 + i\star) = 1$. And $(P^\pm)^2 = \tfrac14(1 \mp i\star)^2 = \tfrac14(1 \mp 2i\star + i^2\star^2) = \tfrac14(1 \mp 2i\star - (-1)) = \tfrac14(2 \mp 2i\star) = \tfrac12(1 \mp i\star) = P^\pm$, so they are idempotent. Also $P^+P^- = \tfrac14(1 - i\star)(1 + i\star) = \tfrac14(1 + \star^2) = \tfrac14(1 - 1) = 0$, so they are complementary. Finally $\star P^\pm = \tfrac12(\star \mp i\star^2) = \tfrac12(\star \pm i) = \pm i\cdot\tfrac12(1 \mp i\star) = \pm iP^\pm$, so $P^\pm$ projects onto the $\pm i$ eigenspace. Since $A$ is real, complex conjugation sends $\star A$ to $\star A$ (the Hodge star is a real operator) and $iF \mapsto -i\bar F$, so it swaps the $+i$ and $-i$ eigenspaces; hence $\overline{\mathscr{A}_2^+} = \mathscr{A}_2^-$ and the two have equal dimension. As they sum to the six-complex-dimensional $\mathscr{A}_2(E)_\mathbb{C}$, each has dimension $3$. $\blacksquare$

> [!note]- Lemma 4: The eigenforms are the complex field combinations
> **Statement:** Relative to an observer $\vec u$ with electric and magnetic parts $\mathbf e, \mathbf b$, the self-dual projection $A^+ = P^+A$ is built from $\mathbf e + i\mathbf b$, and the anti-self-dual $A^- = P^-A$ from $\mathbf e - i\mathbf b$.
>
> **Hint:** Use that $\star$ swaps the electric and magnetic parts (up to sign), so $\star A$ has parts $(-\mathbf b, \mathbf e)$.
>
> **Why needed:** It identifies the abstract eigenspaces with the physical Riemann-Silberstein combinations.
>
> > [!note]- Full proof
> > Decompose $A$ relative to $\vec u$ as electric part $\mathbf e$ and magnetic part $\mathbf b$. The Hodge star exchanges them: $\star A$ relative to the same $\vec u$ has electric part $-\mathbf b$ and magnetic part $\mathbf e$ (a quarter-turn in the $(\mathbf e, \mathbf b)$ plane; this is the field-strength duality, verifiable from the component formula $(\star A)_{\alpha\beta} = \tfrac12\varepsilon_{\mu\nu\alpha\beta}A^{\mu\nu}$ restricted to the rest space). Then $A^+ = \tfrac12(A - i\star A)$ has electric part $\tfrac12(\mathbf e - i(-\mathbf b)) = \tfrac12(\mathbf e + i\mathbf b)$ and magnetic part $\tfrac12(\mathbf b - i\mathbf e) = -\tfrac{i}{2}(\mathbf e + i\mathbf b)$, both proportional to the single complex vector $\mathbf e + i\mathbf b$ — indeed $A^+$ is determined by $\mathbf e + i\mathbf b$ alone, and satisfies the self-dual condition (its magnetic part is $-i$ times its electric part, the rest-space form of $\star A^+ = iA^+$). Likewise $A^-$ is built from $\mathbf e - i\mathbf b$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Observer decomposition.** Let $A$ be a $2$-form and $\vec u$ a unit timelike vector. By [[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms|the orthogonal decomposition of antisymmetric bilinear forms]] (Gourgoulhon eq 3.37), there are a unique one-form $q$ and unique vector $\vec b$, both $\vec u$-orthogonal, with
> $$A = u^\flat\otimes q - q\otimes u^\flat + \varepsilon(\vec u, \vec b, \cdot, \cdot),$$
> where $q = A(\cdot, \vec u)$ (Lemma 1 gives $\langle q, \vec u\rangle = 0$) and $\vec u\cdot\vec b = 0$. The first two terms are by definition the exterior product $u^\flat\wedge q$ (since $a\wedge b = a\otimes b - b\otimes a$ for one-forms). The third term, by the wedge formula of [[Thm - Hodge Star and the Exterior Product]], is $\varepsilon(\vec u, \vec b, \cdot, \cdot) = \star(u^\flat\wedge b^\flat)$. Hence
> $$A = u^\flat\wedge q + \star(u^\flat\wedge b^\flat).$$
> To recover $\vec b$ from $A$, take the Hodge star: $\star A = \star(u^\flat\wedge q) + \star\star(u^\flat\wedge b^\flat) = \varepsilon(\vec u, \vec q^\sharp, \cdot, \cdot) - u^\flat\wedge b^\flat$ (using $\star^2 = -1$ on the $2$-form $u^\flat\wedge b^\flat$). Evaluate the first argument at $\vec u$: the term $\varepsilon(\vec u, \vec q^\sharp, \vec u, \cdot) = 0$ (repeated $\vec u$ in the alternating $\varepsilon$), and $(u^\flat\wedge b^\flat)(\vec u, \cdot) = \langle u^\flat, \vec u\rangle b^\flat - \langle b^\flat, \vec u\rangle u^\flat = b^\flat$ (using $\langle u^\flat, \vec u\rangle = \vec u\cdot\vec u = 1$ and $\langle b^\flat, \vec u\rangle = \vec b\cdot\vec u = 0$). Therefore $\star A(\vec u, \cdot) = b^\flat$, i.e. $\vec b = \star A(\vec u, \cdot)^\sharp$. In components, using $(\star A)_{\alpha\beta} = \tfrac12\varepsilon_{\mu\nu\alpha\beta}A^{\mu\nu}$ and raising, $b^\alpha = (\star A)^\alpha{}_\rho u^\rho = -\tfrac12\varepsilon^{\alpha\mu\nu}{}_\rho A_{\mu\nu}u^\rho$ (the sign from the index ordering of $\varepsilon$). Uniqueness of $q$ and $\vec b$ is inherited from the uniqueness in eq 3.37.
>
> **Self-dual / anti-self-dual decomposition.** By Lemma 2, $\star^2 = -1$ on $\mathscr{A}_2(E)$, so $\star$ is diagonalisable over $\mathbb{C}$ with eigenvalues $\pm i$. By Lemma 3, $P^\pm = \tfrac12(1 \mp i\star)$ are complementary projectors onto the eigenspaces $\mathscr{A}_2^\pm$, each of complex dimension $3$, giving $\mathscr{A}_2(E)_\mathbb{C} = \mathscr{A}_2^+\oplus\mathscr{A}_2^-$. For a real $2$-form $A$, its projections are $A^\pm = P^\pm A = \tfrac12(A \mp i\star A)$, and by Lemma 4 these are built from the complex combinations $\mathbf e \pm i\mathbf b$ of the electric and magnetic parts relative to any observer. The two subspaces are orthogonal with respect to the complex-bilinear extension of the inner product on forms, because they are eigenspaces of $\star$ (which is self-adjoint up to the sign $\star^2 = -1$) for distinct eigenvalues. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The angular-momentum and spin vectors.** Gourgoulhon's Examples 14.11–14.12 are exactly the magnetic-part construction: the [[Def - Spin Four-Vector|angular-momentum vector]] of a particle relative to an observer is $\boldsymbol\sigma_C = \star J_C(\vec u_0, \cdot)$, and the spin vector is $\mathbf s = \star S(\vec u, \cdot)$, where $J_C$ and $S$ are the angular-momentum and spin $2$-forms. The application is the same theorem with $A = J_C$ or $S$; it shows the "vector" forms of angular momentum and spin are Hodge duals of $2$-forms relative to an observer.

**The Riemann-Silberstein vector and the photon.** The combination $\mathbf F = \mathbf E + i\mathbf B$ is the self-dual part of the field strength relative to a lab frame, and Maxwell's source-free equations become $i\partial_t\mathbf F = \nabla\times\mathbf F$ — a single first-order equation that is the closest classical analogue of a one-particle Schrödinger equation for the photon. Positive and negative helicity are the self-dual and anti-self-dual parts. The application is out-of-distribution because it recasts classical electromagnetism as a complex wave equation forced by $\star^2 = -1$.

**Self-dual gauge fields and integrability.** In Euclidean signature the self-duality equation $\star F = F$ (real, since $\star^2 = +1$ there) defines instantons and is integrable by twistor methods. In Lorentzian signature the analogous complex self-dual fields $\star F = iF$ underlie the spinor-helicity formalism of scattering amplitudes, where a positive-helicity gluon is a self-dual field strength. The application connects the Hodge star's eigenvalue to the helicity organisation of modern amplitude calculations.

---

# Bridges

- **[[Thm - The Complexification of so(1,3) and the (A,B) Decomposition]]** — the self-dual/anti-self-dual split of $2$-forms is the *same* $\pm i$ decomposition as the complexification $\mathfrak{so}(1,3)_\mathbb{C}\cong\mathfrak{su}(2)\oplus\mathfrak{su}(2)$. A $2$-form transforms in the adjoint of the Lorentz group, which is $(1,0)\oplus(0,1)$; the self-dual part is the $(1,0)$ summand, the anti-self-dual the $(0,1)$. The generators $\mathbf J \pm i\mathbf K$ that diagonalise the algebra are the algebraic image of the projectors $\tfrac12(1\mp i\star)$ that diagonalise $\star$ on forms — one decomposition, two incarnations.

- **[[Thm - Orthogonal Decomposition of Antisymmetric Bilinear Forms]]** — the observer decomposition here is the compact, wedge-and-star form of that earlier theorem (Gourgoulhon §3.5.2), which established that a unit timelike vector splits any antisymmetric bilinear form into a one-form and a vector in the rest space. This theorem rewrites $\varepsilon(\vec u, \vec b, \cdot, \cdot)$ as $\star(u^\flat\wedge b^\flat)$ using the Hodge machinery, making the magnetic part manifestly a Hodge dual.

- **[[Special Relativity XXI — The Electromagnetic Field|The electromagnetic field]]** — applied to the field strength $F$, the observer decomposition *is* the splitting of $F$ into the electric and magnetic fields $(\mathbf E, \mathbf B)$ measured by an observer, and the self-dual decomposition is the $\mathbf E \pm i\mathbf B$ structure whose squared length $(\mathbf E + i\mathbf B)^2$ packages both field invariants $\mathbf B^2 - \mathbf E^2$ and $\mathbf E\cdot\mathbf B$ into one complex number. The transformation of $\mathbf E, \mathbf B$ under a boost is the change of the observer in the first decomposition.

---

# Unlocked by This

> [!tip] Field Invariants and the Classification of Electromagnetic Fields *(from Electromagnetism)*
> The squared length of the self-dual part, $(\mathbf E + i\mathbf B)^2 = (\mathbf E^2 - \mathbf B^2) + 2i\,\mathbf E\cdot\mathbf B$, is a single complex Lorentz invariant whose real and imaginary parts are the two field invariants $F_{\mu\nu}F^{\mu\nu}$ and $\star F_{\mu\nu}F^{\mu\nu}$. A field is **null** (radiation) exactly when this complex invariant vanishes — both $\mathbf E^2 = \mathbf B^2$ and $\mathbf E\perp\mathbf B$ — which is the self-dual part being a null complex vector; see [[Special Relativity XXI — The Electromagnetic Field]].

> [!tip] Helicity, Spinor-Helicity, and Twistors *(from QFT and Amplitudes)*
> The self-dual and anti-self-dual field strengths are the two **helicities** of the photon, and in the spinor formalism they are written with two undotted or two dotted spinor indices, $F^+_{AB}$ and $F^-_{\dot A\dot B}$ — the field-strength avatar of the $(1,0)$ and $(0,1)$ Weyl representations. This is the entry point to the spinor-helicity and twistor methods that make modern scattering-amplitude computations tractable; see [[Special Relativity XI — SL(2,C), Spinors and the Spinor Map]].
