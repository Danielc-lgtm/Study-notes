---
type: theorem
subject: commutative-algebra
prereqs:
  - "Thm - Zariski's Lemma"
  - "Def - Affine Variety and the Vanishing Set"
  - "Def - Prime and Maximal Ideal"
  - "Def - Polynomial Ring"
  - "Thm - Maximal and Prime Ideals via Quotients"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. We keep the chapter's standing data: a field $k$, an algebraically closed extension $\Omega \supseteq k$, affine space $\Omega^n$, the vanishing operation $V$ ([[Def - Affine Variety and the Vanishing Set]]). For an ideal $\mathfrak a \trianglelefteq k[T_1, \dots, T_n]$, $V(\mathfrak a) = \{x \in \Omega^n : f(x) = 0\ \forall f \in \mathfrak a\}$. We write $\operatorname{mSpec}$ for the set of maximal ideals; $\mathfrak m_x = (T_1 - x_1, \dots, T_n - x_n)$ for the ideal of a point $x \in \Omega^n$. A $k$-algebra homomorphism $\varphi : k[T_1, \dots, T_n] \to \Omega$ is determined by the images $x_i := \varphi(T_i)$, and then $\varphi(f) = f(x)$ — evaluation at $x = (x_1, \dots, x_n)$. The full registry is on [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz]].

---

# Statement

> **Theorem (Weak Nullstellensatz).** Let $k$ be a field, $\Omega \supseteq k$ algebraically closed, and $\mathfrak a$ an ideal of $k[T_1, \dots, T_n]$. Then
> $$V(\mathfrak a) = \varnothing \quad \Longleftrightarrow \quad 1 \in \mathfrak a \quad (\text{i.e. } \mathfrak a = k[T_1, \dots, T_n]).$$
> Contrapositively: **a proper ideal has a nonempty zero set.** Every system of polynomial equations with no common solution in $\Omega^n$ must already be "inconsistent over the ring" — there are $p_1, \dots, p_t$ with $\sum p_i f_i = 1$.

> **Point form (over an algebraically closed base $k = \Omega$).** The maximal ideals of $\Omega[T_1, \dots, T_n]$ are exactly the ideals $\mathfrak m_x = (T_1 - x_1, \dots, T_n - x_n)$ for $x \in \Omega^n$, and $x \mapsto \mathfrak m_x$ is a bijection $\Omega^n \xrightarrow{\ \sim\ } \operatorname{mSpec}\, \Omega[T_1, \dots, T_n]$. **Points are maximal ideals.**

The two forms are equivalent: "every proper ideal has a zero" is the same as "every maximal ideal is a point", because a maximal ideal is proper and is the largest such, and a point of $V(\mathfrak m)$ recovers $\mathfrak m$ as $\mathfrak m_x$.

---

# Motivation

The weak Nullstellensatz is the *existence theorem* for solutions of polynomial systems, and it is the algebraic-geometry analogue of the fundamental theorem of algebra. The fundamental theorem says one polynomial in one variable over $\mathbb{C}$ has a root; the weak Nullstellensatz says *any consistent finite system* of polynomials in *any number* of variables over an algebraically closed field has a common root. "Consistent" gets the precise algebraic meaning "$1 \notin \mathfrak a$": the only obstruction to a common solution is the trivial one, that you can algebraically derive $1 = 0$ from the equations (a Bézout combination $\sum p_i f_i = 1$). If you cannot derive a contradiction in the ring, then a genuine geometric solution exists. This is a remarkable rigidity: algebraic consistency forces geometric solvability.

The "point form" is where the theorem becomes the cornerstone of the algebra–geometry dictionary. Over an algebraically closed field, *the maximal ideals of the polynomial ring are exactly the points of affine space.* You can throw away the set $\Omega^n$ entirely and replace it by $\operatorname{mSpec}\, \Omega[T_1, \dots, T_n]$ — the geometry is fully encoded in the ring. The map "point $x$ $\mapsto$ ideal $\mathfrak m_x$ of functions vanishing at $x$" is a perfect bijection, and it is the seed of "spaces are their rings of functions". Every later correspondence — radical ideals to varieties, primes to irreducible varieties — is a thickening of this single fact about closed points.

