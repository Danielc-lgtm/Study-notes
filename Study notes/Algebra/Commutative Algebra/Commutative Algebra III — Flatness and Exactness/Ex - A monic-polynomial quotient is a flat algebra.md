---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Flat Module"
  - "Def - Free Module"
  - "Def - Polynomial Ring"
  - "Thm - Characterization of Flat Modules"
  - "Def - Ideal"
tags: [algebra, commutative-algebra]
---

# Problem Statement

(a) Let $A$ be a ring and $f \in A[T]$ a **monic** polynomial. Prove that the $A$-algebra $B = A[T]/(f)$ is a [[Def - Flat Module|flat]] $A$-module.

(b) Prove that $B := k[X, Y]/(XY)$ is **not** a flat $k[X]$-module ($k$ a field), where $k[X]\hookrightarrow B$ is the inclusion of the coefficient ring. *Hint:* consider the embedding $(X)\hookrightarrow k[X]$.

Together these are the algebraic skeleton of "a flat family is one whose fibres do not jump": (a) is a finite flat family of $\deg f$ points; (b) is two crossing lines whose fibre jumps at the origin.

**Recall:**

The objects in play are flat modules, free modules, monic polynomials, and the ideal criterion for flatness.

![[Def - Flat Module#The Definition]]

![[Def - Free Module#The Definition]]

A **monic** polynomial $f = T^d + a_{d-1}T^{d-1} + \dots + a_0\in A[T]$ has leading coefficient $1$. Division with remainder by a *monic* $f$ works over *any* ring $A$ (the leading $1$ is a unit, so no denominators are needed), giving for each $p\in A[T]$ a unique $p = qf + r$ with $\deg r < d$.

![[Thm - Characterization of Flat Modules#Statement]]

For an ideal $I$, $M$ is flat iff $I\otimes_R M\to IM$ is injective for finitely generated $I$. In (b) we tensor $(X)\hookrightarrow k[X]$ with $B$ and find the injection breaks.

The bridge that makes (a) run — *division with remainder by a monic polynomial gives $B$ a basis $1, T, \dots, T^{d-1}$ over $A$, so $B$ is a [[Def - Free Module|free]] $A$-module of rank $d$, hence flat*. The bridge for (b) — *$B = k[X,Y]/(XY)$ has $X$-torsion as a $k[X]$-module* (the class of $Y$ is killed by $X$), so $B$ is not even torsion-free over $k[X]$, hence not flat.

---

# Convergent Strategy

**Problem class.** This is a *prove-flatness-by-recognising-freeness* problem paired with a *refute-flatness-by-torsion* problem — the two halves of locating an algebra on the tower. As the [[Commutative Algebra III — Flatness and Exactness]] strategy records, the fastest flatness proof is "this is free," and the fastest refutation is "this has torsion"; this exercise drills both on the geometrically meaningful examples of flat and non-flat families.

**Assumption pattern.** (a) The trigger is "*monic* polynomial": monicity is exactly what makes division with remainder work over an arbitrary base ring $A$, producing a basis. (b) The trigger is "the coefficient ring sits inside a quotient by a *zero-divisor relation* $XY = 0$": the class of $Y$ becomes $X$-torsion, the immediate certificate of non-flatness.

**Theorem routing.** (a) Division with remainder by monic $f$ shows every coset in $A[T]/(f)$ has a unique representative of degree $< d$, so $\{1, T, \dots, T^{d-1}\}$ is an $A$-basis; thus $B$ is [[Def - Free Module|free]] of rank $d$, and free $\Rightarrow$ [[Def - Flat Module|flat]]. (b) Over $k[X]$, the element $\bar Y\in B$ satisfies $X\cdot\bar Y = \overline{XY} = 0$ with $\bar Y\neq 0$ and $X$ a non-zero-divisor in $k[X]$; so $B$ has torsion, hence is not torsion-free, hence not flat (contrapositive of [[Thm - Characterization of Flat Modules|flat $\Rightarrow$ torsion-free]]). Alternatively, tensor $(X)\hookrightarrow k[X]$ with $B$ and watch injectivity fail.

**Key decision point.** For (a) the non-obvious recognition is that *monicity is doing all the work*: over a general ring $A$ you cannot divide by a non-monic polynomial (its leading coefficient may not be invertible), but a monic divisor needs no division of coefficients, so the remainder algorithm and hence the basis exist unconditionally. For (b) the decision is *which torsion element to name*: $\bar Y$ killed by $X$ is the witness, recognised because the defining relation $XY = 0$ directly exhibits $X$ annihilating the non-zero $\bar Y$. The natural wrong instinct in (a) is to attempt a flatness computation; the right one is to spot the free basis. In (b) the wrong instinct is to tensor and chase; the right one is to spot the obvious torsion.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra III — Flatness and Exactness#Legal Operations|the topic page's Legal Operations]]:

1. **Recognise freeness, then read off flatness (operation 5).** A monic quotient has the explicit basis $1, T, \dots, T^{d-1}$, so it is free, hence flat.

2. **Refute flatness by finding torsion (operation 3).** $X\cdot\bar Y = 0$ with $\bar Y\neq 0$ shows $B$ is not torsion-free over $k[X]$, hence not flat.

3. **Use the ideal criterion for a second proof of (b) (operation 4).** Tensoring $(X)\hookrightarrow k[X]$ with $B$ produces a non-injective map.

4. **Divide with remainder by a monic polynomial (operation 5, freeness construction).** Monicity makes the division algorithm work over any base ring.

---

# Hints

> [!note]- Hint 1
> (a) "Monic" is the whole hypothesis. What does it let you do with polynomials over an *arbitrary* ring $A$ that you cannot do with a general polynomial? Think about division. (b) The relation defining $B$ is $XY = 0$. Over $k[X]$, what does that say about the element $\bar Y$?

> [!note]- Hint 2
> (a) Division with remainder by monic $f$ (degree $d$): every $p\in A[T]$ is uniquely $p = qf + r$, $\deg r < d$. So in $B = A[T]/(f)$, every element has a unique representative $r$ of degree $< d$. What does that make $\{1, T, \dots, T^{d-1}\}$? (b) Compute $X\cdot\bar Y$ in $B$.

> [!note]- Hint 3
> (a) $\{1, T, \dots, T^{d-1}\}$ is an $A$-*basis* of $B$, so $B\cong A^d$ is free of rank $d$, hence flat (free $\Rightarrow$ flat). (b) $X\cdot\bar Y = \overline{XY} = \bar 0$ but $\bar Y\neq 0$ in $B$ (it is not a multiple of $XY$). And $X$ is a non-zero-divisor in $k[X]$. So $B$ has $X$-torsion.

> [!note]- Hint 4
> (b) Flat modules are torsion-free ([[Thm - Characterization of Flat Modules|flat $\Rightarrow$ torsion-free]]); $B$ has the torsion element $\bar Y$, so $B$ is not flat over $k[X]$. (Second proof: tensor $(X)\hookrightarrow k[X]$ with $B$; the map $(X)\otimes_{k[X]}B\to XB$ sends $X\otimes\bar Y\mapsto X\bar Y = 0$, but $X\otimes\bar Y\neq 0$, so injectivity fails.)

---

# Solution

The two parts are the cleanest "flat" and "not flat" witnesses in the chapter, and each is a one-idea proof. (a): monicity makes division with remainder work over any base, handing $B$ the explicit basis $1, T, \dots, T^{d-1}$, so $B$ is free, hence flat. (b): the relation $XY = 0$ makes $\bar Y$ an $X$-torsion element, and torsion kills flatness immediately.

**Step 1 (a): Division by a monic polynomial gives a basis.**

Every element of $B = A[T]/(f)$ has a unique representative of degree $< d = \deg f$, so $\{1, T, \dots, T^{d-1}\}$ is an $A$-basis.

> [!note]- Derivation
> Let $f = T^d + a_{d-1}T^{d-1} + \dots + a_0$ be monic of degree $d$ over $A$. *Division with remainder works over any ring when the divisor is monic:* given $p\in A[T]$, repeatedly subtract $A$-multiples of $T^{k}f$ to cancel the leading term of $p$ — each step uses only that the leading coefficient of $f$ is $1$ (a unit), so no coefficient of $A$ need be inverted. This terminates with $p = qf + r$, $\deg r < d$, and $q, r$ are unique (if $qf + r = q'f + r'$ then $(q - q')f = r' - r$ has degree $< d$ on the right but, if $q\neq q'$, degree $\geq d$ on the left since $f$ is monic — contradiction).
>
> Hence in $B = A[T]/(f)$ every coset $\bar p$ equals $\bar r$ for a unique $r = c_0 + c_1 T + \dots + c_{d-1}T^{d-1}$, $c_i\in A$. So
> $$\{\bar 1, \bar T, \dots, \overline{T^{d-1}}\}$$
> spans $B$ over $A$ (existence of $r$) and is $A$-linearly independent (uniqueness of $r$). It is an $A$-basis.

**Step 2 (a): $B$ is free, hence flat.**

$B\cong A^d$ is a free $A$-module of rank $d$, so it is flat.

> [!note]- Derivation
> Having an $A$-basis $\{\bar 1, \dots, \overline{T^{d-1}}\}$ of size $d$ means $B$ is a [[Def - Free Module|free]] $A$-module, $B\cong A^d$. Free modules are [[Def - Flat Module|flat]]: tensoring an injection $h : N\hookrightarrow N'$ with $A^d$ gives the componentwise injection $N^d\to (N')^d$. (Equivalently, by [[Ex - Free implies projective implies flat implies torsion-free|free $\Rightarrow$ flat]].) So $B = A[T]/(f)$ is a flat $A$-module. $\blacksquare$ (a)

**Step 3 (b): $B = k[X,Y]/(XY)$ has $X$-torsion over $k[X]$.**

$\bar Y\neq 0$ but $X\bar Y = 0$, and $X$ is a non-zero-divisor in $k[X]$.

> [!note]- Derivation
> View $B = k[X, Y]/(XY)$ as a $k[X]$-module via the inclusion $k[X]\hookrightarrow B$ (the coefficient ring). Consider the class $\bar Y\in B$.
> - *$\bar Y\neq 0$:* $Y\notin (XY)$, since every non-zero element of the ideal $(XY)$ is a multiple of $XY$ and so has every monomial divisible by both $X$ and $Y$; $Y$ is not such a multiple. So $\bar Y\neq\bar 0$.
> - *$X\bar Y = 0$:* $X\cdot Y = XY\in (XY)$, so $X\bar Y = \overline{XY} = \bar 0$ in $B$.
> - *$X$ is a non-zero-divisor in $k[X]$:* $k[X]$ is a domain, so the only zero-divisor is $0$, and $X\neq 0$.
>
> Thus $\bar Y$ is a non-zero element of $B$ annihilated by the non-zero-divisor $X$: $B$ has $X$-torsion as a $k[X]$-module.

**Step 4 (b): $B$ is not flat over $k[X]$.**

Torsion forbids flatness.

> [!note]- Derivation
> [[Thm - Characterization of Flat Modules|Flat modules are torsion-free]]. Since $B$ has the torsion element $\bar Y$ (Step 3), $B$ is *not* torsion-free over $k[X]$, hence not flat over $k[X]$. $\blacksquare$ (b)
>
> *Second proof via the ideal criterion.* Tensor the inclusion $\iota : (X)\hookrightarrow k[X]$ with $B$. By [[Thm - Characterization of Flat Modules|the ideal criterion]], flatness of $B$ would make $(X)\otimes_{k[X]}B\to XB$, $X\otimes b\mapsto Xb$, injective. Now $(X)\cong k[X]$ as a $k[X]$-module (it is free of rank $1$, generated by $X$), so $(X)\otimes_{k[X]}B\cong B$, and the element $X\otimes\bar Y$ corresponds to $\bar Y\neq 0$. But it maps to $X\bar Y = 0$. So the map is not injective: $B$ is not flat.

> [!note]- Complete formal solution
> **(a)** Let $f\in A[T]$ be monic of degree $d$. Division with remainder by a monic polynomial works over any ring (the leading $1$ needs no inverting): every $p\in A[T]$ is uniquely $p = qf + r$ with $\deg r < d$. Hence $\{\bar 1, \bar T, \dots, \overline{T^{d-1}}\}$ is an $A$-basis of $B = A[T]/(f)$ (spanning by existence, independent by uniqueness), so $B\cong A^d$ is free of rank $d$. Free modules are flat (tensoring with $A^d$ is a componentwise injection on injections). So $B$ is a flat $A$-module.
>
> **(b)** In $B = k[X,Y]/(XY)$ over $k[X]$, the class $\bar Y$ is non-zero ($Y\notin(XY)$) and satisfies $X\bar Y = \overline{XY} = 0$. As $X$ is a non-zero-divisor in the domain $k[X]$, $\bar Y$ is a torsion element, so $B$ is not torsion-free, hence not flat over $k[X]$ ([[Thm - Characterization of Flat Modules|flat $\Rightarrow$ torsion-free]]). $\blacksquare$

---

# Key Takeaways

**A monic-polynomial quotient is free, and monicity is exactly the hypothesis that makes the basis exist over an arbitrary base ring.** The proof of (a) is "division with remainder gives the basis $1, T, \dots, T^{d-1}$," but the load-bearing word is *monic*: over a general ring $A$ you cannot divide by a polynomial whose leading coefficient is a non-unit, so a non-monic quotient need not be free or flat. The reusable principle: whenever you meet $A[T]/(f)$ with $f$ monic, you may immediately treat $B$ as a free $A$-module of rank $\deg f$ — a basis, a flatness certificate, and a finite rank, all at once. The trigger is "monic quotient"; the reaction is "free of rank $d$, hence flat, projective, and torsion-free." This is the single most common way flat algebras arise in practice (integral ring extensions defined by monic equations), and it is why finite *free* extensions are the well-behaved ones.

**Torsion is the instant refutation of flatness — name the element the defining relation kills.** Part (b) is a one-line non-flatness proof because the relation $XY = 0$ *hands you* the torsion: $X$ annihilates $\bar Y\neq 0$, and $X$ is a non-zero-divisor downstairs. The reusable diagnostic: to show an algebra $B = A[\dots]/(\text{relations})$ is not flat over $A$, read the relations for one expressing "(non-zero-divisor of $A$) $\times$ (non-zero element of $B$) $= 0$" — that element is a torsion witness, and [[Thm - Characterization of Flat Modules|flat $\Rightarrow$ torsion-free]] finishes the job with no computation. The trigger is "a relation $a\cdot b = 0$ with $a$ from the base"; the reaction is "$b$ is torsion, so not flat." This is far faster than the ideal-criterion tensor computation, which is worth keeping as a backup but is rarely needed when visible torsion is present.

**Flat versus non-flat is the algebra of families that do versus do not tear, and these two examples are the canonical pictures.** Under the algebra–geometry dictionary, $A[T]/(f)$ for monic $f$ is a **finite flat family of $\deg f$ points** over $\operatorname{Spec} A$: each fibre is the $d$ roots of $f$ (with multiplicity), and the count never drops because the rank $d$ is constant — flatness *is* this constancy. By contrast $k[X,Y]/(XY)$ over $k[X]$ is the union of the $X$-axis and the $Y$-axis mapping to the $X$-line: over $X = c\neq 0$ the fibre is the single point $(c, 0)$, but over $X = 0$ the fibre is the entire $Y$-axis — the fibre *jumps in dimension*, and that jump is exactly the torsion that destroys flatness. The deep takeaway, the spine of the chapter: **flatness is the algebraic condition that fibre dimension (and length) stays locally constant, so flat families are the ones that deform without tearing.** This is the contrast partner of [[Ex - The maximal ideal (X,Y) is torsion-free but not flat]] (where the local structure at a point tears more subtly) and completes the geometric reading of the tower in [[Ex - Free implies projective implies flat implies torsion-free]].
