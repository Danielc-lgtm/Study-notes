---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
  - "Thm - Wedge Product Properties"
  - "Thm - Coordinate Expression for the Exterior Derivative"
  - "Def - Lie Algebra"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth manifold (smooth means $C^\infty$; manifolds are Hausdorff and second countable), and $\mathfrak{g}$ is a finite-dimensional real or complex [[Def - Lie Algebra|Lie algebra]] with bracket $[\,\cdot\,,\cdot\,]:\mathfrak{g}\times\mathfrak{g}\to\mathfrak{g}$. We write $\Omega^p(M)=\Gamma(\Lambda^p T^*M)$ for the ordinary real-valued differential $p$-forms on $M$, and
$$\Omega^p(M;\mathfrak{g})=\Omega^p(M)\otimes_{\mathbb{R}}\mathfrak{g}$$
for the $\mathfrak{g}$-valued $p$-forms — smooth sections of $\Lambda^p T^*M\otimes\mathfrak{g}$. A general element of $\Omega^p(M;\mathfrak{g})$ is a finite sum of **decomposable** forms $a\otimes\xi$ with $a\in\Omega^p(M)$ and $\xi\in\mathfrak{g}$; if $(e_1,\dots,e_m)$ is a basis of $\mathfrak{g}$, every $\alpha\in\Omega^p(M;\mathfrak{g})$ is written uniquely as $\alpha=\sum_{k=1}^m\alpha^k\otimes e_k$ with $\alpha^k\in\Omega^p(M)$.

The letters $\alpha,\beta,\gamma$ denote $\mathfrak{g}$-valued forms of degrees $p,q,r$ respectively; $a,b,c$ denote the ordinary-form factors of decomposables, of the same degrees $p,q,r$; and $\xi,\eta,\zeta$ denote elements of $\mathfrak{g}$. The letter $A$ always denotes a $\mathfrak{g}$-valued $1$-form, $A\in\Omega^1(M;\mathfrak{g})$.

Two operations combine $\mathfrak{g}$-valued forms, both taken from [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|the definition of the bracket of Lie-algebra-valued forms]].

- The **graded bracket** $[\,\cdot\wedge\cdot\,]:\Omega^p(M;\mathfrak{g})\times\Omega^q(M;\mathfrak{g})\to\Omega^{p+q}(M;\mathfrak{g})$ is the $\mathbb{R}$-bilinear map determined on decomposables by
$$[(a\otimes\xi)\wedge(b\otimes\eta)]:=(a\wedge b)\otimes[\xi,\eta],$$
where $a\wedge b$ is the ordinary wedge product and $[\xi,\eta]$ is the Lie bracket. For two $1$-forms this agrees with the pointwise formula $[\alpha\wedge\beta](X,Y)=[\alpha(X),\beta(Y)]-[\alpha(Y),\beta(X)]$, so in particular $[A\wedge A](X,Y)=2[A(X),A(Y)]$.
- When $\mathfrak{g}\subseteq\mathfrak{gl}(n,\mathbb{K})$ is a **matrix Lie algebra** ($\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$), the bracket is the commutator $[\xi,\eta]=\xi\eta-\eta\xi$, and there is a second product, the **matrix wedge** $\alpha\wedge\beta$, the $\mathbb{R}$-bilinear map determined on decomposables by
$$(a\otimes\xi)\wedge(b\otimes\eta):=(a\wedge b)\otimes(\xi\eta),$$
with $\xi\eta$ the matrix product. This is the product for which Haydys writes the curvature as $F=dA+A\wedge A$.

The exterior derivative acts componentwise on $\mathfrak{g}$-valued forms: $d(a\otimes\xi):=da\otimes\xi$, extended $\mathbb{R}$-linearly, so that $d\alpha=\sum_k d\alpha^k\otimes e_k$ for $\alpha=\sum_k\alpha^k\otimes e_k$. This is well defined because the basis vectors $e_k\in\mathfrak{g}$ are constant.

> [!warning] Convention: bracket notation
> The series follows Haydys and writes the graded bracket with a wedge inside the bracket, $[\alpha\wedge\beta]$, to distinguish it from the pointwise Lie bracket $[\xi,\eta]$ of algebra elements. Bär writes the same object with a comma, $[\alpha,\beta]$ (Bär's Proposition 2.4.2 writes $[\omega,\omega]$), and defines it for $1$-forms by $[\eta,\varphi](X,Y)=[\eta(X),\varphi(Y)]-[\eta(Y),\varphi(X)]$; the two notations denote the same operation. Whenever a Bär statement is quoted, replace his $[\,\cdot\,,\cdot\,]$ on forms by the series' $[\,\cdot\wedge\cdot\,]$.

The full symbol registry for the chapter is on the parent page [[Gauge Theory IV — Connections and Curvature on Principal Bundles]].

---

# Statement

> **Theorem (graded antisymmetry, Leibniz rule, and Jacobi identity for the bracket of $\mathfrak{g}$-valued forms).** Let $M$ be a smooth manifold, $\mathfrak{g}$ a finite-dimensional Lie algebra, and let $\alpha\in\Omega^p(M;\mathfrak{g})$, $\beta\in\Omega^q(M;\mathfrak{g})$, $\gamma\in\Omega^r(M;\mathfrak{g})$. Then the graded bracket satisfies:
>
> **(a) Graded antisymmetry.**
> $$[\alpha\wedge\beta]=-(-1)^{pq}\,[\beta\wedge\alpha].$$
>
> **(b) Graded Leibniz rule.**
> $$d[\alpha\wedge\beta]=[d\alpha\wedge\beta]+(-1)^{p}\,[\alpha\wedge d\beta].$$
>
> **(c) Graded Jacobi identity.**
> $$(-1)^{pr}\,[\alpha\wedge[\beta\wedge\gamma]]+(-1)^{pq}\,[\beta\wedge[\gamma\wedge\alpha]]+(-1)^{qr}\,[\gamma\wedge[\alpha\wedge\beta]]=0.$$
> In particular, for a single $1$-form $A\in\Omega^1(M;\mathfrak{g})$,
> $$[A\wedge[A\wedge A]]=0.$$
>
> **(d) Matrix form.** If $\mathfrak{g}\subseteq\mathfrak{gl}(n,\mathbb{K})$ is a matrix Lie algebra, then in terms of the matrix wedge,
> $$[\alpha\wedge\beta]=\alpha\wedge\beta-(-1)^{pq}\,\beta\wedge\alpha.$$
> In particular, for $1$-forms, $[A\wedge A]=2\,A\wedge A$ and $[A\wedge B]=A\wedge B+B\wedge A$.

> **Corollary (specialisation of antisymmetry).** From (a): the bracket of two $1$-forms is *symmetric*, $[\alpha\wedge\beta]=[\beta\wedge\alpha]$ (here $p=q=1$); the bracket of a $2$-form $\omega$ with a $1$-form $\eta$ is antisymmetric in the naive sense, $[\omega\wedge\eta]=-[\eta\wedge\omega]$ (here $p=2$, $q=1$). The second identity is the one used in the local proof of the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]].

