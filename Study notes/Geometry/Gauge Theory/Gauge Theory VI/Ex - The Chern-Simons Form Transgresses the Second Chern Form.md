---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Transgression Formula and the Chern-Simons Form"
  - "Def - Chern-Simons Functional"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
  - "Thm - Wedge Product Properties"
  - "Def - Trace"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $G$ be a matrix Lie group with Lie algebra $\mathfrak{g}\subseteq\mathfrak{gl}_n(\mathbb C)$ (for the application $G=SU(2)$, $\mathfrak{g}=\mathfrak{su}(2)$), let $X$ be a smooth manifold, and let $A\in\Omega^1(X;\mathfrak g)$ be a $\mathfrak g$-valued one-form — in gauge theory the gauge potential of a connection in a fixed trivialisation. Write $F_A:=dA+A\wedge A\in\Omega^2(X;\mathfrak g)$ for the associated curvature two-form, and define the **Chern–Simons three-form**
$$\operatorname{cs}(A):=\operatorname{tr}\!\Big(A\wedge dA+\tfrac23\,A\wedge A\wedge A\Big)\in\Omega^3(X).$$
Prove Haydys's identity $(97)$ by direct expansion:
$$d\operatorname{cs}(A)=\operatorname{tr}(F_A\wedge F_A).$$
In the course of the computation, establish and use explicitly the vanishing $\operatorname{tr}(A\wedge A\wedge A\wedge A)=0$, which follows from the graded cyclicity of the trace with the sign incurred when a one-form is moved past three one-forms.

Here every product of $\mathfrak g$-valued forms is the combined operation "wedge the form parts, multiply the matrix parts": for $\alpha\in\Omega^p(X;\mathfrak g)$ with entries $\alpha_{ij}\in\Omega^p(X)$ and $\beta\in\Omega^q(X;\mathfrak g)$ with entries $\beta_{jk}\in\Omega^q(X)$, the product $\alpha\wedge\beta\in\Omega^{p+q}(X;\mathfrak g)$ has entries $(\alpha\wedge\beta)_{ik}=\sum_j\alpha_{ij}\wedge\beta_{jk}$, and $\operatorname{tr}(\alpha):=\sum_i\alpha_{ii}\in\Omega^p(X)$ is the scalar-valued form obtained by summing the diagonal entries.

**Recall:**

The result to be verified is the special case, in a fixed trivialisation, of the transgression formula; the point of the exercise is to obtain it once more by a bare-hands expansion, so that the algebra behind the coefficient $\tfrac23$ and the cancellation of the quartic term is fully visible.

