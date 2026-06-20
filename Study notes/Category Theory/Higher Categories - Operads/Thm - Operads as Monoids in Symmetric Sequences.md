---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Operad"
  - "Def - Monoid in a Monoidal Category"
  - "Def - Monoidal Category"
  - "Def - Monad and Comonad"
tags: [category-theory, higher-categories, foundations]
---

# Notation

A **symmetric sequence** (or **$S$-module**, or **species**) $P$ in a [[Def - Monoidal Category|symmetric monoidal category]] $(\mathcal{V}, \otimes, \mathbb{1})$ is a sequence of objects $P(n) \in \mathcal{V}$ for $n \geq 0$, each carrying a right $S_n$-action. Equivalently it is a functor $\mathbb{B} \to \mathcal{V}$ from the groupoid $\mathbb{B}$ of finite sets and bijections. Symmetric sequences and their ($S_n$-equivariant, arity-wise) morphisms form a category $\mathrm{SymSeq}(\mathcal{V})$. The **composition product** of two symmetric sequences is the symmetric sequence
$$(P \circ Q)(n) = \coprod_{k \geq 0} \ P(k) \otimes_{S_k} \Big( \coprod_{\substack{f : \{1,\dots,n\} \twoheadrightarrow \{1,\dots,k\}}} \bigotimes_{i=1}^{k} Q(|f^{-1}(i)|) \Big),$$
or, packaged with induction, $(P \circ Q)(n) = \coprod_{k} P(k) \otimes_{S_k} \big( \coprod_{n_1 + \dots + n_k = n} \mathrm{Ind}_{S_{n_1} \times \dots \times S_{n_k}}^{S_n}\, Q(n_1) \otimes \dots \otimes Q(n_k) \big)$. Its two-sided unit is the symmetric sequence $I$ with $I(1) = \mathbb{1}$ and $I(n) = \varnothing$ (initial object) for $n \neq 1$. The full notation registry is on [[Higher Categories — Operads and Multicategories]].

---

# Statement

> **Theorem (operads are monoids in symmetric sequences).** Let $(\mathcal{V}, \otimes, \mathbb{1})$ be a symmetric monoidal category with countable coproducts over which $\otimes$ distributes. Then $(\mathrm{SymSeq}(\mathcal{V}), \circ, I)$ is a monoidal category, and an [[Def - Operad|operad]] in $\mathcal{V}$ is exactly a [[Def - Monoid in a Monoidal Category|monoid]] in it. That is, the category of operads in $\mathcal{V}$ is isomorphic to the category of monoids $(P, \mu : P \circ P \to P, \eta : I \to P)$ in $(\mathrm{SymSeq}(\mathcal{V}), \circ, I)$, with the monoid multiplication $\mu$ corresponding to the operadic composition $\gamma$ and the monoid unit $\eta$ to the operadic unit $\mathrm{id} \in P(1)$.

> **Corollary (operads are monads).** Evaluation of a symmetric sequence on an object, $P \mapsto T_P$ with $T_P(X) = \coprod_n P(n) \otimes_{S_n} X^{\otimes n}$, is a strong monoidal functor from $(\mathrm{SymSeq}(\mathcal{V}), \circ, I)$ to $(\mathrm{End}(\mathcal{V}), \circ, \mathrm{Id})$, so every operad $P$ yields a [[Def - Monad and Comonad|monad]] $T_P$ whose algebras are the $P$-algebras.

---

# Motivation

Before this theorem, an operad looks like an ungainly pile of axioms: a sequence of sets, a symmetric action, a composition $\gamma$ with three different-looking coherence laws, units. One could memorise it, but it would feel ad hoc — why *these* axioms? The theorem dissolves the apparent arbitrariness. It says that an operad is not a new kind of object at all; it is a **monoid**, the most familiar algebraic gadget there is, living in a slightly unusual monoidal category. The associativity of $\gamma$ is just the associativity of monoid multiplication; the unit law is just the monoid unit law; the equivariance is bookkeeping that has been absorbed into the definition of the composition product $\circ$. Everything mysterious about the operad axioms becomes "it is a monoid, and you already know what those are".

