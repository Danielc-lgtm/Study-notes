---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Module Homomorphism"
  - "Def - Exact Sequence and Short Exact Sequence"
  - "Def - Flat Module"
  - "Def - Tensor Product of Modules"
  - "Def - Multiplicative Set and Localization"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $S \subseteq R$ be a [[Def - Multiplicative Set and Localization|multiplicative subset]], $M$ an [[Def - Module|$R$-module]]. Write $S^{-1}M$ for the localized module, $S^{-1}f : S^{-1}M \to S^{-1}N$ for the localization of an $R$-linear map $f : M \to N$ (acting by $\tfrac ms \mapsto \tfrac{f(m)}{s}$), and $\otimes_R$ for the [[Def - Tensor Product of Modules|tensor product]]. A sequence $A \xrightarrow{f} B \xrightarrow{g} C$ is **exact** at $B$ if $\operatorname{im} f = \ker g$. The functor "$S^{-1}(-)$" sends $M \mapsto S^{-1}M$ and $f \mapsto S^{-1}f$. The full registry is on [[Commutative Algebra IV — Localization]].

---

# Statement

> **Theorem (Localization as base change, and exactness/flatness; Becker Prop. 4.6, 4.11).**
> 1. **(Tensor description, Prop. 4.6.)** For every $R$-module $M$ there is a natural isomorphism of $S^{-1}R$-modules
> $$S^{-1}R \otimes_R M \;\xrightarrow{\ \sim\ }\; S^{-1}M, \qquad \tfrac rs \otimes m \mapsto \tfrac{rm}{s}.$$
> So $S^{-1}(-)$ is naturally isomorphic to the base-change functor $S^{-1}R \otimes_R (-)$.
> 2. **(Exactness, Prop. 4.11.)** $S^{-1}(-)$ is an **exact functor**: if $A \xrightarrow{f} B \xrightarrow{g} C$ is exact at $B$, then $S^{-1}A \xrightarrow{S^{-1}f} S^{-1}B \xrightarrow{S^{-1}g} S^{-1}C$ is exact at $S^{-1}B$.
> 3. **(Flatness.)** Equivalently, $S^{-1}R$ is a **flat** $R$-module.

> **Corollary (localization commutes with kernels and images).** For any $R$-linear $f$, $S^{-1}(\ker f) = \ker(S^{-1}f)$ and $S^{-1}(\operatorname{im} f) = \operatorname{im}(S^{-1}f)$, and $S^{-1}N \hookrightarrow S^{-1}M$ for any submodule $N \subseteq M$.

---

# Motivation

This is the technical heart of the chapter: the single result that makes localization a *clean* operation rather than a treacherous one. The slogan is that **fractions never create or destroy relations beyond those forced by the denominators**, and the precise form of that slogan is exactness.

The danger localization could pose is the danger any "quotient-like" construction poses: it might collapse things that should stay separate, or fail to remember relations. Concretely, if $N \subseteq M$ is a submodule, is $S^{-1}N$ a submodule of $S^{-1}M$, or could the localization process glue elements of $S^{-1}N$ that were distinct? If $f$ is injective, is $S^{-1}f$ still injective, or could inverting denominators manufacture a kernel? These are exactly the questions exactness answers, and the answer is the best possible: localization preserves *all* exactness. Injections stay injections, surjections stay surjections, kernels localize to kernels, images to images, short exact sequences to short exact sequences.

The reason this is the chapter's workhorse is that it lets you *localize any diagram*. Every later proof — that localization commutes with quotients, that being-zero/injective/surjective/flat are local properties — proceeds by taking an exact sequence, applying $S^{-1}(-)$, and keeping exactness. Without it, none of the local–global machinery would function: "check it after localizing at each prime" is only legitimate because localization does not corrupt the algebraic relations you are checking.

