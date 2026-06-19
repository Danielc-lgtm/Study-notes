---
type: theorem
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Functor"
  - "Def - Natural Transformation"
  - "Def - Hom-Functor and Representable Functor"
  - "Def - The Yoneda Embedding"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a locally small category, $A \in \mathcal{C}$ an object, and $F : \mathcal{C} \to \mathbf{Set}$ a covariant functor (the contravariant form $F : \mathcal{C}^{op} \to \mathbf{Set}$ is stated as well). We write $\mathcal{C}(A, -)$ for the covariant [[Def - Hom-Functor and Representable Functor|hom-functor]], $\mathrm{Nat}(\mathcal{C}(A, -), F)$ for the set of [[Def - Natural Transformation|natural transformations]] from it to $F$, and $\alpha_X : \mathcal{C}(A, X) \to F(X)$ for the component of $\alpha$ at $X$. The identity at $A$ is $1_A \in \mathcal{C}(A, A)$. For $f : A \to X$ we write $F(f) : F(A) \to F(X)$. The full registry is on [[Category Theory II — Universal Properties, Representability, and the Yoneda Lemma]].

---

# Statement

> **Theorem (Yoneda Lemma, covariant form).** Let $\mathcal{C}$ be locally small, $A \in \mathcal{C}$, and $F : \mathcal{C} \to \mathbf{Set}$ a functor. Then evaluation at the identity,
> $$\mathrm{Nat}\big(\mathcal{C}(A, -),\, F\big) \xrightarrow{\ \cong\ } F(A), \qquad \alpha \longmapsto \alpha_A(1_A),$$
> is a bijection. Its inverse sends an element $a \in F(A)$ to the natural transformation $\Psi(a)$ with components
> $$\Psi(a)_X : \mathcal{C}(A, X) \to F(X), \qquad f \mapsto F(f)(a).$$
> Moreover this bijection is **natural in both $A$ and $F$**, i.e. it is a natural isomorphism of functors $\mathcal{C} \times [\mathcal{C}, \mathbf{Set}] \to \mathbf{Set}$.

> **Theorem (Yoneda Lemma, contravariant form).** For $F : \mathcal{C}^{op} \to \mathbf{Set}$ a [[Def - Presheaf|presheaf]] and $A \in \mathcal{C}$, evaluation at $1_A$ gives a bijection
> $$\mathrm{Nat}\big(\mathcal{C}(-, A),\, F\big) \cong F(A), \qquad \alpha \mapsto \alpha_A(1_A),$$
> natural in $A$ and $F$.

In words: **a natural transformation out of a representable functor into $F$ is the same thing as a single element of $F$ at the representing object.** A side consequence is that this collection of natural transformations, a priori possibly large, is genuinely a set.

---

# Motivation

The hom-functor $\mathcal{C}(A, -)$ packages "all arrows out of $A$" as a functor. The natural next question — and the one the previous section left unanswered — is: what are the natural transformations *out of* this functor? If we want to compare a representable functor with some other functor $F$, we need to know the maps between them, and there could in principle be a wild profusion of them. The Yoneda lemma is the astonishing answer that there are exactly as many as there are elements of $F(A)$, no more and no fewer, and that each one is rigidly determined by where it sends a single morphism, the identity $1_A$.

This is the technical heart of the whole subject. It is what makes the [[Def - The Yoneda Embedding|Yoneda embedding]] fully faithful (set $F = \mathcal{C}(B, -)$ and read off $\mathrm{Nat}(\mathcal{C}(A,-), \mathcal{C}(B,-)) \cong \mathcal{C}(B, A)$); it is what reduces a [[Def - Hom-Functor and Representable Functor|representation]] to a single [[Def - Universal Element|universal element]]; it is what proves [[Thm - Uniqueness of Universal Objects|universal objects are unique]]. Every later result that says "an object is determined by its functor of points", every computation of natural transformations, every functor-of-points argument in algebraic geometry, traces back to this one lemma. Its statement looks innocuous — almost a tautology — but the consequences take a whole subject to unfold.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal precondition is mild: any functor $F$ and any object $A$ in a locally small category. The art is recognizing the situations where computing $\mathrm{Nat}(\mathcal{C}(A,-), F)$ is the right move.