---

# Motivation

The bracket $[\,\cdot\wedge\cdot\,]$ is the operation that lets the whole formalism of connections and curvature on a principal bundle be written in coordinates. The local curvature of a connection is $F_A=dA+\tfrac12[A\wedge A]$, the structure equation reads $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$, and the Bianchi identity in local form is $dF_A+[A\wedge F_A]=0$. Every one of these identities is manipulated — differentiated, rearranged, cancelled — using nothing but the four rules stated above. Without them one cannot even check that the curvature transforms correctly under a change of gauge, let alone prove that $dF_A+[A\wedge F_A]=0$.

The theorem is the exact analogue, for $\mathfrak{g}$-valued forms, of three facts one already knows for ordinary forms: the wedge product is graded-anticommutative, the exterior derivative is a graded derivation of it, and — the new ingredient — the fibrewise multiplication is the Lie bracket, so the associativity of the wedge is replaced by the Jacobi identity of $\mathfrak{g}$. The single most important consequence is the last displayed line, $[A\wedge[A\wedge A]]=0$. That identity is what makes the cubic term in the Bianchi computation vanish, and it is the reason the Chern–Simons integrand and the closedness of Chern–Weil forms behave as they do. It is worth stating plainly at the outset that this identity is a genuinely non-trivial fact: it fails for a general bilinear product and holds only because the Lie bracket obeys Jacobi.

The role of the theorem, then, is not to introduce a new object but to certify that the object introduced on the [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|companion definition page]] obeys the algebraic laws every later computation silently assumes.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is only that $\alpha,\beta,\gamma$ are $\mathfrak{g}$-valued forms of definite degrees; the skill is recognising when an object that does not look like a bracket of forms actually is one, so that these rules become available.

The first disguised source is **a curvature or connection written in a local frame**. A connection on a principal bundle produces, over a trivialising open set $U$, a gauge potential $A\in\Omega^1(U;\mathfrak{g})$, and its curvature is $F_A=dA+\tfrac12[A\wedge A]$. Any statement about $F_A$ — that it is closed under the covariant derivative, that it transforms by the adjoint action, that its trace powers are closed — is a statement about brackets of $\mathfrak{g}$-valued forms and is proved by the four rules. The non-obvious bridge is that $\tfrac12[A\wedge A]$, which contains a *single* form $A$ used twice, is not zero the way $a\wedge a=0$ is for an ordinary $1$-form: because the fibrewise product is the Lie bracket rather than a commutative product, $[A\wedge A](X,Y)=2[A(X),A(Y)]$ need not vanish. *Example problem:* show that $d^{A}F_A:=dF_A+[A\wedge F_A]$ vanishes, purely by expanding with (b) and (c).

The second disguised source is **the Maurer–Cartan form of a Lie group**. The left-invariant form $\theta\in\Omega^1(G;\mathfrak{g})$ satisfies $d\theta+\tfrac12[\theta\wedge\theta]=0$ (the [[Thm - The Maurer-Cartan Equation|Maurer–Cartan equation]]), an identity among $\mathfrak{g}$-valued forms on $G$; differentiating it or pulling it back along a map $g:U\to G$ requires exactly the Leibniz rule (b) and the antisymmetry (a). The bridge is that $\theta$ is a single $\mathfrak{g}$-valued $1$-form, so $[\theta\wedge\theta]$ is governed by the $p=q=1$ symmetric case of (a). *Example problem:* differentiate the Maurer–Cartan equation and use $[\theta\wedge[\theta\wedge\theta]]=0$ to see the result is automatic.

The third disguised source is **any expression $\rho_*(\alpha)\wedge\phi$ in which a $\mathfrak{g}$-valued form acts on a vector-valued form through a representation**. When $\rho:\mathfrak{g}\to\operatorname{End}(V)$ is a [[Def - Representation of a Lie Algebra|representation]], the induced action of $\mathfrak{g}$-valued forms on $V$-valued forms inherits a Leibniz rule and a compatibility with brackets that are proved by exactly the decomposable-reduction argument used here, with the Lie bracket replaced by $\rho_*[\xi,\eta]=\rho_*(\xi)\rho_*(\eta)-\rho_*(\eta)\rho_*(\xi)$. The bridge is that a representation converts the abstract bracket into a commutator of endomorphisms, so part (d) of this theorem applies verbatim in $\operatorname{End}(V)$. *Example problem:* verify that the induced covariant exterior derivative on an associated bundle satisfies its own Leibniz rule.

