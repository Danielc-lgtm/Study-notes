---
type: definition
subject: commutative-algebra
prereqs:
  - "Def - Ring"
  - "Def - Subring"
  - "Def - Integral Domain"
  - "Def - Field of Fractions"
  - "Def - Integral Element and Integral Extension"
  - "Def - Unique Factorization Domain"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $A \subseteq B$ be a subring inclusion. We write $\overline A$ (or $\overline A^{\,B}$ when the ambient ring needs naming) for the **integral closure of $A$ in $B$**, the set of $b \in B$ that are [[Def - Integral Element and Integral Extension|integral]] over $A$. When $A$ is an [[Def - Integral Domain|integral domain]], $\operatorname{Frac}(A)$ is its [[Def - Field of Fractions|field of fractions]], and "the integral closure of $A$" with no ambient named means $\overline A^{\,\operatorname{Frac}(A)}$. A domain $A$ is **normal** if it is integrally closed in $\operatorname{Frac}(A)$. The full registry is on [[Commutative Algebra VI — Integral Extensions]].

This is a compound page: it defines several interlocking notions — the **integral closure** $\overline A$ of $A$ in $B$, the property of being **integrally closed in $B$**, and (for a domain) being **integrally closed / normal** — because they are the same construction read at three levels, and none is fully usable without the others.

---

# Axiom Motivation

The goal is to build, inside a big ring $B$, the *largest subring all of whose elements behave like integers over $A$*, and then to single out the rings that are already complete in this sense. We have just learned ([[Def - Integral Element and Integral Extension]]) what it means for one element to be integral over $A$. The natural next move is to *collect all of them*: form the set $\overline A = \{b \in B : b \text{ integral over } A\}$. Three things must be motivated — that this set deserves to be called a "closure", that it is a *ring*, and that the rings equal to their own closure (the "normal" ones) are a class worth naming.

**Why "closure" — the analogy with algebraic and topological closure.** The word "closure" is earned if the operation $A \mapsto \overline A$ behaves like one: it should *enlarge* ($A \subseteq \overline A$), be *idempotent* ($\overline{\overline A} = \overline A$, closing once closes completely), and be *monotone*. Enlargement is immediate ($a \in A$ satisfies $T - a$, monic). Idempotence is the substantive content — it says that an element integral over the integral closure is already integral over $A$ — and it is true precisely because integrality is *transitive* ([[Thm - Transitivity of Integrality and Finiteness]]): integral-over-integral is integral. So the construction genuinely closes, exactly like algebraic closure (algebraic-over-algebraic is algebraic) or topological closure ($\overline{\overline S} = \overline S$). The integral closure is the "saturation" of $A$ inside $B$ under the operation "adjoin everything integral".

**Why it is a ring — and why that is not obvious.** One would *hope* $\overline A$ is a subring, but this is genuinely surprising from the definition. If $x, y$ are each integral — each satisfies *its own* monic equation — there is no evident monic equation for $x + y$ or $xy$. You cannot just add or multiply the equations. The fact that $\overline A$ is nonetheless closed under $+$ and $\times$ ([[Thm - The Integral Closure is a Subring]]) is a theorem, not a definition, and it is the technical justification for the whole concept: without it, "the integral closure" would be a mere set, useless for algebra. The proof is the chapter's signature move — put $x$ and $y$ together in the finite module $A[x, y]$ and use that *every* element of a finite faithful module is integral. So the ring structure of $\overline A$ is the payoff of the [[Thm - Characterizations of Integrality (Module-Finite Criterion)|module-finite criterion]]. Naming "integral closure" presupposes this theorem; the definition is only well-motivated because the closure really is a ring.

**Why restrict to $\operatorname{Frac}(A)$ for domains — the canonical ambient.** For a general inclusion $A \subseteq B$, the closure $\overline A$ depends on $B$. But for a *domain* there is a canonical, maximal ambient ring: its field of fractions $\operatorname{Frac}(A)$, the smallest field containing $A$. Closing $A$ inside its own fraction field asks: *which fractions of $A$ are secretly integral over $A$?* This is the most important case because it is where "missing integers" live. The fraction field contains all the would-be integers (like $\tfrac{1+\sqrt5}2$ over $\mathbb{Z}[\sqrt5]$, or $t$ over $k[t^2, t^3]$); the integral closure in $\operatorname{Frac}(A)$ rounds $A$ up to include exactly them. A domain that misses none of them — that already contains every integral fraction — is the well-behaved case, and deserves a name.

