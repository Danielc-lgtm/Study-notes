---
type: definition
subject: category-theory
prereqs:
  - "Def - Functor"
  - "Def - Commutative Diagram"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
tags: [category-theory, foundations]
---

# Notation

Natural transformations are written $\alpha, \beta, \eta, \varepsilon$. For [[Def - Functor|functors]] $F, G : \mathcal{C} \to \mathcal{D}$, a natural transformation $\alpha : F \Rightarrow G$ has, for each object $A$ of $\mathcal{C}$, a **component** $\alpha_A : FA \to GA$, a morphism in $\mathcal{D}$. The double arrow $\Rightarrow$ distinguishes natural transformations (2-cells) from functors and morphisms (1-cells and arrows). A natural isomorphism is written $\alpha : F \xRightarrow{\sim} G$ or $F \cong G$. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Axiom Motivation

We have categories, and maps between them ([[Def - Functor|functors]]). Category theory's recurring instinct is "and now the maps between *those*". A natural transformation is a map between two parallel functors $F, G : \mathcal{C} \to \mathcal{D}$ — but to see why the definition is what it is, recall the problem it was invented to solve. The historical and conceptual seed is the distinction between two ways a [[Def - Vector Space|vector space]] relates to its [[Def - Dual Space|dual]]. A finite-dimensional space $V$ is isomorphic to $V^*$, but only after choosing a basis; there is no isomorphism that works for all spaces simultaneously, compatibly with all linear maps. By contrast $V$ is isomorphic to its double dual $V^{**}$ via a formula that uses no choices: $v \mapsto (\varphi \mapsto \varphi(v))$. The first isomorphism is "unnatural", the second "natural", and Eilenberg and Mac Lane invented categories and functors *precisely to make the word "natural" precise*. So the entire notion exists to capture: **a family of maps, one for each object, that is uniform — compatible with every morphism.**

What does "compatible with every morphism" force? We have, for each object $A$, a map $\alpha_A : FA \to GA$. We want this family to interact correctly with the action of $F$ and $G$ on morphisms. Given $f : A \to B$ in $\mathcal{C}$, there are two ways to travel from $FA$ to $GB$: apply $\alpha_A$ then $Gf$, or apply $Ff$ then $\alpha_B$. Uniformity demands these agree — that the transformation does "the same thing" regardless of whether we transform-then-move or move-then-transform. This is the **naturality square**, and demanding it commute is the only sensible meaning of "the family $\alpha$ respects morphisms":
$$Gf \circ \alpha_A = \alpha_B \circ Ff.$$
**Drop the naturality condition** and you have merely an unrelated bag of morphisms $\alpha_A$ with no coherence — exactly the "unnatural, basis-dependent" isomorphism $V \cong V^*$, which exists componentwise but commutes with no maps. The naturality square is what upgrades a pointwise family to a genuine transformation; it is the [[Def - Commutative Diagram|commutative diagram]] that *is* the definition.

One more thing to notice: naturality is a condition on the *interaction* of the components with morphisms, not a condition on the components individually. Each $\alpha_A$ can be any morphism $FA \to GA$; the constraint binds them together across the morphisms of $\mathcal{C}$. This is why a natural transformation is genuinely more than a function on objects, and why "natural" is a substantive adjective rather than a feeling.

---

# The Definition

Let $F, G : \mathcal{C} \to \mathcal{D}$ be [[Def - Functor|functors]]. A **natural transformation** $\alpha : F \Rightarrow G$ assigns to each object $A$ of $\mathcal{C}$ a morphism (**component**)
$$\alpha_A : FA \longrightarrow GA \quad \text{in } \mathcal{D},$$
such that for every morphism $f : A \to B$ in $\mathcal{C}$ the **naturality square** commutes:
$$\begin{array}{ccc} FA & \xrightarrow{\;\alpha_A\;} & GA \\ \downarrow{\scriptstyle Ff} & & \downarrow{\scriptstyle Gf} \\ FB & \xrightarrow{\;\alpha_B\;} & GB \end{array} \qquad Gf \circ \alpha_A = \alpha_B \circ Ff.$$

