---
type: definition
subject: linear-algebra
prereqs:
  - "Def - Linear Map"
  - "Def - Quotient Space"
  - "Def - Null Space and Range"
tags: [algebra, linear-algebra]
---

# Notation

$V$ and $W$ are vector spaces over $\mathbb{F}$ and $T \in \mathcal{L}(V, W)$ is a linear map. The **quotient map** $\pi : V \to V/U$ for a subspace $U \leq V$ is defined by $\pi(v) = v + U$. The **induced map** (or **map induced on the quotient**) $\tilde T : V/\operatorname{null} T \to W$ is defined by $\tilde T(v + \operatorname{null} T) = Tv$. Full registry on [[Linear Algebra IV — §3E–F Products, Quotients, Duality]].

This is a compound page: it defines two interlocking notions — the **quotient map** $\pi$ for a subspace and the **induced map** $\tilde T$ associated to a linear map — because they are introduced together in §3E and the second uses the first.

---

# Axiom Motivation

The quotient map and the induced map are the two natural linear maps associated to the [[Def - Quotient Space|quotient construction]]. They have different jobs.

**The quotient map $\pi$** answers the question "what is the natural linear map relating $V$ and $V/U$?". The quotient space $V/U$ exists; the next question is what map goes between them, and the only candidate that makes geometric sense is "send each vector to its coset", that is, $\pi(v) = v + U$. The map is forced once you accept that $V/U$ consists of cosets — there is nothing else $\pi$ could be.

Why is the quotient map important? Three reasons. First, *it is linear and surjective*, which means the quotient $V/U$ is a *quotient* of $V$ in the appropriate technical sense — a vector space mapped onto by $V$. Second, its *null space is exactly $U$*: $\pi(v) = 0 + U$ iff $v \in U$. So the quotient map is the witness that "every subspace is the null space of some linear map". Third, *it satisfies the universal property* — any linear map $T : V \to W$ vanishing on $U$ factors uniquely as $T = \bar T \circ \pi$ for a unique $\bar T : V/U \to W$.

**The induced map $\tilde T$** answers a different question: given a linear map $T : V \to W$ with non-trivial null space, can we "remove the redundancy" to get an injective map? The redundancy is exactly $\operatorname{null} T$ — two vectors $v, v'$ with $Tv = Tv'$ differ by an element of $\operatorname{null} T$. So the natural fix is to identify any two vectors that differ by an element of $\operatorname{null} T$; this is the quotient $V/\operatorname{null} T$. The induced map $\tilde T : V/\operatorname{null} T \to W$ is the map that "$T$ secretly wanted to be" — the version of $T$ after removing the blindness.

The definition $\tilde T(v + \operatorname{null} T) := Tv$ is forced: if $\tilde T \circ \pi = T$ (which is what "induced by $T$" means), then $\tilde T(v + \operatorname{null} T) = \tilde T(\pi(v)) = T(v)$. Any other definition fails to satisfy this commutativity.

Well-definedness is automatic in this case: if $v + \operatorname{null} T = v' + \operatorname{null} T$, then $v - v' \in \operatorname{null} T$, so $T(v - v') = 0$, so $Tv = Tv'$ — the value $\tilde T(v + \operatorname{null} T)$ is independent of representative. This is the special case of the universal property of the quotient that the *content* of "$T$ vanishes on $\operatorname{null} T$" is trivial (it is the definition of $\operatorname{null} T$).

Why specifically the null space, not some larger subspace? Because $\operatorname{null} T$ is the *unique smallest* subspace $U \subseteq V$ such that "$T$ vanishes on $U$" — anything smaller is not closed under linear combinations, and anything larger throws away information $T$ was capable of distinguishing. The quotient $V/\operatorname{null} T$ is the *minimal* identification needed to make $T$ injective.

The payoff is the **first isomorphism theorem for vector spaces**: $\tilde T$ is an isomorphism from $V/\operatorname{null} T$ onto $\operatorname{range} T$. The reason to introduce $\tilde T$ is precisely to obtain this isomorphism, and the isomorphism reveals that the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]] is *just the counting form* of an underlying structural identity.

---

# The Definition

**Quotient map.** Let $V$ be a vector space and $U \leq V$ a subspace. The **quotient map** $\pi : V \to V/U$ is defined by
$$\pi(v) := v + U \qquad \text{for } v \in V.$$
It is a linear map, surjective, with $\operatorname{null} \pi = U$.

