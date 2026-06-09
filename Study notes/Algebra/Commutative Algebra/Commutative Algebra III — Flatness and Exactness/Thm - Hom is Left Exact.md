---
type: theorem
subject: commutative-algebra
prereqs:
  - "Def - The Hom Functor and Left Exactness"
  - "Def - Exact Sequence and Short Exact Sequence"
  - "Def - Module Homomorphism"
tags: [algebra, commutative-algebra]
---

# Notation

All rings are commutative with $1$; all modules unital. Fix $R$-modules $Q$ (a source) and $P$ (a target). For an $R$-linear $f : M \to N$:
- $f_* : \operatorname{Hom}_R(Q, M) \to \operatorname{Hom}_R(Q, N)$, $\varphi \mapsto f \circ \varphi$ (covariant);
- $f^* : \operatorname{Hom}_R(N, P) \to \operatorname{Hom}_R(M, P)$, $\varphi \mapsto \varphi \circ f$ (contravariant).
A sequence is [[Def - Exact Sequence and Short Exact Sequence|exact at $B$]] when $\operatorname{im} = \ker$ there. The functors and the notion of [[Def - The Hom Functor and Left Exactness|left exactness]] are defined on the companion page. The full registry is on [[Commutative Algebra III — Flatness and Exactness]].

---

# Statement

> **Theorem (The Hom functors are left exact).** Let $Q, P$ be $R$-modules.
>
> 1. **(Covariant.)** If $0 \to A \xrightarrow{f} B \xrightarrow{g} C$ is exact, then so is
> $$0 \to \operatorname{Hom}_R(Q, A) \xrightarrow{f_*} \operatorname{Hom}_R(Q, B) \xrightarrow{g_*} \operatorname{Hom}_R(Q, C).$$
> 2. **(Contravariant.)** If $A \xrightarrow{f} B \xrightarrow{g} C \to 0$ is exact, then so is
> $$0 \to \operatorname{Hom}_R(C, P) \xrightarrow{g^*} \operatorname{Hom}_R(B, P) \xrightarrow{f^*} \operatorname{Hom}_R(A, P).$$

> **Lemma (Converse / exactness criterion).** If $A \xrightarrow{f} B \xrightarrow{g} C$ is a sequence of $R$-modules such that for *every* $R$-module $P$ the sequence $\operatorname{Hom}_R(C, P) \xrightarrow{g^*} \operatorname{Hom}_R(B, P) \xrightarrow{f^*} \operatorname{Hom}_R(A, P)$ is exact, then $A \xrightarrow{f} B \xrightarrow{g} C$ is itself exact.

The covariant functor preserves the *leading injection*; the contravariant functor, reversing arrows, turns the *trailing surjection* into a leading injection. Neither preserves the surjection at the back — that failure is named by [[Def - Projective Module|projectivity]] (covariant case) and injectivity (contravariant case).

---

# Motivation

This is the mirror of [[Thm - Tensoring is Right Exact|right-exactness of tensoring]], and the two are the foundational exactness facts of the chapter. Where tensoring keeps the surjection at the back and may drop the injection at the front, $\operatorname{Hom}$ keeps the injection at the front and may drop the surjection at the back. Knowing exactly which arrows a functor preserves is what lets you compute with it; this theorem is that knowledge for $\operatorname{Hom}$.

The result earns its keep in two ways. First, directly: it is what justifies treating $\operatorname{Hom}(Q, -)$ and $\operatorname{Hom}(-, P)$ as well-behaved on the injective part of any sequence — for instance, a submodule inclusion $A \hookrightarrow B$ always induces an inclusion of Hom-modules, so $\operatorname{Hom}(Q, A)$ embeds in $\operatorname{Hom}(Q, B)$. Second, and more importantly for this chapter, the **converse lemma** is the engine behind the proof that tensoring is right exact: it says exactness can be *detected* by testing against all $P$, which is the device that converts a statement about $\operatorname{Hom}$ into a statement about the original sequence. So this theorem is both a result about $\operatorname{Hom}$ and the lever that proves the companion result about $\otimes$.

It also tells you precisely where the two definitions of §3.5 come from. $\operatorname{Hom}$ is *only* left exact; the question "when is it *also* right exact, hence fully exact?" has two answers — for the covariant functor it is exactly that $Q$ is [[Def - Projective Module|projective]], for the contravariant it is exactly that $P$ is injective. So left-exactness is the baseline, and projectivity/injectivity are the named hypotheses that restore the missing surjectivity.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "an exact sequence with the right shape"; it is invoked from several entry points.

