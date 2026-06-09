---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Flat Module"
  - "Def - Restriction and Extension of Scalars"
  - "Def - Tensor Product of Modules"
  - "Def - Module Homomorphism"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; all modules unital. Let $f : R \to S$ be a ring homomorphism, making any $S$-module an $R$-module by restriction and giving the [[Def - Restriction and Extension of Scalars|extension of scalars]] $M \mapsto S \otimes_R M$ from $R$-modules to $S$-modules. We write $\otimes_R$ and $\otimes_S$ to keep the base ring explicit, and use the associativity isomorphism $(S \otimes_R M) \otimes_S N \cong M \otimes_R N$ for an $S$-module $N$ (an instance of the standard tensor isomorphisms). The full registry is on [[Commutative Algebra III — Flatness and Exactness]].

---

# Statement

> **Theorem (Extension of scalars preserves flatness).** Let $f : R \to S$ be a ring homomorphism and $M$ a flat $R$-module. Then $S \otimes_R M$ is a flat $S$-module.

> **Corollary (Localization is flat).** For a multiplicative set $T \subseteq R$, the localization $T^{-1}R = T^{-1}R \otimes_R R$ is a flat $R$-module, and more generally $T^{-1}M$ is flat over $T^{-1}R$ whenever $M$ is flat over $R$. Taking $R$ flat over itself, every localization $T^{-1}R$ is flat over $R$.

In particular flatness is stable under base change: if $M$ is flat over $R$, its base change $S \otimes_R M$ is flat over $S$ along *any* $R \to S$.

---

# Motivation

Flatness should be a *geometric* condition — "the family has no jumps" — and geometry demands that good conditions survive base change. If a family over a base is flat and you pull it back along a map of bases, the pulled-back family ought to remain flat; otherwise flatness would be an artefact of the chosen base rather than an intrinsic feature of the family. This theorem is exactly that stability, in its algebraic form: extending scalars along $R \to S$ — the algebra of pulling back along $\operatorname{Spec} S \to \operatorname{Spec} R$ — carries flat $R$-modules to flat $S$-modules.

The most important instance, and the one to keep in mind, is **localization**. Localizing is extension of scalars along $R \to T^{-1}R$, so the theorem says localization preserves flatness, and applied to $M = R$ (flat over itself) it says $T^{-1}R$ is a flat $R$-module — the cornerstone fact that "passing to fractions is exact", which powers the entire local theory. The flatness of $\mathbb{Q}$ over $\mathbb{Z}$ is this corollary in its smallest case.

The result also tells you that the *class of flat modules is closed under the operations of the subject*. You can build new flat modules from old ones by base change, compose base changes ($S \otimes_R M$ flat over $S$, then $S' \otimes_S (S \otimes_R M)$ flat over $S'$), and this stability is what makes flatness a workable hypothesis to carry through a construction rather than something that must be re-established at every step.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a flat $R$-module and a ring map $R \to S$", in disguise.

The first disguised source is **a localization**. The property $B$ is "I am localizing a flat module" — the ring map is $R \to T^{-1}R$. The bridge: localization is extension of scalars, so the theorem applies and $T^{-1}M$ is flat over $T^{-1}R$. The non-obvious value: flatness, established once over $R$, is inherited by every localization for free. *Example problem:* show $\mathbb{Z}_{(p)}$-modules obtained by localizing flat $\mathbb{Z}$-modules are flat.

The second disguised source is **a quotient base $S = R/I$**. The property $B$ is "I am reducing modulo an ideal." The bridge: $R \to R/I$ is a ring map, so $M/IM = (R/I)\otimes_R M$ is flat over $R/I$ when $M$ is flat over $R$ — flatness descends to the fibre's base ring. The non-obvious value: fibres of a flat family are themselves flat over the reduced base. *Example problem:* the reduction of a flat module mod a prime is flat over the residue ring.

The third disguised source is **a tower of ring maps $R \to S \to S'$**. The property $B$ is "iterated base change of a flat module." The bridge: apply the theorem twice, using $S' \otimes_S (S \otimes_R M) \cong S' \otimes_R M$. The non-obvious value: flatness composes along towers, so a single flatness over the bottom ring propagates all the way up. *Example problem:* base-change a flat module first to $\mathbb{C}$ then to $\mathbb{C}(t)$ and conclude flatness throughout.

**Targets (Output Amplification)**

The conclusion is "$S \otimes_R M$ is a flat $S$-module."

