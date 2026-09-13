---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Bianchi Identity for a Principal Connection"
  - "Def - Curvature of a Principal Connection"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Work in a single trivialising chart, so that a connection on a principal $SU(2)$-bundle over $\mathbb{R}^4$ is recorded by its local gauge potential
$$A=A_\mu\,dx^\mu,\qquad A_\mu\colon\mathbb{R}^4\to\mathfrak{su}(2)\ \text{smooth},\ \mu=0,1,2,3,$$
where $\mathfrak{su}(2)=\{X\in\mathfrak{gl}_2(\mathbb{C}):X^\ast=-X,\ \operatorname{tr}X=0\}$ is the Lie algebra of $SU(2)$, the bracket $[X,Y]=XY-YX$ is the matrix commutator, and the summation convention is in force ($A_\mu\,dx^\mu:=\sum_{\mu=0}^3 A_\mu\,dx^\mu$). Define the **field strength components**
$$F_{\mu\nu}:=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]\in\mathfrak{su}(2),\qquad \partial_\mu:=\frac{\partial}{\partial x^\mu},$$
which are antisymmetric, $F_{\mu\nu}=-F_{\nu\mu}$, and assemble the curvature two-form $F=\tfrac12 F_{\mu\nu}\,dx^\mu\wedge dx^\nu$.

Introduce the **gauge-covariant derivative** of an $\mathfrak{su}(2)$-valued field $\Phi$ in the direction $\lambda$,
$$D_\lambda\Phi:=\partial_\lambda\Phi+[A_\lambda,\Phi].$$

**Prove, by direct computation in coordinates, the Bianchi identity**
$$\boxed{\ \sum_{\text{cyc}(\lambda\mu\nu)}\bigl(\partial_\lambda F_{\mu\nu}+[A_\lambda,F_{\mu\nu}]\bigr)=D_\lambda F_{\mu\nu}+D_\mu F_{\nu\lambda}+D_\nu F_{\lambda\mu}=0\ }$$
for every triple of indices $(\lambda,\mu,\nu)$, where $\sum_{\text{cyc}(\lambda\mu\nu)}$ denotes the cyclic sum over the three cyclic permutations $(\lambda,\mu,\nu)\to(\mu,\nu,\lambda)\to(\nu,\lambda,\mu)$.

This is the component form, for the concrete structure group $SU(2)$, of the coordinate-free Bianchi identity of the previous theorem page. The point of the exercise is to see that the abstract identity is, after all the intrinsic machinery is unwound, three elementary cancellations: the equality of mixed partial derivatives, the antisymmetry of the commutator, and the Jacobi identity — one for each of the three kinds of term that appear.

**Recall.** The identity we are verifying is the local, component rendering of the following theorem, whose intrinsic statement and complete proof live on its own page.

