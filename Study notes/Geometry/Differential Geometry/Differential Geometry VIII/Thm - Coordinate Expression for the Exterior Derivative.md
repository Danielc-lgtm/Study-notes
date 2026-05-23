---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Differential k-Form on a Manifold"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold. $(U, x^i)$ is a smooth chart. $\Omega^k(M)$ is the space of smooth $k$-forms. $d : \Omega^k \to \Omega^{k+1}$ is the exterior derivative. $\partial_j = \partial/\partial x^j$ are the coordinate vector fields. $dx^I = dx^{i_1} \wedge \cdots \wedge dx^{i_k}$ for an increasing multi-index $I$. $\sum'_I$ is the primed sum over increasing multi-indices. The Lie bracket of vector fields is $[X, Y]$. The full registry is on [[Differential Geometry VIII — Differential Forms]].

---

# Statement

> **Theorem (Coordinate Expression for $d$).** Let $M$ be a smooth manifold with a smooth chart $(U, x^i)$. For any smooth $k$-form $\omega = \sum'_I \omega_I\,dx^I$ on $U$ (with $\omega_I \in C^\infty(U)$ and $I$ increasing of length $k$),
> $$d\omega = \sum'_I d\omega_I \wedge dx^I = \sum'_I \sum_{j=1}^n \frac{\partial \omega_I}{\partial x^j}\,dx^j \wedge dx^I.$$
> In particular, on a $0$-form $f$ this reduces to $df = \sum_j(\partial f/\partial x^j)\,dx^j$, the ordinary differential.

> **Theorem (Invariant Formula, Lee Proposition 14.29 for $1$-forms; Lee Proposition 14.32 for general $k$-forms).** For a smooth $1$-form $\omega \in \Omega^1(M)$ and smooth vector fields $X, Y$ on $M$,
> $$d\omega(X, Y) = X\omega(Y) - Y\omega(X) - \omega([X, Y]).$$
> More generally, for a $k$-form $\omega$ and smooth vector fields $X_0, X_1, \dots, X_k$,
> $$d\omega(X_0, \dots, X_k) = \sum_{i=0}^k (-1)^i X_i\,\omega(X_0, \dots, \widehat{X_i}, \dots, X_k) + \sum_{0 \le i < j \le k}(-1)^{i+j}\omega([X_i, X_j], X_0, \dots, \widehat{X_i}, \dots, \widehat{X_j}, \dots, X_k),$$
> where hats indicate omitted arguments.

> **Corollary (chart-independence of the coordinate formula).** The coordinate formula $d\omega = \sum'_I d\omega_I \wedge dx^I$ produces the same form $d\omega$ regardless of which chart it is computed in. This is the well-definedness of $d$ as a global operator and follows from the uniqueness theorem [[Thm - Uniqueness of the Exterior Derivative]].

---

# Motivation

The theorem gives two different formulas for the exterior derivative — the **coordinate formula** (which makes computation easy in any specific chart) and the **invariant formula** (which manifestly involves no chart at all). Both are useful, and each has a different purpose.

The coordinate formula is what you actually use in calculations. To compute $d\omega$ for a specific $\omega$, expand $\omega$ in coordinates, differentiate each coefficient function, and wedge on the new $dx^j$. The bookkeeping is mechanical. Most of the time, this is how $d$ is computed.

The invariant formula is what you use to prove theorems about $d$ in a chart-independent way. The most important use is to verify identities like $F^* d = d F^*$ without computing in coordinates — both sides of the identity can be checked against the invariant formula, term by term.

The two formulas agree because $d$ is uniquely characterized by its algebraic properties (linearity, $df = $ ordinary differential, graded Leibniz, $d^2 = 0$), and both formulas satisfy these properties. So they must give the same operator.

