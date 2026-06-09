---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - Module"
  - "Def - Module Homomorphism"
  - "Def - Annihilator"
  - "Def - Prime and Maximal Ideal"
  - "Def - Exact Sequence and Short Exact Sequence"
  - "Def - Flat Module"
  - "Def - Multiplicative Set and Localization"
  - "Def - Local Property (Localizable and Local-to-Global)"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$. For an [[Def - Module|$R$-module]] $M$ and a [[Def - Prime and Maximal Ideal|prime]] $\mathfrak{p}$ (resp. maximal ideal $\mathfrak{m}$), $M_{\mathfrak{p}}$ (resp. $M_{\mathfrak{m}}$) is the [[Def - Multiplicative Set and Localization|localization]]; for a map $f$, $f_{\mathfrak{p}}$ is its localization. We write $\operatorname{Spec} R$ for the primes, $\operatorname{mSpec} R$ for the maximal ideals, and $\operatorname{Ann}_R(m) = \{r\in R : rm = 0\}$ for the [[Def - Annihilator|annihilator]] of $m\in M$. The full registry is on [[Commutative Algebra IV — Localization]].

---

# Statement

> **Theorem (The local–global principle; Becker Prop. 4.22, 4.24, 4.25, 4.26).** Let $M, N$ be $R$-modules and $f : M\to N$, $A\xrightarrow{f}B\xrightarrow{g}C$ be $R$-linear. The following are [[Def - Local Property (Localizable and Local-to-Global)|local properties]] — each holds for the global object if and only if it holds after localizing at every prime, equivalently at every maximal ideal:
> 1. **(Zero; Prop. 4.22.)** $M = 0 \iff M_{\mathfrak{p}} = 0\ \forall\mathfrak{p} \iff M_{\mathfrak{m}} = 0\ \forall\mathfrak{m}$.
> 2. **(Exactness; Prop. 4.24.)** $A\xrightarrow{f}B\xrightarrow{g}C$ exact $\iff A_{\mathfrak{p}}\xrightarrow{f_{\mathfrak{p}}}B_{\mathfrak{p}}\xrightarrow{g_{\mathfrak{p}}}C_{\mathfrak{p}}$ exact $\forall\mathfrak{p}$ $\iff$ same $\forall\mathfrak{m}$.
> 3. **(Injectivity/surjectivity; Prop. 4.25.)** $f$ injective (resp. surjective) $\iff f_{\mathfrak{p}}$ injective (resp. surjective) $\forall\mathfrak{p}$ $\iff$ same $\forall\mathfrak{m}$.
> 4. **(Flatness; Prop. 4.26.)** $M$ flat over $R$ $\iff M_{\mathfrak{p}}$ flat over $R_{\mathfrak{p}}$ $\forall\mathfrak{p}$ $\iff M_{\mathfrak{m}}$ flat over $R_{\mathfrak{m}}$ $\forall\mathfrak{m}$.

> **Base lemma.** "Being zero" is the engine: every other statement reduces to it by localizing the appropriate kernel, image, or homology module. The hard direction throughout is local-to-global, proved by the annihilator argument.

---

# Motivation

This is the chapter's destination and its single most-used theorem in the rest of commutative algebra. It is the rigorous licence for the most powerful slogan in the subject: **"to prove it, prove it one prime at a time."** A statement about a module or map over an arbitrarily complicated ring $R$ — zero, injective, surjective, exact, flat — can be replaced by the *same* statement over the much simpler [[Def - Local Ring and Residue Field|local rings]] $R_{\mathfrak{m}}$, one for each maximal ideal, where the heavy local tools ([[Commutative Algebra V — Nakayama's Lemma|Nakayama]], the residue field, "non-units form an ideal") become available.

The reason this works splits, as the [[Def - Local Property (Localizable and Local-to-Global)|local-property definition]] insists, into two directions. The *localizable* direction — global truth descends to each localization — is free: it is nothing but the [[Thm - Localization is Exact and the Localization is Flat|exactness of localization]]. If $f$ is injective, then $f_{\mathfrak{p}}$ is injective because localization preserves injections; if a sequence is exact, its localizations are exact because $S^{-1}(-)$ is an exact functor. No new idea. The content — the surprising, useful, *gluing* direction — is *local-to-global*: if every localization has the property, so does the global object. And this entire direction rests on a single base theorem, "**being zero is a local property**", proved by one beautiful argument about annihilators.