The first disguised source is **a request to compute or count natural transformations whose domain is representable**. Whenever you need to find all natural maps out of a hom-functor — natural endomorphisms of a forgetful functor, natural operations on a representable presheaf — the answer is "evaluate the codomain at the representing object". The non-obvious step is recognizing the domain as representable. *Example problem:* compute all natural endomorphisms of the forgetful functor $U : \mathbf{Grp} \to \mathbf{Set}$; since $U \cong \mathbf{Grp}(\mathbb{Z}, -)$ is representable, they are $\mathrm{Nat}(U, U) \cong U(\mathbb{Z}) = \mathbb{Z}$, one per integer (the $n$-th power map). See [[Ex - Computing a natural transformation set via Yoneda]].

The second disguised source is **proving two objects isomorphic via their represented functors**. If you can show $\mathcal{C}(-, A) \cong \mathcal{C}(-, B)$ as presheaves, Yoneda (through full faithfulness) gives $A \cong B$. The non-obviousness is that an isomorphism of *functors* is often easier to produce than a direct isomorphism of objects — you build it from natural bijections of hom-sets. *Example problem:* prove $V \otimes W \cong W \otimes V$ by exhibiting a natural isomorphism of the bilinear-map functors they represent, then invoke Yoneda (this is Riehl's Proposition 2.3.11; see [[Thm - Universal Property of the Tensor Product]]).

The third disguised source is **establishing representability**. A representation is a universal element $a \in F(A)$ such that $\Psi(a)$ is an isomorphism. The non-obvious bridge is that you do not need to construct a natural isomorphism by hand: by Yoneda it suffices to produce the single element $a$ and check the unique-factorization property. *Example problem:* show the units functor on rings is represented by $\mathbb{Z}[x, x^{-1}]$ by naming the universal element $x$ and checking it (see [[Def - Universal Element]]).

**Targets (Output Amplification)**

The bare conclusion is a bijection $\mathrm{Nat}(\mathcal{C}(A,-), F) \cong F(A)$. Combined with choices of $F$ it produces the main structural theorems.

Combine with **$F = \mathcal{C}(B, -)$ representable**. Then $\mathrm{Nat}(\mathcal{C}(A, -), \mathcal{C}(B, -)) \cong \mathcal{C}(B, A)$, which is exactly [[Thm - The Yoneda Embedding is Fully Faithful|full faithfulness of the Yoneda embedding]]. The further result is that $\mathcal{C}$ embeds into its presheaves, the cornerstone of the functor-of-points method. This is non-obvious because it turns a statement about *all* natural transformations into a statement about a *single* hom-set.

Combine with **naturality of the bijection**. Naturality in $F$ and $A$ is what lets you compose Yoneda identifications coherently — e.g. to show the bijection respects an extra structure, or to prove the category of elements is a comma category (see [[Def - Category of Elements]]). The further result $E$ is that representations are unique up to unique isomorphism ([[Thm - Uniqueness of Universal Objects]]), because the universal element transports naturally.

Combine with **a concrete $F$ and a clever $A$**. Choosing $\mathcal{C}$ to be a one-object category (a group or monoid) and $A$ its object yields Cayley's theorem and its monoid analogue; choosing $\mathcal{C} = \mathbf{CRing}^{op}$ yields "a scheme is determined by its functor of points". The further result is that diverse classical theorems are all the *same* lemma specialized. This is non-obvious because the classical statements look nothing alike.

---

# Why Is It True

Here is the intuition, with no formalism. A natural transformation $\alpha : \mathcal{C}(A, -) \Rightarrow F$ must, at each object $X$, take a morphism $f : A \to X$ and produce an element $\alpha_X(f) \in F(X)$, in a way compatible with all the maps of $\mathcal{C}$. Now ask: how much freedom does $\alpha$ have? Consider the special morphism $1_A : A \to A$. It sits in $\mathcal{C}(A, A)$, and $\alpha_A(1_A)$ is *some* element of $F(A)$ — call it $a$. The claim is that this one element determines everything else.

Why? Take any other $f : A \to X$. There is a fundamental relation: $f = f \circ 1_A$, and $f$ is exactly the image of $1_A$ under the function $\mathcal{C}(A, f) : \mathcal{C}(A, A) \to \mathcal{C}(A, X)$ (postcomposition by $f$). Naturality of $\alpha$ says the square relating the action of $f$ on the domain side and the codomain side commutes:
$$\alpha_X\big(\mathcal{C}(A, f)(1_A)\big) = F(f)\big(\alpha_A(1_A)\big),$$
and the left side is $\alpha_X(f)$ while the right side is $F(f)(a)$. So
$$\alpha_X(f) = F(f)(a).$$
Every value of $\alpha$ is forced: it is $a$ pushed forward along $f$. This is the whole lemma.

> **A natural transformation out of a representable functor is pinned down by where it sends the identity, because every morphism $f : A \to X$ is the identity transported along $f$, and naturality forces $\alpha$ to transport its value on the identity the same way.**

Conversely, *any* element $a \in F(A)$ defines a natural transformation by the formula $\Psi(a)_X(f) = F(f)(a)$ — one checks naturality is automatic, again from functoriality of $F$. So the two operations (evaluate at the identity; transport an element) are mutually inverse, and the correspondence is a bijection. The element $a$ is the universal element; the identity $1_A$ is the universal morphism it springs from.

---

# What Makes This Hard

The lemma is hard not because the proof is long — it is a page — but because the statement is so frictionless that it is easy to misread as a triviality and miss what is being asserted. The non-obvious step is the *direction of the forcing*: it is naturality, applied to the single equation $f = f \circ 1_A$, that converts "the value of $\alpha$ on the identity" into "the value of $\alpha$ on everything". The most common errors are: (i) forgetting to check that $\Psi(a)$ is actually natural (the formula $f \mapsto F(f)(a)$ must satisfy a naturality square for a *generic* morphism $g : X \to Y$, not just for maps out of $A$); (ii) confusing the two directions of the bijection — evaluation versus transport; and (iii) overlooking that the universal element of a *contravariant* functor lives in $F(A)$ and may not be the "obvious" element (the power-set example, where it is $\{1\}$, not $1$). The naturality-in-both-variables clause is also routinely skipped, yet it is what makes the lemma usable in chains of identifications.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Define the forward map by evaluation at $1_A$ and the backward map $\Psi$ by transport, $\Psi(a)_X(f) = F(f)(a)$. Check $\Psi(a)$ is natural; then check the two maps are mutually inverse. Finally verify naturality of the bijection in $A$ and $F$ by chasing the relevant squares.

**Subgoal decomposition:**

1. **The backward map is well-defined.** For $a \in F(A)$, show $\Psi(a)$ with $\Psi(a)_X(f) = F(f)(a)$ is a natural transformation $\mathcal{C}(A, -) \Rightarrow F$.
   - *Hint:* For a generic $g : X \to Y$, both legs of the naturality square send $f \in \mathcal{C}(A, X)$ to $F(g \circ f)(a)$; use $F(g \circ f) = F(g) \circ F(f)$.
   - *Why needed:* Without naturality, $\Psi(a)$ is not even a legal element of the codomain.

2. **$\Psi$ is a right inverse to evaluation.** Show $\mathrm{ev}_{1_A}(\Psi(a)) = a$.
   - *Hint:* $\Psi(a)_A(1_A) = F(1_A)(a) = 1_{F(A)}(a) = a$.
   - *Why needed:* It shows evaluation is surjective and identifies the inverse.

3. **$\Psi$ is a left inverse to evaluation.** Show $\Psi(\alpha_A(1_A)) = \alpha$ for any natural $\alpha$.
   - *Hint:* It suffices to match components: $\Psi(\alpha_A(1_A))_X(f) = F(f)(\alpha_A(1_A))$, and naturality of $\alpha$ applied to $f$ gives $F(f)(\alpha_A(1_A)) = \alpha_X(f)$.
   - *Why needed:* It shows evaluation is injective, completing the bijection.

4. **Naturality in $F$ and in $A$.** Show the bijection commutes with a natural transformation $\beta : F \Rightarrow G$ and with a morphism $f : A \to A'$.
   - *Hint:* For naturality in $F$, both routes send $\alpha$ to $\beta_A(\alpha_A(1_A))$, using the definition of vertical composition. For naturality in $A$, chase $1_A$ versus $1_{A'}$ through precomposition.
   - *Why needed:* It upgrades the object-wise bijection to a natural isomorphism, which is what later applications use.

---

# Lemma Decomposition

> [!note]- Lemma 1: The transport formula defines a natural transformation
> **Statement:** For $a \in F(A)$, the components $\Psi(a)_X : \mathcal{C}(A, X) \to F(X)$, $f \mapsto F(f)(a)$, form a natural transformation $\mathcal{C}(A, -) \Rightarrow F$.
>
> **Hint:** Check the naturality square for an arbitrary $g : X \to Y$; both composites send $f$ to $F(g \circ f)(a)$.
>
> **Why needed:** It guarantees the candidate inverse $\Psi$ actually lands in $\mathrm{Nat}(\mathcal{C}(A, -), F)$.
>
> > [!note]- Full proof
> > Fix $g : X \to Y$. The naturality square requires $\Psi(a)_Y \circ \mathcal{C}(A, g) = F(g) \circ \Psi(a)_X$ as functions $\mathcal{C}(A, X) \to F(Y)$. For $f \in \mathcal{C}(A, X)$:
> > $$\big(\Psi(a)_Y \circ \mathcal{C}(A, g)\big)(f) = \Psi(a)_Y(g \circ f) = F(g \circ f)(a),$$
> > $$\big(F(g) \circ \Psi(a)_X\big)(f) = F(g)\big(F(f)(a)\big) = \big(F(g) \circ F(f)\big)(a) = F(g \circ f)(a),$$
> > using functoriality $F(g \circ f) = F(g) \circ F(f)$. The two agree, so $\Psi(a)$ is natural.

> [!note]- Lemma 2: Evaluation and transport are mutually inverse
> **Statement:** $\mathrm{ev}_{1_A}(\Psi(a)) = a$ for all $a \in F(A)$, and $\Psi(\alpha_A(1_A)) = \alpha$ for all natural $\alpha : \mathcal{C}(A, -) \Rightarrow F$.
>
> **Hint:** The first is immediate from $F(1_A) = \mathrm{id}$. The second is naturality of $\alpha$ applied to the relation $f = f \circ 1_A$.
>
> **Why needed:** Together these say the forward map (evaluation) is a bijection with inverse $\Psi$ — the entire bijection claim.
>
> > [!note]- Full proof
> > *Right inverse.* $\mathrm{ev}_{1_A}(\Psi(a)) = \Psi(a)_A(1_A) = F(1_A)(a) = a$, since $F(1_A) = 1_{F(A)}$.
> >
> > *Left inverse.* Let $\alpha$ be natural and set $a = \alpha_A(1_A)$. We show $\Psi(a) = \alpha$ by matching components. For $f \in \mathcal{C}(A, X)$, naturality of $\alpha$ at the morphism $f$ gives the commuting square $\alpha_X \circ \mathcal{C}(A, f) = F(f) \circ \alpha_A$. Evaluating at $1_A \in \mathcal{C}(A, A)$ and using $\mathcal{C}(A, f)(1_A) = f \circ 1_A = f$:
> > $$\alpha_X(f) = \alpha_X\big(\mathcal{C}(A, f)(1_A)\big) = F(f)\big(\alpha_A(1_A)\big) = F(f)(a) = \Psi(a)_X(f).$$
> > So $\alpha_X = \Psi(a)_X$ for all $X$, i.e. $\alpha = \Psi(a)$.

> [!note]- Lemma 3: The bijection is natural in $F$ and in $A$
> **Statement:** Given $\beta : F \Rightarrow G$, the square relating $\mathrm{ev}^F_{1_A}$, $\mathrm{ev}^G_{1_A}$, postcomposition by $\beta$, and $\beta_A$ commutes. Given $f : A \to A'$, the square relating $\mathrm{ev}_{1_A}$, $\mathrm{ev}_{1_{A'}}$, precomposition by $f$, and $F(f)$ commutes.
>
> **Hint:** Use the definition of vertical composition of natural transformations: $(\beta \circ \alpha)_A = \beta_A \circ \alpha_A$.
>
> **Why needed:** Naturality in both variables is what allows Yoneda identifications to be composed and transported, underpinning [[Thm - Uniqueness of Universal Objects]] and the comma-category description of [[Def - Category of Elements]].
>
> > [!note]- Full proof
> > *Naturality in $F$.* For $\alpha : \mathcal{C}(A, -) \Rightarrow F$, the top-right route gives $\beta_A(\mathrm{ev}^F_{1_A}(\alpha)) = \beta_A(\alpha_A(1_A))$; the left-bottom route gives $\mathrm{ev}^G_{1_A}(\beta \circ \alpha) = (\beta \circ \alpha)_A(1_A) = \beta_A(\alpha_A(1_A))$ by the definition of vertical composition. They agree.
> >
> > *Naturality in $A$.* For $f : A \to A'$, precomposition by $f$ sends $\alpha : \mathcal{C}(A, -) \Rightarrow F$ to $\alpha \circ f^* : \mathcal{C}(A', -) \Rightarrow F$, where $f^* : \mathcal{C}(A', -) \Rightarrow \mathcal{C}(A, -)$ is precomposition. The left-bottom route is $(\alpha \circ f^*)_{A'}(1_{A'}) = \alpha_{A'}(f^*_{A'}(1_{A'})) = \alpha_{A'}(1_{A'} \circ f) = \alpha_{A'}(f)$. The top-right route is $F(f)(\alpha_A(1_A))$. By the naturality square of $\alpha$ at $f$ (as in Lemma 2), $\alpha_{A'}(f) = F(f)(\alpha_A(1_A))$. They agree.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — set-up.** Fix a locally small category $\mathcal{C}$, an object $A$, and a functor $F : \mathcal{C} \to \mathbf{Set}$. Define
> $$\mathrm{ev}_{1_A} : \mathrm{Nat}(\mathcal{C}(A, -), F) \to F(A), \qquad \alpha \mapsto \alpha_A(1_A),$$
> and
> $$\Psi : F(A) \to \mathrm{Nat}(\mathcal{C}(A, -), F), \qquad \Psi(a)_X(f) = F(f)(a) \text{ for } f \in \mathcal{C}(A, X).$$
>
> **Step 1 — $\Psi(a)$ is natural.** For arbitrary $g : X \to Y$ and $f \in \mathcal{C}(A, X)$,
> $$\Psi(a)_Y(g \circ f) = F(g \circ f)(a) = F(g)(F(f)(a)) = F(g)(\Psi(a)_X(f)),$$
> so $\Psi(a)_Y \circ \mathcal{C}(A, g) = F(g) \circ \Psi(a)_X$. Hence $\Psi(a) \in \mathrm{Nat}(\mathcal{C}(A, -), F)$. (Lemma 1.)
>
> **Step 2 — $\mathrm{ev}_{1_A} \circ \Psi = \mathrm{id}$.** $\mathrm{ev}_{1_A}(\Psi(a)) = \Psi(a)_A(1_A) = F(1_A)(a) = a$, since $F(1_A) = 1_{F(A)}$.
>
> **Step 3 — $\Psi \circ \mathrm{ev}_{1_A} = \mathrm{id}$.** Let $\alpha$ be natural, $a = \alpha_A(1_A)$. For $f \in \mathcal{C}(A, X)$, naturality of $\alpha$ at $f$ gives $\alpha_X \circ \mathcal{C}(A, f) = F(f) \circ \alpha_A$. Evaluating at $1_A$ and using $\mathcal{C}(A, f)(1_A) = f$:
> $$\alpha_X(f) = F(f)(\alpha_A(1_A)) = F(f)(a) = \Psi(a)_X(f).$$
> So $\alpha = \Psi(a) = \Psi(\mathrm{ev}_{1_A}(\alpha))$. (Lemma 2.)
>
> **Step 4 — bijection.** Steps 2 and 3 exhibit $\Psi$ as a two-sided inverse of $\mathrm{ev}_{1_A}$, so $\mathrm{ev}_{1_A}$ is a bijection. In particular $\mathrm{Nat}(\mathcal{C}(A, -), F)$ is a set.
>
> **Step 5 — naturality in $F$ and $A$.** By Lemma 3, the bijection commutes with postcomposition by any $\beta : F \Rightarrow G$ (naturality in $F$) and with precomposition along any $f : A \to A'$ matched with $F(f)$ (naturality in $A$). Hence $\mathrm{ev}_{1_A}$ is a natural isomorphism of functors $\mathcal{C} \times [\mathcal{C}, \mathbf{Set}] \to \mathbf{Set}$.
>
> **Contravariant form.** Apply the covariant proof with $\mathcal{C}$ replaced by $\mathcal{C}^{op}$: a presheaf $F : \mathcal{C}^{op} \to \mathbf{Set}$ is a covariant functor on $\mathcal{C}^{op}$, $\mathcal{C}(-, A) = \mathcal{C}^{op}(A, -)$, and the same evaluation-at-$1_A$ map is a natural bijection $\mathrm{Nat}(\mathcal{C}(-, A), F) \cong F(A)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Cayley's theorem in group theory.** Apply the lemma to $\mathcal{C} = BG$, the one-object category of a group $G$, with $F = \mathcal{C}(-, *)$ the representable presheaf. The natural endomorphisms of the right $G$-set $G$ are exactly left multiplications, so $G$ embeds in the permutations of its underlying set — Cayley's theorem (see [[Def - Group]]). The application is non-obvious because Cayley's theorem is usually proved by an ad-hoc left-regular-representation argument; Yoneda reveals it as a structural inevitability. See [[Ex - Yoneda generalizes Cayley's theorem]].

