---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Monoidal Category"
  - "Def - Unbiased Monoidal Category"
  - "Def - Weak and Lax Monoidal Functor"
  - "Thm - Coherence for Unbiased Monoidal Categories"
  - "Thm - The Yoneda Lemma"
tags: [category-theory, higher-categories, foundations]
---

# Notation

A [[Def - Monoidal Category|monoidal category]] $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ is **strict** when $\alpha, \lambda, \rho$ are all identities, so $(A\otimes B)\otimes C = A\otimes(B\otimes C)$ and $I \otimes A = A = A \otimes I$ on the nose. A **monoidal equivalence** is a weak (strong) [[Def - Weak and Lax Monoidal Functor|monoidal functor]] $F : \mathcal{C} \to \mathcal{D}$ that is an equivalence of underlying categories; we write $\mathcal{C} \simeq_{\otimes} \mathcal{D}$. We write $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$ for the [[Thm - The Yoneda Lemma|Yoneda embedding]], $A \mapsto \mathcal{C}(-, A)$. The full registry is on [[Higher Categories — Strict n-Categories and Notions of Monoidal Category]].

---

# Statement

> **Theorem (Strictification of monoidal categories).** Every [[Def - Monoidal Category|monoidal category]] $\mathcal{C}$ is monoidally equivalent to a *strict* monoidal category $\mathcal{C}^{\mathrm{st}}$:
> $$\mathcal{C} \;\simeq_{\otimes}\; \mathcal{C}^{\mathrm{st}}, \qquad \mathcal{C}^{\mathrm{st}} \text{ strict}.$$
> Consequently, in any computation one may assume without loss of generality that the tensor is strictly associative and unital — the associators and unitors may be suppressed. The braided and symmetric cases hold with "strict braided/symmetric" in place of "strict."

