---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - The I-adic Completion"
  - "Def - Noetherian Ring"
  - "Def - Finitely Generated Module"
  - "Def - Module"
  - "Def - Submodule"
  - "Def - Quotient Module"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a [[Def - Noetherian Ring|Noetherian]] ring, $\mathfrak{a}\trianglelefteq R$ an ideal, and let $M, N, P$ be [[Def - Module|R-modules]]. Write $\widehat{M}=\varprojlim_n M/\mathfrak{a}^n M$ for the [[Def - The I-adic Completion|\mathfrak{a}-adic completion]] and $\varphi:M\to\widehat{M}$ for the completion map. A sequence $0\to N\to M\to P\to0$ is **short exact** if the first map is injective, the second surjective, and the image of the first equals the kernel of the second. We write $\varprojlim^1$ for the first derived functor of inverse limit (the obstruction to right-exactness of $\varprojlim$). The full registry is on [[Commutative Algebra X — Completions and Limits]].

---

# Statement

> **Theorem (exactness of completion).** Let $R$ be Noetherian and $\mathfrak{a}\trianglelefteq R$. The $\mathfrak{a}$-adic completion functor $M\mapsto\widehat{M}$ is **exact on the category of finitely generated $R$-modules**: for every short exact sequence
> $$0\to N\to M\to P\to0$$
> of finitely generated $R$-modules, the completed sequence
> $$0\to\widehat{N}\to\widehat{M}\to\widehat{P}\to0$$
> is short exact. Equivalently, completion preserves injections, surjections, kernels, cokernels, and images; in particular for a submodule $N\subseteq M$,
> $$\widehat{N}=\ker\big(\widehat{M}\to\widehat{P}\big)\quad\text{and}\quad\widehat{M}/\widehat{N}\cong\widehat{M/N}.$$

> **Corollary (flat base change form).** Under the same hypotheses, $\widehat{M}\cong\widehat{R}\otimes_R M$ and $\widehat{R}$ is a flat $R$-module, so completion equals base change to $\widehat{R}$ and the exactness above is flatness of $\widehat{R}$.

The slogan: **completing a quotient is the quotient of the completions — the formal disk of $M/N$ is the formal disk of $M$ modulo that of $N$.**

---

# Motivation

To compute with completions you need to know they respect the basic constructions: if you complete a submodule and a quotient, do they fit together into a short exact sequence, or does completion scramble the relationship? For an arbitrary inverse limit the answer is *no* — $\varprojlim$ is only left exact, and a surjection of inverse systems can fail to give a surjection of limits. This is not a pedantic worry: it is the difference between completion being a usable tool and a trap. If $\widehat{M}\to\widehat{P}$ could fail to be surjective, then "$\widehat{M/N}=\widehat{M}/\widehat{N}$" would be false and every computation that completes a quotient would be wrong.

This theorem says that in the right setting — Noetherian ring, finitely generated modules — the pathology does not occur: completion is genuinely exact, as exact as localization. The reason is a single structural fact: the inverse systems $(N/\mathfrak{a}^n N)$ that arise satisfy the **Mittag-Leffler condition**, so the obstruction $\varprojlim^1$ vanishes and left-exactness upgrades to full exactness. The Mittag-Leffler condition is forced by the [[Thm - The Artin-Rees Lemma|Artin–Rees lemma]], which is where Noetherianity is spent. The payoff is the flat-base-change form: $\widehat{M}=\widehat{R}\otimes_R M$, so completion is computed by tensoring, an operation with transparent rules, and $\widehat{R}$ joins $S^{-1}R$ in the small family of flat ring extensions one may pass to freely. This is what makes $\widehat{R}$-module theory a faithful mirror of $R$-module theory.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is "$R$ Noetherian and the modules finitely generated". The disguised sources are the situations where exactness of completion is what you actually need.

