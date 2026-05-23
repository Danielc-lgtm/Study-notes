---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Lie Group"
  - "Def - Left-Invariant Vector Field"
  - "Def - Lie Algebra"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, differential-geometry, lie-groups]
---

# Notation

$G$ is a Lie group; $\mathfrak{X}(G)$ is the space of smooth vector fields on $G$ with the Lie bracket $[X, Y]f = X(Yf) - Y(Xf)$. The space of left-invariant vector fields is $\mathrm{Lie}(G)$ or $\mathfrak{g}$. For $g \in G$, $L_g$ is left translation. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

---

# Statement

> **Theorem.** Let $G$ be a Lie group. The space of smooth left-invariant vector fields on $G$ is closed under the Lie bracket of vector fields, hence is a Lie subalgebra of $\mathfrak{X}(G)$. The evaluation map $\varepsilon : \mathrm{Lie}(G) \to T_e G$, $X \mapsto X_e$, is a vector space isomorphism, and the transported bracket on $T_e G$ makes $T_e G$ into a finite-dimensional Lie algebra of dimension $\dim G$.

> **Corollary (dimension).** $\dim \mathfrak{g} = \dim G$.

> **Corollary (smoothness is automatic).** Every left-invariant rough vector field on $G$ is smooth (Lee Cor 8.38).

---

# Motivation

The fundamental observation that makes Lie group theory work is that a Lie group $G$ has a canonical *finite-dimensional* Lie algebra attached to it. The smooth vector fields $\mathfrak{X}(G)$ on a Lie group form an infinite-dimensional Lie algebra under the bracket of vector fields — far too large to be a useful invariant. The space of left-invariant vector fields, by contrast, is *exactly* $\dim G$-dimensional, and the bracket of two left-invariant vector fields is again left-invariant. So we get a finite-dimensional Lie subalgebra of $\mathfrak{X}(G)$ — the Lie algebra of $G$.

This theorem performs two functions simultaneously:

1. **Closure of left-invariance under the bracket.** A priori, left-invariant vector fields form only a vector subspace of $\mathfrak{X}(G)$. The theorem says they form a *Lie* subspace — closed under the bracket. This is what makes the bracket on $\mathfrak{g}$ well-defined.

2. **Isomorphism with $T_e G$.** The evaluation map "value at $e$" is a vector space isomorphism, so a left-invariant vector field is the same data as a tangent vector at the identity. Concretely, every tangent vector at $e$ extends uniquely to a left-invariant vector field on all of $G$. This is the rigidity statement that makes the theory tractable.

Without (1), we would have a finite-dimensional vector space at $T_e G$ but no algebraic structure. Without (2), we would have a finite-dimensional Lie algebra of left-invariant vector fields but no easy way to compute it (the entire vector field is a complicated object). Together, they say: the Lie algebra of $G$ is canonically $T_e G$ with a bracket inherited from vector-field calculus.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis of this theorem is bare: a Lie group $G$. Every Lie group automatically has a Lie algebra. The non-obvious work is in the existence of left-invariant vector fields and the closure under bracket.

The first source is **a tangent vector at the identity**, $v \in T_e G$. Property $B$ is "a tangent vector at $e$ exists". The bridge is the construction $v \mapsto v^L$ where $v^L|_g = d(L_g)_e(v)$ — extending $v$ to a vector field on all of $G$ by left translation. The theorem provides this extension as smooth and left-invariant; the non-obvious step is that the result is smooth (Lee Cor 8.38) and that two such extensions of brackets agree.

A second source is **a Lie group homomorphism $F : G \to H$**. Property $B$ is "we have a homomorphism between two Lie groups". The bridge to the Lie algebra is: the differential $dF_e : \mathfrak{g} \to \mathfrak{h}$ preserves the bracket. The image of a left-invariant vector field under $F$ is left-invariant (because $F$ is equivariant under left translations), so $F_*$ sends $\mathrm{Lie}(G)$ to $\mathrm{Lie}(H)$ and respects the bracket — this is [[Thm - Lie Group Homomorphism Induces Lie Algebra Homomorphism]].

