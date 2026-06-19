---
type: theorem
subject: category-theory
prereqs:
  - "Def - Functor"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
  - "Def - Full, Faithful, and Essentially Surjective Functor"
tags: [category-theory, foundations]
---

# Notation

$F : \mathcal{C} \to \mathcal{D}$ is a [[Def - Functor|functor]], sending objects $A \mapsto FA$ and morphisms $f \mapsto Ff$ with $F(g \circ f) = Fg \circ Ff$ and $F(1_A) = 1_{FA}$. An [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphism]] is a morphism $f$ with a two-sided inverse $f^{-1}$. A functor is [[Def - Full, Faithful, and Essentially Surjective Functor|fully faithful]] if each action $\mathcal{C}(A,B) \to \mathcal{D}(FA, FB)$ is a bijection. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Statement

> **Theorem (Functors preserve isomorphisms).** Let $F : \mathcal{C} \to \mathcal{D}$ be a [[Def - Functor|functor]] and let $f : A \to B$ be an [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphism]] in $\mathcal{C}$. Then $Ff : FA \to FB$ is an isomorphism in $\mathcal{D}$, with inverse
> $$(Ff)^{-1} = F(f^{-1}).$$
> Consequently $F$ sends isomorphic objects to isomorphic objects: $A \cong B \implies FA \cong FB$.

> **Corollary (Fully faithful functors reflect isomorphisms).** If $F$ is [[Def - Full, Faithful, and Essentially Surjective Functor|fully faithful]] and $Ff : FA \to FB$ is an isomorphism in $\mathcal{D}$, then $f$ is already an isomorphism in $\mathcal{C}$.

The theorem says isomorphisms are *preserved* by every functor; the corollary says they are *reflected* by fully faithful functors. Both are needed downstream — note that monomorphisms and epimorphisms are **not** preserved by functors in general (see Why Is It True).

---

# Motivation

This is the first theorem of the subject, and it earns its place by certifying that functors do the one thing we built them to do: respect "sameness". A [[Def - Functor|functor]] was defined to preserve composition and identities; the immediate dividend is that it preserves the notion built from composition and identities, namely isomorphism. Without this, the entire transfer principle of category theory would be unsound — you could not conclude that two objects are "the same" downstream from their being "the same" upstream.

The corollary is the deeper and more useful statement. A [[Def - Full, Faithful, and Essentially Surjective Functor|fully faithful]] functor not only preserves isomorphisms but *reflects* them: if the images are isomorphic, the originals already were. This is exactly the property that makes the [[Def - The Yoneda Embedding|Yoneda embedding]] an embedding and underwrites the (⟸) direction of [[Thm - Characterization of Equivalence|the characterization of equivalence]]. The role of this little theorem, then, is foundational plumbing: it is invoked silently every time one argues "$F$ is an equivalence, so this iso upstairs gives an iso downstairs and vice versa".

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is literally "$f$ is an isomorphism", so the source question is: when does a problem hand you an isomorphism without announcing it?

The first disguised source is **a morphism with a known one-sided inverse plus a cancellation argument**. If you have $g \circ f = 1$ and separately know $f$ is epi (or $g$ is mono), the one-sided inverse upgrades to two-sided, so $f$ is an iso and the theorem applies. *Example problem:* show that applying the [[Def - Functor|free functor]] $F : \mathbf{Set} \to \mathbf{Grp}$ to a bijection of sets yields an isomorphism of free groups — recognize the bijection as an iso in $\mathbf{Set}$, then transport.

The second disguised source is **an object defined by a universal property**. Universal objects are unique *up to unique isomorphism*, so any two solutions of the same universal problem are canonically isomorphic; feeding that iso through a functor preserves it. *Example problem:* the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] gives $G/\ker\varphi \cong \operatorname{im}\varphi$; apply any functor (abelianization, a representation) and conclude the images are isomorphic, with no new computation.

The third disguised source is **a chain of isomorphisms or a commuting diagram of isos**. Composites of isomorphisms are isomorphisms, so a path of isos in $\mathcal{C}$ feeds through $F$ to a path of isos in $\mathcal{D}$. *Example problem:* in algebraic topology, a [[Def - Homotopy Equivalence and Contractible Space|homotopy equivalence]] induces isomorphisms on every [[Def - Singular Homology|homology group]] $H_n$, because $H_n$ is a functor (to be precise on the homotopy category) and homotopy equivalences are isomorphisms there.