The linearity of $\pi$ is immediate from the definitions of the operations on $V/U$:
$$\pi(v + w) = (v + w) + U = (v + U) + (w + U) = \pi(v) + \pi(w),$$
$$\pi(\lambda v) = (\lambda v) + U = \lambda(v + U) = \lambda \pi(v).$$
Surjectivity is the tautology that every element of $V/U$ has the form $v + U$ for some $v \in V$. The null space computation: $\pi(v) = 0 + U \iff v + U = U \iff v \in U$, using the partition lemma [[Def - Affine Subset#Lemma: Two Translates of a Subspace are Equal or Disjoint|3.101]].

**Induced map of a linear map.** Let $T \in \mathcal{L}(V, W)$. The **induced map** $\tilde T : V/\operatorname{null} T \to W$ is defined by
$$\tilde T(v + \operatorname{null} T) := Tv \qquad \text{for } v \in V.$$
It is well-defined (independent of representative), linear, injective, and has range $\operatorname{range} T$. So $\tilde T$ is an isomorphism from $V/\operatorname{null} T$ onto $\operatorname{range} T$:
$$\boxed{\;V / \operatorname{null} T \;\xrightarrow{\;\cong\;}\; \operatorname{range} T.\;}$$

The composition $\tilde T \circ \pi : V \to W$ recovers $T$:
$$(\tilde T \circ \pi)(v) = \tilde T(\pi(v)) = \tilde T(v + \operatorname{null} T) = Tv.$$
So every linear map $T$ factors canonically as
$$V \;\xrightarrow{\;\pi\;}\; V/\operatorname{null} T \;\xrightarrow{\;\tilde T\;}\; \operatorname{range} T \;\hookrightarrow\; W,$$
a *surjection*, followed by an *isomorphism*, followed by an *inclusion*. This canonical factorisation is the structural identity from which the fundamental theorem of linear maps is the counting consequence.

---

# Categorical Definition

**Universal property of the quotient map.** As discussed in [[Def - Quotient Space|the quotient space page]], the pair $(V/U, \pi)$ is the universal example of a vector space mapped to by $V$ in a way that kills $U$. Precisely: for any linear map $T : V \to W$ with $T|_U = 0$, there is a unique linear map $\bar T : V/U \to W$ with $T = \bar T \circ \pi$.

**The induced map as a special case.** The induced map $\tilde T : V/\operatorname{null} T \to W$ is the case of the universal property with $U = \operatorname{null} T$ — the subspace on which $T$ automatically vanishes. Since $\operatorname{null} T$ is the *largest* subspace of $V$ on which $T$ vanishes, the resulting $\tilde T$ is *injective*: every kernel-class is identified, so no further collapsing happens.

**Functorially.** The construction $T \mapsto \tilde T$ is part of a much larger picture. For any short exact sequence $0 \to U \to V \to V/U \to 0$, the universal property gives a bijection
$$\{T : V \to W : T|_U = 0\} \;\xleftrightarrow{\;\bar T \leftrightarrow \bar T \circ \pi\;}\; \{\bar T : V/U \to W\}.$$
This is one of the simplest examples of an *adjoint functor* pair: "quotient by $U$" is left adjoint to "linear maps that vanish on $U$" — a recurring theme in homological algebra.

---

# Relate to Other Fields / Compression

The quotient map and the induced map are the linear-algebraic specialisation of universally-defined maps in any algebraic category. For [[Def - Quotient Group|groups]] $G/N$, the quotient map $\pi : G \to G/N$ sends $g$ to $gN$, and for a homomorphism $\varphi : G \to H$ the induced map $\tilde \varphi : G/\ker\varphi \to H$ is the [[Thm - First Isomorphism Theorem|first isomorphism theorem]]. For [[Def - Ideal|rings with ideals]] giving the [[Def - Quotient Ring|quotient ring]] $R/I$, the quotient $\pi : R \to R/I$ sends $r$ to $r + I$, and for a ring homomorphism $\varphi$ the induced map gives $R/\ker\varphi \cong \operatorname{im}\varphi$. Every algebraic setting has the same construction.

**True name:** the induced map $\tilde T$ is "the version of $T$ that has been made injective by quotienting out its blindness". The quotient map $\pi$ is "the canonical surjection collapsing $U$ to zero".

A useful slogan: *every linear map factors as quotient-then-injection*. The factorisation $T = \tilde T \circ \pi$ is canonical — no choices are made — and it is the structural content of rank-nullity.

---

# Examples / Corollaries

**Is an instance — $T : \mathbb{R}^3 \to \mathbb{R}^2$, $T(x, y, z) = (x, y)$, the projection.** Here $\operatorname{null} T = \{(0, 0, z) : z \in \mathbb{R}\}$, the $z$-axis, and $\operatorname{range} T = \mathbb{R}^2$. The quotient $\mathbb{R}^3 / \operatorname{null} T$ has elements "vertical lines parallel to the $z$-axis", and the induced map $\tilde T$ sends a vertical line at $(x_0, y_0)$ to $(x_0, y_0) \in \mathbb{R}^2$. This is an isomorphism $\mathbb{R}^3 / \operatorname{null} T \cong \mathbb{R}^2 = \operatorname{range} T$, confirming the first isomorphism theorem.

**Is an instance — evaluation at zero.** Let $V = \mathcal{P}_3(\mathbb{R})$ (polynomials of degree $\leq 3$) and $T : V \to \mathbb{R}$, $T(p) = p(0)$. Then $\operatorname{null} T = \{p : p(0) = 0\} = x\mathcal{P}_2(\mathbb{R})$ (degree-$\leq 3$ polynomials divisible by $x$), of dimension $3$, and $\operatorname{range} T = \mathbb{R}$. The induced map $\tilde T : V/\operatorname{null} T \to \mathbb{R}$ sends $p + \operatorname{null} T$ to $p(0)$, and this is an isomorphism. Geometrically: two polynomials are in the same coset iff they agree at $0$, and the coset is named by their common value at $0$. So $V/\operatorname{null} T$ is the "values at $0$", and isomorphism to $\mathbb{R}$ is automatic.

**Is an instance — the zero map.** Let $T : V \to W$ be the zero map. Then $\operatorname{null} T = V$ (everything is killed), $\operatorname{range} T = \{0\}$, and the quotient $V/\operatorname{null} T = V/V$ has a single element $0 + V$. The induced map $\tilde T$ sends this single coset to $0 \in W$. The isomorphism $V/V \cong \{0\}$ is the degenerate case.

**Is an instance — the identity map.** Let $T : V \to V$ be the identity. Then $\operatorname{null} T = \{0\}$, and $V/\operatorname{null} T = V/\{0\} \cong V$ (cosets of $\{0\}$ are singletons), and $\operatorname{range} T = V$. The induced map is the identity itself. The first isomorphism theorem is a triviality in this case.

**Is NOT an instance — non-linear $T$.** If $T : V \to W$ is not linear (say $T(v) = v + v_0$ for a fixed nonzero $v_0$), there is no induced map on any quotient in the linear-algebra sense, because the construction relies on linearity at every step. The general non-linear analogue would be set-theoretic — a function factors as surjection-bijection-injection — but the universal-property content requires linearity.

**Corollary — every subspace is a null space.** Given any subspace $U \leq V$, the quotient map $\pi : V \to V/U$ is a linear map whose null space is exactly $U$. So the question "which subspaces of $V$ are null spaces of some linear map out of $V$?" has the answer "all of them". This is the linear-algebraic analogue of "every normal subgroup is a kernel".

**Corollary — first isomorphism theorem.** For every linear map $T : V \to W$, the induced map $\tilde T$ is an isomorphism $V/\operatorname{null} T \cong \operatorname{range} T$. This is proved in [[Thm - Quotient Space Dimension and the Fundamental Theorem Reread]] and exercised in [[Ex - Quotient by null space is isomorphic to range]].

**Corollary — canonical factorisation.** Every linear map $T$ factors as $T = j \circ \tilde T \circ \pi$ where $\pi : V \to V/\operatorname{null} T$ is the quotient (surjective), $\tilde T : V/\operatorname{null} T \to \operatorname{range} T$ is the induced isomorphism, and $j : \operatorname{range} T \hookrightarrow W$ is the inclusion (injective). This is the *epi-iso-mono factorisation*, the same one available in any abelian category.

**Calibration check.** Verify that $\pi$ is linear and surjective with $\operatorname{null} \pi = U$. Verify that $\tilde T$ is well-defined and linear (using the definitions of the quotient operations). Confirm that $\tilde T$ is injective and that $\operatorname{range} \tilde T = \operatorname{range} T$, completing the proof of the first isomorphism theorem.

---

# Unlocked by This

> [!tip] Rank-Nullity Reread *(from this topic)*
> The dimension equation $\dim V = \dim \operatorname{null} T + \dim \operatorname{range} T$ from the [[Thm - Fundamental Theorem of Linear Maps|fundamental theorem of linear maps]] is the counting shadow of the isomorphism $V/\operatorname{null} T \cong \operatorname{range} T$ — both sides count the dimension of the same vector space. See [[Thm - Quotient Space Dimension and the Fundamental Theorem Reread]].

> [!tip] Categorical Epimorphisms and Monomorphisms *(from Category Theory)*
> In the category of vector spaces, surjective maps are exactly the *epimorphisms* (right-cancellable maps) and injective maps are exactly the *monomorphisms* (left-cancellable maps). Every linear map factors canonically as epi-then-mono via $T = j \circ \tilde T \circ \pi$, and the existence of this epi-iso-mono factorisation is the defining property of *abelian categories*, which generalise vector spaces and abelian groups.

> [!tip] Exact Sequences *(from Homological Algebra)*
> A short exact sequence of vector spaces is $0 \to U \xrightarrow{i} V \xrightarrow{\pi} V/U \to 0$ where $i$ is injective, $\pi$ is surjective, and $\operatorname{range} i = \operatorname{null} \pi$. The quotient map $\pi$ is the structural object that makes the sequence exact, and short exact sequences are the basic building blocks of homological algebra. For vector spaces every such sequence *splits* — there exists a section $V/U \to V$ inverting $\pi$ — but this is special to vector spaces and modules over fields.
