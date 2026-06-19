---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Category|category]], objects are $A, B, C, X, Y$, and morphisms are $f, g, h$. A morphism from $A$ to $B$ is written $f : A \to B$, the hom-set is $\mathcal{C}(A, B)$, composition is $g \circ f$, and the identity on $A$ is $1_A$. We write $f : A \xrightarrow{\sim} B$ or $A \cong B$ to indicate an isomorphism, and reserve $\hookrightarrow$ for a monomorphism and $\twoheadrightarrow$ for an epimorphism when emphasis helps. This is a **compound page**: it defines three interlocking notions — isomorphism, monomorphism, epimorphism — because they are the three arrow-theoretic shadows of bijectivity, injectivity, and surjectivity, and none is fully understood without seeing how it relates to the other two. The full registry is on [[Category Theory I — Categories, Functors, Natural Transformations]].

---

# Axiom Motivation

In $\mathbf{Set}$ the most important properties of a function are that it is injective, surjective, or bijective. We would like to express these properties for an arbitrary [[Def - Category|category]] — but the definitions we know all mention *elements*, and a general category has no elements, only arrows. So the project is forced upon us: **rephrase injective, surjective, bijective using only composition.** The result is three definitions that agree with the set-theoretic ones in $\mathbf{Set}$ but make sense everywhere, and — this is the subtle and instructive part — they no longer line up the way intuition expects.

Begin with bijectivity, the easiest. A function is a bijection exactly when it has a two-sided inverse function. "Has a two-sided inverse" is already an arrow statement: $f : A \to B$ has an inverse $g : B \to A$ with $g \circ f = 1_A$ and $f \circ g = 1_B$. So **isomorphism** is the arrow-theoretic bijection, and it transports verbatim.

Now injectivity. A function $f$ is injective when $f(x) = f(x')$ forces $x = x'$. We cannot speak of points $x$, so we use *generalized* points: probe $A$ with arrows from a test object. If $f$ is injective and $g, h : X \to A$ satisfy $f \circ g = f \circ h$, then at every point $x \in X$ we have $f(g(x)) = f(h(x))$, hence $g(x) = h(x)$, so $g = h$. This is **left-cancellability**: $f \circ g = f \circ h \implies g = h$. Conversely, in $\mathbf{Set}$, left-cancellability against the one-point set recovers injectivity. So **monomorphism** is "left-cancellable", the arrow-theoretic injection.

Surjectivity is the mirror image. A surjection is right-cancellable: $g \circ f = h \circ f \implies g = h$. So **epimorphism** is "right-cancellable", the arrow-theoretic surjection. In $\mathbf{Set}$ this again recovers surjectivity, by testing against the two-element set.

Here is where intuition must be re-trained, and it is the whole reason these notions deserve their own page. In $\mathbf{Set}$, a function that is both injective and surjective is automatically bijective — mono-and-epi implies iso. **In a general category this implication fails.** A morphism can be left- and right-cancellable yet have no inverse. The reason is that cancellability only sees how $f$ interacts with *other morphisms of the category*, and that may not be enough to manufacture an inverse arrow inside the category. The failure is not a pathology; it is the signal that the category has "too few morphisms" to invert $f$, and it is precisely what distinguishes, say, the category of rings from the category of sets. The definitions are designed so that this gap can appear, because the gap carries information.

---

# The Definition

Let $f : A \to B$ be a morphism in a [[Def - Category|category]] $\mathcal{C}$.

**Isomorphism.** $f$ is an **isomorphism** (or **iso**) if there is a morphism $g : B \to A$ with
$$g \circ f = 1_A \qquad \text{and} \qquad f \circ g = 1_B.$$
Such a $g$ is unique when it exists (if $g, g'$ are both two-sided inverses, $g = g \circ 1_B = g \circ (f \circ g') = (g \circ f) \circ g' = 1_A \circ g' = g'$), and is written $f^{-1}$. Objects $A, B$ are **isomorphic**, $A \cong B$, if some isomorphism between them exists.

**Monomorphism.** $f$ is a **monomorphism** (or **mono**) if it is left-cancellable: for every object $X$ and every pair $g, h : X \to A$,
$$f \circ g = f \circ h \implies g = h.$$

**Epimorphism.** $f$ is an **epimorphism** (or **epi**) if it is right-cancellable: for every object $X$ and every pair $g, h : B \to X$,
$$g \circ f = h \circ f \implies g = h.$$

A morphism that is both mono and epi is **bimorphic**. A category in which every bimorphic morphism is an isomorphism is **balanced** ($\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Ab}$ are balanced; $\mathbf{Ring}$ and $\mathbf{Top}$ are not).

---

# Categorical / Structural Definition

These notions have a clean reformulation through the **hom-functor**, which is worth stating because it is how one actually checks mono/epi in practice and is the bridge to the **Yoneda** viewpoint. Each object $X$ gives a function $\mathcal{C}(X, f) : \mathcal{C}(X, A) \to \mathcal{C}(X, B)$ sending $g \mapsto f \circ g$ (post-composition), and a function $\mathcal{C}(f, X) : \mathcal{C}(B, X) \to \mathcal{C}(A, X)$ sending $g \mapsto g \circ f$ (pre-composition). Then:

$$f \text{ is mono} \iff \mathcal{C}(X, f) \text{ is injective for every } X;$$
$$f \text{ is epi} \iff \mathcal{C}(f, X) \text{ is injective for every } X.$$

