---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Direct and Inverse Limits"
  - "Def - The I-adic Completion"
  - "Def - Ideal"
  - "Def - Module"
  - "Def - Noetherian Ring"
  - "Def - Local Ring and Residue Field"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. Let $R$ be a ring, $\mathfrak{a}\trianglelefteq R$ an [[Def - Ideal|ideal]], $M$ an [[Def - Module|$R$-module]]. Write $\widehat{M}=\varprojlim_n M/\mathfrak{a}^n M$ for the [[Def - The I-adic Completion|$\mathfrak{a}$-adic completion]], $\varphi=\varphi_M:M\to\widehat{M}$, $m\mapsto(m+\mathfrak{a}^n M)_n$ for the completion map, and $\mathrm{Jac}(R)$ for the Jacobson radical (the intersection of all maximal ideals). A ring or module is **complete** (for the $\mathfrak{a}$-adic topology) if $\varphi$ is an isomorphism. The full registry is on [[Commutative Algebra X — Completions and Limits]].

---

# Statement

> **Theorem (kernel of completion and completeness).** Let $R$ be a ring, $\mathfrak{a}\trianglelefteq R$, and $M$ an $R$-module, with completion map $\varphi:M\to\widehat{M}$.
>
> 1. **(Kernel formula.)** $\displaystyle\ker\varphi=\bigcap_{n\geq0}\mathfrak{a}^n M$. In particular $\varphi$ is injective if and only if $\bigcap_n\mathfrak{a}^n M=0$.
> 2. **(Injectivity in the good case.)** If $R$ is [[Def - Noetherian Ring|Noetherian]], $M$ is [[Def - Finitely Generated Module|finitely generated]], and $\mathfrak{a}\subseteq\mathrm{Jac}(R)$ (e.g. $(R,\mathfrak{m})$ local with $\mathfrak{a}=\mathfrak{m}$, or $R$ a Noetherian domain with $\mathfrak{a}$ proper and $M=R$), then $\varphi$ is injective.
> 3. **(Idempotence / completeness.)** The completion is complete: the natural map $\widehat{M}\to\widehat{\widehat{M}}$ is an isomorphism, equivalently $\widehat{\mathfrak{a}^n\widehat{M}}$-truncations of $\widehat{M}$ recover $\widehat{M}$. In particular $\widehat{\widehat{R}}=\widehat{R}$.

> **Corollary (the completion topology).** The sets $\mathfrak{a}^n M$ are a neighbourhood basis of $0$ for a topology (the **$\mathfrak{a}$-adic topology**) making $M$ a topological module; $\widehat{M}$ is its Hausdorff completion, and $\varphi$ is the canonical map. $\varphi$ is injective iff the topology is Hausdorff (separated), i.e. $\bigcap_n\mathfrak{a}^n M=0$.

---

# Motivation

The completion is built by an abstract machine — the inverse limit — and before using it one must know two things: *how faithfully it remembers the original module*, and *whether it is a fixed point of its own construction*. This theorem answers both. The first answer is the kernel formula, which is the single most-used fact in the chapter: it locates the exact information completion destroys, namely the elements lying in *every* power $\mathfrak{a}^n M$. These are the "infinitely $\mathfrak{a}$-divisible" elements — they look like zero to every finite-order approximation, so the completion, which only knows the approximations, cannot tell them from zero. Whether there are any such elements is then the whole question of injectivity, and part 2 says that in the world where commutative algebra actually lives — Noetherian rings, finitely generated modules, ideals inside the radical — there are none, so $M$ embeds in its formal disk.

The second answer, completeness, is what justifies the word "completion". Completing a space should be like taking the closure: once done, doing it again changes nothing, because all the limits are already present. The reals are complete and re-completing them gives the reals; $\mathbb{Z}_p$ is complete and re-completing it gives $\mathbb{Z}_p$. Part 3 is the algebraic form of this, and it is what lets us treat $\widehat{R}$ as a genuine new ground ring to work over rather than an intermediate object that might still be missing elements. Together the three parts certify that completion is a faithful (in the good case) idempotent operation — the prerequisite for everything built on top of it.

---

# Sources and Targets

**Sources (Input Broadening)**

The injectivity statement (part 2) requires the precondition $A$: "$\bigcap_n\mathfrak{a}^n M=0$". Several common hypotheses $B$ deliver it, often non-obviously.