The first disguised source is **"compute the completion of a quotient ring or module"**. The property $B$ is "$M/N$ appears and you want $\widehat{M/N}$". The bridge is the theorem's identity $\widehat{M/N}=\widehat{M}/\widehat{N}$: complete numerator and denominator separately and divide. The non-obviousness is that you may *not* in general interchange completion and quotient — it is exactly this theorem that licenses it, and only under the hypotheses. *Example problem:* $\widehat{(k[x,y]/(xy))}^{(x,y)}=k[[x,y]]/(xy)$, the formal node.

The second disguised source is **"a presentation $R^p\to R^q\to M\to0$ is given"**. The property $B$ is "$M$ has an explicit finite presentation". The bridge is right-exactness of completion: complete the presentation to $\widehat{R}^p\to\widehat{R}^q\to\widehat{M}\to0$, so $\widehat{M}$ is the cokernel of the *completed* presentation matrix. The non-obviousness is that an inverse limit is computed by linear algebra over $\widehat{R}$. *Example problem:* compute $\widehat{M}$ for $M=R/(f)$ as $\widehat{R}/(f)$.

The third disguised source is **"a regular sequence or Koszul complex is in play"**. The property $B$ is "an exact complex of f.g. free modules". The bridge is that completion preserves exactness, so the completed Koszul complex is still a resolution. The non-obviousness is that depth and regularity, defined by exactness of Koszul complexes, are preserved under completion. *Example problem:* show $x_1,\dots,x_d$ regular in $R$ stays regular in $\widehat{R}$.

**Targets (Output Amplification)**

The conclusions are "$0\to\widehat{N}\to\widehat{M}\to\widehat{P}\to0$ exact", "$\widehat{M}=\widehat{R}\otimes_R M$", and "$\widehat{R}$ flat".

Combine **exactness with a free resolution** to compute $\mathrm{Tor}$ and $\mathrm{Ext}$ after completion. The additional structure $D$ is a free resolution of $M$. The result $E$ is $\widehat{R}\otimes_R\mathrm{Tor}_i^R(M,N)=\mathrm{Tor}_i^{\widehat{R}}(\widehat{M},\widehat{N})$ — derived functors commute with completion for f.g. modules. Nonobvious because it lets homological invariants be computed on the formal disk.

Combine **the quotient identity with $\mathfrak{a}$-primary ideals** to study completion of ideals. The additional data $D$ is an ideal $I\subseteq R$. The result $E$ is $\widehat{R/I}=\widehat{R}/I\widehat{R}$ and $\widehat{I}=I\widehat{R}$, so ideal-theoretic structure (primary decomposition, associated primes) transports to $\widehat{R}$. Nonobvious because it says completing does not create or merge ideal components.

Combine **flatness with faithful flatness in the local case** to descend properties. The additional fact $D$ is that $\widehat{R}$ is *faithfully* flat over a Noetherian local $R$. The result $E$ is that a module is zero, a sequence exact, an element a non-zero-divisor, iff the same holds after completion — descent. Nonobvious because it lets hard local statements be checked on the simpler complete ring and pulled back.

---

# Why Is It True

Left-exactness is free and general: $\varprojlim$ always preserves kernels, because a thread in a kernel is a kernel of threads. So given $0\to N\to M\to P\to0$, applying completion always yields an exact $0\to\widehat{N}\to\widehat{M}\to\widehat{P}$. The *only* thing that can fail is surjectivity of $\widehat{M}\to\widehat{P}$ — and that failure is measured precisely by $\varprojlim^1$ of the system of kernels $(N/\mathfrak{a}^n N)$.

**Completion is left-exact for free, and the only obstruction to full exactness — $\varprojlim^1$ of the submodule's filtration — is killed by Artin–Rees, which is where Noetherian is spent.**