The deeper reason the invariant formula exists is that the right-hand side is *manifestly* multilinear over $C^\infty(M)$ and alternating in the vector field arguments, hence (by the tensor characterization lemma) defines a smooth $(k+1)$-form. The fact that this form equals $d\omega$ — defined coordinate-by-coordinate — is the content of the theorem. The invariant formula thus provides a *chart-free definition* of $d$, and one can prove existence and uniqueness of $d$ using this formula as the starting point, then verify the coordinate formula as a consequence.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is bare: "a smooth form $\omega$" in either a chart or globally. The skill is recognizing which formula to use in which context.

The first disguised source is **a computation in a specific chart**. When the problem involves concrete coordinates and a concrete form (e.g., $\omega = e^{xy}(x\,dx + y\,dy)$ on $\mathbb{R}^2$), the coordinate formula is the only sensible tool. Use it mechanically.

The second disguised source is **a question about an abstract vector field on an abstract manifold**. When the problem mentions vector fields $X, Y$ without explicit coordinates, use the invariant formula. For instance, in proofs about Lie groups, the invariant formula evaluated on left-invariant vector fields gives the Maurer–Cartan structure equations.

The third disguised source is **a Frobenius integrability question**. The Frobenius theorem in forms language uses the invariant formula to translate the integrability condition of a distribution into a closedness condition on the annihilator ideal. Specifically, a distribution is involutive if and only if every $1$-form annihilating it satisfies $d\omega \equiv 0$ modulo the ideal — and the invariant formula is what makes this translation work. See [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]].

The fourth disguised source is **a question about the Lie bracket**. The invariant formula on a $1$-form, $d\omega(X, Y) = X\omega(Y) - Y\omega(X) - \omega([X, Y])$, lets you read off $\omega([X, Y])$ from $d\omega$ and the action of $X, Y$ on $\omega$. This is the content of Lee Proposition 14.30: knowing the Lie brackets of basis vector fields in a frame is equivalent to knowing the exterior derivatives of the dual coframe $1$-forms.

**Targets (Output Amplification)**

The conclusion is two formulas. Combined with other facts:

The first target combination is **coordinate formula + uniqueness theorem = well-definedness of $d$**. The coordinate formula in two charts on the overlap gives the same form, because both expressions satisfy the four axioms of $d$ on the overlap (linearity, agreement with differential on functions, graded Leibniz, $d^2 = 0$), and uniqueness then forces them to agree.

The second target combination is **invariant formula + Lie bracket identities = Maurer–Cartan structure equations on a Lie group**. On a Lie group with left-invariant vector fields $E_i$ and dual coframe $\theta^i$, the Lie brackets $[E_i, E_j] = c^k_{ij} E_k$ define the structure constants. The invariant formula then gives $d\theta^k = -\frac12 c^k_{ij}\theta^i \wedge \theta^j$ — the **Maurer–Cartan equations**, the structural identity of a Lie group. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

The third target combination is **coordinate formula + naturality = chart-independence of $d$**. The fact that the coordinate formula in different charts gives the same $d\omega$ is exactly the chart-independence (naturality) of $d$. The proof is via the uniqueness theorem applied chart-by-chart.

The fourth target combination is **invariant formula + Frobenius = the forms-language Frobenius theorem**. A distribution $\mathcal{D}$ is integrable if and only if its annihilator ideal $\mathcal{I}(\mathcal{D}) = \{\omega : \omega|_\mathcal{D} = 0\}$ is a differential ideal, i.e., $d\omega \in \mathcal{I}(\mathcal{D})$ for every $\omega \in \mathcal{I}(\mathcal{D})$. The invariant formula is what bridges the vector-field condition $[\mathcal{D}, \mathcal{D}] \subseteq \mathcal{D}$ to the form condition.

---

# Why Is It True

**The one-liner mechanism:** **the coordinate formula is forced by linearity, graded Leibniz, and the definition $df = $ ordinary differential; the invariant formula is then a consequence of multilinearity over $C^\infty(M)$ and the tensor characterization lemma, combined with verification on a coordinate frame.**

