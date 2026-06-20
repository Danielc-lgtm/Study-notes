---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Monad Monoid and Module in a Bicategory"
  - "Def - 2-Category and Bicategory"
  - "Def - Monad and Comonad"
  - "Def - Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

$\mathcal{K}$ is a [[Def - 2-Category and Bicategory|bicategory]] with objects $\mathcal{A}, \mathcal{B}, \dots$, $1$-cells composed by $\circ$ (juxtaposition), and $2$-cells composed vertically by $\cdot$ and horizontally by $\ast$. A **monad** $(t, \mu, \eta)$ in $\mathcal{K}$ is an object $\mathcal{A}$ with an endo-$1$-cell $t : \mathcal{A} \to \mathcal{A}$ and $2$-cells $\mu : tt \Rightarrow t$, $\eta : 1_{\mathcal{A}} \Rightarrow t$ obeying the [[Def - Monad Monoid and Module in a Bicategory|monad axioms]]. Given monads $s$ on $\mathcal{A}$ and $t$ on $\mathcal{B}$, a **$(t,s)$-bimodule** is a $1$-cell $m : \mathcal{A} \to \mathcal{B}$ with commuting left $t$-action $\lambda : tm \Rightarrow m$ and right $s$-action $\rho : ms \Rightarrow s$. We write $m \otimes_s n$ for the tensor of an $(s,r)$-bimodule $n$ with a $(t,s)$-bimodule $m$ over the shared monad $s$. We assume $\mathcal{K}$ has **local reflexive coequalizers** preserved by composition on each side, so these tensors exist; call such $\mathcal{K}$ **suitable**. The resulting bicategory is $\mathrm{Mod}(\mathcal{K})$. The full registry is on [[Higher Categories — fc-Multicategories and Weak Double Categories]].

---

# Statement