Why does $\varprojlim^1$ vanish here? The Mittag-Leffler condition says: for each $n$, the images of the transition maps $N/\mathfrak{a}^m N\to N/\mathfrak{a}^n N$ stabilise as $m\to\infty$. For the *intrinsic* $\mathfrak{a}$-adic filtration on $N$ this is automatic — the maps are surjective. The subtlety is that inside the sequence the relevant filtration on $N$ is not the intrinsic one but the one *induced from $M$*: $N\cap\mathfrak{a}^n M$ rather than $\mathfrak{a}^n N$. These two filtrations are generally different, and surjectivity of $\widehat{M}\to\widehat{P}$ requires them to be **comparable** — to define the same topology on $N$. That comparability is exactly the content of the [[Thm - The Artin-Rees Lemma|Artin–Rees lemma]]: $N\cap\mathfrak{a}^n M=\mathfrak{a}^{n-c}(N\cap\mathfrak{a}^c M)$ for $n\geq c$, so the induced filtration is $\mathfrak{a}$-adic up to a bounded shift, hence Mittag-Leffler, hence $\varprojlim^1=0$. Noetherianity is what makes Artin–Rees true, and finite generation is what makes the shift $c$ finite.

The flat-base-change corollary is then the same content repackaged. Once completion is exact and agrees with $\widehat{R}\otimes_R(-)$ on free modules (trivially), the five-lemma forces agreement on all finitely generated modules, and an exact functor of the form $\widehat{R}\otimes_R(-)$ is precisely a flat module $\widehat{R}$. So "completion is exact" and "$\widehat{R}$ is flat" are two faces of one theorem, both resting on Artin–Rees. The geometric reading: passing to the formal disk neither creates nor destroys linear relations among finitely many generators, exactly as restricting to a Zariski-open does not — flatness is "no surprises in the fibres".

---

# What Makes This Hard

The trap is believing exactness is automatic, by false analogy with localization. Localization is exact for an *elementary* reason (fractions never manufacture relations), but completion is exact only for a *subtle* reason: $\varprojlim$ is **not** exact in general, and the surjectivity at the right end genuinely fails for badly-behaved inverse systems (the standard counterexample is $\mathbb{Z}\xleftarrow{p}\mathbb{Z}\xleftarrow{p}\cdots$, whose limit is $0$ but which sits in a short exact sequence whose other limits are non-zero). The non-obvious step is recognising that the filtration *induced* on a submodule $N$ from $M$ — namely $N\cap\mathfrak{a}^n M$ — is what must be controlled, and that the [[Thm - The Artin-Rees Lemma|Artin–Rees lemma]] is precisely the tool that controls it. The most common error is to use the intrinsic filtration $\mathfrak{a}^n N$ without checking it agrees with the induced one; without Artin–Rees (i.e. without Noetherian + f.g.) they can differ and exactness fails.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Establish left-exactness for free (general $\varprojlim$). Reduce surjectivity at the right end to vanishing of $\varprojlim^1$ of the induced-filtration system on $N$. Invoke Artin–Rees to show the induced filtration is $\mathfrak{a}$-adic up to a shift, giving Mittag-Leffler and $\varprojlim^1=0$. Deduce the flat-base-change form from exactness plus the free-module case.

**Subgoal decomposition:**

1. **Left-exactness.** Show $0\to\widehat{N}\to\widehat{M}\to\widehat{P}$ is always exact.
   - *Hint:* $\varprojlim$ preserves kernels; a thread in $\ker$ is a $\ker$ of threads.
   - *Why needed:* It gives everything except right-end surjectivity.

2. **Surjectivity criterion.** Show $\widehat{M}\to\widehat{P}$ is surjective iff $\varprojlim^1(N\cap\mathfrak{a}^n M)_n=0$.
   - *Hint:* The $\varprojlim$ exact sequence of the system $0\to(N\cap\mathfrak{a}^n M)\to\mathfrak{a}^n M\to\dots$ has its last map's cokernel governed by $\varprojlim^1$.
   - *Why needed:* It localises the difficulty into one derived-functor term.