That base argument is worth stating as the heart of the chapter. Suppose $M_{\mathfrak{m}} = 0$ for every maximal ideal $\mathfrak{m}$, yet $M\neq 0$; take $0\neq m\in M$. Its annihilator $\operatorname{Ann}(m)$ is a proper ideal (it does not contain $1$, since $1\cdot m = m\neq 0$), so it lies inside *some* maximal ideal $\mathfrak{m}$. But $M_{\mathfrak{m}} = 0$ means $\tfrac m1 = 0$ in $M_{\mathfrak{m}}$, so $um = 0$ for some $u\notin\mathfrak{m}$ — that is, $u\in\operatorname{Ann}(m)\setminus\mathfrak{m}$, contradicting $\operatorname{Ann}(m)\subseteq\mathfrak{m}$. So $M = 0$. Every other local-to-global statement is this one in disguise: to show a map is zero, show its image is zero; to show a sequence is exact, show its homology $\ker g/\operatorname{im} f$ is zero — and "zero" is local. The theorem is therefore *one idea, applied four times*, and the idea is that a nonzero module always has an element whose annihilator hides inside a maximal ideal, which the corresponding localization would have to detect.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition for invoking the principle is *a target property (zero/injective/surjective/exact/flat) over a complicated ring, to be verified locally*.

The first disguised source is **"prove this module/map is zero/injective/etc. and the ring is complicated"**. Property $B$: the target is on the local list and $R$ has many primes. The bridge: replace $R$ by $R_{\mathfrak{m}}$ and the object by its localization, for an arbitrary maximal $\mathfrak{m}$. The non-obvious value: the reduction is *lossless* (it is a biconditional), so nothing is given up. *Example problem:* "$A$ is a domain $\Rightarrow A = \bigcap_{\mathfrak{m}} A_{\mathfrak{m}}$" is proved by showing the inclusion is locally surjective — see [[Ex - A domain is the intersection of its localizations at maximal ideals]].

The second disguised source is **"a homology module or cokernel should vanish"**. Property $B$: you want $\ker g = \operatorname{im} f$, or a cokernel is $0$. The bridge: this is "$\ker g/\operatorname{im} f = 0$", and zero is local, so check it at each $\mathfrak{m}$ where the localized homology is $(\ker g_{\mathfrak{m}})/(\operatorname{im} f_{\mathfrak{m}})$. The non-obvious value: exactness, the most-needed property, reduces to the base lemma. *Example problem:* proving a complex is exact by checking it at every maximal ideal.

The third disguised source is **"reduce a property to the residue field"**. Property $B$: after localizing at $\mathfrak{m}$, you want to pass further to $\kappa(\mathfrak{m}) = R_{\mathfrak{m}}/\mathfrak{m}R_{\mathfrak{m}}$. The bridge: locality plus Nakayama lets a finitely generated module's behaviour be read off the $\kappa$-vector space $M_{\mathfrak{m}}/\mathfrak{m}M_{\mathfrak{m}}$. The non-obvious value: a question over $R$ becomes linear algebra over a field. *Example problem:* surjectivity of $f$ checked by surjectivity of $\bar f : M\otimes\kappa(\mathfrak{m})\to N\otimes\kappa(\mathfrak{m})$ via Nakayama.

**Targets (Output Amplification)**

The conclusion is *the global property holds, having been verified locally*.

Combine with **Nakayama's lemma**. Once local, a finitely generated module over $(R_{\mathfrak{m}}, \mathfrak{m}R_{\mathfrak{m}})$ obeys Nakayama, so generation lifts from $M/\mathfrak{m}M$. The further result $E$: a set generates $M$ iff it generates locally iff its image spans $M_{\mathfrak{m}}/\mathfrak{m}M_{\mathfrak{m}}$ for all $\mathfrak{m}$ — generation is checkable on residue fields. Nonobvious because it converts module generation into linear algebra over fields, the basis of [[Commutative Algebra V — Nakayama's Lemma|Nakayama's chapter]].

Combine with **the boundary of locality (freeness is NOT local)**. Knowing which properties are local *and which are not* is itself a tool: a locally free module need not be free, which detects nontrivial vector bundles. The further result $E$: the *failure* of the principle for freeness is the existence of projective-non-free modules and line bundles. Nonobvious because the value is in the negative result — see [[Ex - Freeness is not a local property]].

