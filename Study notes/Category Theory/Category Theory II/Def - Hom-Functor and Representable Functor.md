---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Functor"
  - "Def - Natural Transformation"
  - "Def - Opposite Category and Duality"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a **locally small** category — every hom-collection $\mathcal{C}(A, B)$ is an honest set, not a proper class — so that the constructions below land in $\mathbf{Set}$. Objects are $A, B, C, X, Y$; morphisms $f, g, h$; the hom-set $\mathcal{C}(A, B) = \mathrm{Hom}_{\mathcal{C}}(A, B)$. We write $f_* = \mathcal{C}(A, f)$ for *post*composition by $f$ and $f^* = \mathcal{C}(f, B)$ for *pre*composition by $f$. The named example categories are $\mathbf{Set}, \mathbf{Grp}, \mathbf{Ring}, \mathbf{CRing}$ (commutative unital rings), $\mathbf{Top}$, $\mathbf{Vect}_k$, $R\text{-}\mathbf{Mod}$. The full registry is on [[Category Theory II — Universal Properties, Representability, and the Yoneda Lemma]].

This is a compound page: it defines four interlocking notions — the **covariant hom-functor** $\mathcal{C}(A, -)$, the **contravariant hom-functor** $\mathcal{C}(-, B)$, a **representable functor**, and a **representing object** — because they are introduced together and a representable functor is *defined* as one isomorphic to a hom-functor, so neither half is usable alone.

---

# Axiom Motivation

The slogan of the chapter is that an object is determined by its relationships, by the network of arrows touching it. To make that slogan into mathematics we need to package "all the arrows out of $A$" and "all the arrows into $B$" as honest functorial gadgets. That packaging is the hom-functor, and asking whether a given $\mathbf{Set}$-valued functor *is* such a package is the notion of representability.

Fix an object $A$. The collection of all morphisms out of $A$ is, object by object, the assignment $X \mapsto \mathcal{C}(A, X)$. This should be a functor $\mathcal{C} \to \mathbf{Set}$, and there is only one natural way to make it one: a morphism $f : X \to Y$ should turn an arrow $A \to X$ into an arrow $A \to Y$ by *post*composition, $g \mapsto f \circ g$. Check functoriality and it works on the nose — identities go to identities, composites to composites — so $\mathcal{C}(A, -)$ is a covariant functor. Now fix instead a target $B$ and look at all morphisms *into* $B$: the assignment $X \mapsto \mathcal{C}(X, B)$. A morphism $f : X \to Y$ now turns an arrow $Y \to B$ into an arrow $X \to B$ by *pre*composition, $g \mapsto g \circ f$ — note the direction has flipped, because precomposition with $f : X \to Y$ sends $\mathcal{C}(Y, B) \to \mathcal{C}(X, B)$. So $\mathcal{C}(-, B)$ is *contravariant*: a functor $\mathcal{C}^{op} \to \mathbf{Set}$. The variance is not a convention to be memorized; it is forced by which slot you fix and which slot composition can act on.

Why should we care about a functor that just reports hom-sets? Because of the converse question, which is where all the power lives. Many functors $F : \mathcal{C} \to \mathbf{Set}$ arising in practice are *not* obviously hom-functors — the forgetful functor $\mathbf{Grp} \to \mathbf{Set}$, the functor sending a ring to its set of units, the functor sending a commutative ring to the solution set of a fixed system of polynomial equations. The astonishing empirical fact is that an enormous number of them turn out to be naturally isomorphic to some $\mathcal{C}(A, -)$. When that happens we say $F$ is **representable** and $A$ **represents** it, and the consequences are immediate and strong: by the [[Thm - The Yoneda Lemma|Yoneda lemma]] the representing object is determined up to unique isomorphism, the natural isomorphism is pinned down by a single **universal element** (see [[Def - Universal Element]]), and $F$ inherits every formal property a hom-functor has — for instance it preserves all limits. Representability is therefore a way to discover that a seemingly unstructured set-valued construction is secretly "the set of maps out of (or into) a single object", which collapses many questions about $F$ to questions about that one object $A$.

One more motivating constraint: why insist $\mathcal{C}$ be locally small? Because if $\mathcal{C}(A, X)$ were a proper class, $\mathcal{C}(A, -)$ would not land in $\mathbf{Set}$ and the whole comparison with $\mathbf{Set}$-valued functors would be ill-typed. Local smallness is exactly the hygiene condition that makes hom-functors legal.