**Row operations as left multiplication (linear algebra).** In the category $\mathbf{Mat}_R$ of matrices, a "row operation on matrices with $n$ rows" is a natural endomorphism of the representable functor $\mathbf{Mat}_R(-, n)$. By Yoneda these correspond to elements of $\mathbf{Mat}_R(n, n) = n \times n$ matrices, namely left multiplication — and the matrix is obtained by performing the operation on the identity matrix. The application is non-obvious because "every row operation is left multiplication" looks like a computation, but is a corollary of naturality.

**Schemes are their points (algebraic geometry).** Apply the contravariant lemma to $\mathcal{C} = \mathbf{CRing}^{op}$: a morphism of affine schemes $\mathrm{Spec}\,R \to \mathrm{Spec}\,S$ is a natural transformation of their functors of points, which by Yoneda is a ring map $S \to R$. This is the statement that an affine scheme is determined by its $R$-points across all rings $R$. The application is non-obvious because it founds an entire subject on the lemma. See [[Ex - A scheme is determined by its functor of points]].

---

# Bridges

- **[[Thm - The Yoneda Embedding is Fully Faithful|Full faithfulness of the Yoneda embedding]]** — the immediate corollary. Setting $F = \mathcal{C}(B, -)$ gives $\mathrm{Nat}(\mathcal{C}(A, -), \mathcal{C}(B, -)) \cong \mathcal{C}(B, A)$, which says the Yoneda embedding induces a bijection on hom-sets — i.e. it is fully faithful. The two results together are jointly called "the Yoneda lemma" in common usage.