This is valuable for the same reason the analogous statements about rings and monads are valuable. Recognising that a ring is a [[Def - Monoid in a Monoidal Category|monoid in Ab]], and a [[Def - Monad and Comonad|monad]] is a monoid in endofunctors, immediately transports the entire vocabulary of monoid theory — modules, free monoids, the bar construction, ideals — to those settings. The same happens here: free operads become free monoids for $\circ$, $P$-algebras become $P$-modules, the bar resolution of an operad becomes the bar construction of a monoid, and Koszul duality becomes a statement about Koszul monoids. The theorem is the gateway through which all of monoidal algebra flows into operad theory.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's literal hypothesis is "$P$ is an operad", but in practice you invoke it whenever you have, or want, a *graded composable structure with substitution*, even when "operad" is not said aloud.

The first disguised source is **a sequence of operations with a substitution law that you suspect is associative**. If you have built sets $P(n)$ of "things of arity $n$" — wiring diagrams, trees, configurations, terms — with a way to plug them into each other, the question "is this an operad?" is often hard to check axiom-by-axiom but easy once rephrased: is $(P, \text{substitution})$ a monoid for $\circ$? You only need a multiplication $P \circ P \to P$ and a unit, plus associativity, and the equivariance is free because $\circ$ already quotients by the $S_n$-actions. *Example problem:* show that the sequence $\mathrm{Tree}(n)$ of planar rooted trees with $n$ leaves, under grafting, is a non-symmetric operad — phrased as "grafting is an associative monoid product on the sequence of trees".

The second disguised source is **a monad you want to recognise as polynomial/analytic**. A monad $T$ on $\mathbf{Set}$ that happens to have the form $T(X) = \coprod_n P(n) \otimes_{S_n} X^n$ for some symmetric sequence $P$ is automatically $T_P$ for an operad $P$, because the corollary's functor $P \mapsto T_P$ is monoidal and (suitably restricted) fully faithful. So "this monad is a sum of arity-graded pieces" is a source for "this monad comes from an operad", which then gives you the entire operadic toolkit on its algebras. *Example problem:* recognise the free-monoid monad $X \mapsto \coprod_n X^n$ as $T_{\mathrm{Assoc}^{\mathrm{ns}}}$, hence its algebras as monoids, via the non-symmetric associative operad.

The third disguised source is **a monoidal category you can present as symmetric sequences**. Many naturally occurring monoidal structures — the substitution/plethysm product on species in combinatorics, the composition of formal power series, the composition of polynomial functors — *are* the composition product $\circ$ in disguise. Whenever you recognise your monoidal product as "substitute one graded gadget into another", the monoids for it are operads. *Example problem:* identify exponential generating functions with species and the plethystic substitution $f[g]$ with the composition product, so that "operad" becomes "monoid under plethysm" and the dimension sequence of an operad becomes a fixed point of a plethystic equation.

**Targets (Output Amplification)**

The conclusion "an operad is a monoid in $(\mathrm{SymSeq}, \circ, I)$" combines with standard monoid technology to produce results that would be laborious to set up directly.

Combine the conclusion with **the existence of free monoids**. In any monoidal category with enough colimits where the tensor preserves them, the free monoid on an object exists and is computed by a sum of tensor powers; transported through the theorem, this gives the **[[Thm - The Free Operad|free operad]]** on a symmetric sequence $E$ as $\coprod_n E^{\circ n}$, which unwinds to the operad of $E$-labelled trees. The nonobvious payoff is that you get the tree description of the free operad *for free* from a general monoidal fact, rather than constructing trees by hand and verifying the universal property.