A natural transformation $\alpha$ is a **natural isomorphism** if every component $\alpha_A$ is an [[Def - Isomorphism, Monomorphism, Epimorphism|isomorphism]] in $\mathcal{D}$; in that case the componentwise inverses $(\alpha_A)^{-1}$ assemble into a natural transformation $\alpha^{-1} : G \Rightarrow F$ (the inverse naturality square is obtained by inverting the original). We then write $F \cong G$ and say $F$ and $G$ are **naturally isomorphic**.

---

# Categorical / Structural Definition

Natural transformations are the **2-cells** of category theory. There are two ways to compose them. **Vertical composition**: given $\alpha : F \Rightarrow G$ and $\beta : G \Rightarrow H$ (both for the same pair $\mathcal{C} \to \mathcal{D}$), the composite $\beta \circ \alpha : F \Rightarrow H$ has components $(\beta \circ \alpha)_A = \beta_A \circ \alpha_A$. This makes the functors $\mathcal{C} \to \mathcal{D}$ into the objects of a [[Def - Functor Category|functor category]] $[\mathcal{C}, \mathcal{D}]$, with natural transformations as morphisms. **Horizontal composition** (whiskering) combines transformations along functor composition $\mathcal{C} \to \mathcal{D} \to \mathcal{E}$, and the two compositions satisfy the **interchange law** — the structure of a 2-category, developed on [[Def - Functor Category]].

A natural transformation also admits a single packaged description: it is a functor $\mathcal{C} \times \mathbf{2} \to \mathcal{D}$ (a functor out of the product of $\mathcal{C}$ with the [[Def - Category|walking arrow]] $\mathbf{2}$) that restricts to $F$ on $\mathcal{C} \times \{0\}$ and to $G$ on $\mathcal{C} \times \{1\}$. The naturality square is exactly the functoriality of this combined functor on the "square" $f \times (0 \to 1)$. This is the cleanest proof that natural transformations compose correctly — composition of the packaged functors does the bookkeeping automatically.

---

# Relate to Other Fields / Compression

**True name:** *a uniform, choice-free family of morphisms, one per object, commuting with every morphism of the source.* The word "natural" in ordinary mathematical speech — "there is a natural map", "this isomorphism is canonical" — is, when the speaker is being honest, a claim that a certain naturality square commutes. The reflex: whenever you build "the same map for every object by a uniform formula", check the naturality square; if it commutes you have a natural transformation and your construction is canonical, if it does not you have made hidden choices.

The contrast with the single [[Def - Dual Space|dual]] is the sharpest compression of the whole idea. The double dual $(-)^{**} : \mathbf{Vect}_k \to \mathbf{Vect}_k$ is a covariant functor, so the family $\eta_V : V \to V^{**}$ can be — and is — a natural transformation $1 \Rightarrow (-)^{**}$. The single dual $(-)^* : \mathbf{Vect}_k^{\mathrm{op}} \to \mathbf{Vect}_k$ is *contravariant*; there is not even a candidate natural transformation $1_{\mathbf{Vect}_k} \Rightarrow (-)^*$, because the two functors have different variance and the squares could not be drawn. **Naturality is impossible to even state when the variances clash — which is exactly why $V \cong V^*$ is not natural and $V \cong V^{**}$ is.**

---

# Examples / Corollaries

**The double dual.** Define $\eta_V : V \to V^{**}$ by $\eta_V(v) = \mathrm{ev}_v$, where $\mathrm{ev}_v(\varphi) = \varphi(v)$ for $\varphi \in V^*$. This is a natural transformation $\eta : 1_{\mathbf{Vect}_k} \Rightarrow (-)^{**}$: for a [[Def - Linear Map|linear map]] $f : V \to W$, the naturality square $f^{**} \circ \eta_V = \eta_W \circ f$ holds because both sides send $v$ to the functional $\psi \mapsto \psi(f(v))$ on $W^*$ — *no basis is chosen anywhere*. On [[Def - Vector Space|finite-dimensional]] spaces each $\eta_V$ is an isomorphism, so $\eta$ is a natural isomorphism $1 \cong (-)^{**}$ on $\mathbf{FinVect}_k$. This is the historical motivating example and the one to keep in working memory.

