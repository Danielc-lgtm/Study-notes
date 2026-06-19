---
type: definition
subject: category-theory
prereqs:
  - "Def - Adjunction"
  - "Def - Natural Transformation"
  - "Def - Functor"
tags: [category-theory, foundations]
---

# Notation

Throughout, $F : \mathcal{C} \to \mathcal{D}$ and $G : \mathcal{D} \to \mathcal{C}$ are [[Def - Functor|functors]] with $F \dashv G$ (see [[Def - Adjunction]]), and $\Phi_{A,B} : \mathcal{D}(FA, B) \cong \mathcal{C}(A, GB)$ is the natural bijection. We write $1_{\mathcal{C}}$ for the identity functor on $\mathcal{C}$, and for a [[Def - Natural Transformation|natural transformation]] $\alpha$ and functor $H$ we write $H\alpha$ and $\alpha H$ for the **whiskered** transformations: $(H\alpha)_X = H(\alpha_X)$ and $(\alpha H)_X = \alpha_{HX}$. Vertical composition of natural transformations is $\circ$. The full symbol registry is on [[Category Theory IV — Adjunctions]].

This is a compound page: it defines three interlocking notions — the **unit** $\eta$, the **counit** $\varepsilon$, and the **triangle identities** they satisfy — because they are introduced together and none is fully usable without the others. The unit and counit are the data; the triangle identities are the axioms that make that data an adjunction.

---

# Axiom Motivation

The hom-set definition of an adjunction ([[Def - Adjunction]]) is clean but abstract: it is a family of bijections, and a family of bijections is awkward to compute with and impossible to draw. We want a *finite* package of concrete data — a couple of morphisms and a couple of equations — that contains the same information. The unit and counit are that package, and the triangle identities are the equations that make it faithful.

Where do the unit and counit come from? The bijection $\Phi$ lets us transpose *any* morphism, so transpose the ones we always have for free: the identities. For each $A$, transpose the identity $1_{FA} : FA \to FA$ across $\Phi_{A, FA}$ to get a morphism $\eta_A := \Phi(1_{FA}) : A \to GFA$. Naturality of $\Phi$ forces these to assemble into a natural transformation $\eta : 1_{\mathcal{C}} \Rightarrow GF$, the **unit**. Dually, for each $B$ transpose $1_{GB} : GB \to GB$ the other way to get $\varepsilon_B := \Phi^{-1}(1_{GB}) : FGB \to B$, the **counit** $\varepsilon : FG \Rightarrow 1_{\mathcal{D}}$. So the unit and counit are not arbitrary; they are the *shadows of the identities* under the adjunction. This is the crucial idea: an isomorphism of hom-functors is, by [[Thm - The Yoneda Lemma|Yoneda]], pinned down by where it sends a single identity element — and the unit and counit are exactly those Yoneda witnesses.

Now, can we *recover* $\Phi$ from $\eta$ and $\varepsilon$? Yes, and the formula is forced. To transpose a general $f : FA \to B$, factor it through the universal $\eta_A$: naturality gives $\Phi(f) = Gf \circ \eta_A$. To transpose a general $g : A \to GB$ back, $\Phi^{-1}(g) = \varepsilon_B \circ Fg$. So the unit and counit determine the whole bijection. But not every pair $(\eta, \varepsilon)$ of natural transformations of the right shape arises this way — we need the two formulas to be mutually inverse, $\Phi^{-1}\Phi = \mathrm{id}$ and $\Phi\Phi^{-1} = \mathrm{id}$. Writing those two conditions out and simplifying is exactly what produces the **triangle identities**:
$$(\varepsilon F) \circ (F\eta) = 1_F \qquad\text{and}\qquad (G\varepsilon) \circ (\eta G) = 1_G.$$

Let us see why each triangle identity is needed and what it means. The first, $(\varepsilon F)\circ(F\eta) = 1_F$, says: apply $F$ to the unit to get $F\eta_A : FA \to FGFA$, then apply the counit $\varepsilon_{FA} : FGFA \to FA$, and you are back to the identity on $FA$. In the free-group picture this reads: insert the generators of $S$ into the free group ($\eta_S$), regard the result as living over $UFS$ and form the free group on *that* (apply $F$), then multiply each one-letter word out ($\varepsilon$) — and you recover the original generators. The second identity, $(G\varepsilon)\circ(\eta G) = 1_G$, is the dual statement on the $G$ side. **If you drop the first triangle identity, $\Phi^{-1}\Phi$ need not be the identity, so $\Phi$ is not a bijection and you do not have an adjunction; if you drop the second, $\Phi\Phi^{-1}$ fails.** Each identity guards one direction of the bijection's invertibility. A pair $(\eta, \varepsilon)$ satisfying *neither* is just two unrelated natural transformations; satisfying *one but not the other* gives a "half-adjunction" with a one-sided inverse, which is genuinely weaker.