Why is the weak form "weak"? Because it only detects whether a variety is *empty*. It says nothing yet about *which* functions vanish on a nonempty variety — that is the **strong** Nullstellensatz, which computes $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$. But the strong form is deduced from the weak form by a clever trick (Rabinowitsch), so the weak form carries all the existential content. Get the weak form, and the dictionary is essentially built.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\mathfrak a$ is an ideal of a polynomial ring over $k$, and $\Omega \supseteq k$ is algebraically closed". The recognition is usually about *which* form to invoke.

The first disguised source is **"a system $f_1 = \dots = f_t = 0$ has no solution in $\Omega^n$"**. The bridge: no solution means $V((f_1, \dots, f_t)) = \varnothing$, so by the weak Nullstellensatz $1 \in (f_1, \dots, f_t)$, giving an explicit certificate $\sum p_i f_i = 1$. The non-obvious value is that *unsolvability is certifiable by an algebraic identity* — the basis of automated theorem-proving over algebraically closed fields. *Example problem:* show three polynomials with no common zero generate the unit ideal.

The second disguised source is **"$\mathfrak m$ is a maximal ideal of $\Omega[T_1, \dots, T_n]$"**. The bridge: maximal ideals are points, so $\mathfrak m = \mathfrak m_x$ for a unique $x \in \Omega^n$. The non-obvious payoff is that one can *list* all maximal ideals concretely as $(T_1 - x_1, \dots, T_n - x_n)$. *Example problem:* [[Ex - Maximal ideals of a polynomial ring over an algebraically closed field|classify the maximal ideals of $\mathbb{C}[X, Y]$]].

The third disguised source is **"I have a finitely generated $\Omega$-algebra $A$ and want a point / a $\Omega$-algebra homomorphism $A \to \Omega$"**. Writing $A = \Omega[T]/\mathfrak a$, a homomorphism $A \to \Omega$ is a point of $V(\mathfrak a)$, which exists iff $\mathfrak a$ is proper. The bridge is the weak Nullstellensatz applied to $\mathfrak a$. *Example problem:* every nonzero finitely generated $\Omega$-algebra admits a homomorphism onto $\Omega$ (has a "rational point").

**Targets (Output Amplification)**

The conclusion is "$V(\mathfrak a) = \varnothing \iff 1 \in \mathfrak a$", or equivalently "maximal ideals are points".

Combine with **the Rabinowitsch trick**. Adjoin a variable $T_{n+1}$ and the polynomial $T_{n+1}f - 1$ to force $f \neq 0$ on the locus; applying the weak Nullstellensatz to the enlarged ideal yields $f \in \sqrt{\mathfrak a}$ whenever $f$ vanishes on $V(\mathfrak a)$. The further result $E$ is the **[[Thm - The Strong Nullstellensatz|strong Nullstellensatz]]** $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$ — the weak form is the *whole* input to the strong form.

Combine with **the order-reversing bijection setup**. "Maximal ideals are points" plus "$V(\mathfrak a) = \varnothing \iff \mathfrak a = R$" feeds the [[Thm - The Nullstellensatz Correspondence (radical ideals and varieties)|radical-ideal/variety correspondence]]: the *closed points* of $\operatorname{Spec}$ are the classical points, and the correspondence restricts to a bijection {points} $\leftrightarrow$ {maximal ideals}. The further result $E$ is the bottom rung of the full dictionary.

Combine with **finite fibre / point-counting over finite fields**. Over $\Omega = \overline{\mathbb{F}_p}$, a maximal ideal of $\mathbb{F}_p[T]$ has residue field a finite extension $\mathbb{F}_{p^d}$; the point lives in $\overline{\mathbb{F}_p}^n$ with coordinates in $\mathbb{F}_{p^d}$. The further result $E$, combined with Galois action, organises points into Frobenius orbits and underlies zeta-function point counts — the arithmetic of [[Ex - Why algebraic closure is needed in the Nullstellensatz|reduction mod p, ES3 Q8]].