**Targets (Output Amplification)**

Combine **(a) and (b) with the structure equation** $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$ to obtain the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]]. Differentiating the structure equation gives $d\Omega=\tfrac12 d[\omega\wedge\omega]$; the Leibniz rule (b) turns this into $\tfrac12([d\omega\wedge\omega]-[\omega\wedge d\omega])$, and antisymmetry (a) for a $2$-form against a $1$-form collapses the two terms into $[d\omega\wedge\omega]=[\Omega\wedge\omega]-\tfrac12[[\omega\wedge\omega]\wedge\omega]$; the extra ingredient is the Jacobi identity (c), which kills the last cubic term. The payoff is the closedness $d^{\omega}\Omega=0$, the single most-used property of curvature.

Combine **(c) with a connection $1$-form** to prove that the local structure equation is *consistent*. In the derivation $F_A=dA+\tfrac12[A\wedge A]$, verifying the Bianchi identity locally produces the term $\tfrac12[A\wedge[A\wedge A]]$; the extra ingredient $[A\wedge[A\wedge A]]=0$ from (c) makes it vanish, and without it the local Bianchi identity would carry a spurious cubic term. The payoff is that $dF_A+[A\wedge F_A]=0$ holds with no correction.

Combine **(b) with an $\operatorname{Ad}$-invariant polynomial** to run the [[Thm - Structure Equation for the Curvature|Chern–Weil]] argument (chapter VI). For an invariant polynomial $f$ of degree $k$, the form $f(F_A)$ is closed; the proof differentiates $f(F_A,\dots,F_A)$ using the Leibniz rule (b) for the bracket and the invariance identity $\sum_i f(\dots,[\xi,F],\dots)=0$. The extra ingredient is invariance of $f$; the payoff is a closed $2k$-form whose de Rham class is independent of the connection — the characteristic class.

---

# Why Is It True

Forget the signs for a moment and picture what the bracket of $\mathfrak{g}$-valued forms *is*. A $\mathfrak{g}$-valued form is a form whose coefficients live in the Lie algebra. To bracket two of them, you wedge the form parts and Lie-bracket the algebra parts — the two structures act in separate slots and do not interfere. So every algebraic law of the combined operation is just the product of a law for the wedge and a law for the Lie bracket, together with the sign that arises when the two slots are reordered against each other.

**The one-sentence mechanism: the graded bracket is the wedge product tensored with the Lie bracket, so its antisymmetry is (graded-anticommutativity of $\wedge$) $\times$ (antisymmetry of $[\,\cdot\,,\cdot\,]$), its Leibniz rule is the Leibniz rule of $d$ on the form slot, and its Jacobi identity is the Jacobi identity of $\mathfrak{g}$ on the algebra slot after the form slots are freely reordered.**

Take antisymmetry (a). Swapping $\alpha$ and $\beta$ swaps the form parts, costing the sign $(-1)^{pq}$ from graded-anticommutativity of the wedge, and swaps the algebra parts, costing the sign $-1$ from antisymmetry of the Lie bracket. The two signs multiply: $(-1)^{pq}\cdot(-1)=-(-1)^{pq}$. That is the whole content of (a). The surprising consequence — that two $1$-forms bracket *symmetrically* — is just $-(-1)^{1\cdot1}=+1$; the minus from the Lie bracket and the minus from the wedge cancel.

Take the Leibniz rule (b). The exterior derivative sees only the form part, because the algebra part is constant. So $d$ of the bracket is $d$ of a wedge of ordinary forms tensored with a fixed bracket $[\xi,\eta]$, and the graded Leibniz rule for the ordinary $d$ — the sign $(-1)^p$ appearing exactly when $d$ moves past the degree-$p$ factor $a$ — reproduces itself in the bracket verbatim.

Take the Jacobi identity (c). Each of the three terms, once reduced to decomposables, is a triple wedge of the form parts times a nested double bracket of the algebra parts. The signs $(-1)^{pr},(-1)^{pq},(-1)^{qr}$ are precisely the signs needed so that, after reordering all three triple wedges into the *same* order $a\wedge b\wedge c$, the three terms carry the identical form factor $(-1)^{pr}(a\wedge b\wedge c)$; the algebra factors are then $[\xi,[\eta,\zeta]]+[\eta,[\zeta,\xi]]+[\zeta,[\xi,\eta]]$, which is zero by the Jacobi identity of $\mathfrak{g}$. The grading in (c) is exactly the bookkeeping that makes the form parts line up so the algebra parts can cancel.

---

# What Makes This Hard

The single non-obvious step is the sign accounting in the Jacobi identity (c): one must reorder three triple wedges $a\wedge b\wedge c$, $b\wedge c\wedge a$, $c\wedge a\wedge b$ into a common order and check that the prefactors $(-1)^{pr},(-1)^{pq},(-1)^{qr}$ combine with the reordering signs to give the *same* coefficient on all three, so that the Jacobi identity of $\mathfrak{g}$ can be applied to the sum of the three double brackets. The common error is to omit the reordering signs — to treat $b\wedge c\wedge a$ as if it equalled $a\wedge b\wedge c$ — which makes the three algebra terms fail to assemble into the Jacobi cyclic sum. The second trap, throughout, is to forget that $[A\wedge A]\ne0$ for a $1$-form $A$: because the fibrewise product is the Lie bracket, not a commutative product, the naive "odd form squares to zero" intuition is wrong, and the correct statement is $[A\wedge A](X,Y)=2[A(X),A(Y)]$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Every identity is $\mathbb{R}$-multilinear in its form arguments, so it holds in general as soon as it holds on decomposable forms $\alpha=a\otimes\xi$, $\beta=b\otimes\eta$, $\gamma=c\otimes\zeta$. On decomposables, the bracket splits as $[(a\otimes\xi)\wedge(b\otimes\eta)]=(a\wedge b)\otimes[\xi,\eta]$, and each identity becomes a known law of the wedge in the form slot tensored with a known law of the Lie bracket in the algebra slot.