Combine the conclusion with **the bar construction for monoids**. A monoid in a monoidal category has a two-sided bar construction $B(M, M, M)$ and, for an augmented monoid, a bar resolution; applied to an operad these give the **operadic bar/cobar adjunction** and the homotopy-coherent resolutions $A_\infty$, $E_\infty$ as cofibrant replacements. The nonobvious result is that "resolve the operad to make its algebras homotopy-invariant" is literally "resolve the monoid", so the machinery of homotopical algebra for monoids applies verbatim.

Combine the conclusion with **the notion of a module over a monoid**. A left module over the monoid $P$ in $\mathrm{SymSeq}$ — an object $M$ with $P \circ M \to M$ — specialises, when $M$ is concentrated appropriately, to a **$P$-algebra**; right modules and bimodules give $P$-(co)operads and the theory of operadic modules used in factorization homology. The nonobvious result is that "$P$-algebra" and "left $P$-module" are the same notion, which is what lets you import module-theoretic constructions (tensor products of modules, induced and restricted algebras along operad maps) into the study of algebras.

---

# Why Is It True

The whole theorem is the assertion that the composition product $\circ$ is *built to make substitution associative*, so that the operad's $\gamma$ becomes an associative monoid product by fiat. To see why, look at what $P \circ Q$ is. An element of $(P \circ Q)(n)$ is the data of: an operation $\theta \in P(k)$ at the top, and $k$ operations $\varphi_1, \dots, \varphi_k$ from $Q$ filling its $k$ inputs, with their $n$ inputs distributed among the $\varphi_i$ — all this *quotiented* by the $S_k$-action permuting the slots of $\theta$ and the matching reindexing of the $\varphi_i$, and *induced up* so the symmetric group $S_n$ acts on the total inputs. In one phrase: **$P \circ Q$ is "a $P$-operation with its slots filled by $Q$-operations", taken up to the symmetric relabelling that the equivariance axiom would impose.**

That is exactly the raw material of operadic composition. The operadic $\gamma$ is precisely a map $P \circ P \to P$: take a $P$-operation with its slots filled by $P$-operations, and graft to get a single $P$-operation. The unit $\mathrm{id} \in P(1)$ is precisely a map $I \to P$, since $I$ is concentrated in arity $1$. So the *data* of an operad — $\gamma$ and $\mathrm{id}$ — is literally the data of a monoid $(\mu, \eta)$ for $\circ$.

Now the axioms match because $\circ$ was engineered to make them match.

> **The composition product is the associativity bookkeeping of substitution, promoted to a monoidal product; once that promotion is made, "operad" and "monoid" are the same word.**

Associativity of $\gamma$ — the two ways of grafting a three-layer tree — is exactly the equation $\mu \circ (\mu \circ_{\mathrm{id}}) = \mu \circ (\mathrm{id} \circ \mu)$ that says $\mu$ is associative, because the two sides of the operad associativity law are the two sides of the monoid associativity law after you trace through how $\circ$ groups the layers. The unit law is the monoid unit law. And equivariance, which looked like a third independent axiom, has *vanished* — it is no longer an axiom at all, because $(P \circ Q)(n)$ already has the $S_n$-action and the quotients $\otimes_{S_k}$ and inductions $\mathrm{Ind}$ are precisely what enforce the block-permutation compatibility. The composition product absorbs equivariance into the ambient structure, leaving only the two monoid axioms. That absorption is the real content: the cleverness is all in the definition of $\circ$, and the theorem is the observation that, once you have it, nothing is left to check.

The corollary is then transparent. Evaluating a symmetric sequence on an object, $P \mapsto T_P$, sends $\circ$ to composition of endofunctors — because $T_{P \circ Q} = T_P \circ T_Q$, substituting operations being the same as composing the functors they induce — and sends $I$ to the identity functor. A strong monoidal functor sends monoids to monoids, so an operad (monoid for $\circ$) becomes a monad (monoid for functor composition).

---

# What Makes This Hard