**Coordinate formula.** Take $\omega = \sum'_I \omega_I\,dx^I$ in a chart. By linearity, $d\omega = \sum'_I d(\omega_I\,dx^I)$. By graded Leibniz with $\omega_I$ a $0$-form,
$$d(\omega_I \cdot dx^I) = (d\omega_I) \cdot dx^I + \omega_I \cdot d(dx^I) = (d\omega_I) \wedge dx^I + \omega_I \cdot 0 = d\omega_I \wedge dx^I,$$
using that $d(dx^I) = 0$ for a constant-coefficient basic form (every basic $1$-form $dx^{i_j}$ has differential $0$, since $\partial_k(x^{i_j}) = \delta^{i_j}_k$ is constant, and the wedge of $1$-forms with zero differential has zero differential by graded Leibniz). So
$$d\omega = \sum'_I d\omega_I \wedge dx^I = \sum'_I \sum_j (\partial_j \omega_I)\,dx^j \wedge dx^I.$$

**Invariant formula on $1$-forms.** Take $\omega = u\,dv$ for smooth functions $u, v$ (every $1$-form is locally a sum of such terms). Compute both sides of the invariant formula and verify they agree.

Left side: $d\omega = d(u\,dv) = du \wedge dv$, by graded Leibniz with $d(dv) = 0$. Then $d\omega(X, Y) = (du \wedge dv)(X, Y) = du(X) dv(Y) - dv(X) du(Y) = (Xu)(Yv) - (Xv)(Yu)$, using the determinant identity for wedges.

Right side: $X\omega(Y) - Y\omega(X) - \omega([X, Y]) = X(u \cdot Yv) - Y(u \cdot Xv) - u \cdot [X, Y]v$. Expand using the Leibniz rule:
- $X(u \cdot Yv) = (Xu)(Yv) + u(X(Yv))$,
- $Y(u \cdot Xv) = (Yu)(Xv) + u(Y(Xv))$,
- $\omega([X, Y]) = u \cdot [X, Y]v = u(XYv - YXv)$.

So the right side is $(Xu)(Yv) + u(XYv) - (Yu)(Xv) - u(YXv) - u(XYv - YXv) = (Xu)(Yv) - (Yu)(Xv)$.

Both sides equal $(Xu)(Yv) - (Xv)(Yu)$ — note that swapping $u, v$ in the formal computation changes the answer by exactly the right amount to make this work out.

So the invariant formula holds on $u\,dv$, hence by linearity on all $1$-forms.

**Invariant formula on higher-degree forms.** By induction on degree, using the graded Leibniz rule for $d$ and careful sign tracking. Lee's proof (Proposition 14.32) reduces to a coordinate computation in a chart with vanishing Lie brackets ($[\partial_i, \partial_j] = 0$), where the formula simplifies dramatically, then propagates by tensor multilinearity to all vector field inputs. The detailed proof is bookkeeping-heavy but mechanical.

**Why the two formulas agree.** Both define $\mathbb{R}$-linear operators $\Omega^k(M) \to \Omega^{k+1}(M)$ satisfying linearity, $df = $ ordinary differential on functions, graded Leibniz, and $d^2 = 0$. By [[Thm - Uniqueness of the Exterior Derivative]], any such operator equals $d$. So both formulas compute the same form.

---

# What Makes This Hard

The coordinate formula is mechanical and easy to apply but bookkeeping-prone — the signs from $dx^j \wedge dx^I$ when $j$ is not larger than $i_1$ require care to put back into increasing-multi-index form. Beginners often forget the sign-flips when reordering.

The invariant formula on higher-degree forms is hard to remember (the precise pattern of signs $(-1)^i$ and $(-1)^{i+j}$ in the two sums) and hard to apply directly. In practice it is rarely used for computation; its role is to provide a chart-free definition.

