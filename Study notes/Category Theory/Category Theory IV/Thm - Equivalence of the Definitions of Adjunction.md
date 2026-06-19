---
type: theorem
subject: category-theory
prereqs:
  - "Def - Adjunction"
  - "Def - Unit and Counit of an Adjunction"
  - "Def - Universal Property and Universal Arrow"
  - "Thm - The Yoneda Lemma"
tags: [category-theory, foundations]
---

# Notation

$F : \mathcal{C} \to \mathcal{D}$ and $G : \mathcal{D} \to \mathcal{C}$ are [[Def - Functor|functors]]. The candidate adjunction data are: a family of bijections $\Phi_{A,B} : \mathcal{D}(FA, B) \cong \mathcal{C}(A, GB)$; or [[Def - Natural Transformation|natural transformations]] $\eta : 1_{\mathcal{C}} \Rightarrow GF$ (unit) and $\varepsilon : FG \Rightarrow 1_{\mathcal{D}}$ (counit); or, for each $A$, an object $FA \in \mathcal{D}$ with a [[Def - Universal Property and Universal Arrow|universal arrow]] $\eta_A : A \to GFA$. We write $(A \downarrow G)$ for the comma category whose objects are pairs $(B, g : A \to GB)$. The full symbol registry is on [[Category Theory IV — Adjunctions]].

---

# Statement

> **Theorem (Equivalence of the Definitions of Adjunction).** For functors $F : \mathcal{C} \to \mathcal{D}$ and $G : \mathcal{D} \to \mathcal{C}$, the following structures are equivalent, and each determines the others:
>
> 1. **(Hom-set isomorphism.)** A bijection $\Phi_{A,B} : \mathcal{D}(FA, B) \cong \mathcal{C}(A, GB)$ natural in $A$ and $B$.
> 2. **(Unit-counit.)** Natural transformations $\eta : 1_{\mathcal{C}} \Rightarrow GF$ and $\varepsilon : FG \Rightarrow 1_{\mathcal{D}}$ satisfying the triangle identities $(\varepsilon F)\circ(F\eta) = 1_F$ and $(G\varepsilon)\circ(\eta G) = 1_G$.
> 3. **(Universal arrows.)** For each $A \in \mathcal{C}$, a universal arrow from $A$ to $G$: an object $FA \in \mathcal{D}$ and a morphism $\eta_A : A \to GFA$ such that every $g : A \to GB$ factors uniquely as $g = G f \circ \eta_A$ for a unique $f : FA \to B$. Equivalently, $\eta_A$ is an [[Def - Initial and Terminal Object|initial object]] of the comma category $(A \downarrow G)$.
>
> The correspondences are: $\eta_A = \Phi(1_{FA})$ and $\varepsilon_B = \Phi^{-1}(1_{GB})$; conversely $\Phi(f) = Gf \circ \eta_A$ and $\Phi^{-1}(g) = \varepsilon_B \circ Fg$. Any one of the three structures may be taken as the definition of an adjunction $F \dashv G$.

---

# Motivation

An adjunction is one relationship, but it can be *presented* in three radically different idioms, and the reason the subject is hard at first is that textbooks switch between them without warning. This theorem is the licence to switch. It says the bijection-of-hom-sets idiom (good for computing transposes), the unit-counit idiom (good for $2$-categorical algebra and for passing to monads), and the universal-arrow idiom (good for *constructing* adjunctions from universal properties) are interchangeable descriptions of the same data.

The practical force is that you get to *choose your battlefield*. To **prove** an adjunction exists you usually have a universal property in hand (Chapter II), so you use form (3) — exhibit a universal arrow for each object, with no naturality square to verify by hand. To **use** an adjunction inside a larger argument — to build a monad, to run a $2$-categorical mate calculation — you carry form (2), the unit and counit. To **compute** a specific transpose you use form (1), the bijection. Without this theorem each of these would be a separate notion; with it, they are one, and the choice is purely tactical.

The deepest part of the theorem is that the *naturality* of the bijection in form (1) is **the same information** as the *triangle identities* in form (2). Naturality looks like infinitely many commuting squares; the triangle identities look like two equations. The theorem says these contain exactly the same content, because the bijection is determined by where it sends identities (Yoneda), and the two triangle identities are precisely the two conditions that make the resulting transpose formulas mutually inverse.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's hypotheses are mild — just two functors and one of the three data packages — so the real source question is: *what disguised situations hand you one of the three forms?*

