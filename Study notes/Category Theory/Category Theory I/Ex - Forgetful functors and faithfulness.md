---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Functor"
  - "Def - Full, Faithful, and Essentially Surjective Functor"
  - "Def - Group"
tags: [category-theory, foundations]
---

# Problem Statement

Let $U : \mathbf{Grp} \to \mathbf{Set}$ be the [[Def - Functor|forgetful functor]] sending a [[Def - Group|group]] to its underlying set and a [[Def - Homomorphism|homomorphism]] to its underlying function.

1. Show $U$ is [[Def - Full, Faithful, and Essentially Surjective Functor|faithful]].
2. Show $U$ is **not** full, by exhibiting a function between underlying sets that is not a homomorphism.
3. Show $U$ is **not** essentially surjective (so it is not, even, surjective up to iso on a meaningful invariant) — or, more precisely, determine the image of $U$ on objects and decide whether it is all of $\mathbf{Set}$ up to iso.
4. Generalize: explain why every "forget structure" functor from an algebraic category to $\mathbf{Set}$ is faithful, and characterize when it is full.

**Recall:**

![[Def - Full, Faithful, and Essentially Surjective Functor#The Definition]]

A [[Def - Functor|functor]] is **faithful** if injective on each hom-set, **full** if surjective on each hom-set, **essentially surjective** if every target object is isomorphic to one in the image.

---

# Convergent Strategy

**Problem class:** This is a "diagnose the properties of a named functor" exercise — running a given functor against the full/faithful/essentially-surjective checklist and producing witnesses for the failures.

**Assumption pattern:** Faithfulness is automatic for forgetful functors because a homomorphism *is* its underlying function plus the (redundant) fact that it preserves structure — so two [[Def - Homomorphism|homomorphisms]] with the same underlying function are equal. Non-fullness needs a witness: a function that is not structure-preserving. Essential surjectivity asks whether every set underlies some group.

**Theorem routing:** Faithfulness: a morphism in $\mathbf{Grp}$ determines its underlying function. Non-fullness: exhibit $f : \mathbb{Z} \to \mathbb{Z}$ that is not additive. Essential surjectivity: every nonempty set carries *some* group structure (so $U$ is "surjective on objects up to iso" on nonempty sets), but the empty set underlies no group — diagnose carefully.

**Key decision point:** The subtle part is (3): one must decide whether "every set is the underlying set of a group" is true. It is true for nonempty sets (transport a group structure along a bijection to any set of the same cardinality, or use free [[Def - Group|groups]] / products of $\mathbb{Z}/n$), but the empty set is not the underlying set of any group (a group has an identity). So $U$ misses exactly $\emptyset$ up to iso, hence is not essentially surjective. Getting this edge case right is the crux.

---

# Legal Operations Used

1. **Operation: a morphism of an algebraic category is its underlying function plus axioms** (topic page, Legal Operation 1). This gives faithfulness for free.

2. **Operation: refute fullness by a non-structure-preserving map** (topic page, Legal Operation 3). Exhibit a function that is not a homomorphism.

3. **Operation: transport structure along a bijection** (topic page, Legal Operation 4). Used to decide essential surjectivity on nonempty sets.

---

# Hints

> [!note]- Hint 1
> Faithful: if two group homomorphisms $\varphi, \psi : G \to H$ have $U\varphi = U\psi$ (same underlying function), what can you conclude about $\varphi$ and $\psi$?

> [!note]- Hint 2
> Not full: take $G = H = \mathbb{Z}$. The homomorphisms $\mathbb{Z} \to \mathbb{Z}$ are exactly $n \mapsto kn$. Is the function $n \mapsto n^2$, or $n \mapsto n+1$, among them?

> [!note]- Hint 3
> Essentially surjective: does every set underlie a group? Consider a nonempty finite set of size $n$ — put $\mathbb{Z}/n$ on it. Now consider $\emptyset$ — does a group with empty underlying set exist?

> [!note]- Hint 4
> Generalize: a homomorphism in any algebraic category is a function satisfying equations. Why does that force faithfulness? When are *all* functions automatically homomorphisms (fullness)?

---

# Solution

The plan: faithfulness is immediate (a homomorphism is determined by its underlying function); non-fullness needs one witness map; essential surjectivity holds on nonempty sets (transport a group structure) but fails on $\emptyset$; the generalization reads off "faithful always, full iff the structure imposes no constraint on maps".

**Step 1: $U$ is faithful.**

> [!note]- Derivation
> Let $\varphi, \psi : G \to H$ be group homomorphisms with $U\varphi = U\psi$, i.e. they are equal *as functions* $G \to H$. Then $\varphi(g) = \psi(g)$ for all $g$, so $\varphi = \psi$ as homomorphisms (a homomorphism carries no data beyond its underlying function — the homomorphism property is a constraint, not extra structure). Hence $U_{G,H} : \mathbf{Grp}(G, H) \to \mathbf{Set}(UG, UH)$ is injective, and $U$ is [[Def - Full, Faithful, and Essentially Surjective Functor|faithful]].

**Step 2: $U$ is not full.**

> [!note]- Derivation
> Take $G = H = (\mathbb{Z}, +)$. A group homomorphism $\mathbb{Z} \to \mathbb{Z}$ is determined by the image of $1$ and has the form $n \mapsto kn$ for some fixed $k$. Now the function $f : \mathbb{Z} \to \mathbb{Z}$, $f(n) = n + 1$, is a perfectly good morphism in $\mathbf{Set}$ (an element of $\mathbf{Set}(U\mathbb{Z}, U\mathbb{Z})$), but it is *not* a homomorphism: $f(0) = 1 \neq 0$, whereas any homomorphism must send $0 \mapsto 0$. So $f$ has no preimage under $U_{\mathbb{Z}, \mathbb{Z}}$, the map is not surjective, and $U$ is **not full**.

**Step 3: $U$ is not essentially surjective.**

> [!note]- Derivation
> Ask which sets are isomorphic (i.e. equal, in $\mathbf{Set}$, up to bijection) to $UG$ for some group $G$. Every *nonempty* set $S$ is: pick any group structure on a set of the same cardinality — for finite $|S| = n$ use $\mathbb{Z}/n$, for infinite $S$ use a [[Def - Free Group and Free Product|free group]] or a direct sum of copies of $\mathbb{Z}$ of the right cardinality — and transport it along a bijection. So every nonempty set is in the essential image.
>
> The exception is the **empty set**. A group must contain an identity element, so its underlying set is nonempty; $|UG| \geq 1$ always. Hence $\emptyset$ is *not* isomorphic to any $UG$, and $U$ is **not essentially surjective**. (It misses exactly one isomorphism class of sets, $\emptyset$.)

**Step 4: The general pattern.**

> [!note]- Derivation
> Let $\mathcal{A}$ be an algebraic category (groups, [[Def - Ring|rings]], [[Def - Module|modules]], lattices, ...) and $U : \mathcal{A} \to \mathbf{Set}$ the functor forgetting the operations. A morphism of $\mathcal{A}$ is a function satisfying equational conditions (preserve the operations), so it is *determined by its underlying function*; therefore $U$ is **always faithful**. The forgetful functor is **full** if and only if every function between underlying sets automatically preserves the structure — which essentially never happens for genuine algebraic structure (there is always a function violating an operation), so forgetful functors are typically not full. The degenerate exception: if the "structure" imposes no constraint on maps (e.g. forgetting a structure carried by *no* operations, or the identity functor), the forgetful functor is full. The takeaway: *forgetful = faithful; full forgetful = no genuine structure.*

> [!note]- Complete formal solution
> *Faithful:* $U\varphi = U\psi \Rightarrow \varphi = \psi$ as functions $\Rightarrow \varphi = \psi$ as homomorphisms.
>
> *Not full:* $f(n) = n+1$ is a function $\mathbb{Z} \to \mathbb{Z}$ but not a homomorphism ($f(0) \neq 0$), so $U_{\mathbb{Z},\mathbb{Z}}$ is not surjective.
>
> *Not essentially surjective:* every nonempty set carries a group structure (transport $\mathbb{Z}/n$ or a free group along a bijection), but $\emptyset$ underlies no group (groups have an identity), so $\emptyset$ is missed.
>
> *General:* forgetful functors from algebraic categories are always faithful (a morphism is its underlying function plus equational constraints); full only when the structure constrains no maps. $\blacksquare$

---

# Key Takeaways

**Forgetful functors are the canonical faithful-but-not-full functors.** The reusable classification is that any "forget the operations" functor $U : \mathcal{A} \to \mathbf{Set}$ is faithful because a structure-preserving map is its underlying function plus a *property* (not extra data), so distinct morphisms have distinct underlying functions. It fails to be full precisely because genuine algebraic structure rules out most functions as homomorphisms. This pair of facts — faithful, not full — is what makes $\mathcal{A}$ a "concrete category sitting over $\mathbf{Set}$ with real structure", and it is the single most common functor profile in algebra. Whenever you forget structure, you should reflexively expect faithful-not-full.

**Faithfulness is the precise meaning of "concrete category".** A category is *concrete* when it comes with a faithful functor to $\mathbf{Set}$, allowing its objects to be treated as "sets with structure" and its morphisms as "structure-preserving functions". This exercise shows why faithfulness is the right requirement: it is exactly what guarantees no information about morphisms is lost in passing to underlying functions, so element-chasing arguments are valid. The trigger: if you want to argue about a category's morphisms by manipulating elements, first confirm there is a faithful functor to $\mathbf{Set}$; faithfulness licenses the element-level reasoning.

**Edge cases live at the empty set and the initial object.** The essential-surjectivity analysis hinges entirely on the empty set, which underlies no group because a group is required to have an identity. This is a recurring pattern: subtle failures of categorical statements about "underlying sets" almost always concentrate at $\emptyset$ or the initial/terminal objects, where existence-of-structure constraints bite. When checking essential surjectivity, surjectivity, or any "every object" claim involving underlying sets, *always test the empty case separately* — it is where the counterexample, if any, hides. The general method of transporting structure along a bijection handles every nonempty case uniformly, leaving the empty case as the sole, and decisive, exception.