Combine with **the "reasonable property" meta-theorem**. For any property invariant under module and base-ring isomorphism, "holds at all maximal ideals" already gives "holds at all primes". The further result $E$: you only ever check maximal ideals, the most concrete primes. Nonobvious because it lets the convenient maximal-ideal form imply the full prime form for *any* sensible property, not just the four listed.

---

# Why Is It True

Everything is the base lemma "being zero is local", and the base lemma is the annihilator argument. Localizable is automatic ($M = 0\Rightarrow M_{\mathfrak{p}} = S^{-1}0 = 0$). For local-to-global, the contrapositive is the whole proof: a *nonzero* module has a nonzero element $m$, whose annihilator $\operatorname{Ann}(m)$ is proper, hence sits inside a maximal ideal $\mathfrak{m}$; but then $M_{\mathfrak{m}}\neq 0$, because $\tfrac m1 = 0$ in $M_{\mathfrak{m}}$ would require $um = 0$ for some $u\notin\mathfrak{m}$, putting $u\in\operatorname{Ann}(m)$ *outside* $\mathfrak{m}$ — impossible. So a nonzero module is *seen* by at least one maximal localization.

**One-line mechanism: a nonzero element's annihilator is a proper ideal, hence lives inside a maximal ideal $\mathfrak{m}$; that $\mathfrak{m}$ is exactly the one whose localization $M_{\mathfrak{m}}$ refuses to vanish — so "$M_{\mathfrak{m}} = 0$ for all $\mathfrak{m}$" forces $M = 0$.**

The other three reduce to this:

*Exactness.* By [[Thm - Localization Commutes with Quotients and Finite Operations|localization commuting with kernels, images, and quotients]], the "homology" localizes: $(\ker g/\operatorname{im} f)_{\mathfrak{m}}\cong\ker g_{\mathfrak{m}}/\operatorname{im} f_{\mathfrak{m}}$. The sequence is exact iff this homology is $0$; the localized sequences are exact iff each localized homology is $0$. By the base lemma, "homology $= 0$" is local. (One first shows $\operatorname{im}(g\circ f) = 0$ by localizing $\operatorname{im}((g\circ f)_{\mathfrak{m}}) = 0$, then the homology.)

*Injectivity/surjectivity.* Injective means $\ker f = 0$; surjective means $\operatorname{coker} f = 0$. Both are "a specific module is zero", and localization commutes with $\ker$ and $\operatorname{coker}$ (exactness), so each is local by the base lemma.

*Flatness.* The localizable direction is base change preserving flatness ($M_{\mathfrak{p}} = R_{\mathfrak{p}}\otimes M$). For local-to-global: take an injection $N\hookrightarrow P$; to show $N\otimes M\hookrightarrow P\otimes M$, check it locally — at each $\mathfrak{m}$, $N_{\mathfrak{m}}\hookrightarrow P_{\mathfrak{m}}$ (injectivity is local) and $M_{\mathfrak{m}}$ flat give $N_{\mathfrak{m}}\otimes M_{\mathfrak{m}}\hookrightarrow P_{\mathfrak{m}}\otimes M_{\mathfrak{m}}$, i.e. $(N\otimes M)_{\mathfrak{m}}\hookrightarrow(P\otimes M)_{\mathfrak{m}}$; since injectivity is local, $N\otimes M\hookrightarrow P\otimes M$ globally. Flatness is local because *injectivity* is local and tensor commutes with localization.

The thread: **the principle is the single fact "a nonzero module is detected by some maximal localization", propagated through the (co)kernel/homology of the situation at hand.**

---

# What Makes This Hard

The deceptive part is that the localizable direction is trivial, so all the difficulty hides in local-to-global, and specifically in the annihilator argument — the move "$\operatorname{Ann}(m)$ is proper, so lies in a maximal ideal, and the localization there cannot kill $m$" is the one genuinely clever step, and it is where everyone gets stuck. The second pitfall is forgetting that exactness/injectivity must be *converted to a vanishing statement* (homology, kernel, cokernel) before the base lemma applies — the principle does not act on "exact" directly but on "this module is zero". The cardinal error is to assume *every* nice property is local; freeness and "is a domain" are not, and the boundary must be respected.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Prove the base lemma "$M = 0$ is local" by the annihilator argument. Reduce exactness, injectivity, and surjectivity to it by localizing the relevant homology/kernel/cokernel (using that localization commutes with these). Prove flatness local-to-global by tensoring an injection and localizing, using that injectivity is already local.

**Subgoal decomposition:**