The first disguised source is **a universal property from Chapter II**, which is form (3) in costume. Any time you have proved "$X$ is the universal object with property $P$", you have a universal arrow, and if such an object exists *for every input* and the construction is functorial, you have the data of (3) and hence (by this theorem) a full adjunction. *Example problem:* the [[Def - Free Group and Free Product|free group]] $FS$ has the universal property "homomorphisms out of $FS$ are functions out of $S$"; this is a universal arrow $\eta_S : S \to UFS$ for each $S$, so by the theorem $F \dashv U$ — with no hom-set naturality to check directly.

The second disguised source is **a representability statement**, which is form (1) seen through Yoneda. If you can show the functor $\mathcal{C}(A, G-) : \mathcal{D} \to \mathbf{Set}$ is [[Def - Hom-Functor and Representable Functor|representable]] for each $A$, with representing object $FA$, then $\mathcal{D}(FA, -) \cong \mathcal{C}(A, G-)$, which is half of (1); functoriality of $A \mapsto FA$ supplies the rest. *Example problem:* show $\mathbf{Top} \to \mathbf{Set}$ has a left adjoint by checking that "functions $S \to UY$" is representable in $Y$ by the discrete space on $S$.

The third disguised source is **a pair of natural transformations that look like they should be inverse but live in different categories** — form (2) waiting to be recognised. Whenever you have a "unit-like" $\eta : 1 \Rightarrow GF$ ("insertion") and a "counit-like" $\varepsilon : FG \Rightarrow 1$ ("evaluation"), checking the two triangle identities is *all* you need to conclude an adjunction. *Example problem:* given completion $\eta : X \to \widehat{X}$ and the identity-on-complete-spaces $\varepsilon$, verify the triangle identities to conclude completion is left adjoint to the inclusion.

**Targets (Output Amplification)**

The conclusion is "the three forms agree", and combining it with other facts is where it pays off.

Combine with **monad theory** (Chapter V): once you have form (2), the unit $\eta$ and the morphism $\mu = G\varepsilon F$ make $GF$ a [[Def - Monad and Comonad|monad]]. The theorem is what lets you start from *any* presentation of the adjunction (say a hom-set bijection) and still extract the monad — you convert to form (2) first. The further result is that every adjunction, however presented, produces a monad and a comonad.

Combine with **uniqueness of universal objects**: form (3) plus [[Thm - Uniqueness of Universal Objects|uniqueness of universal objects]] gives that the left adjoint is determined up to unique isomorphism, which is the content of [[Thm - Adjoints are Unique up to Natural Isomorphism]]. The further result is that "the" adjoint deserves its definite article.

Combine with **RAPL**: form (1) is the input to the proof that [[Thm - Right Adjoints Preserve Limits|right adjoints preserve limits]] — the limit-preservation proof commutes the bijection $\Phi$ past the legs of a limit cone. The theorem guarantees that no matter how the adjunction was handed to you, you can convert to the hom-set form and run RAPL.

---

# Why Is It True

The whole theorem is powered by one observation from the [[Thm - The Yoneda Lemma|Yoneda lemma]]: **a natural isomorphism between hom-functors is completely determined by where it sends a single identity morphism.** Fix $A$. The bijection $\Phi_{A,-} : \mathcal{D}(FA, -) \cong \mathcal{C}(A, G-)$ is a natural isomorphism of functors $\mathcal{D} \to \mathbf{Set}$; by Yoneda it is determined by the image of $1_{FA} \in \mathcal{D}(FA, FA)$, namely the element $\eta_A := \Phi(1_{FA}) \in \mathcal{C}(A, GFA)$. And the formula reconstructing $\Phi$ from that element is exactly $\Phi(f) = Gf \circ \eta_A$ — this is the Yoneda reconstruction. So form (1) and "an element $\eta_A$ for each $A$" carry the same information, and "$\eta_A$ for each $A$, naturally" is form (3): a universal arrow, because saying $\Phi(f) = Gf\circ\eta_A$ is a *bijection* is exactly saying every $g : A \to GB$ factors uniquely through $\eta_A$.