- **[[Def - Universal Element|Universal elements]]** — the conceptual repackaging. The lemma says a natural transformation $\mathcal{C}(A, -) \Rightarrow F$ is a single element $a \in F(A)$; that transformation is a natural *isomorphism* (a representation) exactly when $a$ is a universal element. So Yoneda is what reduces a representation to one element.

- **[[Thm - Uniqueness of Universal Objects|Uniqueness of universal objects]]** — proved using naturality of the Yoneda bijection. Because the universal element transports naturally, two representations are uniquely isomorphic; the contractible-groupoid conclusion is naturality made visible.

- **[[Def - Category of Elements|The category of elements]]** — the comma-category description $\int F \cong (\mathbf{y} \downarrow F)$ is a direct corollary: an object of $\int F$ is an element of $F$, which by Yoneda is a natural transformation from a representable into $F$.

---

# Unlocked by This

> [!tip] A Scheme is Determined by its Functor of Points *(from Algebraic Geometry)*
> The contravariant Yoneda lemma over $\mathbf{CRing}^{op}$ is the founding principle of the functor-of-points approach: **a scheme is completely determined by the sets of its $R$-points as $R$ ranges over all rings**. Morphisms of schemes are natural transformations of point-functors; **Spec** is the Yoneda embedding. See [[Ex - A scheme is determined by its functor of points]].

> [!tip] The Enriched and ∞-categorical Yoneda Lemma *(from Higher Category Theory)*
> Yoneda generalizes to **enriched categories** (hom-objects in a monoidal base $\mathcal{V}$, with the lemma stated via ends) and to **quasi-categories** / $\infty$-categories, where the $\infty$-categorical Yoneda lemma underwrites presentable $\infty$-categories, the theory of (co)limits, and Lurie's higher topos theory.

> [!tip] The Subobject Classifier *(from Topos Theory)*
> Reading the lemma for the contravariant power-set functor identifies its representing object $\Omega = \{0, 1\}$ and universal element $\{1\}$; in a general **topos** this becomes the **subobject classifier**, the internal object of truth values that makes a topos a model of higher-order logic.