**Subgoal decomposition:**

1. **Reduce to decomposables.**
   - *Hint:* Fix a basis of $\mathfrak{g}$; write each form as a finite sum of basis-decomposables; note all four operations ($[\,\cdot\wedge\cdot\,]$, matrix wedge, $d$, ordinary $\wedge$) are $\mathbb{R}$-multilinear.
   - *Why needed:* It turns four identities among arbitrary forms into four identities among single decomposables, where the two slots separate.

2. **Prove (a) on decomposables.**
   - *Hint:* $[\beta\wedge\alpha]=(b\wedge a)\otimes[\eta,\xi]$; apply graded-anticommutativity $b\wedge a=(-1)^{pq}a\wedge b$ and antisymmetry $[\eta,\xi]=-[\xi,\eta]$.
   - *Why needed:* It is (a) itself, and the $p=2,q=1$ case is used inside (b)'s applications and in Bianchi.

3. **Prove the graded Leibniz rule for the ordinary exterior derivative.**
   - *Hint:* In a chart, $a=\sum'_I a_I\,dx^I$, $b=\sum'_J b_J\,dx^J$; expand $d(a\wedge b)$ using the coordinate formula and the product rule $d(fg)=f\,dg+g\,df$ for functions; move a $1$-form past a $p$-form to produce the sign $(-1)^p$.
   - *Why needed:* Part (b) reduces to this after tensoring with the constant $[\xi,\eta]$; the only vault page stating it axiomatically is not proof-complete, so it is proved here.

4. **Prove (b) on decomposables.**
   - *Hint:* $[\alpha\wedge\beta]=(a\wedge b)\otimes[\xi,\eta]$; apply $d$ componentwise and the Leibniz rule of subgoal 3 to $d(a\wedge b)$; regroup the two summands as brackets.
   - *Why needed:* It is (b) itself.

5. **Establish the triple-wedge reordering signs.**
   - *Hint:* Apply graded-anticommutativity twice: $b\wedge c\wedge a=(-1)^{p(q+r)}a\wedge b\wedge c$ and $c\wedge a\wedge b=(-1)^{r(p+q)}a\wedge b\wedge c$.
   - *Why needed:* It lines up the form parts of the three Jacobi terms into a common order.

6. **Prove (c) on decomposables.**
   - *Hint:* Expand each of the three terms as a triple wedge tensored with a nested double bracket; use subgoal 5 and check the prefactors all reduce to $(-1)^{pr}$; sum the algebra parts and apply the Jacobi identity of $\mathfrak{g}$.
   - *Why needed:* It is (c); the $p=q=r=1$ case gives $[A\wedge[A\wedge A]]=0$.

7. **Prove (d) on decomposables.**
   - *Hint:* With $[\xi,\eta]=\xi\eta-\eta\xi$, write $[\alpha\wedge\beta]=(a\wedge b)\otimes\xi\eta-(a\wedge b)\otimes\eta\xi$ and identify the two summands as $\alpha\wedge\beta$ and $(-1)^{pq}\beta\wedge\alpha$.
   - *Why needed:* It is (d), and its $1$-form case explains the factor $\tfrac12$ in the structure equation.

---

# Lemma Decomposition

> [!note]- Lemma 1: Reduction to decomposable forms
> **Statement:** Let $T$ be a map that takes one, two, or three $\mathfrak{g}$-valued forms and returns a $\mathfrak{g}$-valued form, and suppose $T$ is $\mathbb{R}$-linear in each of its arguments. If two such maps $T$ and $T'$ agree on all tuples of decomposable forms $a\otimes\xi$ (with $a\in\Omega^\bullet(M)$, $\xi\in\mathfrak{g}$), then they agree on all tuples of $\mathfrak{g}$-valued forms. Consequently each identity (a)–(d) — whose two sides are $\mathbb{R}$-multilinear in $\alpha,\beta,\gamma$ — holds for all forms as soon as it holds for decomposables.
>
> **Hint:** Fix a basis $(e_1,\dots,e_m)$ of $\mathfrak{g}$ and expand each form in it; both sides are multilinear, so they distribute over the finite sums.
>
> **Why needed:** It is the device that separates the form slot from the algebra slot, reducing every identity to a single computation on $a\otimes\xi$ where the two structures do not interfere.
>
> > [!note]- Full proof
> > **Every $\mathfrak{g}$-valued form is a finite sum of basis-decomposables.** By definition $\Omega^p(M;\mathfrak{g})=\Omega^p(M)\otimes_{\mathbb{R}}\mathfrak{g}$. Choose a basis $(e_1,\dots,e_m)$ of the finite-dimensional space $\mathfrak{g}$. Then any $\alpha\in\Omega^p(M;\mathfrak{g})$ has a unique expansion
> > $$\alpha=\sum_{k=1}^{m}\alpha^{k}\otimes e_{k},\qquad \alpha^{k}\in\Omega^p(M),$$
> > because $\{e_k\}$ is a basis and tensoring $\Omega^p(M)$ with $\mathfrak{g}$ over $\mathbb{R}$ produces exactly the direct sum of $m$ copies of $\Omega^p(M)$, indexed by the basis. In particular $\alpha$ is a finite sum of the decomposables $\alpha^k\otimes e_k$.
> >
> > **Multilinear maps are determined on decomposables.** Consider, for definiteness, a map $T$ of two arguments that is $\mathbb{R}$-linear in each. For $\alpha=\sum_i a_i\otimes\xi_i$ and $\beta=\sum_j b_j\otimes\eta_j$ (finite sums of decomposables),
> > $$T(\alpha,\beta)=T\Big(\sum_i a_i\otimes\xi_i,\ \sum_j b_j\otimes\eta_j\Big)=\sum_{i,j}T(a_i\otimes\xi_i,\ b_j\otimes\eta_j)\qquad(\text{by }\mathbb{R}\text{-linearity in each argument}).$$
> > The same expansion holds for $T'$. If $T$ and $T'$ agree on every decomposable pair, then term by term $T(a_i\otimes\xi_i,b_j\otimes\eta_j)=T'(a_i\otimes\xi_i,b_j\otimes\eta_j)$, and summing gives $T(\alpha,\beta)=T'(\alpha,\beta)$. The argument is identical with one or three arguments, using linearity in each slot in turn.
> >
> > **Application to the identities.** In each of (a)–(d), the left-hand side and the right-hand side are, as functions of $(\alpha,\beta)$ or $(\alpha,\beta,\gamma)$, built from the operations $[\,\cdot\wedge\cdot\,]$, the matrix wedge, and $d$, each of which is $\mathbb{R}$-linear in each argument (the brackets by their bilinear definition; $d$ by $\mathbb{R}$-linearity of the exterior derivative). Hence both sides are $\mathbb{R}$-multilinear, and by the previous paragraph they agree everywhere once they agree on decomposables.