That handles (1) $\Leftrightarrow$ (3). For (1) $\Leftrightarrow$ (2), the same reconstruction gives both $\eta$ (from identities on the $F$ side) and $\varepsilon$ (from identities on the $G$ side), and now the question is precisely *which* pairs $(\eta, \varepsilon)$ come from a genuine bijection. The transpose formulas $\Phi(f) = Gf\circ\eta_A$ and $\Phi^{-1}(g) = \varepsilon_B \circ Fg$ are forced; for them to be mutually inverse you compute $\Phi^{-1}(\Phi(f))$ and $\Phi(\Phi^{-1}(g))$ and find that each reduces to the identity *exactly when a triangle identity holds*.

> **The mechanism in one line:** naturality of $\Phi$ says "$\Phi$ is reconstructed from its value on identities" (Yoneda), and the two triangle identities are precisely the two equations that make the reconstructed transpose-and-untranspose operations cancel.

So the three forms are not "equivalent by a clever argument"; they are the same object viewed through Yoneda. The bijection *is* its unit and counit, and the triangle identities *are* its naturality, just written compactly.

---

# What Makes This Hard

The hard step is seeing that the two triangle identities are equivalent to full naturality of $\Phi$ — most people accept "$\Phi$ natural $\Rightarrow$ triangle identities" but stumble on the converse, where you must *recover* naturality from just two equations using the forced transpose formulas. The common error is to verify only one triangle identity and assume the other follows by symmetry; it does not, because the two identities guard the two different directions of the bijection's invertibility ($\Phi^{-1}\Phi = \mathrm{id}$ versus $\Phi\Phi^{-1} = \mathrm{id}$). A second common slip is forgetting the whiskering: writing the triangle identity as "$\varepsilon\circ\eta$" rather than "$\varepsilon F \circ F\eta$" is a type error, since $\eta$ and $\varepsilon$ live in different categories.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Define the unit and counit by transposing identities. Use Yoneda to show the bijection is reconstructed from the unit via $\Phi(f) = Gf\circ\eta_A$. Then show the reconstructed maps $\Phi, \Phi^{-1}$ are mutually inverse *iff* the triangle identities hold, and that $\Phi$ is natural *iff* $\eta, \varepsilon$ are natural transformations.

**Subgoal decomposition:**

1. **(1) $\Rightarrow$ (2): build $\eta, \varepsilon$ and derive the triangle identities.** Set $\eta_A = \Phi(1_{FA})$, $\varepsilon_B = \Phi^{-1}(1_{GB})$.
   - *Hint:* Naturality of $\Phi$ in each variable forces $\eta, \varepsilon$ to be natural transformations; the triangle identities come from transposing $1_{FA}$ and $1_{GB}$ through both naturality squares.
   - *Why needed:* Produces the data of (2) from the data of (1).

2. **(2) $\Rightarrow$ (1): build $\Phi$ and prove it is a bijection.** Define $\Phi(f) = Gf\circ\eta_A$ and $\Psi(g) = \varepsilon_B\circ Fg$.
   - *Hint:* Compute $\Psi(\Phi(f))$ and $\Phi(\Psi(g))$; each collapses to the identity using *one* triangle identity together with naturality of $\eta$ or $\varepsilon$.
   - *Why needed:* Shows the unit-counit data reconstructs a genuine natural bijection.

3. **(1) $\Leftrightarrow$ (3): identify the bijection with a universal arrow.** Show "$\Phi(f) = Gf\circ\eta_A$ is a bijection" is the same as "$\eta_A$ is universal".
   - *Hint:* "Every $g : A \to GB$ equals $Gf\circ\eta_A$ for a unique $f$" is literally bijectivity of $f \mapsto Gf\circ\eta_A$; restate as initiality in $(A\downarrow G)$.
   - *Why needed:* Connects the hom-set form to the universal-property form of Chapter II.

4. **Naturality $\Leftrightarrow$ triangle identities (the subtle equivalence).** Confirm that the two halves of naturality of $\Phi$ correspond exactly to the two triangle identities.
   - *Hint:* Each triangle identity is the naturality square for $\Phi$ evaluated at an identity; conversely the general naturality square follows from the identity case by functoriality.
   - *Why needed:* This is the non-trivial content — that two equations encode infinitely many commuting squares.

---

# Lemma Decomposition

