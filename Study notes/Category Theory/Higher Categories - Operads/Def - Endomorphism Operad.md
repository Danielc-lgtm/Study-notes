---
type: definition
subject: higher-categories
prereqs:
  - "Def - Operad"
  - "Def - Monoidal Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Fix a [[Def - Monoidal Category|symmetric monoidal category]] $(\mathcal{V}, \otimes, \mathbb{1})$ that is **closed**, meaning each functor $- \otimes Y$ has a right adjoint $[Y, -]$ supplying internal hom-objects $[Y, Z] \in \mathcal{V}$ with $\mathcal{V}(W \otimes Y, Z) \cong \mathcal{V}(W, [Y, Z])$. For an object $X \in \mathcal{V}$, write $X^{\otimes n} = X \otimes \dots \otimes X$ ($n$ factors, with $X^{\otimes 0} = \mathbb{1}$). The **endomorphism operad** of $X$ is the operad
$$\mathrm{End}_X(n) = [X^{\otimes n}, X] = \mathrm{Hom}(X^{\otimes n}, X),$$
the object of $n$-ary operations on $X$. In $\mathcal{V} = \mathbf{Set}$ this is the set of functions $X^n \to X$; in $\mathbf{Vect}_k$ the space of $k$-multilinear maps $X^{\times n} \to X$; in $\mathbf{Top}$ the space of continuous maps $X^n \to X$. The full notation registry is on [[Higher Categories — Operads and Multicategories]].

---

# Axiom Motivation

The endomorphism operad is not a definition you would invent by staring at axioms; it is the definition you are *forced* to write down the moment you ask "what could an [[Def - Operad|operad]] possibly act on?" An operad $P$ is a pile of abstract $n$-ary operations. To make those operations *do* something to an object $X$, each abstract operation $\theta \in P(n)$ must become a genuine $n$-ary operation on $X$, that is, a map $X^{\otimes n} \to X$. The collection of all genuine $n$-ary operations on $X$ is $\mathrm{Hom}(X^{\otimes n}, X)$, and the only thing that makes "$X$ is acted on by $P$" precise is a map $P(n) \to \mathrm{Hom}(X^{\otimes n}, X)$ for each $n$ that respects everything an operad respects. For that target to even be an operad — so that "respects everything" has content — $\mathrm{Hom}(X^{\otimes n}, X)$ must itself carry operad structure. The endomorphism operad is the verification that it does.

So the question is: what structure does the family $\mathrm{Hom}(X^{\otimes n}, X)$ naturally have, and is it an operad? It has a **unit**: the identity $X \to X$ is a $1$-ary operation, the obvious do-nothing. It has a **symmetric action**: given an $n$-ary operation $f : X^{\otimes n} \to X$ and a permutation $\sigma \in S_n$, precomposing with the symmetry that reorders the tensor factors gives a new $n$-ary operation $f \cdot \sigma$ — this is "the same operation with its arguments relabelled". And it has a **composition**: given $f : X^{\otimes k} \to X$ and operations $g_i : X^{\otimes n_i} \to X$, you can feed the $g_i$ into the slots of $f$ by forming $f \circ (g_1 \otimes \dots \otimes g_k) : X^{\otimes (n_1 + \dots + n_k)} \to X$. These three pieces are exactly the data of an operad.

Why do the axioms hold automatically? Because they are inherited from the ambient category. Associativity of operadic composition is *just associativity of composition of morphisms in $\mathcal{V}$* — nesting maps is associative because $\circ$ in any category is. The unit law holds because the identity is a two-sided unit for $\circ$. Equivariance holds because the symmetric monoidal structure of $\mathcal{V}$ has coherent symmetries (the braiding/symmetry is a natural family satisfying the hexagon), so reordering tensor factors interacts correctly with substitution. This is the entire point: the endomorphism operad does not impose new axioms; it *records* the operadic structure that any object's operations already possess. The operad axioms in [[Def - Operad|the abstract definition]] were reverse-engineered to be precisely "whatever $\mathrm{End}_X$ satisfies", which is why an algebra over $P$ can be defined as a map $P \to \mathrm{End}_X$.