> **Theorem (the bicategory of monoids and modules).** Let $\mathcal{K}$ be a suitable [[Def - 2-Category and Bicategory|bicategory]] (one with local reflexive coequalizers preserved by precomposition and postcomposition). Then there is a bicategory $\mathrm{Mod}(\mathcal{K})$ whose
> - **objects** are [[Def - Monad Monoid and Module in a Bicategory|monads]] (equivalently monoids) in $\mathcal{K}$;
> - **$1$-cells** $t \to t'$ are $(t', t)$-**bimodules** $m$;
> - **$2$-cells** are bimodule maps;
>
> with horizontal composition of $1$-cells given by the **tensor over the middle monad**, $n \otimes_{t'} m$, the identity $1$-cell on a monad $t$ given by $t$ regarded as a $(t,t)$-bimodule via its own multiplication, and associativity and unit constraints inherited from those tensors. The composition is associative and unital up to coherent invertible $2$-cells, so $\mathrm{Mod}(\mathcal{K})$ is a genuine bicategory.

> **Corollary (the running examples).** Taking $\mathcal{K} = \mathbf{Span}(\mathbf{Set})$, the objects of $\mathrm{Mod}(\mathcal{K})$ are small [[Def - Category|categories]] and the $1$-cells are **profunctors**, with horizontal composition the profunctor (coend) composite. Taking $\mathcal{K}$ to be the one-object bicategory of an [[Def - Ring|ring]]-enriched setting, $\mathrm{Mod}(\mathcal{K})$ is the bicategory of rings, bimodules, and bimodule maps, with composition $\otimes_R$.

---

# Motivation

In ordinary algebra there is a fundamental upgrade: from a single [[Def - Ring|ring]] $R$ and its modules, you pass to the *bicategory* of all rings, with bimodules as the morphisms between them and tensor product as composition. This bicategory is where Morita theory lives — two rings are Morita-equivalent precisely when they are equivalent *as objects of this bicategory* — and it is the natural arena for descent, for the theory of progenerators, and for thinking of a bimodule as a "generalised ring homomorphism". The question this theorem answers is: *how much of that upgrade depends on rings?* The answer is: none of it. The construction "objects $=$ monoids, morphisms $=$ bimodules, composition $=$ tensor" works in any [[Def - 2-Category and Bicategory|bicategory]] with enough colimits, and it produces a new bicategory $\mathrm{Mod}(\mathcal{K})$ each time.

The importance is that $\mathrm{Mod}(\mathcal{K})$ is a *machine for generating the standard "categories of correspondences"*. Run it on $\mathbf{Span}(\mathbf{Set})$ and out comes the bicategory of categories and profunctors — the home of the [[Thm - The Yoneda Lemma|Yoneda]] and Kan-extension calculus, of weighted limits, and of the formal theory of enriched categories. Run it on relations and out comes a calculus of ordered structures. Run it on rings and out comes Morita theory. The theorem is what lets all of these be studied with one set of tools, because each is a $\mathrm{Mod}(\mathcal{K})$ for a suitable $\mathcal{K}$. Its role, then, is not a single fact but a *factory*: it converts a bicategory into a richer one whose objects carry algebraic structure and whose morphisms are the right notion of "correspondence" between them.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$\mathcal{K}$ is a suitable bicategory and we have monads and bimodules in it". The source question is: *when does a problem secretly present a $\mathrm{Mod}(\mathcal{K})$, so that this theorem organises it?*

The first disguised source is **a category of algebraic objects with a tensor-like composition of morphisms-with-coefficients**. Whenever you have objects carrying an associative multiplication (rings, monoids, algebras, monads) and "morphisms" that are bimodule-like (carrying compatible two-sided actions), with a tensor that composes them, you are looking at $\mathrm{Mod}(\mathcal{K})$ for the appropriate $\mathcal{K}$. The bridge "this is $\mathrm{Mod}(\mathcal{K})$" is non-obvious because the tensor is usually presented concretely (e.g. $\otimes_R$) rather than as a bicategorical coequalizer. *Example problem:* recognise the bicategory of $k$-algebras and bimodules as $\mathrm{Mod}(\mathcal{K})$ with $\mathcal{K}$ the one-object bicategory $\mathbf{Mod}_k$, so that Morita theory becomes "equivalence in $\mathrm{Mod}(\mathcal{K})$".

The second disguised source is **a setting where "small category" and "monad" coincide**. By the identification of small categories with monads in $\mathbf{Span}(\mathbf{Set})$, *any* construction on small categories that you would like to make functorial in profunctors is a $\mathrm{Mod}(\mathbf{Span}(\mathbf{Set}))$ construction. The bridge is the dictionary "category $=$ monad in $\mathbf{Span}(\mathbf{Set})$, profunctor $=$ bimodule". *Example problem:* to prove that profunctor composition is associative-up-to-iso, do not compute coends by hand — invoke this theorem with $\mathcal{K} = \mathbf{Span}(\mathbf{Set})$ and read off the associativity from the bimodule-tensor associativity.

The third disguised source is **an enrichment base $\mathcal{V}$ presenting categories enriched in $\mathcal{V}$**. A $\mathcal{V}$-enriched category is a monad in the bicategory $\mathcal{V}\text{-}\mathbf{Mat}$ of $\mathcal{V}$-valued matrices (objects $=$ sets, $1$-cells $=$ matrices of $\mathcal{V}$-objects, composition $=$ matrix multiplication using $\otimes$ and the coproduct in $\mathcal{V}$). The bridge is "$\mathcal{V}$-category $=$ monad in $\mathcal{V}\text{-}\mathbf{Mat}$, $\mathcal{V}$-profunctor $=$ bimodule". *Example problem:* obtain the bicategory of $\mathcal{V}$-categories and $\mathcal{V}$-profunctors uniformly as $\mathrm{Mod}(\mathcal{V}\text{-}\mathbf{Mat})$, recovering [[Def - Enriched Category|enriched]] category theory as a special case.

**Targets (Output Amplification)**

The bare conclusion is "$\mathrm{Mod}(\mathcal{K})$ is a bicategory". Combined with other facts it yields the standard theory.

Combine the conclusion with **the notion of equivalence in a bicategory**. Two objects of $\mathrm{Mod}(\mathcal{K})$ are equivalent iff there are bimodules between them composing to the identity bimodules up to iso. The further result $E$ is **Morita theory**: for rings, this is the classical statement that $R$ and $S$ are Morita-equivalent iff $S \cong \mathrm{End}_R(P)$ for a progenerator $P$; for categories, it is "Cauchy-completion equivalence". The combination is non-obvious because a purely formal definition (equivalence in a bicategory) specialises to a deep classical theorem.

Combine the conclusion with **adjunctions in $\mathrm{Mod}(\mathcal{K})$**. A $1$-cell (bimodule) in $\mathrm{Mod}(\mathcal{K})$ may have a [[Def - 2-Category and Bicategory|right adjoint]] $1$-cell; for $\mathcal{K} = \mathbf{Span}(\mathbf{Set})$ the adjoint pairs of profunctors are exactly those representable by [[Def - Functor|functors]]. The further result is a characterisation of *functors among profunctors*: a profunctor is (the image of) a functor iff it has a right adjoint in $\mathrm{Mod}(\mathbf{Span}(\mathbf{Set}))$. This is the bicategorical source of the "functors are the maps, profunctors are the relations" slogan.

Combine the conclusion with **monoids/monads internal to $\mathrm{Mod}(\mathcal{K})$**. Since $\mathrm{Mod}(\mathcal{K})$ is itself a bicategory, one can take monads *in it*, iterating the construction. The further result $E$ is structures like *categories enriched in profunctors* and the higher layers of the [[Def - Generalized Multicategory|generalized-multicategory]] tower. The combination is non-obvious because the output of the factory becomes a new input to the same factory, generating an indefinite hierarchy.

---

# Why Is It True

The theorem is true because **the tensor of bimodules is associative for exactly the reason $\otimes_R$ is associative in algebra: it is a coequalizer that balances the two adjacent actions, and balancing is symmetric in how you bracket**. Picture three bimodules $m, n, p$ over monads with matching middles. The composite $m \otimes_{s} n \otimes_{r} p$ should "tensor $m$ with $n$ over $s$, then with $p$ over $r$". Whether you first form $(m \otimes_s n)$ and then tensor with $p$, or first form $(n \otimes_r p)$ and then tensor $m$ with it, you are computing the *same* coequalizer of the iterated action $m\,s\,n\,r\,p \rightrightarrows m\,n\,p$ — the two bracketings are two ways of presenting one universal object, hence canonically isomorphic. That canonical iso is the associator of $\mathrm{Mod}(\mathcal{K})$.

The identity $1$-cell works because **a monad is its own unit bimodule**: $t$ acting on itself by $\mu$ on both sides is a $(t,t)$-bimodule, and $t \otimes_t m$ coequalizes $t\,t\,m \rightrightarrows t\,m$ via $\mu$ and the action, whose coequalizer is $m$ itself (the action $\lambda$ exhibits it) — this is precisely the unit law $R \otimes_R M \cong M$ in algebra. So the unitors come from the monad's own unit and multiplication.

The single sentence to remember: **$\mathrm{Mod}(\mathcal{K})$ is "the bicategory of rings and bimodules", written without the word "ring" — replace "ring" by "monad in $\mathcal{K}$", "bimodule" by "bimodule in $\mathcal{K}$", and "$\otimes_R$" by "the action-balancing coequalizer", and every classical proof transcribes.** The local reflexive coequalizers are needed for exactly one thing — to *form* the tensor — and their preservation by composition is needed for exactly one thing — to make the tensor associative as a coequalizer-of-coequalizers. Everything else is the monoid/module bookkeeping you already know from ring theory.

---

# What Makes This Hard

The genuinely technical point is the **existence and good behaviour of the bimodule tensor**: it is a coequalizer in a hom-category, and for the composition to be associative *up to coherent iso* one needs composition in $\mathcal{K}$ to *preserve* these coequalizers on each side (so that $\,\cdot \otimes_s (\cdot \otimes_r \cdot)$ and $(\cdot \otimes_s \cdot) \otimes_r \cdot$ are both the iterated coequalizer). People get stuck by assuming the tensor exists or assuming composition is cocontinuous without checking; when $\mathcal{K}$ lacks these colimits the construction simply fails (which is why the chapter often works with the *virtual* version — an [[Def - fc-Multicategory|fc-multicategory]] — that needs no colimits at all). The second subtlety is the coherence (pentagon/triangle) of the associator and unitors, which must be derived from the universal properties of the coequalizers rather than assumed.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Define $\mathrm{Mod}(\mathcal{K})$ by transcribing the bicategory of rings-and-bimodules. The only non-formal step is the tensor of bimodules, defined as a reflexive coequalizer balancing the two adjacent actions; assume $\mathcal{K}$ has these coequalizers and that composition preserves them. Then associativity and unitality of the tensor, and the coherence of the resulting constraints, all follow from the universal property of coequalizers exactly as in ring theory.

**Subgoal decomposition:**

1. **Define the tensor $m \otimes_s n$.** For a $(t,s)$-bimodule $m$ and an $(s,r)$-bimodule $n$, define $m \otimes_s n$ as the coequalizer of the right-action-of-$s$-on-$m$ and the left-action-of-$s$-on-$n$, $m\,s\,n \rightrightarrows m\,n \to m \otimes_s n$.
   - *Hint:* This is the reflexive coequalizer presenting "balanced over $s$"; it exists because $\mathcal{K}$ is suitable.
   - *Why needed:* It is the horizontal composition of $\mathrm{Mod}(\mathcal{K})$.

2. **Equip $m \otimes_s n$ with a $(t,r)$-bimodule structure.** Push the outer left $t$-action and right $r$-action through the coequalizer.
   - *Hint:* Composition preserves the coequalizer, so the actions descend uniquely.
   - *Why needed:* The composite must again be a $1$-cell of $\mathrm{Mod}(\mathcal{K})$.

3. **Identity $1$-cells.** Show $t$, as a $(t,t)$-bimodule via $\mu$ on both sides, satisfies $t \otimes_t m \cong m \cong m \otimes_s s$.
   - *Hint:* The action $\lambda : tm \Rightarrow m$ exhibits $m$ as the coequalizer of $t\,t\,m \rightrightarrows t\,m$ (the unit law gives a splitting).
   - *Why needed:* It provides the units and the unitors.

4. **Associator.** Show $(m \otimes_s n) \otimes_r p \cong m \otimes_s (n \otimes_r p)$ canonically.
   - *Hint:* Both are the iterated coequalizer of $m\,s\,n\,r\,p \rightrightarrows m\,n\,p$; use preservation of coequalizers by composition.
   - *Why needed:* Bicategory composition must associate up to iso.

5. **Coherence.** Verify the pentagon for the associator and the triangle relating associator and unitors.
   - *Hint:* All maps in sight are induced by universal properties of coequalizers, so the coherence diagrams commute by uniqueness of induced maps.
   - *Why needed:* Without coherence the constraints are not the data of a bicategory.

---

# Lemma Decomposition

> [!note]- Lemma 1: The balanced tensor of bimodules exists and is a bimodule
> **Statement:** For a $(t,s)$-bimodule $m$ and an $(s,r)$-bimodule $n$ in a suitable $\mathcal{K}$, the coequalizer $m \otimes_s n$ of $\rho_m \ast 1_n,\ 1_m \ast \lambda_n : m\,s\,n \rightrightarrows m\,n$ exists and carries a canonical $(t,r)$-bimodule structure.
>
> **Hint:** Existence is the local reflexive coequalizer hypothesis; the bimodule structure descends because composition preserves these coequalizers, so the outer actions induce unique actions on the quotient.
>
> **Why needed:** This is horizontal composition in $\mathrm{Mod}(\mathcal{K})$; without it there are no $1$-cell composites.
>
> > [!note]- Full proof
> > The parallel pair $m\,s\,n \rightrightarrows m\,n$ is reflexive (the common section is $1_m \ast \eta_s \ast 1_n$ using the monad unit $\eta_s : 1 \Rightarrow s$), so its coequalizer $q : m\,n \to m\otimes_s n$ exists by suitability. For the left $t$-action: $t \ast q : t\,m\,n \to t(m\otimes_s n)$. Since composition with $t$ on the left preserves the coequalizer, $t(m\otimes_s n)$ is the coequalizer of $t\,m\,s\,n \rightrightarrows t\,m\,n$; the left action $\lambda_m \ast 1_n : t\,m\,n \to m\,n$ coequalizes the pair (it commutes with $\rho_m, \lambda_n$ by the bimodule commuting law), so it induces $\bar\lambda : t(m\otimes_s n) \to m\otimes_s n$. Associativity and unitality of $\bar\lambda$ follow from those of $\lambda_m$ by uniqueness of induced maps. The right $r$-action is dual. The two commute because they did before passing to the quotient. $\square$

> [!note]- Lemma 2: A monad is the unit bimodule
> **Statement:** For a monad $t$, the $1$-cell $t$ with $\mu$ as both left and right action is a $(t,t)$-bimodule, and for any $(t,s)$-bimodule $m$ there are canonical isomorphisms $t \otimes_t m \cong m$ and (dually) $m \otimes_s s \cong m$.
>
> **Hint:** The left action $\lambda_m : t\,m \to m$ coequalizes $t\,t\,m \rightrightarrows t\,m$, and the unit $\eta_t$ provides a section, so $\lambda_m$ *is* the coequalizer — which is the definition of $t \otimes_t m$.
>
> **Why needed:** It supplies the identity $1$-cells and the unitors of $\mathrm{Mod}(\mathcal{K})$.
>
> > [!note]- Full proof
> > That $(t, \mu, \mu)$ is a bimodule is the monad associativity and unit laws read as the two action laws plus their commuting (which is again associativity of $\mu$). Now $t \otimes_t m$ is the coequalizer of $\mu \ast 1_m,\ 1_t \ast \lambda_m : t\,t\,m \rightrightarrows t\,m$. The map $\lambda_m : t\,m \to m$ satisfies $\lambda_m \cdot (\mu \ast 1_m) = \lambda_m \cdot (1_t \ast \lambda_m)$ (the module associativity), so it factors through the coequalizer; conversely $\eta_t \ast 1_m : m \to t\,m$ is a section with $\lambda_m \cdot (\eta_t \ast 1_m) = 1_m$ (module unit law), exhibiting $m$ with $\lambda_m$ as the coequalizer. Hence $t \otimes_t m \cong m$ naturally. $\square$

> [!note]- Lemma 3: The two bracketings are the same iterated coequalizer
> **Statement:** For composable bimodules $m, n, p$, both $(m \otimes_s n) \otimes_r p$ and $m \otimes_s (n \otimes_r p)$ are canonically isomorphic to the coequalizer of the four-fold action $m\,s\,n\,r\,p \rightrightarrows m\,n\,p$ (balancing simultaneously over $s$ and $r$).
>
> **Hint:** Composition preserves reflexive coequalizers on each side, so a coequalizer of coequalizers is the coequalizer of the combined diagram (a "$3\times 3$ lemma" for reflexive coequalizers).
>
> **Why needed:** It is the associator of $\mathrm{Mod}(\mathcal{K})$; its naturality and coherence (pentagon) follow from the universal property.
>
> > [!note]- Full proof
> > Form $m \otimes_s n$ as the coequalizer over $s$, then $(m\otimes_s n)\otimes_r p$ as the coequalizer over $r$. Because tensoring with $p$ on the right preserves the first coequalizer, $(m\otimes_s n)\otimes_r p$ is the coequalizer of the pushed-forward $s$-balancing applied to the $r$-balanced $m\,n\,p$. Symmetrically, $m\otimes_s(n\otimes_r p)$ is the coequalizer of the $r$-balancing applied to the $s$-balanced object. By the standard fact that a reflexive coequalizer commutes with another reflexive coequalizer when the relevant functors preserve them (the diagonal of the $3\times 3$ diagram), both equal the simultaneous coequalizer of $m\,s\,n\,r\,p \rightrightarrows m\,n\,p$. The induced comparison is the canonical associator; the pentagon commutes because all five edges are the unique map between universal objects. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — preconditions.** Assume $\mathcal{K}$ is suitable: each hom-category $\mathcal{K}(\mathcal{A},\mathcal{B})$ has reflexive coequalizers, and composition $\circ$ preserves them in each variable. This is exactly what is needed to form and balance the tensors below; with it, every coequalizer invoked exists and descends.
>
> **Step 1 — data of $\mathrm{Mod}(\mathcal{K})$.** Objects: monads $(t, \mu, \eta)$ in $\mathcal{K}$. A $1$-cell $t \to t'$ (where $t$ is on $\mathcal{A}$, $t'$ on $\mathcal{B}$) is a $(t', t)$-bimodule $m : \mathcal{A} \to \mathcal{B}$. A $2$-cell $m \Rightarrow m'$ is a bimodule map. Vertical composition of $2$-cells is that of $\mathcal{K}$.
>
> **Step 2 — horizontal composition.** For $1$-cells $t \xrightarrow{m} t' \xrightarrow{n} t''$ (so $m$ is a $(t',t)$-bimodule, $n$ a $(t'',t')$-bimodule), define $n \circ m := n \otimes_{t'} m$, the balanced tensor of Lemma 1, which is a $(t'',t)$-bimodule. On $2$-cells, bimodule maps induce maps of coequalizers, giving a functor $\mathrm{Mod}(\mathcal{K})(t',t'') \times \mathrm{Mod}(\mathcal{K})(t,t') \to \mathrm{Mod}(\mathcal{K})(t,t'')$.
>
> **Step 3 — identities.** The identity $1$-cell on a monad $t$ is $t$ viewed as a $(t,t)$-bimodule via $\mu$ (Lemma 2). The left and right unitors $t \otimes_t m \cong m$ and $m \otimes_t t \cong m$ are the canonical isomorphisms of Lemma 2; naturality in $m$ is by uniqueness of induced maps.
>
> **Step 4 — associator.** For composable $m, n, p$, the associator $a : (p \otimes_{t''} n) \otimes_{t'} m \xrightarrow{\cong} p \otimes_{t''} (n \otimes_{t'} m)$ is the canonical isomorphism of Lemma 3, both sides being the simultaneous balanced coequalizer. Naturality is again by uniqueness of induced maps from a coequalizer.
>
> **Step 5 — coherence.** *Pentagon:* for four composable bimodules, all five vertices are the simultaneous balanced coequalizer of the five-fold composite, and each edge is the unique comparison map between universal objects; hence the pentagon commutes by uniqueness. *Triangle:* the two routes from $(p \otimes_{t''} t') \otimes_{t'} m$ to $p \otimes_{t''} m$ — one using the right unitor on $p$, one using the left unitor on $m$ via the associator — both equal the canonical map out of the coequalizer that uses the unit $\eta_{t'}$, by Lemma 2; hence they agree.
>
> **Step 6 — conclude.** The data of Steps 1–4 satisfy the bicategory axioms (functoriality of horizontal composition from Step 2, associator and unitors from Steps 3–4, coherence from Step 5). Therefore $\mathrm{Mod}(\mathcal{K})$ is a bicategory.
>
> **Step 7 — the corollary.** For $\mathcal{K} = \mathbf{Span}(\mathbf{Set})$: a monad is a small [[Def - Category|category]] $C$ (objects $C_0$, arrows $C_1$, composition $\mu$, identities $\eta$); a $(D,C)$-bimodule is a span $C_0 \leftarrow P \to D_0$ with commuting left $D$- and right $C$-actions, i.e. a **profunctor** $C^{op}\times D \to \mathbf{Set}$; the balanced tensor over $D$ is the coend $\int^{d} P(-,d)\times Q(d,-)$, the profunctor composite. The reflexive coequalizers in $\mathbf{Span}(\mathbf{Set})$ are computed in $\mathbf{Set}$ and preserved by pullback-composition, so $\mathbf{Span}(\mathbf{Set})$ is suitable. Hence $\mathrm{Mod}(\mathbf{Span}(\mathbf{Set}))$ is the bicategory of small categories, profunctors, and natural transformations. The ring case is the one-object specialisation with $\otimes_R$ the balanced tensor of modules. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Algebra — Morita equivalence as bicategorical equivalence.** Two rings $R, S$ are Morita-equivalent iff $R$ and $S$ are equivalent objects of $\mathrm{Mod}(\mathcal{K})$ for $\mathcal{K} = \mathbf{Mod}_k$, i.e. there exist bimodules ${}_S P_R$ and ${}_R Q_S$ with $P \otimes_R Q \cong S$ and $Q \otimes_S P \cong R$. Recognising the classical progenerator condition as "invertible $1$-cell in $\mathrm{Mod}(\mathcal{K})$" is the non-obvious bridge; the theorem makes Morita theory a corollary of bicategory theory.

**Category theory — Cauchy completion via profunctor adjunctions.** In $\mathrm{Mod}(\mathbf{Span}(\mathbf{Set}))$, a category $C$ is *Cauchy-complete* iff every right-adjoint profunctor into it is representable by a functor. Phrasing absoluteness of colimits and idempotent-splitting as a property of $1$-cells in $\mathrm{Mod}(\mathcal{K})$ is the surprising application — it turns a limit-theoretic notion into a bicategorical one.

**Enriched category theory — change of base as a pseudofunctor.** A lax monoidal functor $\mathcal{V} \to \mathcal{W}$ induces a change-of-base on enriched categories; recast via the theorem, it is a (pseudo)functor $\mathrm{Mod}(\mathcal{V}\text{-}\mathbf{Mat}) \to \mathrm{Mod}(\mathcal{W}\text{-}\mathbf{Mat})$. The non-obvious point is that change-of-enrichment, usually checked by hand on hom-objects, is automatic functoriality of the $\mathrm{Mod}$ construction.

---

# Bridges

- **[[Def - Weak Double Category|Weak double categories]] and the virtual version** — $\mathrm{Mod}(\mathcal{K})$ exists as a bicategory only when $\mathcal{K}$ has the colimits to form bimodule tensors. When those colimits are absent, the monads, bimodules, and module maps still form an [[Def - fc-Multicategory|fc-multicategory]] (a virtual double category): the $2$-cells over a *string* of bimodules are the multilinear/balanced maps, and no tensor need exist. So $\mathrm{Mod}(\mathcal{K})$ is the *representable* shadow of a more robust fc-multicategory, and the theorem is "representability holds when the colimits exist" — exactly the relationship of [[Thm - fc-Multicategories Subsume Bicategories and Monoidal Categories]].

- **[[Def - Monad and Comonad|Eilenberg–Moore and Kleisli]] as formal monad theory** — the objects of $\mathrm{Mod}(\mathcal{K})$ are monads, so this theorem is part of the *formal theory of monads* in a bicategory. The Kleisli and Eilenberg–Moore constructions, which for $\mathcal{K} = \mathbf{Cat}$ produce the [[Def - Monad and Comonad|Kleisli and algebra categories]] of an ordinary monad, generalise to objects in any $2$-category, and the bimodule calculus of $\mathrm{Mod}(\mathcal{K})$ is the ambient setting in which those universal monad-resolutions are compared.

- **[[Thm - The Yoneda Lemma|The Yoneda lemma]] in the profunctor bicategory** — taking $\mathcal{K} = \mathbf{Span}(\mathbf{Set})$, the unit bimodule on a category $C$ is the hom-profunctor $C(-,-)$, and the Yoneda lemma is the statement that this hom-profunctor is the identity $1$-cell of $C$ in $\mathrm{Mod}(\mathcal{K})$ — every profunctor tensored with the hom-profunctor is itself. So Yoneda is, in this bicategory, exactly the unit law $t \otimes_t m \cong m$ of Lemma 2 read for categories and profunctors.

---

# Unlocked by This

> [!tip] Profunctors, weighted limits, and formal category theory *(from category theory)*
> The bicategory $\mathrm{Mod}(\mathbf{Span}(\mathbf{Set}))$ of categories and **profunctors** is the arena for the modern formal development of category theory: **weighted limits**, **Kan extensions**, **pointwise extensions**, and the **Cauchy completion** are all defined via profunctor (bi)adjunctions there. Everything that follows from "$\mathrm{Mod}(\mathcal{K})$ is a bicategory" — adjunctions, equivalences, monads-in-it — becomes available as formal category theory.

> [!tip] Higher algebra and ∞-bimodules *(from derived and higher category theory)*
> Replacing $\mathcal{K}$ by a homotopical or $\infty$-categorical analogue turns $\mathrm{Mod}(\mathcal{K})$ into the bicategory (or $(\infty,2)$-category) of **algebras and bimodules** central to higher algebra: $E_1$-algebras with their bimodules, derived Morita theory, and the bimodule formulation of **Tor** and **Ext**. The classical theorem here is the decategorified shadow of that machinery, and the colimit hypotheses become "geometric realisations exist" in the homotopical setting.
