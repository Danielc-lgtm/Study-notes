---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Distribution on a Manifold"
  - "Def - Vector Field on a Manifold"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, differential-geometry, frobenius]
---

# Notation

$M$ is a smooth manifold; $D$ is a smooth distribution on $M$ — see [[Def - Distribution on a Manifold]]. $\Gamma(D)$ is the space of smooth (local or global) sections of $D$. The [[Def - The Lie Bracket of Vector Fields|Lie bracket]] of two smooth vector fields $X, Y \in \mathfrak{X}(M)$ is the smooth vector field $[X, Y]$ satisfying $[X, Y]f = X(Yf) - Y(Xf)$ for every $f \in C^\infty(M)$.

---

# Axiom Motivation

What we want to invent is a *Lie-algebraic* condition on a distribution $D$ that captures the *geometric* property of having integral submanifolds. The desideratum is concrete: we want a condition that is (i) algebraic and pointwise-checkable, (ii) necessary for the existence of an integral submanifold through every point, and (iii) sufficient — the eventual content of the [[Thm - The Frobenius Theorem|Frobenius theorem]].

Here is the picture that forces the definition. Suppose $D$ does admit an integral submanifold $N$ through every point, so $T_pN = D_p$ for $p \in N$. Take two smooth sections $X, Y \in \Gamma(D)$ — vector fields whose values everywhere lie in $D$. At every $p \in N$, $X_p$ and $Y_p$ lie in $T_pN$, so they are tangent to $N$. Now use a fact from the theory of vector fields on submanifolds: if $X$ and $Y$ are tangent to a submanifold $N$ along all of $N$, then so is their Lie bracket $[X, Y]$. This is `Corollary 8.32` in Lee — it says the bracket of two vector fields tangent to a submanifold is itself tangent to the submanifold. In our setting, this gives $[X, Y]_p \in T_pN = D_p$ for every $p \in N$. Since every point of $M$ lies in *some* integral submanifold (integrability assumption), $[X, Y]_p \in D_p$ everywhere. So the bracket of any two sections of $D$ is itself a section of $D$.

This is the necessary condition. The brilliance of Frobenius is to recognize it is also *sufficient*: a distribution closed under brackets always has integral submanifolds. So bracket-closure is the right algebraic condition to bridge from local linear-algebra data ($D_p \subseteq T_pM$) to global geometric existence (integral submanifolds).

Why brackets and not some other operation? Because the Lie bracket is the natural operation on vector fields induced by the smooth structure — it measures "how non-commutative two flows are." Concretely, $[X, Y]_p = \lim_{t \to 0} (\phi_t^{Y*} X)_p - X_p)/t$ where $\phi_t^Y$ is the flow of $Y$; this is the Lie derivative $\mathcal{L}_Y X$, which is the same as $[Y, X]$ up to sign. The geometric meaning: if you flow along $X$ for time $t$, then along $Y$ for time $t$, then back along $X$, then back along $Y$, you do not return to the starting point — you end up displaced by approximately $t^2 [X, Y]$ at second order. So the bracket measures the "leakage" from a square flow loop. For an integral submanifold to exist, the leakage must stay inside $D$ — the flow square has to close in the $k$-dimensional direction, not escape into the complementary directions.

The "if you stayed strictly inside $D$ along the loop, your residual displacement is inside $D$" is exactly the bracket-closure condition. So involutivity is precisely the condition that the "flow square" of any two sections of $D$ does not escape $D$ — and this is geometrically what it means for $D$ to be the tangent bundle of a submanifold along which we are moving.

What would be wrong with a *stronger* condition, like demanding $[X, Y] = 0$ for all pairs? That would force all local frames of $D$ to commute. Such a distribution would *also* be involutive — vacuously, $0 \in D$. But many involutive distributions are not commutative: take $D = T\mathbb{R}^2$ on $\mathbb{R}^2$ in polar coordinates, with the polar frame $(\partial_r, r^{-1}\partial_\theta)$. The bracket is non-zero, but it remains in $D$ (which is all of $T\mathbb{R}^2$). So "involutive" is the right condition, weaker than "commutative."

