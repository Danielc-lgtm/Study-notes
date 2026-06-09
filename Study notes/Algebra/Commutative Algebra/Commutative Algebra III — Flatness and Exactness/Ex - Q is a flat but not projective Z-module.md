---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐"
prereqs:
  - "Def - Flat Module"
  - "Def - Projective Module"
  - "Def - Field of Fractions"
  - "Thm - Projective iff Direct Summand of a Free Module"
  - "Thm - Extension of Scalars Preserves Flatness"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Prove that $\mathbb{Q}$ is a [[Def - Flat Module|flat]] $\mathbb{Z}$-module but **not** a [[Def - Projective Module|projective]] $\mathbb{Z}$-module. This separates flatness from projectivity, showing the implication "projective $\Rightarrow$ flat" is strict.

**Recall:**

The objects in play are flat modules, projective modules, the field of fractions, and divisibility of abelian groups.

![[Def - Flat Module#The Definition]]

![[Def - Projective Module#The Definition]]

By [[Thm - Projective iff Direct Summand of a Free Module|the characterization]], $M$ is projective over $R$ iff it is a **direct summand of a free module**: $M \oplus N \cong R^{\oplus I}$.

An abelian group $A$ is **divisible** if for every $a \in A$ and every integer $n \geq 1$ there is $a' \in A$ with $na' = a$. $\mathbb{Q}$ is divisible: $\tfrac{p}{q} = n \cdot \tfrac{p}{nq}$. A **free abelian group** $\mathbb{Z}^{\oplus I}$ has no non-zero divisible element: if $x = (x_i) \neq 0$ has some $x_{i_0} \neq 0$, then $x$ is not divisible by any $n > |x_{i_0}|$, since a solution $ny = x$ would need $n y_{i_0} = x_{i_0}$ with $|x_{i_0}| < n$.

The bridge that makes the proof run — *a summand of a free abelian group is a subgroup of a free abelian group, hence cannot be non-trivially divisible*. Projectivity would force $\mathbb{Q}$ into a free abelian group, contradicting its divisibility.

---

# Convergent Strategy

**Problem class.** This is a *separate-two-properties* problem: exhibit a module satisfying one tower condition (flat) but not the next (projective), pinning down a strict inclusion. As the [[Commutative Algebra III — Flatness and Exactness]] strategy records, such separations are how the chapter proves its tower has no collapsing rungs, and each requires a *property a direct sum would have to share* to refute the stronger condition.

**Assumption pattern.** Two halves with opposite flavours. Flatness is *proved by climbing*: $\mathbb{Q}$ is a localization of $\mathbb{Z}$, and localizations are flat. Non-projectivity is *proved by an invariant*: $\mathbb{Q}$ is divisible, free abelian groups are not, and projectivity would embed $\mathbb{Q}$ in a free abelian group. The recognisable trigger for the refutation is "divisible vs. free."

**Theorem routing.** Flatness: $\mathbb{Q} = (\mathbb{Z}\setminus 0)^{-1}\mathbb{Z}$ is extension of scalars along $\mathbb{Z}\to\mathbb{Q}$, so [[Thm - Extension of Scalars Preserves Flatness|localization is flat]] gives flatness directly (alternatively, every tensor in $\mathbb{Q}\otimes V$ is pure, giving exactness by hand). Non-projectivity: if $\mathbb{Q}$ were projective, by the [[Thm - Projective iff Direct Summand of a Free Module|summand characterization]] $\mathbb{Q}$ would be a direct summand, hence a *subgroup*, of a free abelian group $\mathbb{Z}^{\oplus I}$; but $\mathbb{Q}$ is divisible and $\mathbb{Z}^{\oplus I}$ has no non-zero divisible elements — contradiction.

**Key decision point.** The non-obvious move is choosing the right invariant to refute projectivity. Cardinality fails ($\mathbb{Z}^{\oplus I}$ can be huge), rank fails (no obvious notion), and a direct injectivity argument is hopeless. The winning invariant is **divisibility**: it is preserved under passing to direct summands (a summand of a non-divisible group inherits non-divisibility *of its own* elements), and it cleanly separates $\mathbb{Q}$ from any free abelian group. The genuine insight is that "summand of free" forces "subgroup of free", and divisibility is exactly the property a free abelian group lacks at every non-zero element. The natural wrong route — trying to show no surjection $\mathbb{Z}^{\oplus I}\twoheadrightarrow\mathbb{Q}$ splits by constructing sections — is far harder than the one-line divisibility obstruction.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra III — Flatness and Exactness#Legal Operations|the topic page's Legal Operations]]:

1. **Recognise a localization as flat (operations 5 and 9).** $\mathbb{Q}$ is the localization $(\mathbb{Z}\setminus 0)^{-1}\mathbb{Z}$, and localizations are flat by [[Thm - Extension of Scalars Preserves Flatness|extension of scalars]].

2. **Use the summand form of projectivity (operation 7).** Projective $=$ direct summand of free, so a projective $\mathbb{Q}$ would be a subgroup of a free abelian group.

3. **Refute a structural property with a preserved invariant.** Divisibility passes to summands and distinguishes $\mathbb{Q}$ from every free abelian group — the obstruction that kills projectivity.

---

# Hints

> [!note]- Hint 1
> The two halves are unrelated in method. For flatness, ask: what *familiar construction* produces $\mathbb{Q}$ from $\mathbb{Z}$, and is that construction known to be flat? For non-projectivity, recall that projective means "summand of free", and a summand of a group is in particular a *subgroup*. What special property does $\mathbb{Q}$ have that a free abelian group cannot have?

> [!note]- Hint 2
> Flatness: $\mathbb{Q} = (\mathbb{Z}\setminus\{0\})^{-1}\mathbb{Z}$ is a localization, and [[Thm - Extension of Scalars Preserves Flatness|localizations are flat]]. (Or directly: every tensor in $\mathbb{Q}\otimes_{\mathbb{Z}} V$ is pure — you can pull all denominators across the $\otimes$ — which forces the natural map to be an isomorphism, giving exactness.)

> [!note]- Hint 3
> Non-projectivity: suppose $\mathbb{Q}$ were projective. By the [[Thm - Projective iff Direct Summand of a Free Module|summand characterization]], $\mathbb{Q}\oplus N\cong\mathbb{Z}^{\oplus I}$ for some $N$ and index set $I$. Then $\mathbb{Q}$ embeds as a subgroup of $\mathbb{Z}^{\oplus I}$. Now use *divisibility*.

> [!note]- Hint 4
> $\mathbb{Q}$ is divisible: every element is $n$ times another. But in $\mathbb{Z}^{\oplus I}$, take any non-zero $x = (x_i)$ with $x_{i_0}\neq 0$; for $n > |x_{i_0}|$ there is no $y$ with $ny = x$ (the $i_0$-coordinate would need $n y_{i_0} = x_{i_0}$, impossible). So no non-zero element of $\mathbb{Z}^{\oplus I}$ is divisible by *all* $n$. A non-zero element of $\mathbb{Q}$ inside $\mathbb{Z}^{\oplus I}$ would have to be — contradiction.

---

# Solution

The two halves use opposite strategies: flatness is established by recognising $\mathbb{Q}$ as a localization (climb the tower), and non-projectivity by a divisibility obstruction (an invariant a free abelian group cannot have). The crux is that "projective" forces "subgroup of a free abelian group", and divisibility is exactly what no non-zero element of a free abelian group possesses.

**Step 1: $\mathbb{Q}$ is flat over $\mathbb{Z}$.**

$\mathbb{Q}$ is the localization of $\mathbb{Z}$ at $S = \mathbb{Z}\setminus\{0\}$, and localizations are flat.

> [!note]- Derivation
> The [[Def - Field of Fractions|field of fractions]] $\mathbb{Q} = \operatorname{Frac}(\mathbb{Z})$ is the localization $S^{-1}\mathbb{Z}$ with $S = \mathbb{Z}\setminus\{0\}$. Localization is [[Def - Restriction and Extension of Scalars|extension of scalars]] along the ring map $\mathbb{Z}\to\mathbb{Q}$, $\mathbb{Q} = \mathbb{Q}\otimes_{\mathbb{Z}}\mathbb{Z}$, so by [[Thm - Extension of Scalars Preserves Flatness|extension of scalars preserves flatness]] (with $M = \mathbb{Z}$ flat over itself), $\mathbb{Q}$ is a flat $\mathbb{Z}$-module.
>
> *Direct verification, for confidence.* Every tensor in $\mathbb{Q}\otimes_{\mathbb{Z}} V$ is pure: $\sum_i \tfrac{a_i}{b_i}\otimes v_i = 1\otimes\big(\sum_i\tfrac{a_i}{b_i}v_i\big)$ after clearing denominators across the $\otimes$ (using $\tfrac{a}{b}\otimes v = \tfrac1b\otimes av = 1\otimes\tfrac{a}{b}v$ over the field $\mathbb{Q}$ acting on $V = \mathbb{Q}\otimes(\cdots)$). For an injection $f : V\hookrightarrow W$ of $\mathbb{Z}$-modules, $\operatorname{id}_{\mathbb{Q}}\otimes f$ sends $1\otimes v \mapsto 1\otimes f(v)$, and a kernel element $1\otimes w$ with $1\otimes f(w) = 0$ forces (purity plus the map $\mathbb{Q}\otimes V \to \mathbb{Q}\otimes_{\mathbb{Q}}(\mathbb{Q}\otimes V)$) $w$ torsion, hence $1\otimes w = 0$. So $\mathbb{Q}$ preserves injections.

**Step 2: $\mathbb{Q}$ is divisible; free abelian groups are not.**

$\mathbb{Q}$ is divisible, while every non-zero element of a free abelian group fails to be divisible by some integer.

> [!note]- Derivation
> *$\mathbb{Q}$ is divisible:* for $\tfrac{p}{q}\in\mathbb{Q}$ and $n\geq 1$, $\tfrac{p}{q} = n\cdot\tfrac{p}{nq}$, so $\tfrac{p}{q}$ is $n$ times an element of $\mathbb{Q}$. Every element is divisible by every $n$.
>
> *Free abelian groups have no non-zero divisible element:* let $F = \mathbb{Z}^{\oplus I}$ and $0\neq x = (x_i)_{i\in I}\in F$, with some coordinate $x_{i_0}\neq 0$. Choose $n > |x_{i_0}|$. If $ny = x$ for some $y = (y_i)\in F$, then $n y_{i_0} = x_{i_0}$, so $n \mid x_{i_0}$ with $0 < |x_{i_0}| < n$ — impossible. Hence $x$ is not divisible by $n$. So no non-zero $x\in F$ is divisible by all integers.

**Step 3: $\mathbb{Q}$ is not projective.**

If $\mathbb{Q}$ were projective it would be a subgroup of a free abelian group, contradicting Step 2.

> [!note]- Derivation
> Suppose, for contradiction, that $\mathbb{Q}$ is a [[Def - Projective Module|projective]] $\mathbb{Z}$-module. By the [[Thm - Projective iff Direct Summand of a Free Module|summand characterization]], there is a $\mathbb{Z}$-module $N$ and an index set $I$ with
> $$\mathbb{Q}\oplus N \cong \mathbb{Z}^{\oplus I}.$$
> In particular the inclusion of the first summand realizes $\mathbb{Q}$ as a *subgroup* of the free abelian group $F = \mathbb{Z}^{\oplus I}$.
>
> Take any non-zero $x\in\mathbb{Q}\subseteq F$. By Step 2, $x$ is divisible by every $n\geq 1$ *as an element of $\mathbb{Q}$* — and since $\mathbb{Q}$ is a subgroup of $F$, those witnesses $\tfrac{x}{n}\in\mathbb{Q}\subseteq F$ are elements of $F$ too, so $x$ is divisible by every $n$ *in $F$*. But Step 2 also says no non-zero element of $F$ is divisible by all $n$. Contradiction. Hence $\mathbb{Q}$ is not projective. $\blacksquare$

> [!note]- Complete formal solution
> **Flat.** $\mathbb{Q} = (\mathbb{Z}\setminus\{0\})^{-1}\mathbb{Z}$ is a localization of $\mathbb{Z}$, equivalently $\mathbb{Q} = \mathbb{Q}\otimes_{\mathbb{Z}}\mathbb{Z}$ is the extension of scalars of the flat $\mathbb{Z}$-module $\mathbb{Z}$ along $\mathbb{Z}\to\mathbb{Q}$. By [[Thm - Extension of Scalars Preserves Flatness|extension of scalars preserves flatness]], $\mathbb{Q}$ is flat over $\mathbb{Z}$.
>
> **Not projective.** Suppose $\mathbb{Q}$ were projective. By [[Thm - Projective iff Direct Summand of a Free Module|the summand characterization]], $\mathbb{Q}\oplus N\cong\mathbb{Z}^{\oplus I} =: F$ for some $N, I$, so $\mathbb{Q}$ is a subgroup of $F$. Now $\mathbb{Q}$ is divisible: each $\tfrac{p}{q} = n\cdot\tfrac{p}{nq}$. But $F$ has no non-zero divisible element: for $0\neq x = (x_i)\in F$ with $x_{i_0}\neq 0$ and $n > |x_{i_0}|$, no $y\in F$ satisfies $ny = x$ (coordinate $i_0$ fails). A non-zero $x\in\mathbb{Q}\subseteq F$ would be divisible by every $n$ in $F$ (its $\mathbb{Q}$-witnesses lie in $F$), contradicting this. Hence $\mathbb{Q}$ is not projective.
>
> Therefore $\mathbb{Q}$ is flat but not projective: the implication projective $\Rightarrow$ flat is strict. $\blacksquare$

---

# Key Takeaways

**To prove flatness, recognise the module as a localization or a base change of something flat — never grind through the definition.** $\mathbb{Q}$ is flat for the structural reason that it is $(\mathbb{Z}\setminus 0)^{-1}\mathbb{Z}$, and localizations are flat because passing to fractions is exact. This is the fastest flatness proof in the chapter and the template for many: when a module is built by inverting elements, adjoining fractions, or base-changing along a ring map, flatness comes from [[Thm - Extension of Scalars Preserves Flatness|extension of scalars preserves flatness]] rather than from a hand check of injections. The trigger is "fractions" or "base change"; the reaction is "flat, by localization." The direct purity argument ("every tensor in $\mathbb{Q}\otimes V$ is pure") is worth knowing as a sanity check and because it generalizes to $\operatorname{Frac}(R)\otimes V \cong V$ for any domain, but the localization route is the one to reach for.

**To refute a structural property like projectivity, find an invariant that a direct summand of a free module cannot have — divisibility is the canonical one for abelian groups.** The whole non-projectivity argument is one observation: projective forces "subgroup of free", and free abelian groups have *no* non-zero divisible elements, while $\mathbb{Q}$ is entirely divisible. The reusable principle is that "summand of free" is a strong structural constraint, and the way to exploit it is to name a property that (a) passes to subgroups/summands and (b) is visibly absent from free modules. Divisibility, torsion structure, and the existence of infinitely-divisible elements are the standard such invariants over $\mathbb{Z}$. The diagnostic to carry: when asked to show something is *not* projective, do not try to defeat all possible splittings directly — instead embed the hypothetical projective into a free module and find the contradiction in a single preserved invariant.

**Flat-not-projective is the first strict gap in the tower, and divisibility is its signature.** This exercise pins down that flatness genuinely lies below projectivity: $\mathbb{Q}$ has the exactness virtue (tensoring with it preserves injections) without the lifting/splitting virtue (it is no summand of a free module). The conceptual reason is that flatness is a *tensor*-side, finitely-checkable condition that divisible modules can satisfy, whereas projectivity is a *Hom*-side, lifting condition that divisible-but-not-free modules fail. Recognising this gap is what lets you classify a torsion-free non-free module correctly: it may well be flat (like $\mathbb{Q}$, or any localization) without being projective. The companion gaps — projective-not-free ([[Ex - A projective module that is not free]]) and torsion-free-not-flat ([[Ex - The maximal ideal (X,Y) is torsion-free but not flat]]) — complete the picture that all three tower inclusions are strict, the full content of [[Ex - Free implies projective implies flat implies torsion-free]].