The first disguised source is **"$R$ is a Noetherian local ring and $\mathfrak{a}=\mathfrak{m}$"**. The property $B$ is local Noetherianity. The bridge is the [[Thm - The Krull Intersection Theorem|Krull intersection theorem]]: over a Noetherian ring with $\mathfrak{a}\subseteq\mathrm{Jac}(R)$, every finitely generated module has $\bigcap\mathfrak{a}^n M=0$, and in a local ring $\mathfrak{m}$ *is* the Jacobson radical, so the hypothesis is automatic. The non-obvious part is that a *finiteness* condition on ideals (Noetherian) forces an *intersection* of infinitely many submodules to vanish — the link is Artin–Rees. *Example problem:* show the completion map $R\to\widehat{R}$ is injective for $R=k[x,y]_{(x,y)}$, hence $k[x,y]_{(x,y)}\hookrightarrow k[[x,y]]$.

The second disguised source is **"$R$ is a Noetherian domain and $\mathfrak{a}$ is a proper ideal"** (ES4 Q15's note). Here $B$ is "domain, not necessarily local". The bridge is again Krull intersection, now in the form that for a Noetherian domain the intersection $\bigcap\mathfrak{a}^n$ is an ideal $I$ with $\mathfrak{a}I=I$, and an element of $1+\mathfrak{a}$ annihilates $I$; in a domain that forces $I=0$. The non-obviousness: domains are not local, so $\mathfrak{a}$ need not be in the radical, yet the conclusion survives because no non-zero element of a domain can be killed. *Example problem:* $\mathbb{Z}\hookrightarrow\mathbb{Z}_p$ and $k[T]\hookrightarrow k[[T]]$ are injective.

The third disguised source is **"$\mathfrak{a}$ is generated by a non-zero-divisor in a Noetherian domain, or $M$ is $\mathfrak{a}$-adically separated by hypothesis"**. The property $B$ is a separation assumption stated up front. The bridge is the corollary: $\varphi$ injective $\iff$ the $\mathfrak{a}$-adic topology is Hausdorff $\iff\bigcap\mathfrak{a}^n M=0$, so any hypothesis guaranteeing Hausdorffness (e.g. $M$ is a submodule of a separated module) gives injectivity. *Example problem:* prove a submodule of $\widehat{R}$ is separated, hence its own completion embeds.

**Targets (Output Amplification)**

The conclusions are "$\ker\varphi=\bigcap\mathfrak{a}^n M$", "$\varphi$ injective", and "$\widehat{\widehat{M}}=\widehat{M}$".

Combine the **kernel formula with the existence of a non-zero infinitely-divisible element**. If you can exhibit $0\neq m\in\bigcap_n\mathfrak{a}^n M$, then $\varphi$ is *not* injective and completion genuinely loses information. The further result $E$ is a *negative* diagnostic — completion is a poor invariant for the module in question — and it is the standard way to show that some non-Noetherian or non-finitely-generated situation is pathological. This is nonobvious because injectivity is the default expectation; the kernel formula is the tool that locates the counterexample.

Combine **injectivity with completeness** to get $M\hookrightarrow\widehat{M}$ as a *dense* embedding into a complete module. The further result $E$ is that $\widehat{M}$ is the smallest complete module containing $M$ — its Cauchy completion — so any $\mathfrak{a}$-adically continuous map out of $M$ extends uniquely to $\widehat{M}$. This is the engine behind extending $\mathbb{Z}$-valued functions to $\mathbb{Z}_p$-valued ones and is nonobvious because it upgrades an algebraic injection to a topological universal property.

Combine **completeness with unit-detection** ([[Def - The I-adic Completion|units are detected mod $\mathfrak{a}$]]) to invert elements by geometric series. If $u\equiv1\pmod{\mathfrak{a}}$ then $u^{-1}=\sum_n(1-u)^n$ converges in $\widehat{R}$. The further result $E$ is that $\widehat{R}$ has *many more units* than $R$ — every element congruent to a unit mod $\mathfrak{a}$ — which is why $\widehat{R}$ is local with maximal ideal $\widehat{\mathfrak{a}}$ and why Hensel lifting works. Nonobvious because the new units are limiting elements with no finite expression.

---

# Why Is It True

Start with the kernel formula, which is pure unwinding of the inverse-limit definition. An element of $\widehat{M}=\varprojlim M/\mathfrak{a}^n M$ is a thread $(m+\mathfrak{a}^n M)_n$, and the completion map sends $m$ to its own thread. That thread is the zero thread exactly when $m+\mathfrak{a}^n M=0$ in $M/\mathfrak{a}^n M$ for *every* $n$, i.e. $m\in\mathfrak{a}^n M$ for every $n$, i.e. $m\in\bigcap_n\mathfrak{a}^n M$. There is no content here beyond reading the definition — but it reframes the soft question "does completion forget anything?" as the sharp question "is any non-zero element swallowed by every power of $\mathfrak{a}$?", and that is a question algebra can answer.

**The kernel of completion is exactly the set of elements no finite-order observer can distinguish from zero — and Krull's theorem says, in the Noetherian local world, that set is $\{0\}$.**

Why should the intersection vanish in the good case? Intuitively, an element of $\bigcap\mathfrak{a}^n M$ is "infinitely divisible by the small ideal $\mathfrak{a}$" — it is smaller than any order. Over $\mathbb{Z}$ at $(p)$ this would be an integer divisible by $p^n$ for all $n$, which only $0$ can be, because a non-zero integer has a finite $p$-adic valuation. The general statement is the same with "valuation" replaced by the structure theory: in a Noetherian ring, the intersection $I=\bigcap\mathfrak{a}^n M$ satisfies $\mathfrak{a}I=I$ (this is the Artin–Rees consequence), and Nakayama-type reasoning — an element of $1+\mathfrak{a}$ kills $I$ — forces $I=0$ when $\mathfrak{a}$ is in the radical or the ring is a domain. The finiteness (Noetherian + f.g.) is what makes Artin–Rees available; without it, infinitely-divisible elements can persist, as in the idempotent example $\mathfrak{a}^2=\mathfrak{a}$.

Completeness is even more transparent once you picture threads. An element of $\widehat{\widehat{M}}$ is a thread *of threads* — a compatible family of truncations of $\widehat{M}$. But a truncation $\widehat{M}/\mathfrak{a}^n\widehat{M}$ is already just $M/\mathfrak{a}^n M$ (completing and then truncating to order $n$ recovers the order-$n$ data, because the higher-order corrections die mod $\mathfrak{a}^n$). So a thread of threads is the same data as a single thread, and $\widehat{\widehat{M}}=\widehat{M}$. The reals make the same point: a Cauchy sequence of real numbers already has a real limit, so completing $\mathbb{R}$ adds nothing — every limit you could want is present after the first completion.

---

# What Makes This Hard

The kernel formula and completeness are easy — they are definitional unwindings — so the difficulty is concentrated entirely in part 2, and specifically in the fact that injectivity is *not free*: it rests on the [[Thm - The Krull Intersection Theorem|Krull intersection theorem]], which in turn rests on [[Thm - The Artin-Rees Lemma|Artin–Rees]], both genuinely substantial and both requiring Noetherianity. The most common error is to *assume* $\varphi$ is injective by analogy with $\mathbb{Z}\hookrightarrow\mathbb{Z}_p$, forgetting that the embedding there used that $\mathbb{Z}$ is a Noetherian domain; in a non-Noetherian ring or for a non-finitely-generated module the intersection $\bigcap\mathfrak{a}^n M$ can be non-zero and completion can collapse part of $M$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Part 1 is read off the inverse-limit definition. Part 2 reduces "$\varphi$ injective" to "$\bigcap\mathfrak{a}^n M=0$" via part 1, then quotes Krull intersection (whose hypotheses you verify). Part 3 identifies a thread-of-threads with a thread by noting that truncating a completion to order $n$ recovers the order-$n$ data of the original.

**Subgoal decomposition:**

1. **Kernel formula.** Show $\ker\varphi=\bigcap_n\mathfrak{a}^n M$.
   - *Hint:* $\varphi(m)$ is the thread $(m+\mathfrak{a}^n M)_n$; it is zero iff every coordinate is zero iff $m\in\mathfrak{a}^n M$ for all $n$.
   - *Why needed:* It converts injectivity into a vanishing-intersection statement, the only thing Krull can attack.

2. **Reduce injectivity to vanishing.** $\varphi$ injective $\iff\bigcap_n\mathfrak{a}^n M=0$.
   - *Hint:* Immediate from subgoal 1; a homomorphism is injective iff its kernel is $0$.
   - *Why needed:* It is the bridge to the imported theorem.

3. **Apply Krull intersection.** Under "Noetherian + f.g. + $\mathfrak{a}\subseteq\mathrm{Jac}$", conclude $\bigcap_n\mathfrak{a}^n M=0$.
   - *Hint:* Quote [[Thm - The Krull Intersection Theorem]]; for the local case note $\mathfrak{m}=\mathrm{Jac}(R)$, for the domain case note an element of $1+\mathfrak{a}$ kills the intersection and a domain has no zero-divisors.
   - *Why needed:* It supplies the non-trivial vanishing; everything else is formal.

4. **Completeness.** Show $\widehat{\widehat{M}}=\widehat{M}$.
   - *Hint:* $\widehat{M}/\mathfrak{a}^n\widehat{M}\cong M/\mathfrak{a}^n M$, so the inverse system computing $\widehat{\widehat{M}}$ is the same as the one computing $\widehat{M}$; the limits agree.
   - *Why needed:* It is the fixed-point property justifying "completion".

---

# Lemma Decomposition

> [!note]- Lemma 1: The completion map's kernel is the infinite intersection
> **Statement:** For any $R$-module $M$ and ideal $\mathfrak{a}$, $\ker\varphi=\bigcap_{n\geq0}\mathfrak{a}^n M$.
>
> **Hint:** Read off the definition of the inverse limit; a thread is zero iff every coordinate is.
>
> **Why needed:** It is part 1 and the foundation of the injectivity criterion.
>
> > [!note]- Full proof
> > By definition $\varphi(m)=(m+\mathfrak{a}^n M)_n\in\varprojlim M/\mathfrak{a}^n M$. The zero element of the inverse limit is the thread all of whose coordinates are zero. Hence $\varphi(m)=0$ iff $m+\mathfrak{a}^n M=0_{M/\mathfrak{a}^n M}$ for every $n$, i.e. iff $m\in\mathfrak{a}^n M$ for every $n\geq0$, i.e. iff $m\in\bigcap_{n\geq0}\mathfrak{a}^n M$. Therefore $\ker\varphi=\bigcap_n\mathfrak{a}^n M$.

> [!note]- Lemma 2: Truncating the completion to order $n$ recovers $M/\mathfrak{a}^n M$
> **Statement:** The natural map $M/\mathfrak{a}^n M\to\widehat{M}/\mathfrak{a}^n\widehat{M}$ induced by $\varphi$ is an isomorphism for every $n$.
>
> **Hint:** A thread is determined mod $\mathfrak{a}^n\widehat{M}$ by its $n$-th coordinate; higher coordinates differ by elements of $\mathfrak{a}^n M$.
>
> **Why needed:** It is the engine of completeness: it makes the inverse system for $\widehat{\widehat{M}}$ coincide with that for $\widehat{M}$.
>
> > [!note]- Full proof
> > The completion map $\varphi$ induces, for each $n$, a map $M/\mathfrak{a}^n M\to\widehat{M}/\mathfrak{a}^n\widehat{M}$. Surjectivity: given a thread $x=(x_k)_k\in\widehat{M}$, its class mod $\mathfrak{a}^n\widehat{M}$ is determined by $x_n\in M/\mathfrak{a}^n M$ (lift $x_n$ to $m\in M$; then $\varphi(m)$ and $x$ agree in the first $n$ coordinates, so $x-\varphi(m)\in\mathfrak{a}^n\widehat{M}$). Injectivity: if $\varphi(m)\in\mathfrak{a}^n\widehat{M}$ then its $n$-th coordinate $m+\mathfrak{a}^n M$ is $0$, so $m\in\mathfrak{a}^n M$. Hence the map is an isomorphism $M/\mathfrak{a}^n M\cong\widehat{M}/\mathfrak{a}^n\widehat{M}$.

> [!note]- Lemma 3: Krull intersection in the local case
> **Statement:** If $(R,\mathfrak{m})$ is Noetherian local and $M$ is finitely generated, then $\bigcap_n\mathfrak{m}^n M=0$.
>
> **Hint:** Quote [[Thm - The Krull Intersection Theorem]]; the local maximal ideal is the Jacobson radical.
>
> **Why needed:** It delivers injectivity (part 2) in the most-used case.
>
> > [!note]- Full proof
> > Set $I=\bigcap_n\mathfrak{m}^n M$. By the [[Thm - The Artin-Rees Lemma|Artin–Rees lemma]] applied to the submodule $I\subseteq M$ with the $\mathfrak{m}$-adic filtration, there is $c$ with $\mathfrak{m}^n M\cap I=\mathfrak{m}^{n-c}(\mathfrak{m}^c M\cap I)$ for $n\geq c$. Since $I\subseteq\mathfrak{m}^n M$ for all $n$, the left side is $I$, giving $I=\mathfrak{m}\,I$. By [[Commutative Algebra V — Nakayama's Lemma|Nakayama's lemma]] (valid because $\mathfrak{m}=\mathrm{Jac}(R)$ in a local ring and $I$ is finitely generated, being a submodule of the f.g. module $M$ over a Noetherian ring), $I=0$. This is exactly the [[Thm - The Krull Intersection Theorem|Krull intersection theorem]] in the local case.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $R$ be commutative with $1$, $\mathfrak{a}\trianglelefteq R$, $M$ an $R$-module, $\varphi:M\to\widehat{M}=\varprojlim M/\mathfrak{a}^n M$ the completion map.
>
> ---
> **Part 1 — kernel formula.** This is Lemma 1: $\varphi(m)=0$ iff $m+\mathfrak{a}^n M=0$ for all $n$ iff $m\in\bigcap_n\mathfrak{a}^n M$. Hence $\ker\varphi=\bigcap_n\mathfrak{a}^n M$, and $\varphi$ is injective iff this intersection is $0$.
>
> ---
> **Part 2 — injectivity in the good case.** By Part 1 it suffices to show $\bigcap_n\mathfrak{a}^n M=0$ under the stated hypotheses.
>
> *Local case.* If $(R,\mathfrak{m})$ is Noetherian local and $M$ f.g. with $\mathfrak{a}=\mathfrak{m}$, this is Lemma 3.
>
> *General Noetherian case with $\mathfrak{a}\subseteq\mathrm{Jac}(R)$.* Set $I=\bigcap_n\mathfrak{a}^n M$. [[Thm - The Artin-Rees Lemma|Artin–Rees]] gives $\mathfrak{a}I=I$ as in Lemma 3 (with $\mathfrak{m}$ replaced by $\mathfrak{a}$). By the general form of Nakayama, since $\mathfrak{a}\subseteq\mathrm{Jac}(R)$ and $I$ is finitely generated, $1+a$ is a unit for any $a\in\mathfrak{a}$ and the determinant trick yields $I=0$.
>
> *Domain case.* If $R$ is a Noetherian domain and $\mathfrak{a}$ proper, $M=R$: again $\mathfrak{a}I=I$ with $I=\bigcap\mathfrak{a}^n$, so by the determinant trick there is $a\in\mathfrak{a}$ with $(1+a)I=0$. As $\mathfrak{a}\neq R$, $1+a\neq0$, and $R$ is a domain, so $I=0$. Hence $\varphi$ is injective.
>
> ---
> **Part 3 — completeness.** By Lemma 2, $\widehat{M}/\mathfrak{a}^n\widehat{M}\cong M/\mathfrak{a}^n M$ for every $n$, compatibly with the projections. Therefore the inverse system $\big(\widehat{M}/\mathfrak{a}^n\widehat{M}\big)_n$ computing $\widehat{\widehat{M}}$ is isomorphic to the inverse system $\big(M/\mathfrak{a}^n M\big)_n$ computing $\widehat{M}$. Inverse limits of isomorphic systems are isomorphic, so $\widehat{\widehat{M}}\cong\widehat{M}$, and one checks the natural map $\widehat{M}\to\widehat{\widehat{M}}$ realises this isomorphism. In particular $\widehat{\widehat{R}}=\widehat{R}$. $\blacksquare$
>
> **Corollary (topology).** The submodules $\mathfrak{a}^n M$ are closed under the module operations and nested, so the cosets $\{m+\mathfrak{a}^n M\}$ form a basis for a topology (the $\mathfrak{a}$-adic topology); it is Hausdorff iff $\bigcap_n\mathfrak{a}^n M=0$ (points are separated iff no non-zero element lies in every neighbourhood of $0$), which by Part 1 is exactly injectivity of $\varphi$. $\widehat{M}$ is the Hausdorff completion in the metric sense.

---

# Cross-Field Exercise Suggestions

**Completion of the reals as the model.** The construction $\mathbb{R}=$ (Cauchy sequences of rationals)/(null sequences) is the inverse-limit completeness statement in metric clothing: $\bigcap_n(\text{balls of radius }2^{-n})=\{0\}$ is Hausdorffness (injectivity of $\mathbb{Q}\to\mathbb{R}$), and "$\mathbb{R}$ is complete" is $\widehat{\widehat{\mathbb{Q}}}=\widehat{\mathbb{Q}}$. Recognising the $\mathfrak{a}$-adic statements as the same facts with $|\cdot|_p$ in place of $|\cdot|_\infty$ is the bridge; nonobvious because the algebraic version hides the metric.

**Profinite completion of a group and the residual finiteness diagnostic.** For a group $G$, the profinite completion $\widehat{G}=\varprojlim G/N$ over finite-index normal $N$ has kernel $\bigcap_N N$, and the completion map is injective iff $G$ is *residually finite*. This is the exact group-theoretic analogue of the kernel formula, with "$\mathfrak{a}^n$" replaced by "finite-index normal subgroups". The application is nonobvious because residual finiteness — a separation property — is precisely Hausdorffness of the profinite topology.

**Power series solutions of ODEs.** Solving $y'=f(x,y)$ by a formal power series ansatz $y=\sum a_n x^n$ is a completion computation in $k[[x]]$: the recursion determines $a_n$ from $a_0,\dots,a_{n-1}$, i.e. it builds a compatible thread in $\varprojlim k[x]/(x^n)$, and completeness guarantees the thread assembles into an element of $k[[x]]$. The application is nonobvious because the "limit" of the truncated solutions is exactly the inverse-limit element, with no convergence analysis needed in the formal setting.

---

# Bridges

- **[[Thm - The Krull Intersection Theorem|Krull Intersection Theorem]]** — the theorem that powers part 2. It states $\bigcap_n\mathfrak{a}^n M=0$ for finitely generated $M$ over a Noetherian ring with $\mathfrak{a}$ in the radical (or $R$ a domain). This kernel-formula theorem *reduces* injectivity of completion to Krull intersection, and Krull intersection *supplies* the vanishing; the two are the two halves of "completion is faithful in the good case". The mechanism inside Krull is that $I=\bigcap\mathfrak{a}^n M$ satisfies $\mathfrak{a}I=I$, then Nakayama forces $I=0$.

- **[[Thm - The Artin-Rees Lemma|Artin–Rees Lemma]]** — the lemma under Krull. It says the $\mathfrak{a}$-adic filtration on a submodule $N\subseteq M$ is, up to a shift, the restriction of the filtration on $M$; this is what gives $\mathfrak{a}I=I$ and, more broadly, why $\varprojlim^1$ vanishes (Mittag-Leffler), making completion exact. Noetherianity enters here and nowhere else.

- **[[Commutative Algebra V — Nakayama's Lemma|Nakayama's Lemma]]** — the finishing move. From $\mathfrak{a}I=I$ with $I$ finitely generated and $\mathfrak{a}$ in the radical, Nakayama concludes $I=0$. This is the same determinant-trick argument that pervades local commutative algebra, here applied to the intersection module.

- **[[Commutative Algebra IV — Localization|Localization]]** — the comparison construction. Both localization and completion are "pass to a more local ring", and both are exact in good cases; but localization keeps a Zariski neighbourhood (and $R\to R_{\mathfrak{p}}$ is injective iff no element is killed by something outside $\mathfrak{p}$), while completion keeps only the formal disk (and $R\to\widehat{R}$ is injective iff no element is infinitely $\mathfrak{a}$-divisible). The kernel formulas are parallel; completion is the finer, harder-to-control of the two.

---

# Unlocked by This

> [!tip] Henselian rings and unique lifting *(from Algebraic Geometry / Number Theory)*
> Completeness (part 3) is exactly the hypothesis that makes **Hensel's lemma** run: in a complete local ring every $\mathfrak{a}$-adic Cauchy sequence converges, so Newton's iteration on a simple root produces an honest root. A ring with this lifting property is **Henselian**, and complete local rings are the primary examples. This is why $\mathbb{Z}_p$ and $k[[T]]$ behave like rings of analytic functions and why the strict Henselisation is the algebraic model of a small contractible neighbourhood in the étale topology.

> [!tip] The $\varprojlim^1$ obstruction and derived completion *(from Homological Algebra)*
> The corollary "$\varphi$ injective iff the topology is Hausdorff" is the $0$-th piece of a longer story: the failure of $\varprojlim$ to be exact is measured by $\varprojlim^1$, and the *derived completion* corrects ordinary completion when the module is not finitely generated. For Noetherian rings and f.g. modules $\varprojlim^1$ vanishes (via Artin–Rees / Mittag-Leffler), which is why this chapter's completion is so well-behaved; outside that range, derived completion is the right object.
