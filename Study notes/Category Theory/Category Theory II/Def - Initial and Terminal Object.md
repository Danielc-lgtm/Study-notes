---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
  - "Def - Opposite Category and Duality"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}, \mathcal{D}$ are [[Def - Category|categories]]; $A, B, C, X, Y$ are objects; $f, g, h$ are morphisms; and $\mathcal{C}(A, B)$ (also written $\mathrm{Hom}_{\mathcal{C}}(A, B)$) is the set of morphisms from $A$ to $B$, the **hom-set**. We write $1_A$ or $\mathrm{id}_A$ for the identity morphism on $A$, and $g \circ f$ for composition. The symbol $\mathbf{0}$ (or sometimes $\emptyset$, $\bot$) denotes an initial object and $\mathbf{1}$ (or $*$, $\top$) a terminal object; we use $0$ for a zero object when both coincide. The named categories used as examples are $\mathbf{Set}$ (sets and functions), $\mathbf{Grp}$ (groups and homomorphisms), $\mathbf{Ab}$ (abelian groups), $\mathbf{Ring}$ (unital rings and ring homomorphisms), $\mathbf{Top}$ (topological spaces and continuous maps), and $\mathbf{Cat}$ (small categories and functors). The full symbol registry is on the parent page [[Category Theory II — Universal Properties, Representability, and the Yoneda Lemma]].

This is a compound page: it defines four interlocking notions — **initial object**, **terminal object**, **zero object**, and **zero morphism** — because they are introduced together, the second is the formal dual of the first, and the last two are built directly on the first two and are not usable without them.

---

# Axiom Motivation

The whole of category theory rests on a single methodological commitment: an object is known not by what it is made of, but by how it relates to everything around it. The element-level description of a set, a group, or a space is invisible to a category; all the category sees is the arrows. So if we want to single out a distinguished object — the empty set, the one-point space, the trivial group — we are not allowed to say "the object with no elements" or "the object with one point". We have to say something about *arrows*. The definitions of initial and terminal object are the answer to the question: which purely arrow-theoretic conditions pin down these familiar objects?

Start with the empty set $\emptyset$ in $\mathbf{Set}$. What is special about it, said only in terms of functions? There is exactly one function from $\emptyset$ to any set $X$ — the empty function, which has nothing to do but exist. And $\emptyset$ is the *only* set with this property: if $S$ has even one element, there are $|X|$-many functions $S \to X$ when $|X| > 1$, not one. So "there is a unique function from me to every object" picks out $\emptyset$ on the nose. This is the **initial** condition. Dually, the one-point set $\{*\}$ has exactly one function *into* it from any $X$ (send everything to $*$), and again it is the only such set. That is the **terminal** condition. The two conditions are mirror images: terminal in $\mathcal{C}$ is precisely initial in the [[Def - Opposite Category and Duality|opposite category]] $\mathcal{C}^{op}$, where every arrow is reversed.

Why insist on *uniqueness* of the arrow, rather than mere existence? Existence alone is far too weak. Every set admits *some* function into $\{*\}$ and *some* function from $\emptyset$, but those facts are not what is special — uniqueness is the entire content. Drop uniqueness and you lose the object: in $\mathbf{Set}$ a two-element set still receives a function from $\emptyset$ (the empty one) but it is no longer characterized, because so does everything else, and many objects admit a function *into* a two-element set. It is the clause "there is **exactly one**" that forces the object to be determined up to a *unique* isomorphism (see [[Thm - Uniqueness of Universal Objects]]). This uniqueness-of-the-map is not decoration; it is the whole mechanism by which an arrow-condition can name an object. Strengthen the condition the other way — demand that the unique map also be, say, a monomorphism — and you exclude the genuine initial objects (the empty map $\emptyset \to \emptyset$ is fine, but there is no reason a unique map should be monic in general), so the definition would name nothing in most categories.

A subtlety worth internalizing now: a category may have an initial object, a terminal object, both, neither, or several of each — but any two initial objects are uniquely isomorphic, so we speak of *the* initial object. In $\mathbf{Set}$ the initial object $\emptyset$ is unique on the nose, while terminal objects (the singletons) form a whole family, all uniquely isomorphic. When the initial and terminal objects *coincide* — one object that is simultaneously initial and terminal — something rigid happens: between any two objects there is then a canonical "do-nothing" morphism that factors through it. That object is called a **zero object**, and the canonical morphisms it manufactures are the **zero morphisms**. These are exactly the right notions for categories of structures with a distinguished trivial element (the zero vector, the identity element of a group, the zero of a ring-module): the trivial group, the trivial vector space, the zero module are all zero objects, and "the zero map" between two modules is the zero morphism in this precise sense.

---

# The Definition