> [!note]- Lemma 1: A natural transformation of representables is determined by one element (Yoneda)
> **Statement:** A natural transformation $\alpha : \mathcal{D}(D, -) \Rightarrow K$ (for $K : \mathcal{D} \to \mathbf{Set}$) is determined by the single element $\alpha_D(1_D) \in K(D)$, via $\alpha_B(f) = K(f)(\alpha_D(1_D))$.
>
> **Hint:** This is the [[Thm - The Yoneda Lemma|Yoneda lemma]]: $\mathrm{Nat}(\mathcal{D}(D,-), K) \cong K(D)$, evaluation at $1_D$.
>
> **Why needed:** It is the engine: the adjunction bijection is a natural iso of representables, so it is pinned down by its value on the identity, which is the unit/counit. Every reconstruction formula in the proof is an instance of this lemma.
>
> > [!note]- Full proof
> > By naturality of $\alpha$, for $f : D \to B$ the square relating $\mathcal{D}(D, D) \to \mathcal{D}(D, B)$ (postcompose with $f$) and $K(D) \to K(B)$ ($K(f)$) commutes. Chasing $1_D$ around: $\alpha_B(f \circ 1_D) = \alpha_B(f) = K(f)(\alpha_D(1_D))$. So $\alpha$ is determined by $\alpha_D(1_D)$, and conversely any element $u \in K(D)$ defines a natural $\alpha$ by $\alpha_B(f) = K(f)(u)$.

> [!note]- Lemma 2: The transpose formulas are forced
> **Statement:** If $\Phi_{A,B} : \mathcal{D}(FA, B) \cong \mathcal{C}(A, GB)$ is natural and $\eta_A := \Phi(1_{FA})$, then $\Phi(f) = Gf \circ \eta_A$ for all $f : FA \to B$; dually with $\varepsilon_B := \Phi^{-1}(1_{GB})$, $\Phi^{-1}(g) = \varepsilon_B \circ Fg$.
>
> **Hint:** Apply Lemma 1 to the natural iso $\Phi_{A,-} : \mathcal{D}(FA,-) \Rightarrow \mathcal{C}(A, G-)$, whose value on $1_{FA}$ is $\eta_A$ and on which $\mathcal{C}(A, G-)$ acts by postcomposition with $Gf$.
>
> **Why needed:** Fixes the only possible formulas relating $\Phi$ to $\eta, \varepsilon$; all subsequent computations use these.
>
> > [!note]- Full proof
> > Naturality of $\Phi$ in $B$ says: for $f : FA \to B$, regarded as $f \circ 1_{FA}$, $\Phi(f) = \Phi(f \circ 1_{FA}) = Gf \circ \Phi(1_{FA}) = Gf \circ \eta_A$, using $\Phi(k\circ f') = Gk\circ\Phi(f')$ with $f' = 1_{FA}$, $k = f$. The dual computation, using naturality of $\Phi^{-1}$ in $A$, gives $\Phi^{-1}(g) = \varepsilon_B \circ Fg$.

> [!note]- Lemma 3: Mutual-inverse $\Leftrightarrow$ triangle identities
> **Statement:** With $\Phi(f) = Gf\circ\eta_A$ and $\Psi(g) = \varepsilon_B\circ Fg$, one has $\Psi\circ\Phi = \mathrm{id}$ iff $(\varepsilon F)\circ(F\eta) = 1_F$, and $\Phi\circ\Psi = \mathrm{id}$ iff $(G\varepsilon)\circ(\eta G) = 1_G$.
>
> **Hint:** Compute $\Psi(\Phi(1_{FA}))$ and $\Phi(\Psi(1_{GB}))$ and use naturality of $\varepsilon$ and $\eta$ to reduce to a triangle identity.
>
> **Why needed:** This is the heart — it shows the two equations of (2) are exactly the bijectivity of (1).
>
> > [!note]- Full proof
> > Compute $\Psi(\Phi(f))$ for $f : FA \to B$: $\Psi(\Phi(f)) = \Psi(Gf\circ\eta_A) = \varepsilon_B \circ F(Gf\circ\eta_A) = \varepsilon_B\circ FGf\circ F\eta_A$. By naturality of $\varepsilon$ applied to $f : FA \to B$, $\varepsilon_B \circ FGf = f\circ\varepsilon_{FA}$. So $\Psi(\Phi(f)) = f\circ\varepsilon_{FA}\circ F\eta_A = f\circ(\varepsilon_{FA}\circ F\eta_A)$. This equals $f$ for all $f$ iff $\varepsilon_{FA}\circ F\eta_A = 1_{FA}$ for all $A$, i.e. iff $(\varepsilon F)\circ(F\eta) = 1_F$. The computation of $\Phi(\Psi(g)) = (G\varepsilon_B\circ\eta_{GB})\circ g$-style reduction, using naturality of $\eta$, gives $\Phi\circ\Psi = \mathrm{id}$ iff $(G\varepsilon)\circ(\eta G) = 1_G$.

