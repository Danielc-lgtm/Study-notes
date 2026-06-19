---
type: exercise
subject: category-theory
difficulty: "⭐"
prereqs:
  - "Def - Product and Coproduct"
  - "Def - Initial and Terminal Object"
  - "Def - Limit and Colimit"
tags: [category-theory, foundations]
---

# Problem Statement

Show that the [[Def - Product and Coproduct|product]] of the *empty* family of objects is a [[Def - Initial and Terminal Object|terminal object]], and dually that the empty coproduct is an initial object. Conclude that a category "with all finite products" must have a terminal object (the nullary case), and identify the terminal objects of $\mathbf{Set}$, $\mathbf{Grp}$, and $\mathbf{Top}$.

**Recall:**

A **product** $\prod_{i \in I} A_i$ is an object with projections $\pi_i$ such that for every $X$, a map $X \to \prod_i A_i$ is the same as a family of maps $(X \to A_i)_{i \in I}$.

![[Def - Initial and Terminal Object#The Definition]]

The empty product is the [[Def - Limit and Colimit|limit]] of the unique diagram $\emptyset \to \mathcal{C}$ (the empty diagram), whose index category has no objects and no morphisms.

---

# Convergent Strategy

**Problem class:** This is a "degenerate-case identification" problem: take a general universal construction and specialise its index to the empty set, then read off what the universal property becomes. The routine is to write the universal property with $I = \emptyset$ and simplify the (now vacuous) family-of-maps data.

**Assumption pattern:** The only "assumption" is the index set being empty. The unlocking observation is that a family of maps indexed by the empty set is *no data at all* — the empty family — so the universal property degenerates from "a map into the product is a family of maps" to "a map into the object is unique/exists".

**Theorem routing:** The universal property of the empty product says: for every $X$, maps $X \to \prod_\emptyset A_i$ correspond to empty families of maps, of which there is exactly one. So there is exactly one map $X \to \prod_\emptyset$ for every $X$ — which is precisely the [[Def - Initial and Terminal Object|definition of a terminal object]]. The route is "empty product $=$ limit of empty diagram $=$ terminal object".

**Key decision point:** The subtle point is that "exactly one empty family" must be parsed correctly: the empty family is unique (there is one function from $\emptyset$, the empty function), and it satisfies all (zero) compatibility conditions vacuously. Conflating "no maps" with "no object" is the trap — the empty product is a genuine object (terminal), not nothing.

---

# Legal Operations Used

1. **Specialise a universal property to a degenerate index (from the topic page: "verify the universal property").** Set $I = \emptyset$ in the product universal property and simplify.

2. **Read maps into a limit as cones (representability / [[Def - Cone and Cocone|cone]] description).** A cone over the empty diagram is just an apex with no legs, so a map into the empty product is just "a map to the object", with no constraints.

3. **Dualize (pass to the opposite category).** The empty coproduct is the empty product in $\mathcal{C}^{op}$, hence an initial object.

---

# Hints

> [!note]- Hint 1
> Write down the universal property of $\prod_{i \in I} A_i$ and then put $I = \emptyset$. What does "a family of maps indexed by $\emptyset$" amount to?

> [!note]- Hint 2
> A family indexed by the empty set carries no information — there is exactly one such family (empty), and it satisfies every (vacuous) condition. So "a map into the empty product is a family of maps" collapses to "there is exactly one map into the empty product".

> [!note]- Hint 3
> "Exactly one map from every $X$" is the definition of a terminal object. For $\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Top}$, find the object that everything maps to uniquely.

---

# Solution

The argument is to specialise the product universal property to the empty index and observe it becomes the terminal-object property. The empty family of maps is unique, so a map into the empty product exists and is unique from every object — which is terminality. Dualizing gives the initial-object statement, and the concrete terminal objects follow.

**Step 1: A map into the empty product is unique.**

> [!note]- Derivation
> By the universal property of $\prod_{i \in I} A_i$, for every object $X$ a morphism $X \to \prod_{i \in I} A_i$ corresponds bijectively to a family of morphisms $(\lambda_i : X \to A_i)_{i \in I}$ satisfying the (here vacuous) compatibility conditions. With $I = \emptyset$, a family indexed by $\emptyset$ is the empty family, of which there is exactly one, and it satisfies all zero conditions vacuously. Hence there is exactly one morphism $X \to \prod_\emptyset A_i$ for each $X$.

**Step 2: The empty product is terminal.**

> [!note]- Derivation
> An object $T$ with a unique morphism $X \to T$ from every object $X$ is by definition a [[Def - Initial and Terminal Object|terminal object]]. Step 1 shows $\prod_\emptyset A_i$ has exactly this property, so it *is* a terminal object. Equivalently, the empty product is the [[Def - Limit and Colimit|limit]] of the empty diagram, and the limit of the empty diagram is terminal because a cone over it with apex $X$ is just $X$ (no legs), so the terminal cone is the terminal object.

**Step 3: Finite products require a terminal object; dual statement; examples.**

> [!note]- Derivation
> A category "with all finite products" must include the nullary product, so it has a terminal object. Dually, in $\mathcal{C}^{op}$ the empty coproduct is the empty product, hence terminal in $\mathcal{C}^{op}$, i.e. **initial** in $\mathcal{C}$; so "all finite coproducts" forces an initial object. Concretely the terminal objects are: in $\mathbf{Set}$ a one-point set $\{*\}$ (a unique function $X \to \{*\}$); in $\mathbf{Grp}$ the trivial group $\{e\}$ (a unique homomorphism, sending everything to $e$ — note $\{e\}$ is also *initial* in $\mathbf{Grp}$, a zero object); in $\mathbf{Top}$ the one-point space (a unique continuous map $X \to \{*\}$).

> [!note]- Complete formal solution
> Let $\prod_{i \in I} A_i$ be the product of a family indexed by $I$. Its universal property states that for every object $X$, morphisms $X \to \prod_{i} A_i$ correspond bijectively to families $(X \to A_i)_{i \in I}$. Taking $I = \emptyset$: a family indexed by the empty set is the empty family, the unique such family, satisfying all (zero) compatibility conditions vacuously. Therefore there is exactly one morphism $X \to \prod_{\emptyset} A_i$ from every object $X$, which is the defining property of a [[Def - Initial and Terminal Object|terminal object]]. Hence the empty product is a terminal object; equivalently it is the [[Def - Limit and Colimit|limit]] of the empty diagram. Consequently any category with all finite products has a terminal object (the nullary case). Dualizing in $\mathcal{C}^{op}$, the empty coproduct is an initial object, so any category with all finite coproducts has an initial object. The terminal objects are: $\{*\}$ in $\mathbf{Set}$, the trivial group in $\mathbf{Grp}$ (which is also initial, hence a zero object), and the one-point space in $\mathbf{Top}$. By [[Thm - Limits are Unique up to Unique Isomorphism|uniqueness of limits]], the terminal object is unique up to unique isomorphism. $\blacksquare$

---

# Key Takeaways

**Nullary cases of universal constructions are not curiosities — they force the existence of unit objects.** The decisive realisation is that specialising a product to the empty index turns its universal property into the terminal-object property, so "has finite products" automatically packages "has a terminal object" as the nullary case, just as "has finite coproducts" packages an initial object. This is why the definition of a [[Def - Complete and Cocomplete Category|finitely complete]] category lists "finite products and equalizers" and the terminal object comes for free: the empty product *is* the terminal object. The transferable diagnostic: whenever a construction is defined for families, check what it does on the empty family — the answer is usually the relevant unit (terminal/initial object, the trivial group, the zero module, the empty union), and it is forced, not optional.

**The empty family carries exactly one element of data, and that is what makes the empty product terminal.** The trigger-reaction pattern to internalise is "indexed by $\emptyset$ $\Rightarrow$ unique, vacuous data". A family of maps over the empty index set is the empty function, which exists and is unique, and satisfies every quantified-over-$\emptyset$ condition automatically. This vacuous-uniqueness is exactly the "exactly one map from every $X$" that defines terminality. The same parsing resolves a host of degenerate cases: the empty intersection is the whole space, the empty sum is $0$, the empty product (of numbers) is $1$, the limit over the empty diagram is terminal — all instances of "the universal construction over no constraints is the unit".

**Distinguish "no maps" from "no object": the empty product is a real, terminal object.** The common error is to think the empty product is somehow empty or nonexistent. It is the opposite — it is the object every other object maps to uniquely, which in $\mathbf{Set}$ is a one-point set, not the empty set (the empty set is *initial*, the empty coproduct). Keeping the terminal/initial duality straight is the reusable skill: terminal objects receive unique maps (empty product, one-point set, trivial group as target), initial objects emit unique maps (empty coproduct, empty set, trivial group as source). In $\mathbf{Grp}$ the trivial group is *both*, a zero object, which is why $\mathbf{Grp}$ has a zero morphism between any two groups — a fact that becomes important for kernels and the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] viewed categorically.