![[Thm - Transgression Formula and the Chern-Simons Form#Statement]]

The [[Thm - Transgression Formula and the Chern-Simons Form|transgression formula]] states, in the special case $p(\xi)=\operatorname{tr}(\xi^2)$ and $\omega_0$ the product connection with $\omega_1$ given by $A$, precisely that $\operatorname{tr}(F_A\wedge F_A)=d\operatorname{cs}(A)$; this exercise reproves that special case standalone, so it does not invoke the theorem as the source of the identity.

![[Def - Lie-Algebra-Valued Differential Forms and Their Bracket#The Definition]]

The three algebraic facts about the operations $(\alpha,\beta)\mapsto\alpha\wedge\beta$, $\alpha\mapsto d\alpha$, $\alpha\mapsto\operatorname{tr}\alpha$ on matrix-valued forms that the computation rests on are recalled and proved inside the solution, since each is a one-line consequence of the corresponding scalar fact:

- **Graded Leibniz rule.** For $\alpha\in\Omega^p(X;\mathfrak g)$ and $\beta\in\Omega^q(X;\mathfrak g)$, $d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^p\,\alpha\wedge d\beta$.
- **The trace commutes with $d$.** For $\alpha\in\Omega^p(X;\mathfrak g)$, $d\operatorname{tr}(\alpha)=\operatorname{tr}(d\alpha)$.
- **Graded cyclicity of the trace.** For $\alpha\in\Omega^p(X;\mathfrak g)$ and $\beta\in\Omega^q(X;\mathfrak g)$, $\operatorname{tr}(\alpha\wedge\beta)=(-1)^{pq}\operatorname{tr}(\beta\wedge\alpha)$.

The scalar inputs are graded commutativity of the wedge, $\eta\wedge\zeta=(-1)^{|\eta||\zeta|}\zeta\wedge\eta$, and the graded Leibniz rule for the exterior derivative, both from [[Thm - Wedge Product Properties|the wedge-product properties]]; the trace is the linear map [[Def - Trace|tr]] applied entrywise.

---

# Convergent Strategy

**Problem class.** This is an *identity-verification* problem in the exterior algebra of matrix-valued forms: expand both sides in the primitive quantities $dA$ and $A$, and match. It belongs to the family of "transgression" computations, in which a closed invariant polynomial of the curvature is exhibited as an exact form with an explicit primitive. The distinguishing feature of the class is that the two sides are polynomials of low degree in a single object $A$ and its differential $dA$, so the entire content is bookkeeping of signs and of trace symmetries — no analysis, no geometry, only the graded-commutative algebra of forms and the cyclic symmetry of the matrix trace.

**Assumption pattern.** Nothing is assumed about $X$ beyond smoothness and nothing about $A$ beyond that it is a global $\mathfrak g$-valued one-form; in particular $A$ need not come from a flat or a Yang–Mills connection, and $X$ need not be compact or oriented. The identity is *pointwise* and *algebraic*: it holds at every point of $X$ as an identity of alternating forms on the tangent space, so it is enough to manipulate $A$, $dA$, and their products formally. The one structural hypothesis that is genuinely used is that $\operatorname{tr}$ is the trace of a matrix representation, so that it enjoys ordinary cyclicity $\operatorname{tr}(MN)=\operatorname{tr}(NM)$; this is what upgrades to the graded cyclicity that both makes the two cross terms equal and annihilates the quartic term.

**Theorem routing.** The route has two independent expansions that must meet in the middle. On the target side, substitute $F_A=dA+A\wedge A$ into $\operatorname{tr}(F_A\wedge F_A)$ and expand into four terms; the graded cyclicity of the trace collapses the two cross terms into one doubled term and kills the pure-quartic term. On the source side, apply the trace–$d$ commutation and the graded Leibniz rule to $d\operatorname{cs}(A)$, using $d(dA)=0$; the quadratic piece contributes $\operatorname{tr}(dA\wedge dA)$ and the cubic piece, after the coefficient $\tfrac23$ is multiplied against the factor $3$ produced by three cyclically equal terms, contributes exactly the doubled cross term. Matching the two expansions is the whole proof.

**Key decision point.** The single non-obvious move is to *track the graded signs through every cyclic rearrangement of the trace rather than treating the trace as fully symmetric*. The naive expectation, imported from the scalar trace, is that all reorderings of a product under the trace are equal; for matrix-valued forms this is false, and the corrections are exactly the mechanism of the identity. Concretely, moving a one-form past a three-form under the trace produces a sign $(-1)^{1\cdot3}=-1$, which is what forces $\operatorname{tr}(A^{\wedge4})=-\operatorname{tr}(A^{\wedge4})$ and hence $\operatorname{tr}(A^{\wedge4})=0$; and moving a two-form past a two-form produces $(-1)^{2\cdot2}=+1$, which is what makes the two cross terms in $\operatorname{tr}(F_A\wedge F_A)$ equal rather than cancelling. Getting either sign wrong destroys the identity, so the discipline is to write the degree of every factor beside every rearrangement.

---

# Legal Operations Used

The topic page for this chapter organises these under its Legal Operations; until it is written they are named descriptively.

1. **Expand the curvature and collect by form degree.** Substitute $F_A=dA+A\wedge A$ and multiply out $\operatorname{tr}(F_A\wedge F_A)$, sorting the resulting four terms by which are quadratic, cubic, and quartic in $A$. This is the operation of reducing a curvature invariant to a polynomial in the gauge potential.

2. **Differentiate a matrix-valued form entrywise with the graded Leibniz rule.** Apply $d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^{\deg\alpha}\alpha\wedge d\beta$ term by term to $A\wedge dA$ and $A\wedge A\wedge A$, using $d(dA)=0$ from $d^2=0$.

3. **Commute the trace past the exterior derivative.** Use $d\operatorname{tr}(\alpha)=\operatorname{tr}(d\alpha)$ to move $d$ inside the trace before differentiating, so that only the matrix-valued product need be differentiated.

4. **Rearrange a trace of a product of matrix-valued forms by graded cyclicity.** Apply $\operatorname{tr}(\alpha\wedge\beta)=(-1)^{\deg\alpha\,\deg\beta}\operatorname{tr}(\beta\wedge\alpha)$ to identify equal terms and to prove $\operatorname{tr}(A^{\wedge4})=0$; this is the operation that exploits the cyclic symmetry of the matrix trace in the graded setting.

---

# Hints

> [!note]- Hint 1
> Do not touch $d\operatorname{cs}(A)$ first. Expand the *right-hand* side. Put $F_A=dA+A\wedge A$ and multiply $\operatorname{tr}(F_A\wedge F_A)$ out into four traces, sorted by degree in $A$: one quadratic ($\operatorname{tr}(dA\wedge dA)$), two cubic, and one quartic ($\operatorname{tr}(A^{\wedge4})$). Your goal is to show the quartic vanishes and the two cubics are equal.

> [!note]- Hint 2
> For a matrix-valued $p$-form $\alpha$ and $q$-form $\beta$, the trace of $\alpha\wedge\beta$ is $\sum_{i,j}\alpha_{ij}\wedge\beta_{ji}$, a sum of products of *scalar* forms. Ordinary scalar forms graded-commute: $\alpha_{ij}\wedge\beta_{ji}=(-1)^{pq}\beta_{ji}\wedge\alpha_{ij}$. Summing gives $\operatorname{tr}(\alpha\wedge\beta)=(-1)^{pq}\operatorname{tr}(\beta\wedge\alpha)$. Apply this with $\alpha=A$ (degree $1$) and $\beta=A\wedge A\wedge A$ (degree $3$) to $\operatorname{tr}(A^{\wedge4})$.

> [!note]- Hint 3
> With $\alpha=A$, $\beta=A^{\wedge3}$ the sign is $(-1)^{1\cdot3}=-1$, and $A\wedge A^{\wedge3}=A^{\wedge3}\wedge A=A^{\wedge4}$, so $\operatorname{tr}(A^{\wedge4})=-\operatorname{tr}(A^{\wedge4})$, forcing $\operatorname{tr}(A^{\wedge4})=0$. For the two cubic cross terms $\operatorname{tr}(dA\wedge A\wedge A)$ and $\operatorname{tr}(A\wedge A\wedge dA)$, use graded cyclicity with the two-forms $dA$ and $A\wedge A$: the sign is $(-1)^{2\cdot2}=+1$, so they are equal.

> [!note]- Hint 4
> Now the left-hand side. Use $d\operatorname{tr}=\operatorname{tr}\,d$ and the graded Leibniz rule. For the quadratic piece, $d(A\wedge dA)=dA\wedge dA-A\wedge d(dA)=dA\wedge dA$. For the cubic piece, $d(A\wedge A\wedge A)=dA\wedge A\wedge A-A\wedge dA\wedge A+A\wedge A\wedge dA$; take the trace and use graded cyclicity to show all three terms are equal to $\operatorname{tr}(dA\wedge A\wedge A)$, so the trace of the derivative of the cube is $3\operatorname{tr}(dA\wedge A\wedge A)$. Multiply by $\tfrac23$ and compare with the right-hand side.

---

# Solution

The proof is two expansions that meet. Expanding $\operatorname{tr}(F_A\wedge F_A)$ with $F_A=dA+A\wedge A$ gives $\operatorname{tr}(dA\wedge dA)$ plus two cubic cross terms plus a quartic term; graded cyclicity makes the cross terms equal and kills the quartic, leaving $\operatorname{tr}(dA\wedge dA)+2\operatorname{tr}(dA\wedge A\wedge A)$. Expanding $d\operatorname{cs}(A)$ with the Leibniz rule and $d^2=0$ gives $\operatorname{tr}(dA\wedge dA)$ from the quadratic term and $\tfrac23\cdot 3\operatorname{tr}(dA\wedge A\wedge A)=2\operatorname{tr}(dA\wedge A\wedge A)$ from the cubic term, where the factor $3$ is the number of cyclically equal terms in $d(A^{\wedge3})$. The two expansions coincide, which is the identity.

**Step 0: The three algebraic properties of matrix-valued forms.**

Before either expansion we record, with proof, the graded Leibniz rule, the commutation of the trace with $d$, and the graded cyclicity of the trace; every later line cites one of these.

> [!note]- Derivation
> Fix $\alpha\in\Omega^p(X;\mathfrak g)$ with scalar entries $\alpha_{ij}\in\Omega^p(X)$ and $\beta\in\Omega^q(X;\mathfrak g)$ with entries $\beta_{jk}\in\Omega^q(X)$; the product $\alpha\wedge\beta$ has entries $(\alpha\wedge\beta)_{ik}=\sum_j\alpha_{ij}\wedge\beta_{jk}$.
>
> **Graded Leibniz rule.** Applying the exterior derivative entrywise and using the scalar graded Leibniz rule $d(\eta\wedge\zeta)=d\eta\wedge\zeta+(-1)^{|\eta|}\eta\wedge d\zeta$ ([[Thm - Wedge Product Properties|wedge-product properties]]) on each summand,
> $$d\big((\alpha\wedge\beta)_{ik}\big)=\sum_j d(\alpha_{ij}\wedge\beta_{jk})=\sum_j\Big(d\alpha_{ij}\wedge\beta_{jk}+(-1)^p\,\alpha_{ij}\wedge d\beta_{jk}\Big)\qquad\text{(entrywise, scalar Leibniz, }|\alpha_{ij}|=p\text{)},$$
> which are the entries of $d\alpha\wedge\beta+(-1)^p\,\alpha\wedge d\beta$. Hence $d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^p\,\alpha\wedge d\beta$.
>
> **Trace commutes with $d$.** The trace $\operatorname{tr}(\alpha)=\sum_i\alpha_{ii}$ is a fixed real-linear combination of the entries, and $d$ is real-linear, so $d\operatorname{tr}(\alpha)=d\sum_i\alpha_{ii}=\sum_i d\alpha_{ii}=\operatorname{tr}(d\alpha)$ (linearity of $d$).
>
> **Graded cyclicity of the trace.** Expanding the definitions,
> $$\operatorname{tr}(\alpha\wedge\beta)=\sum_i(\alpha\wedge\beta)_{ii}=\sum_{i,j}\alpha_{ij}\wedge\beta_{ji}\qquad\text{(definition of the product and of }\operatorname{tr}\text{)}.$$
> Each $\alpha_{ij}$ is a scalar $p$-form and each $\beta_{ji}$ a scalar $q$-form, so by scalar graded commutativity $\alpha_{ij}\wedge\beta_{ji}=(-1)^{pq}\beta_{ji}\wedge\alpha_{ij}$ ([[Thm - Wedge Product Properties|wedge-product properties]]). Substituting and relabelling the dummy indices $i\leftrightarrow j$ in the last sum,
> $$\operatorname{tr}(\alpha\wedge\beta)=(-1)^{pq}\sum_{i,j}\beta_{ji}\wedge\alpha_{ij}=(-1)^{pq}\sum_{i,j}\beta_{ij}\wedge\alpha_{ji}=(-1)^{pq}\operatorname{tr}(\beta\wedge\alpha)\qquad\text{(relabel }i\leftrightarrow j\text{; definition of }\operatorname{tr}\text{)}.$$
> This is the graded cyclicity; the scalar cyclicity $\operatorname{tr}(MN)=\operatorname{tr}(NM)$ is its degree-zero case.

**Step 1: Expand the target $\operatorname{tr}(F_A\wedge F_A)$ into four terms.**

Substituting $F_A=dA+A\wedge A$ and multiplying out, $\operatorname{tr}(F_A\wedge F_A)$ is a sum of one quadratic, two cubic, and one quartic trace.

> [!note]- Derivation
> The curvature in the trivialisation is $F_A=dA+A\wedge A$; for a matrix group the general structure equation $F_A=dA+\tfrac12[A\wedge A]$ reduces to this, because $\tfrac12[A\wedge A]=A\wedge A$ for the matrix commutator bracket of one-forms ([[Thm - Structure Equation for the Curvature|structure equation]]). Then, writing $A^2:=A\wedge A$ (a two-form) for brevity and expanding the bilinear product,
> $$\operatorname{tr}(F_A\wedge F_A)=\operatorname{tr}\big((dA+A^2)\wedge(dA+A^2)\big)=\operatorname{tr}(dA\wedge dA)+\operatorname{tr}(dA\wedge A^2)+\operatorname{tr}(A^2\wedge dA)+\operatorname{tr}(A^2\wedge A^2)$$
> by bilinearity of $\wedge$ and linearity of $\operatorname{tr}$. The four terms are quadratic, cubic, cubic, and quartic in $A$ respectively; we treat the quartic term in Step 2 and the two cubic terms in Step 3.

**Step 2: The quartic term vanishes, $\operatorname{tr}(A\wedge A\wedge A\wedge A)=0$.**

Graded cyclicity applied to a one-form moved past a three-form yields a minus sign, and a quantity equal to its own negative is zero.

> [!note]- Derivation
> Write $A^{\wedge4}=A^2\wedge A^2=A\wedge(A\wedge A\wedge A)=A\wedge A^{\wedge3}$; this is legitimate because $\wedge$ on matrix-valued forms is associative (it is associative entrywise, being built from the associative scalar $\wedge$ and matrix multiplication). Apply graded cyclicity from Step 0 with $\alpha=A$ (degree $p=1$) and $\beta=A^{\wedge3}$ (degree $q=3$):
> $$\operatorname{tr}(A\wedge A^{\wedge3})=(-1)^{1\cdot3}\operatorname{tr}(A^{\wedge3}\wedge A)=-\operatorname{tr}(A^{\wedge4})\qquad\text{(graded cyclicity, }(-1)^{3}=-1\text{)}.$$
> The left-hand side is itself $\operatorname{tr}(A^{\wedge4})$, since $A\wedge A^{\wedge3}=A^{\wedge4}$. Hence $\operatorname{tr}(A^{\wedge4})=-\operatorname{tr}(A^{\wedge4})$, so $2\operatorname{tr}(A^{\wedge4})=0$ and therefore
> $$\operatorname{tr}(A\wedge A\wedge A\wedge A)=0.$$
> This is the vanishing announced in the problem: the odd total sign incurred by transposing a single one-form past the remaining three is exactly what makes the quartic self-cancelling. (The same argument shows $\operatorname{tr}(B^{\wedge4})=0$ for any single one-form-degree matrix-valued form; it fails for even-degree factors, where the sign would be $+1$.)

**Step 3: The two cubic cross terms are equal.**

Graded cyclicity applied to a two-form moved past a two-form yields a plus sign, so the two cross terms coincide.

> [!note]- Derivation
> Apply graded cyclicity from Step 0 with $\alpha=dA$ and $\beta=A^2=A\wedge A$, both of degree $2$:
> $$\operatorname{tr}(dA\wedge A^2)=(-1)^{2\cdot2}\operatorname{tr}(A^2\wedge dA)=\operatorname{tr}(A^2\wedge dA)\qquad\text{(graded cyclicity, }(-1)^{4}=+1\text{)}.$$
> Therefore, combining with Steps 1 and 2 (which discard the quartic term),
> $$\operatorname{tr}(F_A\wedge F_A)=\operatorname{tr}(dA\wedge dA)+2\,\operatorname{tr}(dA\wedge A\wedge A)\qquad\text{(Step 1, }\operatorname{tr}(A^{\wedge4})=0\text{ by Step 2, cross terms equal)}.$$
> This is the reduced form of the target that Step 5 will match.

**Step 4: Differentiate the quadratic part of $\operatorname{cs}(A)$.**

Commuting the trace past $d$ and using $d(dA)=0$, the derivative of $\operatorname{tr}(A\wedge dA)$ is $\operatorname{tr}(dA\wedge dA)$.

> [!note]- Derivation
> Using the trace–$d$ commutation and then the graded Leibniz rule from Step 0, with $A$ of degree $1$,
> $$d\operatorname{tr}(A\wedge dA)=\operatorname{tr}\big(d(A\wedge dA)\big)=\operatorname{tr}\big(dA\wedge dA+(-1)^{1}A\wedge d(dA)\big)\qquad\text{(}d\operatorname{tr}=\operatorname{tr}\,d\text{; graded Leibniz)}.$$
> By $d^2=0$ ([[Thm - Wedge Product Properties|wedge-product properties]]) we have $d(dA)=0$, so the second term drops and
> $$d\operatorname{tr}(A\wedge dA)=\operatorname{tr}(dA\wedge dA).$$

**Step 5: Differentiate the cubic part of $\operatorname{cs}(A)$.**

The Leibniz rule produces three terms; graded cyclicity shows all three traces are equal, giving $3\operatorname{tr}(dA\wedge A\wedge A)$, and the coefficient $\tfrac23$ turns this into the doubled cross term.

> [!note]- Derivation
> By the graded Leibniz rule (Step 0) applied twice, with $A$ of degree $1$,
> $$d(A\wedge A\wedge A)=dA\wedge A\wedge A+(-1)^{1}A\wedge d(A\wedge A)=dA\wedge A\wedge A-A\wedge(dA\wedge A-A\wedge dA),$$
> using $d(A\wedge A)=dA\wedge A-A\wedge dA$ (Leibniz, degree $1$). Distributing,
> $$d(A\wedge A\wedge A)=dA\wedge A\wedge A-A\wedge dA\wedge A+A\wedge A\wedge dA\qquad\text{(graded Leibniz, twice)}.$$
> Now take the trace and evaluate each term by graded cyclicity. For the second term, move the leading $A$ (degree $1$) past $dA\wedge A$ (degree $3$):
> $$\operatorname{tr}(A\wedge dA\wedge A)=(-1)^{1\cdot3}\operatorname{tr}(dA\wedge A\wedge A)=-\operatorname{tr}(dA\wedge A\wedge A)\qquad\text{(graded cyclicity, }(-1)^3=-1\text{)}.$$
> For the third term, move $A\wedge A$ (degree $2$) past $dA$ (degree $2$):
> $$\operatorname{tr}(A\wedge A\wedge dA)=(-1)^{2\cdot2}\operatorname{tr}(dA\wedge A\wedge A)=\operatorname{tr}(dA\wedge A\wedge A)\qquad\text{(graded cyclicity, }(-1)^4=+1\text{)}.$$
> Therefore, using $d\operatorname{tr}=\operatorname{tr}\,d$ and combining the three traces,
> $$d\operatorname{tr}(A\wedge A\wedge A)=\operatorname{tr}(dA\wedge A\wedge A)-\big(-\operatorname{tr}(dA\wedge A\wedge A)\big)+\operatorname{tr}(dA\wedge A\wedge A)=3\,\operatorname{tr}(dA\wedge A\wedge A).$$
> Multiplying by the coefficient $\tfrac23$ of the cubic term,
> $$\tfrac23\,d\operatorname{tr}(A\wedge A\wedge A)=\tfrac23\cdot 3\,\operatorname{tr}(dA\wedge A\wedge A)=2\,\operatorname{tr}(dA\wedge A\wedge A).$$
> This is where the coefficient $\tfrac23$ earns its place: it is exactly the reciprocal of the count $3$ of cyclically equal cubic terms, up to the factor $2$ needed to match the doubled cross term of the curvature.

**Step 6: Assemble the two expansions.**

Adding Steps 4 and 5 gives $d\operatorname{cs}(A)$, which equals the reduced target of Step 3.

> [!note]- Derivation
> By linearity of $d$ and $\operatorname{tr}$,
> $$d\operatorname{cs}(A)=d\operatorname{tr}(A\wedge dA)+\tfrac23\,d\operatorname{tr}(A\wedge A\wedge A)=\operatorname{tr}(dA\wedge dA)+2\,\operatorname{tr}(dA\wedge A\wedge A)\qquad\text{(Step 4 and Step 5)}.$$
> By Step 3 the right-hand side is exactly $\operatorname{tr}(F_A\wedge F_A)$. Hence
> $$d\operatorname{cs}(A)=\operatorname{tr}(F_A\wedge F_A),$$
> which is the required identity $(97)$.

> [!note]- Complete formal solution
> **Claim.** For a matrix Lie algebra $\mathfrak g$, a smooth manifold $X$, and $A\in\Omega^1(X;\mathfrak g)$ with $F_A=dA+A\wedge A$, one has $d\operatorname{tr}\big(A\wedge dA+\tfrac23A\wedge A\wedge A\big)=\operatorname{tr}(F_A\wedge F_A)$.
>
> Throughout, products of matrix-valued forms are wedge-of-forms combined with matrix multiplication, and the following hold for $\alpha\in\Omega^p(X;\mathfrak g)$, $\beta\in\Omega^q(X;\mathfrak g)$: the graded Leibniz rule $d(\alpha\wedge\beta)=d\alpha\wedge\beta+(-1)^p\alpha\wedge d\beta$; the commutation $d\operatorname{tr}(\alpha)=\operatorname{tr}(d\alpha)$; and the graded cyclicity $\operatorname{tr}(\alpha\wedge\beta)=(-1)^{pq}\operatorname{tr}(\beta\wedge\alpha)$. Each follows entrywise from the scalar graded commutativity $\eta\wedge\zeta=(-1)^{|\eta||\zeta|}\zeta\wedge\eta$, the scalar Leibniz rule, and the linearity of $d$ and of $\operatorname{tr}$.
>
> *Right-hand side.* Substituting $F_A=dA+A\wedge A$ and writing $A^2=A\wedge A$,
> $$\operatorname{tr}(F_A\wedge F_A)=\operatorname{tr}(dA\wedge dA)+\operatorname{tr}(dA\wedge A^2)+\operatorname{tr}(A^2\wedge dA)+\operatorname{tr}(A^{\wedge4}).$$
> The quartic term vanishes: with $\alpha=A$ ($p=1$), $\beta=A^{\wedge3}$ ($q=3$), graded cyclicity gives $\operatorname{tr}(A^{\wedge4})=(-1)^{3}\operatorname{tr}(A^{\wedge4})=-\operatorname{tr}(A^{\wedge4})$, so $\operatorname{tr}(A^{\wedge4})=0$. The two cross terms are equal: with $\alpha=dA$, $\beta=A^2$, both of degree $2$, graded cyclicity gives $\operatorname{tr}(dA\wedge A^2)=(-1)^{4}\operatorname{tr}(A^2\wedge dA)=\operatorname{tr}(A^2\wedge dA)$. Hence
> $$\operatorname{tr}(F_A\wedge F_A)=\operatorname{tr}(dA\wedge dA)+2\,\operatorname{tr}(dA\wedge A\wedge A).$$
>
> *Left-hand side.* By $d\operatorname{tr}=\operatorname{tr}\,d$, the graded Leibniz rule, and $d^2=0$,
> $$d\operatorname{tr}(A\wedge dA)=\operatorname{tr}\big(dA\wedge dA-A\wedge d(dA)\big)=\operatorname{tr}(dA\wedge dA).$$
> For the cubic term, the Leibniz rule (twice) gives $d(A^{\wedge3})=dA\wedge A\wedge A-A\wedge dA\wedge A+A\wedge A\wedge dA$; graded cyclicity gives $\operatorname{tr}(A\wedge dA\wedge A)=(-1)^{3}\operatorname{tr}(dA\wedge A\wedge A)=-\operatorname{tr}(dA\wedge A\wedge A)$ and $\operatorname{tr}(A\wedge A\wedge dA)=(-1)^{4}\operatorname{tr}(dA\wedge A\wedge A)=\operatorname{tr}(dA\wedge A\wedge A)$, so
> $$d\operatorname{tr}(A^{\wedge3})=\operatorname{tr}(dA\wedge A\wedge A)+\operatorname{tr}(dA\wedge A\wedge A)+\operatorname{tr}(dA\wedge A\wedge A)=3\,\operatorname{tr}(dA\wedge A\wedge A).$$
> Therefore
> $$d\operatorname{cs}(A)=d\operatorname{tr}(A\wedge dA)+\tfrac23\,d\operatorname{tr}(A^{\wedge3})=\operatorname{tr}(dA\wedge dA)+2\,\operatorname{tr}(dA\wedge A\wedge A).$$
>
> *Conclusion.* The two expansions agree, so $d\operatorname{cs}(A)=\operatorname{tr}(F_A\wedge F_A)$. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to declare "$\operatorname{tr}(A\wedge A\wedge A\wedge A)=0$ because the trace is cyclic and $A$ anticommutes with itself", collapsing the sign bookkeeping into a slogan. This is unsafe: the *even*-degree analogue $\operatorname{tr}\big((A\wedge A)\wedge(A\wedge A)\big)$ is the *same* form $\operatorname{tr}(A^{\wedge4})$, yet the naive slogan applied to the two-form $A\wedge A$ would give the sign $(-1)^{2\cdot2}=+1$ and conclude nothing. The vanishing depends on choosing the factorisation $A^{\wedge4}=A\wedge A^{\wedge3}$, whose factors have degrees $1$ and $3$ and hence the sign $(-1)^{1\cdot3}=-1$. The lesson is that the graded sign is a property of the chosen factorisation of the product, not of the product itself, so the degrees must be written down at each rearrangement.

---

# Key Takeaways

**A closed characteristic form is exhibited as exact by naming its primitive, and the primitive is found by integrating the polynomial identity for a one-parameter family of connections — but in a single trivialisation it is a pure algebra computation.** The identity $d\operatorname{cs}(A)=\operatorname{tr}(F_A\wedge F_A)$ is the local, trivialised heart of the [[Thm - Transgression Formula and the Chern-Simons Form|transgression formula]], and it is worth having seen it fall out of nothing but the Leibniz rule and the cyclicity of the trace. The reusable principle is that whenever one meets an invariant polynomial $\operatorname{tr}(F^{\wedge k})$ of a curvature, its exactness on a trivial bundle is not a deep fact but a bookkeeping identity: expand $F=dA+A\wedge A$, and the $d$-exact primitive is a universal polynomial in $A$ and $dA$ whose coefficients (here $1$ and $\tfrac23$) are fixed by counting cyclically equal terms. The trigger to reach for this pattern is the appearance of $\operatorname{tr}(F\wedge F)$ or a higher Chern–Weil density in a setting where a trivialisation is available; the payoff is an explicit boundary term, which is exactly what the Chern–Simons functional integrates.

**Graded cyclicity of the trace, not full symmetry, is the correct algebraic law for matrix-valued forms, and its sign is $(-1)^{\deg\alpha\,\deg\beta}$.** The single most transferable lesson is the discipline of writing the degree of each factor beside every rearrangement of a trace. Two consequences of the same law do opposite things in this problem: moving a one-form past a three-form gives $-1$ and annihilates $\operatorname{tr}(A^{\wedge4})$, while moving a two-form past a two-form gives $+1$ and doubles the cross term. The diagnostic that recurs across gauge theory is: *odd-times-odd products under the trace tend to vanish or antisymmetrise, even-times-even products tend to survive and symmetrise.* This is why $\operatorname{tr}(A^{\wedge2m+1})$-type terms behave so differently from $\operatorname{tr}(A^{\wedge2m})$-type terms, and why odd Chern–Simons forms exist in odd dimensions at all.

**The coefficient $\tfrac23$ is not a normalisation to be memorised but the reciprocal of a combinatorial count.** When $d$ falls on $A\wedge A\wedge A$, the Leibniz rule produces three terms; graded cyclicity makes all three traces equal, so the derivative of the cube is $3\operatorname{tr}(dA\wedge A\wedge A)$. The curvature's two cross terms, on the other hand, sum to $2\operatorname{tr}(dA\wedge A\wedge A)$. The coefficient that reconciles $3$ with $2$ is $\tfrac23$, and this is the same coefficient one finds on the cubic term of every $\operatorname{tr}(F^{\wedge2})$ transgression. The habit to carry away is that whenever a mysterious rational coefficient appears in a differential-geometric identity — the $\tfrac23$ here, the $\tfrac12$ in the structure equation $F=dA+\tfrac12[A\wedge A]$, the $\tfrac1{8\pi^2}$ in $\vartheta$ — it is almost always a count of equal terms or a symmetry factor, and tracing it to that count is more illuminating than accepting it. This exercise is the companion computation to [[Ex - The Chern-Simons Functional along a Path of Connections]], where the same identity is integrated over $M\times[t_0,t_1]$ to compare the functional at the two ends of a path of connections.