> [!note]- Lemma 4: Universal arrow $=$ bijection $f \mapsto Gf\circ\eta_A$
> **Statement:** "$\eta_A : A \to GFA$ is a universal arrow from $A$ to $G$" is equivalent to "$f \mapsto Gf\circ\eta_A$ is a bijection $\mathcal{D}(FA, B) \to \mathcal{C}(A, GB)$ for every $B$".
>
> **Hint:** Universality says every $g : A \to GB$ has a unique $f : FA \to B$ with $g = Gf\circ\eta_A$ — that is surjectivity plus injectivity of $f\mapsto Gf\circ\eta_A$.
>
> **Why needed:** Identifies form (3) with form (1) directly, completing the triangle of equivalences.
>
> > [!note]- Full proof
> > By definition, $\eta_A$ is universal iff for every $(B, g)$ with $g : A \to GB$ there is a *unique* $f : FA \to B$ with $Gf\circ\eta_A = g$. "Exists" is surjectivity of $f \mapsto Gf\circ\eta_A$; "unique" is injectivity. So universality is exactly bijectivity of $f \mapsto Gf\circ\eta_A$ for each $B$, which is form (1) by Lemma 2. Initiality in $(A\downarrow G)$ is a restatement: $(FA, \eta_A)$ has a unique morphism to every object $(B, g)$.

---

# Formal Proof