---

# The Definition

Let $\mathcal{C}$ be a locally small category.

**Covariant hom-functor.** For a fixed object $A \in \mathcal{C}$, the **covariant hom-functor** $\mathcal{C}(A, -) : \mathcal{C} \to \mathbf{Set}$ sends an object $X$ to the set $\mathcal{C}(A, X)$, and a morphism $f : X \to Y$ to the function
$$f_* = \mathcal{C}(A, f) : \mathcal{C}(A, X) \to \mathcal{C}(A, Y), \qquad g \mapsto f \circ g \quad (\text{postcomposition}).$$

**Contravariant hom-functor.** For a fixed object $B \in \mathcal{C}$, the **contravariant hom-functor** $\mathcal{C}(-, B) : \mathcal{C}^{op} \to \mathbf{Set}$ sends an object $X$ to $\mathcal{C}(X, B)$, and a morphism $f : X \to Y$ to
$$f^* = \mathcal{C}(f, B) : \mathcal{C}(Y, B) \to \mathcal{C}(X, B), \qquad g \mapsto g \circ f \quad (\text{precomposition}).$$

**Representable functor and representing object.** A functor $F : \mathcal{C} \to \mathbf{Set}$ is **representable** if there is an object $A \in \mathcal{C}$ and a [[Def - Natural Transformation|natural isomorphism]]
$$\eta : \mathcal{C}(A, -) \xrightarrow{\ \cong\ } F.$$
The pair $(A, \eta)$ is a **representation**, $A$ is a **representing object**, and one says $A$ **represents** $F$. Dually, a contravariant functor $F : \mathcal{C}^{op} \to \mathbf{Set}$ is representable if $F \cong \mathcal{C}(-, B)$ for some $B$. (Some authors call the covariant case *corepresentable*; we follow Riehl and let the variance of $F$ disambiguate.)

---

# Categorical / Structural Definition

The two hom-functors are the two slots of a single two-variable functor, the **hom-bifunctor**
$$\mathcal{C}(-, -) : \mathcal{C}^{op} \times \mathcal{C} \to \mathbf{Set}, \qquad (X, Y) \mapsto \mathcal{C}(X, Y),$$
contravariant in the first slot (precomposition) and covariant in the second (postcomposition), with the two actions commuting — this commuting is the *functoriality of composition*. Fixing the first slot at $A$ gives the covariant $\mathcal{C}(A, -)$; fixing the second at $B$ gives the contravariant $\mathcal{C}(-, B)$. Representability of $F : \mathcal{C} \to \mathbf{Set}$ then says: $F$ lies in the image, up to natural isomorphism, of the assignment $A \mapsto \mathcal{C}(A, -)$ — that is, $F$ is in the *essential image of the Yoneda embedding* $\mathbf{y}$ (see [[Def - The Yoneda Embedding]]). This is the cleanest one-line definition of representability and the form used in [[Thm - The Yoneda Embedding is Fully Faithful]].

---

# Relate to Other Fields / Compression

The covariant hom-functor $\mathcal{C}(A, -)$ is "the view of the category from $A$, looking out"; the contravariant $\mathcal{C}(-, B)$ is "the view of the category looking into $B$". A representable functor is one that turns out to be exactly one of these views. The existing vault page [[Def - The Hom Functor and Left Exactness]] studies the *module-specific* hom-functor $\mathrm{Hom}_R(M, -) : R\text{-}\mathbf{Mod} \to R\text{-}\mathbf{Mod}$, which is the covariant hom-functor of the category $R\text{-}\mathbf{Mod}$ here — *enriched* to land in modules rather than mere sets, because hom-sets of modules are themselves modules. That page's "left exactness" is the statement that $\mathrm{Hom}_R(M, -)$ preserves kernels; the general fact behind it, proved categorically, is that *every covariant hom-functor preserves all limits* (a representable functor is continuous). Do not conflate the two pages: ours is the general categorical hom-functor, theirs is the module instance with extra structure.

**True name:** a representable functor is *a set-valued functor that is secretly "maps out of (or into) a single object"*. The operational reflex: when a $\mathbf{Set}$-valued functor $F$ shows up, ask "is there one object $A$ such that an element of $F(X)$ is the same as a morphism $A \to X$?" If yes, $F$ is representable, $A$ is forced up to unique isomorphism, and the matching is recorded by a single universal element $u \in F(A)$, namely the image of $1_A$.