3. **Artin–Rees gives Mittag-Leffler.** Show the induced filtration $(N\cap\mathfrak{a}^n M)$ is $\mathfrak{a}$-adic up to a shift, hence Mittag-Leffler, hence $\varprojlim^1=0$.
   - *Hint:* [[Thm - The Artin-Rees Lemma|Artin–Rees]]: $N\cap\mathfrak{a}^n M=\mathfrak{a}^{n-c}(N\cap\mathfrak{a}^c M)$ for $n\geq c$.
   - *Why needed:* It kills the obstruction; this is where Noetherian enters.

4. **Flat base change.** Deduce $\widehat{M}=\widehat{R}\otimes_R M$ and $\widehat{R}$ flat.
   - *Hint:* Exactness + agreement on free modules + five-lemma; an exact $\widehat{R}\otimes(-)$ means $\widehat{R}$ flat.
   - *Why needed:* It is the working corollary.

---

# Lemma Decomposition

> [!note]- Lemma 1: Inverse limit is left exact
> **Statement:** For a short exact sequence of inverse systems $0\to(A_n)\to(B_n)\to(C_n)\to0$, the sequence $0\to\varprojlim A_n\to\varprojlim B_n\to\varprojlim C_n$ is exact.
>
> **Hint:** A thread is a kernel element levelwise; check directly.
>
> **Why needed:** It supplies injectivity and exactness in the middle for free, leaving only right-end surjectivity.
>
> > [!note]- Full proof
> > Injectivity of $\varprojlim A_n\to\varprojlim B_n$: a thread $(a_n)$ mapping to $0$ has each $a_n\mapsto0$ in $B_n$, so each $a_n=0$ by injectivity at level $n$. Exactness at $\varprojlim B_n$: a thread $(b_n)$ mapping to $0$ in $\varprojlim C_n$ has each $b_n\in\ker(B_n\to C_n)=\mathrm{im}(A_n\to B_n)$, so $b_n=$ image of a unique $a_n\in A_n$; uniqueness makes $(a_n)$ a thread, giving the preimage. Hence $0\to\varprojlim A_n\to\varprojlim B_n\to\varprojlim C_n$ is exact. (Surjectivity onto $\varprojlim C_n$ need not hold — that is the $\varprojlim^1$ obstruction.)

> [!note]- Lemma 2: The induced filtration is $\mathfrak{a}$-adic up to a shift (Artin–Rees)
> **Statement:** For a submodule $N\subseteq M$ of a finitely generated module over a Noetherian ring, there is $c\geq0$ with $N\cap\mathfrak{a}^n M=\mathfrak{a}^{n-c}(N\cap\mathfrak{a}^c M)$ for all $n\geq c$.
>
> **Hint:** This is exactly [[Thm - The Artin-Rees Lemma|Artin–Rees]].
>
> **Why needed:** It shows the induced filtration on $N$ defines the same topology as the $\mathfrak{a}$-adic one, giving Mittag-Leffler.
>
> > [!note]- Full proof
> > This is the [[Thm - The Artin-Rees Lemma|Artin–Rees lemma]], proved via the Rees algebra in the [[Commutative Algebra XI — Graded Rings and the Artin-Rees Lemma|next chapter]]. Its consequence here: the two filtrations $(\mathfrak{a}^n N)$ and $(N\cap\mathfrak{a}^n M)$ on $N$ satisfy $\mathfrak{a}^n N\subseteq N\cap\mathfrak{a}^n M\subseteq\mathfrak{a}^{n-c}N$ for $n\geq c$, so each is cofinal in the other — they define the same topology on $N$, and the system $(N/(N\cap\mathfrak{a}^n M))$ has surjective transition maps with stabilising images, i.e. it is Mittag-Leffler.