1. **Base lemma.** Show $M = 0\iff M_{\mathfrak{m}} = 0\ \forall\mathfrak{m}$.
   - *Hint:* contrapositive — $0\neq m$ has proper $\operatorname{Ann}(m)\subseteq$ some $\mathfrak{m}$; then $M_{\mathfrak{m}}\neq 0$ because killing $m$ would need a unit annihilator outside $\mathfrak{m}$.
   - *Why needed:* it is the engine; all else reduces to it.

2. **Exactness, injectivity, surjectivity.** Reduce each to the base lemma.
   - *Hint:* exact $\iff$ homology $\ker g/\operatorname{im} f = 0$; injective $\iff\ker f = 0$; surjective $\iff\operatorname{coker} f = 0$; localization commutes with all these, so apply step 1.
   - *Why needed:* these are the working properties; all are "a module vanishes".

3. **Flatness.** Show $M_{\mathfrak{m}}$ flat $\forall\mathfrak{m}\Rightarrow M$ flat.
   - *Hint:* take $N\hookrightarrow P$; locally $N_{\mathfrak{m}}\otimes M_{\mathfrak{m}}\hookrightarrow P_{\mathfrak{m}}\otimes M_{\mathfrak{m}}$ by local flatness, i.e. $(N\otimes M)_{\mathfrak{m}}\hookrightarrow(P\otimes M)_{\mathfrak{m}}$; injectivity is local, so global injection.
   - *Why needed:* the deepest of the four, built on the locality of injectivity.

---

# Lemma Decomposition

> [!note]- Lemma 1: Being zero is a local property (the base lemma)
> **Statement:** $M = 0\iff M_{\mathfrak{m}} = 0$ for every maximal ideal $\mathfrak{m}$.
>
> **Hint:** Contrapositive via annihilators: a nonzero element's annihilator is proper, lands in some $\mathfrak{m}$, and that localization cannot vanish.
>
> **Why needed:** Every other part of the theorem is this lemma applied to a kernel, image, cokernel, or homology.
>
> > [!note]- Full proof
> > ($\Rightarrow$) trivial: $M = 0\Rightarrow M_{\mathfrak{m}} = (R\setminus\mathfrak{m})^{-1}0 = 0$.
> >
> > ($\Leftarrow$) Suppose $M_{\mathfrak{m}} = 0$ for all $\mathfrak{m}\in\operatorname{mSpec} R$ but $M\neq 0$; pick $0\neq m\in M$. The [[Def - Annihilator|annihilator]] $\operatorname{Ann}(m) = \{r\in R : rm = 0\}$ is an ideal not containing $1$ (since $1\cdot m = m\neq 0$), hence proper, hence contained in some maximal ideal $\mathfrak{m}$. Consider $M_{\mathfrak{m}}$: since it is $0$, $\tfrac m1 = \tfrac01$, so there is $u\in R\setminus\mathfrak{m}$ with $um = 0$. Then $u\in\operatorname{Ann}(m)$ but $u\notin\mathfrak{m}$, contradicting $\operatorname{Ann}(m)\subseteq\mathfrak{m}$. Hence $M = 0$.

> [!note]- Lemma 2: Localization commutes with kernel, image, cokernel, homology
> **Statement:** For $R$-linear $f$, $(\ker f)_{\mathfrak{p}} = \ker(f_{\mathfrak{p}})$, $(\operatorname{im} f)_{\mathfrak{p}} = \operatorname{im}(f_{\mathfrak{p}})$, and $(\ker g/\operatorname{im} f)_{\mathfrak{p}}\cong\ker(g_{\mathfrak{p}})/\operatorname{im}(f_{\mathfrak{p}})$.
>
> **Hint:** Apply the exact functor $S^{-1}(-)$ to the defining sequences; quotients localize by [[Thm - Localization Commutes with Quotients and Finite Operations]].
>
> **Why needed:** It lets the base lemma act on the homology of the situation, turning "exact" into "a module is zero".
>
> > [!note]- Full proof
> > [[Thm - Localization is Exact and the Localization is Flat|Localization is exact]], so applying it to $0\to\ker f\to M\xrightarrow{f}\operatorname{im} f\to 0$ gives $(\ker f)_{\mathfrak{p}} = \ker(f_{\mathfrak{p}})$ and $(\operatorname{im} f)_{\mathfrak{p}} = \operatorname{im}(f_{\mathfrak{p}})$. Since localization commutes with quotients ([[Thm - Localization Commutes with Quotients and Finite Operations|Prop. 4.14(3)]]), $(\ker g/\operatorname{im} f)_{\mathfrak{p}}\cong(\ker g)_{\mathfrak{p}}/(\operatorname{im} f)_{\mathfrak{p}} = \ker(g_{\mathfrak{p}})/\operatorname{im}(f_{\mathfrak{p}})$, using $\operatorname{im} f\subseteq\ker g$ throughout.