---

# Why Is It True

The whole theorem is **Zariski's lemma plus the observation that a maximal ideal of $\Omega[T]$ has residue field $\Omega$.** Once you see that, everything is forced.

**The bolded one-liner: a maximal ideal gives a field quotient that is finitely generated as a $k$-algebra, hence finite over $k$ by Zariski's lemma, hence (over algebraically closed $\Omega$) equal to $\Omega$ — so the quotient map is "evaluation at a point", and that point lies in $V(\mathfrak a)$.**

Here is the mechanism for the "$\Leftarrow$ direction" / contrapositive (the content). Suppose $\mathfrak a$ is proper. It is contained in some maximal ideal $\mathfrak m$ (every proper ideal is, by Zorn). The quotient $k[T_1, \dots, T_n]/\mathfrak m$ is a field ([[Thm - Maximal and Prime Ideals via Quotients|maximal ⟹ field quotient]]) and is finitely generated as a $k$-algebra (generated by the images of the $T_i$). By [[Thm - Zariski's Lemma|Zariski's lemma]] it is a *finite* extension of $k$, hence embeds $k$-linearly into the algebraically closed $\Omega$ (every finite extension of $k$ does). Compose:
$$\varphi : k[T_1, \dots, T_n] \twoheadrightarrow k[T]/\mathfrak m \hookrightarrow \Omega.$$
This $\varphi$ is a $k$-algebra homomorphism to $\Omega$, so it is *evaluation at the point* $x := (\varphi(T_1), \dots, \varphi(T_n)) \in \Omega^n$: indeed $\varphi(f) = f(x)$ for all $f$. Its kernel contains $\mathfrak m \supseteq \mathfrak a$, so for every $f \in \mathfrak a$, $f(x) = \varphi(f) = 0$. Thus $x \in V(\mathfrak a)$, and $V(\mathfrak a) \neq \varnothing$.

The reason this works and is forced: **a $k$-algebra homomorphism out of a polynomial ring is the same data as a point** ($\varphi \leftrightarrow x = (\varphi(T_i))$, with $\varphi = \operatorname{ev}_x$). So "finding a common solution" $=$ "finding a homomorphism to $\Omega$" $=$ "finding a maximal ideal with residue field embeddable in $\Omega$". Zariski's lemma guarantees the residue field is small enough (finite over $k$) to embed, and algebraic closure of $\Omega$ guarantees the embedding exists. The empty-zero-set obstruction is exactly the failure of these — i.e. $\mathfrak a = R$, no maximal ideal above it that is proper.

The "$\Rightarrow$ direction" ($1 \in \mathfrak a \Rightarrow V(\mathfrak a) = \varnothing$) is trivial: if $1 = \sum p_i f_i$ with $f_i \in \mathfrak a$, then at any putative solution $x$, $1 = \sum p_i(x) f_i(x) = 0$, absurd.

---

# What Makes This Hard

The difficulty is entirely in [[Thm - Zariski's Lemma|Zariski's lemma]] — once that is granted, the weak Nullstellensatz is a short deduction, and the common mistake is to underestimate how much work the lemma is doing. The non-obvious conceptual step is the identification **"$k$-algebra homomorphism $k[T] \to \Omega$" = "point of $\Omega^n$"**, via $\varphi \mapsto (\varphi(T_i))$ and $\varphi(f) = f(\varphi(T))$; readers new to the subject often do not see that a homomorphism *is* a point. The role of algebraic closure is the second subtlety: Zariski gives a finite extension, and closure is needed to *embed* that finite field into $\Omega$ (and, when $k = \Omega$, to collapse it to $\Omega$). Omitting "algebraically closed" is the standard error — over $\mathbb{R}$, $(T^2+1)$ is a proper (maximal) ideal with empty zero set, and the theorem is false.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
The forward direction is the trivial substitution argument. For the contrapositive, embed $\mathfrak a$ in a maximal ideal $\mathfrak m$; the field $k[T]/\mathfrak m$ is finite over $k$ by Zariski's lemma, embeds into $\Omega$, and the composite homomorphism $k[T] \to \Omega$ is evaluation at a point of $V(\mathfrak a)$.