The first disguised source is **a submodule inclusion $A \hookrightarrow B$**. The property $B$ is "$f$ is injective." The bridge: extend to $0 \to A \xrightarrow{f} B$ and apply the covariant part to get $f_*$ injective, so $\operatorname{Hom}(Q, A) \hookrightarrow \operatorname{Hom}(Q, B)$. The non-obvious value: maps into a submodule are exactly the maps into the big module that land inside it, and they stay distinct. *Example problem:* show that if $A \subseteq B$ then every $Q \to A$ is recoverable from its composite into $B$.

The second disguised source is **a surjection $g : B \twoheadrightarrow C$**, fed to the *contravariant* functor. The property $B$ is "$g$ is onto." The bridge: $g^*$ is injective, $\operatorname{Hom}(C, P) \hookrightarrow \operatorname{Hom}(B, P)$ — two maps out of $C$ that agree after precomposition with a surjection are equal. The non-obvious value: the arrow-reversal converts back-surjectivity into front-injectivity. *Example problem:* deduce that distinct quotient maps stay distinct after pullback along $B \twoheadrightarrow C$.

The third disguised source is **a requirement to prove some sequence is exact**, where direct verification is awkward. The property $B$ is "I want exactness of $A \to B \to C$." The bridge: the converse lemma lets you instead check that $\operatorname{Hom}(-, P)$ of it is exact for *all* $P$, which is sometimes easier (it is how right-exactness of tensor is proved). The non-obvious value: exactness is a representable condition, testable against all targets. *Example problem:* prove a tensored sequence is exact by dualizing into Hom.

**Targets (Output Amplification)**

The conclusion is "the Hom sequence is left exact (injective at front, exact in middle)."

Combine with **projectivity of $Q$** (covariant case). Left-exactness gives the front; if $Q$ is [[Def - Projective Module|projective]], the back surjection survives too, and $E$ is full exactness of $\operatorname{Hom}(Q, -)$. This is nonobvious because left-exactness alone never gives the back, and it is precisely the equivalence "(ii)" of the projectivity characterization. *Use:* lifting maps through surjections.