The single hard thing is the **definition of the composition product** $\circ$ and seeing that it is associative and unital — that $(\mathrm{SymSeq}, \circ, I)$ is genuinely a monoidal category. The associativity isomorphism $P \circ (Q \circ R) \cong (P \circ Q) \circ R$ requires carefully matching the $S_n$-quotients and inductions on both sides, and this is where most people stall: the formula for $\circ$ is intimidating, and the bookkeeping of which symmetric groups act where is unforgiving. The common error is to define $\circ$ *without* the $\otimes_{S_k}$ coinvariants and $\mathrm{Ind}$, getting a non-symmetric (plain) version; that version is monoidal and its monoids are non-symmetric operads, but it does *not* encode equivariance, so one wrongly concludes the symmetric and non-symmetric stories are the same. The second subtlety is that $\circ$ is **not symmetric** as a monoidal product (substituting $Q$ into $P$ differs from substituting $P$ into $Q$), so one must not expect a braiding — operads are monoids in a merely monoidal, not symmetric monoidal, category.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Define $\circ$ on symmetric sequences as "$P$-operations with slots filled by $Q$-operations, up to symmetry"; check $(\mathrm{SymSeq}, \circ, I)$ is monoidal; then observe that a monoid structure $(\mu, \eta)$ for $\circ$ unpacks exactly to operad data $(\gamma, \mathrm{id})$, with the monoid axioms matching the operad axioms term for term and equivariance already built into $\circ$.

**Subgoal decomposition:**

1. **Define the composition product and the unit $I$.** Give the formula for $(P \circ Q)(n)$ with its $S_n$-action and set $I(1) = \mathbb{1}$, $I(n) = \varnothing$ otherwise.
   - *Hint:* Think "rooted trees of height $2$": a top node from $P$, leaves filled by nodes from $Q$, all input-labellings identified up to the symmetric relabelling.
   - *Why needed:* The product and unit are the monoidal structure whose monoids will be operads; everything else is checking and matching.

2. **Show $(\mathrm{SymSeq}, \circ, I)$ is a monoidal category.** Construct the associator $P \circ (Q \circ R) \cong (P \circ Q) \circ R$ and the unitors $I \circ P \cong P \cong P \circ I$, and verify pentagon and triangle.
   - *Hint:* Both sides of associativity describe height-$3$ trees; the iso re-brackets the levels. The unitors use $I(1) = \mathbb{1}$ to insert a do-nothing node.
   - *Why needed:* Without a monoidal category there is no notion of "monoid in it".

3. **Unpack monoid data into operad data.** Show a monoid multiplication $\mu : P \circ P \to P$ is exactly an operadic composition $\gamma$, and a unit $\eta : I \to P$ is exactly an element $\mathrm{id} \in P(1)$.
   - *Hint:* By the definition of $\circ$, a map out of $P \circ P$ is the same as a compatible family $P(k) \otimes_{S_k} (\dots) \to P(n)$, which is $\gamma$. A map out of $I$ picks out the arity-$1$ component.
   - *Why needed:* This is the bijection on *data*; the axioms come next.

4. **Match the axioms.** Show monoid associativity $\mu(\mu \circ \mathrm{id}) = \mu(\mathrm{id} \circ \mu)$ is operad associativity of $\gamma$, and monoid unitality is the operad unit laws; note equivariance is automatic.
   - *Hint:* Apply both monoid-associativity composites to a height-$3$ tree and read off the two grafting orders of the operad axiom.
   - *Why needed:* Establishes the isomorphism of categories, not just a bijection of objects.

5. **Prove the corollary.** Show $P \mapsto T_P$ is strong monoidal, sending $\circ$ to $\circ$ (functor composition) and $I$ to $\mathrm{Id}$, hence operads to monads.
   - *Hint:* Verify $T_{P \circ Q} \cong T_P \circ T_Q$ by substituting the formula for $T_Q(X)$ into $T_P$ and using distributivity of $\otimes$ over the coproducts.
   - *Why needed:* This is the operad-to-monad bridge and the link to [[Def - Algebra for an Operad|operadic algebras]] as monad algebras.