What about a *weaker* condition, like $[X, Y]_p \in D_p$ only for one chosen frame? Lemma 19.4 in Lee shows that involutivity *is* a local-frame condition: $D$ is involutive iff for some (equivalently any) local frame $V_1, \dots, V_k$, every bracket $[V_i, V_j]$ is a section of $D$ on the same neighborhood. So we have not weakened the definition by going from "every pair of sections" to "every pair of frame vectors" — the latter is equivalent, and computationally easier.

In summary, involutivity is forced by exactly one consideration: it is the *infinitesimal* version of "integral submanifolds exist," forced from the global geometric fact by taking brackets along the submanifold.

---

# The Definition

Let $D$ be a smooth distribution on $M$. We say $D$ is **involutive** (or **in involution**) if for every pair of smooth vector fields $X, Y$ that are local sections of $D$ (i.e. $X_p, Y_p \in D_p$ for every $p$ in some open set $U \subseteq M$), the Lie bracket $[X, Y]$ is also a local section of $D$ on $U$.

Equivalently: the space $\Gamma(D)$ of smooth global sections of $D$ is a **Lie subalgebra** of the Lie algebra $\mathfrak{X}(M)$ of all smooth vector fields (closed under the bracket operation).

Equivalently (Lemma 19.4 in Lee): if in a neighborhood of every point $p \in M$ there exists a smooth local frame $V_1, \dots, V_k$ for $D$ such that $[V_i, V_j]$ is a section of $D$ for each pair $i, j \in \{1, \dots, k\}$, then $D$ is involutive.

---

# Categorical / Structural Definition

A smooth distribution $D$ on $M$ corresponds to a $C^\infty(M)$-[[Def - Submodule|submodule]] $\Gamma(D) \subseteq \mathfrak{X}(M)$. The Lie bracket gives $\mathfrak{X}(M)$ the structure of a [[Def - Lie Algebra|Lie algebra]] over $\mathbb{R}$ (not over $C^\infty(M)$ — the bracket is not $C^\infty$-bilinear). **Involutivity** is the categorical statement that $\Gamma(D)$ is a *Lie subalgebra* of $\mathfrak{X}(M)$ — closed under the bracket operation, in addition to being closed under $\mathbb{R}$-linear combinations.

The dual reformulation: a distribution can be described by its **annihilating [[Def - Ideal|ideal]]** $\mathcal{I}(D) \subseteq \Omega^*(M)$, the graded [[Def - Ideal|ideal]] of forms that vanish when contracted with any section of $D$. Involutivity is equivalent to $\mathcal{I}(D)$ being a **differential ideal** — closed under the exterior derivative ($d\mathcal{I}(D) \subseteq \mathcal{I}(D)$). This is the forms-language version, proved in [[Thm - Frobenius Theorem in Forms Language]].

---

# Relate to Other Fields / Compression

**True name:** Involutivity is *flow-square closure*. The operational meaning is: if you flow infinitesimally along $X$, then $Y$, then $-X$, then $-Y$ (all sections of $D$), you don't return to where you started — but the residual displacement $\approx t^2 [X, Y]$ stays inside $D$. So involutivity is precisely the condition that flow-loops in $D$ have residuals that *stay in $D$*. This is the correct image to carry when working with the condition.

**Compression to Lie algebra theory.** A Lie subalgebra is by definition a vector subspace closed under the bracket. The space $\Gamma(D)$ is an $\mathbb{R}$-vector subspace of $\mathfrak{X}(M)$ (closed under addition and scalar multiplication, since $D_p$ is a subspace fiberwise); involutivity is just demanding it also be closed under the bracket. So "involutive distribution" = "Lie-subalgebra structure on $\Gamma(D)$." The Frobenius theorem can then be read as: *every Lie subalgebra of $\mathfrak{X}(M)$ that comes from a vector subbundle of $TM$ is the tangent bundle of a foliation*.