Let $\mathcal{C}$ be a category.

**Initial object.** An object $\mathbf{0} \in \mathcal{C}$ is **initial** if for every object $X \in \mathcal{C}$ the hom-set $\mathcal{C}(\mathbf{0}, X)$ has exactly one element: there is a unique morphism $\mathbf{0} \to X$.

**Terminal object.** An object $\mathbf{1} \in \mathcal{C}$ is **terminal** if for every object $X \in \mathcal{C}$ the hom-set $\mathcal{C}(X, \mathbf{1})$ has exactly one element: there is a unique morphism $X \to \mathbf{1}$. Equivalently, $\mathbf{1}$ is terminal in $\mathcal{C}$ if and only if it is initial in $\mathcal{C}^{op}$.

**Zero object.** An object $0 \in \mathcal{C}$ is a **zero object** if it is both initial and terminal.

**Zero morphism.** If $\mathcal{C}$ has a zero object $0$, then for any two objects $X, Y$ the **zero morphism** $0_{X,Y} : X \to Y$ is the unique composite
$$X \longrightarrow 0 \longrightarrow Y,$$
where $X \to 0$ is the unique map to the terminal object and $0 \to Y$ is the unique map from the initial object. These zero morphisms are absorbing: $0_{Y,Z} \circ f = 0_{X,Z}$ and $g \circ 0_{X,Y} = 0_{X,Z}$ for any $f : X \to Y$ and $g : Y \to Z$, because both sides factor through $0$.

---

# Categorical / Structural Definition

The cleanest categorical packaging — and the one that makes the link to representability immediate — is this. Recall the **constant functor** $\Delta_{*} : \mathcal{C} \to \mathbf{Set}$ that sends every object to a fixed one-point set $* = \{\bullet\}$ and every morphism to the identity of $*$. Then:

> An object $\mathbf{0}$ is initial if and only if the covariant hom-functor $\mathcal{C}(\mathbf{0}, -) : \mathcal{C} \to \mathbf{Set}$ is naturally isomorphic to $\Delta_{*}$. An object $\mathbf{1}$ is terminal if and only if the contravariant hom-functor $\mathcal{C}(-, \mathbf{1}) : \mathcal{C}^{op} \to \mathbf{Set}$ is naturally isomorphic to $\Delta_{*}$.

Unwound, this says nothing more than "every hom-set out of $\mathbf{0}$ is a singleton" and "every hom-set into $\mathbf{1}$ is a singleton", which is the definition above. But phrased this way it announces the theme of the whole chapter: an object's universal property is a statement about its represented functor. In the language of [[Def - Hom-Functor and Representable Functor|representable functors]], $\mathcal{C}$ has an initial object if and only if the constant singleton functor $\Delta_{*} : \mathcal{C} \to \mathbf{Set}$ is representable, and a terminal object if and only if $\Delta_{*} : \mathcal{C}^{op} \to \mathbf{Set}$ is representable. Initial and terminal objects are thus the very first — and simplest — examples of [[Def - Universal Property and Universal Arrow|universal properties]].

---

# Relate to Other Fields / Compression

Initial and terminal objects are the categorical residue of "empty" and "full" across mathematics. The empty set, the trivial group, the zero module, the zero ideal, the least element of a lattice — these are all initial objects in their respective categories; the one-point set, the trivial group again, the whole space, the greatest element of a lattice are terminal. A surprisingly large amount of structure is governed by the single observation that a particular object is initial or terminal: it forces the existence of canonical maps, and (via [[Thm - Uniqueness of Universal Objects]]) forces those maps to assemble coherently.

The deepest compression is the one in the categorical definition: **an initial object is just a terminal object viewed in the mirror.** Every statement about initial objects becomes a statement about terminal objects by reversing all arrows and passing to $\mathcal{C}^{op}$, and conversely. This is the first instance of the [[Def - Opposite Category and Duality|duality principle]] that you should learn to use reflexively — prove a theorem about one, get the other for free.

**True name:** an initial (terminal) object is *an object with a unique-map property* — the unique-out (unique-in) object. When you see "unique morphism to every object" or "unique morphism from every object", do not picture the empty set or the singleton; picture the universal property, because that is what transfers to unfamiliar categories where "empty" and "one-point" make no sense.

---

# Examples / Corollaries

**Is an instance — $\emptyset$ and $\{*\}$ in $\mathbf{Set}$.** The empty set is initial: the unique function $\emptyset \to X$ is the empty function. Any one-element set $\{*\}$ is terminal: the unique function $X \to \{*\}$ is the constant. Note $\mathbf{Set}$ has a single initial object but a proper class of terminal objects (every singleton), all uniquely isomorphic. These do *not* coincide, so $\mathbf{Set}$ has no zero object.