Why are the components of $\eta$ and $\varepsilon$ not literally inverse morphisms? Because they live in different categories: $\eta_A : A \to GFA$ is a morphism in $\mathcal{C}$, while $\varepsilon_B : FGB \to B$ is a morphism in $\mathcal{D}$, and the two are not composable. The triangle identities are the closest sensible statement — they say $\varepsilon$ is a one-sided inverse of $\eta$ *after translating one of them across $F$ or $G$ so that they live in the same category*. This is why the identities involve the whiskerings $F\eta, \varepsilon F$ and $\eta G, G\varepsilon$ rather than $\eta$ and $\varepsilon$ raw. Reading "$\varepsilon \circ \eta = 1$" with no whiskering is a type error.

---

# The Definition

Let $F \dashv G$ with natural bijection $\Phi$.

The **unit** of the adjunction is the [[Def - Natural Transformation|natural transformation]]
$$\eta : 1_{\mathcal{C}} \Rightarrow GF, \qquad \eta_A := \Phi_{A, FA}(1_{FA}) : A \to GFA.$$

The **counit** of the adjunction is the natural transformation
$$\varepsilon : FG \Rightarrow 1_{\mathcal{D}}, \qquad \varepsilon_B := \Phi_{GB, B}^{-1}(1_{GB}) : FGB \to B.$$

These satisfy the **triangle identities**: as equations of natural transformations,
$$(\varepsilon F) \circ (F\eta) = 1_F \quad (\text{in } [\mathcal{C}, \mathcal{D}]), \qquad (G\varepsilon) \circ (\eta G) = 1_G \quad (\text{in } [\mathcal{D}, \mathcal{C}]).$$
Componentwise, for $A \in \mathcal{C}$ and $B \in \mathcal{D}$,
$$\varepsilon_{FA} \circ F(\eta_A) = 1_{FA}, \qquad G(\varepsilon_B) \circ \eta_{GB} = 1_{GB}.$$

The transpose of a morphism is recovered from this data by
$$\Phi(f) = Gf \circ \eta_A \quad (f : FA \to B), \qquad \Phi^{-1}(g) = \varepsilon_B \circ Fg \quad (g : A \to GB).$$

Conversely (the content of [[Thm - Equivalence of the Definitions of Adjunction]]): given functors $F, G$ and natural transformations $\eta : 1_{\mathcal{C}} \Rightarrow GF$, $\varepsilon : FG \Rightarrow 1_{\mathcal{D}}$ satisfying the two triangle identities, the formulas above define a natural bijection $\Phi$, hence an adjunction $F \dashv G$.

---

# Relate to Other Fields / Compression

The triangle identities are the categorification of the **zig-zag identities** for dual vector spaces. If $V$ is a finite-dimensional [[Def - Vector Space|vector space]] with dual $V^*$, there is a coevaluation $\mathrm{coev} : k \to V \otimes V^*$ (the "name of the identity", $1 \mapsto \sum e_i \otimes e^i$) and an evaluation $\mathrm{ev} : V^* \otimes V \to k$, and they satisfy $(\mathrm{ev} \otimes 1)\circ(1 \otimes \mathrm{coev}) = 1_V$ — visibly the same zig-zag shape as $(\varepsilon F)\circ(F\eta) = 1_F$. Coevaluation is a unit, evaluation a counit, and "$V$ is dualizable" is "$V \dashv V^*$ as $1$-morphisms in the monoidal category". Adjunctions in a general $2$-category abstract exactly this picture, and the triangle identities are the zig-zags drawn as string diagrams.

In the poset / Galois-connection special case, the unit and counit degenerate into the two inequalities defining a monotone Galois connection. For $f \dashv g$ between posets, $\eta_a : a \leq g(f(a))$ and $\varepsilon_b : f(g(b)) \leq b$, and the triangle identities are automatic because hom-sets in a poset have at most one element. So "unit $\leq$, counit $\leq$" is the order-theoretic shadow of the unit-counit data.

**True name:** the **unit is "insertion of generators"** and the **counit is "evaluation"**. Whenever an adjunction is concrete, $\eta_A$ is the universal map embedding $A$ into the underlying object of its free construction (the inclusion of generators, the inclusion into the completion, the unit map to the abelianisation), and $\varepsilon_B$ is the universal map that "evaluates" a free construction on actual data back down to $B$ (multiply a formal word out, sum a formal linear combination, evaluate a function at a point). When you meet a new adjunction, the fastest way to understand it is to identify what its unit inserts and what its counit evaluates.

---

# Examples / Corollaries