---

# Lemma Decomposition

> [!note]- Lemma 1: The composition product is associative
> **Statement:** There is a natural isomorphism $P \circ (Q \circ R) \cong (P \circ Q) \circ R$ of symmetric sequences, satisfying the pentagon axiom.
>
> **Hint:** Both sides classify the same combinatorial object — a $3$-level labelled tree (a $P$-node, $Q$-nodes on its slots, $R$-nodes on theirs) modulo symmetric relabelling — so write each side out as a coproduct over surjections / ordered partitions and exhibit the bijection that re-associates the partition.
>
> **Why needed:** Associativity of $\circ$ is the heart of "$\mathrm{SymSeq}$ is monoidal"; without it there is no monoidal category to host operads.
>
> > [!note]- Full proof
> > Expand $(Q \circ R)(m) = \coprod_j Q(j) \otimes_{S_j} \mathrm{Ind}\big(\bigotimes R(m_i)\big)$ over $m_1 + \dots + m_j = m$, and substitute into $P \circ (Q \circ R)$. The result is a coproduct indexed by: $k$ (arity of the $P$-node), then for each of the $k$ slots a number $j_i$ (arity of the $Q$-node there), then for each of those an arity of an $R$-node, with $\otimes_{S_k}$, $\otimes_{S_{j_i}}$, and inductions interleaved. Doing the same expansion on $(P \circ Q) \circ R$ produces a coproduct over the same indexing data (a $P$-node with $\sum j_i$ ultimate slots filled by $R$-nodes, the $Q$-layer recording how the slots group), with the coinvariants and inductions in the other grouping. The canonical map identifying "group by $P$-then-$(Q,R)$" with "group by $(P,Q)$-then-$R$" is a bijection on index sets and an isomorphism on the tensor factors because $\mathrm{Ind}$ is associative ($\mathrm{Ind}_{H}^{G}\mathrm{Ind}_{K}^{H} = \mathrm{Ind}_K^G$) and coinvariants commute with the coproducts (as $\otimes$ distributes over them). The pentagon is the statement that the two ways of re-associating a $4$-level tree agree, which holds because both are induced by the associativity of ordered partition refinement.

> [!note]- Lemma 2: $I$ is a two-sided unit
> **Statement:** For the symmetric sequence $I$ with $I(1) = \mathbb{1}$ and $I(n) = \varnothing$ otherwise, there are natural isomorphisms $I \circ P \cong P$ and $P \circ I \cong P$ satisfying the triangle axiom.
>
> **Hint:** Substituting $I$ into the slots ($P \circ I$) forces each slot's filler to be the arity-$1$ unit, recovering $P$; substituting $P$ into the single slot of $I$ ($I \circ P$) recovers $P$ because $I$ has one node of arity $1$.
>
> **Why needed:** A monoidal product needs a unit; the operadic $\mathrm{id} \in P(1)$ will be $\eta : I \to P$, so $I$ must be the unit.
>
> > [!note]- Full proof
> > For $P \circ I$: in the formula, the inner $Q = I$ contributes $\bigotimes_i I(n_i)$, which is $\varnothing$ unless every $n_i = 1$, in which case it is $\mathbb{1}^{\otimes k} \cong \mathbb{1}$. The surviving term is $k = n$, all $n_i = 1$, giving $P(n) \otimes_{S_n} \mathrm{Ind}_{S_1^{\times n}}^{S_n}(\mathbb{1}) \cong P(n) \otimes_{S_n} \mathbb{1}[S_n] \cong P(n)$, naturally and $S_n$-equivariantly. For $I \circ P$: the outer $P' = I$ contributes $I(k)$, nonzero only at $k = 1$, where $I(1) = \mathbb{1}$ and there is a single slot; the term is $\mathbb{1} \otimes_{S_1} P(n) \cong P(n)$. Both isomorphisms are natural, and the triangle axiom holds because both unitors arise from the same identification of an arity-$1$ unit node.

