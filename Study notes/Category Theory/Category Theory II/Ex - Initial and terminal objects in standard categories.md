---
type: exercise
subject: category-theory
difficulty: "⭐"
prereqs:
  - "Def - Initial and Terminal Object"
  - "Def - Category"
tags: [category-theory, foundations]
---

# Problem Statement

Identify the initial object, the terminal object, and (where it exists) the zero object in each of the following categories. In each case prove the universal property — that the relevant hom-set is a singleton — and state whether initial and terminal coincide.

1. $\mathbf{Set}$ (sets and functions).
2. $\mathbf{Grp}$ (groups and homomorphisms).
3. $\mathbf{Ring}$ (unital rings and ring homomorphisms).
4. $\mathbf{Top}$ (topological spaces and continuous maps).
5. A poset $(P, \leq)$ regarded as a category.
6. $\mathbf{Cat}$ (small categories and functors).

**Recall:**

![[Def - Initial and Terminal Object#The Definition]]

An [[Def - Initial and Terminal Object|initial object]] $\mathbf{0}$ has a unique morphism $\mathbf{0} \to X$ to every object $X$; a terminal object $\mathbf{1}$ has a unique morphism $X \to \mathbf{1}$ from every object; a **zero object** is one that is both, and it manufactures a **zero morphism** $X \to 0 \to Y$ between any two objects. In a poset-as-category there is one arrow $a \to b$ exactly when $a \leq b$ (see [[Def - Category]]).

---

# Convergent Strategy

**Problem class:** This is an existence-and-uniqueness problem of the most basic categorical type: pin down a distinguished object purely by the cardinality of certain hom-sets. The routine, as set out on the topic page, is to translate "initial/terminal" into "every hom-set out of/into this object is a singleton" and then verify that count concretely in each category.

**Assumption pattern:** Each category comes with a concrete description of its morphisms (functions, homomorphisms, continuous maps, functors), so the assumptions are the *defining constraints those morphisms must satisfy*. The skill is to ask: given the constraints, how much freedom does a morphism out of a candidate $\mathbf{0}$ (or into a candidate $\mathbf{1}$) have? When the constraints force the morphism uniquely, you have found the universal object.

**Theorem routing:** No deep theorem is needed; the entire route is the definition of [[Def - Initial and Terminal Object|initial and terminal object]] plus, for the coincidence question, the observation that a zero object exists exactly when the unique candidate is simultaneously initial and terminal. [[Thm - Uniqueness of Universal Objects]] guarantees the answers are unique up to unique isomorphism, which is why we may speak of "the" initial object.

**Key decision point:** The non-obvious move is in $\mathbf{Ring}$, where one must remember that ring homomorphisms preserve $1$. That single constraint forces $\mathbb{Z}$ to be initial (the image of $1$ is forced, hence everything) and prevents $\mathbb{Z}$ from being terminal — so $\mathbf{Ring}$, unlike $\mathbf{Grp}$, has *no* zero object. Recognizing that the unit-preservation axiom breaks the symmetry is the heart of the exercise.

---

# Legal Operations Used

1. **Operation 1 from the topic page (translate universality into a hom-set count).** In every part, "initial" is replaced by "$\mathcal{C}(\mathbf{0}, X)$ is a singleton for all $X$" and "terminal" by "$\mathcal{C}(X, \mathbf{1})$ is a singleton for all $X$", and we verify the count directly.

2. **Operation 2 from the topic page (read off a morphism from generators / forced values).** In $\mathbf{Grp}$ and $\mathbf{Ring}$ we use that a homomorphism is determined by where it sends the identity / the unit, which forces uniqueness.

---

# Hints

> [!note]- Hint 1
> For each category, separately hunt for the initial object (unique map *out*) and the terminal object (unique map *in*). They may or may not coincide.

> [!note]- Hint 2
> In $\mathbf{Set}$: how many functions are there from $\emptyset$ to any set? How many into a one-point set? In $\mathbf{Top}$ the same answers hold with "continuous" added for free.

> [!note]- Hint 3
> In $\mathbf{Grp}$ the trivial group $\{e\}$ admits a unique homomorphism in *both* directions — it is a zero object. In $\mathbf{Ring}$, ask what a homomorphism $\mathbb{Z} \to R$ must do to $1$, and separately what the terminal object must be (hint: $0 = 1$).

> [!note]- Hint 4
> A poset has an initial object iff it has a least element, terminal iff a greatest. $\mathbf{Cat}$: the empty category and the one-arrow category.

---

# Solution

The route is uniform: in each category translate "initial/terminal" into a singleton-hom-set condition and verify it from the concrete description of morphisms. The one subtlety is $\mathbf{Ring}$, where unit-preservation makes $\mathbb{Z}$ initial but blocks a zero object; everywhere else the bookkeeping is routine.

**Step 1: $\mathbf{Set}$ — $\emptyset$ initial, singletons terminal, no zero object.**

> [!note]- Derivation
> There is exactly one function $\emptyset \to X$ for any set $X$: a function is a single-valued total assignment on its domain, and the empty domain has nothing to assign, so the empty function is the unique such. Hence $\emptyset$ is initial. For any one-point set $\{*\}$ and any $X$, a function $X \to \{*\}$ must send every element to $*$, and exactly one function does this; so $\{*\}$ is terminal. Since $\emptyset \neq \{*\}$ (different cardinalities), they do not coincide: $\mathbf{Set}$ has **no zero object**. (Note there are many terminal objects, all uniquely isomorphic, but a single initial object.)

**Step 2: $\mathbf{Grp}$ — the trivial group is a zero object.**

> [!note]- Derivation
> Let $\{e\}$ be the [[Def - Group|trivial group]]. A homomorphism $\{e\} \to G$ must send $e \mapsto e_G$ (the identity goes to the identity), and exactly one map does so; so $\{e\}$ is initial. A homomorphism $G \to \{e\}$ must send everything to $e$, and exactly one does; so $\{e\}$ is terminal. Both at once: $\{e\}$ is a **zero object**. The induced zero morphism $G \to H$ is the homomorphism sending every $g \mapsto e_H$ — the trivial homomorphism. (The same holds in $\mathbf{Ab}$ and $\mathbf{Vect}_k$.)

**Step 3: $\mathbf{Ring}$ — $\mathbb{Z}$ initial, the zero ring terminal, no zero object.**

> [!note]- Derivation
> A unital ring homomorphism preserves $1$. A homomorphism $f : \mathbb{Z} \to R$ (see [[Def - Ring]]) must have $f(1) = 1_R$, hence $f(n) = n \cdot 1_R$ for all $n$ — completely forced, and this assignment is a homomorphism. So there is exactly one map $\mathbb{Z} \to R$: $\mathbb{Z}$ is **initial**. The terminal object is the **zero ring** $\{0\}$ in which $0 = 1$: every ring maps onto it by the unique map sending everything to $0$ (this respects $1 \mapsto 1$ because $1 = 0$ there). Since $\mathbb{Z} \neq \{0\}$, there is **no zero object** — the unit-preservation axiom breaks the symmetry that gives $\mathbf{Grp}$ its zero object.

**Step 4: $\mathbf{Top}$ — $\emptyset$ initial, the one-point space terminal.**

> [!note]- Derivation
> The empty space $\emptyset$ has a unique (empty, vacuously continuous) map to any space $X$, so it is initial. The one-point space $*$ receives a unique continuous map from any $X$ (the constant map, which is always continuous), so it is terminal. They differ, so no zero object. This mirrors $\mathbf{Set}$, with continuity coming for free.

**Step 5: poset $(P, \leq)$ — least element initial, greatest element terminal.**

> [!note]- Derivation
> In the poset-as-category there is at most one arrow between any two objects. An initial object is an element $\bot$ with an arrow to every object, i.e. $\bot \leq x$ for all $x$ — a **least element**. A terminal object is a **greatest element** $\top$. Both hom-sets are automatically singletons when the elements exist (thinness of the category). Many posets have neither: $(\mathbb{Z}, \leq)$ has no least or greatest element.

**Step 6: $\mathbf{Cat}$ — the empty category initial, the terminal category terminal.**

> [!note]- Derivation
> The empty category $\mathbf{0}$ (no objects, no arrows) admits a unique functor to any small category $\mathcal{C}$ (the empty functor), so it is initial. The terminal category $\mathbf{1}$ (one object, only its identity) receives a unique functor from any $\mathcal{C}$ (everything goes to the one object, every arrow to the identity), so it is terminal. They differ, no zero object.

> [!note]- Complete formal solution
> **$\mathbf{Set}$:** $\emptyset$ is initial (unique empty function out), any singleton is terminal (unique constant in); distinct, so no zero object. **$\mathbf{Grp}$:** $\{e\}$ is both initial and terminal — a zero object — since the identity-to-identity constraint forces a unique homomorphism each way; the zero morphism is the trivial homomorphism. **$\mathbf{Ring}$:** $\mathbb{Z}$ is initial because $f(1) = 1_R$ forces $f(n) = n \cdot 1_R$; the zero ring $\{0\}$ ($0=1$) is terminal; distinct, no zero object. **$\mathbf{Top}$:** $\emptyset$ initial, one-point space terminal; no zero object. **Poset:** least element initial, greatest element terminal; may have neither. **$\mathbf{Cat}$:** empty category initial, terminal category $\mathbf{1}$ terminal; no zero object. In every case [[Thm - Uniqueness of Universal Objects]] guarantees the objects are unique up to unique isomorphism. $\blacksquare$

---

# Key Takeaways

**The unit-preservation axiom is what severs initial from terminal in $\mathbf{Ring}$.** The single most instructive contrast in this exercise is $\mathbf{Grp}$ versus $\mathbf{Ring}$. Groups have a zero object because the trivial group sits symmetrically at both ends: the identity-to-identity rule lets you map in and out uniquely. Rings break this symmetry because a homomorphism must send $1 \mapsto 1$, and the only ring where $1$ is "trivial enough" to receive everything is the degenerate ring with $0 = 1$, which is *not* the initial ring $\mathbb{Z}$. The general lesson: whenever a category's morphisms must preserve a chosen element or constant, check whether that constraint makes the trivial object fail to be initial or terminal — it often does, and the presence or absence of a zero object is a fingerprint of how rigid the morphisms are.

**Initial and terminal are dual, so you always solve two mirror problems at once.** Every part of this exercise is really two problems joined by [[Def - Opposite Category and Duality|duality]]: find the unique-map-out object and find the unique-map-in object. Recognizing the symmetry halves the work and is the right reflex: once you have found the initial object of $\mathcal{C}$, you have found the terminal object of $\mathcal{C}^{op}$ for free, and vice versa. The trigger is the literal phrase "initial or terminal"; the reaction is to set up the singleton-hom-set condition and check it in both variances.

**Existence is not guaranteed, and the poset case is the cleanest reminder.** It is tempting to assume every category has these distinguished objects, but $(\mathbb{Z}, \leq)$ has neither a least nor a greatest element, hence neither an initial nor a terminal object. The poset case is the diagnostic: initial/terminal objects are *least/greatest elements*, and most orders have neither. When a problem hands you a category, do not presuppose universal objects exist — prove existence, or find the obstruction. This same caution recurs for [[Def - Limit and Colimit|limits and colimits]], which need not exist in an arbitrary category.