![[Thm - Bianchi Identity for a Principal Connection#Statement]]

In particular, part (c) of that theorem states that in a local gauge with potential $A_\alpha=s_\alpha^\ast\omega$ and local curvature form $F_\alpha=s_\alpha^\ast\Omega=dA_\alpha+\tfrac12[A_\alpha\wedge A_\alpha]$, the induced exterior covariant derivative annihilates the curvature:
$$dF_\alpha+[A_\alpha\wedge F_\alpha]=0.$$
Our task is to expand this equation of $\mathfrak{su}(2)$-valued three-forms into its coordinate components and check it by hand. The curvature two-form itself is defined intrinsically by:

![[Def - Curvature of a Principal Connection#The Definition]]

The bracket $[\,\cdot\wedge\cdot\,]$ of Lie-algebra-valued forms used here is the one fixed on its definition page: for a $\mathfrak{g}$-valued $p$-form $\alpha$ and $q$-form $\beta$ it is the unique bilinear form-valued bracket with $[\alpha\wedge\beta]=(\alpha\wedge\beta)\otimes[\xi,\eta]$ on decomposables $\alpha=a\otimes\xi$, $\beta=b\otimes\eta$.

![[Def - Lie-Algebra-Valued Differential Forms and Their Bracket#The Definition]]

For a matrix Lie algebra such as $\mathfrak{su}(2)$ the only algebraic facts about the bracket we shall use are the three that hold in **every** Lie algebra:

- **Bilinearity:** $[X,aY+bZ]=a[X,Y]+b[X,Z]$ and $[aX+bY,Z]=a[X,Z]+b[Y,Z]$ for scalars $a,b$;
- **Antisymmetry:** $[X,Y]=-[Y,X]$, in particular $[X,X]=0$;
- **Jacobi identity:** $[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0$.

For matrix commutators the Jacobi identity is a one-line consequence of the associativity of matrix multiplication, verified in the solution below, so the entire argument is self-contained.

---

# Convergent Strategy

**Problem class.** This is a *verify-an-identity-by-direct-expansion* problem: an intrinsic differential-geometric equation has been handed to us in coordinates, and we are asked to confirm it purely algebraically, without invoking the abstract proof. The characteristic feature of this class is that success comes not from a clever idea but from *bookkeeping discipline* — we expand every term, sort the resulting monomials into groups by their algebraic type, and show each group cancels on its own. The reward is that the abstract identity is demystified: we see exactly which elementary fact kills which family of terms.

**Assumption pattern.** Three standing facts drive the whole computation, and each is used exactly once, on exactly one family of terms. The smoothness of $A_\mu\colon\mathbb{R}^4\to\mathfrak{su}(2)$ delivers the **equality of mixed second partial derivatives** $\partial_\lambda\partial_\mu A_\nu=\partial_\mu\partial_\lambda A_\nu$ (Schwarz/Clairaut), which annihilates the terms built from two derivatives and no bracket. The **antisymmetry** of the commutator annihilates the terms built from one derivative and one bracket. The **Jacobi identity** of $\mathfrak{su}(2)$ annihilates the terms built from two brackets and no derivative. The recognisable trigger for this decomposition is that $F_{\mu\nu}$ is a sum of a *derivative part* $\partial_\mu A_\nu-\partial_\nu A_\mu$ and a *bracket part* $[A_\mu,A_\nu]$, and the operator $D_\lambda=\partial_\lambda+[A_\lambda,\cdot]$ is a sum of a *derivative part* and a *bracket part*; multiplying the two sums produces exactly the three homogeneous families.

**Theorem routing.** The route is: substitute the definition of $F_{\mu\nu}$ into $D_\lambda F_{\mu\nu}$; expand $D_\lambda F_{\mu\nu}=\partial_\lambda F_{\mu\nu}+[A_\lambda,F_{\mu\nu}]$ into seven monomials; sort the twenty-one monomials of the full cyclic sum into three families (two-derivative, mixed, two-bracket); cancel each family using, respectively, *equality of mixed partials*, *antisymmetry of the bracket*, and *the Jacobi identity*. No external theorem beyond these three elementary facts is needed; the coordinate-free theorem [[Thm - Bianchi Identity for a Principal Connection]] is what this computation reproves in components, not a tool the computation uses.

**Key decision point.** The one genuinely non-mechanical decision is *how to organise the twenty-one terms*. Attempting to cancel them in the order they arise is hopeless; the terms that cancel each other come from *different* cyclic summands and *different* halves of $D_\lambda$. The productive move is to sort by algebraic type first and only then look for cancellations within each type. A second, smaller decision is to keep the commutators unexpanded — never write $[A_\mu,A_\nu]=A_\mu A_\nu-A_\nu A_\mu$ in components — because the antisymmetry and Jacobi cancellations are transparent at the level of brackets and become opaque once the products are multiplied out.

---

# Legal Operations Used

This solution deploys the following legal operations. Because the chapter topic page has not yet been assembled, the operations are named descriptively; the orchestrator will reconcile the numbering with the topic page's Legal Operations section.

1. **Expand a covariant derivative into ordinary derivative plus bracket.** Apply $D_\lambda=\partial_\lambda+[A_\lambda,\,\cdot\,]$ to $F_{\mu\nu}$; this is the coordinate incarnation of the exterior covariant derivative $d^\nabla=d+[A\wedge\,\cdot\,]$ acting on an $\operatorname{ad}P$-valued form, restated in components.

2. **Substitute the definition of the field strength.** Replace $F_{\mu\nu}$ everywhere by $\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]$, so that every term is a monomial in $A$ and its first two derivatives.

3. **Distribute a bracket over a sum using bilinearity.** Use $[A_\lambda,\,X+Y\,]=[A_\lambda,X]+[A_\lambda,Y]$ to split $[A_\lambda,F_{\mu\nu}]$ into its three constituent brackets; likewise distribute inside $\partial_\lambda[A_\mu,A_\nu]$ via the Leibniz rule.

4. **Differentiate a bracket by the Leibniz rule.** Use $\partial_\lambda[A_\mu,A_\nu]=[\partial_\lambda A_\mu,A_\nu]+[A_\mu,\partial_\lambda A_\nu]$, valid because the bracket is bilinear with constant (index-independent) structure constants.

5. **Sort into homogeneous families and cancel each separately.** Group the twenty-one monomials by their algebraic type (two-derivative, one-derivative-one-bracket, two-bracket) and cancel each family using the single elementary fact appropriate to it.

6. **Cancel two-derivative terms by the equality of mixed partials.** Invoke $\partial_a\partial_b A_c=\partial_b\partial_a A_c$ (Schwarz's theorem, valid since each $A_c$ is smooth) to pair off and cancel the derivative-only terms.

7. **Cancel mixed terms by the antisymmetry of the commutator.** Use $[X,Y]=-[Y,X]$ to pair off and cancel the one-derivative-one-bracket terms.

8. **Cancel two-bracket terms by the Jacobi identity.** Recognise the cyclic sum of $[A_\lambda,[A_\mu,A_\nu]]$ as the left-hand side of the Jacobi identity for $\mathfrak{su}(2)$, hence zero.

---

# Hints

> [!note]- Hint 1
> Do not touch the abstract theorem. Everything is algebra in coordinates. Start by writing out $D_\lambda F_{\mu\nu}=\partial_\lambda F_{\mu\nu}+[A_\lambda,F_{\mu\nu}]$ with $F_{\mu\nu}$ replaced by its definition. Count the kinds of term you get: some have two derivatives of $A$ and no bracket, some have one derivative and one bracket, and some have two brackets and no derivative. These three families never mix, so you can treat them one at a time.

> [!note]- Hint 2
> The two-derivative terms are $\partial_\lambda\partial_\mu A_\nu-\partial_\lambda\partial_\nu A_\mu$ and its cyclic images. There are six of them. Write all six down and use that $A_\nu$ is a smooth function of $x$, so its mixed second partials commute. Each of the six pairs with exactly one other to cancel.

> [!note]- Hint 3
> The mixed terms come in two kinds: from $\partial_\lambda[A_\mu,A_\nu]$ (via the Leibniz rule) and from $[A_\lambda,\partial_\mu A_\nu-\partial_\nu A_\mu]$. Write out all twelve. Three of them cancel *between the two kinds* directly (same term with opposite sign). For the remaining six, you will need $[X,Y]=-[Y,X]$ to see the cancellation: a term $[\partial_\lambda A_\mu,A_\nu]$ equals $-[A_\nu,\partial_\lambda A_\mu]$, and that negative is sitting in another cyclic summand.

> [!note]- Hint 4
> The two-bracket terms are exactly $[A_\lambda,[A_\mu,A_\nu]]+[A_\mu,[A_\nu,A_\lambda]]+[A_\nu,[A_\lambda,A_\mu]]$. This *is* the Jacobi identity — read it against $[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0$ with $X=A_\lambda$, $Y=A_\mu$, $Z=A_\nu$. If you want the identity to be genuinely self-contained, prove Jacobi for matrix commutators by expanding each double commutator into its six triple products and watching all twelve cancel.

---

# Solution

The plan is to expand the cyclic sum completely, then partition its terms into three families that never interact: the terms with two derivatives and no bracket, the terms with one derivative and one bracket, and the terms with two brackets and no derivative. We show each family sums to zero on its own — the first by the equality of mixed partial derivatives, the second by the antisymmetry of the commutator, the third by the Jacobi identity. Because the three families exhaust every term and each vanishes separately, the whole cyclic sum vanishes.

**Step 1: Expand $D_\lambda F_{\mu\nu}$ into seven monomials.**

Substituting the definition of $F_{\mu\nu}$ and distributing gives $D_\lambda F_{\mu\nu}$ as a sum of two second-derivative terms, four one-derivative-one-bracket terms, and one two-bracket term.

> [!note]- Derivation
> By definition $D_\lambda F_{\mu\nu}=\partial_\lambda F_{\mu\nu}+[A_\lambda,F_{\mu\nu}]$ (operation 1). Substitute $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]$ (operation 2).
>
> First the derivative part. Differentiating term by term, and using the Leibniz rule $\partial_\lambda[A_\mu,A_\nu]=[\partial_\lambda A_\mu,A_\nu]+[A_\mu,\partial_\lambda A_\nu]$ (operation 4, valid because the bracket is bilinear with constant structure constants, so differentiation passes through it),
> $$\partial_\lambda F_{\mu\nu}=\underbrace{\partial_\lambda\partial_\mu A_\nu-\partial_\lambda\partial_\nu A_\mu}_{\text{two-derivative}}+\underbrace{[\partial_\lambda A_\mu,A_\nu]+[A_\mu,\partial_\lambda A_\nu]}_{\text{mixed}}\qquad\text{(term-by-term }\partial_\lambda\text{, Leibniz rule on the bracket).}$$
>
> Next the bracket part. Distributing $[A_\lambda,\,\cdot\,]$ over the three summands of $F_{\mu\nu}$ by bilinearity (operation 3),
> $$[A_\lambda,F_{\mu\nu}]=\underbrace{[A_\lambda,\partial_\mu A_\nu]-[A_\lambda,\partial_\nu A_\mu]}_{\text{mixed}}+\underbrace{[A_\lambda,[A_\mu,A_\nu]]}_{\text{two-bracket}}\qquad\text{(bilinearity of the bracket).}$$
>
> Adding the two lines, $D_\lambda F_{\mu\nu}$ is the sum of the two-derivative pair, four mixed terms, and one two-bracket term:
> $$D_\lambda F_{\mu\nu}=\bigl(\partial_\lambda\partial_\mu A_\nu-\partial_\lambda\partial_\nu A_\mu\bigr)+\bigl([\partial_\lambda A_\mu,A_\nu]+[A_\mu,\partial_\lambda A_\nu]+[A_\lambda,\partial_\mu A_\nu]-[A_\lambda,\partial_\nu A_\mu]\bigr)+[A_\lambda,[A_\mu,A_\nu]].$$

**Step 2: Cancel the two-derivative family by the equality of mixed partials.**

The six two-derivative terms produced by the cyclic sum cancel in pairs because each $A_c$ is smooth and hence has commuting second partial derivatives.

> [!note]- Derivation
> The two-derivative contribution to the cyclic sum is (operation 5, isolating the family)
> $$S_{\partial\partial}=\sum_{\text{cyc}(\lambda\mu\nu)}\bigl(\partial_\lambda\partial_\mu A_\nu-\partial_\lambda\partial_\nu A_\mu\bigr).$$
> Writing out the three cyclic summands explicitly,
> $$
> \begin{aligned}
> (\lambda\mu\nu):&\quad \partial_\lambda\partial_\mu A_\nu-\partial_\lambda\partial_\nu A_\mu,\\
> (\mu\nu\lambda):&\quad \partial_\mu\partial_\nu A_\lambda-\partial_\mu\partial_\lambda A_\nu,\\
> (\nu\lambda\mu):&\quad \partial_\nu\partial_\lambda A_\mu-\partial_\nu\partial_\mu A_\lambda.
> \end{aligned}
> $$
> Because each component $A_c\colon\mathbb{R}^4\to\mathfrak{su}(2)$ is smooth, Schwarz's theorem gives $\partial_a\partial_b A_c=\partial_b\partial_a A_c$ (operation 6). Apply it to pair the terms:
> $$\partial_\lambda\partial_\mu A_\nu-\partial_\mu\partial_\lambda A_\nu=0\quad(\text{first term of row }1,\ \text{last term of row }2),$$
> $$-\partial_\lambda\partial_\nu A_\mu+\partial_\nu\partial_\lambda A_\mu=0\quad(\text{last term of row }1,\ \text{first term of row }3),$$
> $$\partial_\mu\partial_\nu A_\lambda-\partial_\nu\partial_\mu A_\lambda=0\quad(\text{first term of row }2,\ \text{last term of row }3).$$
> Every term appears in exactly one such pair, so $S_{\partial\partial}=0$.

**Step 3: Cancel the mixed family by the antisymmetry of the commutator.**

The twelve one-derivative-one-bracket terms cancel: three cancel directly between the two halves of $D$, and the remaining six cancel in pairs after applying $[X,Y]=-[Y,X]$.

> [!note]- Derivation
> The mixed contribution to the cyclic sum is
> $$S_{\partial[\,]}=\sum_{\text{cyc}(\lambda\mu\nu)}\Bigl([\partial_\lambda A_\mu,A_\nu]+[A_\mu,\partial_\lambda A_\nu]+[A_\lambda,\partial_\mu A_\nu]-[A_\lambda,\partial_\nu A_\mu]\Bigr).$$
> Writing out the three cyclic summands and labelling the twelve terms:
> $$
> \begin{aligned}
> (\lambda\mu\nu):&\quad \underbrace{[\partial_\lambda A_\mu,A_\nu]}_{1}+\underbrace{[A_\mu,\partial_\lambda A_\nu]}_{2}+\underbrace{[A_\lambda,\partial_\mu A_\nu]}_{3}-\underbrace{[A_\lambda,\partial_\nu A_\mu]}_{4},\\
> (\mu\nu\lambda):&\quad \underbrace{[\partial_\mu A_\nu,A_\lambda]}_{5}+\underbrace{[A_\nu,\partial_\mu A_\lambda]}_{6}+\underbrace{[A_\mu,\partial_\nu A_\lambda]}_{7}-\underbrace{[A_\mu,\partial_\lambda A_\nu]}_{8},\\
> (\nu\lambda\mu):&\quad \underbrace{[\partial_\nu A_\lambda,A_\mu]}_{9}+\underbrace{[A_\lambda,\partial_\nu A_\mu]}_{10}+\underbrace{[A_\nu,\partial_\lambda A_\mu]}_{11}-\underbrace{[A_\nu,\partial_\mu A_\lambda]}_{12}.
> \end{aligned}
> $$
> *Direct cancellations (no antisymmetry needed).* Terms $2$ and $8$ are $[A_\mu,\partial_\lambda A_\nu]$ and $-[A_\mu,\partial_\lambda A_\nu]$: they cancel. Terms $4$ and $10$ are $-[A_\lambda,\partial_\nu A_\mu]$ and $+[A_\lambda,\partial_\nu A_\mu]$: they cancel. Terms $6$ and $12$ are $[A_\nu,\partial_\mu A_\lambda]$ and $-[A_\nu,\partial_\mu A_\lambda]$: they cancel.
>
> *Antisymmetric cancellations.* The six survivors are $1,3,5,7,9,11$. Apply $[X,Y]=-[Y,X]$ (operation 7):
> $$\text{term }3=[A_\lambda,\partial_\mu A_\nu]=-[\partial_\mu A_\nu,A_\lambda]=-(\text{term }5),$$
> $$\text{term }7=[A_\mu,\partial_\nu A_\lambda]=-[\partial_\nu A_\lambda,A_\mu]=-(\text{term }9),$$
> $$\text{term }11=[A_\nu,\partial_\lambda A_\mu]=-[\partial_\lambda A_\mu,A_\nu]=-(\text{term }1).$$
> Thus $3+5=0$, $7+9=0$, and $11+1=0$. Every one of the twelve terms lies in exactly one cancelling pair, so $S_{\partial[\,]}=0$.

**Step 4: Cancel the two-bracket family by the Jacobi identity.**

The three two-bracket terms are precisely the left-hand side of the Jacobi identity for $\mathfrak{su}(2)$, hence sum to zero.

> [!note]- Derivation
> The two-bracket contribution to the cyclic sum is
> $$S_{[\,][\,]}=\sum_{\text{cyc}(\lambda\mu\nu)}[A_\lambda,[A_\mu,A_\nu]]=[A_\lambda,[A_\mu,A_\nu]]+[A_\mu,[A_\nu,A_\lambda]]+[A_\nu,[A_\lambda,A_\mu]].$$
> This is exactly the left-hand side of the **Jacobi identity** $[X,[Y,Z]]+[Y,[Z,X]]+[Z,[X,Y]]=0$ with $X=A_\lambda$, $Y=A_\mu$, $Z=A_\nu$ (operation 8), so $S_{[\,][\,]}=0$.
>
> For completeness we verify Jacobi for matrix commutators, which is all $\mathfrak{su}(2)$ requires. For matrices $X,Y,Z$ with $[X,Y]=XY-YX$, expand each double commutator into six triple products:
> $$[X,[Y,Z]]=XYZ-XZY-YZX+ZYX,$$
> $$[Y,[Z,X]]=YZX-YXZ-ZXY+XZY,$$
> $$[Z,[X,Y]]=ZXY-ZYX-XYZ+YXZ.$$
> Adding the three lines, each of the twelve triple products appears once with a plus sign and once with a minus sign — $XYZ$ in row $1$ against $-XYZ$ in row $3$, $-XZY$ in row $1$ against $+XZY$ in row $2$, and so on — so the sum is $0$. (Associativity of matrix multiplication is what lets us write each product without parentheses.) Hence $S_{[\,][\,]}=0$.

**Step 5: Assemble.**

The full cyclic sum is $S_{\partial\partial}+S_{\partial[\,]}+S_{[\,][\,]}$, and each summand is zero.

> [!note]- Derivation
> By Step 1, the cyclic sum decomposes as
> $$\sum_{\text{cyc}(\lambda\mu\nu)}D_\lambda F_{\mu\nu}=S_{\partial\partial}+S_{\partial[\,]}+S_{[\,][\,]}$$
> because the three families exhaust the terms of $D_\lambda F_{\mu\nu}$ and cyclic summation preserves the partition. By Step 2, $S_{\partial\partial}=0$; by Step 3, $S_{\partial[\,]}=0$; by Step 4, $S_{[\,][\,]}=0$. Therefore the sum is $0$.

> [!note]- Complete formal solution
> **Claim.** For $A=A_\mu\,dx^\mu$ with $A_\mu\colon\mathbb{R}^4\to\mathfrak{su}(2)$ smooth and $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu+[A_\mu,A_\nu]$, the identity $\sum_{\text{cyc}(\lambda\mu\nu)}\bigl(\partial_\lambda F_{\mu\nu}+[A_\lambda,F_{\mu\nu}]\bigr)=0$ holds for every triple $(\lambda,\mu,\nu)$.
>
> Write $D_\lambda F_{\mu\nu}=\partial_\lambda F_{\mu\nu}+[A_\lambda,F_{\mu\nu}]$. Substituting the definition of $F_{\mu\nu}$ and using the Leibniz rule for $\partial_\lambda$ on the bracket (bilinearity with constant structure constants) and the bilinearity of $[A_\lambda,\,\cdot\,]$,
> $$D_\lambda F_{\mu\nu}=\bigl(\partial_\lambda\partial_\mu A_\nu-\partial_\lambda\partial_\nu A_\mu\bigr)+\bigl([\partial_\lambda A_\mu,A_\nu]+[A_\mu,\partial_\lambda A_\nu]+[A_\lambda,\partial_\mu A_\nu]-[A_\lambda,\partial_\nu A_\mu]\bigr)+[A_\lambda,[A_\mu,A_\nu]].$$
> Summing cyclically over $(\lambda,\mu,\nu)$ and separating the three homogeneous families gives $\sum_{\text{cyc}}D_\lambda F_{\mu\nu}=S_{\partial\partial}+S_{\partial[\,]}+S_{[\,][\,]}$, where:
>
> - $S_{\partial\partial}=\sum_{\text{cyc}}(\partial_\lambda\partial_\mu A_\nu-\partial_\lambda\partial_\nu A_\mu)=0$: each of the six terms cancels against another under the equality of mixed partials $\partial_a\partial_b A_c=\partial_b\partial_a A_c$ (Schwarz's theorem, valid since $A_c$ is smooth), the pairs being $(\partial_\lambda\partial_\mu A_\nu,-\partial_\mu\partial_\lambda A_\nu)$, $(-\partial_\lambda\partial_\nu A_\mu,\partial_\nu\partial_\lambda A_\mu)$, $(\partial_\mu\partial_\nu A_\lambda,-\partial_\nu\partial_\mu A_\lambda)$.
> - $S_{\partial[\,]}=0$: of the twelve one-derivative-one-bracket terms, three cancel directly ($[A_\mu,\partial_\lambda A_\nu]$ from $\partial_\lambda F_{\mu\nu}$ against $-[A_\mu,\partial_\lambda A_\nu]$ from $[A_\mu,F_{\nu\lambda}]$, and cyclically), and the remaining six cancel in pairs after $[X,Y]=-[Y,X]$: $[A_\lambda,\partial_\mu A_\nu]=-[\partial_\mu A_\nu,A_\lambda]$ and cyclically.
> - $S_{[\,][\,]}=[A_\lambda,[A_\mu,A_\nu]]+[A_\mu,[A_\nu,A_\lambda]]+[A_\nu,[A_\lambda,A_\mu]]=0$ by the Jacobi identity of $\mathfrak{su}(2)$, which for matrix commutators follows by expanding the three double commutators into twelve triple products that cancel in plus/minus pairs.
>
> Since each of $S_{\partial\partial},S_{\partial[\,]},S_{[\,][\,]}$ vanishes, so does their sum. Therefore $\sum_{\text{cyc}(\lambda\mu\nu)}\bigl(\partial_\lambda F_{\mu\nu}+[A_\lambda,F_{\mu\nu}]\bigr)=0$. This is the component form of $dF_\alpha+[A_\alpha\wedge F_\alpha]=0$, i.e. of $d^{\nabla_\omega}F_\omega=0$, for the structure group $SU(2)$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: "the bracket terms cancel by antisymmetry too"
> It is tempting to try to dispose of the two-bracket family $S_{[\,][\,]}$ the same way as the mixed family, by antisymmetry alone. This fails: antisymmetry gives $[A_\mu,[A_\nu,A_\lambda]]=-[[A_\nu,A_\lambda],A_\mu]$, which merely reorders the *outer* bracket and produces no cancellation among the three cyclic terms. The three terms cancel only through the *Jacobi* identity, which is a statement about *nested* brackets and is genuinely independent of antisymmetry (a bilinear antisymmetric bracket need not satisfy Jacobi). This is why the two-bracket family is the one place where the Lie-algebra structure of $\mathfrak{su}(2)$ — not merely the vector-space structure with an antisymmetric product — is actually used.

> [!note]- Independent sanity check on the Jacobi step with explicit $\mathfrak{su}(2)$ generators
> Fix the standard basis $T_a=-\tfrac{i}{2}\sigma_a$ of $\mathfrak{su}(2)$, where $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices. From $\sigma_a\sigma_b=\delta_{ab}I+i\,\varepsilon_{abc}\sigma_c$ one gets $[\sigma_a,\sigma_b]=2i\,\varepsilon_{abc}\sigma_c$, hence
> $$[T_a,T_b]=\Bigl(-\tfrac{i}{2}\Bigr)^2[\sigma_a,\sigma_b]=-\tfrac14\cdot 2i\,\varepsilon_{abc}\sigma_c=-\tfrac{i}{2}\varepsilon_{abc}\sigma_c=\varepsilon_{abc}T_c,$$
> so the structure constants are the totally antisymmetric symbol $\varepsilon_{abc}$. The Jacobi combination on generators is then
> $$[T_a,[T_b,T_c]]+[T_b,[T_c,T_a]]+[T_c,[T_a,T_b]]=\bigl(\varepsilon_{bcd}\varepsilon_{ade}+\varepsilon_{cad}\varepsilon_{bde}+\varepsilon_{abd}\varepsilon_{cde}\bigr)T_e.$$
> Using $\varepsilon_{bcd}\varepsilon_{ade}=\delta_{be}\delta_{ac}-\delta_{ab}\delta_{ce}$ (contraction over $d$, from $\varepsilon_{dbc}\varepsilon_{dea}=\delta_{be}\delta_{ca}-\delta_{ba}\delta_{ce}$ after cyclically moving $d$ to the front of each symbol) and its two cyclic images under $a\to b\to c\to a$, the coefficient of $T_e$ is $(\delta_{be}\delta_{ac}-\delta_{ab}\delta_{ce})+(\delta_{ab}\delta_{ce}-\delta_{ae}\delta_{bc})+(\delta_{ae}\delta_{bc}-\delta_{be}\delta_{ac})$, in which each Kronecker product is immediately followed by its own negative (the sum telescopes), giving $0$. This confirms independently that the two-bracket family vanishes for $\mathfrak{su}(2)$, consistent with Step 4.

---

# Key Takeaways

**The abstract Bianchi identity is three elementary cancellations wearing one coat, and each cancellation is tied to one structural axiom.** The intrinsic statement $d^{\nabla}F=0$ compresses into a single line of exterior calculus what, in coordinates, is the vanishing of three independent families of terms. The two-derivative family vanishes because *partial derivatives commute*; the mixed family vanishes because *the bracket is antisymmetric*; the two-bracket family vanishes because *the bracket satisfies Jacobi*. The reusable principle is diagnostic: whenever an identity involving a covariant derivative $D=\partial+[A,\cdot]$ of a curvature-like object collapses to zero, look for exactly these three engines, one per algebraic type of term. The trigger condition is the presence of an operator that is a sum "derivative $+$ bracket" acting on an object that is itself a sum "derivative $+$ bracket": the product generates precisely the graded families, and each is killed by the axiom matching its type. This is the same bookkeeping that proves $d^2=0$ (two-derivative terms only, killed by commuting partials) and that proves the second Bianchi identity in Riemannian geometry (where the curvature tensor plays the role of $F$).

**Keep brackets unexpanded; the structure of the cancellation lives at the level of the Lie algebra, not the matrix entries.** A common and costly error is to expand $[A_\mu,A_\nu]=A_\mu A_\nu-A_\nu A_\mu$ into components at the start. Doing so replaces each bracket-bearing term among the twenty-one by two or more, multiplying the bookkeeping and, worse, disguising the antisymmetry and Jacobi cancellations behind a wall of triple products. The transferable diagnostic is that the *only* properties of $\mathfrak{su}(2)$ the identity uses are bilinearity, antisymmetry, and Jacobi — properties shared by every Lie algebra — so the concrete matrix realisation should be invoked only at the very end, as a sanity check, and never as the medium of the computation. The identity therefore holds verbatim for a potential valued in *any* matrix Lie algebra ($\mathfrak{u}(1)$, $\mathfrak{su}(n)$, $\mathfrak{so}(n)$, $\mathfrak{gl}_k$); the abelian case $\mathfrak{u}(1)$ is the special one in which the bracket vanishes identically, so the mixed and two-bracket families are empty and the identity reduces to $\sum_{\text{cyc}}\partial_\lambda F_{\mu\nu}=0$, i.e. the ordinary $dF=0$ of Maxwell theory.

**The Jacobi identity is the load-bearing axiom, and it is the one place the non-abelian nature of the theory is felt.** In the abelian ($U(1)$) theory the field strength is $F_{\mu\nu}=\partial_\mu A_\nu-\partial_\nu A_\mu$ and the Bianchi identity is the source-free half of Maxwell's equations, $\partial_{[\lambda}F_{\mu\nu]}=0$ — pure calculus, no algebra. The moment the group becomes non-abelian, the potential $A$ couples to itself through $[A_\mu,A_\nu]$, the curvature acquires a quadratic term, and the covariant derivative acquires its $[A_\lambda,\cdot]$ correction. That the identity still holds is not automatic: it requires the bracket to satisfy Jacobi. The lesson for spaced practice is to remember *which axiom does which job* — if, months from now, you reconstruct this computation and find a family that will not cancel, the family is almost certainly the two-bracket one, and the fix is to recognise the Jacobi identity rather than to search for an antisymmetry that is not there. Companion exercises to revisit alongside this one are [[Ex - Curvature of a Connection on a Trivial Bundle and the Abelian Case]], where the abelian collapse $F=dA$, $dF=0$ is made explicit, and [[Ex - The Bracket of Matrix-Valued 1-Forms is Twice the Wedge Square]], which supplies the wedge-versus-bracket dictionary that turns the coordinate-free $dF_\alpha+[A_\alpha\wedge F_\alpha]=0$ into the components used here.