A reader could invent this. Ask: what are the operations on $X$? Functions $X^n \to X$. Can I compose them? Yes, by substitution. Is there a do-nothing? Yes, the identity. Can I permute arguments? Yes. Do these satisfy the operad axioms? Yes, because composition of functions does. You have built the endomorphism operad — and in doing so you have discovered why operads have the axioms they do.

---

# The Definition

Let $(\mathcal{V}, \otimes, \mathbb{1})$ be a closed symmetric monoidal category and $X \in \mathcal{V}$. The **endomorphism operad** $\mathrm{End}_X$ is the operad in $\mathcal{V}$ with:

- **Operations.** $\mathrm{End}_X(n) = [X^{\otimes n}, X]$, the internal hom (in $\mathbf{Set}$: the hom-set $\mathrm{Hom}_{\mathcal{V}}(X^{\otimes n}, X)$).
- **Unit.** $\mathrm{id} = 1_X \in \mathrm{End}_X(1) = [X, X]$.
- **Symmetric action.** For $\sigma \in S_n$ and $f \in \mathrm{End}_X(n)$, $f \cdot \sigma = f \circ \sigma_X$, where $\sigma_X : X^{\otimes n} \to X^{\otimes n}$ is the symmetry permuting the tensor factors by $\sigma$.
- **Composition.** For $f \in \mathrm{End}_X(k)$ and $g_i \in \mathrm{End}_X(n_i)$,
$$\gamma(f; g_1, \dots, g_k) = f \circ (g_1 \otimes \dots \otimes g_k) : X^{\otimes (n_1 + \dots + n_k)} \longrightarrow X.$$

These data satisfy the operad axioms (associativity, unit, equivariance) automatically, inherited from associativity of $\circ$, the unit law for $1_X$, and the coherence of the symmetry in $\mathcal{V}$.

---

# Categorical / Structural Definition

The endomorphism operad is the **representing structure for "the operations on $X$"**, and it has a clean universal description through its relationship with algebras. For any operad $P$ in $\mathcal{V}$, the set of operad morphisms $P \to \mathrm{End}_X$ is in natural bijection with the set of $P$-algebra structures on $X$:
$$\mathrm{Operad}(\mathcal{V})\big(P, \mathrm{End}_X\big) \cong \{\,P\text{-algebra structures on } X\,\}.$$
This says $\mathrm{End}_X$ is the *terminal* recipient of any operad action on $X$: every way of making $X$ an algebra over any operad factors through $\mathrm{End}_X$, because $\mathrm{End}_X$ already contains *all* the operations $X$ admits. In multicategory language (an [[Def - Operad|operad]] is a one-object [[Def - Multicategory|multicategory]]), $\mathrm{End}_X$ is the endomorphism operad at the single colour $X$ inside the underlying multicategory of $\mathcal{V}$; for several objects $X_1, X_2, \dots$ the analogous construction is the full sub-multicategory on those colours, with $\mathcal{V}(X_{i_1}, \dots, X_{i_n}; X_j) = \mathrm{Hom}(X_{i_1} \otimes \dots \otimes X_{i_n}, X_j)$.

---

# Relate to Other Fields / Compression

The endomorphism operad is the operadic analogue of two familiar constructions, and seeing it as their common generalisation is the compression. First, it generalises the **symmetric group acting on a set as $\mathrm{Sym}(X)$**: just as a group action on $X$ is a homomorphism $G \to \mathrm{Sym}(X)$ into the group of *invertible unary* operations, an operad action on $X$ is a morphism $P \to \mathrm{End}_X$ into the operad of *all-arity* operations. Second, it generalises the **monoid of endomorphisms $\mathrm{End}(X) = \mathrm{Hom}(X,X)$**: that monoid is exactly the arity-$1$ part $\mathrm{End}_X(1)$, and the higher arities $\mathrm{End}_X(n)$ extend it from "unary self-maps composed in sequence" to "$n$-ary self-maps composed by substitution".

**True name:** the endomorphism operad is *the operad of all genuine operations on $X$, into which any abstract operation must land to act*. The official definition is $[X^{\otimes n}, X]$ with substitution; the operational name is "the universal target for operad actions on $X$". Whenever you want to say a structure acts on an object, the move is always the same: build the endomorphism operad of the object, and exhibit a morphism into it. This is the operadic instance of the universal pattern *to act on $X$ is to map into the gadget of all actions on $X$* — the same pattern as $G \to \mathrm{Sym}(X)$ for group actions and $T \to \mathrm{End}(X)$-style structure maps for monad algebras.