The deep structural insight, due to the tensor description, is that **localization is base change**: $S^{-1}M = S^{-1}R \otimes_R M$ is "extend scalars from $R$ to $S^{-1}R$". Once you see this, exactness is no longer surprising — it is the statement that $S^{-1}R$ is a *flat* module, and flatness is *defined* as "tensoring with me preserves injections". So the three parts of the theorem are one fact wearing three hats: a concrete isomorphism, a property of a functor, and a property of a module. The prototype to keep in mind throughout is $\mathbb{Q}$ over $\mathbb{Z}$: $\mathbb{Q} = S^{-1}\mathbb{Z}$ is flat, which is why clearing denominators never loses solutions to linear systems.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ for "apply exactness" is: *an exact sequence (or an injection, surjection, kernel, image, or submodule inclusion) that you wish to localize*.

The first disguised source is **a submodule, quotient, kernel, or image appears and you want its localization**. Property $B$: any of these standard constructions is present. The bridge is that each fits into a short exact sequence — $0 \to N \to M \to M/N \to 0$ for a submodule, $0 \to \ker f \to M \to \operatorname{im} f \to 0$ for a map — so applying the exact functor commutes the construction past localization. The non-obvious part: you never compute the localized object from scratch; you localize the sequence. *Example problem:* show $S^{-1}(M/N) \cong S^{-1}M / S^{-1}N$ by localizing $0\to N\to M\to M/N\to 0$ — see [[Thm - Localization Commutes with Quotients and Finite Operations]].

The second disguised source is **you must prove an injection of localized modules**. Property $B$: a map between honest modules is injective, and you want injectivity after localizing. The bridge is flatness: tensoring (i.e. localizing) with the flat module $S^{-1}R$ preserves injections. The non-obviousness: flatness is precisely the property that licenses this, and not every base change has it. *Example problem:* if $N_1, N_2 \subseteq M$ then $S^{-1}(N_1 \cap N_2) = S^{-1}N_1 \cap S^{-1}N_2$ — the $\supseteq$ direction uses that the localized inclusions remain inclusions.

The third disguised source is **a property is to be shown "local"**. Property $B$: a target property is on the local list. The bridge is that localizability of every such property is *exactly* the exactness of $S^{-1}(-)$ — "$f$ injective $\Rightarrow f_{\mathfrak{p}}$ injective" is just preservation of injections. The non-obvious value: the entire localizable-direction of the [[Thm - The Local-Global Principle|local–global principle]] is a one-line corollary of this theorem. *Example problem:* any local-property proof begins "localization is exact, so the property descends".

**Targets (Output Amplification)**

The conclusion $C$ is *exactness is preserved* (equivalently, $S^{-1}R$ is flat, equivalently localization commutes with kernels/images).

Combine $C$ with **a free presentation $R^t \to R^n \to M \to 0$**. Localizing gives $S^{-1}R^t \to S^{-1}R^n \to S^{-1}M \to 0$, a presentation of $S^{-1}M$ over $S^{-1}R$ with the *same* matrices. The further result $E$: localization is computable on presentations — $S^{-1}M$ has the same generators and relations, now over $S^{-1}R$. Nonobvious because it reduces computing a localization to base-changing a matrix.

Combine $C$ with **the tensor identity $S^{-1}M \otimes_{S^{-1}R} S^{-1}N \cong S^{-1}(M\otimes_R N)$**. Flatness lets localization pass through tensor products as well as exact sequences. The further result $E$: all the finite module operations (sums, intersections, quotients, tensors) commute with localization, so $S^{-1}(-)$ is transparent to module algebra ([[Thm - Localization Commutes with Quotients and Finite Operations]]). Nonobvious because tensor does *not* generally commute with arbitrary base change without flatness.

Combine $C$ with **a long exact sequence (Tor/Ext)**. Because $S^{-1}R$ is flat, $\operatorname{Tor}_i^R(S^{-1}R, M) = 0$ for $i \geq 1$, so localization is exact at the derived level and commutes with $\operatorname{Tor}$ and $\operatorname{Ext}$ of finitely presented modules. The further result $E$: homological invariants are computable prime-by-prime. Nonobvious because it promotes a statement about short exact sequences to one about derived functors.