The conceptual difficulty is recognizing that the two formulas compute the same operator. Students sometimes think the invariant formula is a special case of the coordinate formula, or vice versa; they are actually two different proofs of the same theorem (that $d$ exists and has these properties), with the equivalence underwritten by the uniqueness theorem.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For the coordinate formula, reduce to basic forms via linearity, then apply graded Leibniz plus the observation that constant-coefficient basic forms have zero $d$. For the invariant formula on $1$-forms, take $\omega = u\,dv$, expand both sides, and use the Leibniz rule and the definition of the Lie bracket.

**Subgoal decomposition:**

1. **Verify $d(dx^I) = 0$ for a constant-coefficient basic form.**
   - *Hint:* $dx^I = 1 \cdot dx^{i_1} \wedge \cdots \wedge dx^{i_k}$; apply graded Leibniz; each $d(dx^{i_j}) = d^2(x^{i_j}) = 0$.
   - *Why needed:* Inductive base for the propagation of the formula.

2. **Use graded Leibniz to reduce $d(\omega_I\,dx^I)$ to $d\omega_I \wedge dx^I$.**
   - *Hint:* $d(\omega_I \wedge dx^I) = d\omega_I \wedge dx^I + (-1)^0 \omega_I \wedge d(dx^I) = d\omega_I \wedge dx^I$.
   - *Why needed:* Coordinate formula on basic forms.

3. **Propagate to general forms by linearity.**
   - *Hint:* Every form is a finite sum of basic forms; both $d$ and the formula are linear.
   - *Why needed:* Finishes the coordinate formula.

4. **For the invariant formula on a $1$-form, take $\omega = u\,dv$, compute both sides.**
   - *Hint:* Left side: $d(u\,dv) = du \wedge dv$, then evaluate on $(X, Y)$ using the determinant identity. Right side: expand $X\omega(Y) - Y\omega(X) - \omega([X, Y])$ using Leibniz and the bracket.
   - *Why needed:* Establishes the invariant formula on a generating set; linearity propagates.

5. **For higher-degree, induct on degree using graded Leibniz.**
   - *Hint:* Write a general form as a sum of wedges of $1$-forms, and use the inductive hypothesis on each factor.
   - *Why needed:* Generalizes the formula to all degrees.

---

# Lemma Decomposition

> [!note]- Lemma 1: $d$ of a constant-coefficient basic form is zero
> **Statement:** For any increasing multi-index $I = (i_1, \dots, i_k)$ on $M$, $d(dx^I) = 0$ in any chart.
>
> **Hint:** $dx^I = 1 \cdot dx^{i_1} \wedge \cdots \wedge dx^{i_k}$; the constant function $1$ has zero differential.
>
> **Why needed:** Base case for the coordinate formula on basic forms.
>
> > [!note]- Full proof
> > Apply graded Leibniz iteratively. $d(dx^{i_j}) = d(d(x^{i_j})) = 0$ by $d^2 = 0$ (or by the coordinate formula on the function $x^{i_j}$, whose differential is $dx^{i_j}$). The wedge of $1$-forms with zero differentials has zero differential.

> [!note]- Lemma 2: Coordinate formula on a basic form
> **Statement:** For a smooth function $\omega_I$ and an increasing multi-index $I$, $d(\omega_I\,dx^I) = d\omega_I \wedge dx^I$.
>
> **Hint:** Graded Leibniz with $\omega_I$ a $0$-form: $d(\omega_I \cdot dx^I) = d\omega_I \wedge dx^I + \omega_I \cdot d(dx^I) = d\omega_I \wedge dx^I + 0$.
>
> **Why needed:** Coordinate formula on each basic term; linearity propagates to all forms.
>
> > [!note]- Full proof
> > $d(\omega_I \wedge dx^I) = d\omega_I \wedge dx^I + (-1)^0 \omega_I \wedge d(dx^I) = d\omega_I \wedge dx^I + \omega_I \wedge 0 = d\omega_I \wedge dx^I$ by Lemma 1 and graded Leibniz with $\deg(\omega_I) = 0$.