**Why name "normal" — the per-axiom point of the definition.** A domain $A$ with $\overline A = A$ (integrally closed in $\operatorname{Frac}(A)$) is called **normal**. Why is this worth isolating rather than treating as a passing property? Because normality is *exactly the right amount of regularity* for two central theorems. First, it is what unique factorization gives for free ([[Thm - A UFD is Integrally Closed|every UFD is normal]]) — so it is a weakening of UFD that is far more common (every regular local ring is normal, hence every smooth variety is normal) yet still strong enough to be useful. Second, it is the precise hypothesis under which **going-down** holds, under which the ring of integers becomes a **Dedekind domain** with unique factorization of *ideals*, and under which a variety is *smooth in codimension one*. The definition is calibrated: drop integral-closedness and you lose ideal factorization and codimension-one smoothness; strengthen it to UFD and you exclude too much (most normal rings are not UFDs). Normality is the Goldilocks regularity condition, and that is why it is named. The failure of normality is itself meaningful — it measures a singularity (the cusp $k[t^2,t^3]$ is not normal) or a "missing algebraic integer" ($\mathbb{Z}[\sqrt5]$ is not normal), and the integral closure is the canonical repair, the **normalization**.

---

# The Definition

Let $A \subseteq B$ be commutative rings.

**Integral closure in $B$.** The **integral closure of $A$ in $B$** is
$$\overline A^{\,B} = \{\, b \in B : b \text{ is integral over } A \,\}.$$
By [[Thm - The Integral Closure is a Subring]] this is a subring of $B$ containing $A$; we usually write $\overline A$ when $B$ is understood.

**Integrally closed in $B$.** $A$ is **integrally closed in $B$** if $\overline A^{\,B} = A$ — that is, every element of $B$ integral over $A$ already lies in $A$.

**Integral closure of a domain; normal domain.** Let $A$ be an [[Def - Integral Domain|integral domain]] with field of fractions $\operatorname{Frac}(A)$.

- The **integral closure of $A$** is $\overline A = \overline A^{\,\operatorname{Frac}(A)}$, its integral closure in $\operatorname{Frac}(A)$.
- $A$ is **integrally closed**, or **normal**, if it is integrally closed in $\operatorname{Frac}(A)$: every element of $\operatorname{Frac}(A)$ integral over $A$ lies in $A$.

**Idempotence.** The closure is idempotent: $\overline{\overline A^{\,B}}^{\,B} = \overline A^{\,B}$ (Becker 6.12), so $\overline A$ is always integrally closed in $B$. Hence for a domain, $\overline A$ is a normal domain — the *normalization* of $A$.

---

# Relate to Other Fields / Compression

The integral closure is the abstraction of **"the ring of integers"** to any domain. For $\mathbb{Z}$ inside a number field $K$, the integral closure of $\mathbb{Z}$ in $K$ is $\mathcal{O}_K$, the ring of integers — and "$\mathbb{Z}$ is integrally closed (in $\mathbb{Q}$)" is the statement $\mathcal{O}_{\mathbb{Q}} = \mathbb{Z}$, i.e. the only rationals that are algebraic integers are the ordinary integers. Normality is the property that a ring already *is* its own ring of integers, having no missing algebraic integers in its fraction field.

**True name:** the operational form of "normal" is **"a UFD-like cancellation works: if $\tfrac ab$ is integral and $\tfrac ab$ is in lowest terms, then $b$ is a unit"** — equivalently, **"every monic equation with a root in the fraction field already has that root in the ring"**. This is what you check or exploit: normality lets you conclude $x \in A$ from "$x \in \operatorname{Frac}(A)$ and $x$ satisfies a monic over $A$", which is exactly how a UFD's integral-closedness is used.