> [!note]- Complete formal proof
> We prove (1) $\Rightarrow$ (2), (2) $\Rightarrow$ (1), and (1) $\Leftrightarrow$ (3); together these give the full equivalence with the stated correspondences.
>
> **Step 0 — the data.** Assume the functors $F, G$ are given. We freely use that $\Phi$ being a natural bijection means both halves: $\Phi(k\circ f) = Gk\circ\Phi(f)$ (naturality in the codomain) and $\Phi(f\circ Fh) = \Phi(f)\circ h$ (naturality in the domain).
>
> **Step 1 — (1) $\Rightarrow$ (2).** Define $\eta_A = \Phi_{A,FA}(1_{FA})$ and $\varepsilon_B = \Phi^{-1}_{GB, B}(1_{GB})$. Naturality of $\Phi$ in $A$ gives, for $h : A' \to A$: $\eta_A \circ h = \Phi(1_{FA})\circ h = \Phi(1_{FA}\circ Fh) = \Phi(Fh) $ and $GFh\circ\eta_{A'} = GFh\circ\Phi(1_{FA'}) = \Phi(Fh\circ 1_{FA'}) = \Phi(Fh)$, so $\eta_A\circ h = GFh\circ\eta_{A'}$: $\eta$ is natural. Dually $\varepsilon$ is natural. By Lemma 3, the bijectivity of $\Phi$ (which holds by hypothesis) forces both triangle identities. So (2) holds.
>
> **Step 2 — (2) $\Rightarrow$ (1).** Define $\Phi(f) = Gf\circ\eta_A$ and $\Psi(g) = \varepsilon_B\circ Fg$. Both are natural in $A$ and $B$ (compositions of natural pieces). By Lemma 3, the two triangle identities give $\Psi\circ\Phi = \mathrm{id}$ and $\Phi\circ\Psi = \mathrm{id}$, so $\Phi$ is a natural bijection with inverse $\Psi$. So (1) holds, and the correspondence formulas are exactly the definitions of $\Phi, \Psi$.
>
> **Step 3 — (1) $\Leftrightarrow$ (3).** By Lemma 2, $\Phi(f) = Gf\circ\eta_A$ where $\eta_A = \Phi(1_{FA})$. By Lemma 4, $\Phi_{A,-}$ being a bijection for all $B$ is equivalent to $\eta_A$ being a universal arrow from $A$ to $G$, equivalently $(FA, \eta_A)$ being initial in $(A\downarrow G)$. Functoriality of $A \mapsto FA$ is automatic: given $h : A' \to A$, $Fh : FA' \to FA$ is the unique morphism with $GFh\circ\eta_{A'} = \eta_A\circ h$, by universality of $\eta_{A'}$. So the family of universal arrows assembles into the functor $F$ and the natural unit $\eta$. Hence (1) $\Leftrightarrow$ (3).
>
> **Conclusion.** Forms (1), (2), (3) are equivalent and mutually determining, with $\eta_A = \Phi(1_{FA})$, $\varepsilon_B = \Phi^{-1}(1_{GB})$, $\Phi(f) = Gf\circ\eta_A$, $\Phi^{-1}(g) = \varepsilon_B\circ Fg$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Galois connections (order theory).** For posets viewed as categories, all three forms degenerate: the bijection becomes the bi-implication $f(a)\leq b \iff a \leq g(b)$, the unit and counit become $a \leq g(f(a))$ and $f(g(b))\leq b$, and the triangle identities are automatic (posets have at most one morphism per hom-set). Verifying the equivalence here is a clean low-dimensional sanity check — it shows the triangle identities carry *no* extra information in the poset case, which clarifies what they add in general.

**Free constructions (algebra).** Take the [[Def - Free Group and Free Product|free group]] and verify that its Chapter II universal property (form 3) yields, through this theorem, the hom-set bijection (form 1) and the unit-counit pair (form 2) — insertion of generators and "multiply a word out". This shows that the universal-property proofs you already did *are* adjunction proofs.

**Tensor-hom (homological algebra).** The [[Thm - Universal Property of the Tensor Product of Modules|universal property of the tensor product]] is form (3) for the adjunction $-\otimes_R M \dashv \mathrm{Hom}_R(M,-)$: the universal bilinear map $A \times M \to A\otimes M$ is the unit. Recovering the hom-set bijection $\mathrm{Hom}(A\otimes M, B)\cong\mathrm{Hom}(A,\mathrm{Hom}(M,B))$ via the theorem is a good test that you can move between forms in a category that is not a category of sets-with-structure-over-$\mathbf{Set}$.

---

# Bridges

- **[[Thm - The Yoneda Lemma|The Yoneda Lemma]]** — the proof's engine. The adjunction bijection $\Phi_{A,-}$ is a natural isomorphism of representable functors, so Yoneda says it is determined by its value on a single identity, which is the unit. Every reconstruction formula ($\Phi(f) = Gf\circ\eta_A$) is the Yoneda reconstruction of a natural transformation from its defining element. Without Yoneda the equivalence of (1) and (3) would have no clean proof.

- **[[Def - Universal Property and Universal Arrow|Universal Arrows]]** — form (3) is literally a family of universal arrows. This theorem is what upgrades "a universal property at each object" to "an adjunction", and it is the precise statement that the Chapter II material was secretly about adjunctions all along.

- **[[Thm - Adjoints are Unique up to Natural Isomorphism|Uniqueness of Adjoints]]** — a corollary via form (3). Since the left adjoint is built from universal arrows and universal objects are unique up to unique isomorphism, the adjoint is determined up to unique natural isomorphism.

- **[[Def - Monad and Comonad|Monads]]** (Chapter V) — consume form (2). Building the monad $GF$ requires the unit and counit and uses the triangle identities to verify the monad axioms; this theorem guarantees you can extract that data from any presentation of the adjunction.

---

# Unlocked by This

> [!tip] Mates and the Calculus of Adjunctions *(from 2-Category Theory)*
> Once an adjunction is the data $(\eta, \varepsilon)$ with triangle identities, the entire **calculus of adjoints** — composing adjunctions, whiskering, and the **mates correspondence** (natural transformations between adjoints correspond to natural transformations between their adjoints) — becomes formal $2$-categorical algebra. This is the foundation of *formal category theory* and of string-diagram reasoning in higher categories.

> [!tip] Doctrines and Categorical Semantics *(from Categorical Logic)*
> The universal-arrow form makes adjunctions the carriers of **logical structure**: quantifiers $\exists, \forall$ are left and right adjoints to substitution (pullback), and this "adjoints model logical connectives" slogan, due to Lawvere, organizes all of categorical logic and the semantics of type theory.
