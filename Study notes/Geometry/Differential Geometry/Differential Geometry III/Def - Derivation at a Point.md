---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Function on a Manifold"
  - "Def - The Smooth Functions Ring"
  - "Def - Vector Space"
tags: [geometry, differential-geometry]
---

# Notation

Let $M$ be a [[Def - Smooth Manifold|smooth manifold]] and $p \in M$. The ring of smooth real-valued functions on $M$ is $C^{\infty}(M)$, see [[Def - The Smooth Functions Ring]]. Linear maps and the Leibniz product rule are written in standard notation; the action of an operator $v$ on a function $f$ is written either $v(f)$ or $vf$. The full notation registry is on [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# Axiom Motivation

The thing we want to axiomatize is **a first-order local linear operator at $p$**. The motivation comes from two parallel observations in Euclidean space — both true, both essential — that together force the definition.

The first observation is that in $\mathbb{R}^{n}$, a tangent vector $v$ at a point $a$ acts naturally on smooth functions through directional differentiation: $D_{v}|_{a} f = (d/dt)|_{0} f(a + tv) = v^{i}\,\partial f/\partial x^{i}(a)$. Two different vectors give two different directional-derivative operators (apply both to the linear coordinate functions $x^{i}$ to read off the components), so the map $v \mapsto D_{v}|_{a}$ is injective. The vector is its directional derivative — the "thing that differentiates functions in the $v$-direction" *is* the vector. So if we want a definition of tangent vector that uses only $C^{\infty}(M)$, we should look at the class of operators on $C^{\infty}(M)$ that "look like directional derivatives".

The second observation is that every directional-derivative operator $D_{v}|_{a}$ satisfies *exactly two* algebraic identities: it is $\mathbb{R}$-linear in $f$, and it satisfies the Leibniz product rule $D_{v}|_{a}(fg) = f(a)\,D_{v}|_{a} g + g(a)\,D_{v}|_{a} f$. Linearity is immediate; the Leibniz rule comes from the standard product rule for derivatives, since $(fg)'(t) = f'(t)g(t) + f(t)g'(t)$ at $t = 0$ gives precisely that statement. So directional-derivative operators belong to the set of linear operators satisfying these two identities — and a remarkable fact, proved in [[Thm - Equivalence of Tangent Vector Definitions]], is that this set contains *nothing else* on $\mathbb{R}^{n}$. Every linear-and-Leibniz operator at $a \in \mathbb{R}^{n}$ is a directional derivative.

That fact is the whole motivation for the definition. We take the two algebraic identities — linearity and Leibniz — and *promote them to axioms*. On an abstract manifold $M$ where there is no ambient $\mathbb{R}^{N}$ and no directional derivative to define, we define a tangent vector at $p$ as a linear map $v : C^{\infty}(M) \to \mathbb{R}$ that satisfies $v(fg) = f(p)\,v(g) + g(p)\,v(f)$. The theorem (3.2 in Lee) certifies that on $\mathbb{R}^{n}$ this recovers the geometric tangent vectors. On a manifold, this becomes the *definition* — there is nothing else to recover from. The Leibniz rule is doing all the work: it forces $v$ to depend only on the first-order behaviour of $f$ at $p$, because if $f(p) = g(p) = 0$ then $v(fg) = 0$, so any function with a double zero at $p$ is killed; and if $f$ is constant then $v(f) = 0$, because $v(c) = v(c \cdot 1) = c \cdot v(1) + 1 \cdot v(c) - c \cdot v(1)$ ... actually $v(1) = v(1 \cdot 1) = 1 \cdot v(1) + 1 \cdot v(1) = 2v(1)$ forces $v(1) = 0$, and then linearity finishes the job. So the Leibniz rule alone implies that constants are annihilated and that $v$ depends only on the first Taylor coefficient of $f$ at $p$ — which is exactly the "first-order" content.

Why not strengthen the Leibniz rule to demand the second-order rule $v(fgh) = f(p)g(p)v(h) + \cdots$ as well? Because that would be vacuous — the second-order rule follows from the first-order rule by induction. Why not weaken the Leibniz rule to merely $v(fg) = v(f)g(p) + f(p)v(g) + \text{error}$? Because then the operator would no longer be first-order — second-order terms would survive — and we would be axiomatizing the wrong thing. The Leibniz rule at $p$ is exactly the threshold at which "first-order" is forced and "second-order" is forbidden.

Why demand $\mathbb{R}$-linearity rather than $C^{\infty}$-linearity? Because $C^{\infty}$-linearity is much *stronger* and would exclude the operators we want. A linear-over-smooth-functions operator $v : C^{\infty}(M) \to \mathbb{R}$ would satisfy $v(fg) = f \cdot v(g)$, which evaluated at $p$ becomes $v(fg) = f(p)\,v(g)$ — losing the symmetric Leibniz contribution from $f$. This would make $v$ a multiplication-by-function operator, not a derivation. The right level of linearity is over the base field $\mathbb{R}$, which lets the Leibniz term be the *symmetric* combination $f(p)\,v(g) + g(p)\,v(f)$ that genuinely encodes first-order behaviour.

A reader who has never seen this definition could invent it as follows. Start with the desire to define "tangent vector at $p$" using only $C^{\infty}(M)$. Observe that in $\mathbb{R}^{n}$ vectors are directional derivatives. Observe that directional derivatives satisfy linearity and Leibniz at the point. Promote these two identities to axioms. The remarkable consequence, which has to be proved, is that this captures *exactly* the right notion — no more, no less.

---

# The Definition

Let $M$ be a smooth manifold and $p \in M$. A **derivation at $p$** is a map
$$v : C^{\infty}(M) \to \mathbb{R}$$
that is

1. **$\mathbb{R}$-linear**: $v(\alpha f + \beta g) = \alpha\,v(f) + \beta\,v(g)$ for all $\alpha, \beta \in \mathbb{R}$ and $f, g \in C^{\infty}(M)$,
2. **Leibniz at $p$**: $v(fg) = f(p)\,v(g) + g(p)\,v(f)$ for all $f, g \in C^{\infty}(M)$.

The set of all derivations at $p$ is a real vector space under pointwise operations:
$$(v_{1} + v_{2})(f) = v_{1}(f) + v_{2}(f), \qquad (cv)(f) = c \cdot v(f).$$

This vector space is called the **tangent space** to $M$ at $p$ and is denoted $T_{p}M$; see [[Def - The Tangent Space]].

**Two immediate consequences of the axioms** (proved below as corollaries):

- Constants are annihilated: if $f \equiv c$ then $v(f) = 0$.
- Vanishing-pairs are annihilated: if $f(p) = g(p) = 0$ then $v(fg) = 0$.

These two facts together show that $v$ depends only on the *first-order* behaviour of its argument at $p$.

---

# Relate to Other Fields / Compression

A derivation at a point of a manifold is the special case of a **derivation of a commutative algebra** valued in a module at a fixed character. Concretely: $C^{\infty}(M)$ is a commutative $\mathbb{R}$-algebra; evaluation at $p$ is a ring homomorphism $\mathrm{ev}_{p} : C^{\infty}(M) \to \mathbb{R}$; and a derivation at $p$ is a linear map satisfying the Leibniz rule *with respect to* $\mathrm{ev}_{p}$. In the algebraic-geometry tradition this is called a **point derivation**, and the space of point derivations at a maximal ideal $\mathfrak{m}_{p} = \ker(\mathrm{ev}_{p})$ is canonically the dual of the cotangent space $\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2}$. In differential-geometry language this same space is $T_{p}M$, and the Lee construction is built to extract it from $C^{\infty}(M)$ without going through the algebraic detour.