> [!note]- Lemma 3: Monoid data equals operad data, and the axioms match
> **Statement:** A monoid $(\mu : P \circ P \to P, \eta : I \to P)$ is the same as an operad structure $(\gamma, \mathrm{id})$ on the underlying symmetric sequence $P$, with monoid associativity $\Leftrightarrow$ operad associativity and monoid unitality $\Leftrightarrow$ operad unit laws.
>
> **Hint:** Use the universal description of maps out of $\circ$: a morphism $P \circ P \to P$ is precisely a family $P(k) \otimes_{S_k}(\dots) \to P(n)$, i.e. the operadic $\gamma$. Then evaluate the monoid associativity square on a $3$-level tree.
>
> **Why needed:** This is the actual content of the theorem — the isomorphism of categories operads $\cong$ monoids.
>
> > [!note]- Full proof
> > By the construction of $\circ$, $\mathrm{SymSeq}(P \circ P, P)$ is naturally isomorphic to the set of $S_n$-equivariant families $\big\{P(k) \otimes_{S_k} \mathrm{Ind}(P(n_1) \otimes \dots \otimes P(n_k)) \to P(n)\big\}$ — equivalently, families $P(k) \otimes P(n_1) \otimes \dots \otimes P(n_k) \to P(\sum n_i)$ satisfying equivariance (the equivariance is forced because the map must descend through the $\otimes_{S_k}$ coinvariants and the induction). That family is exactly the operadic composition $\gamma$. Likewise $\mathrm{SymSeq}(I, P) \cong P(1)$ picks out $\mathrm{id}$. Monoid associativity $\mu \circ (\mu \circ \mathrm{id}_P) = \mu \circ (\mathrm{id}_P \circ \mu) : P \circ P \circ P \to P$, evaluated on the component indexed by a $3$-level tree, is precisely the equation $\gamma(\gamma(\theta; \varphi_\bullet); \psi_\bullet) = \gamma(\theta; \gamma(\varphi_i; \psi_\bullet))$ — operad associativity. Monoid unitality $\mu \circ (\eta \circ \mathrm{id}) = \mathrm{id}_P = \mu \circ (\mathrm{id} \circ \eta)$ becomes $\gamma(\mathrm{id}; \theta) = \theta = \gamma(\theta; \mathrm{id}, \dots, \mathrm{id})$. The correspondence is a bijection on morphisms (operad maps $=$ monoid maps), giving an isomorphism of categories.

