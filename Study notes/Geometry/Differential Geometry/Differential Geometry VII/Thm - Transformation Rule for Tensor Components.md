---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Tensor Field on a Manifold"
  - "Def - Mixed Tensor"
  - "Def - Change of Basis Matrix"
tags: [geometry, differential-geometry, transformation-rule]
---

# Notation

$M$ is a smooth $n$-manifold. $(U, x^i)$ and $(\tilde U, \tilde x^i)$ are smooth charts on $M$ with overlapping domain. The Jacobians of the change-of-coordinates map are $\frac{\partial \tilde x^i}{\partial x^a}$ (new-from-old, the Jacobian of $\tilde x \circ x^{-1}$) and $\frac{\partial x^a}{\partial \tilde x^i}$ (old-from-new, its inverse). Einstein summation is in force. A $(k, \ell)$-tensor field $A$ has components $A^{i_1\cdots i_k}_{j_1\cdots j_\ell}$ in the $(x)$ chart and $\tilde A^{i_1\cdots i_k}_{j_1\cdots j_\ell}$ in the $(\tilde x)$ chart. Full notation registry: [[Differential Geometry VII — Tensors and Tensor Fields]].

---

# Statement

> **Theorem (Transformation Rule).** Let $A$ be a smooth $(k, \ell)$-tensor field on $M$, with components $A^{i_1\cdots i_k}_{j_1\cdots j_\ell}$ in a chart $(x^i)$ and $\tilde A^{i_1\cdots i_k}_{j_1\cdots j_\ell}$ in an overlapping chart $(\tilde x^i)$. On the overlap,
> $$\tilde A^{i_1\cdots i_k}_{j_1\cdots j_\ell} = \frac{\partial \tilde x^{i_1}}{\partial x^{a_1}}\cdots\frac{\partial \tilde x^{i_k}}{\partial x^{a_k}}\,\frac{\partial x^{b_1}}{\partial \tilde x^{j_1}}\cdots\frac{\partial x^{b_\ell}}{\partial \tilde x^{j_\ell}}\, A^{a_1\cdots a_k}_{b_1\cdots b_\ell}.$$
> *Each upper index contracts with the new-from-old Jacobian; each lower index with the old-from-new Jacobian.*

> **Converse (Classical Definition).** Conversely, if a collection of smooth functions $A^{i_1\cdots i_k}_{j_1\cdots j_\ell}$ defined chart-by-chart transforms by the above rule on every overlap, then they are the components of a unique smooth $(k, \ell)$-tensor field.

---

# Motivation