---

# Examples / Corollaries

**Is an instance — $U : \mathbf{Grp} \to \mathbf{Set}$ is represented by $\mathbb{Z}$.** The forgetful functor sending a group to its underlying set is representable: there is a natural bijection
$$\mathbf{Grp}(\mathbb{Z}, G) \cong U(G), \qquad \varphi \mapsto \varphi(1).$$
A homomorphism $\mathbb{Z} \to G$ is completely determined by the image of the generator $1$, and any element of $G$ is a legal image; this is the statement that $\mathbb{Z}$ is the [[Def - Free Group and Free Product|free group on one generator]] (see [[Def - Group]]). So "an element of $G$" and "a homomorphism $\mathbb{Z} \to G$" are the same thing, naturally in $G$. This is the cleanest possible illustration of representability: the underlying-set functor is "maps out of $\mathbb{Z}$".

**Is an instance — $U : \mathbf{Ring} \to \mathbf{Set}$ is represented by $\mathbb{Z}[x]$.** A ring homomorphism $\mathbb{Z}[x] \to R$ is determined by the image of $x$, which may be any element of $R$, so $\mathbf{Ring}(\mathbb{Z}[x], R) \cong U(R)$ naturally — $\mathbb{Z}[x]$ is the free ring on one generator. Drilled in [[Ex - Representable forgetful functors]].

**Is an instance — the forgetful $U : \mathbf{Top} \to \mathbf{Set}$ is represented by the one-point space.** A continuous map from the one-point space $* $ into $X$ picks out a point of $X$, and every point arises uniquely, so $\mathbf{Top}(*, X) \cong U(X)$ naturally.

**Is an instance — the units functor on $\mathbf{CRing}$.** The functor $(-)^\times : \mathbf{CRing} \to \mathbf{Set}$ sending a ring to its set of *units* (invertible elements) is represented by the Laurent polynomial ring $\mathbb{Z}[x, x^{-1}]$: a ring map $\mathbb{Z}[x, x^{-1}] \to R$ must send $x$ to a unit (since $x$ is invertible, with inverse $x^{-1}$), and conversely any unit is a legal image. So $\mathbf{CRing}(\mathbb{Z}[x, x^{-1}], R) \cong R^\times$. This is the algebraic group $\mathbb{G}_m$ of the AG callout below.

> [!note]- Algebraic geometry background: the functor of points and the affine line
> No algebraic geometry is assumed; everything is built from scratch here. A **commutative ring** $R$ is a set with $+, \times$ both commutative and associative, with $0, 1$, additive inverses, and distributivity (see [[Def - Ring]]); $\mathbb{Z}$, any field, and any polynomial ring $k[x_1, \dots, x_n]$ are examples. $\mathbf{CRing}$ is the category of commutative unital rings and ring homomorphisms.
>
> Algebraic geometry studies solution sets of polynomial equations. The key move of *categorical* algebraic geometry — the **functor-of-points** viewpoint — is to refuse to fix one number system and instead record the solutions *in every ring at once*. Fix a system of polynomials, say the single equation $y^2 = x^3 - 1$ with integer coefficients. For any commutative ring $R$, let
> $$C(R) = \{(a, b) \in R^2 : b^2 = a^3 - 1\}$$
> be the set of solutions with coordinates in $R$. A ring homomorphism $R \to S$ pushes a solution in $R$ to a solution in $S$ (apply the homomorphism to the coordinates; it respects the equation), so $C : \mathbf{CRing} \to \mathbf{Set}$ is a covariant functor. The claim that organizes the subject: **this functor is representable.** Indeed, let
> $$A = \mathbb{Z}[x, y]/(y^2 - x^3 + 1).$$
> A ring homomorphism $f : A \to R$ is exactly a choice of $f(x) = a$ and $f(y) = b$ in $R$ subject to the *one relation that defines $A$*, namely $b^2 - a^3 + 1 = 0$. So
> $$\mathbf{CRing}(A, R) \cong C(R), \qquad f \mapsto (f(x), f(y)),$$
> naturally in $R$. The solution functor *is* a hom-functor: $C \cong \mathbf{CRing}(A, -)$.
>
> The categorical concept illustrated is **representability**, and the slogan it earns is the definition of an affine scheme: *an **affine scheme** is a representable functor $\mathbf{CRing} \to \mathbf{Set}$*, and the representing ring $A$ is its ring of functions. The value $C(R)$ is called the set of **$R$-points**. The simplest non-trivial example is the **affine line** $\mathbb{A}^1$: the functor $R \mapsto R$ sending a ring to its own underlying set. It is represented by the polynomial ring $k[x]$ over a base ring $k$, because $\mathbf{CRing}_k(k[x], R) \cong R$, a $k$-algebra map being a free choice of where to send $x$. More generally **affine $n$-space** $\mathbb{A}^n$, the functor $R \mapsto R^n$, is represented by $k[x_1, \dots, x_n]$. And the **multiplicative group** $\mathbb{G}_m$, the functor $R \mapsto R^\times$ of units, is represented by $k[x, x^{-1}]$ as computed above. Why is this illuminating? Because it converts geometry into the single, uniform statement "solving equations in $R$ = mapping a fixed ring into $R$", and the Yoneda lemma (next sections) will turn that statement into the theorem that a scheme is *completely determined by its $R$-points as $R$ ranges over all rings*.

