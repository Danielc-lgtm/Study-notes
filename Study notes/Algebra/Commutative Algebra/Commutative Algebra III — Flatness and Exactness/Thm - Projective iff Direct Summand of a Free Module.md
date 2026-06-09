---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Projective Module"
  - "Def - Free Module"
  - "Def - The Hom Functor and Left Exactness"
  - "Thm - Hom is Left Exact"
  - "Def - Flat Module"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; all modules unital. Let $R$ be a ring and $M$ an $R$-module. A surjection $\pi : F \twoheadrightarrow M$ from a [[Def - Free Module|free module]] is a **free cover**; presenting $M$ this way gives a short exact sequence $0 \to \ker\pi \to F \xrightarrow{\pi} M \to 0$. A short exact sequence $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$ **splits** if there is a section $s : C \to B$ with $gs = \operatorname{id}_C$; see [[Ex - The splitting lemma]]. We use the [[Def - The Hom Functor and Left Exactness|Hom functor]] $\operatorname{Hom}_R(M, -)$ and write $R^{\oplus I}$ for the free module on $I$. The full registry is on [[Commutative Algebra III — Flatness and Exactness]].

---

# Statement

> **Theorem (Characterizations of projectivity).** For an $R$-module $M$ the following are equivalent:
>
> 1. **(Lifting)** $M$ is [[Def - Projective Module|projective]]: every map $M \to N/N'$ to a quotient lifts through the quotient map.
> 2. **(Exactness)** The functor $\operatorname{Hom}_R(M, -)$ is exact.
> 3. **(Splitting)** Every short exact sequence $0 \to A \to B \to M \to 0$ splits.
> 4. **(Summand)** $M$ is a direct summand of a free module: there is an $R$-module $N$ with $M \oplus N \cong R^{\oplus I}$ for some index set $I$.

> **Corollary.** Every projective module is [[Def - Flat Module|flat]]: $(4)$ exhibits $M$ as a direct summand of a free (hence flat) module, and a direct summand of a flat module is flat.

The pivot of the proof is $(3)\Leftrightarrow(4)$ via a free cover $F \twoheadrightarrow M$: projectivity of $M$ makes this particular sequence split, which is the same as $M$ being a summand of $F$.

---

# Motivation

[[Def - Projective Module|Projective]] modules are defined by an abstract lifting property, which is exactly the right *behaviour* to demand but the wrong thing to *compute with*. This theorem converts that abstract property into three concrete, usable forms — most importantly into "$M$ is a direct summand of a free module," which is how one actually recognises, constructs, and reasons about projective modules. The whole point of §3.5 is the equivalence; the definition is the entrance, this theorem is the toolkit.

Each equivalent form is the natural face of projectivity in a different context. The **lifting** form is the categorical definition (projective object). The **exactness** form places projectivity in homological algebra: $\operatorname{Hom}(M, -)$ is always left exact, and projectivity is exactly the extra condition making it fully exact — the dual of flatness for tensor. The **splitting** form connects to the splitting lemma and to extension theory: $M$ is projective iff it "cannot be a non-trivial extension as the quotient", iff every surjection onto it has a section. The **summand** form is the structural reality: projectives are the pieces of free modules, the algebra of vector bundles. Knowing they are one notion lets a problem stated in any one form be solved in whichever is easiest.

The single most consequential payoff is the **corollary projective $\Rightarrow$ flat**, which falls out of the summand form in one line and is the link tying §3.5 back to §3.4. It is *why* the tower free $\Rightarrow$ projective $\Rightarrow$ flat holds at its middle step, and it is the reason vector bundles (finitely generated projectives) give flat families.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$M$ is projective", in one of its disguises, or projectivity is to be established.

The first disguised source is **a free cover whose kernel sequence splits**. The property $B$ is "the presentation $0 \to K \to F \to M \to 0$ has a section." The bridge: by $(3)\Leftrightarrow(4)$, a splitting exhibits $M$ as a summand of $F$, hence projective. The non-obvious value: projectivity is detected by a *single* sequence — the free cover — not all sequences. *Example problem:* show a module is projective by splitting its canonical free presentation.