**True name:** A derivation at $p$ is "the first-order Taylor coefficient at $p$, viewed as a linear functional on $C^{\infty}(M)$". Everything beyond first order is annihilated by the Leibniz rule (via the double-vanishing corollary), and the constant term is annihilated by the constant-killing corollary, so $v(f)$ depends only on the *gradient* of $f$ at $p$. This is what makes derivations finite-dimensional even though they are defined on an infinite-dimensional function space: they see only first-order information, and first-order information at a point in an $n$-manifold has $n$ free parameters.

The same axioms — linearity and Leibniz — define the more general notion of a **derivation of an algebra valued in a module**: if $A$ is a commutative algebra and $M$ is an $A$-module, an $A$-linear derivation $D : A \to M$ satisfies $D(ab) = a\,D(b) + b\,D(a)$. Vector fields on $M$ are precisely the derivations of $C^{\infty}(M)$ valued in $C^{\infty}(M)$ itself (no point pinned down), and the bracket of two such derivations is again a derivation — this is the algebraic source of the [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket|Lie bracket of vector fields]].

In **algebraic geometry**, the same definition applied to the local ring at $p$ gives the **Zariski tangent space** $(\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2})^{*}$ of an algebraic variety, which can be larger than the dimension of the variety at singular points. Smoothness of a variety at $p$ is precisely the condition that the Zariski tangent space has the expected dimension. The differential-geometric and algebraic-geometric tangent-space constructions are *the same construction*, applied to different algebras (smooth functions vs. regular functions).