**Is an instance — free group.** For free $\dashv$ forgetful $F \dashv U$ on $\mathbf{Grp}$, the unit $\eta_S : S \to UFS$ sends each $s \in S$ to itself viewed as a one-letter word in the [[Def - Free Group and Free Product|free group]] — this is the insertion of generators. The counit $\varepsilon_H : FUH \to H$ takes a formal word $h_1 h_2 \cdots h_n$ of elements of $H$ (an element of the free group on the underlying set of $H$) and multiplies it out using the actual multiplication of $H$. The first triangle identity $\varepsilon_{FS} \circ F\eta_S = 1_{FS}$ says: include generators, form the free group on the resulting one-letter words, then multiply each one-letter word out — you get back the generators. The second, $U\varepsilon_H \circ \eta_{UH} = 1_{UH}$, says: include the elements of $H$ as one-letter words, then multiply each out — the identity on $UH$.

**Is an instance — currying in $\mathbf{Set}$.** For $-\times B \dashv (-)^B$ (see [[Def - Cartesian Closed Category]]), the counit is **evaluation** $\varepsilon_C : C^B \times B \to C$, $(\phi, b) \mapsto \phi(b)$, and the unit is $\eta_A : A \to (A\times B)^B$, $a \mapsto (b \mapsto (a,b))$. The first triangle identity is the statement that currying then evaluating returns the original two-argument function — the basic computation rule of the lambda calculus.

**Is an instance — abelianisation.** For the reflector $L = (-)^{ab} : \mathbf{Grp} \to \mathbf{Ab}$ left adjoint to the inclusion $\iota : \mathbf{Ab} \hookrightarrow \mathbf{Grp}$, the unit $\eta_G : G \to G/[G,G]$ is the quotient map onto the abelianisation, and the counit $\varepsilon_A : (\iota A)^{ab} \to A$ is an isomorphism (because an abelian group is already its own abelianisation). When the counit is an isomorphism the subcategory is [[Def - Reflective Subcategory|reflective]]; this is the defining feature.

**Is NOT an instance — natural transformations with no triangle identity.** Take $\mathcal{C} = \mathcal{D} = \mathbf{Set}$, $F = G = \mathrm{id}$, and let $\eta = \varepsilon = $ "the identity natural transformation". These satisfy both triangle identities trivially. But now perturb: keep $\eta = 1$ and set $\varepsilon_B = $ the constant map collapsing everything (where one exists). Then $\eta, \varepsilon$ are still natural transformations of the right *shape*, but $(\varepsilon F)\circ(F\eta) = \varepsilon \neq 1$, so the triangle identity fails and there is **no** adjunction — confirming that the shape of the data is not enough; the identities are the content.

**Corollary — the unit at a free object computes the universal arrow.** The unit component $\eta_A : A \to GFA$ is a [[Def - Universal Property and Universal Arrow|universal arrow]] from $A$ to $G$: every $g : A \to GB$ factors uniquely as $Gf \circ \eta_A$. This is the form of the data that connects directly to Chapter II.

**Corollary — an equivalence is an adjunction with invertible unit and counit.** If both $\eta$ and $\varepsilon$ are natural isomorphisms, then $F$ and $G$ are inverse [[Def - Equivalence of Categories|equivalences]] (an *adjoint equivalence*), and conversely every equivalence can be upgraded to one. So equivalences sit inside adjunctions as the case where the universal arrows are isomorphisms.

**Calibration check.** Verify that $\eta_A = \Phi(1_{FA})$ and $\varepsilon_B = \Phi^{-1}(1_{GB})$ by transposing the identity and reading off the formula $\Phi(f) = Gf\circ\eta_A$ at $f = 1_{FA}$. Confirm the two triangle identities have the correct *types* — that $\varepsilon_{FA}\circ F\eta_A$ is a morphism $FA \to FA$ in $\mathcal{D}$ and $G\varepsilon_B \circ \eta_{GB}$ is a morphism $GB \to GB$ in $\mathcal{C}$. Finally, explain in one sentence why "$\varepsilon \circ \eta = 1$" without whiskering is a type error.

---

# Unlocked by This

> [!tip] Every Adjunction Gives a Monad *(from Chapter V)*
> The unit $\eta$ and the counit-built multiplication $\mu = G\varepsilon F$ make $T = GF$ a **monad** on $\mathcal{C}$: the monad unit *is* the adjunction unit, and the monad axioms are consequences of the triangle identities and naturality. Dually $FG$ is a **comonad** on $\mathcal{D}$. This is the bridge to [[Def - Monad and Comonad|monads]] and to **Thm - Every Adjunction Gives a Monad**, the launching point of Chapter V and of the **probability monad** in categorical probability.

> [!tip] Adjunctions in a 2-Category and Dualizable Objects *(from Higher Category Theory / TQFT)*
> The triangle identities make sense for any $1$-morphisms in a $2$-category, defining **adjunctions internally**. In a monoidal category (a one-object $2$-category) they become the zig-zag identities of a **dualizable object**, the structure underlying **TQFT** via the cobordism hypothesis. See Chapter VII.