The second disguised source is **an idempotent or an evident complement**. The property $B$ is "$M \oplus N$ is free for some explicit $N$" (e.g. $M = Re$ with $e^2 = e$, complement $R(1-e)$). The bridge: form (4) directly gives projectivity. The non-obvious value: a concrete decomposition certifies an abstract lifting property. *Example problem:* $Re$ is projective for any idempotent $e$, hence $\mathbb{Z}/2$ is projective over $\mathbb{Z}/6$.

The third disguised source is **a need to lift a map through a surjection**. The property $B$ is "I have $M \to C$ and a surjection $B \twoheadrightarrow C$ and want $M \to B$ over it." The bridge: if $M$ is projective, form (1) supplies the lift. The non-obvious value: projectivity is the *license to lift*, the input to many diagram chases. *Example problem:* lift a homomorphism from a projective module to construct a splitting elsewhere.

**Targets (Output Amplification)**

The conclusion is "$M$ is projective, in all four senses."

Combine projectivity with **a short exact sequence ending in $M$** to split it: $0 \to A \to B \to M \to 0$ splits, so $E$: $B \cong A \oplus M$. This is the workhorse for decomposing modules and is how a projective quotient pries apart a middle term. Nonobvious because the splitting is automatic, requiring no construction beyond lifting $\operatorname{id}_M$.

Combine projectivity with **flatness machinery**. Via (4), $M$ is a summand of free, hence flat, so $E$: $M\otimes(-)$ is exact. The combination is the bridge to §3.4 and lets projective modules be used wherever flatness is needed (base change, localization arguments). Nonobvious because a Hom-side property (lifting) yields a tensor-side property (exactness).

Combine projectivity with **the structure of the base ring**. Over a [[Def - Principal Ideal Domain|PID]] or local ring, projective collapses to free, so $E$: a projective module over such a ring has a basis. The combination converts the summand form into an actual basis under extra hypotheses. Nonobvious because it identifies exactly when the projective-free gap closes.

---

# Why Is It True

The intuition is that **a free module's defining virtue is that maps out of it are arbitrary choices of basis-images, which is exactly what makes lifting through a surjection always possible; a summand of a free module inherits half of that virtue — enough to lift, not enough to have a basis.** Run the equivalences.

$(1)\Leftrightarrow(2)$: $\operatorname{Hom}(M,-)$ is [[Thm - Hom is Left Exact|always left exact]]; the only exactness it can lack is surjectivity of $\operatorname{Hom}(M, N) \to \operatorname{Hom}(M, N/N')$, and that surjectivity *is* the lifting property (every map $M \to N/N'$ comes from a map $M \to N$). So "lifting" and "$\operatorname{Hom}(M,-)$ exact" are literally the same statement.

$(1)\Leftrightarrow(3)$: a short exact $0 \to A \to B \xrightarrow{g} M \to 0$ presents $M$ as the quotient $B/A$. Lifting the identity map $\operatorname{id}_M : M \to M = B/A$ through $g$ produces a section $s : M \to B$ with $gs = \operatorname{id}_M$ — which is exactly a splitting. Conversely, given splittings of all such sequences, build a lift of any $M \to N/N'$ by pulling back. Projectivity is "can lift the identity off any free cover."

$(3)\Leftrightarrow(4)$ — **the heart**: every module has a free cover $\pi : F \twoheadrightarrow M$, giving $0 \to \ker\pi \to F \xrightarrow{\pi} M \to 0$. If this splits, the section $s : M \to F$ embeds $M$ as a summand, $F \cong \ker\pi \oplus s(M) \cong \ker\pi \oplus M$, so $M$ is a summand of a free module — form (4). Conversely if $M \oplus N \cong R^{\oplus I}$, then $M$ inherits the lifting property from the free module (a map out of $M$ extends to the free module by zero on $N$, lifts there using basis-images, restricts back), so every sequence onto $M$ splits.

**The whole mechanism in one sentence: project a free module's "maps out are free choices" through a chosen complement, and the lifting/splitting that free modules enjoy survives onto any direct summand.**

For the corollary, **projective $\Rightarrow$ flat** because free modules are flat and flatness passes to summands: $M \oplus N \cong R^{\oplus I}$ flat forces each summand flat.

---