Combine with **exactness of base change**. Flat $S \otimes_R M$ means $(S \otimes_R M) \otimes_S (-)$ is exact, so $E$: an $S$-linear exact sequence stays exact after tensoring with the base-changed module. This is the technical content of "flat base change preserves exact sequences," used constantly in cohomology-and-base-change arguments. Nonobvious because it transfers exactness across two different base rings.

Combine with **the structure of $S$ as an $R$-algebra**. If $S$ itself is flat over $R$ and $M$ is flat over $R$, then $S \otimes_R M$ is flat over $S$ *and* (by transitivity) flat over $R$, so $E$: flatness over the bottom ring is preserved. The combination is useful for proving that compositions of flat maps are flat. Nonobvious in that two separate flatness hypotheses combine into flatness over a third ring.

Combine with **faithful flatness**. If moreover $S$ is faithfully flat over $R$, flatness of $S \otimes_R M$ over $S$ can be *descended* to flatness of $M$ over $R$, so $E$: flatness is a faithfully-flat-local property. This is the descent direction and is nonobvious because it runs the theorem backwards.

---

# Why Is It True

The intuition is that **flatness is an injectivity-preservation property, and the only thing base change does to an injectivity question is relabel it across an isomorphism — so the injectivity survives.** Concretely, to test flatness of $S \otimes_R M$ over $S$, take an $S$-injection $g : N \to N'$ and ask whether $\operatorname{id}\otimes g$ stays injective. The associativity isomorphism $(S \otimes_R M) \otimes_S N \cong M \otimes_R N$ turns this *top-row* $S$-question into a *bottom-row* $R$-question: the map you are testing is, up to the isomorphism, just $\operatorname{id}_M \otimes g$ viewed over $R$. But $g$ is still injective when viewed as an $R$-map (restriction of scalars does not change the underlying map), and $M$ is flat over $R$, so $\operatorname{id}_M \otimes g$ is injective on the bottom. The vertical isomorphisms transport this injectivity back to the top. Nothing is created or destroyed; the isomorphism merely re-expresses the same kernel.

**The whole mechanism in one sentence: $(S\otimes_R M)\otimes_S N \cong M\otimes_R N$ converts the $S$-flatness of $S\otimes_R M$ into the $R$-flatness of $M$, which is given.** The proof is one commutative square and a diagram chase; the content is entirely in the associativity isomorphism that lets the two base rings talk to each other.

There is a cleaner high-level reason worth recording: extension of scalars is the [[Def - Restriction and Extension of Scalars|left adjoint]] to restriction, and tensoring with a flat module is exact; the composite "extend then tensor over $S$" equals "tensor over $R$" by associativity, and a composite of exact functors is exact — so $(S\otimes_R M)\otimes_S(-) = M\otimes_R(-) \circ (\text{restriction})$ is exact, i.e. $S\otimes_R M$ is flat.

---

# What Makes This Hard

There is almost no difficulty here once the associativity isomorphism is in hand — the proof is a single diagram chase — so the "hard" part is *recognising the right isomorphism* and getting its $S$-linearity right. The non-obvious step is to view the $S$-flatness question as an $R$-flatness question via $(S \otimes_R M)\otimes_S N \cong M \otimes_R N$; readers often try to prove injectivity directly over $S$ and get tangled in the two module structures. The common error is to forget that the test map $g$, though given as $S$-linear, must be used as an $R$-linear injection on the bottom row — and that its injectivity is unchanged by restriction of scalars, which is the one fact making the chase go through.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Test $S$-flatness of $S \otimes_R M$ by tensoring an arbitrary $S$-injection $g : N \to N'$. Set up the commutative square whose vertical arrows are the associativity isomorphisms $(S \otimes_R M)\otimes_S N \cong M \otimes_R N$, whose bottom arrow is $\operatorname{id}_M \otimes g$, and whose top arrow is the map to be shown injective. Use flatness of $M$ over $R$ to get the bottom injective, then chase the square.

**Subgoal decomposition:**

1. **Build the square.** Exhibit the commutative diagram with verticals the associativity isomorphisms and horizontals $\operatorname{id}_{S\otimes M}\otimes_S g$ (top) and $\operatorname{id}_M\otimes_R g$ (bottom).
   - *Hint:* On pure tensors, $(s\otimes m)\otimes n \mapsto m\otimes(sn)$ down each side; check commutativity by following $(s\otimes m)\otimes n$.
   - *Why needed:* It links the $S$-question to the $R$-question.