**Compression to PDE compatibility.** For an overdetermined system $\partial u/\partial x^i = \alpha^i(x, u)$, the **compatibility condition** for solvability is precisely the involutivity of the associated distribution $D$ spanned by $X_i = \partial_{x^i} + \alpha^i\partial_u$. Computing $[X_i, X_j]$ yields the cross-condition $\partial_j\alpha^i + \alpha^j\partial_u\alpha^i = \partial_i\alpha^j + \alpha^i\partial_u\alpha^j$ — the symmetry-of-mixed-partials condition in disguise.

**Compression to mechanics.** A *holonomic* constraint on configuration space is one definable by configuration equations $f_1 = \cdots = f_r = 0$ — the constraint is integrable. A *nonholonomic* constraint, given as velocity equations $\omega^1(\dot{q}) = \cdots = \omega^r(\dot{q}) = 0$, is holonomic iff the distribution $D = \bigcap_i \ker \omega^i$ is involutive. The skate on ice and the rolling ball are non-involutive examples; gear-train constraints and surface constraints are involutive.

---

# Examples / Corollaries

**Is an instance: every rank-$1$ distribution is involutive.** A rank-$1$ distribution is locally spanned by a single nowhere-vanishing vector field $V$, and the only bracket to check is $[V, V] = 0 \in \Gamma(D)$ trivially. So involutivity is vacuous at rank $1$, and the Frobenius theorem at rank $1$ just recovers the existence of integral curves — already known from ODE theory. Involutivity becomes interesting at rank $\geq 2$.

**Is an instance: the distribution spanned by coordinate vector fields $\partial_1, \dots, \partial_k$ in $\mathbb{R}^n$.** All brackets $[\partial_i, \partial_j] = 0$, so trivially involutive. The integral submanifolds are the slices $x^{k+1} = c^{k+1}, \dots, x^n = c^n$. This is the "flat" example, and the Frobenius theorem guarantees that *every* involutive distribution is locally of this form, up to a change of coordinates.

**Is an instance: the kernel of a submersion.** Let $F : M \to N$ be a smooth submersion; the distribution $D_p = \ker dF_p$ has integral manifolds the fibers $F^{-1}(F(p))$. Sections of $D$ are vector fields that are tangent to every fiber, equivalently, vector fields $X$ such that $dF(X) = 0$. If $X, Y$ are such, then $dF([X, Y]) = [dF(X), dF(Y)] = [0, 0] = 0$ (using naturality of brackets under smooth maps for projectable fields, and noting that vertical fields are projectable), so $[X, Y] \in \Gamma(D)$. This is the structural source of involutivity from "level sets exist by construction."

**Is an instance: the orbit distribution of a [[Def - Group|group]] action.** If a Lie [[Def - Group|group]] $G$ acts smoothly on $M$, with Lie algebra $\mathfrak{g}$, the fundamental vector fields $X^*$ for $X \in \mathfrak{g}$ span a distribution $D$ (the *orbit distribution*) whose fiber $D_p$ is the tangent space to the orbit through $p$ (assuming locally free action so the rank is constant). Involutivity of $D$ follows from the Lie algebra homomorphism property $[X^*, Y^*] = -[X, Y]^* \in \Gamma(D)$. The integral submanifolds are the orbits, by construction.

**Is NOT an instance: the standard contact distribution $\ker(dz - y\,dx)$ on $\mathbb{R}^3$.** With $X = \partial_y$ and $Y = \partial_x + y\partial_z$ a frame, we compute $[X, Y] = [\partial_y, \partial_x + y\partial_z] = \partial_z$. But $\partial_z$ is *not* in $D$: $\alpha(\partial_z) = dz(\partial_z) - y\,dx(\partial_z) = 1 \neq 0$. So $[X, Y] \notin \Gamma(D)$, and the distribution fails to be involutive. This is the prototype non-example — see [[Ex - A Non-Integrable Distribution on R^3 from the Standard Contact Form]] for the full picture.