> [!note]- Lemma 3: Invariant formula on $\omega = u\,dv$ for smooth functions $u, v$
> **Statement:** For smooth functions $u, v$ on $M$ and smooth vector fields $X, Y$,
> $$d(u\,dv)(X, Y) = X(u \cdot dv(Y)) - Y(u \cdot dv(X)) - u\,dv([X, Y]).$$
> Equivalently, $d(u\,dv)(X, Y) = X\omega(Y) - Y\omega(X) - \omega([X, Y])$ for $\omega = u\,dv$.
>
> **Hint:** Expand both sides. Left side via the determinant identity for $du \wedge dv$; right side via the Leibniz rule for $X, Y$ on the product $u \cdot Yv$.
>
> **Why needed:** Base case for the invariant formula on $1$-forms; linearity propagates.
>
> > [!note]- Full proof
> > **Left side:** $d(u\,dv) = du \wedge dv$ by Lemma 2 (with $\omega_I = u$ and $dx^I = dv$, treating $v$ as a coordinate function-like object — in a coordinate-free way, $d(u \cdot dv) = du \wedge dv + u \cdot d(dv) = du \wedge dv$ since $d^2 v = 0$). Then $(du \wedge dv)(X, Y) = du(X)dv(Y) - du(Y)dv(X) = (Xu)(Yv) - (Yu)(Xv)$ by the determinant identity.
> >
> > **Right side:** $X\omega(Y) = X(u \cdot Yv) = (Xu)(Yv) + u \cdot X(Yv)$ by the Leibniz rule for vector fields on products. Similarly $Y\omega(X) = (Yu)(Xv) + u \cdot Y(Xv)$. Then $\omega([X, Y]) = u \cdot [X, Y]v = u(XYv - YXv) = u \cdot XYv - u \cdot YXv$.
> >
> > Combining: $X\omega(Y) - Y\omega(X) - \omega([X, Y]) = [(Xu)(Yv) + u \cdot XYv] - [(Yu)(Xv) + u \cdot YXv] - [u \cdot XYv - u \cdot YXv] = (Xu)(Yv) - (Yu)(Xv)$. The $u \cdot XYv$ terms cancel and the $u \cdot YXv$ terms cancel.
> >
> > Both sides equal $(Xu)(Yv) - (Yu)(Xv)$. The lemma is proved.