> [!note]- Lemma 2: Graded Leibniz rule for the ordinary exterior derivative
> **Statement:** For real-valued forms $a\in\Omega^p(M)$ and $b\in\Omega^q(M)$,
> $$d(a\wedge b)=da\wedge b+(-1)^{p}\,a\wedge db.$$
>
> **Hint:** Work in a chart; expand $a$ and $b$ in the basic forms $dx^I$; use the coordinate formula for $d$, the product rule for the differential of a function, and move a $1$-form past a $p$-form.
>
> **Why needed:** Part (b) of the theorem reduces, on decomposables, to exactly this identity tensored with the constant bracket $[\xi,\eta]$. The vault's axiomatic page for $d$ is not proof-complete, so the rule is proved here from the coordinate expression, which is.
>
> > [!note]- Full proof
> > The identity is local — both sides are forms, and two forms are equal if and only if they are equal in every chart — so it suffices to prove it in a fixed smooth chart $(U,x^1,\dots,x^n)$. Write
> > $$a=\sum\nolimits'_{I}a_I\,dx^I,\qquad b=\sum\nolimits'_{J}b_J\,dx^J,$$
> > where $I$ ranges over increasing multi-indices of length $p$, $J$ over increasing multi-indices of length $q$, $a_I,b_J\in C^\infty(U)$, and $dx^I=dx^{i_1}\wedge\cdots\wedge dx^{i_p}$. By $\mathbb{R}$-bilinearity of the wedge and $\mathbb{R}$-linearity of $d$ it suffices to treat a single pair of terms $a=a_I\,dx^I$, $b=b_J\,dx^J$.
> >
> > **The differential of a function-product.** For $f,g\in C^\infty(U)$ and any smooth vector field $X$, the differential satisfies $(d(fg))(X)=X(fg)=f\,X(g)+g\,X(f)=(f\,dg+g\,df)(X)$, using that $X$ acts as a derivation on the product of functions and that $(dh)(X)=X(h)$ for a function $h$. As this holds for every $X$, we obtain the product rule for $0$-forms,
> > $$d(fg)=f\,dg+g\,df.\qquad(\ast)$$
> >
> > **Apply the coordinate formula.** By the [[Thm - Coordinate Expression for the Exterior Derivative|coordinate expression for the exterior derivative]] — for $\omega=\sum'_K\omega_K\,dx^K$ one has $d\omega=\sum'_K d\omega_K\wedge dx^K$ — and using $a\wedge b=(a_Ib_J)\,dx^I\wedge dx^J$,
> > $$d(a\wedge b)=d\big((a_Ib_J)\,dx^I\wedge dx^J\big)=d(a_Ib_J)\wedge dx^I\wedge dx^J\qquad(\text{coordinate formula, }dx^I\wedge dx^J\text{ a basic form}).$$
> > By the product rule $(\ast)$, $d(a_Ib_J)=b_J\,da_I+a_I\,db_J$, so
> > $$d(a\wedge b)=(b_J\,da_I)\wedge dx^I\wedge dx^J+(a_I\,db_J)\wedge dx^I\wedge dx^J.\qquad(\dagger)$$
> >
> > **First summand.** Since $b_J$ is a function it commutes with wedging, and $dx^I\wedge dx^J$ regroups by associativity of the wedge:
> > $$(b_J\,da_I)\wedge dx^I\wedge dx^J=(da_I\wedge dx^I)\wedge(b_J\,dx^J)=da\wedge b\qquad(\text{associativity of }\wedge;\ da=da_I\wedge dx^I,\ b=b_J\,dx^J).$$
> >
> > **Second summand.** The factor $da_I$ is absent; we must move the $1$-form $db_J$ past the $p$-form $dx^I$. By graded-anticommutativity of the wedge (part (c) of [[Thm - Wedge Product Properties|the wedge product properties]]: $u\wedge v=(-1)^{(\deg u)(\deg v)}v\wedge u$), a $1$-form past a $p$-form costs $(-1)^{p\cdot1}=(-1)^p$:
> > $$db_J\wedge dx^I=(-1)^{p}\,dx^I\wedge db_J.$$
> > Therefore, moving the scalar $a_I$ freely,
> > $$(a_I\,db_J)\wedge dx^I\wedge dx^J=a_I\,(db_J\wedge dx^I)\wedge dx^J=(-1)^{p}\,a_I\,dx^I\wedge db_J\wedge dx^J=(-1)^{p}\,(a_I\,dx^I)\wedge(db_J\wedge dx^J)=(-1)^{p}\,a\wedge db,$$
> > using $db=db_J\wedge dx^J$ (coordinate formula applied to $b$) at the last step.
> >
> > **Combine.** Substituting the two summands into $(\dagger)$,
> > $$d(a\wedge b)=da\wedge b+(-1)^{p}\,a\wedge db.$$
> > This proves the rule for a single term-pair; $\mathbb{R}$-bilinearity extends it to all $a,b$, and locality extends it to all of $M$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\alpha\in\Omega^p(M;\mathfrak{g})$, $\beta\in\Omega^q(M;\mathfrak{g})$, $\gamma\in\Omega^r(M;\mathfrak{g})$. By **Lemma 1**, each of the four identities is $\mathbb{R}$-multilinear in its arguments, so it suffices to verify each on decomposable forms
> $$\alpha=a\otimes\xi,\qquad \beta=b\otimes\eta,\qquad \gamma=c\otimes\zeta,$$
> with $a\in\Omega^p(M)$, $b\in\Omega^q(M)$, $c\in\Omega^r(M)$ and $\xi,\eta,\zeta\in\mathfrak{g}$. Throughout we use, from the [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|definition of the bracket]], the decomposable rule $[(a\otimes\xi)\wedge(b\otimes\eta)]=(a\wedge b)\otimes[\xi,\eta]$; from [[Thm - Wedge Product Properties|the wedge product properties]], graded-anticommutativity $u\wedge v=(-1)^{(\deg u)(\deg v)}v\wedge u$ and associativity of $\wedge$; and from the [[Def - Lie Algebra|Lie-algebra axioms]], antisymmetry $[\xi,\eta]=-[\eta,\xi]$ and the Jacobi identity $[\xi,[\eta,\zeta]]+[\eta,[\zeta,\xi]]+[\zeta,[\xi,\eta]]=0$.
>
> **Part (a) — graded antisymmetry.** We must show $[\alpha\wedge\beta]=-(-1)^{pq}[\beta\wedge\alpha]$. On decomposables,
> $$[\beta\wedge\alpha]=(b\wedge a)\otimes[\eta,\xi]\qquad(\text{decomposable rule for the bracket}).$$
> Now $b\wedge a=(-1)^{qp}\,a\wedge b=(-1)^{pq}\,a\wedge b$ (graded-anticommutativity of $\wedge$, with $\deg b=q$, $\deg a=p$), and $[\eta,\xi]=-[\xi,\eta]$ (antisymmetry of the Lie bracket). Substituting,
> $$[\beta\wedge\alpha]=(-1)^{pq}(a\wedge b)\otimes(-[\xi,\eta])=-(-1)^{pq}\,(a\wedge b)\otimes[\xi,\eta]=-(-1)^{pq}\,[\alpha\wedge\beta].$$
> Multiplying both sides by $-(-1)^{pq}$ and using $(-1)^{2pq}=1$ gives $[\alpha\wedge\beta]=-(-1)^{pq}[\beta\wedge\alpha]$, as required.
>
> **Part (b) — graded Leibniz rule.** We must show $d[\alpha\wedge\beta]=[d\alpha\wedge\beta]+(-1)^p[\alpha\wedge d\beta]$. Since $\xi,\eta$ are constant elements of $\mathfrak{g}$, the exterior derivative acts only on the form factor: $d(a\otimes\xi)=da\otimes\xi$. Hence
> $$d[\alpha\wedge\beta]=d\big((a\wedge b)\otimes[\xi,\eta]\big)=\big(d(a\wedge b)\big)\otimes[\xi,\eta]\qquad(d\text{ acts componentwise};\ [\xi,\eta]\text{ constant}).$$
> By **Lemma 2**, $d(a\wedge b)=da\wedge b+(-1)^p\,a\wedge db$, so
> $$d[\alpha\wedge\beta]=(da\wedge b)\otimes[\xi,\eta]+(-1)^p\,(a\wedge db)\otimes[\xi,\eta]\qquad(\text{Lemma 2, then distribute }\otimes[\xi,\eta]).$$
> Reading the two summands back through the decomposable rule, with $d\alpha=da\otimes\xi$ and $d\beta=db\otimes\eta$,
> $$(da\wedge b)\otimes[\xi,\eta]=[(da\otimes\xi)\wedge(b\otimes\eta)]=[d\alpha\wedge\beta],\qquad (a\wedge db)\otimes[\xi,\eta]=[(a\otimes\xi)\wedge(db\otimes\eta)]=[\alpha\wedge d\beta].$$
> Therefore $d[\alpha\wedge\beta]=[d\alpha\wedge\beta]+(-1)^p[\alpha\wedge d\beta]$.
>
> **Part (c) — graded Jacobi identity.** We must show the cyclic sum $S:=(-1)^{pr}[\alpha\wedge[\beta\wedge\gamma]]+(-1)^{pq}[\beta\wedge[\gamma\wedge\alpha]]+(-1)^{qr}[\gamma\wedge[\alpha\wedge\beta]]$ vanishes.
>
> *Step 1 — expand each term on decomposables.* Applying the decomposable rule twice (first to the inner bracket, then to the outer),
> $$[\alpha\wedge[\beta\wedge\gamma]]=(a\wedge b\wedge c)\otimes[\xi,[\eta,\zeta]],$$
> $$[\beta\wedge[\gamma\wedge\alpha]]=(b\wedge c\wedge a)\otimes[\eta,[\zeta,\xi]],$$
> $$[\gamma\wedge[\alpha\wedge\beta]]=(c\wedge a\wedge b)\otimes[\zeta,[\xi,\eta]].$$
>
> *Step 2 — reorder the form parts.* By graded-anticommutativity of $\wedge$ applied twice (moving the degree-$p$ factor $a$ from the tail to the head past $c$ and $b$, of total degree $q+r$; and moving the degree-$r$ factor $c$ from the head to the tail past $a$ and $b$, of total degree $p+q$),
> $$b\wedge c\wedge a=(-1)^{p(q+r)}\,a\wedge b\wedge c,\qquad c\wedge a\wedge b=(-1)^{r(p+q)}\,a\wedge b\wedge c.$$
>
> *Step 3 — collect the sign of each term.* Insert Step 2 into Step 1 and multiply by the prefactors of $S$:
> $$(-1)^{pr}[\alpha\wedge[\beta\wedge\gamma]]=(-1)^{pr}\,(a\wedge b\wedge c)\otimes[\xi,[\eta,\zeta]],$$
> $$(-1)^{pq}[\beta\wedge[\gamma\wedge\alpha]]=(-1)^{pq}(-1)^{p(q+r)}\,(a\wedge b\wedge c)\otimes[\eta,[\zeta,\xi]]=(-1)^{pr}\,(a\wedge b\wedge c)\otimes[\eta,[\zeta,\xi]],$$
> $$(-1)^{qr}[\gamma\wedge[\alpha\wedge\beta]]=(-1)^{qr}(-1)^{r(p+q)}\,(a\wedge b\wedge c)\otimes[\zeta,[\xi,\eta]]=(-1)^{pr}\,(a\wedge b\wedge c)\otimes[\zeta,[\xi,\eta]],$$
> where in the second line $(-1)^{pq+pq+pr}=(-1)^{2pq}(-1)^{pr}=(-1)^{pr}$ (since $(-1)^{2pq}=1$), and in the third line $(-1)^{qr+rp+rq}=(-1)^{2qr}(-1)^{pr}=(-1)^{pr}$.
>
> *Step 4 — apply the Jacobi identity of $\mathfrak{g}$.* All three terms share the common form factor $(-1)^{pr}(a\wedge b\wedge c)$, so
> $$S=(-1)^{pr}\,(a\wedge b\wedge c)\otimes\Big([\xi,[\eta,\zeta]]+[\eta,[\zeta,\xi]]+[\zeta,[\xi,\eta]]\Big)=(-1)^{pr}\,(a\wedge b\wedge c)\otimes 0=0,$$
> the middle bracketed sum vanishing by the Jacobi identity of $\mathfrak{g}$. Hence $S=0$.
>
> *The $1$-form specialisation.* Take $\alpha=\beta=\gamma=A$ with $A\in\Omega^1(M;\mathfrak{g})$, so $p=q=r=1$. Each prefactor is $(-1)^{1}=-1$ and each of the three bracket terms equals $[A\wedge[A\wedge A]]$, so $S=-3\,[A\wedge[A\wedge A]]$. Since $S=0$ and $3\ne0$ in $\mathbb{R}$ (or $\mathbb{C}$),
> $$[A\wedge[A\wedge A]]=0.$$
>
> **Part (d) — matrix form.** Let $\mathfrak{g}\subseteq\mathfrak{gl}(n,\mathbb{K})$ be a matrix Lie algebra, so $[\xi,\eta]=\xi\eta-\eta\xi$ (commutator). On decomposables, using $[\xi,\eta]=\xi\eta-\eta\xi$ in the decomposable rule,
> $$[\alpha\wedge\beta]=(a\wedge b)\otimes[\xi,\eta]=(a\wedge b)\otimes(\xi\eta)-(a\wedge b)\otimes(\eta\xi).$$
> The first summand is, by definition of the matrix wedge, $(a\otimes\xi)\wedge(b\otimes\eta)=\alpha\wedge\beta$. For the second, the matrix wedge in the opposite order is $\beta\wedge\alpha=(b\wedge a)\otimes(\eta\xi)$; applying graded-anticommutativity $b\wedge a=(-1)^{pq}a\wedge b$,
> $$(-1)^{pq}\,\beta\wedge\alpha=(-1)^{pq}(b\wedge a)\otimes(\eta\xi)=(-1)^{pq}(-1)^{pq}(a\wedge b)\otimes(\eta\xi)=(a\wedge b)\otimes(\eta\xi),$$
> using $(-1)^{2pq}=1$. Therefore
> $$[\alpha\wedge\beta]=(a\wedge b)\otimes(\xi\eta)-(a\wedge b)\otimes(\eta\xi)=\alpha\wedge\beta-(-1)^{pq}\,\beta\wedge\alpha.$$
> Specialising to $1$-forms $A,B$ ($p=q=1$): $[A\wedge B]=A\wedge B-(-1)^{1}\,B\wedge A=A\wedge B+B\wedge A$, and with $B=A$, $[A\wedge A]=A\wedge A+A\wedge A=2\,A\wedge A$.
>
> All four identities hold on decomposables; by **Lemma 1** they hold for all $\mathfrak{g}$-valued forms. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Maurer–Cartan equation and its self-consistency (Lie theory).** On a Lie group $G$ the left-invariant Maurer–Cartan form obeys $d\theta+\tfrac12[\theta\wedge\theta]=0$. Differentiate this equation: $0=d(d\theta)+\tfrac12 d[\theta\wedge\theta]$, and by the Leibniz rule (b) with $p=q=1$ together with the symmetry of the $1$-form bracket from (a), $d[\theta\wedge\theta]=2[d\theta\wedge\theta]$. Substituting $d\theta=-\tfrac12[\theta\wedge\theta]$ gives $-[[\theta\wedge\theta]\wedge\theta]$, and this vanishes by the Jacobi identity (c) in the form $[\theta\wedge[\theta\wedge\theta]]=0$. The theorem applies because $\theta$ is a $\mathfrak{g}$-valued $1$-form; the point that is non-obvious is that differentiating an identity that already holds returns $0=0$ only because the cubic Jacobi term vanishes — the consistency is not automatic but a consequence of (c).