> [!note]- Lemma 4: $T_{P \circ Q} \cong T_P \circ T_Q$
> **Statement:** The functor $P \mapsto T_P$, $T_P(X) = \coprod_n P(n) \otimes_{S_n} X^{\otimes n}$, satisfies $T_{P \circ Q} \cong T_P \circ T_Q$ and $T_I \cong \mathrm{Id}$ naturally; hence it is strong monoidal from $(\mathrm{SymSeq}, \circ, I)$ to $(\mathrm{End}(\mathcal{V}), \circ, \mathrm{Id})$.
>
> **Hint:** Compute $T_P(T_Q(X))$ by substituting $T_Q(X) = \coprod_m Q(m) \otimes_{S_m} X^{\otimes m}$ into $T_P$ and expanding the tensor powers using distributivity.
>
> **Why needed:** It is the corollary — the operad-to-monad bridge — and shows $P$-algebras are $T_P$-algebras.
>
> > [!note]- Full proof
> > $T_P(T_Q(X)) = \coprod_k P(k) \otimes_{S_k} (T_Q X)^{\otimes k} = \coprod_k P(k) \otimes_{S_k} \big(\coprod_m Q(m) \otimes_{S_m} X^{\otimes m}\big)^{\otimes k}$. Distributing $\otimes$ over the coproducts, the $k$-fold tensor power becomes a coproduct over $(m_1, \dots, m_k)$ of $\big(\bigotimes_i Q(m_i)\big) \otimes X^{\otimes(\sum m_i)}$, with the $S_{m_i}$-actions inducing up to $S_{\sum m_i}$. Collecting by total arity $n = \sum m_i$ and using the definition of $\circ$ to recognise the coefficient of $X^{\otimes n}$ as $(P \circ Q)(n) \otimes_{S_n}(-)$ gives $T_P(T_Q(X)) \cong T_{P \circ Q}(X)$. And $T_I(X) = I(1) \otimes_{S_1} X = X$, so $T_I = \mathrm{Id}$. Strong monoidality follows; a strong monoidal functor carries monoids to monoids, so $T_P$ is a monad.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — hypotheses on $\mathcal{V}$.** Assume $\mathcal{V}$ is symmetric monoidal with all countable coproducts and with $\otimes$ distributing over them; this guarantees the coproducts, coinvariants $(-)_{S_n} = (-) \otimes_{S_n}$, and inductions in the formula for $\circ$ exist and that $\otimes$ commutes with them. ($\mathbf{Set}, \mathbf{Vect}_k, \mathbf{Top}$, and chain complexes all satisfy this.)
>
> **Step 1 — the monoidal category.** Define $\circ$ and $I$ as in Notation. By Lemma 1, $\circ$ has a coherent associator; by Lemma 2, $I$ is a two-sided unit with coherent unitors; the pentagon and triangle hold. Hence $(\mathrm{SymSeq}(\mathcal{V}), \circ, I)$ is a monoidal category. (It is not symmetric: $P \circ Q \not\cong Q \circ P$ in general.)
>
> **Step 2 — data correspondence.** By the universal property of $\circ$ established in Lemma 3, morphisms $P \circ P \to P$ correspond bijectively and naturally to operadic composition operations $\gamma$, and morphisms $I \to P$ correspond to elements $\mathrm{id} \in P(1)$.
>
> **Step 3 — axiom correspondence.** By Lemma 3, the associativity and unit axioms of a monoid $(P, \mu, \eta)$ are, under the correspondence of Step 2, exactly the associativity and unit axioms of an operad $(P, \gamma, \mathrm{id})$. The equivariance axiom of an operad is automatically satisfied by any such $\gamma$, since $\gamma$ arises as a map descending through the $\otimes_{S_k}$ and $\mathrm{Ind}$ in the definition of $\circ$. A morphism of monoids is precisely a morphism of operads (it commutes with $\mu, \eta$ iff it commutes with $\gamma, \mathrm{id}$). Therefore the category of operads in $\mathcal{V}$ is isomorphic to the category of monoids in $(\mathrm{SymSeq}(\mathcal{V}), \circ, I)$.
>
> **Step 4 — corollary.** By Lemma 4, $P \mapsto T_P$ is strong monoidal $(\mathrm{SymSeq}, \circ, I) \to (\mathrm{End}(\mathcal{V}), \circ, \mathrm{Id})$. A strong monoidal functor sends monoids to monoids; applied to the operad $P$ (a monoid for $\circ$) it yields a monad $T_P$ (a monoid for functor composition), with multiplication and unit the images of $\gamma$ and $\mathrm{id}$. The algebras over the monad $T_P$ are, by direct comparison of the structure maps, exactly the [[Def - Algebra for an Operad|P-algebras]]. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Combinatorial species and exponential generating functions.** A symmetric sequence in $\mathbf{Set}$ (a *species*) has an exponential generating function $\sum_n |P(n)| x^n / n!$, and the composition product $\circ$ corresponds to *plethystic substitution* $f[g]$ of generating functions. An operad is then a "monoid under plethysm", and the dimension sequence of an operad satisfies a functional equation. Apply this to compute that the generating function of the associative operad is $x/(1-x)$ and of the commutative operad is $e^x - 1$, recovering classical species identities from operad structure.