**The determinant.** For each commutative [[Def - Ring|ring]] $R$, the [[Def - Determinant|determinant]] is a [[Def - Homomorphism|group homomorphism]] $\det_R : \mathrm{GL}_n(R) \to R^\times$ from invertible $n \times n$ matrices to units. As $R$ varies, $\mathrm{GL}_n(-)$ and $(-)^\times$ are both functors $\mathbf{CRing} \to \mathbf{Grp}$, and $\det$ is a natural transformation $\det : \mathrm{GL}_n \Rightarrow (-)^\times$. Naturality says: for a ring homomorphism $\varphi : R \to S$, computing $\det$ then applying $\varphi$ equals applying $\varphi$ entrywise to the matrix then computing $\det$ — which holds because the determinant is a fixed polynomial in the entries, and $\varphi$ respects $+$ and $\times$. **The determinant is "the same formula in every ring", and that uniformity is precisely naturality.**

**Singleton inclusion.** The map $\eta_X : X \to P(X)$, $x \mapsto \{x\}$, is a natural transformation $\eta : 1_{\mathbf{Set}} \Rightarrow P$ from the identity to the covariant power-set [[Def - Functor|functor]]: for $f : X \to Y$ the square $P(f) \circ \eta_X = \eta_Y \circ f$ says $f(\{x\}) = \{f(x)\}$, which is true. (This $\eta$ is the unit of the power-set monad — a forward connection to Chapter V.)

**Is NOT a natural transformation — the basis isomorphism $V \cong V^*$.** Choosing a basis of each finite-dimensional $V$ gives an isomorphism $V \to V^*$, but the family is *not* natural: there is no consistent choice making all the squares commute, and in any case $(-)^*$ is contravariant so the square cannot even be formed against the identity functor. This is the non-example that gives the whole subject its name.

**Calibration check.** Verify that for the double dual, both routes around the naturality square send $v \mapsto (\psi \mapsto \psi(f(v)))$. Verify that the components of a natural isomorphism's inverse really are natural (invert the naturality square). Confirm you can explain in one sentence why $\det$ being a polynomial in matrix entries forces its naturality.

---

# Unlocked by This

> [!tip] The Yoneda Lemma *(from this subject, Chapter II)*
> The [[Thm - The Yoneda Lemma|Yoneda lemma]] computes the *set of all natural transformations* out of a representable functor: $[\mathcal{C}^{\mathrm{op}}, \mathbf{Set}](\mathcal{C}(-, A), G) \cong GA$, naturally. Natural transformations between hom-functors turn out to be just elements of a set — the most important calculation in the subject, and it is a calculation about naturality squares.

> [!tip] Chain Homotopies and Derived Functors *(from Homological Algebra)*
> A [[Def - Chain Map and Chain Homotopy|chain homotopy]] is a natural transformation up to boundary, and the natural transformations between **derived functors** (the connecting maps of long exact sequences, the comparison maps of $\mathrm{Tor}$ and $\mathrm{Ext}$) are the structural glue of homological algebra. Naturality is what makes long exact sequences functorial.

> [!tip] Monads and Categorical Probability *(from this subject, Chapter V)*
> A **monad** is an endofunctor with two natural transformations (unit $\eta$ and multiplication $\mu$) satisfying coherence. The **Giry/probability monad** — whose algebras are convex spaces and whose Kleisli category houses **Markov categories** — packages "form distributions over" as a monad. Naturality of $\eta$ and $\mu$ is the backbone of categorical probability.