**Chern–Simons and the trace of a cube (topology of gauge fields).** The Chern–Simons $3$-form of a gauge potential $A$ contains the term $\tfrac13\operatorname{tr}(A\wedge[A\wedge A])$ (equivalently $\operatorname{tr}(A\wedge A\wedge A)$ up to a constant, using the matrix identity (d)). Computing its exterior derivative requires the Leibniz rule (b) applied to a bracket of $\mathfrak{g}$-valued forms and the invariance $\operatorname{tr}[\xi,\eta]=0$ of the trace. The theorem applies because the integrand is assembled entirely from brackets and matrix wedges of $A$; the non-obvious ingredient is that the $\operatorname{tr}$ of the triple product is totally symmetric only after the Jacobi and antisymmetry identities are used to reorder factors.

**Deformations of flat connections and the graded Lie algebra of forms (deformation theory).** The space $\Omega^\bullet(M;\mathfrak{g})$ with the bracket $[\,\cdot\wedge\cdot\,]$ and differential $d$ is a differential graded Lie algebra, and the flatness condition $dA+\tfrac12[A\wedge A]=0$ is its Maurer–Cartan equation. First-order deformations $A+t\,a$ preserving flatness are governed by the linearised operator $d_A a=da+[A\wedge a]$, whose square is $d_A^2 a=[F_A\wedge a]$; the identities (a),(b),(c) are exactly what make $d_A^2=0$ when $F_A=0$ and make the deformation complex a genuine complex. The theorem applies because every operator in sight is built from the graded bracket; the subtlety is that the sign conventions in (a)–(c) are precisely those of a graded Lie algebra, so the abstract deformation machinery transfers without modification.