---

# Why Is It True

There are two complementary explanations, and both are worth holding.

The *fraction-level* explanation: an element of $\ker(S^{-1}g)$ is some $\tfrac bs$ with $\tfrac{g(b)}{s} = 0$, meaning $u\,g(b) = 0$ in $C$ for some $u \in S$. But $u\,g(b) = g(ub)$, so $ub \in \ker g = \operatorname{im} f$ (here the original exactness is used), say $ub = f(a)$. Then $\tfrac bs = \tfrac{f(a)}{us} = S^{-1}f(\tfrac{a}{us}) \in \operatorname{im}(S^{-1}f)$. The whole proof is the single move "clear the denominator with a $u \in S$ to land back in the honest module, use exactness there, then divide back". **The clearing factor that defines the localization equivalence relation is *exactly* the device that lets fraction-level exactness be reduced to module-level exactness.**

The *structural* explanation: $S^{-1}M = S^{-1}R \otimes_R M$, so $S^{-1}(-)$ is the base-change functor $S^{-1}R \otimes_R (-)$. Tensoring is always *right* exact; the content is that here it is also *left* exact, i.e. preserves injections, which is the definition of $S^{-1}R$ being a flat module. And $S^{-1}R$ is flat for a reason you can feel: making elements of $S$ invertible cannot introduce a linear relation, because if $\sum \tfrac{r_i}{s_i} m_i = 0$ then clearing all denominators gives $u\sum r_i' m_i = 0$ in $M$ for some $u \in S$ — the relation was already present in $M$ (after scaling by a unit-to-be). Flatness is the formalisation of "denominators don't create relations".

**One-line mechanism: localization is base change along the flat extension $R \to S^{-1}R$, and the proof of flatness is "clear denominators with a single $u\in S$, use exactness in $M$, divide back".**

The tensor isomorphism itself (part 1) is proved by exhibiting the bilinear map $(\tfrac rs, m) \mapsto \tfrac{rm}{s}$, checking the induced linear map is surjective and injective; injectivity uses the slick observation that *every* tensor in $S^{-1}R \otimes_R M$ is **pure** — a single $\tfrac1s \otimes m$ — because you can pull all denominators to a common $s$ and absorb numerators into the module slot. Purity is what makes the injectivity check a one-liner.

---

# What Makes This Hard

The non-obvious step in the fraction proof is recognising that "$\tfrac{g(b)}{s} = 0$" does not mean "$g(b) = 0$" but "$u\,g(b) = 0$ for some $u \in S$" — you must reintroduce the clearing factor and use $u\,g(b) = g(ub)$ to land inside $\ker g$. People stuck here forget that fraction-zero is weaker than numerator-zero. In the tensor proof, the subtle point is the *purity of tensors* over $S^{-1}R$: that every element is a single pure tensor $\tfrac1s\otimes m$ is what makes injectivity tractable, and missing it leaves you trying to handle arbitrary sums. The common error is to assume tensoring preserves injections in general — it does not; flatness of $S^{-1}R$ specifically is what is being used.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Prove the tensor isomorphism $S^{-1}R\otimes_R M \cong S^{-1}M$ first (via purity of tensors), so that "localize" becomes "tensor with $S^{-1}R$". Then prove exactness directly at the fraction level by the clear-denominators argument, and observe that exactness of $S^{-1}R\otimes_R(-)$ is, by definition, flatness of $S^{-1}R$.

**Subgoal decomposition:**

1. **Tensor isomorphism.** Show $\varphi : S^{-1}R\otimes_R M \to S^{-1}M$, $\tfrac rs\otimes m \mapsto \tfrac{rm}{s}$, is an isomorphism.
   - *Hint:* surjectivity is clear; for injectivity, show every tensor equals a pure $\tfrac1s\otimes m$ (common denominator), then $\varphi(\tfrac1s\otimes m)=0 \Rightarrow um=0 \Rightarrow \tfrac1s\otimes m = \tfrac{1}{us}\otimes um = 0$.
   - *Why needed:* recasts localization as base change, giving the flatness reading.