> [!note]- Lemma 4: Higher-degree invariant formula
> **Statement:** For $\omega \in \Omega^k(M)$ and vector fields $X_0, \dots, X_k$, the invariant formula of the theorem statement holds.
>
> **Hint:** Show the right side is $C^\infty(M)$-multilinear and alternating in the $X_i$, hence defines a smooth $(k+1)$-form. Verify it equals $d\omega$ by comparing on a coordinate frame (where Lie brackets vanish).
>
> **Why needed:** Generalizes the invariant formula to all degrees.
>
> > [!note]- Full proof
> > See Lee Proposition 14.32 for the detailed proof. The key step is showing $C^\infty(M)$-multilinearity (which fails naively because of the $X_i\,\omega(\cdots)$ terms — derivatives of multilinear scalars — but works out when the $\omega([X_i, X_j], \dots)$ terms are added, with the Lie-bracket Leibniz rule canceling the extra derivatives). Once $C^\infty(M)$-multilinearity and alternation are established, both sides are smooth $(k+1)$-forms; they agree on a coordinate frame (where Lie brackets vanish and only the first sum survives, matching $d\omega(\partial_{i_0}, \dots, \partial_{i_k}) = \sum_p (-1)^p \partial_{i_p}\omega(\partial_{i_0}, \dots, \widehat{\partial_{i_p}}, \dots, \partial_{i_k})$ via the coordinate formula and a determinant expansion).

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem (coordinate formula).** $d\omega = \sum'_I d\omega_I \wedge dx^I$ for $\omega = \sum'_I \omega_I\,dx^I$ in a chart.
>
> *Proof.* By linearity of $d$ and the assumption on $\omega$, it suffices to verify the formula on a single basic term $\omega = \omega_I\,dx^I$.
>
> By Lemma 2, $d(\omega_I\,dx^I) = d\omega_I \wedge dx^I$. Linearity propagates to general forms.
>
> The chart-independence (Corollary) follows from the uniqueness theorem [[Thm - Uniqueness of the Exterior Derivative]]: any operator on $\Omega^\bullet$ satisfying the four axioms equals $d$, and the coordinate formula satisfies all four axioms (linearity by definition, agreement with differential on functions because $d(f) = \sum_j(\partial_j f)\,dx^j$, graded Leibniz by direct computation, and $d^2 = 0$ by Schwarz's theorem on mixed partials). So the coordinate formula in chart $A$ and the coordinate formula in chart $B$ both compute $d$ on the overlap, hence agree.
>
> **Theorem (invariant formula on $1$-forms).** $d\omega(X, Y) = X\omega(Y) - Y\omega(X) - \omega([X, Y])$.
>
> *Proof.* By linearity in $\omega$, it suffices to verify on $\omega = u\,dv$ for smooth functions $u, v$ — every $1$-form is locally a sum of such terms.
>
> By Lemma 3, both sides equal $(Xu)(Yv) - (Yu)(Xv)$. Linearity propagates.
>
> **Theorem (invariant formula on higher-degree forms).** The general invariant formula holds by Lemma 4.
>
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Maurer–Cartan equations on a Lie [[Def - Group|group]].** Let $G$ be a Lie group with left-invariant vector fields $E_i$ and dual coframe $\theta^i$. The Lie brackets $[E_i, E_j] = c^k_{ij} E_k$ define the structure constants. Applying the invariant formula to $d\theta^k(E_i, E_j) = E_i\theta^k(E_j) - E_j\theta^k(E_i) - \theta^k([E_i, E_j]) = E_i\delta^k_j - E_j\delta^k_i - \theta^k(c^l_{ij}E_l) = 0 - 0 - c^k_{ij}$ (using $E_i\delta^k_j = 0$ since $\delta^k_j$ is constant). So $d\theta^k(E_i, E_j) = -c^k_{ij}$, equivalently $d\theta^k = -\tfrac12 c^k_{ij}\theta^i \wedge \theta^j$. The whole structure of the Lie algebra is encoded in the exterior derivatives of the dual coframe.

**Frobenius theorem in forms language.** A distribution $\mathcal{D}$ of rank $k$ on $M$ is involutive if and only if its [[Def - Annihilator|annihilator]] [[Def - Ideal|ideal]] $\mathcal{I}(\mathcal{D}) = \{\omega \in \Omega^\bullet(M) : \omega|_\mathcal{D} = 0\}$ is closed under $d$. The invariant formula on a $1$-form $\omega \in \mathcal{I}(\mathcal{D})$ shows that $d\omega(X, Y) = X\omega(Y) - Y\omega(X) - \omega([X, Y])$ for $X, Y \in \mathcal{D}$. The first two terms vanish because $\omega(X) = \omega(Y) = 0$ (since $\omega$ annihilates $\mathcal{D}$). So $d\omega(X, Y) = -\omega([X, Y])$, which is zero exactly when $[X, Y] \in \mathcal{D}$ — i.e., when $\mathcal{D}$ is involutive. See [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]].

**Curvature of a connection in gauge theory.** For a connection $1$-form $A$ with values in a Lie algebra $\mathfrak{g}$, the curvature $F_A = dA + \tfrac12[A, A]$ involves a combination of $d$ and the Lie bracket (the second term is the wedge product of $\mathfrak{g}$-valued $1$-forms, with the bracket combining the values). The invariant formula gives $F_A(X, Y) = X(A(Y)) - Y(A(X)) - A([X, Y]) + [A(X), A(Y)]$, exhibiting the curvature as the "failure" of $A$ to be the exterior derivative of a function in the Lie-algebra-valued sense.