Combine with **injectivity of $P$** (contravariant case). Left-exactness of $\operatorname{Hom}(-, P)$ becomes full exactness exactly when $P$ is injective, and $E$ is that every map out of a submodule *extends* to the whole module (the Baer criterion's habitat). This is the dual of projectivity and the foundation of injective resolutions. *Use:* extending maps from submodules.

Combine with **the converse lemma to detect exactness**. Given that $\operatorname{Hom}(-, P)$ of a sequence is exact for all $P$, conclude the sequence is exact. $E$ is the right-exactness of tensor (via the adjunction), and more generally any "exactness by testing against all targets" argument. This is nonobvious because it lets a property of *all* Hom-images certify a property of the *single* original sequence.

---

# Why Is It True

The intuition is that **a map into a submodule is determined by, and stays distinct as, a map into the whole module, while a map out of a quotient is determined by, and stays distinct as, a map out of the whole module — but neither lifting nor extending is automatic, which is why only one end of exactness survives.** Take the covariant case. A map $\varphi : Q \to A$ becomes, via $f : A \hookrightarrow B$, the map $f \circ \varphi : Q \to B$ landing inside $A$. Two such become equal in $\operatorname{Hom}(Q, B)$ only if $f \varphi = f \varphi'$, and since $f$ is injective, $\varphi = \varphi'$: distinct maps into the submodule stay distinct, so $f_*$ is injective. In the middle, a map $Q \to B$ lands in $\ker g = \operatorname{im} f = A$ exactly when it is $g_*$-killed, and then (since $f$ is injective onto $A$) it factors uniquely through $f$, giving exactness. What you *cannot* do is *lift* an arbitrary $Q \to C$ to $Q \to B$: that needs choosing preimages compatibly, which can fail, so $g_*$ need not be onto. Hence left-exactness, no more.

**The whole mechanism in one sentence: $\operatorname{Hom}$ preserves the end of an exact sequence that is about "being a sub/quotient" (a *limit*-flavoured condition) and drops the end about "lifting/surjecting" (a *colimit*-flavoured condition), because $\operatorname{Hom}$ is a limit-preserving functor.** Kernels and injections are limits; $\operatorname{Hom}(Q, -)$, being a right adjoint, preserves them; cokernels and surjections are colimits, which it need not preserve. The contravariant $\operatorname{Hom}(-, P)$ sends colimits to limits, which is why it converts the back surjection into a front injection.

---

# What Makes This Hard

The proofs themselves are short element-chases; the difficulty is conceptual, in three places. First, keeping straight that the *contravariant* functor preserves left-exactness *with the ends swapped* — the surjection $\to 0$ at the back becomes the injection $0 \to$ at the front — which is easy to misremember. Second, seeing that the **converse lemma** is the substantive content (the forward directions are routine), and that it requires a clever choice of test module $P$ (one takes $P = B/\operatorname{im} f$, the cokernel, to force the needed factorization). Third, resisting the urge to prove the back surjection is preserved — it is not, and that non-preservation is exactly what projectivity and injectivity are invented to repair. The common error is asserting $g_*$ (or $f^*$) is surjective; it generally is not.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
For each forward statement, chase elements: injectivity at the front from injectivity (covariant) or surjectivity (contravariant) of the original map; exactness in the middle from $\operatorname{im} f = \ker g$ plus the universal factorization of maps through an injection or a surjection. For the converse lemma, plug in two cleverly chosen test modules $P$ — first $P = C$ to force $g \circ f = 0$, then $P = B/\operatorname{im} f$ with the quotient map to force $\ker g \subseteq \operatorname{im} f$.

**Subgoal decomposition:**

1. **Covariant front-injectivity.** Show $f_*$ is injective when $f$ is.
   - *Hint:* $f_*(\varphi) = f\varphi = 0$ and $f$ injective force $\varphi = 0$.
   - *Why needed:* It is the $0 \to$ at the start of the covariant sequence.

2. **Covariant middle-exactness.** Show $\ker g_* = \operatorname{im} f_*$.
   - *Hint:* $g_*\psi = 0 \iff \operatorname{im}\psi \subseteq \ker g = \operatorname{im} f$; since $f$ is injective, $\psi$ factors uniquely as $f\varphi$.
   - *Why needed:* Exactness at the middle term.

3. **Contravariant front-injectivity from surjectivity.** Show $g^*$ is injective when $g$ is onto.
   - *Hint:* $g^*(\psi) = \psi g = 0$ and $g$ onto force $\psi = 0$.
   - *Why needed:* The arrow-reversed $0 \to$.

4. **Contravariant middle-exactness.** Show $\ker f^* = \operatorname{im} g^*$.
   - *Hint:* $f^*\psi = \psi f = 0 \iff \operatorname{im} f \subseteq \ker\psi \iff \psi$ factors through $C = B/\operatorname{im} f = B/\ker g$ via $g$.
   - *Why needed:* Exactness at $\operatorname{Hom}(B,P)$.

5. **Converse lemma.** From exactness of all $\operatorname{Hom}(-, P)$ sequences, deduce exactness of $A \to B \to C$.
   - *Hint:* Plug $P = C$ to get $g f = 0$; plug $P = B/\operatorname{im} f$ and the quotient $h$, note $h \in \ker f^*$, so $h = e g$ for some $e$, giving $\ker g \subseteq \ker h = \operatorname{im} f$.
   - *Why needed:* It is the exactness-detection tool used by [[Thm - Tensoring is Right Exact|right-exactness of tensor]].

---

# Lemma Decomposition

> [!note]- Lemma 1: Covariant Hom is left exact
> **Statement:** If $0 \to A \xrightarrow{f} B \xrightarrow{g} C$ is exact then $0 \to \operatorname{Hom}(Q,A) \xrightarrow{f_*} \operatorname{Hom}(Q,B) \xrightarrow{g_*} \operatorname{Hom}(Q,C)$ is exact.
>
> **Hint:** Front-injectivity from injectivity of $f$; middle from "a map into $\ker g = \operatorname{im} f$ factors uniquely through the injection $f$."
>
> **Why needed:** It is statement (1); it also names projectivity as the condition restoring the missing surjectivity.
>
> > [!note]- Full proof
> > *Injective at front:* if $f_*(\varphi) = f \circ \varphi = 0$ then, $f$ being injective, $\varphi(q) = 0$ for all $q$, so $\varphi = 0$.
> > *Middle:* $g_* f_* = (gf)_* = 0$ since $gf = 0$ (as $\operatorname{im} f = \ker g$), so $\operatorname{im} f_* \subseteq \ker g_*$. Conversely if $\psi : Q \to B$ has $g_*\psi = g\psi = 0$, then $\operatorname{im}\psi \subseteq \ker g = \operatorname{im} f$. As $f : A \to \operatorname{im} f$ is a bijection, $\varphi := f^{-1}\circ\psi : Q \to A$ is $R$-linear with $f_*\varphi = f\varphi = \psi$. Hence $\ker g_* \subseteq \operatorname{im} f_*$.

> [!note]- Lemma 2: Contravariant Hom is left exact
> **Statement:** If $A \xrightarrow{f} B \xrightarrow{g} C \to 0$ is exact then $0 \to \operatorname{Hom}(C,P) \xrightarrow{g^*} \operatorname{Hom}(B,P) \xrightarrow{f^*} \operatorname{Hom}(A,P)$ is exact.
>
> **Hint:** Front-injectivity from surjectivity of $g$; middle from "a map out of $B$ killing $\operatorname{im} f$ descends to the quotient $C = B/\operatorname{im} f$."
>
> **Why needed:** It is statement (2) and the workhorse used by [[Thm - Tensoring is Right Exact|tensoring is right exact]]; injectivity of $P$ is what restores the missing surjectivity.
>
> > [!note]- Full proof
> > *Injective at front:* if $g^*(\psi) = \psi \circ g = 0$ then, $g$ being surjective, $\psi(c) = \psi(g(b)) = 0$ for all $c = g(b)$, so $\psi = 0$.
> > *Middle:* $f^* g^* = (gf)^* = 0$, so $\operatorname{im} g^* \subseteq \ker f^*$. Conversely if $\psi : B \to P$ has $f^*\psi = \psi f = 0$, then $\operatorname{im} f \subseteq \ker\psi$, so $\psi$ factors through $B/\operatorname{im} f = B/\ker g \cong C$ (using $g$ onto with kernel $\operatorname{im} f$): there is $\bar\psi : C \to P$ with $\bar\psi g = \psi$, i.e. $\psi = g^*(\bar\psi)$. Hence $\ker f^* \subseteq \operatorname{im} g^*$.

> [!note]- Lemma 3: The exactness criterion (converse)
> **Statement:** If $\operatorname{Hom}(C,P) \xrightarrow{g^*} \operatorname{Hom}(B,P) \xrightarrow{f^*} \operatorname{Hom}(A,P)$ is exact for every $P$, then $A \xrightarrow{f} B \xrightarrow{g} C$ is exact.
>
> **Hint:** Test $P = C$ to get $\operatorname{im} f \subseteq \ker g$; test $P = B/\operatorname{im} f$ with the quotient map to get $\ker g \subseteq \operatorname{im} f$.
>
> **Why needed:** It is the converse that powers [[Thm - Tensoring is Right Exact|right-exactness of tensor]] — it lets a Hom-exactness fact certify the original sequence.
>
> > [!note]- Full proof
> > *$\operatorname{im} f \subseteq \ker g$:* Take $P = C$ and $\operatorname{id}_C \in \operatorname{Hom}(C, C)$. By exactness at $\operatorname{Hom}(B, P)$ (specifically $\ker f^* \supseteq \operatorname{im} g^*$, giving $f^* g^* = 0$), $f^*(g^*(\operatorname{id}_C)) = \operatorname{id}_C \circ g \circ f = g f = 0$. So $\operatorname{im} f \subseteq \ker g$.
> > *$\ker g \subseteq \operatorname{im} f$:* Take $P = B/\operatorname{im} f$ and the quotient map $h : B \to B/\operatorname{im} f$. Then $f^*(h) = h \circ f = 0$ (as $\operatorname{im} f$ maps to $0$), so $h \in \ker f^* = \operatorname{im} g^*$ by exactness. Thus $h = g^*(e) = e \circ g$ for some $e : C \to B/\operatorname{im} f$. Now if $b \in \ker g$ then $h(b) = e(g(b)) = e(0) = 0$, i.e. $b \in \ker h = \operatorname{im} f$. So $\ker g \subseteq \operatorname{im} f$, completing exactness.

---

# Formal Proof

> [!note]- Complete formal proof
> Statement (1) is Lemma 1 and statement (2) is Lemma 2; the converse lemma is Lemma 3. We assemble them.
>
> **Covariant (1).** Given $0 \to A \xrightarrow{f} B \xrightarrow{g} C$ exact: by Lemma 1, $f_*$ is injective and $\ker g_* = \operatorname{im} f_*$, so $0 \to \operatorname{Hom}(Q,A) \to \operatorname{Hom}(Q,B) \to \operatorname{Hom}(Q,C)$ is exact.
>
> **Contravariant (2).** Given $A \xrightarrow{f} B \xrightarrow{g} C \to 0$ exact: by Lemma 2, $g^*$ is injective and $\ker f^* = \operatorname{im} g^*$, so $0 \to \operatorname{Hom}(C,P) \to \operatorname{Hom}(B,P) \to \operatorname{Hom}(A,P)$ is exact.
>
> **Converse.** Lemma 3 gives exactness of $A \to B \to C$ from exactness of $\operatorname{Hom}(-,P)$ of it for all $P$, via the test modules $P = C$ and $P = B/\operatorname{im} f$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Distinct linear functionals stay distinct after restriction.** For a subspace inclusion $A \hookrightarrow B$ of vector spaces, the contravariant Hom (dualization) gives a surjection $B^* \twoheadrightarrow A^*$ — but consider instead a quotient $B \twoheadrightarrow C$: then $C^* \hookrightarrow B^*$ injects, exactly statement (2) with $P$ the ground field. The application is nonobvious because it is the familiar "the dual of a surjection is an injection" of linear algebra, recognised as left-exactness of contravariant Hom.

**Why short exact sequences of vector spaces always split, via Hom-exactness.** Over a field every module is free hence [[Def - Projective Module|projective]], so $\operatorname{Hom}(Q, -)$ is *fully* exact (not just left exact); the back surjection survives, meaning every map lifts, which is exactly why every short exact sequence of vector spaces splits. The application is nonobvious because it traces a basic linear-algebra fact to the projectivity that upgrades this theorem's left-exactness to exactness.

**Detecting exactness of a complex by testing against all coefficients.** In algebraic topology, a chain complex is exact iff its cochain complexes $\operatorname{Hom}(-, A)$ are exact for all $A$ — the converse lemma in disguise, and the reason universal-coefficient arguments work. The application is nonobvious because it shows the exactness criterion (Lemma 3) is the algebraic foundation under "test homology against every coefficient group."

---

# Bridges

- **[[Thm - Tensoring is Right Exact|Tensoring is Right Exact]]** — the mirror theorem, and the place the converse lemma is *used*. Right-exactness of tensor is proved by applying the contravariant left-exactness here to the sequence $\operatorname{Hom}(-, \operatorname{Hom}(M, L))$ and then transporting across the tensor–Hom adjunction. The two exactness facts are dual faces of one adjunction.

- **[[Def - Projective Module|Projective Module]]** — names the gap in the covariant statement. $\operatorname{Hom}(Q, -)$ is left exact always; it is *fully* exact exactly when $Q$ is projective. So this theorem is the "before" picture and projectivity is the hypothesis completing it.

- **Injective modules** — the dual gap, in the contravariant statement. $\operatorname{Hom}(-, P)$ is fully exact exactly when $P$ is injective; the Baer criterion characterizes such $P$ by the extension property "every map from an ideal extends to $R$." Injective modules are the building blocks of injective resolutions and sheaf cohomology, the exact dual of projective resolutions.

- **The dual module $M^* = \operatorname{Hom}(M, R)$** — taking $P = R$ specializes the contravariant functor to dualization. Left-exactness explains why dualizing reverses arrows and preserves injections-into-surjections, and the *failure* of right-exactness is why $M \to M^{**}$ can fail to be an isomorphism for non-finitely-generated or torsion modules.

---

# Unlocked by This

> [!tip] Injective modules and the Baer criterion *(from Homological Algebra)*
> The contravariant $\operatorname{Hom}(-, P)$ is fully exact exactly when $P$ is **injective**, characterized (Baer) by: every $R$-linear map $I \to P$ from an ideal extends to $R \to P$. Injective modules give injective resolutions and right-derived functors $\operatorname{Ext}^n$, the dual of projective resolutions — and $\mathbb{Q}/\mathbb{Z}$, $\mathbb{Q}$ are the basic injective abelian groups.

> [!tip] Ext as the derived functor of Hom *(from Homological Algebra)*
> Because $\operatorname{Hom}$ is left exact but not exact, its **right-derived functors** $\operatorname{Ext}^n_R(M, N)$ measure the failure of the back surjection to survive — the mirror of $\operatorname{Tor}_n$ for tensor. $\operatorname{Ext}^1$ classifies extensions $0 \to N \to E \to M \to 0$, so the splitting of short exact sequences is governed by the vanishing of $\operatorname{Ext}^1$, tying this theorem to the splitting lemma of §3.5.