2. **Bottom row injective.** Show $\operatorname{id}_M \otimes_R g : M\otimes_R N \to M\otimes_R N'$ is injective.
   - *Hint:* $g$ is injective as an $R$-map; $M$ is flat over $R$, so apply flatness.
   - *Why needed:* It is the only place the hypothesis is used.

3. **Chase.** Conclude the top row is injective.
   - *Hint:* Verticals are isomorphisms; injective bottom plus commuting square forces injective top.
   - *Why needed:* It delivers $S$-flatness of $S\otimes_R M$.

---

# Lemma Decomposition

> [!note]- Lemma 1: The associativity isomorphism
> **Statement:** For a ring map $R \to S$, an $R$-module $M$, and an $S$-module $N$, there is a natural $S$-module isomorphism $(S \otimes_R M) \otimes_S N \cong M \otimes_R N$, $(s \otimes m)\otimes n \mapsto m \otimes (sn)$, with inverse $m \otimes n \mapsto (1 \otimes m)\otimes n$.
>
> **Hint:** Both sides are universal for the appropriate balanced/bilinear maps; build maps both ways and check they are mutually inverse on pure tensors.
>
> **Why needed:** It is the entire bridge between the $S$-flatness question and the $R$-flatness hypothesis.
>
> > [!note]- Full proof
> > The map $(S \otimes_R M)\times N \to M \otimes_R N$, $((s\otimes m), n) \mapsto m \otimes (sn)$, is $S$-balanced (it respects the $S$-action: $((s'\cdot(s\otimes m)), n) = ((ss'\otimes m), n)\mapsto m\otimes(ss' n)$ and $((s\otimes m), s' n)\mapsto m\otimes(s s' n)$ agree), so it factors through $(S\otimes_R M)\otimes_S N$. Conversely $m \otimes n \mapsto (1\otimes m)\otimes n$ is $R$-bilinear and factors through $M\otimes_R N$. On pure tensors the composites are the identity, using $(s\otimes m)\otimes n = (1\otimes m)\otimes (sn)$ in $(S\otimes_R M)\otimes_S N$. Both are $S$-linear, so they are inverse $S$-isomorphisms.

> [!note]- Lemma 2: Restriction does not change injectivity
> **Statement:** If $g : N \to N'$ is an injective $S$-linear map, then $g$ is injective as an $R$-linear map (via $R \to S$).
>
> **Hint:** Injectivity is a statement about the underlying map of sets/abelian groups, unchanged by which ring acts.
>
> **Why needed:** It lets the $S$-injection $g$ feed the $R$-flatness of $M$ on the bottom row.
>
> > [!note]- Full proof
> > The underlying function of $g$ is the same whether $N, N'$ are regarded as $S$-modules or, by restriction of scalars along $R \to S$, as $R$-modules. Injectivity ($g(n) = 0 \Rightarrow n = 0$) is a property of this underlying function, hence holds in both interpretations.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $g : N \to N'$ be an injective $S$-linear map; we must show $\operatorname{id}_{S\otimes_R M} \otimes_S g : (S\otimes_R M)\otimes_S N \to (S\otimes_R M)\otimes_S N'$ is injective.
>
> Consider the commutative diagram with vertical arrows the associativity isomorphisms of Lemma 1:
> $$
> \begin{array}{ccc}
> (S\otimes_R M)\otimes_S N & \xrightarrow{\ \operatorname{id}\otimes_S g\ } & (S\otimes_R M)\otimes_S N' \\
> \downarrow{\cong} & & \downarrow{\cong} \\
> M\otimes_R N & \xrightarrow{\ \operatorname{id}_M\otimes_R g\ } & M\otimes_R N'
> \end{array}
> $$
> *Commutativity:* a pure tensor $(s\otimes m)\otimes n$ in the top-left goes right to $(s\otimes m)\otimes g(n)$ then down to $m\otimes(s\,g(n)) = m \otimes g(sn)$ (as $g$ is $S$-linear); going down first gives $m\otimes(sn)$, then right gives $m\otimes g(sn)$. The two agree, so the square commutes.
>
> By Lemma 2, $g$ is $R$-linear injective. Since $M$ is a [[Def - Flat Module|flat]] $R$-module, $\operatorname{id}_M \otimes_R g$ — the bottom arrow — is injective.
>
> Now chase: the vertical arrows are isomorphisms, hence injective. Take $x$ in the top-left with $(\operatorname{id}\otimes_S g)(x) = 0$. Going right then down sends $x$ to $0$; by commutativity, going down then right also sends $x$ to $0$, i.e. $(\operatorname{id}_M\otimes_R g)(\text{down}(x)) = 0$. The bottom arrow is injective, so $\text{down}(x) = 0$; the left vertical is an isomorphism, so $x = 0$. Hence the top arrow is injective.
>
> Therefore $\operatorname{id}_{S\otimes_R M}\otimes_S g$ is injective for every $S$-injection $g$, so $S \otimes_R M$ is a flat $S$-module. $\blacksquare$
>
> **Corollary (localization).** Apply the theorem to $f : R \to T^{-1}R$: since $R$ is flat over itself, $T^{-1}R = T^{-1}R \otimes_R R$ is flat over $T^{-1}R$ — and tracing the same diagram with $M$ flat over $R$ shows $T^{-1}M = T^{-1}R\otimes_R M$ is flat over $T^{-1}R$. In particular $T^{-1}R$ is a flat $R$-module (apply to $S = T^{-1}R$, $M = R$, viewing $T^{-1}R$ as an $R$-module).

---

# Cross-Field Exercise Suggestions

**Flatness of $\mathbb{Q}$ over $\mathbb{Z}$ as a base change.** The localization $\mathbb{Q} = (\mathbb{Z}\setminus 0)^{-1}\mathbb{Z}$ is extension of scalars along $\mathbb{Z} \to \mathbb{Q}$, so the corollary makes $\mathbb{Q}$ flat over $\mathbb{Z}$ with no direct tensor computation. The application is nonobvious because the standard "every tensor in $\mathbb{Q}\otimes V$ is pure" proof is replaced by a one-line appeal to base change of the flat module $\mathbb{Z}$.

**Complexifying a flat real module.** For a flat $\mathbb{R}$-module $M$, the complexification $\mathbb{C}\otimes_\mathbb{R} M$ is flat over $\mathbb{C}$ by the theorem (base change along $\mathbb{R}\hookrightarrow\mathbb{C}$). The application is nonobvious because it guarantees flatness of complexified families in real algebraic geometry without re-checking injectivity over $\mathbb{C}$ — exactly the stability that lets one pass between real and complex points.

**Fibres of a flat family are flat over the residue ring.** Reducing a flat $R$-module $M$ modulo a prime, $(R/\mathfrak p)\otimes_R M = M/\mathfrak p M$, is flat over $R/\mathfrak p$ by base change along $R \to R/\mathfrak p$. The application is nonobvious because it shows flatness propagates *down* to fibres' base rings, a compatibility used pervasively when studying how a flat family restricts over subvarieties.

---

# Bridges

- **[[Def - Restriction and Extension of Scalars|Extension of Scalars]]** — the functor whose flatness-preservation this theorem asserts. Extension of scalars $S \otimes_R(-)$ is the algebra of base change / pullback; the theorem says this geometric operation respects the geometric condition of flatness, which is what makes flatness a sensible hypothesis on families.

- **[[Def - Flat Module|Flat Module]]** — the property being preserved, used exactly once (on the bottom row). The whole proof is the observation that base change relabels an $S$-injectivity question as the $R$-injectivity question that flatness of $M$ already answers.

- **Localization is exact** — the headline corollary. Localization $T^{-1}R\otimes_R(-)$ is extension of scalars along $R \to T^{-1}R$, so this theorem makes $T^{-1}R$ flat, which is the precise statement that *localizing preserves injections* — the engine of the local–global principle and of the whole [[Commutative Algebra IV — Localization|localization chapter]].

- **Transitivity of flatness** — combine with itself along $R \to S \to S'$ using $S'\otimes_S(S\otimes_R M)\cong S'\otimes_R M$: a flat module stays flat up a tower of base changes, and a composite of flat ring maps is flat. This is the closure property that lets flatness be carried through multi-step constructions.

---

# Unlocked by This

> [!tip] Flat morphisms and base change of schemes *(from Algebraic Geometry)*
> A flat $R$-module base-changes to a flat $S$-module, which says geometrically that **pulling back a flat family along any map of bases keeps it flat** — the stability that makes flat morphisms $\operatorname{Spec} S \to \operatorname{Spec} R$ the right notion of a "continuous family of fibres." This is the hypothesis under which cohomology-and-base-change theorems hold and fibre dimensions stay controlled.

> [!tip] Faithfully flat descent *(from Algebraic Geometry)*
> When $S$ is moreover **faithfully flat** over $R$, the implication can be run backwards: flatness (and many other properties) of a module can be *checked after base change to $S$ and descended* to $R$. Faithfully flat descent is the engine gluing local algebraic data into global geometry, underpinning the fppf and étale topologies — and it begins with this theorem's stability of flatness under base change.
