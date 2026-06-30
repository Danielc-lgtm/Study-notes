---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Natural Transformation"
  - "Def - Determinant"
  - "Def - Functor"
tags: [category-theory, foundations]
---

# Problem Statement

Fix $n \geq 1$. For each commutative [[Def - Ring|ring]] $R$, the [[Def - Determinant|determinant]] is a [[Def - Homomorphism|group homomorphism]] $\det_R : \mathrm{GL}_n(R) \to R^\times$ from the invertible $n \times n$ matrices over $R$ to the units of $R$. Show that, as $R$ ranges over $\mathbf{CRing}$, the determinant is a [[Def - Natural Transformation|natural transformation]]
$$\det : \mathrm{GL}_n \Longrightarrow (-)^\times$$
between the functors $\mathrm{GL}_n, (-)^\times : \mathbf{CRing} \to \mathbf{Grp}$. That is, verify that for every ring homomorphism $\varphi : R \to S$ the naturality square commutes:
$$\varphi^\times \circ \det_R = \det_S \circ \mathrm{GL}_n(\varphi),$$
where $\mathrm{GL}_n(\varphi)$ applies $\varphi$ entrywise and $\varphi^\times$ is $\varphi$ restricted to units.

**Recall:**

The [[Def - Determinant|determinant]] of an $n \times n$ matrix is the polynomial $\det(A) = \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) \prod_{i} A_{i,\sigma(i)}$ in its entries; over any commutative ring it satisfies $\det(AB) = \det(A)\det(B)$, so it restricts to a homomorphism on invertible matrices. ![[Def - Natural Transformation#The Definition]]

---

# Convergent Strategy

**Problem class:** This is a "verify naturality of a uniform formula" exercise. The route is to recognize that $\mathrm{GL}_n$ and $(-)^\times$ are functors $\mathbf{CRing} \to \mathbf{Grp}$, then check the naturality square reduces to "$\varphi$ commutes with the determinant polynomial".

**Assumption pattern:** The leverage is that the determinant is a *fixed polynomial in the matrix entries with integer coefficients*, and a ring homomorphism $\varphi$ preserves $+$ and $\times$ and fixes integer coefficients. So applying $\varphi$ after computing $\det$ equals computing $\det$ after applying $\varphi$ entrywise — naturality is "polynomials commute with ring [[Def - Homomorphism|homomorphisms]]".

**Theorem routing:** First confirm $\mathrm{GL}_n$ and $(-)^\times$ are functors (a ring map induces a [[Def - Group|group]] map on matrices and on units). Then the naturality square is the identity $\varphi(\det_R(A)) = \det_S(\varphi(A))$, proved by pushing $\varphi$ through the determinant sum.

**Key decision point:** The conceptual realization is that "the determinant is the same formula in every ring" is *precisely* the statement of naturality — the uniformity of the formula across [[Def - Ring|rings]] is what makes the square commute. The decision is to verify naturality at the level of the defining polynomial rather than case by case.

---

# Legal Operations Used

1. **Operation: recognize parallel functors and form the naturality square** (topic page, Legal Operation 10). Identify $\mathrm{GL}_n, (-)^\times : \mathbf{CRing} \to \mathbf{Grp}$ and write the square for $\varphi$.

2. **Operation: push a ring homomorphism through a polynomial** (topic page, Legal Operation 4). $\varphi$ commutes with $+, \times$ and fixes $\mathbb{Z}$-coefficients, so it commutes with $\det$.

---

# Hints

> [!note]- Hint 1
> First check $\mathrm{GL}_n$ is a functor $\mathbf{CRing} \to \mathbf{Grp}$: a ring map $\varphi : R \to S$ applied entrywise sends an invertible matrix to an invertible matrix and is a group homomorphism. Same for $(-)^\times$.

> [!note]- Hint 2
> The naturality square for $\varphi : R \to S$ reads $\varphi^\times(\det_R(A)) = \det_S(\mathrm{GL}_n(\varphi)(A))$. Write $\det$ as the polynomial sum and apply $\varphi$ to it.

> [!note]- Hint 3
> $\varphi$ preserves sums and products and fixes the coefficients $\mathrm{sgn}(\sigma) \in \{\pm 1\} \subseteq \mathbb{Z}$. So $\varphi\big(\sum_\sigma \mathrm{sgn}(\sigma)\prod_i A_{i\sigma(i)}\big) = \sum_\sigma \mathrm{sgn}(\sigma)\prod_i \varphi(A_{i\sigma(i)})$ — which is $\det$ of the matrix with entries $\varphi(A_{ij})$.

---

# Solution

The plan: confirm $\mathrm{GL}_n$ and $(-)^\times$ are functors $\mathbf{CRing} \to \mathbf{Grp}$, then verify the naturality square by pushing $\varphi$ through the determinant polynomial. The whole computation is "a ring homomorphism commutes with a fixed integer polynomial".

**Step 1: $\mathrm{GL}_n$ and $(-)^\times$ are functors $\mathbf{CRing} \to \mathbf{Grp}$.**

> [!note]- Derivation
> *$(-)^\times$:* sends $R \mapsto R^\times$ (its group of units) and a ring homomorphism $\varphi : R \to S$ to its restriction $\varphi^\times : R^\times \to S^\times$ — a unit $u$ with inverse $u^{-1}$ maps to $\varphi(u)$ with inverse $\varphi(u^{-1})$, so $\varphi(u) \in S^\times$, and $\varphi^\times$ is a group homomorphism. Functoriality is inherited from $\varphi$.
>
> *$\mathrm{GL}_n$:* sends $R \mapsto \mathrm{GL}_n(R)$ and $\varphi$ to $\mathrm{GL}_n(\varphi)$, the entrywise application $A \mapsto (\varphi(A_{ij}))$. This preserves matrix products ($\varphi$ is a ring map, so $\varphi(\sum_k A_{ik}B_{kj}) = \sum_k \varphi(A_{ik})\varphi(B_{kj})$) and sends $I$ to $I$, so it is a monoid homomorphism on matrices; it sends invertible matrices to invertible matrices (apply it to $A A^{-1} = I$), hence is a group homomorphism on $\mathrm{GL}_n$. Functoriality is inherited. So both are functors $\mathbf{CRing} \to \mathbf{Grp}$.

**Step 2: The naturality square commutes.**

> [!note]- Derivation
> Fix $\varphi : R \to S$ and $A = (A_{ij}) \in \mathrm{GL}_n(R)$. Compute the two legs.
>
> Down-then-right ($\det_S \circ \mathrm{GL}_n(\varphi)$): first apply $\varphi$ entrywise to get the matrix $\varphi(A) := (\varphi(A_{ij})) \in \mathrm{GL}_n(S)$, then take its determinant:
> $$\det_S(\varphi(A)) = \sum_{\sigma \in S_n} \mathrm{sgn}(\sigma) \prod_{i=1}^n \varphi(A_{i,\sigma(i)}).$$
> Right-then-down ($\varphi^\times \circ \det_R$): first take the determinant in $R$, then apply $\varphi$:
> $$\varphi\big(\det_R(A)\big) = \varphi\Big(\sum_{\sigma} \mathrm{sgn}(\sigma)\prod_i A_{i,\sigma(i)}\Big) = \sum_\sigma \mathrm{sgn}(\sigma)\,\varphi\Big(\prod_i A_{i,\sigma(i)}\Big) = \sum_\sigma \mathrm{sgn}(\sigma)\prod_i \varphi(A_{i,\sigma(i)}),$$
> where the second equality uses that $\varphi$ preserves sums and fixes the integer coefficients $\mathrm{sgn}(\sigma) \in \{\pm1\}$, and the third uses that $\varphi$ preserves products. The two legs are *identical*, so
> $$\varphi^\times \circ \det_R = \det_S \circ \mathrm{GL}_n(\varphi),$$
> i.e. the naturality square commutes for every $\varphi$. Hence $\det : \mathrm{GL}_n \Rightarrow (-)^\times$ is a [[Def - Natural Transformation|natural transformation]].

> [!note]- Complete formal solution
> $\mathrm{GL}_n$ and $(-)^\times$ are functors $\mathbf{CRing} \to \mathbf{Grp}$ (entrywise application and restriction to units are group homomorphisms, functorially). For $\varphi : R \to S$ and $A \in \mathrm{GL}_n(R)$,
> $$\varphi(\det_R A) = \varphi\Big(\sum_\sigma \mathrm{sgn}(\sigma)\prod_i A_{i\sigma(i)}\Big) = \sum_\sigma \mathrm{sgn}(\sigma)\prod_i \varphi(A_{i\sigma(i)}) = \det_S(\varphi A),$$
> using that $\varphi$ preserves $+$, $\times$, and the coefficients $\pm 1$. So $\varphi^\times \det_R = \det_S \mathrm{GL}_n(\varphi)$, and $\det$ is a natural transformation. $\blacksquare$

---

# Key Takeaways

**A formula uniform across rings is, by definition, a natural transformation.** The reusable principle is that any construction given by *the same polynomial (or the same universal formula) in every object* is automatically natural, because a morphism — here a ring homomorphism — commutes with the formula. The determinant, the trace, the characteristic polynomial, the symmetric and exterior powers, and indeed every "natural operation" of multilinear algebra are natural transformations for exactly this reason. The trigger: when you define an operation by a single formula that makes sense in every object of a category, you have a natural transformation, and the naturality square is the statement "morphisms commute with the formula" — usually a one-line check.

**Naturality reduces to "ring maps preserve the operations".** The whole computation collapsed because a [[Def - Ring Homomorphism|ring homomorphism]] preserves $+$, $\times$, and the integer coefficients of the determinant polynomial. This is the algebraic source of naturality for any polynomial or rational construction: the structure-preserving maps of the category preserve the operations the construction is built from. Whenever you suspect a uniform algebraic construction is natural, isolate the operations it uses ($+$, $\times$, scalar multiplication, exponentiation) and confirm the morphisms of your category preserve them; if they do, naturality is automatic, and the square need not be drawn case by case.

**Functoriality of the source and target is a prerequisite, not an afterthought.** Before $\det$ can be a natural transformation, $\mathrm{GL}_n$ and $(-)^\times$ must be functors $\mathbf{CRing} \to \mathbf{Grp}$ — and verifying that (entrywise application is a group homomorphism on invertible matrices, restriction to units is a group homomorphism) is genuinely part of the problem. The general lesson: a natural transformation lives *between two functors*, so the first obligation is to pin down both functors and confirm their functoriality; only then does the naturality square make sense. Skipping this step is the most common structural error — writing down components $\alpha_A$ before establishing that the source and target are functors at all.