---

# Bridges

- **[[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]]** — the object this theorem is about. That page constructs $\Omega^p(M;\mathfrak{g})$, defines the graded bracket on decomposables and checks it agrees with the pointwise formula for $1$-forms, and defines the matrix wedge; this page proves the four algebraic laws those constructions must obey. Together they make $(\Omega^\bullet(M;\mathfrak{g}),[\,\cdot\wedge\cdot\,],d)$ a differential graded Lie algebra.

- **[[Thm - Wedge Product Properties]]** — the ordinary-form input. Graded-anticommutativity $u\wedge v=(-1)^{(\deg u)(\deg v)}v\wedge u$ and associativity of the ordinary wedge are used at every reordering step; the construction here is nothing more than tensoring those laws in the form slot with the Lie-bracket laws in the algebra slot.

- **[[Thm - Coordinate Expression for the Exterior Derivative]]** — supplies the local formula $d(\sum'_I\omega_I\,dx^I)=\sum'_I d\omega_I\wedge dx^I$ from which the graded Leibniz rule for the ordinary $d$ (Lemma 2) is derived; that rule, tensored with the constant bracket, is exactly part (b).

- **[[Thm - Structure Equation for the Curvature]]** — the first consumer. The structure equation $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$, and its local form $F_A=dA+\tfrac12[A\wedge A]$, are manipulated using (a),(b),(d); part (d) is what turns the bracket normalisation $\tfrac12[A\wedge A]$ into the matrix expression $A\wedge A$, explaining why Haydys' matrix formula carries no factor $\tfrac12$.

- **[[Thm - Bianchi Identity for a Principal Connection]]** — the theorem whose proof this page's identities were built to serve. Differentiating the structure equation and cancelling with (a),(b) leaves a single cubic term, which vanishes by the Jacobi consequence $[A\wedge[A\wedge A]]=0$ from (c); the result is $dF_A+[A\wedge F_A]=0$.

---

# Unlocked by This

> [!tip] Differential Graded Lie Algebra *(from Homological Algebra / Deformation Theory)*
> With the bracket $[\,\cdot\wedge\cdot\,]$ (antisymmetric and Jacobi by (a),(c)) and the derivation $d$ (Leibniz by (b), squaring to zero), $\Omega^\bullet(M;\mathfrak{g})$ is a **differential graded Lie algebra**. The flatness equation $dA+\tfrac12[A\wedge A]=0$ is its Maurer–Cartan equation, and the deformation theory of flat connections is governed by its cohomology.

> [!tip] The Adjoint Bundle and Its Covariant Derivative *(from Gauge Theory)*
> Because the identities are natural in $\mathfrak{g}$, they carry over to forms valued in the adjoint bundle $\operatorname{ad}P$, where the fibrewise bracket makes $\Omega^\bullet(M;\operatorname{ad}P)$ a bundle of differential graded Lie algebras. The covariant exterior derivative $d^A=d+[A\wedge\,\cdot\,]$ then satisfies $(d^A)^2=[F_A\wedge\,\cdot\,]$, the bundle-valued shadow of the Bianchi identity.
