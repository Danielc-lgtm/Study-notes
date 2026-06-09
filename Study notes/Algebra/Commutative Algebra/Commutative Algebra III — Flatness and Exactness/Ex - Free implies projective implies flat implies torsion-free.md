---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Free Module"
  - "Def - Projective Module"
  - "Def - Flat Module"
  - "Thm - Projective iff Direct Summand of a Free Module"
  - "Thm - Characterization of Flat Modules"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Prove the chain of implications, for an $R$-module $M$:
$$\textbf{free} \;\Longrightarrow\; \textbf{projective} \;\Longrightarrow\; \textbf{flat} \;\Longrightarrow\; \textbf{torsion-free},$$
and recall (via the separating examples) that none of the reverse implications holds in general. Concretely, show: (a) every [[Def - Free Module|free module]] is [[Def - Projective Module|projective]]; (b) every projective module is [[Def - Flat Module|flat]]; (c) every flat module is **torsion-free** (no non-zero element is annihilated by a non-zero-divisor).

**Recall:**

The objects in play are free, projective, flat, and torsion-free modules, and the structural characterization of projectivity.

![[Def - Free Module#The Definition]]

A [[Def - Free Module|free module]] $R^{\oplus I}$ is one with a basis: an indexed set whose elements are $R$-linearly independent and generate. Tensoring with it is taking $I$ copies, $R^{\oplus I}\otimes N \cong N^{\oplus I}$.

![[Def - Projective Module#The Definition]]

By [[Thm - Projective iff Direct Summand of a Free Module|the characterization theorem]], $M$ is projective iff it is a **direct summand of a free module**: $M \oplus N \cong R^{\oplus I}$ for some $N$.

![[Def - Flat Module#The Definition]]

$M$ is **torsion-free** if $rm = 0$ with $r$ a non-zero-divisor forces $m = 0$ — equivalently, multiplication by each non-zero-divisor acts injectively on $M$. Under $M \otimes_R R \cong M$, $m \otimes r \mapsto rm$, so "$\operatorname{id}_M\otimes\mu_r$ injective" is the same as "$\mu_r$ injective on $M$," i.e. no $r$-torsion.

The bridge that makes the whole chain run — *a property of a module is inherited by its direct summands*: if $M\oplus N$ has a property preserved by the relevant functor (flatness, here), so does each summand, because the functor splits over the direct sum.

---

# Convergent Strategy

**Problem class.** This is the *establish-a-tower* problem: prove a sequence of implications between module-theoretic properties, each one a single clean lemma, assembling the chapter's structural backbone. As the [[Commutative Algebra III — Flatness and Exactness]] strategy records, this tower is the spine on which every separating example hangs — knowing it is knowing where any given module sits.

**Assumption pattern.** Each implication has a *different* mechanism, and recognising which one applies is the whole skill. "Free $\Rightarrow$ projective" is pure structure (a free module is a summand of itself). "Projective $\Rightarrow$ flat" is the summand-inheritance of flatness. "Flat $\Rightarrow$ torsion-free" is the contrapositive observation that a torsion element is a *witness* of a broken injection $\mu_r$.

**Theorem routing.** The route is three independent steps. (a) Free $\Rightarrow$ projective directly from the [[Thm - Projective iff Direct Summand of a Free Module|summand characterization]] (take complement $0$). (b) Projective $\Rightarrow$ flat: a projective module is a summand of a free module ([[Thm - Projective iff Direct Summand of a Free Module|characterization]]); free modules are flat; flatness passes to summands. (c) Flat $\Rightarrow$ torsion-free: for a non-zero-divisor $r$, $\mu_r : R \to R$ is injective, so flatness makes $\operatorname{id}_M\otimes\mu_r = \mu_r|_M$ injective, i.e. no torsion.

**Key decision point.** The one non-obvious move is in step (c): recognising that the *injection to tensor* is $\mu_r : R \to R$, multiplication by $r$ on the *base ring*, not on $M$. Flatness applied to *this particular injection* says exactly that $r$ acts injectively on $M$ — that is torsion-freeness. The genuine insight is that torsion-freeness is "flatness, but only tested on the maps $\mu_r$", so flat (tested on *all* injections) trivially implies it. The natural wrong instinct is to look for a fancy argument; the right one is to identify the single injection that turns flatness into torsion-freeness.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra III — Flatness and Exactness#Legal Operations|the topic page's Legal Operations]]:

1. **Recognise freeness, then read off the tower (operation 5).** A free module is a summand of itself, so it is projective with no work.

2. **Use that flatness passes to summands (operation 5, summand form).** A direct summand of a flat module is flat because the induced map on a direct sum splits as a direct sum of the maps on summands.

3. **Test flatness on the injection $\mu_r : R \to R$ (operation 3).** Tensoring multiplication-by-$r$ (injective for a non-zero-divisor $r$) with $M$ gives multiplication by $r$ on $M$; flatness forces it injective, which is torsion-freeness.

4. **Present a module as a summand of a free module (operation 7).** Projectivity *is* the summand form, by the [[Thm - Projective iff Direct Summand of a Free Module|characterization]], which is the hinge between (a) and (b).

---

# Hints

> [!note]- Hint 1
> Three implications, three different ideas. For the first, what is the *easiest* free module to exhibit a given free module as a summand of? For the third, torsion-freeness is a statement about injectivity of multiplication maps — and flatness is *also* about injectivity. Which injection should you tensor?

> [!note]- Hint 2
> (a) A free module $F$ is a direct summand of $F$ itself (complement $0$), so by the [[Thm - Projective iff Direct Summand of a Free Module|summand characterization]] it is projective. (b) A projective $M$ has $M\oplus N\cong R^{\oplus I}$; the free $R^{\oplus I}$ is flat — now use that a summand of a flat module is flat. (c) Take a non-zero-divisor $r$ and consider $\mu_r : R \to R$, $x\mapsto rx$.

> [!note]- Hint 3
> For (b): if $f$ is injective, $\operatorname{id}_{M\oplus N}\otimes f = (\operatorname{id}_M\otimes f)\oplus(\operatorname{id}_N\otimes f)$; a direct sum of maps is injective iff each summand is, and the left side is injective because $M\oplus N$ is flat (free). For (c): $\mu_r$ is injective because $r$ is a non-zero-divisor, so flatness makes $\operatorname{id}_M\otimes\mu_r$ injective; under $M\otimes R\cong M$ ($m\otimes x\mapsto xm$) this map is exactly $m\mapsto rm$. Injectivity of $m\mapsto rm$ is "no $r$-torsion."

> [!note]- Hint 4
> Assemble: free $\Rightarrow$ projective (summand of self), projective $\Rightarrow$ flat (summand of free, flatness inherited), flat $\Rightarrow$ torsion-free (tensor $\mu_r$). For the failures of the reverses, name the four witnesses: $\mathbb{Q}$ over $\mathbb{Z}$ (flat not projective), $\mathbb{Z}/2$ over $\mathbb{Z}/6$ (projective not free), $(X,Y)\trianglelefteq k[X,Y]$ (torsion-free not flat).

---

# Solution

The proof is three short, independent lemmas, each using a different face of the definitions. The cleanest framing: freeness sits at the top because a free module is trivially a summand of itself; flatness is inherited downward through direct summands; and torsion-freeness is just flatness restricted to the special injections "multiply by a non-zero-divisor." The chain is then immediate, and the reverse failures are supplied by the chapter's separating examples.

**Step 1: Free $\Rightarrow$ projective.**

Every free module is a direct summand of a free module (itself), hence projective.

> [!note]- Derivation
> Let $F = R^{\oplus I}$ be [[Def - Free Module|free]]. Trivially $F \oplus 0 \cong F$ is free, so $F$ is a direct summand of a free module. By the [[Thm - Projective iff Direct Summand of a Free Module|summand characterization of projectivity]] (form (4)), $F$ is [[Def - Projective Module|projective]]. (Equivalently and directly: a map out of $F$ is determined by arbitrary images of a basis, so any $\bar h : F \to N/N'$ lifts by choosing preimages of the basis-images under the surjection $N \twoheadrightarrow N/N'$.)

**Step 2: Projective $\Rightarrow$ flat.**

A projective module is a direct summand of a free module, free modules are flat, and a direct summand of a flat module is flat.

> [!note]- Derivation
> Let $M$ be projective. By the [[Thm - Projective iff Direct Summand of a Free Module|characterization]], there is a module $N$ with $M \oplus N \cong R^{\oplus I}$ free.
>
> *Free modules are flat.* For an injection $f : A \to B$, the map $\operatorname{id}_{R^{\oplus I}}\otimes f$ is, under $R^{\oplus I}\otimes A \cong A^{\oplus I}$, the componentwise map $(a_i)_i \mapsto (f(a_i))_i$, injective because $f$ is. So $R^{\oplus I}$ is [[Def - Flat Module|flat]].
>
> *Flatness passes to summands.* Tensoring commutes with direct sums: for an injection $f$,
> $$\operatorname{id}_{M\oplus N}\otimes f = (\operatorname{id}_M\otimes f)\oplus(\operatorname{id}_N\otimes f).$$
> The left side is injective (as $M\oplus N\cong R^{\oplus I}$ is flat). A direct sum of $R$-linear maps is injective if and only if each summand is — if $(\operatorname{id}_M\otimes f)(x) = 0$ then $(x, 0)$ is killed by the direct sum, forcing $(x,0) = 0$, so $x = 0$. Hence $\operatorname{id}_M\otimes f$ is injective for every injection $f$: $M$ is flat.

**Step 3: Flat $\Rightarrow$ torsion-free.**

For a non-zero-divisor $r$, multiplication $\mu_r : R \to R$ is an injection; tensoring it with a flat $M$ yields the injective map "multiply by $r$ on $M$," which is exactly the no-$r$-torsion condition.

> [!note]- Derivation
> Suppose $M$ is [[Def - Flat Module|flat]]; we show it is torsion-free. Let $r \in R$ be a non-zero-divisor and suppose $rm_0 = 0$ for some $m_0 \in M$; we must show $m_0 = 0$.
>
> Consider $\mu_r : R \to R$, $\mu_r(x) = rx$. It is *injective*: $rx = 0$ with $r$ a non-zero-divisor forces $x = 0$. Since $M$ is flat,
> $$\operatorname{id}_M \otimes \mu_r : M \otimes_R R \longrightarrow M \otimes_R R \quad\text{is injective.}$$
> Identify $M \otimes_R R \cong M$ by $m \otimes x \mapsto xm$. Under this isomorphism, $\operatorname{id}_M\otimes\mu_r$ becomes
> $$m \mapsto (\text{image of } m\otimes 1 \mapsto m\otimes r \mapsto rm) = rm,$$
> i.e. multiplication by $r$ on $M$. Injectivity of this map says $rm = 0 \Rightarrow m = 0$. In particular $rm_0 = 0$ forces $m_0 = 0$. Hence $M$ has no $r$-torsion for any non-zero-divisor $r$: $M$ is torsion-free.

**Step 4: The reverses all fail.**

Each implication is strict, witnessed by a standard example.

> [!note]- Derivation
> - **Flat but not projective:** $\mathbb{Q}$ over $\mathbb{Z}$ ([[Ex - Q is a flat but not projective Z-module]]) — flat as a localization, but not a summand of a free abelian group because it is divisible.
> - **Projective but not free:** $\mathbb{Z}/2$ over $\mathbb{Z}/6 \cong \mathbb{Z}/2\times\mathbb{Z}/3$ ([[Ex - A projective module that is not free]]) — a summand cut out by the idempotent $(1,0)$, but too small to be free.
> - **Torsion-free but not flat:** $(X,Y) \trianglelefteq k[X,Y]$ ([[Ex - The maximal ideal (X,Y) is torsion-free but not flat]]) — torsion-free inside the domain $R$, but tensoring its inclusion with itself breaks injectivity.
>
> So free $\subsetneq$ projective $\subsetneq$ flat $\subsetneq$ torsion-free, all inclusions strict.

> [!note]- Complete formal solution
> **(a) Free $\Rightarrow$ projective.** A free module $F$ satisfies $F \oplus 0 \cong F$, so $F$ is a direct summand of a free module, hence projective by [[Thm - Projective iff Direct Summand of a Free Module|the summand characterization]].
>
> **(b) Projective $\Rightarrow$ flat.** Let $M$ be projective, so $M \oplus N \cong R^{\oplus I}$ for some $N$. Free modules are flat: $\operatorname{id}_{R^{\oplus I}}\otimes f$ is the componentwise injection $A^{\oplus I}\to B^{\oplus I}$ when $f : A\hookrightarrow B$. For any injection $f$, $\operatorname{id}_{M\oplus N}\otimes f = (\operatorname{id}_M\otimes f)\oplus(\operatorname{id}_N\otimes f)$ is injective (left side flat), and a direct sum of maps is injective iff each summand is; so $\operatorname{id}_M\otimes f$ is injective. Thus $M$ is flat.
>
> **(c) Flat $\Rightarrow$ torsion-free.** Let $M$ be flat and $r$ a non-zero-divisor. Then $\mu_r : R \to R$, $x\mapsto rx$, is injective, so flatness gives $\operatorname{id}_M\otimes\mu_r$ injective; under $M\otimes R\cong M$ this is $m\mapsto rm$. Hence $rm = 0 \Rightarrow m = 0$: $M$ is torsion-free.
>
> **Strictness.** $\mathbb{Q}/\mathbb{Z}$-style and the three witnesses above show none of the reverse implications holds: $\mathbb{Q}$ (flat, not projective), $\mathbb{Z}/2$ over $\mathbb{Z}/6$ (projective, not free), $(X,Y)\trianglelefteq k[X,Y]$ (torsion-free, not flat). $\blacksquare$

---

# Key Takeaways

**A property descends a tower of module classes via a single mechanism: direct summands inherit whatever the relevant functor preserves.** The middle implication "projective $\Rightarrow$ flat" is the model. Projective is *defined* (after the characterization) as "summand of free", free is flat, and flatness is preserved by the splitting of a tensor over a direct sum — so the property slides down from the free module to its summand for free. This is a reusable template: whenever you want to push a functorial property (flatness, but also projectivity, finite generation, finite presentation) from a big module to a piece of it, check that the functor commutes with the direct-sum decomposition, and the summand inherits the property automatically. The trigger to recognise the pattern is the phrase "summand of": it almost always signals "inherit the property by splitting the functor."

**Torsion-freeness is flatness in miniature — flatness tested only on the maps "multiply by a non-zero-divisor."** The implication flat $\Rightarrow$ torsion-free looks like it should need an argument, but it is nearly tautological once you see the right injection. Flatness asks that $\operatorname{id}_M\otimes f$ be injective for *every* injection $f$; torsion-freeness asks exactly this for the *particular* injections $f = \mu_r$, multiplication by a non-zero-divisor on the base ring $R$, since $\operatorname{id}_M\otimes\mu_r$ is multiplication by $r$ on $M$. So flat trivially implies torsion-free — the universal statement implies its special case. The transferable insight is diagnostic: to test torsion-freeness, you only ever tensor $\mu_r : R \to R$; to test flatness, you must tensor *all* injections, including ones like $\mathfrak m \hookrightarrow R$ that are not of the form $\mu_r$. The gap between the two is precisely the injections flatness sees that torsion-freeness does not — which is why over a [[Def - Principal Ideal Domain|PID]] (where every ideal is principal, so every relevant inclusion *is* essentially a $\mu_r$) the two notions coincide, and over $k[X,Y]$ they part ways.

**Knowing the tower with a witness at each gap is a classification reflex that solves "where does this module sit?" problems instantly.** The four witnesses — a free module, the projective-not-free $\mathbb{Z}/2$ over $\mathbb{Z}/6$, the flat-not-projective $\mathbb{Q}$ over $\mathbb{Z}$, the torsion-free-not-flat $(X,Y)$ — are the library every concrete module reduces to. When handed an unfamiliar module and asked whether it is flat, the reflex is to locate it on the tower: does it have a basis (free, done)? a complement in a free module (projective, hence flat)? a localization presentation (flat)? any torsion (not even torsion-free, so not flat)? And if it is torsion-free but you cannot climb higher, suspect the $(X,Y)$ phenomenon and test the criterion directly. The tower turns an open-ended "is it flat?" into a finite decision procedure, and the witnesses are the landmarks that tell you when each implication is strict and so cannot be reversed — see the companion exercises [[Ex - Q is a flat but not projective Z-module]], [[Ex - A projective module that is not free]], and [[Ex - The maximal ideal (X,Y) is torsion-free but not flat]] for the gaps in full.
