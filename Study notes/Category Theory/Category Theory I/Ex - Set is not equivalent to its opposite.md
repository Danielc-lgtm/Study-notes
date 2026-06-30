---
type: exercise
subject: category-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Opposite Category and Duality"
  - "Def - Equivalence of Categories"
  - "Def - Full, Faithful, and Essentially Surjective Functor"
tags: [category-theory, foundations]
---

# Problem Statement

Prove that $\mathbf{Set}$ is **not** [[Def - Equivalence of Categories|equivalent]] to its [[Def - Opposite Category and Duality|opposite category]] $\mathbf{Set}^{\mathrm{op}}$. Use the asymmetry between the **initial object** (the empty set $\emptyset$) and the **terminal object** (a singleton $1$): there is exactly one function $\emptyset \to X$ for every set $X$, and exactly one function $X \to 1$ for every set $X$, but the behaviour of these two objects is not interchangeable.

**Recall:**

![[Def - Equivalence of Categories#The Definition]]

An object $I$ is **initial** if $\mathbf{Set}(I, X)$ is a singleton for every $X$; an object $T$ is **terminal** if $\mathbf{Set}(X, T)$ is a singleton for every $X$. An [[Def - Equivalence of Categories|equivalence]] is [[Def - Full, Faithful, and Essentially Surjective Functor|full, faithful, and essentially surjective]] and preserves all categorical properties. A property of an object expressed purely with hom-sets is preserved by any equivalence.

---

# Convergent Strategy

**Problem class:** This is a "prove no equivalence exists" impossibility argument — the hardest exercise type, because one must rule out *all* functors at once. The route is to find a categorical invariant that an equivalence must preserve and exhibit a value it cannot match across $\mathbf{Set}$ and $\mathbf{Set}^{\mathrm{op}}$.

**Assumption pattern:** The leverage is that an equivalence preserves every property stated in the language of categories, in particular it sends initial objects to initial objects and terminal objects to terminal objects. Crucially, passing to $\mathbf{Set}^{\mathrm{op}}$ *swaps* initial and terminal (an initial object of $\mathbf{Set}^{\mathrm{op}}$ is a terminal object of $\mathbf{Set}$). So an equivalence $\mathbf{Set} \simeq \mathbf{Set}^{\mathrm{op}}$ would force a structural symmetry between the empty set and a singleton that does not exist.

**Theorem routing:** Use that equivalences preserve initial/terminal objects and, more sharply, preserve the entire hom-functor profile of each object up to natural iso. Then compute a hom-set asymmetry: $\mathbf{Set}(X, \emptyset) = \emptyset$ for $X \neq \emptyset$, while dually $\mathbf{Set}(1, X) = X$ is never empty. No bijection can match these profiles.

**Key decision point:** The non-obvious choice is *which* invariant to use. "Initial and terminal both exist in both categories" is not enough — both $\mathbf{Set}$ and $\mathbf{Set}^{\mathrm{op}}$ have an initial and a terminal object. The sharper invariant is the *map-counting profile around the initial object versus the terminal object*: the empty set has the property "almost nothing maps into it" while the singleton has "everything maps into it", and these profiles are genuinely different and must be preserved.

---

# Legal Operations Used

1. **Operation: use that equivalences preserve categorical properties** (topic page, Legal Operation 9). An equivalence sends initial to initial, terminal to terminal, and preserves hom-set cardinalities up to the object-isomorphism.

2. **Operation: pass a property through the opposite to swap it** (topic page, Legal Operation 8). Initial in $\mathbf{Set}^{\mathrm{op}}$ = terminal in $\mathbf{Set}$; this swap is the engine of the contradiction.

3. **Operation: refute existence by an invariant mismatch** (topic page, Legal Operation 3). Exhibit a hom-set profile preserved by equivalence that cannot be matched.

---

# Hints

> [!note]- Hint 1
> An equivalence preserves initial and terminal objects. In $\mathbf{Set}$, the initial object is $\emptyset$ and the terminal object is a singleton $1$. What are they in $\mathbf{Set}^{\mathrm{op}}$?

> [!note]- Hint 2
> Suppose $F : \mathbf{Set} \to \mathbf{Set}^{\mathrm{op}}$ is an equivalence. It must send the initial object $\emptyset$ of $\mathbf{Set}$ to the initial object of $\mathbf{Set}^{\mathrm{op}}$. But the initial object of $\mathbf{Set}^{\mathrm{op}}$ is the *terminal* object of $\mathbf{Set}$, a singleton.

> [!note]- Hint 3
> Now compare hom-set profiles. Around $\emptyset$ in $\mathbf{Set}$: $\mathbf{Set}(X, \emptyset)$ is empty for all $X \neq \emptyset$. Around a singleton $1$ in $\mathbf{Set}$: $\mathbf{Set}(X, 1)$ is a singleton for all $X$. An equivalence preserves these profiles up to the object-bijection. Can the empty-set profile equal the singleton profile?

---

# Solution

The plan: suppose an equivalence $F : \mathbf{Set} \to \mathbf{Set}^{\mathrm{op}}$ exists. It must preserve initial and terminal objects, but the opposite swaps them, so $F$ matches $\emptyset$ with a singleton. We then compute that the categorical "profile" of $\emptyset$ (how morphisms relate to it) differs from that of a singleton in a way an equivalence cannot reconcile, yielding a contradiction.

**Step 1: An equivalence preserves initial and terminal objects.**

> [!note]- Derivation
> Both "initial" and "terminal" are categorical properties: $I$ is initial iff each $\mathcal{C}(I, X)$ is a singleton; $T$ is terminal iff each $\mathcal{C}(X, T)$ is a singleton. An [[Def - Equivalence of Categories|equivalence]] $F$ is [[Def - Full, Faithful, and Essentially Surjective Functor|fully faithful]], so it induces bijections $\mathcal{C}(A, B) \cong \mathcal{D}(FA, FB)$, and it is essentially surjective, so it hits every object up to iso. Hence $F$ sends an initial object to an initial object and a terminal object to a terminal object. In $\mathbf{Set}$ the initial object is $\emptyset$ (one map $\emptyset \to X$, the empty function) and the terminal object is any singleton $1$ (one map $X \to 1$, the constant map).

**Step 2: The opposite swaps initial and terminal.**

> [!note]- Derivation
> By the [[Def - Opposite Category and Duality|definition of the opposite]], $\mathbf{Set}^{\mathrm{op}}(I, X) = \mathbf{Set}(X, I)$. So $I$ is initial in $\mathbf{Set}^{\mathrm{op}}$ iff $\mathbf{Set}(X, I)$ is a singleton for all $X$, i.e. iff $I$ is *terminal* in $\mathbf{Set}$ — a singleton. Likewise the terminal object of $\mathbf{Set}^{\mathrm{op}}$ is the initial object of $\mathbf{Set}$, namely $\emptyset$.
>
> Therefore an equivalence $F : \mathbf{Set} \to \mathbf{Set}^{\mathrm{op}}$ must send the initial object $\emptyset$ of $\mathbf{Set}$ to the initial object of $\mathbf{Set}^{\mathrm{op}}$, which is a singleton $1$ of $\mathbf{Set}$. So $F(\emptyset) \cong 1$ in $\mathbf{Set}^{\mathrm{op}}$, equivalently $F(\emptyset)$ "is" the singleton.

**Step 3: The profiles of $\emptyset$ and $1$ disagree — contradiction.**

> [!note]- Derivation
> An equivalence preserves *all* hom-set cardinalities up to the object-bijection: $|\mathcal{C}(A, B)| = |\mathcal{D}(FA, FB)|$. Apply this with $A = \emptyset$. In $\mathbf{Set}$, the empty set has the property
> $$|\mathbf{Set}(X, \emptyset)| = 0 \quad \text{for every } X \neq \emptyset,$$
> because a function $X \to \emptyset$ from a nonempty set does not exist. Translating to $\mathbf{Set}^{\mathrm{op}}$: $\mathbf{Set}^{\mathrm{op}}(F\emptyset, FX) = \mathbf{Set}^{\mathrm{op}}(1, FX) = \mathbf{Set}(FX, 1)$, which is a *singleton* for every $FX$. So the equivalence demands
> $$0 = |\mathbf{Set}(X, \emptyset)| = |\mathbf{Set}^{\mathrm{op}}(F\emptyset, FX)| = |\mathbf{Set}(FX, 1)| = 1$$
> for every $X \neq \emptyset$ — that is, $0 = 1$, a contradiction. (Concretely: the initial object $\emptyset$ has *almost no* morphisms into it, while the singleton it would be matched with has *exactly one* morphism into it from every object. These profiles cannot be reconciled by any functor inducing hom-set bijections.) Hence no equivalence $\mathbf{Set} \simeq \mathbf{Set}^{\mathrm{op}}$ exists.

> [!note]- Complete formal solution
> Suppose $F : \mathbf{Set} \to \mathbf{Set}^{\mathrm{op}}$ is an equivalence. Being fully faithful and essentially surjective, $F$ preserves initial objects and induces hom-set bijections $|\mathbf{Set}(A,B)| = |\mathbf{Set}^{\mathrm{op}}(FA, FB)|$. The initial object of $\mathbf{Set}$ is $\emptyset$; the initial object of $\mathbf{Set}^{\mathrm{op}}$ is the terminal object of $\mathbf{Set}$, a singleton $1$. So $F\emptyset \cong 1$. For any $X \neq \emptyset$,
> $$0 = |\mathbf{Set}(X, \emptyset)| = |\mathbf{Set}^{\mathrm{op}}(F\emptyset, FX)| = |\mathbf{Set}(FX, 1)| = 1,$$
> a contradiction. Hence $\mathbf{Set} \not\simeq \mathbf{Set}^{\mathrm{op}}$. $\blacksquare$

> [!warning] Why the cheaper argument fails
> One might try "$\mathbf{Set}$ has an initial object distinct from its terminal object, so does $\mathbf{Set}^{\mathrm{op}}$, no contradiction" — and indeed that observation alone proves nothing, since both categories have a distinct initial and terminal object. The asymmetry must be located in the *hom-set profile* (how many maps run into versus out of the special objects), not merely in the existence of initial/terminal objects. The empty set's defining feature is "nothing nonempty maps into it", which has no mirror at the singleton; that is the irreducible asymmetry.

---

# Key Takeaways

**Impossibility proofs run on preserved invariants.** To show two categories are *not* equivalent, you cannot inspect candidate functors one at a time — there are too many. Instead, find a property that *every* equivalence must preserve, and exhibit a value of that property that the two categories cannot share. Here the invariant is the hom-set profile around initial/terminal objects. This is the universal shape of non-equivalence and non-isomorphism arguments throughout mathematics: identify a functorial or categorical invariant, compute it on both sides, observe a mismatch. The skill is choosing an invariant fine enough to detect the difference.

**The opposite category swaps every "in" with every "out".** The decisive mechanism is that $(-)^{\mathrm{op}}$ interchanges initial with terminal, monomorphism with epimorphism, products with coproducts, "injective into" with "surjective onto". So to use duality against self-equivalence, look for a categorical asymmetry between an "in" notion and its "out" mirror. $\mathbf{Set}$ is asymmetric in exactly this way: the empty set is extreme for *outgoing* maps (one map out to anything) but degenerate for *incoming* maps (no maps in from anything nonempty), while the singleton is the reverse. A category with a built-in in/out asymmetry cannot be self-dual, and recognizing such asymmetries is the quickest route to ruling out self-equivalence.

**Most categories are not self-dual, and the few that are are special.** This exercise should permanently calibrate the expectation that $\mathcal{C} \simeq \mathcal{C}^{\mathrm{op}}$ is *rare*. Self-duality holds for finite-dimensional vector spaces, finite abelian [[Def - Group|groups]] (Pontryagin), and compact-versus-discrete (Gelfand/Stone), and in each case it is a substantive theorem encoding a genuine symmetry of the subject. For everyday categories — $\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Top}$, $\mathbf{Ring}$ — the opposite is a genuinely different category (the opposite of $\mathbf{Set}$ is complete atomic Boolean algebras, the opposite of $\mathbf{CRing}$ is affine schemes), and that difference is precisely what makes duality a tool that *relates* fields rather than reflecting one onto itself.