---

# Examples / Corollaries

**Is an instance: directional derivative on $\mathbb{R}^{n}$.** Fix $a \in \mathbb{R}^{n}$ and $v \in \mathbb{R}^{n}$. The map $D_{v}|_{a} : C^{\infty}(\mathbb{R}^{n}) \to \mathbb{R}$ defined by $D_{v}|_{a} f = (d/dt)|_{0} f(a + tv) = v^{i}\,\partial f/\partial x^{i}(a)$ is a derivation at $a$. Linearity is immediate; the Leibniz rule follows from the product rule of one-variable calculus applied to $(fg)(a + tv) = f(a + tv)\,g(a + tv)$. This is the prototype — and on $\mathbb{R}^{n}$, *every* derivation at $a$ has this form, with $v^{i} = D_{v}|_{a}(x^{i})$, see [[Thm - Equivalence of Tangent Vector Definitions]].

**Is an instance: $\partial/\partial x^{i}|_{p}$ in a chart.** Given a chart $(U, \varphi)$ on $M$ with coordinates $x^{1}, \dots, x^{n}$ and a point $p \in U$, the map $(\partial/\partial x^{i}|_{p})(f) = (\partial \hat{f}/\partial x^{i})(\varphi(p))$, where $\hat{f} = f \circ \varphi^{-1}$, is a derivation at $p$. This is the special case of the previous example, taken on the coordinate representative — the Leibniz rule transfers because $\widehat{fg} = \hat{f}\hat{g}$ for the standard coordinate representation. See [[Def - Coordinate Tangent Vectors]] for the full development.

**Is an instance: velocity of a curve.** For a smooth curve $\gamma : J \to M$ with $\gamma(0) = p$, the map $v : C^{\infty}(M) \to \mathbb{R}$ defined by $v(f) = (f \circ \gamma)'(0)$ is a derivation at $p$. Linearity is immediate; the Leibniz rule follows from $(f \circ \gamma)(g \circ \gamma) = (fg) \circ \gamma$ and the one-variable product rule. See [[Def - Velocity of a Curve]].

**Is NOT an instance: evaluation at $p$.** The map $\mathrm{ev}_{p}(f) = f(p)$ is linear but does *not* satisfy the Leibniz rule at $p$: $\mathrm{ev}_{p}(fg) = f(p)g(p)$, while $f(p)\,\mathrm{ev}_{p}(g) + g(p)\,\mathrm{ev}_{p}(f) = 2f(p)g(p)$. The two agree only when $f(p)g(p) = 0$. So evaluation at $p$ is a ring homomorphism but not a derivation — it sees the *value* of $f$, not its first-order behaviour.

**Is NOT an instance: second-order operator.** The map $v(f) = (\partial^{2} f/\partial x^{1} \partial x^{2})(p)$ on $C^{\infty}(\mathbb{R}^{n})$ is $\mathbb{R}$-linear but fails the Leibniz rule. Apply it to $f(x) = x^{1}$ and $g(x) = x^{2}$: then $f(p) = p^{1}$, $g(p) = p^{2}$, $v(f) = v(g) = 0$ (each is a single coordinate), but $v(fg) = v(x^{1}x^{2}) = 1$. Yet the Leibniz rule would give $f(p) \cdot 0 + g(p) \cdot 0 = 0$. The contradiction is the signature of "second-order" — the Leibniz rule precisely rules out operators that look at second derivatives.