# What Makes This Hard

The difficulty is entirely in the pivot $(3)\Leftrightarrow(4)$ and in *choosing the right sequence to split*. The non-obvious move is to apply projectivity not to an arbitrary sequence but to the canonical **free cover** $F \twoheadrightarrow M$, and then to lift the **identity** $\operatorname{id}_M$ — beginners try to lift a general map and lose the thread. The second subtlety is the direction $(4)\Rightarrow(1)$: showing a summand of free inherits the lifting property requires extending a map off $M$ to the whole free module (by zero on the complement), lifting there, and restricting — a three-step manoeuvre that is easy to state but easy to skip. The common error is to conflate "summand of free" with "free" and assert a basis exists; the theorem deliberately stops at summand, and the projective-not-free examples show the gap is real.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Prove $(1)\Leftrightarrow(2)$ by unwinding what surjectivity of $\operatorname{Hom}(M,-)$ on a quotient means. Prove $(1)\Rightarrow(3)$ by lifting $\operatorname{id}_M$. Prove $(3)\Rightarrow(4)$ by splitting a free cover. Prove $(4)\Rightarrow(1)$ by extending-lifting-restricting through the free module. Deduce flatness from the summand form.

**Subgoal decomposition:**

1. **$(1)\Leftrightarrow(2)$.** Show lifting $=$ exactness of $\operatorname{Hom}(M,-)$.
   - *Hint:* $\operatorname{Hom}(M,-)$ is left exact; the missing piece is surjectivity of $\operatorname{Hom}(M, N) \to \operatorname{Hom}(M, N/N')$, which is exactly "every map $M\to N/N'$ lifts."
   - *Why needed:* Identifies the homological and categorical forms.

2. **$(1)\Rightarrow(3)$.** Split any $0 \to A \to B \xrightarrow{g} M \to 0$.
   - *Hint:* Lift $\operatorname{id}_M : M \to M = B/A$ through $g$ to a section $s$.
   - *Why needed:* Produces the section from the lifting property.

3. **$(3)\Rightarrow(4)$.** Split the free cover.
   - *Hint:* Choose $F \twoheadrightarrow M$ free; the section embeds $M$ as a summand, $F \cong \ker\pi \oplus M$.
   - *Why needed:* This is the structural conclusion.

4. **$(4)\Rightarrow(1)$.** A summand of free has the lifting property.
   - *Hint:* Extend a map $M \to N/N'$ to $M \oplus N' \cong$ free by zero, lift on the free module (basis-images), restrict to $M$.
   - *Why needed:* Closes the loop.

5. **Corollary.** Projective $\Rightarrow$ flat.
   - *Hint:* Free is flat; a summand of flat is flat; apply to $M \oplus N \cong R^{\oplus I}$.
   - *Why needed:* Links §3.5 to §3.4.

---

# Lemma Decomposition

> [!note]- Lemma 1: Lifting equals exactness of $\operatorname{Hom}(M,-)$
> **Statement:** $M$ is projective (lifting form) iff $\operatorname{Hom}_R(M, -)$ is exact.
>
> **Hint:** $\operatorname{Hom}(M,-)$ is left exact already; the only failure possible is right-end surjectivity, which equals the lifting property.
>
> **Why needed:** It is $(1)\Leftrightarrow(2)$, identifying the categorical and homological faces.
>
> > [!note]- Full proof
> > By [[Thm - Hom is Left Exact|left-exactness]], applying $\operatorname{Hom}(M,-)$ to $0 \to N' \to N \xrightarrow{\pi} N/N' \to 0$ gives an exact $0 \to \operatorname{Hom}(M, N') \to \operatorname{Hom}(M, N) \xrightarrow{\pi_*} \operatorname{Hom}(M, N/N')$. The functor is exact iff $\pi_*$ is *surjective* for every such $\pi$. Surjectivity of $\pi_*$ says every $\bar h : M \to N/N'$ equals $\pi \circ g$ for some $g : M \to N$ — exactly the lifting property. Hence projective $\iff \operatorname{Hom}(M,-)$ exact.

> [!note]- Lemma 2: Projective implies every surjection onto $M$ splits
> **Statement:** If $M$ is projective and $0 \to A \to B \xrightarrow{g} M \to 0$ is short exact, then $g$ has a section, so the sequence splits and $B \cong A \oplus M$.
>
> **Hint:** Lift the identity $\operatorname{id}_M$ through the surjection $g$.
>
> **Why needed:** It is $(1)\Rightarrow(3)$ and feeds the summand construction.
>
> > [!note]- Full proof
> > View $M = B/A$ via $g$, so $g : B \to M$ is the quotient map. Apply the lifting property to $\bar h = \operatorname{id}_M : M \to M = B/A$ and the surjection $g$: there is $s : M \to B$ with $g \circ s = \operatorname{id}_M$. So $s$ is a section, and by [[Ex - The splitting lemma|the splitting lemma]] the sequence splits with $B \cong A \oplus M$.

> [!note]- Lemma 3: Splitting a free cover gives a summand of free, and conversely
> **Statement:** $M$ is a direct summand of a free module iff some (equivalently every) free cover $0 \to K \to F \xrightarrow{\pi} M \to 0$ splits.
>
> **Hint:** A section of $\pi$ embeds $M$ in $F$ as a complement of $K$; conversely a summand inherits the splitting.
>
> **Why needed:** It is the pivot $(3)\Leftrightarrow(4)$.
>
> > [!note]- Full proof
> > Take a free cover $\pi : F \twoheadrightarrow M$ (send a basis of $F$ to a generating set of $M$). If it splits, a section $s : M \to F$ satisfies $\pi s = \operatorname{id}_M$, so $F = \ker\pi \oplus s(M)$ with $s(M) \cong M$; thus $M$ is a summand of the free $F$. Conversely, if $M \oplus N \cong R^{\oplus I}$, then $M$ inherits the lifting property (Lemma 4 direction), so by Lemma 2 every sequence onto $M$ splits, in particular the free cover.

> [!note]- Lemma 4: A summand of a free module has the lifting property
> **Statement:** If $M \oplus N \cong R^{\oplus I}$ is free, then $M$ satisfies the lifting property (is projective).
>
> **Hint:** Extend a map off $M$ to the free module by zero on $N$, lift on the free module using basis-image freedom, restrict.
>
> **Why needed:** It is $(4)\Rightarrow(1)$, closing the equivalence loop.
>
> > [!note]- Full proof
> > Let $F = M \oplus N \cong R^{\oplus I}$ with inclusion $\iota : M \hookrightarrow F$ and projection $p : F \twoheadrightarrow M$, $p\iota = \operatorname{id}_M$. Given $\bar h : M \to Q$ and a surjection $q : P \twoheadrightarrow Q$, form $\bar h \circ p : F \to Q$. Since $F$ is free with basis $(e_i)$, choose $g_i \in P$ with $q(g_i) = (\bar h p)(e_i)$ (using surjectivity of $q$) and extend linearly to $G : F \to P$ with $qG = \bar h p$. Set $g := G \iota : M \to P$. Then $q g = q G \iota = \bar h p \iota = \bar h$, so $g$ lifts $\bar h$. Hence $M$ is projective.

---

# Formal Proof

> [!note]- Complete formal proof
> We prove $(1)\Leftrightarrow(2)$, then $(1)\Rightarrow(3)\Rightarrow(4)\Rightarrow(1)$.
>
> **$(1)\Leftrightarrow(2)$.** Lemma 1.
>
> **$(1)\Rightarrow(3)$.** Lemma 2: projectivity lets us lift $\operatorname{id}_M$ off any surjection onto $M$, producing a section, so the sequence splits.
>
> **$(3)\Rightarrow(4)$.** Lemma 3: choose a free cover $0 \to K \to F \xrightarrow{\pi} M \to 0$; by (3) it splits, so $M$ is a direct summand of the free module $F$, giving (4).
>
> **$(4)\Rightarrow(1)$.** Lemma 4: a direct summand of a free module satisfies the lifting property.
>
> This closes the cycle, so (1)–(4) are equivalent.
>
> **Corollary — projective $\Rightarrow$ flat.** By (4), $M \oplus N \cong R^{\oplus I}$. The free module $R^{\oplus I}$ is [[Def - Flat Module|flat]] (tensoring with it is a direct sum of copies, preserving injections). A direct summand of a flat module is flat: if $M \oplus N$ is flat and $f$ is an injection, then $\operatorname{id}_{M\oplus N}\otimes f = (\operatorname{id}_M\otimes f)\oplus(\operatorname{id}_N\otimes f)$ is injective, forcing each summand $\operatorname{id}_M\otimes f$ injective. Hence $M$ is flat. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Idempotents produce projectives in any product ring.** In $R = R_1 \times R_2$ the idempotent $e = (1, 0)$ gives $R = Re \oplus R(1-e)$ with $Re \cong R_1$, so $R_1$ (as an $R$-module) is projective by (4). The application is nonobvious because it manufactures projective-not-free modules from the ring's idempotent structure alone — the $\mathbb{Z}/6 = \mathbb{Z}/2 \times \mathbb{Z}/3$ example is the smallest case.

**Vector bundles as summands of trivial bundles.** Over the ring of continuous functions on a compact space, Swan's theorem realizes every vector bundle as a direct summand of a trivial bundle, i.e. a finitely generated projective module via form (4). The application is nonobvious because the algebraic summand characterization is exactly the topological fact "every bundle embeds in a trivial bundle with a complement," the content of Serre–Swan.

**Splitting via a projective cokernel in homological algebra.** Whenever a short exact sequence $0 \to A \to B \to P \to 0$ has projective cokernel $P$, form (3) forces it to split, so $\operatorname{Ext}^1(P, A) = 0$ for projective $P$. The application is nonobvious because it identifies projectives as the modules with vanishing $\operatorname{Ext}^1$, the homological signature used to build projective resolutions.

---

# Bridges

- **[[Def - Projective Module|Projective Module]]** — this theorem is the definition's toolkit, converting the abstract lifting property into the computable "summand of free" and the homological "$\operatorname{Hom}(M,-)$ exact". It is what makes projectivity recognisable in practice.

- **[[Thm - Hom is Left Exact|Hom is Left Exact]]** — the input to $(1)\Leftrightarrow(2)$. $\operatorname{Hom}(M,-)$ is always left exact; projectivity is exactly the hypothesis upgrading it to fully exact, so projective is to $\operatorname{Hom}(M,-)$ what flat is to $M\otimes(-)$.

- **[[Def - Flat Module|Flat Module]]** — linked by the corollary projective $\Rightarrow$ flat, the middle step of the tower. The summand form makes this a one-line consequence and is the reason finitely generated projectives (vector bundles) give flat families.

- **[[Ex - The splitting lemma|The Splitting Lemma]]** — the mechanism behind $(1)\Rightarrow(3)$: a section of the surjection onto $M$, obtained by lifting the identity, splits the sequence and yields $B \cong A \oplus M$. Projectivity is precisely "the section always exists."

---

# Unlocked by This

> [!tip] Serre–Swan and vector bundles *(from Algebraic Geometry / Topology)*
> The summand form $M \oplus N \cong R^n$ is the algebraic incarnation of "every vector bundle is a sub-bundle of a trivial bundle with a complement." The **Serre–Swan theorem** turns this into an equivalence: finitely generated projective modules over the ring of functions on a space are exactly vector bundles over the space, with free modules the trivial bundles. The projective-not-free gap is the existence of non-trivial bundles.

> [!tip] The Quillen–Suslin theorem *(from Commutative Algebra)*
> Over a polynomial ring $k[x_1, \dots, x_n]$ every finitely generated projective module is in fact **free** (Quillen–Suslin, the solution to Serre's problem). Geometrically: every algebraic vector bundle over affine space is trivial. This is the deep statement of *when* the summand form forces an actual basis, the affirmative answer that the projective-free gap closes over affine space.

> [!tip] Projective resolutions and homological dimension *(from Homological Algebra)*
> Because $\operatorname{Hom}(M,-)$ is exact for projective $M$, projectives build **projective resolutions** $\cdots \to P_1 \to P_0 \to M \to 0$, and the least length of such a resolution is the projective dimension of $M$. These resolutions compute $\operatorname{Ext}$ and $\operatorname{Tor}$ and underlie the global dimension theory of rings.