> [!note]- Lemma 3: Flatness is local-to-global
> **Statement:** If $M_{\mathfrak{m}}$ is flat over $R_{\mathfrak{m}}$ for all maximal $\mathfrak{m}$, then $M$ is flat over $R$.
>
> **Hint:** Test flatness on an injection $N\hookrightarrow P$; localize, use local flatness and that injectivity is local.
>
> **Why needed:** It is the deepest part, combining local flatness with the locality of injectivity.
>
> > [!note]- Full proof
> > Let $f : N\hookrightarrow P$ be an injection of $R$-modules; we must show $f\otimes\operatorname{id}_M : N\otimes_R M\to P\otimes_R M$ is injective. Fix a maximal ideal $\mathfrak{m}$. By part 3 (injectivity is local — proved from Lemma 1), $f_{\mathfrak{m}} : N_{\mathfrak{m}}\to P_{\mathfrak{m}}$ is injective. Since $M_{\mathfrak{m}}$ is flat over $R_{\mathfrak{m}}$, $f_{\mathfrak{m}}\otimes\operatorname{id}_{M_{\mathfrak{m}}} : N_{\mathfrak{m}}\otimes_{R_{\mathfrak{m}}}M_{\mathfrak{m}}\to P_{\mathfrak{m}}\otimes_{R_{\mathfrak{m}}}M_{\mathfrak{m}}$ is injective. By [[Thm - Localization Commutes with Quotients and Finite Operations|localization commuting with tensor]], this is exactly $(N\otimes_R M)_{\mathfrak{m}}\to(P\otimes_R M)_{\mathfrak{m}}$, i.e. $(f\otimes\operatorname{id}_M)_{\mathfrak{m}}$ is injective for every $\mathfrak{m}$. Since injectivity is a local property, $f\otimes\operatorname{id}_M$ is injective. Hence $M$ is flat.

---

# Formal Proof

> [!note]- Complete formal proof
> **Part 1 (zero).** Lemma 1.
>
> **Part 3 (injectivity/surjectivity).** $f$ injective $\iff\ker f = 0$. By Lemma 2, $(\ker f)_{\mathfrak{m}} = \ker(f_{\mathfrak{m}})$, so "$\ker f = 0$" is, via Lemma 1, equivalent to "$\ker(f_{\mathfrak{m}}) = 0$ for all $\mathfrak{m}$", i.e. "$f_{\mathfrak{m}}$ injective for all $\mathfrak{m}$". The argument for surjective is identical with $\operatorname{coker} f = N/\operatorname{im} f$ in place of $\ker f$ (cokernel localizes by Lemma 2).
>
> **Part 2 (exactness).** The localizable direction is [[Thm - Localization is Exact and the Localization is Flat|exactness of localization]]. For local-to-global, assume each $A_{\mathfrak{m}}\to B_{\mathfrak{m}}\to C_{\mathfrak{m}}$ exact. First, $\operatorname{im}((g\circ f)_{\mathfrak{m}}) = \operatorname{im}(g_{\mathfrak{m}}\circ f_{\mathfrak{m}}) = 0$ for all $\mathfrak{m}$, so by Lemmas 1–2, $\operatorname{im}(g\circ f) = 0$, i.e. $g\circ f = 0$, i.e. $\operatorname{im} f\subseteq\ker g$. Then by Lemma 2, $(\ker g/\operatorname{im} f)_{\mathfrak{m}}\cong\ker(g_{\mathfrak{m}})/\operatorname{im}(f_{\mathfrak{m}}) = 0$ (local exactness) for all $\mathfrak{m}$, so by Lemma 1, $\ker g/\operatorname{im} f = 0$, i.e. $\operatorname{im} f = \ker g$. The sequence is exact.
>
> **Part 4 (flatness).** Localizable: $M$ flat $\Rightarrow M_{\mathfrak{p}} = R_{\mathfrak{p}}\otimes_R M$ flat, since [[Thm - Extension of Scalars Preserves Flatness|extension of scalars preserves flatness]]. Maximal from prime: every maximal ideal is prime. Local-to-global: Lemma 3. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**A domain is the intersection of its localizations.** For an integral domain $A$, the inclusion $A\hookrightarrow\bigcap_{\mathfrak{m}}A_{\mathfrak{m}}$ (intersection inside $\operatorname{Frac} A$) is an equality, proved by showing the inclusion is *surjective*, which is a local property: at each $\mathfrak{m}$ it is the identity $A_{\mathfrak{m}} = A_{\mathfrak{m}}$. Nonobvious recognition: a global equality of modules is established by checking surjectivity locally — see [[Ex - A domain is the intersection of its localizations at maximal ideals]].