The transformation rule is the **classical (and physicists') definition of a tensor**: a tensor *is* a quantity that transforms by this rule under coordinate change. The modern manifold-level definition (smooth section of $T^{(k,\ell)}M$) and the $C^\infty(M)$-multilinearity definition both reduce to the transformation rule when read in coordinates, so the three perspectives are equivalent and the rule is the operational test.

Why is the rule structured this way? The answer is **Jacobian factors come from the chain rule applied to the basis transformations**. In a chart change from $(x^a)$ to $(\tilde x^i)$, the coordinate vector fields transform as

$$\partial_a = \frac{\partial \tilde x^i}{\partial x^a}\, \tilde\partial_i,$$

by the chain rule for partial derivatives. Dually, the coordinate 1-forms transform as

$$dx^a = \frac{\partial x^a}{\partial \tilde x^i}\, d\tilde x^i.$$

So a basis vector picks up a *new-from-old Jacobian* factor when expanded in the new basis, and a basis covector picks up an *old-from-new* factor. A tensor expanded in the basis is a linear combination of basis tensor products, and each factor's Jacobian appears in the corresponding slot of the components.

The rule is **the substance of "covariant" and "contravariant"**:
- A *covariant* index transforms with the *old-from-new* Jacobian — the same direction as a covector transforms ($dx^a$ picks up $\partial x^a / \partial \tilde x^i$).
- A *contravariant* index transforms with the *new-from-old* Jacobian — the same direction as a vector's component $v^a$ transforms ($v^a = (\partial x^a / \partial \tilde x^i) \tilde v^i$, so $\tilde v^i = (\partial \tilde x^i / \partial x^a) v^a$).

The names record dual behavior, not a mnemonic about matrix direction. Covariant tensors accept vectors, so their components acquire the inverse coordinate Jacobian when the vector basis changes; contravariant tensors accept covectors, so their components acquire the opposite Jacobian. The safest practice is to rederive the factors from $\tilde\partial_i=(\partial x^a/\partial\tilde x^i)\partial_a$ and duality rather than relying on the words.

One could ask: why is the rule formulated in terms of Jacobian factors at all, rather than in some more invariant way? The answer is that the rule *is* the invariant content of "tensor" expressed in coordinates: a coordinate-invariant quantity is one that the rule preserves between charts, and this is exactly what makes the multilinear functional (the modern definition) well-defined globally. Strip away the coordinates and you get the bundle definition; strip away the bundle and you get the functor (the $C^\infty(M)$-multilinear gadget); but coordinate-level computations need the rule.

A historical remark: classical tensor analysts (Ricci, Levi-Civita, the early 1900s) *defined* a tensor as a collection of functions on each chart that transformed by this rule. The modern bundle-section definition came later (1950s–60s) and was felt by some to be unnecessary abstraction. In practice, the two are perfectly equivalent, and most physics calculations still proceed by writing components and checking the transformation rule.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem applies whenever you have a collection of functions, one collection per chart, and you want to know if they assemble into a tensor field. The most common situation is "you have a coordinate description on a single chart; does it extend?"

**A single-chart description of an object.** Given functions $A^{i_1\cdots i_k}_{j_1\cdots j_\ell}(x)$ on a chart, *try* to extend to all of $M$ by declaring the transformation rule. If the rule produces *consistent* values on every overlap of charts, the object is a tensor field. *Bridge to the precondition:* check the cocycle condition on triple overlaps — the rule is automatically self-consistent if you start with the rule, but a non-tensorial single-chart object will produce inconsistencies on overlaps. The standard non-example: the Christoffel symbols of a connection, which have the right index structure but the wrong transformation rule (an extra second-derivative term).

**A construction defined by formula on each chart.** Often you have a formula that makes sense in any chart but uses chart-specific objects like partial derivatives. The bridge: compute the components in two charts, transform one set using the rule, and see whether they agree with the other set. If they agree, you have a tensor field; if there is an extra anomalous term (a second derivative of the transition function, or similar), you do not.

**A pulled-back tensor field.** If $F : M \to N$ is smooth and $A$ is a covariant tensor field on $N$ with components $A_{i_1\cdots i_k}(y)$, then $F^*A$ has components $(F^*A)_{a_1\cdots a_k}(x) = A_{i_1\cdots i_k}(F(x))\, (\partial F^{i_1}/\partial x^{a_1})\cdots(\partial F^{i_k}/\partial x^{a_k})$. The bridge: the components of $F^*A$ are given by the *same formula* as the transformation rule, with $F$ playing the role of the chart change. The transformation rule is what makes the pullback formula a tensor field on $M$.

**An invariant constructed from tensor fields.** If $A$ and $B$ are tensor fields and you build a contraction $C = A^{ij}B_{ij}$ (a scalar in this example), then $C$ should be invariant under chart change. The transformation rule tells you exactly: $\tilde A^{ij}\tilde B_{ij} = (\partial \tilde x^i/\partial x^a)(\partial \tilde x^j / \partial x^b)A^{ab} \cdot (\partial x^c/\partial \tilde x^i)(\partial x^d/\partial \tilde x^j)B_{cd} = A^{ab}B_{ab}$, by the cancellation of Jacobian factors. So the contraction of a tensor against a tensor gives a tensor — and the *invariance of scalars* is a special case.

**Targets (Output Amplification)**

**Tensoriality criterion in coordinates.** Once a candidate object's components transform correctly, it is automatically a tensor field, with all the consequences: it has a chart-independent meaning, it can be contracted with other tensors, it pulls back under smooth maps, etc.

**Distinction between tensors and pseudo-tensors.** Pseudo-tensors transform by the rule **plus** an extra factor of $\operatorname{sgn}(\det J)$ — a sign depending on whether the change of coordinates is orientation-preserving. Pseudo-tensors are not tensors, but they appear in physics on non-orientable manifolds (notably for densities and the Levi-Civita symbol $\epsilon$).

**Identification of non-tensors (connections, Christoffel symbols).** Christoffel symbols transform by the tensor rule plus an extra second-derivative term: $\tilde\Gamma^k_{ij} = (\partial \tilde x^k/\partial x^a)(\partial x^b/\partial \tilde x^i)(\partial x^c/\partial \tilde x^j)\Gamma^a_{bc} + (\partial \tilde x^k/\partial x^a)(\partial^2 x^a / \partial \tilde x^i \partial \tilde x^j)$. The second term is the "connection anomaly" — it disqualifies $\Gamma$ as a tensor and identifies it as a connection. The *difference* of two connections is a tensor (the anomaly cancels), which is a useful trick.

**Existence theorems for tensors via the rule.** Given functions defined on each chart that satisfy the transformation rule on overlaps, the rule certifies the existence of a global tensor field. This is how connections, metrics, and other geometric objects are built in coordinate-by-coordinate constructions — verify the rule, and the rule's universality gives you the global object.

---

# Why Is It True

The intuition is **the components of a tensor transform exactly so that the underlying tensor remains the same**. A tensor is an abstract multilinear gadget; the components are its values on basis tuples; the rule is the consequence of changing the basis.

**Mechanism in one line: $A_p$ is a basis-independent multilinear functional; the rule is the change-of-basis formula at the algebraic level, applied chart-by-chart on the manifold.**

Concretely: a covariant $k$-tensor $A_p$ at $p$ is a multilinear functional on $T_pM^k$. Pick a basis $(E_a)$ of $T_pM$ — say the coordinate frame $\partial_a$ of one chart. The components are $A_{a_1\cdots a_k} := A_p(\partial_{a_1}, \dots, \partial_{a_k})$. Now pick a different basis $(\tilde E_i)$ — say $\tilde\partial_i$ of another chart. The components in the new basis are $\tilde A_{i_1\cdots i_k} = A_p(\tilde\partial_{i_1}, \dots, \tilde\partial_{i_k})$.

But $\tilde\partial_i = (\partial x^a / \partial \tilde x^i)\, \partial_a$ by the chain rule. Substituting and using multilinearity of $A_p$:

$$\tilde A_{i_1\cdots i_k} = A_p((\partial x^{a_1}/\partial \tilde x^{i_1})\partial_{a_1}, \dots, (\partial x^{a_k}/\partial \tilde x^{i_k})\partial_{a_k}) = (\partial x^{a_1}/\partial \tilde x^{i_1})\cdots(\partial x^{a_k}/\partial \tilde x^{i_k})\,A_p(\partial_{a_1}, \dots, \partial_{a_k}) = (\partial x^{a_1}/\partial \tilde x^{i_1})\cdots(\partial x^{a_k}/\partial \tilde x^{i_k})\,A_{a_1\cdots a_k}.$$

This is the transformation rule for purely covariant tensors. The contravariant case is dual: a vector $v = v^a \partial_a = \tilde v^i \tilde\partial_i$, with $\tilde v^i = (\partial \tilde x^i/\partial x^a) v^a$ by the chain rule. The mixed case combines both factors.

**Why upper-index Jacobians and lower-index Jacobians go in opposite directions:** It is forced by the dual pairing $\varepsilon^j(E_i) = \delta^j_i$. If $E_i$ transforms by Jacobian $J^a_i$ ("old basis from new"), then $\varepsilon^j$ must transform by $(J^{-1})^j_b$ ("new from old") to preserve the dual pairing. So basis vectors and basis covectors transform by *inverse* matrices, and a tensor's components (which are values on basis tuples) inherit this duality.

---

# What Makes This Hard

The non-trivial part is keeping the index conventions consistent. There are *eight* different ways to write a Jacobian factor (depending on which indices are old and which are new, and whether it is the new-from-old or old-from-new), and confusion about which one to use is the most common source of error. The mnemonic that almost never fails:

- "Upper index $i$ on tensor, lower index $a$ on Jacobian, both new-versus-old" — the Jacobian is $\partial \tilde x^i / \partial x^a$, new-from-old.
- "Lower index $j$ on tensor, upper index $b$ on Jacobian, both new-versus-old" — the Jacobian is $\partial x^b / \partial \tilde x^j$, old-from-new.

The general rule: **the Jacobian factor has the *new* index on the top in the same position as the tensor index**. Upper tensor index $\tilde i$ → upper Jacobian numerator $\tilde x^i$. Lower tensor index $\tilde j$ → lower Jacobian denominator $\tilde x^j$.

A second common error is confusing a differential form, a coordinate symbol, and a density. A volume form is a genuine nowhere-vanishing covariant $n$-tensor and obeys the ordinary tensor rule. The array $\epsilon_{i_1\dots i_n}$ whose entries are fixed to $0,\pm1$ in every coordinate system is not the component array of a tensor; a metric volume form has components $\sqrt{|\det g|}\,\epsilon_{i_1\dots i_n}$ in an oriented chart. A density instead uses an absolute-Jacobian transformation law and can be integrated without choosing an orientation.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show that the transformation rule for components is forced by writing the tensor as a sum over basis tensor products and using the chain rule to relate coordinate frames of two charts. Conversely, given components satisfying the rule on every overlap, the rule's cocycle condition (triple overlap consistency) lets you assemble them into a global tensor field.

**Subgoal decomposition:**

1. **Chain rule for coordinate frames.** Show $\tilde\partial_i = (\partial x^a / \partial \tilde x^i)\, \partial_a$ and $dx^a = (\partial x^a / \partial \tilde x^i)\, d\tilde x^i$.
   - *Hint:* Apply $\tilde\partial_i = \partial/\partial \tilde x^i$ to a function $f$ by the chain rule, $\partial f / \partial \tilde x^i = (\partial f / \partial x^a)(\partial x^a / \partial \tilde x^i)$. For the dual statement, use $dx^a(\tilde\partial_i) = \partial x^a / \partial \tilde x^i$ on both sides.
   - *Why needed:* This is the fundamental change-of-basis formula for the tangent and cotangent frames.

2. **Substitution in the tensor.** Write $A = A^{a_1\cdots a_k}_{b_1\cdots b_\ell}\, \partial_{a_1}\otimes\cdots\otimes\partial_{a_k}\otimes dx^{b_1}\otimes\cdots\otimes dx^{b_\ell}$. Substitute $\partial_{a_j} = (\partial \tilde x^{i_j}/\partial x^{a_j})\, \tilde\partial_{i_j}$ (the *inverse* of step 1, used to express old basis in terms of new) and similarly for $dx^{b_j}$, and read off the new components.
   - *Hint:* Multilinearity moves the Jacobian factors past the tensor product symbols.
   - *Why needed:* This actually computes $\tilde A$ from $A$ and verifies it equals the prescribed rule.

3. **Cocycle condition for the converse.** For three charts $(x), (\tilde x), (\hat x)$, verify that applying the rule from $(x)$ to $(\tilde x)$ then from $(\tilde x)$ to $(\hat x)$ gives the same result as applying it directly from $(x)$ to $(\hat x)$.
   - *Hint:* This is the chain rule for Jacobians: $\partial \hat x^p / \partial x^a = (\partial \hat x^p / \partial \tilde x^i)(\partial \tilde x^i / \partial x^a)$. The Jacobian factors compose.
   - *Why needed:* This is what makes the converse work — given the rule on each pair of overlapping charts, the global tensor field exists because the rules are mutually consistent.

---

# Lemma Decomposition

> [!note]- Lemma 1: Chain rule for coordinate frames
> **Statement:** Given two overlapping charts $(x^a)$ and $(\tilde x^i)$, the coordinate vector fields and 1-forms satisfy
> $$\tilde\partial_i = \frac{\partial x^a}{\partial \tilde x^i}\, \partial_a, \qquad dx^a = \frac{\partial x^a}{\partial \tilde x^i}\, d\tilde x^i.$$
>
> **Hint:** Apply both sides as operators on a smooth function and use the chain rule for partial derivatives.
>
> **Why needed:** This is the elementary computation underlying the entire transformation rule; without it, the rule would have to be postulated rather than derived.
>
> > [!note]- Full proof
> > For the vector field statement: for any smooth $f$ on the chart overlap,
> > $$\tilde\partial_i f = \frac{\partial f}{\partial \tilde x^i} = \frac{\partial f}{\partial x^a}\frac{\partial x^a}{\partial \tilde x^i} = \frac{\partial x^a}{\partial \tilde x^i}\, \partial_a f,$$
> > by the chain rule. So $\tilde\partial_i = (\partial x^a/\partial \tilde x^i)\, \partial_a$ as derivations of smooth functions.
> >
> > For the 1-form statement: $dx^a$ is the 1-form whose pairing with any tangent vector $v$ is $dx^a(v) = v^a$ (its $a$-th component in the $(x)$ chart). Apply both sides of the asserted equality to $\tilde\partial_i$: the left gives $dx^a(\tilde\partial_i) = \partial x^a/\partial \tilde x^i$ (the chain-rule expression for the $a$-th $(x)$-component of $\tilde\partial_i$), the right gives $(\partial x^a/\partial \tilde x^j) d\tilde x^j(\tilde\partial_i) = (\partial x^a/\partial \tilde x^j)\,\delta^j_i = \partial x^a/\partial \tilde x^i$. Agreement on every $\tilde\partial_i$ gives the identity. $\blacksquare$

> [!note]- Lemma 2: Components transform by the rule
> **Statement:** A $(k, \ell)$-tensor field $A$ has components in two charts related by
> $$\tilde A^{i_1\cdots i_k}_{j_1\cdots j_\ell} = \frac{\partial \tilde x^{i_1}}{\partial x^{a_1}}\cdots\frac{\partial \tilde x^{i_k}}{\partial x^{a_k}}\,\frac{\partial x^{b_1}}{\partial \tilde x^{j_1}}\cdots\frac{\partial x^{b_\ell}}{\partial \tilde x^{j_\ell}}\, A^{a_1\cdots a_k}_{b_1\cdots b_\ell}.$$
>
> **Hint:** Write $A$ as a sum over the basis-induced basis using both charts' frames, set the two expressions equal, and use Lemma 1 to expand each frame element of one chart in terms of the other.
>
> **Why needed:** This is the theorem statement.
>
> > [!note]- Full proof
> > By definition of components,
> > $$\tilde A^{i_1\cdots i_k}_{j_1\cdots j_\ell} = A(d\tilde x^{i_1}, \dots, d\tilde x^{i_k}, \tilde\partial_{j_1}, \dots, \tilde\partial_{j_\ell}).$$
> > Apply Lemma 1: $\tilde\partial_{j_p} = (\partial x^{b_p}/\partial \tilde x^{j_p})\partial_{b_p}$ and $d\tilde x^{i_q} = (\partial \tilde x^{i_q}/\partial x^{a_q})dx^{a_q}$ (inverse of Lemma 1's covector identity). Substituting,
> > $$\tilde A^{i_1\cdots i_k}_{j_1\cdots j_\ell} = A\bigg(\frac{\partial \tilde x^{i_1}}{\partial x^{a_1}}dx^{a_1}, \dots, \frac{\partial \tilde x^{i_k}}{\partial x^{a_k}}dx^{a_k}, \frac{\partial x^{b_1}}{\partial \tilde x^{j_1}}\partial_{b_1}, \dots, \frac{\partial x^{b_\ell}}{\partial \tilde x^{j_\ell}}\partial_{b_\ell}\bigg).$$
> > By multilinearity of $A_p$, the Jacobian factors come out:
> > $$\tilde A^{i_1\cdots i_k}_{j_1\cdots j_\ell} = \frac{\partial \tilde x^{i_1}}{\partial x^{a_1}}\cdots\frac{\partial \tilde x^{i_k}}{\partial x^{a_k}}\,\frac{\partial x^{b_1}}{\partial \tilde x^{j_1}}\cdots\frac{\partial x^{b_\ell}}{\partial \tilde x^{j_\ell}}\, A(dx^{a_1}, \dots, dx^{a_k}, \partial_{b_1}, \dots, \partial_{b_\ell}),$$
> > and the last factor is $A^{a_1\cdots a_k}_{b_1\cdots b_\ell}$ by definition. $\blacksquare$

> [!note]- Lemma 3: Cocycle condition for the converse
> **Statement:** If components $A^{i_1\cdots i_k}_{j_1\cdots j_\ell}$ defined chart-by-chart transform by the rule on every chart overlap, then there is a unique smooth tensor field having these as its components.
>
> **Hint:** Define $A_p$ on each chart by the basis-induced sum. Show that on chart overlaps, the resulting fibrewise tensors agree, using the transformation rule and the fact that the basis-induced sums differ by Jacobian factors that exactly cancel.
>
> **Why needed:** This is the converse direction — verifying that the rule is *sufficient* to define a tensor field.
>
> > [!note]- Full proof
> > On each chart $(U_\alpha, x_\alpha)$, define $A_\alpha := A^{\cdots}_{\cdots}(x_\alpha)\, \partial_{i_1}^\alpha\otimes\cdots$ — the sum-of-tensor-products with the chart's components.
> >
> > To check that $A_\alpha = A_\beta$ on $U_\alpha \cap U_\beta$ as fibrewise tensors: use Lemma 1 to expand each $\partial^\beta_i$ in terms of $\partial^\alpha_a$, and substitute. The components of $A_\beta$ in the $(x_\alpha)$ basis become $\tilde A^{\cdots}_{\cdots} (\partial x_\alpha/\partial x_\beta) \cdots$ factors, which by hypothesis equal $A_\alpha$'s components. So $A_\alpha = A_\beta$ on the overlap.
> >
> > The chart-by-chart definitions therefore glue to a unique global tensor field. Smoothness is automatic from the smoothness of the components on each chart. The cocycle condition on triple overlaps is automatic from the chain rule for Jacobians: $\partial x_\gamma/\partial x_\alpha = (\partial x_\gamma/\partial x_\beta)(\partial x_\beta/\partial x_\alpha)$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Components of a $(k, \ell)$-tensor field transform by the rule
> $$\tilde A^{i_1\cdots i_k}_{j_1\cdots j_\ell} = \frac{\partial \tilde x^{i_1}}{\partial x^{a_1}}\cdots\frac{\partial \tilde x^{i_k}}{\partial x^{a_k}}\,\frac{\partial x^{b_1}}{\partial \tilde x^{j_1}}\cdots\frac{\partial x^{b_\ell}}{\partial \tilde x^{j_\ell}}\, A^{a_1\cdots a_k}_{b_1\cdots b_\ell}.$$
>
> *Proof of the rule (Lemmas 1 + 2).* Lemma 1 establishes the chain-rule for frames: $\tilde\partial_i = (\partial x^a/\partial \tilde x^i)\partial_a$ and $d\tilde x^i = (\partial \tilde x^i / \partial x^a)dx^a$ (and their inverses).
>
> Lemma 2 substitutes these into the definition $\tilde A^{i_1\cdots i_k}_{j_1\cdots j_\ell} = A(d\tilde x^{i_1}, \dots, d\tilde x^{i_k}, \tilde\partial_{j_1}, \dots, \tilde\partial_{j_\ell})$ and uses the multilinearity of $A_p$ to extract the Jacobian factors:
> $$\tilde A^{i_1\cdots i_k}_{j_1\cdots j_\ell} = \frac{\partial \tilde x^{i_1}}{\partial x^{a_1}}\cdots\frac{\partial \tilde x^{i_k}}{\partial x^{a_k}}\,\frac{\partial x^{b_1}}{\partial \tilde x^{j_1}}\cdots\frac{\partial x^{b_\ell}}{\partial \tilde x^{j_\ell}}\, A^{a_1\cdots a_k}_{b_1\cdots b_\ell}.$$
>
> *Proof of the converse (Lemma 3).* Given functions on each chart satisfying the rule on overlaps, define a fibrewise tensor on each chart by the basis-induced expansion. Lemma 3 verifies these agree on overlaps via the rule. The cocycle condition on triple overlaps comes from the Jacobian chain rule, so the chart-by-chart definitions glue to a unique smooth global tensor field. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**General relativity: the metric in different coordinate systems.** The metric of Schwarzschild spacetime is famously simple in Schwarzschild coordinates $(t, r, \theta, \phi)$: $g = -(1 - 2GM/r)\, dt \otimes dt + (1 - 2GM/r)^{-1}\, dr \otimes dr + r^2(d\theta^2 + \sin^2\theta\, d\phi^2)$. In Kruskal coordinates $(U, V, \theta, \phi)$, it is $g = (32 G^3 M^3 / r)\, e^{-r/2GM}(-dV \otimes dU - dU \otimes dV) + r^2(\dots)$. The two expressions are related by the transformation rule: the Jacobian of the Schwarzschild-to-Kruskal map enters quadratically (two covariant Jacobian factors for the symmetric 2-tensor), and the transformation makes manifest the structure across the event horizon.

**Number theory / arithmetic geometry: tensors over schemes.** The transformation rule generalizes to schemes: a tensor on a scheme is a collection of sheaf sections that transforms by the rule under change of local frame. The classical chart-by-chart formulation of a vector bundle (transition functions) is exactly the transformation rule for $(1, 0)$-tensors (sections of $TM$) in algebraic-geometric language.

**Numerical relativity: the BSSN formulation.** The Baumgarte-Shapiro-Shibata-Nakamura formulation of the Einstein equations re-formulates them in terms of variables that have well-behaved transformation laws under coordinate change (specifically, the conformal metric and its trace-free part). The transformation rule for tensors is the basic tool for checking that the BSSN variables are tensorial.

**Fluid dynamics in arbitrary coordinates.** The Navier-Stokes equations on a curved space are intrinsically tensorial: the velocity field is a $(1, 0)$-tensor, the stress is a $(0, 2)$-tensor, the rate of strain is a $(0, 2)$-tensor. Re-deriving them in non-Cartesian coordinates (cylindrical, spherical, orthogonal) is *literally* applying the transformation rule, and the coordinate-corrections that appear (e.g., the centrifugal and Coriolis terms in rotating frames) are the Christoffel-symbol-like terms from the *non-tensorial* part of the connection.

---

# Bridges

- **Lee's tensor characterization lemma.** [[Thm - Tensor Field is C-Infinity Multilinear over C-Infinity Functions|The tensor characterization lemma]] gives a coordinate-free criterion for being a tensor field. The transformation rule is the coordinate-level statement of the same fact: a multilinear functional whose components transform by the rule is precisely a $C^\infty(M)$-multilinear gadget on vector fields and 1-forms. The two perspectives certify the same class of objects.

- **The Christoffel symbols of a connection.** Christoffel symbols transform by the tensor rule plus an extra second-derivative term. The anomaly term identifies $\Gamma$ as a non-tensor; the difference of two Christoffel symbols *is* a tensor (the anomaly cancels), and is called the *difference of connections* or *contorsion*. So the transformation rule is the diagnostic for "tensor versus connection".

- **Tensor densities.** A density of weight $w$ has an additional absolute-determinant factor in its component law. The Riemannian density is locally $\sqrt{|\det(g_{ij})|}\,|dx^1\cdots dx^n|$; unlike the Riemannian volume form, it is defined without an orientation. Keeping forms and densities distinct prevents determinant factors from being assigned to ordinary tensors.

- **Pullback as a chart change.** The transformation rule is the special case of [[Def - Pullback of a Covariant Tensor Field|pullback]] where the smooth map is a chart transition $\tilde x \circ x^{-1}$. In other words, "changing coordinates" *is* "pulling back along the chart change". This connects the rule to the general theory of pullback, and shows that the rule's universality is a special case of the functoriality of pullback.

---

# Unlocked by This

> [!tip] Tensors vs. Connections vs. Densities — A Taxonomy by Transformation Behaviour *(from Tensor Analysis)*
> The transformation rule classifies geometric quantities by how they transform under change of coordinates. **Tensors** transform by the rule alone. **Connections** transform by the rule plus a second-derivative anomaly. **Densities** transform by the rule plus a Jacobian-determinant factor. **Pseudo-tensors** transform by the rule plus a sign of the Jacobian determinant. These four categories cover essentially all geometric objects in classical differential geometry, and the rule is the diagnostic for each.

> [!tip] The Levi-Civita Symbol $\epsilon_{ijk}$ as a Pseudo-Tensor *(from Tensor Analysis / Index Gymnastics)*
> The Levi-Civita symbol $\epsilon_{ijk}$ defined by $\epsilon_{123} = 1$ and antisymmetric — is *not* a tensor: under a change of coordinates with Jacobian $J$, $\tilde\epsilon_{ijk} = (\det J) \cdot \epsilon_{ijk}$ rather than $\epsilon_{ijk}$ (without the determinant). So $\epsilon$ is a pseudo-tensor of weight 1. To make a true covariant tensor, combine it with the metric determinant: the resulting components $\varepsilon_{ijk} = \sqrt{|\det g|}\,\epsilon_{ijk}$ define the Riemannian volume form — the Riemannian volume form's components.

> [!tip] Why Physicists Define Tensors by the Rule *(History of Physics)*
> Before the mathematical formulation of manifolds (mid-20th century), physicists *defined* a tensor as "a collection of components on each coordinate system that transforms by the rule under coordinate change". This definition predates the bundle formulation by decades and is still standard in physics curricula. The two definitions are equivalent on smooth manifolds, but the rule-based one is operationally simpler for calculations and remains the working definition in general relativity and continuum mechanics.