**Corollary (constants are annihilated).** If $f \equiv c$ is a constant function, then $v(f) = 0$. *Proof:* First, $v(1) = v(1 \cdot 1) = 1 \cdot v(1) + 1 \cdot v(1) = 2\,v(1)$ by the Leibniz rule, so $v(1) = 0$. Then $v(c) = v(c \cdot 1) = c\,v(1) = 0$ by linearity. This is the most elementary consequence of the Leibniz rule and is used constantly.

**Corollary (vanishing pairs are annihilated).** If $f(p) = g(p) = 0$, then $v(fg) = 0$. *Proof:* By the Leibniz rule, $v(fg) = f(p)\,v(g) + g(p)\,v(f) = 0 + 0 = 0$. The geometric content is that functions with a double zero at $p$ (which $fg$ has when both factors vanish there) lie in the *square* of the maximal ideal $\mathfrak{m}_{p}$ and are killed by any derivation at $p$. This is the algebraic root of "derivations are first-order".

**Corollary (locality).** If $f, g \in C^{\infty}(M)$ agree on a neighbourhood of $p$, then $v(f) = v(g)$. *Proof:* Let $h = f - g$; then $h$ vanishes in a neighbourhood of $p$. Choose a bump function $\psi$ (see [[Def - Bump Function and Smooth Cutoff]]) supported in $M \setminus \{p\}$ that equals $1$ on the support of $h$. Then $\psi h = h$ identically, and $\psi(p) = h(p) = 0$, so $v(h) = v(\psi h) = \psi(p)\,v(h) + h(p)\,v(\psi) = 0$. By linearity $v(f) = v(g)$. This is the key technical fact that lets us identify $T_{p}M$ with $T_{p}U$ for any open neighbourhood $U$ of $p$.

**Calibration check.** Verify that the operator $v(f) = f'(0) + f''(0)$ on $C^{\infty}(\mathbb{R})$ is *not* a derivation at $0$ — show by computing $v(x \cdot x) = v(x^{2}) = 2$ versus $x(0)\,v(x) + x(0)\,v(x) = 0$ that the Leibniz rule fails. Verify that $v(f) = 3\,f'(0)$ *is* a derivation. Verify that for two derivations $v_{1}, v_{2}$ at $p$, the sum $v_{1} + v_{2}$ is again a derivation. If you can also explain why constants are annihilated using only linearity and the Leibniz rule, you have understood the definition.

---

# Unlocked by This

> [!tip] The Tangent Space $T_{p}M$ *(from Differential Geometry)*
> The set of all derivations at $p$ forms a real vector space, the **tangent space** $T_{p}M$, see [[Def - The Tangent Space]]. The vector space structure is what makes derivations the cleanest definition of tangent vector — addition and scalar multiplication are pointwise on functions, and the axioms are preserved.

> [!tip] Vector Fields as Global Derivations *(from Differential Geometry)*
> Dropping the "at $p$" specification and instead asking for a map $X : C^{\infty}(M) \to C^{\infty}(M)$ that is $\mathbb{R}$-linear and satisfies $X(fg) = f X(g) + g X(f)$ globally gives the **algebraic** definition of a vector field. This is the perspective of [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]] and connects to the ring-theoretic side: vector fields are derivations of the [[Def - Ring|ring]] $C^{\infty}(M)$.

> [!tip] Zariski Tangent Space *(from Algebraic Geometry)*
> The same definition applied to the local ring $\mathcal{O}_{X, p}$ of an algebraic variety $X$ at a point $p$ gives the **Zariski tangent space** $(\mathfrak{m}_{p}/\mathfrak{m}_{p}^{2})^{*}$. For smooth algebraic varieties, this matches the differential-geometric tangent space; for singular points it is larger, and the discrepancy detects the singularity. This is one of the cleanest bridges between differential and algebraic geometry.