**Targets (Output Amplification)**

The bare conclusion is "$Ff$ is an iso". Combined with other facts it does more.

Combine with **a computation of $FA$ and $FB$**. If you can compute the images on objects and they are *not* isomorphic, the contrapositive forces $A \not\cong B$ — a functor becomes an **invariant** that distinguishes objects. This is the entire strategy of algebraic topology: $\pi_1(S^1) = \mathbb{Z} \neq 0 = \pi_1(\text{point})$, so $S^1 \not\cong \text{point}$ (not homotopy equivalent). The further result $E$ is a non-isomorphism proof, obtained from a functor that separates the images.

Combine with **fully faithfulness (the corollary)**. If $F$ is fully faithful, "$Ff$ iso" and "$f$ iso" become equivalent, so you may check isomorphy in whichever category is easier. The further result is a transport-of-isomorphism in both directions, the workhorse of equivalence arguments.

Combine with **essential surjectivity**. If $F$ also hits every object up to iso, then "isomorphism class of $FA$" ranges over all of $\mathcal{D}$, and preservation-plus-reflection of isos means $F$ induces a *bijection* on isomorphism classes of objects. The further result is half of the proof that $F$ is an [[Def - Equivalence of Categories|equivalence]].

---

# Why Is It True

A functor preserves every equation between composites, because that is its defining property. An isomorphism is *defined* by two such equations, $g \circ f = 1_A$ and $f \circ g = 1_B$. Apply $F$ to both: functoriality turns the composites into composites and the identities into identities, so $Fg \circ Ff = 1_{FA}$ and $Ff \circ Fg = 1_{FB}$ — which is the statement that $Ff$ is an isomorphism with inverse $Fg = F(f^{-1})$. There is nothing more to it.

**The whole content is that "isomorphism" is written purely in the language a functor is sworn to preserve — composition and identities — so preservation is automatic.** This also explains the limits of the theorem. [[Def - Isomorphism, Monomorphism, Epimorphism|Monomorphism]] and [[Def - Isomorphism, Monomorphism, Epimorphism|epimorphism]] are *not* defined by equations between specific composites; they are defined by a *cancellation* property quantified over all test objects ("$f \circ g = f \circ h \implies g = h$"). A functor has no obligation to that quantified statement — it might fail to be surjective on the relevant arrows, so the cancellation that held upstairs need not hold downstairs. Concretely, the inclusion $\mathbb{Z} \hookrightarrow \mathbb{Q}$ is epi in $\mathbf{CRing}$, but the forgetful functor $\mathbf{CRing} \to \mathbf{Set}$ sends it to the non-surjective (hence non-epi) inclusion of underlying sets. So functors preserve isos but not monos/epis, and the reason is exactly the difference between an equational definition and a quantified one.

The corollary's intuition: a [[Def - Full, Faithful, and Essentially Surjective Functor|fully faithful]] functor sets up a bijection between $\mathcal{C}(A,B)$ and $\mathcal{D}(FA,FB)$, so the inverse arrow that exists downstairs *must come from* an arrow upstairs, and faithfulness forces that arrow to satisfy the inverse equations. The hom-set bijection transports the inverse back up.

---

# What Makes This Hard

The theorem itself is a two-line consequence of the axioms; the only way to get it wrong is to forget that *both* defining equations of an isomorphism must be pushed through $F$. The genuine subtlety, and where intuition misleads, is the corollary's hypothesis: students expect *every* functor to reflect isomorphisms, but reflection requires fully faithfulness. The forgetful functor $\mathbf{Top} \to \mathbf{Set}$ does not reflect isos — a continuous bijection is an iso of underlying sets without being a homeomorphism. The error to avoid is conflating preservation (true for all functors) with reflection (true only for fully faithful ones).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Apply $F$ to the two equations defining the inverse, and read off that $F(f^{-1})$ is the inverse of $Ff$. For the corollary, use fullness to lift the downstairs inverse to an upstairs morphism, then faithfulness to verify it is a genuine inverse.

**Subgoal decomposition:**