**Subgoal decomposition:**

1. **Trivial direction.** $1 \in \mathfrak a \Rightarrow V(\mathfrak a) = \varnothing$.
   - *Hint:* Evaluate a Bézout identity $\sum p_i f_i = 1$ at any candidate point.
   - *Why needed:* One half of the iff.

2. **Embed in a maximal ideal.** A proper $\mathfrak a$ lies in some maximal $\mathfrak m$ (Zorn).
   - *Hint:* Every proper ideal of a nonzero ring is contained in a maximal ideal.
   - *Why needed:* Replaces $\mathfrak a$ by a maximal ideal with a field quotient.

3. **The residue field is finite over $k$.** $k[T]/\mathfrak m$ is a field, finitely generated as a $k$-algebra, so finite over $k$ by [[Thm - Zariski's Lemma|Zariski]].
   - *Hint:* Maximal $\Rightarrow$ field quotient; images of $T_i$ generate it as an algebra.
   - *Why needed:* Makes the quotient small enough to embed into $\Omega$.

4. **Embed into $\Omega$ and read off a point.** A finite extension of $k$ embeds $k$-linearly into algebraically closed $\Omega$; the composite $\varphi : k[T] \to \Omega$ satisfies $\varphi(f) = f(x)$ for $x = (\varphi(T_i))$, and $\ker \varphi \supseteq \mathfrak a$, so $x \in V(\mathfrak a)$.
   - *Hint:* A homomorphism from a polynomial ring is evaluation at the image-tuple.
   - *Why needed:* Produces the solution point; uses algebraic closure.

---

# Lemma Decomposition

> [!note]- Lemma 1: A homomorphism out of a polynomial ring is evaluation at a point
> **Statement:** A $k$-algebra homomorphism $\varphi : k[T_1, \dots, T_n] \to \Omega$ is determined by $x := (\varphi(T_1), \dots, \varphi(T_n)) \in \Omega^n$, and then $\varphi(f) = f(x)$ for all $f$. Conversely every $x \in \Omega^n$ gives such a $\varphi = \operatorname{ev}_x$.
>
> **Hint:** A $k$-algebra homomorphism preserves $+, \times$ and fixes $k$; a polynomial is built from $T_i$ and scalars by these operations.
>
> **Why needed:** It is the identification "homomorphism = point" that turns the algebraic conclusion (a homomorphism to $\Omega$ exists) into the geometric one (a solution point exists).
>
> > [!note]- Full proof
> > Since $\varphi$ fixes $k$ and is a ring homomorphism, for $f = \sum_\alpha a_\alpha T^\alpha$ ($a_\alpha \in k$) we have $\varphi(f) = \sum_\alpha a_\alpha \varphi(T_1)^{\alpha_1} \cdots \varphi(T_n)^{\alpha_n} = \sum_\alpha a_\alpha x^\alpha = f(x)$. So $\varphi$ is determined by $x$, and equals $\operatorname{ev}_x$. Conversely, for any $x \in \Omega^n$, $\operatorname{ev}_x : f \mapsto f(x)$ is a $k$-algebra homomorphism (evaluation respects sums and products).

> [!note]- Lemma 2: The residue field at a maximal ideal embeds into $\Omega$
> **Statement:** For a maximal ideal $\mathfrak m \trianglelefteq k[T_1, \dots, T_n]$, the field $k[T]/\mathfrak m$ is finite over $k$, and there is a $k$-algebra embedding $k[T]/\mathfrak m \hookrightarrow \Omega$.
>
> **Hint:** Zariski's lemma gives finiteness; field theory gives that a finite (algebraic) extension of $k$ embeds into any algebraically closed $\Omega \supseteq k$.
>
> **Why needed:** Without the embedding into $\Omega$ there is no point in $\Omega^n$; this is exactly where algebraic closure of $\Omega$ is used.
>
> > [!note]- Full proof
> > $k[T]/\mathfrak m$ is a field ([[Thm - Maximal and Prime Ideals via Quotients|maximal ideals have field quotients]]), and finitely generated as a $k$-algebra by the images of $T_1, \dots, T_n$, so by [[Thm - Zariski's Lemma|Zariski's lemma]] it is a finite, hence algebraic, extension $L$ of $k$. Every element of $L$ is algebraic over $k$, so satisfies a polynomial over $k$, which splits in $\Omega$; building the embedding generator-by-generator (each algebraic element maps to a root of its minimal polynomial in $\Omega$, available because $\Omega$ is algebraically closed) yields a $k$-algebra embedding $L \hookrightarrow \Omega$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\mathfrak a \trianglelefteq R := k[T_1, \dots, T_n]$ and $\Omega \supseteq k$ algebraically closed.
>
> **($\Rightarrow$, the trivial direction.)** Suppose $1 \in \mathfrak a$, say $1 = \sum_i p_i f_i$ with $f_i \in \mathfrak a$. If some $x \in \Omega^n$ lay in $V(\mathfrak a)$, then $f_i(x) = 0$ for all $i$, so $1 = \sum_i p_i(x) f_i(x) = 0$ in $\Omega$, a contradiction. Hence $V(\mathfrak a) = \varnothing$.
>
> **($\Leftarrow$, the substance.)** Suppose $\mathfrak a$ is proper, $1 \notin \mathfrak a$. Then $\mathfrak a$ is contained in a maximal ideal $\mathfrak m$ of $R$ (Zorn's lemma). By **Lemma 2**, the residue field $R/\mathfrak m$ is finite over $k$ and admits a $k$-algebra embedding $\sigma : R/\mathfrak m \hookrightarrow \Omega$. Let $\pi : R \to R/\mathfrak m$ be the quotient map and set $\varphi := \sigma \circ \pi : R \to \Omega$, a $k$-algebra homomorphism with $\ker \varphi = \mathfrak m$ (since $\sigma$ is injective and $\ker \pi = \mathfrak m$).
>
> By **Lemma 1**, $\varphi = \operatorname{ev}_x$ for $x := (\varphi(T_1), \dots, \varphi(T_n)) \in \Omega^n$, i.e. $\varphi(f) = f(x)$. For every $f \in \mathfrak a \subseteq \mathfrak m = \ker \varphi$, we get $f(x) = \varphi(f) = 0$. Hence $x \in V(\mathfrak a)$ and $V(\mathfrak a) \neq \varnothing$.
>
> **Point form.** When $k = \Omega$, $R/\mathfrak m$ is finite over $\Omega$, hence equals $\Omega$ (algebraically closed fields have no proper finite extensions), so $\varphi : R \to \Omega$ is surjective with kernel $\mathfrak m$ and $\varphi = \operatorname{ev}_x$. Then $\mathfrak m = \ker \operatorname{ev}_x \supseteq (T_1 - x_1, \dots, T_n - x_n) = \mathfrak m_x$; since $\mathfrak m_x$ is itself maximal ($\Omega[T]/\mathfrak m_x \cong \Omega$) and $\mathfrak m$ is proper, $\mathfrak m = \mathfrak m_x$. So every maximal ideal is some $\mathfrak m_x$; and distinct points give distinct ideals ($\mathfrak m_x = \mathfrak m_y \Rightarrow x_i \equiv y_i$ for all $i \Rightarrow x = y$). The map $x \mapsto \mathfrak m_x$ is a bijection $\Omega^n \to \operatorname{mSpec} R$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Consistency of polynomial systems / Positivstellensatz cousins.** Over $\mathbb{C}$, the weak Nullstellensatz says a system is unsolvable iff $1$ is in the ideal — a *decidable* condition via Gröbner bases. Use it to decide solvability of a concrete system, e.g. show $\{x^2 + y^2 + 1,\ x + y,\ x - y\}$ has no complex common zero by finding the Bézout combination. The application is nonobvious because it converts a geometric search into an ideal-membership computation, the basis of computational algebraic geometry.

**Common eigenvectors and simultaneous solvability.** A family of commuting operators over $\mathbb{C}$ has a common eigenvector; the eigenvalue tuple is a common solution of the characteristic-type equations, whose existence is the weak Nullstellensatz applied to the algebra generated by the operators. The application battle-tests the source "homomorphism to $\Omega$ = point" in a linear-algebra context.

**Rational points and the field of definition.** Over $\Omega = \overline{\mathbb{Q}}$, the weak Nullstellensatz produces solutions with *algebraic* coordinates; the *smallest field* over which a solution exists is a finite extension of $\mathbb{Q}$, controlled by the residue field of the maximal ideal. The application is nonobvious because it ties the existence theorem to Galois theory and the **field of definition** of a point, the arithmetic refinement that classical geometry over $\mathbb{C}$ hides.

---

# Bridges

- **[[Thm - Zariski's Lemma|Zariski's Lemma]]** — the engine. The weak Nullstellensatz is "Zariski's lemma applied to a residue field, then embedded into $\Omega$". Zariski supplies finiteness of $k[T]/\mathfrak m$ over $k$; algebraic closure supplies the embedding into $\Omega$; Lemma 1 reads the embedding as a point. The entire nontrivial content is in Zariski.

- **[[Thm - Maximal and Prime Ideals via Quotients|Maximal ideals via quotients]]** — the bridge from "maximal ideal" to "field". The proof needs that $k[T]/\mathfrak m$ is a *field* to invoke Zariski's lemma; that is exactly "maximal $\iff$ field quotient", imported from [[Rings II — §2.3–2.4|Rings]]. The point form refines this: maximal ideals are not just field quotients but, over $\Omega$, residue field $= \Omega$, i.e. *points*.

- **[[Thm - The Strong Nullstellensatz|The Strong Nullstellensatz]]** — the upgrade. The strong form $I(V(\mathfrak a)) = \sqrt{\mathfrak a}$ is deduced from the weak form by the Rabinowitsch trick (adjoin $T_{n+1}$ with $T_{n+1}f - 1$). So the weak form is logically prior and carries all the existence content; the strong form is a packaging that identifies *which* functions vanish.

- **[[Def - Affine Variety and the Vanishing Set|The vanishing set]]** — the object. The theorem is the statement that the geometry-side map $V$ does not collapse proper ideals to $\varnothing$ (over $\Omega$ closed): $V$ is "faithful on emptiness". This is what makes $V$ and $I$ inverse on the right objects.

---

# Unlocked by This

> [!tip] Points are maximal ideals: the foundation of the variety–ring dictionary *(from Algebraic Geometry)*
> The point form — $\Omega^n \xrightarrow{\sim} \operatorname{mSpec} \Omega[T_1, \dots, T_n]$, $x \mapsto \mathfrak m_x$ — is the bedrock identification of algebraic geometry: **a geometric point is a maximal ideal of the coordinate ring**, and "the value of $f$ at $x$" is the image of $f$ in the residue field $\Omega[T]/\mathfrak m_x = \Omega$. For any affine variety $X$ with coordinate ring $\Omega[X]$, the points of $X$ are exactly the maximal ideals of $\Omega[X]$. This is what lets the entire geometry be reconstructed from the ring, and it is the closed-point stratum of $\operatorname{Spec}$; the **scheme**-theoretic refinement keeps *all* primes, the extra (non-closed) ones being the generic points of positive-dimensional subvarieties.

> [!tip] Effective and arithmetic Nullstellensatz *(from Computational and Arithmetic Geometry)*
> The Bézout certificate $\sum p_i f_i = 1$ for an inconsistent system can be taken with *bounded degree*: the **effective Nullstellensatz** gives $\deg p_i \leq (\max\{3, \deg f_j\})^n$, turning solvability into a finite system of linear equations in the coefficients of the $p_i$ — solvable by Gaussian elimination, an *algorithm* deciding emptiness of a variety. Over $\mathbb{Z}$ one gets height bounds (the **arithmetic Nullstellensatz**) controlling the size of coefficients, central to reduction-mod-$p$ techniques ([[Ex - Why algebraic closure is needed in the Nullstellensatz|ES3 Q8]]) and to bounding solutions of Diophantine systems.