A third source is **a closed Lie subgroup $H \leq G$**. Property $B$ is "$H$ is a closed Lie subgroup". The bridge: $\mathfrak{h} = T_e H \subseteq T_e G = \mathfrak{g}$ is a Lie subalgebra (closed under the bracket). The closure under bracket comes from the fact that $\mathfrak{X}(H)$-related vector fields have $\mathfrak{X}(H)$-related brackets — see [[Def - Lie Subgroup]].

**Targets (Output Amplification)**

The conclusion of the theorem is that $\mathfrak{g}$ is a finite-dimensional Lie algebra of dimension $\dim G$. Combined with further structure, this conclusion amplifies.

A first combination is **finite-dimensional Lie algebra + classification theorems** $\implies$ structural information about $G$. By the Lie algebra side, semisimple/nilpotent/solvable classification (Cartan-Killing, Lie-Kolchin) sorts $\mathfrak{g}$, and via the [[Thm - Naturality of the Exponential Map|exponential map]] and Lie correspondence this lifts to structural conclusions about $G$.

A second combination is **finite-dimensional + parallelizability of $G$**. Because every Lie group has a global frame given by a basis of left-invariant vector fields, every Lie group is parallelizable (its tangent bundle is trivial). This rules out many manifolds as Lie groups: $S^2$ is not parallelizable (the hairy ball theorem), so $S^2$ admits no Lie group structure. Only $S^0, S^1, S^3$ (and infinitely many others not in the sphere family) admit Lie group structure.

A third combination is **bracket on $\mathfrak{g}$ + matrix realization** $\implies$ commutator. For matrix Lie groups, the bracket coincides with the matrix commutator (see [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]]). This is non-obvious because the bracket is defined abstractly via vector-field brackets, but it agrees with the elementary commutator $AB - BA$ when both sides are computed.

---

# Why Is It True

The theorem rests on a single fact about pushforward of vector fields: **pushforward by a diffeomorphism commutes with the Lie bracket** (Lee Cor 8.31). For any diffeomorphism $\phi : M \to N$ and vector fields $X, Y$ on $M$,

$$\phi_*[X, Y] = [\phi_* X, \phi_* Y].$$

Apply this to $\phi = L_g$, left translation. If $X, Y$ are left-invariant, then $(L_g)_* X = X$ and $(L_g)_* Y = Y$. Hence

$$(L_g)_*[X, Y] = [(L_g)_* X, (L_g)_* Y] = [X, Y].$$

So $[X, Y]$ is invariant under every left translation — i.e., $[X, Y]$ is left-invariant. **The bracket of two left-invariant vector fields is left-invariant.** That is the entire proof of closure.

**The bolded mechanism summary: pushforward respects the bracket, and left-invariant vector fields are exactly those preserved by every left translation; therefore the bracket of left-invariant vector fields is also preserved by every left translation, hence is left-invariant.**