1. **Preservation.** Show $Ff$ is an iso with inverse $F(f^{-1})$.
   - *Hint:* Apply $F$ to $f^{-1} \circ f = 1_A$ and $f \circ f^{-1} = 1_B$; use $F(g\circ f) = Fg \circ Ff$ and $F(1) = 1$.
   - *Why needed:* This is the theorem; the corollary builds on it.

2. **Lift the inverse (corollary).** Given $Ff$ iso with inverse $h : FB \to FA$, produce $g : B \to A$ with $Fg = h$.
   - *Hint:* Use **fullness** — every morphism $FB \to FA$ is $Fg$ for some $g$.
   - *Why needed:* The candidate inverse upstairs must exist before it can be checked.

3. **Verify the inverse (corollary).** Show $g \circ f = 1_A$ and $f \circ g = 1_B$.
   - *Hint:* $F(g \circ f) = Fg \circ Ff = h \circ Ff = 1_{FA} = F(1_A)$; now use **faithfulness** to drop the $F$. Symmetrically for the other side.
   - *Why needed:* Produces the two-sided inverse, completing "$f$ is an iso".

---

# Lemma Decomposition

> [!note]- Lemma 1: A functor preserves the inverse equations
> **Statement:** If $f^{-1} \circ f = 1_A$ and $f \circ f^{-1} = 1_B$ in $\mathcal{C}$, then $F(f^{-1}) \circ Ff = 1_{FA}$ and $Ff \circ F(f^{-1}) = 1_{FB}$ in $\mathcal{D}$.
>
> **Hint:** Apply $F$ to each equation and use the two functor axioms.
>
> **Why needed:** This *is* preservation — it directly exhibits $F(f^{-1})$ as the two-sided inverse of $Ff$.
>
> > [!note]- Full proof
> > Apply $F$ to $f^{-1} \circ f = 1_A$. By preservation of composition, $F(f^{-1} \circ f) = F(f^{-1}) \circ Ff$, and by preservation of identities $F(1_A) = 1_{FA}$. Equating, $F(f^{-1}) \circ Ff = 1_{FA}$. The same applied to $f \circ f^{-1} = 1_B$ gives $Ff \circ F(f^{-1}) = 1_{FB}$. Hence $Ff$ is an isomorphism with inverse $F(f^{-1})$.

> [!note]- Lemma 2: Fullness lifts the candidate inverse
> **Statement:** If $F$ is full and $Ff$ has a two-sided inverse $h : FB \to FA$ in $\mathcal{D}$, then there is $g : B \to A$ in $\mathcal{C}$ with $Fg = h$.
>
> **Hint:** Fullness is exactly surjectivity of $\mathcal{C}(B, A) \to \mathcal{D}(FB, FA)$.
>
> **Why needed:** Reflection cannot even begin until the inverse downstairs is named by something upstairs.
>
> > [!note]- Full proof
> > By fullness, the action $F_{B,A} : \mathcal{C}(B, A) \to \mathcal{D}(FB, FA)$ is surjective. Since $h \in \mathcal{D}(FB, FA)$, there is $g \in \mathcal{C}(B, A)$ with $Fg = h$.