> **Remark (the limit of strictification).** The analogous statement is *true* for [[Def - 2-Category and Bicategory|bicategories]] (every bicategory is biequivalent to a strict $2$-category, [[Thm - Strictification of Bicategories|strictification of bicategories]]) but **false** for tricategories: not every weak $3$-category (**tricategory**) is equivalent to a strict $3$-category, the first obstruction being the [[Higher Categories — Strict n-Categories and Notions of Monoidal Category#§3 Coherence and the Periodic Table|braiding produced by Eckmann–Hilton]]. Strictification is a low-dimensional miracle.

---

# Motivation

Coherence ([[Thm - Coherence for Unbiased Monoidal Categories|the previous theorem]]) tells us every diagram of associators and unitors commutes, so the bracketing genuinely does not matter. Strictification turns that *epistemic* fact ("you may not worry about brackets") into an *ontological* one ("you may pretend the brackets are not there, because there is an equivalent category in which they really are not"). The two are different in kind: coherence is a statement about which diagrams commute in $\mathcal{C}$; strictification produces a *new* category $\mathcal{C}^{\mathrm{st}}$, equivalent to $\mathcal{C}$, in which the structural isomorphisms are literally identities.

Why bother, given coherence? Because many constructions and proofs become dramatically shorter when the tensor is strict — no associators to insert, no pentagon to track, string diagrams that are honestly unambiguous. Strictification is the licence behind the universal working convention "assume the monoidal category is strict." It is also the cleanest demonstration of what coherence *buys*: a coherent weak structure is, up to equivalence, no weaker than a strict one. And it sets up the central cautionary tale of higher category theory: this convenient collapse works in dimensions $1$ and $2$ and then *stops*, which is the content of the Remark and the deep reason weak higher categories cannot be wished away.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal input is "a monoidal category." The recognition skill is knowing when strictification is the right tool to deploy.

The first disguised source is **a proof or construction cluttered with associators and unitors**. Whenever a calculation in a monoidal category threatens to drown in coherence isomorphisms — defining a Hopf algebra antipode, checking a string-diagram identity, building a [[Def - Monoid in a Monoidal Category|monoid]] with many factors — the move is to strictify first, do the calculation with strict $\otimes$, and transport back. The non-obvious step is that the strict calculation is valid for the original category because the equivalence is *monoidal*. *Example problem:* verify a tangle/braid identity in a braided monoidal category by computing in its strictification, where the wires carry no bracketing.

The second disguised source is **a monoidal category arising as a category of modules or representations**, where $\otimes$ is a tensor product defined by a universal property and hence associative only up to canonical iso. Such categories are the bread and butter of representation theory and quantum algebra, and strictification lets one treat $V \otimes W \otimes U$ as a single object. The non-obviousness is that the equivalent strict model exists even though the universal-property tensor is irreducibly non-strict. *Example problem:* work in the strictification of $\mathbf{Rep}(G)$ to define the symmetric/antisymmetric powers without bracketing bookkeeping.

The third disguised source is **a one-object [[Def - 2-Category and Bicategory|bicategory]]**, equivalently a monoidal category viewed one dimension up. Strictifying it is the bicategorical strictification restricted to one object. The non-obvious link is that strictifying a monoidal category and strictifying its associated one-object bicategory are the same operation, which is why the proofs run in parallel and why the *failure* in dimension three (tricategories) is foreshadowed here. *Example problem:* deduce that the endomorphism monoidal category of an object in a bicategory is strictifiable from the one-object case.

**Targets (Output Amplification)**

The bare conclusion is a monoidal equivalence to a strict category. Combined with other facts it is a workhorse.

Combine strictification with **a property invariant under monoidal equivalence**. Anything preserved by monoidal equivalences — having duals, being braided, the structure of its [[Def - Monoid in a Monoidal Category|monoids]] and modules, the [[Def - Limit and Colimit|limits and colimits]] of the underlying category — can be checked in the strict model and exported. The further result is that "without loss of generality strict" is rigorous for all such properties, which is most properties of interest. The combination is nonobvious only in that one must confirm the property *is* equivalence-invariant.

Combine strictification with **the coherence theorem**. Coherence is the input that *makes* strictification possible (it is what guarantees the comparison functor is monoidal); conversely, strictification gives a slick *re-proof* of coherence — in the strict model all canonical diagrams commute trivially, and the equivalence transports this back. The two theorems are nearly equivalent, and having both lets one choose whichever is easier in a given argument.

Combine strictification with **the dimensional ladder**. Strictification holds in dimension $1$ (monoidal $=$ one-object bicategory) and $2$ (bicategories) but fails in dimension $3$. The target is a *diagnostic*: when a would-be strictification fails, the obstruction is genuine higher-categorical content (a braiding, a syllepsis), not a bookkeeping artefact. This is how one recognises that weak $n$-categories for $n \geq 3$ are unavoidable.

---

# Why Is It True

The mechanism is a single beautiful idea: **embed $\mathcal{C}$ into a category of "tensoring operators," where tensoring becomes composition of functors — and composition is strictly associative.** Strictness is manufactured by trading the non-strict operation $\otimes$ for the always-strict operation $\circ$.

Here is the construction in outline. By [[Thm - The Yoneda Lemma|Yoneda]], $\mathcal{C}$ embeds in the [[Def - Functor Category|functor category]] $[\mathcal{C}^{op}, \mathbf{Set}]$. Each object $A$ gives an *endofunctor* "tensor with $A$" of an appropriate target, and the endofunctor category $([\mathcal{D}, \mathcal{D}], \circ, \mathrm{id})$ is **strictly** monoidal because functor composition is strictly associative and the identity functor is a strict unit (this is the strict example on [[Def - Monoidal Category]]). The objects of the strict model $\mathcal{C}^{\mathrm{st}}$ are these tensoring endofunctors (concretely, lists of objects of $\mathcal{C}$ acting by iterated tensor), morphisms are the appropriate transformations, and the tensor in $\mathcal{C}^{\mathrm{st}}$ is *composition* of these operators — strict by construction. The functor $A \mapsto (-\otimes A)$ embeds $\mathcal{C}$ into $\mathcal{C}^{\mathrm{st}}$, is fully faithful and essentially surjective (so an equivalence of categories), and is weak monoidal with comparison isomorphisms built from $\alpha, \lambda, \rho$. **Coherence is exactly what makes those comparison isomorphisms well-defined and the functor monoidal.**

So the bolded mechanism is: **replace each object by the operator "tensor with it," because operators compose strictly, and embed $\mathcal{C}$ among the operators using Yoneda.** The non-strictness of $\otimes$ is absorbed into the equivalence; the surviving operation is composition, which has no associativity defect.

Why does this fail for tricategories? Because the same trick promotes a tricategory to *strict* composition but cannot simultaneously strictify the *interchange* coherence at the top level — the Eckmann–Hilton phenomenon forces a genuine braiding among the top cells that no choice of strict model can remove. The operator trick strictifies one kind of associativity per dimension; in dimension $3$ there are two interacting kinds, and one of them is irreducibly weak.

---

# What Makes This Hard

The hard part is not the construction of $\mathcal{C}^{\mathrm{st}}$ — the operator/Yoneda idea is clean — but checking that the embedding $\mathcal{C} \to \mathcal{C}^{\mathrm{st}}$ is genuinely a *monoidal* equivalence, i.e. that its tensor-comparison isomorphisms satisfy the lax/weak coherence axioms. This is where every associator and unitor of $\mathcal{C}$ must be shown to fit together, and it is exactly the step that *uses* [[Thm - Coherence for Unbiased Monoidal Categories|coherence]]. The common error is to declare victory after building the strict category and the underlying equivalence, forgetting to verify that the equivalence respects $\otimes$; an equivalence of underlying categories that is *not* monoidal would not let you transport monoidal statements. The second subtlety is the unit: making $I$ a strict unit (not just associativity strict) requires the unitor coherence and is the fiddly part of the proof.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Build the strict model from "tensoring operators," whose tensor is functor composition (strict). Embed $\mathcal{C}$ via $A \mapsto (-\otimes A)$. Show the embedding is an equivalence of categories and is weak monoidal, using coherence to define and verify the comparison isomorphisms. Then $\mathcal{C} \simeq_\otimes \mathcal{C}^{\mathrm{st}}$.

**Subgoal decomposition:**

1. **Define the strict model $\mathcal{C}^{\mathrm{st}}$.** Objects = finite lists of objects of $\mathcal{C}$ (equivalently, the tensoring endofunctors they induce); tensor = concatenation/composition; unit = empty list.
   - *Hint:* Concatenation of lists is strictly associative and the empty list is a strict unit.
   - *Why needed:* It produces a category whose tensor is strict by construction.

2. **Define the comparison functor $E : \mathcal{C}^{\mathrm{st}} \to \mathcal{C}$.** Send a list $(A_1, \dots, A_n)$ to the (left-bracketed) tensor $\otimes_n(A_1,\dots,A_n)$.
   - *Hint:* On morphisms use the canonical isomorphisms from coherence.
   - *Why needed:* It connects the strict model back to $\mathcal{C}$.

3. **Show $E$ is an equivalence of underlying categories.** Fully faithful and essentially surjective.
   - *Hint:* Essential surjectivity: every object $A$ is $E$ of the singleton list $(A)$. Full faithfulness: morphisms of lists are defined to be morphisms of their tensors.
   - *Why needed:* An equivalence is required for a monoidal equivalence.

4. **Make $E$ (or its inverse) weak monoidal — invoke coherence.** Equip $E$ with comparison isomorphisms $E(\vec A) \otimes E(\vec B) \cong E(\vec A \frown \vec B)$ and verify the lax coherence axioms.
   - *Hint:* The comparison is a canonical map (a $\gamma$); the lax axioms are commuting diagrams of canonical maps, true by [[Thm - Coherence for Unbiased Monoidal Categories|coherence]].
   - *Why needed:* This is the crux — without it $E$ is only an ordinary equivalence.

5. **Conclude the monoidal equivalence.** A weak monoidal functor that is an equivalence of categories is a monoidal equivalence.
   - *Hint:* Invert $E$ (up to natural iso) and check the inverse is also weak monoidal.
   - *Why needed:* It delivers $\mathcal{C} \simeq_\otimes \mathcal{C}^{\mathrm{st}}$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The list category is strict monoidal
> **Statement:** Let $\mathcal{C}^{\mathrm{st}}$ have objects the finite lists $(A_1, \dots, A_n)$ of objects of $\mathcal{C}$, a morphism $(A_1,\dots,A_n) \to (B_1,\dots,B_m)$ being a morphism $\otimes_n(\vec A) \to \otimes_m(\vec B)$ in $\mathcal{C}$, tensor given by concatenation, and unit the empty list. Then $\mathcal{C}^{\mathrm{st}}$ is a *strict* monoidal category.
>
> **Hint:** Concatenation of lists satisfies $(\vec A \frown \vec B)\frown \vec C = \vec A \frown(\vec B \frown \vec C)$ and $()\frown \vec A = \vec A = \vec A \frown ()$ literally.
>
> **Why needed:** It is the strict target of the equivalence (subgoal 1).
>
> > [!note]- Full proof
> > Define composition of morphisms via composition in $\mathcal{C}$ (using the chosen tensor $\otimes_n$); this is associative and unital because composition in $\mathcal{C}$ is. The tensor on objects, $(\vec A, \vec B) \mapsto \vec A \frown \vec B$, is strictly associative and unital because list concatenation is. The tensor on morphisms is concatenation of the corresponding morphisms in $\mathcal{C}$, made functorial using coherence (the canonical iso identifying $\otimes_{n+m}(\vec A \frown \vec B)$ with a composite). Strict associativity and unit laws hold on objects on the nose; the structural isomorphisms are identities. Hence $\mathcal{C}^{\mathrm{st}}$ is strict monoidal.
>
> [!note]- Lemma 2: The comparison functor is an equivalence of categories
> **Statement:** The functor $E : \mathcal{C}^{\mathrm{st}} \to \mathcal{C}$, $(A_1,\dots,A_n) \mapsto \otimes_n(A_1,\dots,A_n)$, is fully faithful and essentially surjective, hence an equivalence of underlying categories.
>
> **Hint:** Morphisms in $\mathcal{C}^{\mathrm{st}}$ were *defined* to be morphisms of the tensors, giving full faithfulness; the singleton list $(A)$ has $E(A) = A$, giving essential surjectivity.
>
> **Why needed:** A monoidal equivalence requires an underlying equivalence (subgoal 3).
>
> > [!note]- Full proof
> > Full faithfulness: by definition $\mathcal{C}^{\mathrm{st}}\big((\vec A),(\vec B)\big) = \mathcal{C}\big(\otimes_n(\vec A), \otimes_m(\vec B)\big) = \mathcal{C}(E(\vec A), E(\vec B))$, and $E$ acts as the identity on these hom-sets, so it is fully faithful. Essential surjectivity: for any object $A \in \mathcal{C}$, the singleton list $(A)$ satisfies $E((A)) = \otimes_1(A) \cong A$ via $\iota$. A fully faithful, essentially surjective functor is an equivalence.
>
> [!note]- Lemma 3: $E$ is weak monoidal
> **Statement:** $E$ carries comparison isomorphisms $\phi : E(\vec A) \otimes E(\vec B) \xrightarrow{\cong} E(\vec A \frown \vec B)$ and $\phi_0 : I \xrightarrow{\cong} E(())$ satisfying the [[Def - Weak and Lax Monoidal Functor|weak monoidal functor]] coherence axioms.
>
> **Hint:** $\phi$ is the canonical map $\otimes_n(\vec A)\otimes \otimes_m(\vec B) \cong \otimes_{n+m}(\vec A \frown \vec B)$ (a $\gamma$); the axioms are diagrams of canonical maps.
>
> **Why needed:** This upgrades the equivalence of Lemma 2 to a *monoidal* equivalence (subgoal 4) — the crux.
>
> > [!note]- Full proof
> > Define $\phi_{\vec A, \vec B} : \otimes_n(\vec A)\otimes \otimes_m(\vec B) \to \otimes_{n+m}(\vec A \frown \vec B)$ to be the composition isomorphism $\gamma_{n,m}$, and $\phi_0 : I \to \otimes_0() = I$ the identity. These are isomorphisms. The associativity coherence axiom for $E$ asserts equality of two composites of $\gamma$'s between $\big(\otimes(\vec A)\otimes\otimes(\vec B)\big)\otimes \otimes(\vec C)$ and $\otimes_{n+m+p}(\vec A \frown \vec B \frown \vec C)$; both are canonical maps with the same source and target, hence equal by [[Thm - Coherence for Unbiased Monoidal Categories|coherence]]. The unit axioms are similarly diagrams of canonical maps, true by coherence. Thus $E$ is weak (strong) monoidal.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — well-posedness.** Fix a monoidal category $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$. By [[Thm - Biased and Unbiased Monoidal Categories Coincide|biased = unbiased]] we may use the $n$-ary tensors $\otimes_n$ and their composition isomorphisms $\gamma$, and by [[Thm - Coherence for Unbiased Monoidal Categories|coherence]] all canonical diagrams commute. These two facts are the only inputs.
>
> **Step 1 — construct $\mathcal{C}^{\mathrm{st}}$.** By Lemma 1, the category of finite lists of objects of $\mathcal{C}$, with concatenation as tensor and the empty list as unit, is a *strict* monoidal category $\mathcal{C}^{\mathrm{st}}$.
>
> **Step 2 — the comparison functor.** Define $E : \mathcal{C}^{\mathrm{st}} \to \mathcal{C}$ by $E(A_1, \dots, A_n) = \otimes_n(A_1, \dots, A_n)$ and the identity on hom-sets (legitimate since hom-sets of $\mathcal{C}^{\mathrm{st}}$ are hom-sets of the corresponding tensors in $\mathcal{C}$).
>
> **Step 3 — $E$ is an equivalence of categories.** By Lemma 2, $E$ is fully faithful and essentially surjective, hence an equivalence; choose a pseudo-inverse $E'$ with natural isomorphisms $E E' \cong \mathrm{id}_{\mathcal{C}}$ and $E' E \cong \mathrm{id}_{\mathcal{C}^{\mathrm{st}}}$.
>
> **Step 4 — $E$ is weak monoidal.** By Lemma 3, $E$ carries comparison isomorphisms $\phi = \gamma$ and $\phi_0 = \mathrm{id}$ satisfying the weak monoidal coherence axioms, all of which hold by coherence. So $E$ is a strong monoidal functor.
>
> **Step 5 — conclude.** A strong monoidal functor that is an equivalence of underlying categories is a monoidal equivalence (its pseudo-inverse inherits a strong monoidal structure via the comparison isomorphisms). Hence $\mathcal{C} \simeq_\otimes \mathcal{C}^{\mathrm{st}}$ with $\mathcal{C}^{\mathrm{st}}$ strict. The braided/symmetric cases carry the symmetric-group data along, replacing coherence by its braided/symmetric form. $\qquad \blacksquare$

---

# Cross-Field Exercise Suggestions

**Quantum algebra — Drinfeld's strictification of quasi-Hopf algebras.** The representation category of a quasi-Hopf algebra is monoidal with a nontrivial associator (the Drinfeld associator); strictification says it is monoidally equivalent to a strict one, which is the conceptual content behind being able to ignore the associator in many computations of quantum invariants. The application is nonobvious because the associator there is a genuinely transcendental object, yet the equivalence still strictifies it away.

**Topology — strict models for the smash product.** The smash product on pointed spaces is non-strict, but the category of pointed spaces is monoidally equivalent to a strict model; this is what underlies the construction of strictly associative ring spectra (a delicate analogue one dimension up, where the *symmetric* strictification famously fails for naive spectra and forces symmetric/orthogonal spectra). Recognising where strictification succeeds and where it must be replaced by a more careful model is the lesson.

**Logic — coherence and proof normalization.** In categorical logic, a monoidal category models a fragment of (linear) logic, and strictification corresponds to a normal form for proofs in which the structural rules (associativity, unit) are invisible. The application is nonobvious: strictification is the semantic counterpart of cut-elimination / normalization for the associativity structural rules.

---

# Bridges

- **[[Thm - Coherence for Unbiased Monoidal Categories|Coherence]]** — the essential input. Strictification builds a strict model and an equivalence; coherence is what makes the equivalence *monoidal* (Lemma 3). Conversely, strictification re-proves coherence: in the strict model every canonical diagram commutes trivially, and the monoidal equivalence transports this back to $\mathcal{C}$. The two theorems are two faces of one fact.

- **[[Thm - Strictification of Bicategories|Strictification of bicategories]]** — the one-dimension-up analogue, and literally the same statement for one-object bicategories. Every bicategory is biequivalent to a strict $2$-category; restricting to a single $0$-cell recovers monoidal strictification. The shared proof (the operator/Yoneda embedding into a strict structure) is why the two run in parallel.

- **The failure for tricategories** — the boundary of the phenomenon. Not every weak $3$-category is equivalent to a strict one; the first obstruction is the braiding forced by the [[Higher Categories — Strict n-Categories and Notions of Monoidal Category#§3 Coherence and the Periodic Table|Eckmann–Hilton argument]] among top cells. This is the precise sense in which "you can always assume strict" is a dimension-$\leq 2$ luxury, and weak higher categories become unavoidable from dimension $3$.

- **[[Thm - The Yoneda Lemma|The Yoneda lemma]]** — the technical engine. The strict model is built from "tensoring operators," and Yoneda is what embeds $\mathcal{C}$ faithfully among such operators, trading the non-strict $\otimes$ for strict functor composition $\circ$.

---

# Unlocked by This

> [!tip] "Assume the Category is Strict" *(from this chapter and beyond)*
> The everyday convention in monoidal category theory, quantum algebra, and TQFT — dropping all associators and unitors — is licensed exactly by this theorem. Any monoidal statement may be proved in the strict model and transported, because monoidal equivalences preserve everything monoidal.

> [!tip] Why Weak Higher Categories Are Unavoidable *(from Higher Category Theory)*
> Strictification works through dimension $2$ and fails at dimension $3$. This is not a technical nuisance but the structural reason the subject needs **weak ω-categories**: from dimension $3$ on, coherence cells (braidings, syllepses) carry genuine information that no strict model can hold. The periodic table of §3 is the bookkeeping of exactly these surviving cells.

> [!tip] Strictness vs. Strictifiability in Homotopy Theory *(from Algebraic Topology)*
> The pattern "coherent-weak structures are equivalent to strict ones in low dimensions, not in high ones" recurs for **$A_\infty$- and $E_\infty$-algebras**: $A_\infty$ (weakly associative) algebras are strictifiable to honest dg-algebras, but $E_\infty$ (weakly commutative) ones are *not* strictifiable to commutative dg-algebras over $\mathbb{Z}$ — the same Eckmann–Hilton obstruction, now in the homotopical world.