**Is NOT an instance: a rank-$2$ distribution on $\mathbb{R}^3$ defined by a generic $1$-form.** Pick $\alpha = a(x,y,z)\,dx + b(x,y,z)\,dy + c(x,y,z)\,dz$ a non-vanishing $1$-form with $a, b, c$ generic functions. The distribution $D = \ker \alpha$ is involutive iff $\alpha \wedge d\alpha = 0$, which after expansion becomes the single PDE $a(\partial_y c - \partial_z b) + b(\partial_z a - \partial_x c) + c(\partial_x b - \partial_y a) = 0$. For *generic* choices of $a, b, c$ this condition fails, so generically the distribution is *not* involutive — non-involutivity is the "default" behavior of rank-$(n-1)$ distributions.

**Corollary (involutivity is a local condition).** $D$ is involutive iff every point has a neighborhood on which the local-frame criterion holds. So checking involutivity reduces to a finite computation at every point — pick a local frame, compute its $\binom{k}{2}$ brackets, verify each is in $\Gamma(D)$.

**Corollary (involutivity is preserved by [[Def - Diffeomorphism|diffeomorphism]]).** If $F : M \to N$ is a diffeomorphism and $D$ is an involutive distribution on $M$, then $F_*D$ (pushforward) is an involutive distribution on $N$. Proof: the bracket is natural under [[Def - Diffeomorphism|diffeomorphisms]], $F_*[X, Y] = [F_*X, F_*Y]$, so if $X, Y$ are sections of $D$ and their bracket is in $D$, the same holds for the pushforwards.

**Corollary (the orbit distribution of a free Lie group action is involutive).** Used in Lee's proof of the existence of Lie [[Def - Subgroup|subgroups]] associated to Lie subalgebras (`Theorem 19.26`).

**Calibration check.** If you have understood the definition you should be able to (i) verify a given distribution is involutive by computing all bracket pairs of a local frame, (ii) identify the standard contact distribution as a non-example by computing $[\partial_y, \partial_x + y\partial_z]$ and checking the result is not in the kernel of $dz - y\,dx$, and (iii) state in one sentence why involutivity is a *necessary* condition for integrability (vector fields tangent to a submanifold have brackets tangent to the same submanifold).

---

# Unlocked by This

> [!tip] **The Frobenius theorem** *(from this same topic)*
> The deep content of involutivity is that it is *sufficient* for integrability: every involutive distribution admits integral submanifolds through every point, with a flat chart structure. This is the [[Thm - The Frobenius Theorem|Frobenius theorem]], proved by reducing to commuting vector fields via the canonical-form construction.

> [!tip] **Forms-language criterion** *(from this same topic)*
> Involutivity has an equivalent formulation entirely in differential forms: the annihilating ideal $\mathcal{I}(D)$ is a *differential ideal*, $d\mathcal{I}(D) \subseteq \mathcal{I}(D)$. Equivalently, $d\omega^i = \sum_j \omega^j \wedge \alpha^i_j$ for some $1$-forms $\alpha^i_j$, where $\omega^1, \dots, \omega^{n-k}$ are local defining forms. See [[Thm - Frobenius Theorem in Forms Language]].

> [!tip] **Lie subalgebra of $\mathfrak{X}(M)$** *(from Lie Theory and Differential Geometry)*
> Involutive distributions on $M$ correspond to (locally-free, finitely-generated) Lie subalgebras of $\mathfrak{X}(M)$ that are also $C^\infty(M)$-submodules. This algebraic viewpoint is the bridge between geometric questions (does a foliation exist?) and Lie-theoretic ones (does a Lie subalgebra integrate to a Lie subgroup?).

> [!tip] **Bracket-generating distributions and the Chow–Rashevskii theorem** *(from Sub-Riemannian Geometry and Control Theory)*
> The *opposite* of involutivity: a distribution is **bracket-generating** if iterating brackets $[X_i, X_j], [X_i, [X_j, X_k]], \dots$ eventually spans all of $TM$. The Chow–Rashevskii theorem says a bracket-generating distribution is *controllable* — any two points can be connected by a path tangent to $D$. The non-involutive standard contact distribution is bracket-generating on $\mathbb{R}^3$, which is why a parallel-parking maneuver (only allowed motions in $D$) can reach any configuration.