> [!note]- Lemma 3: Faithfulness verifies the inverse
> **Statement:** With $g$ as in Lemma 2, $g \circ f = 1_A$ and $f \circ g = 1_B$, so $f$ is an isomorphism.
>
> **Hint:** Compute $F(g \circ f)$ and recognize it as $F(1_A)$; then drop $F$ using injectivity on hom-sets.
>
> **Why needed:** Faithfulness is the step that turns an equation about images into an equation about the originals — the heart of reflection.
>
> > [!note]- Full proof
> > $F(g \circ f) = Fg \circ Ff = h \circ Ff = 1_{FA} = F(1_A)$, where the third equality is because $h$ is the inverse of $Ff$. Since $F$ is faithful, $F_{A,A}$ is injective, so $F(g \circ f) = F(1_A)$ forces $g \circ f = 1_A$. Symmetrically, $F(f \circ g) = Ff \circ Fg = Ff \circ h = 1_{FB} = F(1_B)$ gives $f \circ g = 1_B$. Thus $f$ is an isomorphism with inverse $g$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Preservation.** Let $f : A \to B$ be an isomorphism with inverse $f^{-1} : B \to A$, so $f^{-1} \circ f = 1_A$ and $f \circ f^{-1} = 1_B$. Apply the functor $F$, using $F(g \circ f') = Fg \circ Ff'$ and $F(1_X) = 1_{FX}$:
> $$F(f^{-1}) \circ Ff = F(f^{-1} \circ f) = F(1_A) = 1_{FA},$$
> $$Ff \circ F(f^{-1}) = F(f \circ f^{-1}) = F(1_B) = 1_{FB}.$$
> Hence $Ff$ is an isomorphism with $(Ff)^{-1} = F(f^{-1})$. In particular if $A \cong B$ via some iso then $FA \cong FB$.
>
> **Corollary (reflection for fully faithful $F$).** Suppose $F$ is fully faithful and $Ff$ is an isomorphism, with inverse $h : FB \to FA$.
>
> By fullness (Lemma 2), choose $g : B \to A$ with $Fg = h$. Then
> $$F(g \circ f) = Fg \circ Ff = h \circ Ff = 1_{FA} = F(1_A),$$
> and by faithfulness (injectivity of $F_{A,A}$), $g \circ f = 1_A$. Symmetrically,
> $$F(f \circ g) = Ff \circ Fg = Ff \circ h = 1_{FB} = F(1_B),$$
> and faithfulness gives $f \circ g = 1_B$. Therefore $f$ is an isomorphism with inverse $g$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Homotopy invariance of homology.** The functor $H_n : \mathbf{Top} \to \mathbf{Ab}$ (singular [[Def - Singular Homology|homology]]) sends [[Def - Homotopy Equivalence and Contractible Space|homotopy equivalences]] to isomorphisms. Phrased through this theorem: homotopy equivalences are isomorphisms in the homotopy category, and $H_n$ factors through it, so it preserves them. This is the basis for computing homology by replacing a space with a simpler homotopy-equivalent one.

**Group invariants distinguish groups.** Functors $\mathbf{Grp} \to \mathbf{Set}$ such as "order of the group", "number of elements of order 2", or "abelianization" are isomorphism invariants by this theorem. To prove two groups non-isomorphic, exhibit a functor whose values differ — the contrapositive of preservation. This is why "they have different numbers of elements of order 2" is a valid non-isomorphism proof.

**Spectra of rings.** Applying the contravariant [[Def - Functor|Spec functor]] to a ring isomorphism gives a homeomorphism of spectra: $R \cong S \implies \mathrm{Spec}\,R \cong \mathrm{Spec}\,S$ in $\mathbf{Top}$. Conversely, if two affine schemes are non-homeomorphic the rings are non-isomorphic. This is the algebra-geometry dictionary respecting isomorphism in both directions.

---

# Bridges

- **[[Thm - Characterization of Equivalence|Characterization of Equivalence]]** — the corollary here is a load-bearing lemma there. To prove a full, faithful, essentially surjective functor $F$ is an equivalence, one constructs a quasi-inverse $G$ and must show the unit and counit are *natural isomorphisms*; reflection of isos (this corollary) is what certifies the relevant components are invertible. The two results are usually proved back to back.

- **[[Def - The Yoneda Embedding|Yoneda Embedding]]** — the embedding is fully faithful, so by the corollary it reflects isomorphisms: two objects of $\mathcal{C}$ are isomorphic if and only if their representable presheaves are. This is the precise sense in which "an object is determined by its functor of points".

- **[[Thm - First Isomorphism Theorem|First Isomorphism Theorem]]** — supplies isomorphisms to feed in. Any isomorphism produced upstream (a quotient identified, a universal object pinned down) is transported by every functor, so structural isomorphisms propagate through all the functors in sight without re-proof.

---

# Unlocked by This

> [!tip] Algebraic Invariants and the Method of Algebraic Topology *(from Algebraic Topology)*
> The recipe "build a functor $\mathbf{Top} \to \mathbf{Alg}$, compute it on two spaces, observe the values are non-isomorphic, conclude the spaces are non-homeomorphic" is *entirely* this theorem in contrapositive. [[Def - Singular Homology|Homology]], the [[Def - Path-Product and the Fundamental Group|fundamental group]], and cohomology are all isomorphism-invariant because they are functors, and that single fact powers the whole discipline.