In words: $f$ is a monomorphism exactly when post-composing by $f$ never collapses two distinct arrows *into* $A$, and an epimorphism exactly when pre-composing by $f$ never collapses two distinct arrows *out of* $B$. This is the precise sense in which mono/epi are "injectivity/surjectivity tested by all generalized points". The Yoneda philosophy — an object is determined by the arrows into it — is already visible here: mono and epi are statements about the hom-functors $\mathcal{C}(-, A)$ and $\mathcal{C}(B, -)$, and the **Yoneda lemma** later makes "tested by all objects" into an exact equivalence.

---

# Relate to Other Fields / Compression

In $\mathbf{Set}$: mono $=$ injective, epi $=$ surjective, iso $=$ bijective, and all three agree with the naive notions. In $\mathbf{Grp}$ and $\mathbf{Ab}$ the same coincidences hold, and these categories are balanced, so mono $+$ epi $=$ iso. The interesting and instructive cases are the categories where the coincidence breaks.

**True name:** *iso = invertible, mono = left-cancellable, epi = right-cancellable; and "mono + epi" is strictly weaker than "iso" outside balanced categories.* The single most useful thing to remember is the asymmetry of failure: an isomorphism is *always* both mono and epi (proof below), but a mono-epi need not be iso. When a morphism is "obviously injective and surjective" yet refuses to be invertible, you are not in $\mathbf{Set}$, and the obstruction is that the inverse function fails to be a morphism of your category.

---

# Examples / Corollaries

**Iso always implies mono and epi.** If $f$ has inverse $f^{-1}$ and $f \circ g = f \circ h$, then $g = f^{-1} \circ f \circ g = f^{-1} \circ f \circ h = h$, so $f$ is mono; the symmetric computation gives epi. This direction never fails, in any category.

**In $\mathbf{Set}$, the three notions are injective/surjective/bijective.** For monomorphism, test against the one-point set $1 = \{\ast\}$: arrows $1 \to A$ are points of $A$, and left-cancellability against them is exactly $f(a) = f(a') \implies a = a'$, i.e. injectivity. For epimorphism, test against the two-point set $2 = \{0, 1\}$: if $f$ missed a point $b_0 \in B$, the two functions "constant $0$" and "indicator of $b_0$" agree after $f$ but differ, so $f$ would not be epi; thus epi forces surjective, and surjective is easily seen to be epi.

**Is NOT iso though mono and epi — $\mathbb{Z} \hookrightarrow \mathbb{Q}$ in $\mathbf{CRing}$.** The inclusion $\iota : \mathbb{Z} \to \mathbb{Q}$ of [[Def - Ring|rings]] is a [[Def - Ring Homomorphism|ring homomorphism]]. It is a monomorphism (it is injective, and injective ring maps are left-cancellable). It is *also* an epimorphism in $\mathbf{CRing}$, which is the surprise: if two ring homomorphisms $g, h : \mathbb{Q} \to S$ agree on $\mathbb{Z}$, they agree on all of $\mathbb{Q}$, because the value of a ring map on a fraction $a/b$ is forced — $g(a/b) = g(a)g(b)^{-1}$, and $g(a), g(b)$ are already pinned down by their values on $\mathbb{Z}$. So $g \circ \iota = h \circ \iota$ forces $g = h$, making $\iota$ right-cancellable. But $\iota$ is plainly not an isomorphism: there is no ring map $\mathbb{Q} \to \mathbb{Z}$ at all, since $1/2$ has nowhere to go. **An epimorphism of rings need not be surjective** — $\mathbb{Z} \to \mathbb{Q}$ is epi precisely because $\mathbb{Q}$ is generated by $\mathbb{Z}$ under the operations that a ring map must respect.

**Is NOT iso though mono and epi — a continuous bijection in $\mathbf{Top}$.** Let $f : [0, 1) \to S^1$ be $t \mapsto (\cos 2\pi t, \sin 2\pi t)$, wrapping the half-open interval once around the circle $S^1 = \{(x,y) : x^2 + y^2 = 1\}$. As a function it is a continuous bijection, so it is both a monomorphism and an epimorphism in $\mathbf{Top}$ (underlying-set injectivity and surjectivity give cancellability). But its inverse function is not continuous — points near the join at $t = 0$ map back to points near both ends of $[0,1)$ — so $f$ is not a homeomorphism, not an isomorphism in $\mathbf{Top}$. The missing inverse arrow is the entire obstruction. **In $\mathbf{Top}$, iso means homeomorphism, strictly stronger than continuous bijection.**

**Calibration check.** Verify that in a [[Def - Group|group]] regarded as a one-object [[Def - Category|category]] *every* morphism is an isomorphism (every group element is invertible), so the category is a [[Def - Groupoid|groupoid]]. Verify that the inverse of an iso is itself an iso, and that a composite of isos (respectively monos, epis) is again an iso (respectively mono, epi). Finally, confirm you can state the reason $\mathbb{Z} \to \mathbb{Q}$ is epi in $\mathbf{CRing}$ without computing a single conjugation: a ring map out of $\mathbb{Q}$ is determined by its restriction to $\mathbb{Z}$.

---

# Unlocked by This

> [!tip] Subobjects and the Subobject Classifier *(from Topos Theory)*
> A **subobject** of $A$ is an isomorphism class of monomorphisms into $A$ — the categorical replacement for "subset". In a **topos** the subobjects of $A$ are classified by maps $A \to \Omega$ into a single object $\Omega$, the subobject classifier, generalizing the indicator-function description of subsets of a set. Monomorphism is the starting notion.

> [!tip] Effective Epimorphisms and Descent *(from Algebraic Geometry)*
> The failure of "epi = surjective" forces a more careful notion of "covering" in geometry. **Effective epimorphisms** and **descent** are the machinery that decides when local data glued along an epimorphism assemble into a global object, and they are the categorical heart of sheaf theory and of the **fpqc/fppf topologies** on schemes.