**Is an instance — the trivial group is a zero object in $\mathbf{Grp}$.** The trivial group $\{e\}$ (see [[Def - Group]]) is *both* initial and terminal in $\mathbf{Grp}$: from $\{e\}$ to any group $G$ there is exactly one homomorphism (it must send $e \mapsto e_G$), and from any $G$ to $\{e\}$ there is exactly one (everything goes to $e$). So $\{e\}$ is a **zero object**, and the resulting zero morphism $G \to H$ is the homomorphism sending every element of $G$ to the identity of $H$ — exactly "the trivial homomorphism". The same holds in $\mathbf{Ab}$, $\mathbf{Vect}_k$, and $R\text{-}\mathbf{Mod}$: the trivial/zero object is a zero object, and zero morphisms are the zero maps. This is the categorical reason these subjects have a well-behaved "kernel and cokernel" calculus.

**Is an instance — $\mathbb{Z}$ is initial in $\mathbf{Ring}$, the zero ring is terminal.** The ring of integers $\mathbb{Z}$ (see [[Def - Ring]]) is the initial object in the category of unital rings: for any unital ring $R$ there is exactly one ring homomorphism $\mathbb{Z} \to R$, forced by $1 \mapsto 1_R$ (then $n \mapsto n \cdot 1_R$, with no freedom). The terminal object is the **zero ring** $\{0\}$ in which $0 = 1$: every ring maps uniquely onto it. Since $\mathbb{Z} \neq \{0\}$, $\mathbf{Ring}$ has no zero object — a structural difference from $\mathbf{Grp}$ that reflects the rigidity forced by demanding $1 \mapsto 1$.

**Is an instance — least and greatest elements of a poset.** A [[Def - Category|partially ordered set]] $(P, \leq)$ is a category with one arrow $a \to b$ exactly when $a \leq b$. An initial object is then an element below everything: the **least element** $\bot$. A terminal object is the **greatest element** $\top$. Most posets have neither — $(\mathbb{Z}, \leq)$ has no least or greatest element — which is the cleanest illustration that initial/terminal objects need not exist.

**Is NOT an instance — the integers under their usual order.** In the poset $(\mathbb{Z}, \leq)$ there is no initial object: no integer is $\leq$ every integer. Likewise no terminal object. This is the standard witness that a category can have neither.

**Is NOT an instance — a two-element set is not terminal in $\mathbf{Set}$.** From a set $X$ with $|X| \geq 1$ there are $2^{|X|}$ functions into $\{0, 1\}$, not one. Existence of *a* map is not the point; uniqueness is. The two-element set famously *represents* the [[Def - Hom-Functor and Representable Functor|power-set functor]] instead, a different universal property entirely.

**Corollary — initial/terminal objects are unique up to unique isomorphism.** If $\mathbf{0}, \mathbf{0}'$ are both initial, the unique maps $u : \mathbf{0} \to \mathbf{0}'$ and $v : \mathbf{0}' \to \mathbf{0}$ compose to endomorphisms $vu : \mathbf{0} \to \mathbf{0}$ and $uv : \mathbf{0}' \to \mathbf{0}'$, which must equal the unique endomorphisms $1_{\mathbf{0}}$ and $1_{\mathbf{0}'}$. So $u$ is an isomorphism, and it is the only one. This is proved in full at [[Thm - Uniqueness of Universal Objects]].

**Calibration check.** Verify that in $\mathbf{Cat}$ the empty category $\mathbf{0}$ (no objects) is initial and the terminal category $\mathbf{1}$ (one object, one arrow) is terminal. Check that the zero morphism in $\mathbf{Ab}$ from $\mathbb{Z}$ to $\mathbb{Z}$ is the map $n \mapsto 0$, and confirm it is absorbing: composing it with any homomorphism on either side gives the zero map again. Finally, explain why $\mathbf{Set}$ cannot have a zero object (the candidate would have to be both empty and a singleton).

---

# Unlocked by This

> [!tip] Universal Property as Initial/Terminal *(from this chapter)*
> Every [[Def - Universal Property and Universal Arrow|universal property]] in mathematics — free groups, tensor products, quotients, limits — is secretly the statement that some object is initial or terminal in a cleverly chosen auxiliary category (a [[Def - Category of Elements|category of elements]] or a comma category). Initial and terminal objects are not a minor special case; they are the *template* for all universality.

> [!tip] Zero Objects and Abelian Categories *(from Homological Algebra)*
> A category with a zero object, in which every morphism has a kernel and a cokernel and these behave well, is the road to an **abelian category** — the setting for homological algebra, **derived functors**, **Ext** and **Tor**. The zero morphism defined here is exactly the morphism whose kernel and cokernel build the long exact sequences of the subject.