**Polynomial functors and data types.** In the semantics of programming languages, a *polynomial functor* $F(X) = \coprod_n P(n) \times X^n$ models an algebraic data type (lists, trees) and is precisely $T_P$ for a non-symmetric operad $P$ of "shapes". The corollary says such functors compose as operads compose, so the substitution of one data type into another is operadic composition; this is the source of the "container" and "species" formalisms in functional programming and underlies the derivative-of-a-data-type calculus.

**Formal group laws and power series.** The monoid structure under substitution of formal power series $\{f : f(0) = 0, f'(0) = 1\}$ with composition $f \circ g$ is the one-dimensional shadow of the composition product: a one-dimensional "operad" of reparametrisations. Recognising the substitution monoid of power series as a degenerate composition product clarifies why the bar/cobar and Koszul-duality machinery for operads has analogues for formal groups and why both feature in chromatic homotopy theory.

---

# Bridges

- **[[Def - Monoid in a Monoidal Category|Monoid in a monoidal category]]** — this theorem is one entry in the master table of that page. A ring is a monoid in $(\mathbf{Ab}, \otimes_{\mathbb{Z}})$; a $k$-algebra is a monoid in $(\mathbf{Vect}_k, \otimes_k)$; a [[Def - Monad and Comonad|monad]] is a monoid in $([\mathcal{C},\mathcal{C}], \circ)$; and now an operad is a monoid in $(\mathrm{SymSeq}, \circ)$. The unifying lesson is that "associative unital structure" is a single definition, and exotic algebraic objects are obtained by exotic choices of ambient monoidal category — here, symmetric sequences under substitution.

- **[[Def - Monad and Comonad|Monad]]** — the corollary $P \mapsto T_P$ realises every operad as a monad, and identifies operads with the *analytic* (Schur-polynomial) monads: those whose underlying endofunctor is a sum $\coprod_n P(n) \otimes_{S_n} X^{\otimes n}$. This is why operad theory is a refinement of monad theory: an operad is a monad presented by a graded pile of operations rather than handed over as an opaque endofunctor, and the extra presentation is exactly what makes free algebras and resolutions computable.

- **[[Thm - The Free Operad|The free operad]]** — the free-monoid construction in $(\mathrm{SymSeq}, \circ, I)$ *is* the free operad. Transporting "the free monoid on $M$ is $\coprod_n M^{\otimes n}$" through the theorem gives "the free operad on a symmetric sequence $E$ is $\coprod_n E^{\circ n}$", which unwinds to the operad of $E$-labelled rooted trees. The monoid viewpoint is what makes the free operad a one-line corollary rather than a hand construction.

- **[[Def - Operad|Operad]]** — this theorem is the structural definition promised on the operad page: it replaces the three operad axioms by the single statement "monoid in symmetric sequences", absorbing equivariance into the composition product. It is the recommended way to *remember* the definition.

---

# Unlocked by This

> [!tip] Operadic Bar–Cobar and Koszul Duality *(from Operadic Homotopy Theory)*
> Once an operad is a monoid, the **bar construction** of a monoid applies, giving the operadic bar–cobar adjunction between operads and cooperads and the theory of **Koszul duality** (which exchanges $\mathrm{Comm}$ and $\mathrm{Lie}$). The cofibrant resolutions $A_\infty$ and $E_\infty$ are the bar–cobar resolutions of $\mathrm{Assoc}$ and $\mathrm{Comm}$ as monoids in $\mathrm{SymSeq}$.

> [!tip] Operadic Modules and Factorization Homology *(from Operadic Homotopy Theory)*
> Modules over the monoid $P$ in $\mathrm{SymSeq}$ are **$P$-algebras** (left modules) and **operadic bimodules** (used to change operads); the bimodule calculus over $E_n$ is the algebraic backbone of **factorization homology**, which integrates an $E_n$-algebra over a manifold. The monoid-and-module language is what makes these constructions routine.