---

# Examples / Corollaries

**Is an instance — $\mathrm{End}_X$ for a set $X$.** $\mathrm{End}_X(n) = \{$functions $X^n \to X\}$. A monoid structure on $X$ is a morphism $\mathrm{Assoc} \to \mathrm{End}_X$, which picks out a binary function $m : X^2 \to X$ (the image of the generating binary operation) that is associative and unital — that is, it picks out an associative unital multiplication, recovering exactly the data of a monoid. So "$X$ is a monoid" literally means "there is an operad map from the associative operad into $\mathrm{End}_X$".

**Is an instance — $\mathrm{End}_V$ for a vector space $V$.** $\mathrm{End}_V(n) = \{$multilinear maps $V^{\times n} \to V\}$. An associative algebra structure on $V$ is a map $\mathrm{Assoc} \to \mathrm{End}_V$; a Lie algebra structure is a map $\mathrm{Lie} \to \mathrm{End}_V$, whose value on the generating bracket is a bilinear $[-,-]$ satisfying antisymmetry and Jacobi because the operad relations force them. The endomorphism operad is where "the bracket satisfies Jacobi" becomes a statement about an operad map respecting relations rather than a hand-checked identity.

**Is an instance — $\mathrm{End}_X$ for a topological space $X$, and the loop space.** $\mathrm{End}_X(n)$ is the space of continuous maps $X^n \to X$. For $X = \Omega Y$ a loop space, concatenation of loops gives a point of $\mathrm{End}_X(2)$ that is associative *only up to homotopy*; the higher endomorphism spaces record the higher homotopies, and the resulting map from the [[Thm - May's Recognition Principle|little intervals operad]] $E_1$ into $\mathrm{End}_{\Omega Y}$ is what makes $\Omega Y$ an $E_1$-algebra. This is the example that motivates topological operads in the first place.

**Is NOT an instance — "the operations on $X$" without the symmetric structure of $\mathcal{V}$.** If $\mathcal{V}$ is merely monoidal (not symmetric), there is no coherent way to permute tensor factors, so $f \cdot \sigma$ is undefined and $\mathrm{End}_X$ is at best a *non-symmetric* operad. Trying to equip it with an $S_n$-action anyway fails equivariance, because the braiding needed to commute substitution past a permutation does not exist. This pins down why symmetric operads live over symmetric monoidal categories: the endomorphism operad's $S_n$-action *is* the ambient symmetry.

**Calibration check.** Verify that (i) $\mathrm{End}_X(1) = \mathrm{Hom}(X,X)$ is the endomorphism monoid of $X$, with operadic composition restricting to ordinary composition; (ii) for $X$ a set, $\mathrm{End}_X(0) = \mathrm{Hom}(\{*\}, X) = X$ itself, the "nullary operations" being the elements of $X$ (so a unit element of a monoid is a nullary operation); and (iii) an operad morphism $P \to \mathrm{End}_X$ is the same data as a family of maps $P(n) \times X^n \to X$ compatible with composition — i.e. a [[Def - Algebra for an Operad|P-algebra structure]]. If these are clear, the endomorphism operad has done its job.

---

# Unlocked by This

> [!tip] Algebra for an Operad *(from this topic)*
> The endomorphism operad is exactly the device that makes [[Def - Algebra for an Operad|"algebra over an operad"]] definable: a $P$-algebra is an object $X$ with an operad morphism $P \to \mathrm{End}_X$. Without $\mathrm{End}_X$ there is no codomain for the action map, so this definition is logically prior to the entire theory of operadic algebras.

> [!tip] Coendomorphism Operad and Coalgebras *(from Operadic Homotopy Theory)*
> Dualising — using $[X, X^{\otimes n}]$ in place of $[X^{\otimes n}, X]$ — gives the **coendomorphism cooperad**, whose coalgebras are the operadic duals of algebras (for instance $C_\infty$-coalgebras). The same universal-target pattern runs in the dual direction.