**Is NOT an instance — the covariant power-set functor.** The functor $\mathcal{P} : \mathbf{Set} \to \mathbf{Set}$ sending a set $X$ to its power set $\mathcal{P}(X)$, with $f : X \to Y$ acting by *direct image* $\mathcal{P}(f)(S) = f(S)$, is **not representable**. The clean obstruction: a representable functor $\mathcal{C}(A, -)$ preserves all limits, in particular it sends the empty set (the initial object) to a single value $\mathcal{C}(A, \emptyset)$, and more sharply it preserves monomorphisms in a way the covariant power set violates — there is no set $A$ with $\mathbf{Set}(A, X) \cong \mathcal{P}(X)$ naturally, since the right-hand side has cardinality $2^{|X|}$ growing faster than any $|X|^{|A|}$. (By contrast, the *contravariant* power-set functor $\mathcal{P} : \mathbf{Set}^{op} \to \mathbf{Set}$, using *preimages*, **is** representable, by the two-element set — see [[Def - Universal Element]].) Worked at [[Ex - A non-representable functor]].

**Calibration check.** Verify directly that $\mathcal{C}(A, -)$ sends $1_X$ to the identity function and a composite $g \circ f$ to $(g \circ f)_* = g_* \circ f_*$. Confirm the variance flip for $\mathcal{C}(-, B)$ by checking $(g \circ f)^* = f^* \circ g^*$. Finally, exhibit the universal element of $U : \mathbf{Grp} \to \mathbf{Set}$ as represented by $\mathbb{Z}$ — it should be the generator $1 \in U(\mathbb{Z})$.

---

# Unlocked by This

> [!tip] The Yoneda Lemma and Embedding *(from this chapter)*
> Once hom-functors exist, the [[Thm - The Yoneda Lemma|Yoneda lemma]] computes *all* natural transformations out of them, and the [[Def - The Yoneda Embedding|Yoneda embedding]] $\mathbf{y} : \mathcal{C} \to [\mathcal{C}^{op}, \mathbf{Set}]$, $A \mapsto \mathcal{C}(-, A)$, embeds any category into its presheaves. Representability is membership in the image of $\mathbf{y}$.

> [!tip] Affine Schemes and the Functor of Points *(from Algebraic Geometry)*
> The representability of solution functors is the foundation of the functor-of-points approach: the category of **affine schemes** is equivalent to $\mathbf{CRing}^{op}$, with **Spec** the Yoneda embedding. The affine line, affine $n$-space, and $\mathbb{G}_m$ above are the first players in this dictionary. See [[Thm - The Yoneda Embedding is Fully Faithful]] and [[Ex - A scheme is determined by its functor of points]].

> [!tip] Representable Functors Preserve Limits *(from Category Theory III)*
> Every representable functor preserves all [[Def - Limit and Colimit|limits]] that exist — products go to products, equalizers to equalizers, pullbacks to pullbacks. This single fact is the most-used tool for *disproving* representability (a functor that breaks a limit cannot be representable) and is the categorical source of the left-exactness of $\mathrm{Hom}$ in [[Def - The Hom Functor and Left Exactness]].
