---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Chern-Weil Form of an Invariant Polynomial"
  - "Def - Ad-Invariant Polynomial"
  - "Def - Curvature of a Principal Connection"
  - "Thm - Bianchi Identity for a Principal Connection"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $P\to M$ be a principal $U(1)$-bundle over a smooth manifold $M$, equipped with a connection whose curvature descends to the form $F=F_{\omega}\in\Omega^{2}(M;\mathfrak{u}(1))$ on the base. Take the invariant polynomial of degree one
$$p=\tfrac{i}{2\pi}\operatorname{tr}\colon\mathfrak{u}(1)\to\mathbb{C}.$$
Show that its Chern–Weil form is the curvature itself up to the normalising constant,
$$p(F)=\tfrac{i}{2\pi}\,F,$$
and that this form is **real-valued** and **closed**; it is a representative of the first Chern class $c_{1}(P)\in H^{2}_{\mathrm{dR}}(M;\mathbb{R})$.

> [!warning] Convention: the normalising constant of $c_{1}$
> This series follows Haydys and writes the degree-one Chern polynomial with the factor $\tfrac{i}{2\pi}$, so that $c_{1}(P)=\big[\tfrac{i}{2\pi}\operatorname{tr}(F)\big]$ and, more generally, $c(E)=\det(1+\tfrac{i}{2\pi}F)$. Bär (Wernli's notes, Example 2.5.11) instead writes the same polynomial as $\lambda(A)=\tfrac{1}{2\pi i}\operatorname{tr}(A)$. These two constants are **not** equal: since $\tfrac{1}{i}=-i$,
> $$\tfrac{1}{2\pi i}=-\tfrac{i}{2\pi},$$
> so Bär's first Chern class is the *negative* of the series' first Chern class. Both conventions make $p(F)$ real (as we verify below), and the sign difference is a well-known convention split in the literature; every page in this series uses the $\tfrac{i}{2\pi}$ normalisation, and one converts a Bär computation by an overall sign. We record both forms of the polynomial and carry out the exercise in the series convention.

**Recall:**

The objects in play are the Chern–Weil form of an invariant polynomial, the trace as the degree-one invariant polynomial, the curvature of a principal connection, and the Bianchi identity.

![[Def - Chern-Weil Form of an Invariant Polynomial#The Definition]]

For a principal $G$-bundle $P\to M$ with connection $\omega$ and an $\operatorname{Ad}$-invariant polynomial $p\in I(G)$ of degree $d$, one evaluates $p$ on the curvature to obtain a basic, $G$-invariant $2d$-form on $P$, which descends to a form $p(F_{\omega})\in\Omega^{2d}(M)$ on the base. For $d=1$ this is $p(F_{\omega})=p\circ F_{\omega}$, the pointwise application of the linear functional $p\colon\mathfrak{g}\to\mathbb{C}$ to the $\mathfrak{g}$-valued $2$-form $F_{\omega}$.

![[Def - Ad-Invariant Polynomial#The Definition]]

The trace $\operatorname{tr}\colon\mathfrak{u}(1)\to\mathbb{C}$ is $\operatorname{Ad}$-invariant and homogeneous of degree one: $\operatorname{tr}(\operatorname{Ad}_{g}\xi)=\operatorname{tr}(g\xi g^{-1})=\operatorname{tr}(\xi)$ for all $g\in U(1)$ and $\xi\in\mathfrak{u}(1)$, so $\operatorname{tr}\in I\big(U(1)\big)$, and hence so is $p=\tfrac{i}{2\pi}\operatorname{tr}$. (For the abelian group $U(1)$ the adjoint action is trivial, $\operatorname{Ad}_{g}=\operatorname{id}$, so *every* polynomial on $\mathfrak{u}(1)$ is invariant; the trace is singled out only because it is the degree-one one.)

![[Def - Curvature of a Principal Connection#The Definition]]

The curvature of a principal $U(1)$-connection is $\mathfrak{u}(1)$-valued, and $\mathfrak{u}(1)=\{z\in\mathbb{C}:\bar z=-z\}=i\mathbb{R}$ is the purely imaginary line; thus $F_{\omega}\in\Omega^{2}(M;i\mathbb{R})$.

![[Thm - Bianchi Identity for a Principal Connection#Statement]]

The **Bianchi identity** states that the exterior covariant derivative of the curvature vanishes, $d^{\omega}\Omega=0$; in terms of a local connection form $A$ and local curvature $F_{A}$ it reads
$$dF_{A}+[A\wedge F_{A}]=0.$$

---

# Convergent Strategy

**Problem class.** This is a *specialise-and-verify* drill: a general construction (the Chern–Weil form of an invariant polynomial) is evaluated in the smallest possible case (the rank-one, abelian group $U(1)$), and one checks that it reduces to the object it is supposed to generalise (the curvature) and that the two properties every characteristic form must have — reality and closedness — hold transparently here. The recognisable shape is "compute the general definition in the base case and confirm it matches the hand-built prototype."

**Assumption pattern.** Two features of $U(1)$ do all the work. First, $U(1)$ is *rank one*: $\mathfrak{u}(1)$ is a one-dimensional space of $1\times 1$ matrices, so the trace is the identity map and "matrix of $2$-forms" is a single $2$-form. Second, $U(1)$ is *abelian*: its Lie algebra bracket is identically zero, so the quadratic term in the curvature and the correction term in the Bianchi identity both vanish. The trigger to notice is that abelianness collapses $dF_{A}+[A\wedge F_{A}]=0$ to $dF_{A}=0$, making closedness immediate.

**Theorem routing.** The route is short. Use [[Def - Chern-Weil Form of an Invariant Polynomial|the Chern–Weil construction]] to write $p(F)=\tfrac{i}{2\pi}\operatorname{tr}(F)$; use $\dim\mathfrak{u}(1)=1$ to reduce the trace to the identity, giving $\tfrac{i}{2\pi}F$; use $\mathfrak{u}(1)=i\mathbb{R}$ (from [[Def - Curvature of a Principal Connection|the curvature definition]]) to see the form is real; and use the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]] with the vanishing abelian bracket to see it is closed. Membership in $c_{1}(P)$ is then the definition of the first Chern class.

**Key decision point.** The only genuine decision is *how to prove closedness*. Two routes are available: (a) invoke the Bianchi identity, which for the abelian group loses its bracket term and hands closedness directly; or (b) argue locally that $F=dA$ (the abelian structure equation), so $dF=d\,dA=0$. Both are legitimate and we present route (a) as primary and (b) as a remark. The subtlety worth flagging is that reality of $\tfrac{i}{2\pi}F$ depends on $F$ being *imaginary*-valued — a factor of $i$ turning an imaginary form into a real one — which is exactly the reason the normalising constant carries an $i$.

---

# Legal Operations Used

This solution deploys the following legal operations (numbered as descriptive operations; the orchestrator will reconcile them with the [[Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional|topic page]]'s Legal Operations once written):

1. **Evaluate an invariant polynomial on a curvature.** Apply the linear functional $p\colon\mathfrak{g}\to\mathbb{C}$ pointwise to the $\mathfrak{g}$-valued curvature form, using the descent already established for the Chern–Weil form.

2. **Reduce a trace on a rank-one Lie algebra to the identity.** On $\mathfrak{u}(1)$, a matrix is a single complex scalar, so $\operatorname{tr}(\xi)=\xi$; the degree-one polynomial is therefore just a rescaling.

3. **Use the identification $\mathfrak{u}(1)=i\mathbb{R}$ to read off reality.** Write the curvature as $F=i\varphi$ with $\varphi$ a real $2$-form and multiply by the constant $\tfrac{i}{2\pi}$ to land in the real forms.

4. **Kill the bracket term with abelianness in the Bianchi identity.** For the abelian Lie algebra $\mathfrak{u}(1)$ the bracket $[\,\cdot\,,\cdot\,]$ is identically zero, so $dF_{A}+[A\wedge F_{A}]=0$ becomes $dF_{A}=0$.

---

# Hints

> [!note]- Hint 1
> How big is a matrix in $\mathfrak{u}(1)$? The group $U(1)$ consists of $1\times 1$ unitary matrices, so its Lie algebra is one-dimensional. What does $\operatorname{tr}$ do to a $1\times 1$ matrix?

> [!note]- Hint 2
> Reality: $\mathfrak{u}(1)=\{z\in\mathbb{C}:\bar z=-z\}$, the imaginary axis $i\mathbb{R}$. So the curvature is $F=i\varphi$ for a *real* $2$-form $\varphi$. Now compute $\tfrac{i}{2\pi}F$ and check whether it is real. Note the factor of $i$ is doing the work.

> [!note]- Hint 3
> Closedness: recall the Bianchi identity $dF_{A}+[A\wedge F_{A}]=0$. The Lie algebra $\mathfrak{u}(1)$ is *abelian*. What is $[A\wedge F_{A}]$ then, and what does the identity reduce to?

---

# Solution

The computation is a direct specialisation of the Chern–Weil construction to the abelian rank-one group. In one dimension the trace is the identity, so evaluating the degree-one polynomial on the curvature merely rescales it by $\tfrac{i}{2\pi}$; the factor of $i$ converts the imaginary-valued curvature into a real form, and the vanishing of the $U(1)$ bracket makes the Bianchi identity assert closedness outright.

**Step 1: In rank one the Chern–Weil form of $\tfrac{i}{2\pi}\operatorname{tr}$ is $\tfrac{i}{2\pi}F$.**

The invariant polynomial $p=\tfrac{i}{2\pi}\operatorname{tr}$ evaluated on the $U(1)$-curvature gives $p(F)=\tfrac{i}{2\pi}F$.

> [!note]- Derivation
> The group $U(1)=\{z\in\mathbb{C}:|z|=1\}$ is the group of $1\times 1$ unitary matrices, and its Lie algebra
> $$\mathfrak{u}(1)=\{\xi\in\mathbb{C}:\bar\xi=-\xi\}=i\mathbb{R}$$
> is one-dimensional, consisting of $1\times 1$ skew-Hermitian matrices, that is, purely imaginary numbers. On a $1\times 1$ matrix the **trace is the identity map**: $\operatorname{tr}(\xi)=\xi$ for $\xi\in\mathfrak{u}(1)$. Hence the degree-one polynomial acts as
> $$p(\xi)=\tfrac{i}{2\pi}\operatorname{tr}(\xi)=\tfrac{i}{2\pi}\,\xi\qquad(\xi\in\mathfrak{u}(1)).$$
> By the [[Def - Chern-Weil Form of an Invariant Polynomial|Chern–Weil construction]], for a degree-one invariant polynomial the associated form on the base is obtained by applying the linear functional $p$ pointwise to the descended curvature $F=F_{\omega}\in\Omega^{2}(M;\mathfrak{u}(1))$. Since $p$ is the linear map $\xi\mapsto\tfrac{i}{2\pi}\xi$, this pointwise application is
> $$p(F)=\tfrac{i}{2\pi}\operatorname{tr}(F)=\tfrac{i}{2\pi}\,F\qquad\text{(trace is the identity on }1\times 1\text{ matrices).}$$
> The curvature $F$ descends to a genuine form on $M$ by the Chern–Weil descent (its pullback $\pi^{*}p(F)=p(\pi^{*}F_{\omega})$ is basic and $U(1)$-invariant), so $p(F)=\tfrac{i}{2\pi}F$ is a well-defined $2$-form on $M$.

**Step 2: The form $\tfrac{i}{2\pi}F$ is real-valued.**

Although $F$ takes values in the imaginary line $i\mathbb{R}$, the constant $\tfrac{i}{2\pi}$ turns it into a real $2$-form.

> [!note]- Derivation
> By the [[Def - Curvature of a Principal Connection|curvature definition]] the curvature of a $U(1)$-connection is $\mathfrak{u}(1)$-valued, and $\mathfrak{u}(1)=i\mathbb{R}$. Write the curvature accordingly as
> $$F=i\,\varphi,\qquad \varphi\in\Omega^{2}(M;\mathbb{R})$$
> a *real* $2$-form $\varphi$ (this is possible precisely because $F$ is imaginary-valued). Then
> $$p(F)=\tfrac{i}{2\pi}\,F=\tfrac{i}{2\pi}\,(i\varphi)=\tfrac{i^{2}}{2\pi}\,\varphi=-\tfrac{1}{2\pi}\,\varphi\qquad\text{(since }i^{2}=-1\text{).}$$
> The right-hand side is a real scalar multiple of a real $2$-form, hence $p(F)=-\tfrac{1}{2\pi}\varphi\in\Omega^{2}(M;\mathbb{R})$ is real-valued. This is exactly why the normalising constant carries the factor $i$: it compensates the imaginary values of $F$ so that the characteristic form lands in real cohomology. (Under Bär's constant $\tfrac{1}{2\pi i}=-\tfrac{i}{2\pi}$ one would instead get $+\tfrac{1}{2\pi}\varphi$, real as well but of the opposite sign, consistent with the Convention callout above.)

**Step 3: The form $\tfrac{i}{2\pi}F$ is closed.**

The Bianchi identity, whose bracket term vanishes because $U(1)$ is abelian, gives $dF=0$, hence $d\,p(F)=0$.

> [!note]- Derivation
> By the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]], in a local trivialisation with connection form $A\in\Omega^{1}(U;\mathfrak{u}(1))$ and local curvature $F_{A}$,
> $$dF_{A}+[A\wedge F_{A}]=0\qquad\text{(Bianchi identity).}$$
> The Lie algebra $\mathfrak{u}(1)=i\mathbb{R}$ is **abelian**: the bracket of any two elements is zero, $[\xi,\eta]=0$. Consequently the bracket of $\mathfrak{u}(1)$-valued forms $[A\wedge F_{A}]$ vanishes identically, because by definition it is built pointwise from the Lie bracket of the values,
> $$[A\wedge F_{A}]=0\qquad\text{(}\mathfrak{u}(1)\text{ is abelian).}$$
> The Bianchi identity therefore reduces to
> $$dF_{A}=0\qquad\text{(bracket term dropped).}$$
> Since the local curvatures $F_{A}$ are the local expressions of the single descended form $F\in\Omega^{2}(M;i\mathbb{R})$, and $d$ is a local operator, this gives $dF=0$ on all of $M$. Finally, $d$ is $\mathbb{R}$-linear and $\tfrac{i}{2\pi}$ is a constant, so
> $$d\,p(F)=d\Big(\tfrac{i}{2\pi}F\Big)=\tfrac{i}{2\pi}\,dF=0\qquad\text{(constant pulls through }d\text{; }dF=0\text{).}$$
> Hence $p(F)$ is a closed real $2$-form.
>
> *(Alternative route to closedness.)* For the abelian group the structure equation for the curvature loses its quadratic term, $F_{A}=dA+\tfrac12[A\wedge A]=dA$, so locally $F=dA$ and $dF=d\,dA=0$ by $d^{2}=0$; this reproves $dF=0$ without invoking Bianchi and exhibits $F$ as locally exact.

**Step 4: The class $[p(F)]$ is the first Chern class.**

Being closed, $p(F)$ defines a de Rham class, and by definition this class is $c_{1}(P)$.

> [!note]- Derivation
> A closed $2$-form defines a de Rham cohomology class $[p(F)]\in H^{2}_{\mathrm{dR}}(M;\mathbb{R})$ (Step 2 places it in real cohomology; Step 3 gives closedness). By the definition of the Chern classes via Chern–Weil, the class of the degree-one polynomial's form is the **first Chern class**,
> $$c_{1}(P)=\big[p(F)\big]=\Big[\tfrac{i}{2\pi}F\Big]\in H^{2}_{\mathrm{dR}}(M;\mathbb{R}).$$
> That this class is independent of the chosen connection $\omega$ — and hence a genuine invariant of the bundle $P$ — is the content of the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]], proved separately; here we have only verified the two properties (reality, closedness) that make the definition sensible in the base case. The further facts that $\tfrac{i}{2\pi}\int_{\Sigma}F\in\mathbb{Z}$ over a closed oriented surface $\Sigma$ and equals the degree of the line bundle are established on [[Thm - First Chern Class of a Line Bundle from Curvature]].

> [!note]- Complete formal solution
> **Claim.** For a principal $U(1)$-bundle $P\to M$ with curvature $F=F_{\omega}\in\Omega^{2}(M;\mathfrak{u}(1))$ and $p=\tfrac{i}{2\pi}\operatorname{tr}$, the Chern–Weil form is $p(F)=\tfrac{i}{2\pi}F$, a real closed $2$-form representing $c_{1}(P)$.
>
> The Lie algebra $\mathfrak{u}(1)=\{\xi\in\mathbb{C}:\bar\xi=-\xi\}=i\mathbb{R}$ is one-dimensional, so on it $\operatorname{tr}(\xi)=\xi$ and $p(\xi)=\tfrac{i}{2\pi}\xi$. Applying the degree-one Chern–Weil construction, which evaluates the linear functional $p$ pointwise on the descended curvature,
> $$p(F)=\tfrac{i}{2\pi}\operatorname{tr}(F)=\tfrac{i}{2\pi}F.$$
> Writing $F=i\varphi$ with $\varphi\in\Omega^{2}(M;\mathbb{R})$ (possible since $F$ is $i\mathbb{R}$-valued), we get $p(F)=\tfrac{i}{2\pi}(i\varphi)=-\tfrac{1}{2\pi}\varphi$, which is real-valued.
>
> For closedness, the Bianchi identity reads $dF_{A}+[A\wedge F_{A}]=0$ locally; since $\mathfrak{u}(1)$ is abelian, $[A\wedge F_{A}]=0$, so $dF_{A}=0$, hence $dF=0$ globally and $d\,p(F)=\tfrac{i}{2\pi}dF=0$. (Equivalently, $F=dA$ locally by the abelian structure equation, so $dF=d\,dA=0$.)
>
> Thus $p(F)=\tfrac{i}{2\pi}F$ is a closed real $2$-form, and by the definition of the Chern classes $[p(F)]=c_{1}(P)\in H^{2}_{\mathrm{dR}}(M;\mathbb{R})$. $\blacksquare$

---

# Key Takeaways

**The abelian, rank-one case is the prototype from which every Chern–Weil form is a generalisation, and it reveals what each ingredient is for.** On a $U(1)$-bundle the whole apparatus of invariant polynomials collapses to a single rescaling of the curvature, and in that collapse one can see the role of each piece cleanly: the trace is the degree-one invariant polynomial; the normalising constant $\tfrac{i}{2\pi}$ exists to convert the imaginary-valued curvature into a real form (and to make periods integral, as the line-bundle degree theorem later shows); and closedness — the property that lets the form define a cohomology class — comes from the Bianchi identity. When learning or re-deriving the general Chern–Weil homomorphism, anchoring on this case answers "why the $i$, why closed, why real" before the higher-rank bookkeeping obscures them. The transferable diagnostic: to understand any characteristic-class normalisation, evaluate it on a line bundle and demand that the answer be a real class with integral periods; that single requirement pins down the constant up to sign.

**Reality of a characteristic form is a statement about where the curvature takes its values, mediated by the constant.** The curvature of a *unitary* connection is skew-Hermitian-valued, and for $U(1)$ that means imaginary-valued; multiplying by $\tfrac{i}{2\pi}$ rotates the imaginary line to the real line. This is not a cosmetic normalisation but the mechanism that lands Chern classes in *real* (indeed integral) cohomology rather than in a complex vector space. The same phenomenon recurs at higher rank: the coefficients $c_{j}$ of $\det(1+\tfrac{i}{2\pi}\xi)$ are real on $\mathfrak{u}(r)$ precisely because of the interplay between the factors of $i$ and the skew-Hermitian values of the curvature, verified by the conjugation argument $\det(\lambda 1+\tfrac{i}{2\pi}\xi)=\overline{\det(\bar\lambda 1+\tfrac{i}{2\pi}\xi)}$. Whenever a characteristic form is claimed to be real, the check is always the same: identify the value-space of the curvature (which structure group's Lie algebra?) and confirm the normalising constant maps it into $\mathbb{R}$.

**Abelianness is what makes the $U(1)$ theory of electromagnetism linear, and it is visible here as the vanishing bracket.** The single fact that $\mathfrak{u}(1)$ is abelian removes the quadratic term from the structure equation ($F=dA$ rather than $F=dA+\tfrac12[A\wedge A]$) and the correction term from the Bianchi identity ($dF=0$ rather than $dF+[A\wedge F]=0$). These are exactly the statements that, in the physics of a $U(1)$ gauge field, become $F=dA$ and $dF=0$ — the homogeneous Maxwell equation. The exercise therefore quietly contains the reason electromagnetism is a *linear* field theory while Yang–Mills for a nonabelian group is not: the obstruction is the Lie bracket, and it is zero for $U(1)$. When a computation in gauge theory simplifies dramatically, the first thing to check is whether the structure group is abelian, because that is where the nonlinear terms hide; the companion exercise [[Ex - The Coefficients of the Characteristic Polynomial are Ad-Invariant]] shows the contrasting behaviour once the group is enlarged to $U(r)$ and $SU(2)$.
