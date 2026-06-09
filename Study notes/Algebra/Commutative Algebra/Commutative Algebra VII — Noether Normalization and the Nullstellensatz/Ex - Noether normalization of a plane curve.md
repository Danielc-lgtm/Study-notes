---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Thm - Noether Normalization"
  - "Def - Algebraic Independence and Transcendence Degree"
  - "Def - Integral Element and Integral Extension"
  - "Def - The Coordinate Ring and the Ideal of a Set"
  - "Def - Polynomial Ring"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $k$ be an infinite field and let $A = k[X, Y]/(f)$ be the coordinate ring of a plane curve $C = V(f) \subseteq k^2$, where $f \in k[X, Y]$ is a nonconstant polynomial of degree $d$. 

**(a)** Carry out Noether normalization explicitly: find an element $u \in A$ (a linear combination of the coordinate functions) such that $A$ is a finite module over the polynomial subring $k[u]$, and exhibit the monic integral equation for the other coordinate over $k[u]$.

**(b)** Conclude that $\dim A = \operatorname{trdeg}_k \operatorname{Frac}(A) = 1$ when $f$ is irreducible, recovering the fact that $\operatorname{trdeg}_k k[T_1, \dots, T_n]/(g) = n - 1$ for irreducible $g$ (Example Sheet 4, Question 2, in the case $n = 2$).

Work the concrete case $f = Y^2 - X^3 - X$ (an elliptic curve over, say, $\mathbb{C}$) to illustrate.

**Recall:**

The objects in play are Noether normalization, transcendence degree, integral elements, and the coordinate ring.