**Reducedness via the local-global principle.** A ring is reduced iff $\operatorname{nil} R = 0$ iff $R_{\mathfrak{p}}$ is reduced for all $\mathfrak{p}$, because $\operatorname{nil}(R_{\mathfrak{p}}) = (\operatorname{nil} R)_{\mathfrak{p}}$ and "$\operatorname{nil} R = 0$" is local. Nonobvious because a *ring* property (no nilpotents) is reduced to checking local rings, using the module-level principle on $\operatorname{nil} R$ — see [[Ex - Being reduced is a local property]].

**Noetherian from local data (with a finiteness condition).** A ring with all $R_{\mathfrak{m}}$ Noetherian and each $0\neq x$ in only finitely many maximal ideals is Noetherian, proved by showing an ideal is finitely generated using "surjectivity is local" on an inclusion $\mathfrak{b}\hookrightarrow\mathfrak{a}$ that is locally an equality. Nonobvious because "Noetherian" is *not* local in general, yet the local-global principle for surjectivity still drives the proof under the extra finiteness — Becker's Prop. 4.29.

---

# Bridges

- **[[Def - Local Property (Localizable and Local-to-Global)|Local property]]** — this theorem populates the definition with its five canonical examples and exhibits the two-direction structure: localizable (free, from exactness) versus local-to-global (the content, from the annihilator argument).

- **[[Thm - Localization is Exact and the Localization is Flat|Exactness and flatness of localization]]** — supplies the entire localizable direction and the lemma that localization commutes with kernels/images/quotients, without which the homology could not be localized.

- **[[Commutative Algebra V — Nakayama's Lemma|Nakayama's lemma]]** — the standard *second step* after reducing to local: over $(R_{\mathfrak{m}}, \mathfrak{m}R_{\mathfrak{m}})$, Nakayama converts generation and surjectivity into linear algebra over the residue field $\kappa(\mathfrak{m})$. Local-global reduces; Nakayama solves.

- **[[Thm - The Radical is the Intersection of the Primes Above It|The radical theorem]]** — shares the base technique: both ultimately rely on "a nonzero ring/module is detected at some maximal ideal", here via annihilators, there via localizing at an element to manufacture a prime.

---

# Unlocked by This

> [!tip] Checking sheaf statements on stalks *(from Algebraic Geometry / Sheaf Theory)*
> Under the dictionary $M_{\mathfrak{p}} = $ stalk at $\mathfrak{p}$, this theorem *is* the foundational mechanism of sheaf theory: a quasicoherent sheaf is zero iff all stalks vanish, a morphism is injective/surjective/an isomorphism iff it is so on every stalk, a complex is exact iff exact on stalks, a sheaf is flat over the base iff flat on stalks. Every "it suffices to check on stalks" argument in algebraic geometry — that a map of vector bundles is an isomorphism, that a sequence of sheaves is exact, that a family is flat — is an instance of the local–global principle, proved here by the pure algebra of annihilators. The annihilator argument is the affine shadow of the conservativity of the stalk functors.

> [!tip] Vector bundles: where the principle deliberately fails *(from Algebraic Geometry)*
> The five properties above are local; **freeness is not**, and that controlled failure is the entire content of vector-bundle theory. A finitely generated projective module is locally free (free at every prime) yet may not be free, exactly as a vector bundle is locally trivial yet globally twisted. So the local–global principle tells you *which* questions can be answered point-by-point and *which* carry irreducibly global information — the latter living in the **Picard group** and higher cohomology. Knowing the boundary is as important as knowing the principle: it is why $\operatorname{Pic}$, $H^i$, and the **Serre–Swan** correspondence (projective modules $=$ vector bundles) exist — see [[Ex - Freeness is not a local property]].