For the dimension count: the evaluation map $X \mapsto X_e$ is linear (immediate), injective (a left-invariant vector field is determined by its value at one point, since $X_g = d(L_g)_e(X_e)$), and surjective (given $v \in T_e G$, the construction $v^L|_g = d(L_g)_e(v)$ produces a left-invariant vector field with value $v$ at $e$, and Lee's smoothness argument shows it is smooth). Hence the map is an isomorphism, and $\dim \mathfrak{g} = \dim T_e G = \dim G$.

---

# What Makes This Hard

The main subtlety is **the smoothness of the constructed vector field $v^L$**. It is easy to see that the formula $v^L|_g = d(L_g)_e(v)$ defines a vector field on $G$ (a rough section of the tangent bundle), but smoothness of $g \mapsto v^L|_g$ is not automatic. Lee proves it by testing against a smooth function $f \in C^\infty(G)$ and a smooth curve $\sigma : (-\delta, \delta) \to G$ with $\sigma(0) = e, \sigma'(0) = v$, then writing $v^L f(g) = \frac{d}{dt}|_{t=0} f(g \sigma(t))$ and recognizing this as smooth in $g$.

The second subtlety is **the dimension count**. It is tempting to think $\dim \mathfrak{X}(G) = \dim G$ — but $\mathfrak{X}(G)$ is infinite-dimensional. The finite-dimensional fact is specifically about the *left-invariant* subspace, and it is what the evaluation isomorphism delivers.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Show that pushforward by a left translation $(L_g)_*$ preserves the bracket of vector fields (a special case of the diffeomorphism-pushforward identity); apply this to two left-invariant vector fields; conclude their bracket is also left-invariant. Separately, verify the evaluation map $X \mapsto X_e$ is a vector space isomorphism by exhibiting an explicit inverse.

**Subgoal decomposition:**

1. **Bracket of left-invariant vector fields is left-invariant.** Show that if $X, Y \in \mathrm{Lie}(G)$ then $[X, Y] \in \mathrm{Lie}(G)$.
   - *Hint:* $(L_g)_*[X, Y] = [(L_g)_* X, (L_g)_* Y]$ for any diffeomorphism $L_g$, and $(L_g)_* X = X$, $(L_g)_* Y = Y$ by left-invariance.
   - *Why needed:* This is closure under the bracket, the property that makes the left-invariant vector fields a Lie subalgebra.

2. **Evaluation map is injective.** Show that if $X_e = 0$ then $X = 0$.
   - *Hint:* Left-invariance gives $X_g = d(L_g)_e(X_e) = d(L_g)_e(0) = 0$ for every $g$.
   - *Why needed:* It shows a left-invariant vector field is determined by its value at $e$.

3. **Evaluation map is surjective.** Show that every $v \in T_e G$ extends to a left-invariant vector field.
   - *Hint:* Define $v^L|_g := d(L_g)_e(v)$. Check this is smooth (via curves at $e$) and satisfies $d(L_h)_g(v^L|_g) = v^L|_{hg}$ (by chain rule and $L_h \circ L_g = L_{hg}$).
   - *Why needed:* It shows every tangent vector at $e$ produces a left-invariant vector field, so the evaluation map is onto.

4. **Dimension.** Conclude $\dim \mathrm{Lie}(G) = \dim T_e G = \dim G$.
   - *Hint:* Vector space isomorphism preserves dimension.

---

# Lemma Decomposition

> [!note]- Lemma 1: Pushforward by a diffeomorphism preserves the Lie bracket
> **Statement:** For any diffeomorphism $\phi : M \to N$ and vector fields $X, Y$ on $M$, $\phi_*[X, Y] = [\phi_* X, \phi_* Y]$.
>
> **Hint:** Compute on functions: $(\phi_* X)(f) = X(f \circ \phi) \circ \phi^{-1}$. Apply twice.
>
> **Why needed:** Specializing to $\phi = L_g$ and noting left-invariance gives the closure of left-invariance under bracket.
>
> > [!note]- Full proof
> > For $f \in C^\infty(N)$, $(\phi_* X)(f) = X(f \circ \phi) \circ \phi^{-1}$ by definition of pushforward. Hence
> > $$(\phi_* X)(\phi_* Y(f)) = X(\phi_* Y(f) \circ \phi) \circ \phi^{-1} = X(Y(f \circ \phi)) \circ \phi^{-1}.$$
> > Similarly $(\phi_* Y)(\phi_* X(f)) = Y(X(f \circ \phi)) \circ \phi^{-1}$. Subtracting,
> > $$[\phi_* X, \phi_* Y](f) = \big(X(Y(f \circ \phi)) - Y(X(f \circ \phi))\big) \circ \phi^{-1} = [X, Y](f \circ \phi) \circ \phi^{-1} = \phi_*[X, Y](f).$$
> > Hence $\phi_*[X, Y] = [\phi_* X, \phi_* Y]$.

> [!note]- Lemma 2: The vector field $v^L|_g := d(L_g)_e(v)$ is left-invariant
> **Statement:** For $v \in T_e G$, the rough section $g \mapsto d(L_g)_e(v)$ of $TG$ is left-invariant: $d(L_h)_g(v^L|_g) = v^L|_{hg}$ for all $h, g \in G$.
>
> **Hint:** Chain rule applied to $L_h \circ L_g = L_{hg}$ at the point $e$.
>
> **Why needed:** It is the construction giving surjectivity of the evaluation map.
>
> > [!note]- Full proof
> > $$d(L_h)_g(v^L|_g) = d(L_h)_g \circ d(L_g)_e(v) = d(L_h \circ L_g)_e(v) = d(L_{hg})_e(v) = v^L|_{hg}.$$
> > Hence $v^L$ is left-invariant.

> [!note]- Lemma 3: $v^L$ is smooth
> **Statement:** The vector field $v^L$ defined above is a smooth vector field on $G$.
>
> **Hint:** Show $v^L f$ is smooth for every $f \in C^\infty(G)$, using a smooth curve $\sigma$ at $e$ with $\sigma'(0) = v$.
>
> **Why needed:** Smoothness is part of the definition of a vector field, and needed for $v^L \in \mathrm{Lie}(G)$.
>
> > [!note]- Full proof
> > Choose a smooth curve $\sigma : (-\delta, \delta) \to G$ with $\sigma(0) = e$, $\sigma'(0) = v$. For $g \in G$ and $f \in C^\infty(G)$,
> > $$v^L f(g) = (v^L|_g) f = d(L_g)_e(v) f = v(f \circ L_g) = \sigma'(0)(f \circ L_g) = \frac{d}{dt}\bigg|_{t=0} f(L_g(\sigma(t))) = \frac{d}{dt}\bigg|_{t=0} f(g \sigma(t)).$$
> > Define $\varphi : (-\delta, \delta) \times G \to \mathbb{R}$ by $\varphi(t, g) = f(g \sigma(t))$. This is smooth (composition of group multiplication, $\sigma$, and $f$, all smooth). Hence $v^L f(g) = \partial \varphi/\partial t|_{(0, g)}$ is smooth in $g$. Since this holds for every $f$, Proposition 8.14 of Lee says $v^L$ is a smooth vector field.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $G$ be a Lie group with identity $e$, and let $\mathrm{Lie}(G) \subseteq \mathfrak{X}(G)$ be the space of smooth left-invariant vector fields.
>
> **Step 1 (bracket-closure).** Let $X, Y \in \mathrm{Lie}(G)$. For any $g \in G$, $(L_g)_* X = X$ and $(L_g)_* Y = Y$ by left-invariance. Since $L_g$ is a diffeomorphism and pushforward commutes with the Lie bracket (Lemma 1), $(L_g)_*[X, Y] = [(L_g)_* X, (L_g)_* Y] = [X, Y]$. Hence $[X, Y]$ is left-invariant.
>
> **Step 2 (evaluation is injective).** Let $X \in \mathrm{Lie}(G)$ with $X_e = 0$. For any $g \in G$, $X_g = d(L_g)_e(X_e) = 0$ (by left-invariance applied with $h = e$, or by the formula $X_g = d(L_g)_e(X_e)$ directly). Hence $X = 0$.
>
> **Step 3 (evaluation is surjective).** Let $v \in T_e G$. Define $v^L|_g := d(L_g)_e(v)$ for $g \in G$. By Lemma 2, $v^L$ is left-invariant: $d(L_h)_g(v^L|_g) = v^L|_{hg}$. By Lemma 3, $v^L$ is smooth. Thus $v^L \in \mathrm{Lie}(G)$ with $\varepsilon(v^L) = v^L|_e = v$. So $\varepsilon$ is surjective.
>
> **Step 4 (dimension).** $\varepsilon : \mathrm{Lie}(G) \to T_e G$ is a vector space isomorphism (linear, injective, surjective). Hence $\dim \mathrm{Lie}(G) = \dim T_e G = \dim G$.
>
> **Step 5 (Lie algebra structure on $T_e G$).** Transport the bracket from $\mathrm{Lie}(G)$ to $T_e G$ via $\varepsilon$: for $u, v \in T_e G$, define $[u, v]_{T_e G} := \varepsilon([u^L, v^L])$. By Step 1, $[u^L, v^L] \in \mathrm{Lie}(G)$, so the right-hand side makes sense. By construction, $\varepsilon$ is an isomorphism of Lie algebras (Lie subalgebra of $\mathfrak{X}(G)$ on one side, $T_e G$ with the transported bracket on the other). The bracket on $T_e G$ inherits bilinearity, antisymmetry, and the Jacobi identity from the corresponding properties of the vector-field bracket.
>
> Hence $\mathfrak{g} := \mathrm{Lie}(G) \cong T_e G$ is a finite-dimensional Lie algebra of dimension $\dim G$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Algebraic topology — parallelizability of Lie groups.** Every Lie group $G$ is parallelizable: its tangent bundle $TG$ is trivializable, with the trivialization $TG \cong G \times \mathfrak{g}$ given by $(g, X) \mapsto d(L_g)_e(X) = X^L|_g$. As a consequence, $TG \to G$ admits a smooth global frame given by any basis of $\mathfrak{g}$. The implications: spheres $S^n$ that are not parallelizable cannot be Lie groups. By the Bott–Milnor and Kervaire theorems, only $S^0, S^1, S^3, S^7$ are parallelizable, and only $S^0, S^1, S^3$ are Lie groups ($S^7$ is an "H-space" but not a Lie group, lacking associativity).

**Algebraic structure theory — the bracket on matrix Lie algebras.** Compute the bracket on $\mathfrak{gl}(n) = T_I \mathrm{GL}(n)$ via two routes: (a) the abstract definition via left-invariant vector fields, and (b) the matrix commutator $[A, B] = AB - BA$. Show they agree. This is the content of [[Ex - The Lie Bracket on a Matrix Lie Algebra is the Commutator]]. The agreement is not automatic — it relies on the formula $X^L|_g = gX$ for matrix groups, which then gives the bracket via the vector-field bracket on matrix-valued functions.

**Differential equations — completeness of left-invariant vector fields.** Every left-invariant vector field on a Lie group is **complete**: its flow is defined for all time $t \in \mathbb{R}$ (Lee Cor 9.18). The proof uses that the flow of $X^L$ is right-translation by the one-parameter subgroup, which is defined globally. This completeness is crucial for the definition of the exponential map ($\exp(X) = \phi_1^{X^L}(e)$), since otherwise we could only evaluate $\exp$ on a small disk around $0$.

---

# Bridges

- **[[Def - The Lie Algebra of a Lie Group|Definition of the Lie Algebra]]** — this theorem is exactly the existence-and-structure half of that definition. Together with the canonical isomorphism $\mathrm{Lie}(G) \cong T_e G$, it provides the bracket on $T_e G$ that makes the tangent space at the identity into a finite-dimensional Lie algebra. Equivalently, this theorem says: every Lie group has a finite-dimensional Lie algebra, computed at the identity.

- **[[Thm - Lie Group Homomorphism Induces Lie Algebra Homomorphism|The Lie functor]]** — once $\mathrm{Lie}(G)$ is established as a Lie algebra, the next theorem upgrades this to a functor: $G \mapsto \mathfrak{g}$, $F \mapsto F_*$. The bracket compatibility of $F_*$ uses this theorem in a critical way: $F_*$ sends left-invariant vector fields to left-invariant vector fields (by equivariance), and the bracket on each side is the vector-field bracket, so $F_*$ preserves it.

- **The infinite-dimensional generalization** — for a Lie groupoid (rather than a Lie group), the analogue of "left-invariant vector fields" gives the **Lie algebroid** structure. For loop groups $LG$ and other infinite-dimensional Lie groups, the left-invariant vector fields form an infinite-dimensional Lie algebra; the structural theorems are subtler but the basic construction is the same.

---

# Unlocked by This

> [!tip] The Exponential Map *(from this chapter)*
> Now that $\mathfrak{g}$ is established as a Lie algebra, the [[Def - Exponential Map of a Lie Group|exponential map]] $\exp : \mathfrak{g} \to G$ can be constructed: each $X \in \mathfrak{g}$ has a left-invariant vector field $X^L$, which is complete (by left-invariance), and $\exp(X) := \phi_1^{X^L}(e)$ is the time-$1$ flow.

> [!tip] Parallelizability of Lie Groups *(from this chapter)*
> Every Lie group is **parallelizable**: $TG \cong G \times \mathfrak{g}$ via $(g, X) \mapsto X^L|_g$. The global frame given by any basis of $\mathfrak{g}$ trivializes the tangent bundle. This rules out many manifolds from being Lie groups: $S^2$ has no global frame, hence no Lie group structure.

> [!tip] Bracket-Preserving Functor *(from this chapter)*
> The construction $G \mapsto \mathrm{Lie}(G)$ extends to a functor by sending $F : G \to H$ to $F_* : \mathfrak{g} \to \mathfrak{h}$, which is a Lie algebra homomorphism — see [[Thm - Lie Group Homomorphism Induces Lie Algebra Homomorphism]]. This is the Lie functor, the cornerstone of the categorical formulation of the theory.