![[Thm - Noether Normalization#Statement]]

![[Def - Algebraic Independence and Transcendence Degree#The Definition]]

The **coordinate ring** $A = k[X, Y]/(f)$ is the ring of polynomial functions on $C = V(f)$; write $x, y$ for the images of $X, Y$ in $A$, so $f(x, y) = 0$ ([[Def - The Coordinate Ring and the Ideal of a Set|coordinate ring]]). An element $a \in A$ is **integral** over a subring $B$ if it satisfies a monic polynomial with coefficients in $B$ ([[Def - Integral Element and Integral Extension|integral element]]); $A$ is **finite** over $B$ if it is a finitely generated $B$-module.

---

# Convergent Strategy

**Problem class.** This is a *carry-out-the-normalization-explicitly* problem — the concrete, hands-on face of [[Thm - Noether Normalization|Noether normalization]], where you do the linear change of variables by hand and read off the integral equation. It also computes a *dimension as a transcendence degree*, illustrating $\dim = \operatorname{trdeg}$ for a curve.

**Assumption pattern.** $A = k[X, Y]/(f)$ is a *finitely generated $k$-algebra* (two generators $x, y$ with one relation $f(x, y) = 0$), and $k$ is *infinite*, so the linear-shear version of normalization applies. The single relation $f(x, y) = 0$ is the algebraic dependence that normalization will convert into an integral dependence — exactly the mechanism of the theorem's proof, here with $m = 2$ generators.

**Theorem routing.** The route mirrors the proof of normalization in the two-generator case: the relation $f(x, y) = 0$ shows $x, y$ are *not* algebraically independent; shear $X \mapsto X + cY$ (or work with $u = y - cx$) so that the top-degree part $F$ of $f$ becomes monic in one variable; the new coordinate $u$ is a transcendental (algebraically independent) base, and the other coordinate is integral over $k[u]$. Then $A$ is finite over $k[u] \cong k[T]$, so $\operatorname{trdeg}_k A = 1$ and (with $f$ irreducible, hence $A$ a domain) $\dim A = 1$ via [[Thm - Noether Normalization|finiteness preserving dimension]].

**Key decision point.** The non-obvious move is *which linear combination to choose as the transcendental base $u$*: you must avoid the directions where the leading form $F$ of $f$ degenerates. For $f$ of degree $d$ with leading form $F(X, Y)$, the bad directions are the roots of $F(X, 1)$ (or $F(1, Y)$); a generic $c$ avoids them, and over an infinite field such $c$ exists. The second subtlety is recognising that the integral equation for the remaining coordinate is *literally $f$ rewritten in the new coordinates*, with the leading coefficient normalized to a unit — the normalization is not abstract, it is the relation $f = 0$ made monic.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra VII — Noether Normalization and the Nullstellensatz#Legal Operations|the topic page's Legal Operations]]:

1. **Read off the algebraic relation from the coordinate ring.** The defining relation $f(x, y) = 0$ is the dependence to be normalized.

2. **Shear coordinates to make the leading form monic.** Substitute $X \mapsto X + cY$ (or set $u = y - cx$) with $c$ avoiding the roots of the leading form.

3. **Extract the monic integral equation.** Divide the sheared relation by the (nonzero) leading coefficient to exhibit one coordinate as integral over $k[u]$.

4. **Conclude finiteness and read dimension as transcendence degree.** $A$ finite over $k[u] \cong k[T]$ gives $\dim A = \operatorname{trdeg}_k A = 1$.

---

# Hints

> [!note]- Hint 1
> The two coordinate functions $x, y \in A$ satisfy one relation, $f(x, y) = 0$, so they are algebraically dependent. Normalization says: after a linear change, one of them becomes integral over $k[\text{the other combination}]$. Which change of variables makes the relation *monic* in $y$ (say)?

> [!note]- Hint 2
> Look at the top-degree part $F$ of $f$ (the degree-$d$ homogeneous piece). If $f$ were already monic in $Y$ — i.e. the coefficient of $Y^d$ is a nonzero scalar — then $y$ would be integral over $k[x]$ directly. The shear $X \mapsto X + cY$ changes the coefficient of $Y^d$ to $F(c, 1)$; choose $c$ with $F(c, 1) \neq 0$.

> [!note]- Hint 3
> With $F(c, 1) \neq 0$, set $u := x - cy$ (so $x = u + cy$). Substitute into $f(x, y) = 0$: as a polynomial in $y$ over $k[u]$, it has degree $d$ with leading coefficient $F(c, 1) \in k^\times$. Divide by $F(c, 1)$: $y$ is integral over $k[u]$, so $A = k[u][y]$ is finite over $k[u]$.

> [!note]- Hint 4
> $k[u] \cong k[T]$ is a polynomial ring (one transcendental), and $A$ is finite over it. So $\operatorname{trdeg}_k A = 1$, and if $f$ is irreducible (so $A$ is a domain), $\dim A = 1$ because finite extensions preserve dimension. For $f = Y^2 - X^3 - X$: it is already monic in $Y$ (coefficient of $Y^2$ is $1$), so $u = x$ works with no shear, and $y^2 = x^3 + x$ is the integral equation — $A = k[x][y]$ is a free $k[x]$-module of rank $2$.

---

# Solution

The defining relation $f(x, y) = 0$ is an algebraic dependence between the two coordinate functions; normalization turns it into an integral dependence by a linear shear that makes the leading term a unit. Concretely, choose a transcendental base $u = x - cy$ avoiding the degenerate directions of the leading form, and the relation becomes monic in $y$ over $k[u]$, so $A$ is a finite $k[u]$-module. Since $k[u]$ is a one-variable polynomial ring, the curve has transcendence degree — and dimension — one.

**Step 1: The relation $f(x, y) = 0$ and the leading form.**

Write $f = F + (\text{lower degree})$ with $F$ the degree-$d$ leading form; the coordinate functions $x, y$ satisfy $f(x, y) = 0$ in $A$.

> [!note]- Derivation
> In $A = k[X, Y]/(f)$ the images $x, y$ of $X, Y$ satisfy $f(x, y) = 0$ by construction. Decompose $f = \sum_{i=0}^d f_i$ into homogeneous parts, with $f_d = F \neq 0$ the **leading form** of degree $d = \deg f$. Viewing $f$ as a polynomial in $Y$ over $k[X]$, its $Y$-degree-$d$ coefficient is the coefficient of $Y^d$ in $F$ — which may be zero (e.g. if $f = X Y^{d-1} + \dots$, the pure $Y^d$ term is absent), and *that* is the obstruction to $y$ being directly integral over $k[x]$. The shear repairs it.

**Step 2: Shear to make the relation monic in $y$.**

Choose $c$ with $F(c, 1) \neq 0$; set $u := x - cy$. Then $f(x, y) = 0$ becomes a monic equation for $y$ over $k[u]$.

> [!note]- Derivation
> Since $F$ is a nonzero homogeneous polynomial of degree $d$, $F(T, 1) \in k[T]$ is nonzero ([[Thm - Noether Normalization|Lemma 1 of normalization]]); as $k$ is infinite, there is $c \in k$ with $F(c, 1) \neq 0$ ([[Thm - Noether Normalization|Lemma 2]]). Set $u := x - cy$, so $x = u + cy$. Substituting $X = U + cY$ into $f$ gives a polynomial $g(U, Y) := f(U + cY, Y)$ with, by [[Thm - Noether Normalization|Lemma 3]], leading $Y$-coefficient $F(c, 1) \neq 0$:
> $$g(U, Y) = F(c, 1)\, Y^d + (\text{terms of lower degree in } Y, \text{ coefficients in } k[U]).$$
> Now $g(u, y) = f(u + cy, y) = f(x, y) = 0$ in $A$. Dividing by the unit $\lambda := F(c, 1) \in k^\times$:
> $$y^d + \lambda^{-1}c_{d-1}(u)\, y^{d-1} + \dots + \lambda^{-1}c_0(u) = 0, \qquad c_i(u) \in k[u],$$
> a **monic** equation for $y$ over $k[u]$. So $y$ is [[Def - Integral Element and Integral Extension|integral]] over $k[u]$.

**Step 3: $A$ is a finite $k[u]$-module, and $u$ is transcendental.**

$A = k[u][y]$ with $y$ integral over $k[u]$, so $A$ is finite over $k[u] \cong k[T]$.

> [!note]- Derivation
> The subring $k[u] \subseteq A$ is generated by the single element $u = x - cy$. Since $A = k[x, y] = k[u + cy, y] = k[u, y] = k[u][y]$, and $y$ satisfies a monic degree-$d$ relation over $k[u]$, $A$ is generated as a $k[u]$-module by $1, y, \dots, y^{d-1}$ — a **finite** module. Moreover $u$ is *transcendental* over $k$: if $u$ satisfied a polynomial $p(u) = 0$, then since $A$ is finite (algebraic) over $k[u]$, $A$ would be algebraic over $k$, making $\operatorname{Frac}(A)$ algebraic over $k$ — but $\operatorname{Frac}(A)$ contains $x, y$ with $\operatorname{trdeg} \geq 1$ (the curve is not a point). So $k[u] \cong k[T]$ is a genuine polynomial ring, and $A$ is finite over it. This *is* the Noether normalization of $A$: $A' = k[u]$, $n = 1$.

**Step 4: Dimension equals transcendence degree equals $1$.**

For irreducible $f$, $A$ is a domain finite over $k[u]$, so $\operatorname{trdeg}_k A = 1$ and $\dim A = 1$.

> [!note]- Derivation
> Since $A$ is finite over $k[u]$, the extension $\operatorname{Frac}(A) / k(u)$ is algebraic, so
> $$\operatorname{trdeg}_k \operatorname{Frac}(A) = \operatorname{trdeg}_k k(u) = 1$$
> by additivity of transcendence degree ([[Def - Algebraic Independence and Transcendence Degree|trdeg additivity]]). When $f$ is irreducible, $(f)$ is prime ($k[X, Y]$ is a [[Def - Unique Factorization Domain|UFD]], irreducible $\Rightarrow$ prime), so $A = k[X, Y]/(f)$ is a domain and $\operatorname{Frac}(A)$ makes sense. Finally $\dim A = 1$: finite (integral) extensions preserve Krull dimension ([[Commutative Algebra VIII — Going Up and Going Down|going up / incomparability]]), and $\dim k[u] = \dim k[T] = 1$, so $\dim A = 1$. This recovers $\operatorname{trdeg}_k k[X, Y]/(f) = 2 - 1 = 1$ — the $n = 2$ case of [[Def - Algebraic Independence and Transcendence Degree|ES4 Q2]], "$\operatorname{trdeg}_k k[T_1, \dots, T_n]/(g) = n - 1$ for irreducible $g$": one equation cuts one dimension.

**Step 5: The elliptic curve $f = Y^2 - X^3 - X$.**

Here $f$ is already monic in $Y$, so no shear is needed: $u = x$, and $y^2 = x^3 + x$ is the integral equation.

> [!note]- Derivation
> For $f = Y^2 - X^3 - X$ over $\mathbb{C}$, the coefficient of $Y^2$ is $1$ — already a unit — so the leading form $F = Y^2$ (degree $2$) gives $F(c, 1) = 1 \neq 0$ for *every* $c$; take $c = 0$, $u = x$. The relation $y^2 - x^3 - x = 0$ is monic in $y$:
> $$y^2 = x^3 + x,$$
> so $y$ is integral over $k[x]$, and $A = k[x][y]$ is a *free* $k[x]$-module with basis $\{1, y\}$ (rank $2$). The normalization is $A' = k[x] \cong k[T]$, and the finite map $C \to \mathbb{A}^1$ is the **projection to the $x$-axis**: a $2$-sheeted cover, with the two sheets $y = \pm\sqrt{x^3 + x}$ meeting where $x^3 + x = 0$ (the branch points $x = 0, \pm i$). The curve $C$ has dimension $1$, as a curve should. (Note: projecting to the $y$-axis would *not* work — $f$ is not monic in $X$, the coefficient of $X^3$ is $-1$ but there are issues; in fact $X^3$ has coefficient $-1$, a unit, so projection to $y$-axis also normalizes here, $x$ integral over $k[y]$ via $x^3 + x - y^2 = 0$ after sign-fixing.)

> [!note]- Complete formal solution
> **Claim.** $A = k[X, Y]/(f)$, $\deg f = d$, $k$ infinite, is finite over a polynomial ring $k[u]$ with $u$ a linear combination of $x, y$; if $f$ is irreducible, $\dim A = \operatorname{trdeg}_k \operatorname{Frac}(A) = 1$.
>
> Let $F$ be the degree-$d$ leading form of $f$. Pick $c \in k$ with $F(c, 1) \neq 0$ (possible: $F(T, 1) \neq 0$ by homogeneity, $k$ infinite). Set $u = x - cy$. Then $f(u + cy, y) = 0$ is, as a polynomial in $y$ over $k[u]$, of degree $d$ with leading coefficient $F(c, 1) \in k^\times$; dividing through, $y$ is integral over $k[u]$. Hence $A = k[u][y]$ is a finite $k[u]$-module, generated by $1, y, \dots, y^{d-1}$. The element $u$ is transcendental over $k$ (else $\operatorname{Frac}(A)$ would be algebraic over $k$, contradicting that the curve is positive-dimensional), so $k[u] \cong k[T]$. By trdeg-additivity, $\operatorname{trdeg}_k \operatorname{Frac}(A) = \operatorname{trdeg}_k k(u) = 1$; for irreducible $f$, $A$ is a domain and finite extensions preserve dimension, so $\dim A = \dim k[u] = 1$.
>
> *Example.* $f = Y^2 - X^3 - X$: monic in $Y$, so $u = x$, $y^2 = x^3 + x$, $A = k[x] \oplus k[x]y$ free of rank $2$, normalization equal to the projection $C \to \mathbb{A}^1$, $(x, y) \mapsto x$, a $2$-sheeted cover. $\blacksquare$

> [!warning] Illegal but tempting: assuming any projection direction normalizes
> It is tempting to just project to the $x$-axis (map $y$ to integral over $k[x]$) regardless of $f$. This *fails* when $f$ is not monic in $Y$ — i.e. when the leading form $F$ has zero $Y^d$-coefficient, equivalently when the projection direction is "bad" (the line at infinity meets the curve there). Example: $f = XY - 1$ (a hyperbola, degree $2$, leading form $F = XY$). Projecting to the $x$-axis gives $xy = 1$, so $y = 1/x$ — **not integral** over $k[x]$ (the hyperbola is asymptotic to the $y$-axis, "escaping to infinity" over $x = 0$). The fix is the shear: $u = x - cy$ with $F(c, 1) = c \neq 0$, i.e. *any* $c \neq 0$; then $A = k[x, y]/(xy - 1)$ is finite over $k[x - cy]$. The bad directions are exactly the roots of $F(c, 1) = c$, here $c = 0$ — the $x$-axis projection. Over an infinite field a generic direction always works; over a finite field one may need a nonlinear (Nagata) change.

---

# Key Takeaways

**Noether normalization of a hypersurface is just "make the defining equation monic by a shear".** The abstract theorem becomes completely concrete for a hypersurface $A = k[X_1, \dots, X_n]/(f)$: the single relation $f = 0$ is the only algebraic dependence, and normalization is the act of shearing coordinates so that $f$ becomes monic in the last variable, exhibiting it as integral over the rest. The leading form $F$ governs everything — its non-degenerate directions are the good projection directions, and $F(c, 1) \neq 0$ is the exact condition. The trigger is "coordinate ring of a hypersurface, want a finite map to affine space"; the reaction is "shear to make $f$ monic, project". This is the workhorse computation behind every explicit dimension calculation and every "curve as a branched cover" picture.

**Dimension is transcendence degree, and one equation drops it by one.** The headline arithmetic — $\operatorname{trdeg}_k k[X_1, \dots, X_n]/(f) = n - 1$ for irreducible $f$ — is the algebraic form of "a hypersurface in $\mathbb{A}^n$ has dimension $n - 1$". The mechanism is normalization: the curve is finite over a polynomial ring in $n - 1$ variables, and finite extensions preserve both transcendence degree (algebraic, so no new transcendentals) and Krull dimension (going-up/incomparability). The diagnostic: each independent equation you impose on $\mathbb{A}^n$ cuts the dimension by one, *provided* the equation is "non-degenerate" (its leading form does not vanish identically in the projection direction) — which Krull's principal ideal theorem makes precise in general. This is the bridge from the soft invariant trdeg to the hard invariant $\dim$.

**The finite map is a geometric projection, and its sheets are the conjugate roots.** Reading the normalization geometrically, $A$ finite over $k[u]$ is a **finite surjection $C \to \mathbb{A}^1$**, the projection along the sheared direction; the number of sheets is the degree $d$ of $f$ in the projected variable (the rank of $A$ as a $k[u]$-module), and the sheets are the $d$ roots $y$ of the monic equation, branching where the discriminant vanishes. For $y^2 = x^3 + x$, the two sheets $y = \pm\sqrt{x^3 + x}$ are the two square roots, glued at the branch points where $x^3 + x = 0$. The takeaway for spaced practice: whenever you normalize a curve, *picture the projection* — the algebra of "finite module of rank $d$" is the geometry of "$d$-sheeted branched cover", and the branch locus is where the cover degenerates. This picture, multiplied across all of [[Thm - Noether Normalization|Noether normalization]], is "every variety is a branched cover of affine space".