2. **Exactness at the fraction level.** Show $\operatorname{im}(S^{-1}f) = \ker(S^{-1}g)$ from $\operatorname{im} f = \ker g$.
   - *Hint:* $\subseteq$ is $S^{-1}(g\circ f) = S^{-1}(0) = 0$. For $\supseteq$, take $\tfrac bs \in \ker(S^{-1}g)$, get $u\,g(b)=g(ub)=0$, so $ub\in\operatorname{im} f$, write $ub=f(a)$, then $\tfrac bs = S^{-1}f(\tfrac{a}{us})$.
   - *Why needed:* this *is* the exactness statement; everything else is corollary.

3. **Flatness.** State that exactness of $S^{-1}R\otimes_R(-)$ is the definition of $S^{-1}R$ flat.
   - *Hint:* a functor preserving all length-3 exact sequences preserves all exact sequences; tensoring is right exact, so left exactness (preserving injections) is the only new content — that is flatness.
   - *Why needed:* identifies the result with a reusable module property.

---

# Lemma Decomposition

> [!note]- Lemma 1: Every tensor in $S^{-1}R\otimes_R M$ is pure
> **Statement:** Each element of $S^{-1}R\otimes_R M$ can be written as a single pure tensor $\tfrac1s\otimes m$.
>
> **Hint:** Bring all fractions to a common denominator $s = s_1\cdots s_\ell$ and pull numerators into the module slot.
>
> **Why needed:** It reduces the injectivity of $\varphi$ to a one-line check on pure tensors.
>
> > [!note]- Full proof
> > Take $t = \sum_{i=1}^\ell \tfrac{r_i}{s_i}\otimes m_i$. Let $s = s_1\cdots s_\ell$ and $t_i = \prod_{j\neq i} s_j$, so $\tfrac{r_i}{s_i} = \tfrac{t_i r_i}{s}$. Then
> > $$t = \sum_i \tfrac{t_i r_i}{s}\otimes m_i = \sum_i \tfrac1s\otimes (t_i r_i m_i) = \tfrac1s\otimes\Big(\sum_i t_i r_i m_i\Big),$$
> > using $R$-bilinearity to move the scalar $t_i r_i$ across the tensor and additivity in the second slot. So $t = \tfrac1s\otimes m$ with $m = \sum_i t_i r_i m_i$.

> [!note]- Lemma 2: The tensor map is an isomorphism
> **Statement:** $\varphi : S^{-1}R\otimes_R M \to S^{-1}M$, $\tfrac rs\otimes m\mapsto\tfrac{rm}{s}$, is an $S^{-1}R$-linear isomorphism.
>
> **Hint:** Surjectivity is immediate; for injectivity use Lemma 1 and the fraction-zero criterion.
>
> **Why needed:** It is part 1 of the theorem, and the bridge to the flatness interpretation.
>
> > [!note]- Full proof
> > The map $(\tfrac rs, m)\mapsto\tfrac{rm}{s}$ is $R$-bilinear, so induces $\varphi$ with $\varphi(\tfrac rs\otimes m) = \tfrac{rm}{s}$; it is $S^{-1}R$-linear by inspection and surjective since $\tfrac ms = \varphi(\tfrac1s\otimes m)$. For injectivity, take $t$ in the kernel; by Lemma 1 write $t = \tfrac1s\otimes m$. Then $\varphi(t) = \tfrac ms = 0$ in $S^{-1}M$, so $um = 0$ for some $u\in S$. Hence
> > $$t = \tfrac1s\otimes m = \tfrac{u}{us}\otimes m = \tfrac{1}{us}\otimes um = \tfrac{1}{us}\otimes 0 = 0.$$
> > So $\ker\varphi = 0$ and $\varphi$ is an isomorphism.