**Holonomic constraints in mechanics.** A constraint $1$-form $\omega$ on configuration space is **holonomic** if locally $\omega = df$ for some function $f$ (whose level sets are the constraint surfaces). The Frobenius integrability criterion in this language is $d\omega = 0$ for a single $1$-form, equivalently $\omega \wedge d\omega = 0$ when the $1$-form has nonzero kernel direction. The invariant formula on $d\omega(X, Y)$ converts this into a Lie-bracket condition on vector fields tangent to the constraint.

---

# Bridges

- **[[Thm - Uniqueness of the Exterior Derivative]]** — The coordinate formula and the invariant formula both define operators satisfying the four axioms of $d$, hence both equal $d$ by uniqueness. The uniqueness theorem is what allows one to switch freely between the two formulas.

- **[[Def - The Lie Bracket of Vector Fields]]** — The invariant formula on $1$-forms involves the Lie bracket as the third term: $d\omega(X, Y) = X\omega(Y) - Y\omega(X) - \omega([X, Y])$. The bracket measures the failure of $\omega$ to be exact in a chart-independent way. The bridge to the dynamic side of differential geometry (vector fields, flows, Lie brackets) runs through this formula.

- **Maurer–Cartan structure equation** — On a Lie group, the dual coframe $\theta^i$ of left-invariant vector fields satisfies $d\theta^k = -\tfrac12 c^k_{ij}\theta^i \wedge \theta^j$, with the structure constants $c^k_{ij}$ of the Lie algebra. The invariant formula plus the left-invariant Lie bracket give this directly. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

- **Frobenius theorem** — The involutivity of a distribution is equivalent to the closedness of the annihilator ideal under $d$. The invariant formula is the bridge: it translates the vector-field condition $[X, Y] \in \mathcal{D}$ into the form condition $d\omega \in \mathcal{I}(\mathcal{D})$.

- **[[Thm - Pullback Commutes with d for Forms on Manifolds]]** — Naturality of $d$ is verified using the coordinate formula or the invariant formula on each side, both producing the same answer. The cleaner proof uses uniqueness.

---

# Unlocked by This

> [!tip] Maurer–Cartan Form on a Lie Group *(from Differential Geometry XI)*
> The dual coframe of left-invariant vector fields on a Lie group $G$ satisfies the **Maurer–Cartan equation** $d\theta + \tfrac12[\theta, \theta] = 0$, where $\theta$ is the Maurer–Cartan $\mathfrak{g}$-valued $1$-form. The invariant formula for $d$ plus the structure constants is what makes this an honest equation.

> [!tip] Frobenius Theorem in Forms Language *(from DG X)*
> A distribution $\mathcal{D}$ is integrable if and only if its annihilator ideal is closed under $d$. The invariant formula is the bridge between the vector-field version (involutivity: $[X, Y] \in \mathcal{D}$) and the form version (differential ideal: $d\omega \in \mathcal{I}(\mathcal{D})$).

> [!tip] Cartan Structure Equations *(from Gauge Theory)*
> The curvature $F = dA + \tfrac12[A, A]$ of a connection $A$ uses the invariant formula's combination of $d$ and Lie bracket. The Bianchi identity $dF + [A, F] = 0$ is derived using this formula plus $d^2 = 0$.

> [!tip] Coordinate-Free Stokes' Theorem *(from DG IX)*
> Stokes' theorem $\int_M d\omega = \int_{\partial M}\omega$ is naturally phrased in coordinate-free language. The invariant formula for $d$ is what makes this well-defined without reference to any chart.

> [!tip] Spectral Sequences in Fibre Bundles *(from Algebraic Topology)*
> The invariant formula's higher-degree version is the input to the de Rham spectral sequence of a fibre bundle, where it encodes the differential of the $E_2$ page in terms of bundle data (transition functions and connection).