> [!note]- Lemma 3: Mittag-Leffler kills $\varprojlim^1$ and gives surjectivity
> **Statement:** If $(A_n)$ satisfies the Mittag-Leffler condition (the images $\mathrm{im}(A_m\to A_n)$ stabilise as $m\to\infty$, for each $n$), then $\varprojlim^1 A_n=0$, and the right map $\varprojlim B_n\to\varprojlim C_n$ in Lemma 1 is surjective.
>
> **Hint:** A compatible thread in $(C_n)$ is lifted level by level using the stabilised images; the stabilisation removes the obstruction to extending the lift.
>
> **Why needed:** It converts the Artin–Rees consequence into the surjectivity that completes exactness.
>
> > [!note]- Full proof
> > Given a thread $(c_n)\in\varprojlim C_n$, lift each $c_n$ to $b_n\in B_n$; the threads fail to be compatible only by elements of $A_n$, i.e. the discrepancy $b_n-(\text{image of }b_{n+1})$ lies in $\mathrm{im}(A_{n+1}\to A_n)$. Under Mittag-Leffler these images stabilise, so one can correct the lifts successively without an ever-growing error — the corrections form a convergent (Mittag-Leffler) scheme producing a compatible thread $(b_n')\in\varprojlim B_n$ mapping to $(c_n)$. Hence $\varprojlim B_n\to\varprojlim C_n$ is surjective and $\varprojlim^1 A_n=0$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be Noetherian, $\mathfrak{a}\trianglelefteq R$, and $0\to N\xrightarrow{i} M\xrightarrow{\pi} P\to0$ a short exact sequence of finitely generated $R$-modules.
>
> ---
> **Step 0 — the relevant inverse systems.** Tensoring the sequence with $R/\mathfrak{a}^n$ is right exact, giving $M/\mathfrak{a}^n M\to P/\mathfrak{a}^n P\to0$ with kernel the image of $N$; precisely, the kernel of $M/\mathfrak{a}^n M\to P/\mathfrak{a}^n P$ is $(N+\mathfrak{a}^n M)/\mathfrak{a}^n M\cong N/(N\cap\mathfrak{a}^n M)$. So the relevant short exact sequence of inverse systems is
> $$0\to\big(N/(N\cap\mathfrak{a}^n M)\big)_n\to\big(M/\mathfrak{a}^n M\big)_n\to\big(P/\mathfrak{a}^n P\big)_n\to0.$$
>
> ---
> **Step 1 — left exactness.** By Lemma 1, applying $\varprojlim$ gives the exact $0\to\varprojlim N/(N\cap\mathfrak{a}^n M)\to\widehat{M}\to\widehat{P}$.
>
> ---
> **Step 2 — the first term is $\widehat{N}$.** By [[Thm - The Artin-Rees Lemma|Artin–Rees]] (Lemma 2), the filtration $(N\cap\mathfrak{a}^n M)$ on $N$ is cofinal with the $\mathfrak{a}$-adic filtration $(\mathfrak{a}^n N)$, so $\varprojlim N/(N\cap\mathfrak{a}^n M)\cong\varprojlim N/\mathfrak{a}^n N=\widehat{N}$. Hence $0\to\widehat{N}\to\widehat{M}\to\widehat{P}$ is exact.
>
> ---
> **Step 3 — surjectivity on the right.** By Lemma 2 the system $(N/(N\cap\mathfrak{a}^n M))$ is Mittag-Leffler, so by Lemma 3 its $\varprojlim^1$ vanishes and $\widehat{M}\to\widehat{P}$ is surjective. Therefore
> $$0\to\widehat{N}\to\widehat{M}\to\widehat{P}\to0$$
> is short exact: completion is exact on finitely generated modules. Taking $P=M/N$ gives $\widehat{M/N}\cong\widehat{M}/\widehat{N}$.
>
> ---
> **Corollary — flat base change.** The natural map $\widehat{R}\otimes_R M\to\widehat{M}$ is an isomorphism on free modules and both functors are right exact; by the five-lemma applied to a finite presentation, it is an isomorphism for all finitely generated $M$. Exactness of $\widehat{(-)}$ then says $\widehat{R}\otimes_R(-)$ is exact on f.g. modules, i.e. $\widehat{R}$ is flat over $R$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Completion and homology of a filtered complex.** A filtered chain complex completes to $\widehat{C_\bullet}$, and exactness of completion (for f.g. terms over Noetherian $R$) means $H_i(\widehat{C_\bullet})=\widehat{H_i(C_\bullet)}$ — homology commutes with completion. This is the input to convergence theorems for the spectral sequence of a filtered complex. The application is nonobvious because "homology commutes with completion" is exactly the exactness of this theorem applied to cycles and boundaries.

**Formal smoothness and the cotangent complex.** A map is formally smooth iff a certain lifting problem along nilpotent thickenings is solvable, a condition tested by completing at points; exactness of completion is what guarantees the obstruction module (a piece of the cotangent complex) is computed correctly after completion. The application is nonobvious because deformation obstructions are a $\mathrm{Ext}$ group, and this theorem is what makes $\mathrm{Ext}$ commute with completion.

**$p$-adic interpolation of modular forms.** Families of modular forms are encoded by modules over $\mathbb{Z}_p[[T]]$, and the exactness of $p$-adic completion is what allows congruences between forms (statements mod $p^n$ for all $n$) to be assembled into a single statement over the completed Hecke algebra. The application is nonobvious because "interpolate a family across all $p^n$" is the inverse-limit exactness made arithmetic.

---

# Bridges

- **[[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]]** — the engine of the whole theorem. It says the filtration a submodule inherits from its ambient module is $\mathfrak{a}$-adic up to a bounded shift, which is precisely the Mittag-Leffler condition that makes $\varprojlim^1$ vanish and completion exact. Every use of Noetherianity in this theorem flows through Artin–Rees; without it, exactness fails and $\widehat{M/N}\neq\widehat{M}/\widehat{N}$.

- **[[Thm - The Completion of a Noetherian Ring is Noetherian|Completion of a Noetherian Ring is Noetherian]]** — the companion theorem. Parts 2 and 3 of that theorem (flatness and $\widehat{M}=\widehat{R}\otimes M$) are the same content as the corollary here; the two pages develop the same flatness from the same Artin–Rees input, one emphasising Noetherianity, the other exactness. Together they constitute the "completion behaves like localization" package.

- **[[Commutative Algebra IV — Localization|Localization]] (exactness of $S^{-1}$)** — the parallel, and the contrast. Localization is exact for an elementary reason; completion is exact only via Artin–Rees and the vanishing of $\varprojlim^1$. The two exactness theorems have the same *statement* (a flat base change) but profoundly different *proofs* — the difference between an algebraic localization and an infinite limit.

- **$\varprojlim^1$ and derived inverse limits (homological algebra)** — the framework that makes the obstruction precise. The failure of $\varprojlim$ to be right exact is the functor $\varprojlim^1$; this theorem is the statement that $\varprojlim^1$ vanishes for the $\mathfrak{a}$-adic systems of f.g. modules over Noetherian rings, via Mittag-Leffler. Outside that range, $\varprojlim^1$ is non-zero and one must use *derived* completion.

---

# Unlocked by This

> [!tip] Faithfully flat descent from the formal disk *(from Algebraic Geometry)*
> For a Noetherian local ring, the completion $R\to\widehat{R}$ is **faithfully flat**, so exactness can be both pushed up and pulled back: a sequence of f.g. modules is exact iff it is exact after completion. This **faithfully flat descent** lets one prove statements about a variety — a module is zero, a map injective, an ideal radical — by passing to the formal disk, where the ring is a power-series quotient and far simpler, then descending the conclusion. It is one of the most-used techniques in local algebraic geometry, and it is exactly the exactness of this theorem upgraded by the non-vanishing of $\widehat{R}\otimes_R k$.

> [!tip] Comparison of formal and analytic / coherent cohomology *(from Algebraic Geometry)*
> Because completion is exact and commutes with finite presentations, the cohomology of a coherent sheaf along a subscheme can be computed on the **formal completion** — this is the content of the formal-functions theorem and Grothendieck's comparison of formal and algebraic coherent cohomology. The exactness proved here is the local input that makes the global comparison work: completing a resolution stays a resolution, so derived functors are preserved, and formal-analytic GAGA-type theorems become available.