> [!note]- Lemma 3: The clear-denominators step
> **Statement:** If $\tfrac bs\in\ker(S^{-1}g)$ for an exact $A\xrightarrow{f}B\xrightarrow{g}C$, then $\tfrac bs\in\operatorname{im}(S^{-1}f)$.
>
> **Hint:** Fraction-zero gives $u\,g(b)=0$; rewrite as $g(ub)=0$ and use exactness in $B$.
>
> **Why needed:** It is the $\supseteq$ inclusion, the only nontrivial half of exactness.
>
> > [!note]- Full proof
> > Suppose $S^{-1}g(\tfrac bs) = \tfrac{g(b)}{s} = 0$ in $S^{-1}C$. Then there is $u\in S$ with $u\,g(b) = 0$, i.e. $g(ub) = 0$, so $ub\in\ker g = \operatorname{im} f$. Choose $a\in A$ with $f(a) = ub$. Then
> > $$\tfrac bs = \tfrac{ub}{us} = \tfrac{f(a)}{us} = S^{-1}f\!\left(\tfrac{a}{us}\right) \in \operatorname{im}(S^{-1}f).$$
> > Combined with $\operatorname{im}(S^{-1}f)\subseteq\ker(S^{-1}g)$ (since $S^{-1}g\circ S^{-1}f = S^{-1}(g\circ f) = S^{-1}0 = 0$), this gives exactness.

---

# Formal Proof

> [!note]- Complete formal proof
> **Part 1 — tensor description.** By Lemma 2, $\varphi : S^{-1}R\otimes_R M \to S^{-1}M$ is an $S^{-1}R$-linear isomorphism, natural in $M$ (the defining formula commutes with $S^{-1}f$ for any $R$-linear $f$, by direct check on pure tensors). Hence the functors $S^{-1}(-)$ and $S^{-1}R\otimes_R(-)$ from $R$-modules to $S^{-1}R$-modules are naturally isomorphic.
>
> **Part 2 — exactness.** Let $A\xrightarrow{f}B\xrightarrow{g}C$ be exact at $B$, so $\operatorname{im} f = \ker g$.
>
> *Inclusion $\operatorname{im}(S^{-1}f)\subseteq\ker(S^{-1}g)$:* $S^{-1}g\circ S^{-1}f = S^{-1}(g\circ f)$, and $g\circ f = 0$ on $\operatorname{im} f = \ker g$, so $S^{-1}(g\circ f) = S^{-1}0 = 0$.
>
> *Inclusion $\ker(S^{-1}g)\subseteq\operatorname{im}(S^{-1}f)$:* this is Lemma 3.
>
> Hence $\operatorname{im}(S^{-1}f) = \ker(S^{-1}g)$: the localized sequence is exact at $S^{-1}B$. Since a functor preserving exactness of all length-three sequences preserves exactness of all sequences, $S^{-1}(-)$ is exact.
>
> **Part 3 — flatness.** By Part 1, $S^{-1}(-) \cong S^{-1}R\otimes_R(-)$. Tensoring with any module is right exact; Part 2 shows $S^{-1}R\otimes_R(-)$ is moreover *left* exact (it preserves injections: apply exactness to $0\to A\xrightarrow{f}B$). A module whose tensor functor preserves injections is, by definition, **flat**. Hence $S^{-1}R$ is a flat $R$-module.
>
> **Corollary.** Applying exactness to $0\to\ker f\to M\xrightarrow{f}\operatorname{im} f\to 0$ gives $S^{-1}(\ker f) = \ker(S^{-1}f)$ and $S^{-1}(\operatorname{im} f) = \operatorname{im}(S^{-1}f)$; applying it to $0\to N\to M$ gives $S^{-1}N\hookrightarrow S^{-1}M$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Clearing denominators in linear algebra over $\mathbb{Z}$.** A system $Ax = 0$ with integer matrix $A$ has the same solution space over $\mathbb{Q}$ as the $\mathbb{Q}$-span of its $\mathbb{Z}$-solutions, precisely because $\mathbb{Q} = S^{-1}\mathbb{Z}$ is flat: localization does not create new relations or kill old ones. Nonobvious recognition: the everyday "clear denominators" move in solving linear systems is an instance of flatness of the field of fractions.