In **algebraic geometry** the integral closure is the coordinate ring of the **normalization** $\tilde X \to X$ of a variety $X = \operatorname{Spec} A$: the universal finite, birational map from a normal variety onto $X$. Normality compresses to **"smooth in codimension one" (Serre's $R_1 + S_2$)**: a normal variety's singular locus has codimension $\geq 2$, so normal *curves* are smooth, and normalization *resolves all curve singularities*. The standard pictures are the node and the cusp: the cusp $y^2 = x^3$ has coordinate ring $k[t^2, t^3]$, not normal, with normalization $k[t]$ (the smooth line) adding the missing function $t = y/x$. In **number theory**, normality is the hypothesis that makes a one-dimensional Noetherian domain a [[Commutative Algebra XIII — Dedekind Domains and DVRs|Dedekind domain]], where ideals factor uniquely into primes — the modern rescue of unique factorization.

---

# Examples / Corollaries

**Is integrally closed (normal) — $\mathbb{Z}$ in $\mathbb{Q}$.** The integral closure of $\mathbb{Z}$ in $\mathbb{Q}$ is $\mathbb{Z}$ itself: a rational integral over $\mathbb{Z}$ is an ordinary integer ([[Thm - Rational Algebraic Integers are Integers]]). So $\mathbb{Z}$ is normal — as is every [[Def - Principal Ideal Domain|PID]] and, more generally, every [[Def - Unique Factorization Domain|UFD]] ([[Thm - A UFD is Integrally Closed]]). In particular every polynomial ring $k[T_1, \dots, T_n]$ over a field is normal: affine space is a normal variety.

**Is NOT integrally closed — $\mathbb{Z}[\sqrt5]$.** The ring $A = \mathbb{Z}[\sqrt5]$ is a domain with $\operatorname{Frac}(A) = \mathbb{Q}(\sqrt5)$, but it is *not* normal. The element $\alpha = \tfrac{1+\sqrt5}2 \in \mathbb{Q}(\sqrt5)$ satisfies the monic $T^2 - T - 1 = 0$ (so $\alpha$ is integral over $\mathbb{Z}$, a fortiori over $A$) yet $\alpha \notin \mathbb{Z}[\sqrt5]$ (its $\sqrt5$-coefficient is $\tfrac12$, not an integer). So $\overline A = \mathbb{Z}[\alpha] = \mathbb{Z}[\tfrac{1+\sqrt5}2] \supsetneq A$. This is the canonical "missing algebraic integer": $\mathbb{Z}[\sqrt5]$ is too small to be the ring of integers of $\mathbb{Q}(\sqrt5)$.

**Is NOT integrally closed — the cusp ring $k[t^2, t^3]$.** The subring $A = k[t^2, t^3] \subseteq k[t]$ (coordinate ring of the cusp $y^2 = x^3$ via $x = t^2, y = t^3$) has $\operatorname{Frac}(A) = k(t)$, since $t = t^3/t^2 \in \operatorname{Frac}(A)$. The element $t$ satisfies the monic $T^2 - t^2 = 0$ over $A$ (as $t^2 \in A$), so $t$ is integral over $A$, but $t \notin k[t^2, t^3]$ (it has no degree-$1$ term available). Hence $\overline A = k[t]$, the smooth line — the normalization unfolds the cusp. This is the geometric prototype: non-normality $=$ singularity.

**Corollary — the closure is idempotent.** Closing $A$ inside $B$ once already gives an integrally closed ring: $\overline{\overline A} = \overline A$. So $\mathbb{Z}[\tfrac{1+\sqrt5}2]$ is itself normal (indeed it is the ring of integers of $\mathbb{Q}(\sqrt5)$, a Dedekind domain), and $k[t]$ is normal (it is a PID). You never need to close twice. This is the calibration check that integrality is transitive.

**Corollary — normal is strictly weaker than UFD.** Every UFD is normal, but not conversely: $\mathbb{Z}[\tfrac{1+\sqrt5}2]$ and $k[x,y,z]/(xy - z^2)$ are normal but not UFDs (the latter has $xy = z^2$ with $x, y, z$ irreducible, breaking unique factorization while remaining normal). So normality sits strictly between "domain" and "UFD". This probes the boundary of the definition.

**Calibration check.** Confirm that $\overline{\mathbb{Z}[\sqrt5]} = \mathbb{Z}[\tfrac{1+\sqrt5}2]$ by checking $\alpha = \tfrac{1+\sqrt5}2$ is integral and that $\mathbb{Z}[\alpha]$ is a UFD (hence normal, hence caps the closure). Verify that $k[t]$ is the integral closure of $k[t^2,t^3]$ by exhibiting the monic equation for $t$ and noting $k[t]$ is a PID. Explain in one sentence why "integrally closed" is an idempotent operation, and why a domain failing to be normal signals either a missing algebraic integer or a singularity. If you can identify the missing element in each non-example and the monic equation it satisfies, you have understood the definition.

---

# Unlocked by This

> [!tip] The ring of integers and Dedekind domains *(from Algebraic Number Theory)*
> For a number field $K/\mathbb{Q}$, the **ring of integers** $\mathcal{O}_K$ is the integral closure of $\mathbb{Z}$ in $K$ — automatically a normal, Noetherian domain of dimension one, hence a **Dedekind domain**, where every nonzero ideal factors uniquely into prime ideals. Normality is the exact hypothesis that rescues unique factorization at the level of ideals when it fails at the level of elements; this is why one *must* pass to the full integral closure (not just $\mathbb{Z}[\alpha]$) before doing ideal arithmetic. Developed in [[Commutative Algebra XIII — Dedekind Domains and DVRs]].

> [!tip] Normalization and resolution of singularities *(from Algebraic Geometry)*
> The integral closure of a coordinate ring is the coordinate ring of the **normalization** $\tilde X \to X$, the universal finite birational map from a normal variety. For curves, normal $=$ smooth, so normalization *completely resolves curve singularities* — it separates the branches of a node and unfolds the cusp. In higher dimensions, **Serre's criterion** says normal $= R_1 + S_2$ (regular in codimension one plus a depth condition), so normalization resolves only codimension-one singularities, leaving the rest to the general resolution problem. That **regular $\Rightarrow$ normal** (via regular local rings being UFDs) is why smooth varieties never need normalizing.

> [!tip] Going-down and the geometry of fibres *(from Commutative Algebra)*
> Normality of the base is the precise hypothesis of the **going-down theorem**: for $A \subseteq B$ integral with $A$ normal and $B$ a domain, chains of primes descend from $B$ to $A$. Geometrically, going-down controls how the fibres of a finite map vary and is what makes finite maps from normal varieties **open** (or at least equidimensional). The failure of going-down without normality is exactly the pathology that the cusp's non-normality exhibits; see [[Commutative Algebra VIII — Going Up and Going Down]].
