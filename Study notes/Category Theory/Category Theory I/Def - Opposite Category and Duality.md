---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
tags: [category-theory, foundations]
---

# Notation

For a [[Def - Category|category]] $\mathcal{C}$, its opposite is written $\mathcal{C}^{\mathrm{op}}$. For a morphism $f : A \to B$ in $\mathcal{C}$, the corresponding morphism in $\mathcal{C}^{\mathrm{op}}$ is written $f^{\mathrm{op}} : B \to A$ (same underlying arrow, reversed reading). Composition in $\mathcal{C}^{\mathrm{op}}$ is denoted $\circ^{\mathrm{op}}$ when contrast is needed. This is a compound page: it defines two interlocking notions — the **opposite category** $\mathcal{C}^{\mathrm{op}}$ (a construction) and **duality** (the meta-principle that construction supports) — because the construction exists in order to make the principle precise. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Axiom Motivation

Look at the three notions on [[Def - Isomorphism, Monomorphism, Epimorphism]]. Monomorphism is left-cancellability; epimorphism is right-cancellability. They are not two unrelated concepts that happen to resemble each other — they are *literally the same definition with the direction of composition reversed*. The same mirror relates many pairs: products and coproducts, kernels and cokernels, initial and terminal objects, limits and colimits. Every time, the second member of the pair is obtained from the first by "reverse all the arrows". This is too systematic to be coincidence, and the right response is to give the mirror an official mathematical existence.

That official existence is the opposite category. The idea is forced: if reversing arrows is a meaningful operation on definitions, it should be a meaningful operation on the *category itself*. So define $\mathcal{C}^{\mathrm{op}}$ to have the same objects as $\mathcal{C}$ but with every arrow turned around — a morphism $A \to B$ in $\mathcal{C}^{\mathrm{op}}$ is a morphism $B \to A$ in $\mathcal{C}$. The only nontrivial decision is how composition must behave, and it is dictated by consistency. In $\mathcal{C}$ a composite $A \xrightarrow{f} B \xrightarrow{g} C$ exists; reversing gives $C \to B \to A$, so in $\mathcal{C}^{\mathrm{op}}$ the composable pair is $(f^{\mathrm{op}} : B \to A,\ g^{\mathrm{op}} : C \to B)$ with composite $C \to A$. That composite, read back in $\mathcal{C}$, must be $g \circ f : A \to C$. Hence the **reversal-of-composition law**:
$$f^{\mathrm{op}} \circ^{\mathrm{op}} g^{\mathrm{op}} = (g \circ f)^{\mathrm{op}}.$$
The order of composition flips — this is exactly the rule $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$ for inverses, and the rule $(AB)^T = B^T A^T$ for matrix transpose, and the rule for reversing a path. **Drop the flip** (i.e. try to set $f^{\mathrm{op}} \circ^{\mathrm{op}} g^{\mathrm{op}} = (f \circ g)^{\mathrm{op}})$ and you fail to land in the right hom-set: the domains and codomains will not match, so the construction is not even a category. The flip is not a convention; it is forced by the typing.

Once $\mathcal{C}^{\mathrm{op}}$ is a category, two facts make it a *principle* rather than a curiosity. First, the construction is an involution: $(\mathcal{C}^{\mathrm{op}})^{\mathrm{op}} = \mathcal{C}$, because reversing twice restores every arrow. Second, every categorical statement about $\mathcal{C}^{\mathrm{op}}$ is, after un-reversing, a statement about $\mathcal{C}$ with all arrows reversed. Together these say: **proving a theorem for all categories automatically proves its arrow-reversed "dual" for all categories**, because the dual statement for $\mathcal{C}$ is the original statement for $\mathcal{C}^{\mathrm{op}}$, which is a category like any other. That is the [[Thm - The Duality Principle|duality principle]], and the opposite category is the machine that makes it run.

---

# The Definition

Let $\mathcal{C}$ be a [[Def - Category|category]]. Its **opposite** (or **dual**) category $\mathcal{C}^{\mathrm{op}}$ is defined by:

- $\mathrm{ob}(\mathcal{C}^{\mathrm{op}}) = \mathrm{ob}(\mathcal{C})$ — the same objects;
- $\mathcal{C}^{\mathrm{op}}(A, B) = \mathcal{C}(B, A)$ — a morphism $A \to B$ in $\mathcal{C}^{\mathrm{op}}$ is a morphism $B \to A$ in $\mathcal{C}$;
- the identity $1_A$ in $\mathcal{C}^{\mathrm{op}}$ is the identity $1_A$ of $\mathcal{C}$;
- composition is the reversal of composition in $\mathcal{C}$:
$$g \circ^{\mathrm{op}} f := f \circ g \qquad \text{(where } f : A \to B,\ g : B \to C \text{ in } \mathcal{C}^{\mathrm{op}}\text{)}.$$

The category axioms for $\mathcal{C}^{\mathrm{op}}$ follow immediately from those of $\mathcal{C}$. One has $(\mathcal{C}^{\mathrm{op}})^{\mathrm{op}} = \mathcal{C}$.

**Duality.** Every concept, statement, or construction $S$ phrased in the language of categories (objects, morphisms, domains, codomains, composition, identities) has a **dual** $S^{\mathrm{op}}$, obtained by reversing every morphism, swapping every "domain" with "codomain", and reversing the order of every composite. A property holds for an object/morphism $X$ in $\mathcal{C}$ if and only if the dual property holds for $X$ in $\mathcal{C}^{\mathrm{op}}$.

---

# Relate to Other Fields / Compression