**Flat families in deformation theory.** A family of varieties over a base is "flat" exactly when the fibres vary without sudden jumps in dimension or length; the algebraic condition is flatness of the structure map. That localization $R \to R_{\mathfrak{p}}$ is flat means restricting a flat family to a point's neighbourhood keeps it flat — the local model of a flat family is always flat. Nonobvious because the geometric notion of "continuously varying family" is encoded by the same algebraic flatness proved here.

**Exactness of stalks in sheaf cohomology.** A sequence of sheaves is exact iff it is exact on every stalk, and stalks are localizations; the exactness of localization is what makes "check exactness stalkwise" valid. This underlies the computation of cohomology via local data. Nonobvious because it converts a global exactness question into pointwise localizations, the foundational move of homological sheaf theory.

---

# Bridges

- **[[Def - Flat Module|Flat module]]** — this theorem is the most important *example* of flatness: $S^{-1}R$ is flat over $R$, with $\mathbb{Q}/\mathbb{Z}$ as prototype. Flatness is defined as "tensoring preserves injections", and the content here is that base change along a localization map never destroys injectivity — which is what "denominators don't create relations" means precisely.

- **[[Thm - Extension of Scalars Preserves Flatness|Extension of scalars preserves flatness]]** — used in the converse direction to prove flatness is a [[Def - Local Property (Localizable and Local-to-Global)|local property]]: since $M_{\mathfrak{p}} = R_{\mathfrak{p}}\otimes_R M$ and base change preserves flatness, $M$ flat $\Rightarrow M_{\mathfrak{p}}$ flat. This theorem provides the localizable half; the local-to-global half is in [[Thm - The Local-Global Principle]].

- **[[Thm - Localization Commutes with Quotients and Finite Operations|Localization commutes with quotients and finite operations]]** — the immediate consequence. Every identity there ($S^{-1}(M/N) = S^{-1}M/S^{-1}N$, $S^{-1}(N\cap P) = S^{-1}N\cap S^{-1}P$, the tensor identity) is proved by localizing an exact sequence and keeping exactness, i.e. by this theorem.

- **[[Thm - The Local-Global Principle|The local–global principle]]** — exactness is the *localizable* direction of every local property. "$f$ injective $\Rightarrow f_{\mathfrak{p}}$ injective" is just preservation of injections; the harder *local-to-global* direction needs the separate annihilator argument.

---

# Unlocked by This

> [!tip] Flat morphisms and flat families *(from Algebraic Geometry)*
> Flatness of $R \to S^{-1}R$ is the local model of a **flat morphism** of schemes — the algebraic condition for a family of fibres to vary "continuously", without the dimension or length of the fibre jumping. Open immersions (restrictions to opens $D(f)$) are flat because localizations are flat, so flatness is the right notion of "nice family" that includes all open restrictions. The entire theory of flat families, **Hilbert schemes**, and degeneration in moduli theory rests on flatness, and localization is the first and most basic flat map.

> [!tip] Localization commutes with cohomology *(from Homological Algebra / Sheaf Theory)*
> Because $S^{-1}R$ is flat, $\operatorname{Tor}_i^R(S^{-1}R, -) = 0$ for $i\geq 1$, so localization is **exact on the derived level** and commutes with $\operatorname{Tor}$, $\operatorname{Ext}$, and sheaf cohomology of quasicoherent sheaves: $(\operatorname{Tor}_i^R(M,N))_{\mathfrak{p}} = \operatorname{Tor}_i^{R_{\mathfrak{p}}}(M_{\mathfrak{p}}, N_{\mathfrak{p}})$ and $H^i(X, \mathcal{F})_{\mathfrak{p}}$ is computed locally. This is precisely why homological invariants can be computed one prime at a time — the derived form of the [[Thm - The Local-Global Principle|local–global principle]].