The opposite category is the categorical incarnation of the universal "reverse the arrows" symmetry that appears all over mathematics. The transpose of a [[Def - Linear Map|linear map]], $T^T : W^* \to V^*$, reverses the direction of $T : V \to W$ and reverses composition: $(ST)^T = T^T S^T$. The [[Def - Dual Map|dual map]] is the $\mathbf{Vect}_k^{\mathrm{op}}$ shadow of the original. The inverse in a [[Def - Group|group]] reverses products: $(gh)^{-1} = h^{-1}g^{-1}$, which is exactly the opposite-category law in the one-object groupoid $\mathbf{B}G$. Reversing a path, $\bar\gamma$, with $\overline{\gamma_1 \cdot \gamma_2} = \bar\gamma_2 \cdot \bar\gamma_1$, is the same flip in the [[Def - Groupoid|fundamental groupoid]].

**True name:** *the formal "reverse all arrows" operation, with composition order flipped, that is its own inverse.* Carrying this name has an immediate payoff: every theorem you prove buys a second theorem for free, and every definition you make comes with a dual you did not have to invent. The mental move is "what is this statement saying about $\mathcal{C}^{\mathrm{op}}$?" — answering it reveals the dual concept.

---

# Examples / Corollaries

**Mono and epi are dual.** $f$ is a [[Def - Isomorphism, Monomorphism, Epimorphism|monomorphism]] in $\mathcal{C}$ if and only if $f^{\mathrm{op}}$ is an epimorphism in $\mathcal{C}^{\mathrm{op}}$, and vice versa. Left-cancellability in $\mathcal{C}$ becomes right-cancellability in $\mathcal{C}^{\mathrm{op}}$ verbatim. This is the prototypical dual pair and the reason the two notions look so alike.

**The opposite of a poset.** A [[Def - Topological Space|partially ordered set]] $(P, \leq)$ viewed as a category (one arrow $a \to b$ iff $a \leq b$) has opposite $(P, \geq)$: reversing the unique arrow $a \to b$ gives a unique arrow $b \to a$, i.e. $b \leq a$. So $P^{\mathrm{op}}$ is the same set with the order *reversed*. Greatest lower bounds (meets) in $P$ are least upper bounds (joins) in $P^{\mathrm{op}}$ — the duality between infima and suprema is opposite-category duality.

**The opposite of a group is isomorphic to the group.** For a [[Def - Group|group]] $G$, the opposite of $\mathbf{B}G$ is $\mathbf{B}(G^{\mathrm{op}})$, where $G^{\mathrm{op}}$ has multiplication $g \ast h = hg$. But $G^{\mathrm{op}} \cong G$ via $g \mapsto g^{-1}$: this map sends $gh$ to $(gh)^{-1} = h^{-1}g^{-1}$, which is $g^{-1} \ast h^{-1}$ in $G^{\mathrm{op}}$. So a group is (non-canonically) isomorphic to its own opposite — inversion is the witnessing anti-automorphism. This is special to groups; it is the invertibility that makes $g \mapsto g^{-1}$ available.

**Is NOT self-opposite — $\mathbf{Set}$.** The category of sets is *not* isomorphic, nor even [[Def - Equivalence of Categories|equivalent]], to its opposite. The empty set $\emptyset$ is initial (one map out of it to each set) while the singleton is terminal (one map into it from each set), and $\mathbf{Set}$ has no object that is initial *and* terminal — but an equivalence $\mathbf{Set} \simeq \mathbf{Set}^{\mathrm{op}}$ would have to swap initial and terminal objects, forcing such a symmetry. So $\mathbf{Set} \not\simeq \mathbf{Set}^{\mathrm{op}}$. The opposite of $\mathbf{Set}$ is genuinely different — it is equivalent to the category of complete atomic Boolean algebras. **Self-opposite is the exception, not the rule.**

**Calibration check.** Verify $(\mathcal{C}^{\mathrm{op}})^{\mathrm{op}} = \mathcal{C}$ directly from the definition. Verify that a [[Def - Functor|functor]] $\mathcal{C} \to \mathcal{D}$ is the same data as a functor $\mathcal{C}^{\mathrm{op}} \to \mathcal{D}^{\mathrm{op}}$, but a *contravariant* functor $\mathcal{C} \to \mathcal{D}$ is a functor $\mathcal{C}^{\mathrm{op}} \to \mathcal{D}$. Confirm you can state the dual of "every object has a morphism to a fixed object $T$" (answer: "every object receives a morphism from a fixed object $I$").

---

# Unlocked by This

> [!tip] The Duality Principle *(from this chapter)*
> The opposite category turns the informal "reverse the arrows" into the rigorous [[Thm - The Duality Principle|duality principle]]: any theorem provable for all categories has a dual, provable for free. This halves the labour of the entire subject — product/coproduct, limit/colimit, mono/epi, initial/terminal are each one theorem proved twice.

> [!tip] Presheaves and CRing^op ≃ Affine Schemes *(from Algebraic Geometry)*
> A **presheaf** on $\mathcal{C}$ is a functor $\mathcal{C}^{\mathrm{op}} \to \mathbf{Set}$ — the opposite category is built into the definition. In algebraic geometry the central duality is $\mathbf{CRing}^{\mathrm{op}} \simeq$ **affine schemes**: a commutative ring is the ring of functions on a space, and a ring map runs *backward* against the geometry. The arrow-reversal is exactly $(-)^{\mathrm{op}}$, made precise by the contravariant functor **Spec** (see [[Def - Functor]]).
