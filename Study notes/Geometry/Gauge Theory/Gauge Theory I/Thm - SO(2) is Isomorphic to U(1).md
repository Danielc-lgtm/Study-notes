---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Classical Matrix Groups"
  - "Def - Lie Group Homomorphism"
  - "Def - Embedded Submanifold"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\operatorname{Mat}(2\times 2;\mathbb{R})$ is the real vector space of $2\times 2$ real matrices, identified with $\mathbb{R}^4$ by reading off the four entries; $A^t$ is the transpose of $A$; $\det A$ is its [[Def - Determinant|determinant]]; and $1$ (or $1_2$) is the $2\times 2$ identity matrix. We write
$$R(\varphi) := \begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix}, \qquad \varphi\in\mathbb{R},$$
for the matrix of the counter-clockwise rotation of the Euclidean plane by the angle $\varphi$. The **special orthogonal group** is
$$SO(2) = \{A\in\operatorname{Mat}(2\times 2;\mathbb{R}) : A^t A = 1,\ \det A = 1\}\subset GL(2;\mathbb{R}),$$
and the **circle group** is
$$U(1) = \{z\in\operatorname{Mat}(1\times 1;\mathbb{C}) : \bar z\, z = 1\} = \{z\in\mathbb{C} : |z| = 1\}\subset GL(1;\mathbb{C}) = \mathbb{C}^\times;$$
these are two of the classical matrix groups defined on **[[Def - Classical Matrix Groups]]**, where each is proved to be a closed subgroup of a general linear group and hence, by the closed subgroup theorem, an [[Def - Embedded Submanifold|embedded submanifold]] and a Lie group. We identify a scalar $z = x + iy\in\mathbb{C}$ ($x,y\in\mathbb{R}$) with the point $(x,y)\in\mathbb{R}^2$, so that $U(1)$ sits inside $\mathbb{C}\cong\mathbb{R}^2$. The complex exponential is $e^{i\varphi} = \cos\varphi + i\sin\varphi$ (Euler's formula), and $S^1 := \{(x,y)\in\mathbb{R}^2 : x^2 + y^2 = 1\}$ is the standard unit circle. The symbol $\cong$ denotes isomorphism of Lie groups; a **[[Def - Lie Group Homomorphism|homomorphism of Lie groups]]** is a smooth group homomorphism $\varphi:G\to H$, and an **isomorphism of Lie groups** is a Lie group homomorphism that is invertible with smooth inverse.

We follow the standing series conventions: manifolds are smooth ($C^\infty$), Hausdorff, and second countable, and "smooth" always means $C^\infty$.

> [!warning] Convention: matrix layout in the source
> Bär's Example 1.1.8 writes a general element of $SO(2)$ as $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ with the four entries named $a,b,c,d$ **column by column**, so that his $b$ is our lower-left entry $A_{21}$ and his $c$ is our upper-right entry $A_{12}$. To keep the standard reading order we write $A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}$ and, once the constraints are solved, $A = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$ with $a = \cos\varphi$, $b = \sin\varphi$. The two conventions give the same set $SO(2)$ and the same final parametrisation; only the intermediate labels differ.

---

# Statement

> **Theorem ($SO(2)\cong U(1)$).** The special orthogonal group admits the parametrisation
> $$SO(2) = \left\{ R(\varphi) = \begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix} : \varphi\in\mathbb{R} \right\},$$
> the circle group admits the parametrisation
> $$U(1) = \{ e^{i\varphi} : \varphi\in\mathbb{R} \} = \{ z\in\mathbb{C} : |z| = 1\},$$
> and the map
> $$\Phi : SO(2)\longrightarrow U(1), \qquad \Phi\big(R(\varphi)\big) = e^{i\varphi},$$
> is a well-defined isomorphism of Lie groups. Consequently $SO(2)\cong U(1)$, and both groups are diffeomorphic to the unit circle $S^1$.

The isomorphism has the coordinate-free description
$$\Phi\begin{pmatrix} a & -b \\ b & a \end{pmatrix} = a + ib, \qquad \Phi^{-1}(x + iy) = \begin{pmatrix} x & -y \\ y & x \end{pmatrix},$$
which does not mention any angle and which we will use to prove smoothness; the two descriptions agree because $R(\varphi)$ has upper-left entry $\cos\varphi$ and lower-left entry $\sin\varphi$, and $e^{i\varphi} = \cos\varphi + i\sin\varphi$.

---

# Motivation

The very first thing one wants from the classical matrix groups is to recognise the small ones. Both $SO(2)$ and $U(1)$ are, set-theoretically, circles: a rotation of the plane is fixed by one angle, and a unit-modulus complex number is fixed by one argument. The theorem says that this coincidence is not merely a coincidence of underlying sets but an identity of Lie groups — the two circles carry *the same* multiplication once the angle is used as the coordinate on each, because composing two rotations adds their angles and multiplying two unit complex numbers adds their arguments. The circle group is thereby pinned down as the abstract object "$\mathbb{R}$ modulo $2\pi\mathbb{Z}$ with addition", presented in two different concrete guises, one geometric ($2\times 2$ rotation matrices) and one algebraic (unit complex numbers).

This is the smallest nontrivial instance of the general programme of the whole subject: a Lie group can be presented as a group of matrices in more than one way, and the interesting content is the dictionary between the presentations. Here the dictionary is exact — a genuine isomorphism — and once it is in hand every fact about one side transports to the other. The representation theory of $U(1)$ (the characters $z\mapsto z^k$) becomes the representation theory of planar rotations; the exponential map $\theta\mapsto e^{i\theta}$ of $U(1)$ becomes the exponential map $\theta\mapsto R(\theta)$ of $SO(2)$; and — the fact that matters most downstream — the *abelianness* of one group is the abelianness of the other.

That last point is why this seemingly elementary identification earns a place at the head of a gauge theory course. In chapter IV a connection on a principal $U(1)$-bundle is governed by the structure equation $F = dA + \tfrac12[A\wedge A]$, and the bracket term vanishes precisely because $U(1)$ is abelian, so its adjoint representation $\operatorname{Ad}$ is trivial. Electromagnetism is exactly the $U(1)$ gauge theory, and its curvature is the plain exterior derivative $F = dA$ with no self-interaction; the entire nonlinearity of Yang–Mills theory is the difference between this abelian circle and the nonabelian groups $SU(2)$, $SU(n)$ that replace it. Establishing $SO(2)\cong U(1)$ now, and recording that both are abelian, fixes the model against which every later nonabelian complication is measured.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis needed to place a matrix in $SO(2)$ is "$A$ is a $2\times 2$ real matrix with $A^t A = 1$ and $\det A = 1$". The skill is to recognise when a problem hands you such a matrix without saying so.

The first disguised source is **an orientation-preserving linear isometry of the Euclidean plane**. A linear map $A:\mathbb{R}^2\to\mathbb{R}^2$ preserves the inner product, $\langle Au, Av\rangle = \langle u, v\rangle$ for all $u,v$, if and only if $A^t A = 1$ (write the inner product as $\langle u, v\rangle = u^t v$; then $\langle Au, Av\rangle = u^t A^t A v$ equals $u^t v$ for all $u,v$ exactly when $A^t A = 1$), and among such $A$ the condition $\det A = 1$ singles out those that also preserve orientation, since $A^t A = 1$ forces $(\det A)^2 = 1$, hence $\det A = \pm 1$. So "distance-preserving and orientation-preserving linear map of the plane" is the hypothesis in disguise, and the bridge $B\Rightarrow A$ is the two computations just given. *Example problem:* show that the symmetry group of a circle centred at the origin, acting linearly and preserving orientation, is $SO(2)$ — every such symmetry is a rotation $R(\varphi)$, and the theorem then reads it as a unit complex number.

The second disguised source is **the time-$t$ flow of the planar harmonic oscillator**. The linear system $\dot u = J u$ with $J = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix}$ has flow $u(t) = e^{tJ}u(0)$, and $e^{tJ} = \cos t\cdot 1 + \sin t\cdot J = R(t)$ (because $J^2 = -1$, so the matrix exponential series splits into the cosine and sine series). The bridge is that $J^t = -J$ makes $e^{tJ}$ orthogonal, and $\operatorname{tr}J = 0$ makes $\det e^{tJ} = e^{t\operatorname{tr}J} = 1$, so the flow lands in $SO(2)$ for every $t$; the hypothesis "$A\in SO(2)$" is delivered by "$A$ is a flow matrix of $\dot u = Ju$". *Example problem:* identify the phase-space rotation of a unit-frequency oscillator with the one-parameter subgroup $t\mapsto e^{it}$ of $U(1)$; this is exactly the passage used on **[[Ex - The Exponential Map of so(2) is Surjective but Not Injective]]**.

The third disguised source is **multiplication by a unit complex number, regarded as a real linear map**. Fix $z = a + ib$ with $|z| = 1$. Multiplication $w\mapsto zw$ on $\mathbb{C}\cong\mathbb{R}^2$ is $\mathbb{R}$-linear, and in the real basis $\{1, i\}$ its matrix is $\begin{pmatrix} a & -b \\ b & a\end{pmatrix}$ (compute $z\cdot 1 = a + ib$ and $z\cdot i = -b + ia$). The bridge is that $|z| = 1$ gives $a^2 + b^2 = 1$, which is precisely $A^t A = 1$ and $\det A = a^2 + b^2 = 1$ for this matrix, so "the real form of multiplication by a unit complex number" is a source for "$A\in SO(2)$". *Example problem:* prove that the map sending $z\in U(1)$ to its real multiplication matrix is exactly the inverse isomorphism $\Phi^{-1}$ of the theorem, so the disguised source *is* the theorem read backwards.

**Targets (Output Amplification).** The bare conclusion is an isomorphism $SO(2)\cong U(1)$. Combined with further ingredients it yields more.

Combine the conclusion with **the abelianness of $U(1)$**. Complex multiplication is commutative, so $U(1)$ is abelian, and transporting this across $\Phi$ shows $SO(2)$ is abelian: planar rotations commute. The amplified output is that the adjoint representation is trivial, $\operatorname{Ad}_g = \operatorname{id}$ for every $g$, since for an abelian group conjugation $\alpha_g(h) = ghg^{-1} = h$ is the identity and $\operatorname{Ad}_g = d_e\alpha_g = \operatorname{id}$ (this is exactly clause (iv) of **[[Thm - Ad is a Smooth Representation and its Differential is ad]]**). This is the ingredient chapter IV uses to strip the bracket term out of the structure equation of a $U(1)$-connection.

Combine the conclusion with **the classification of complex representations of $U(1)$**. The irreducible complex representations of $U(1)$ are the characters $\varrho_k:z\mapsto z^k$, $k\in\mathbb{Z}$ (proved on **[[Thm - Complex Representations of U(1) and SU(2)]]**). Through $\Phi$ these become the representations $R(\varphi)\mapsto e^{ik\varphi}$ of $SO(2)$, the "spin-$k$" or weight-$k$ rotation modes. The amplified output is a complete Fourier-type decomposition of any finite-dimensional complex $SO(2)$-representation into rotation modes, the abelian prototype of the weight decomposition used for every compact group.

Combine the conclusion with **the exponential map**. The exponential of $U(1)$ is $\theta\mapsto e^{i\theta}$, surjective with kernel $2\pi\mathbb{Z}$; transported across $\Phi$ it is $\theta\mapsto R(\theta)$, the exponential of $SO(2)$. The amplified output is the presentation $SO(2)\cong\mathbb{R}/2\pi\mathbb{Z}$ as a quotient group and the identification of $\mathfrak{so}(2)\cong\mathfrak{u}(1) = i\mathbb{R}$ as one-dimensional abelian Lie algebras, which is where **[[Ex - The Exponential Map of so(2) is Surjective but Not Injective]]** lives.

---

# Why Is It True

Strip away the two presentations and ask what a rotation of the plane and a unit complex number have in common. A rotation is determined by one number, the angle $\varphi$; a unit complex number is determined by one number, the argument $\varphi$; and both numbers live on the same footing, defined only up to adding a multiple of $2\pi$. So each group is a circle's worth of data. The reason the multiplications match is that composing rotations and multiplying complex exponentials are the *same arithmetic on the angle*: $R(\varphi)R(\psi) = R(\varphi + \psi)$ by the addition formulas for sine and cosine, and $e^{i\varphi}e^{i\psi} = e^{i(\varphi+\psi)}$ by the exponential law. Adding angles is all that either group does.

> **The mechanism in one sentence:** the two orthonormality equations $a^2+b^2 = 1$, $c^2+d^2=0\ (\text{after }c=-b, d=a)$ together with $\det = 1$ collapse the four real entries of a $2\times 2$ matrix down to a single angle, exactly the datum that also parametrises the unit circle, and both groups turn that datum into their product by adding it modulo $2\pi$.

Here is the collapse made concrete. A general $2\times 2$ real matrix has four free entries. The orthogonality condition $A^t A = 1$ is three real equations (the diagonal entries of $A^t A$ give two unit-length conditions on the columns, the off-diagonal entry gives one orthogonality condition), cutting four degrees of freedom to one and leaving a discrete choice of sign; the determinant condition $\det A = 1$ fixes that sign. What survives is a single continuous parameter living on a circle. On the $U(1)$ side the modulus condition $|z| = 1$ cuts the two real degrees of freedom of a complex number down to one, again a circle. The map $\Phi$ simply declares that the surviving parameter on the left equals the surviving parameter on the right, and the reason $\Phi$ respects multiplication is that on both sides the group law, read in that parameter, is "add".

The only subtlety is bookkeeping: the parameter is an angle, so it is ambiguous modulo $2\pi$. But this ambiguity is *identical* on the two sides — $R(\varphi) = R(\varphi')$ exactly when $\varphi - \varphi'\in 2\pi\mathbb{Z}$, and $e^{i\varphi} = e^{i\varphi'}$ under exactly the same condition — so the ambiguity cancels and $\Phi$ is a genuine, single-valued map. That cancellation is the whole reason $\Phi$ is well-defined, and it is the point the source leaves unremarked.

---

# What Makes This Hard

The mathematics is elementary, and the two ways to go wrong are both bookkeeping traps. The first is **well-definedness**: the map is written "$R(\varphi)\mapsto e^{i\varphi}$", but $\varphi$ is not a function of the matrix — it is defined only modulo $2\pi$ — so before anything else one must check that changing $\varphi$ to another angle representing the same matrix does not change $e^{i\varphi}$. Skipping this is the standard error; it looks like a triviality but it is precisely the content that the two circles have the same period. The second trap is **smoothness**. The set-level bijection and the homomorphism property are easy, but "isomorphism of Lie groups" demands that both $\Phi$ and $\Phi^{-1}$ be smooth as maps of the two manifolds $SO(2)\subset\mathbb{R}^4$ and $U(1)\subset\mathbb{R}^2$ — and one cannot prove this by differentiating "$\varphi$" as a function of the matrix, because that function is only locally defined and its smoothness is the very thing in question. The clean route is to abandon the angle and write $\Phi$ and $\Phi^{-1}$ as restrictions of *linear* ambient maps on matrix entries, whose smoothness is manifest; recognising that this reformulation is available is the one genuinely non-obvious step.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Solve the defining equations of $SO(2)$ to get the rotation parametrisation; describe $U(1)$ as unit-modulus complex numbers via Euler's formula; observe that both the matrix $R(\varphi)$ and the number $e^{i\varphi}$ depend on $\varphi$ only modulo $2\pi$, which makes $\Phi$ well-defined; get the homomorphism property from $R(\varphi)R(\psi) = R(\varphi+\psi)$; get bijectivity by writing down the inverse in closed form on entries; and get smoothness of both directions by recognising $\Phi$ and $\Phi^{-1}$ as restrictions of linear maps between the ambient matrix spaces.

**Subgoal decomposition:**

1. **Parametrise $SO(2)$ by rotations.** Show every $A\in SO(2)$ equals $R(\varphi)$ for some $\varphi\in\mathbb{R}$, and that $R(\varphi) = R(\varphi')$ if and only if $\varphi\equiv\varphi'\pmod{2\pi}$.
   - *Hint:* Write $A = \begin{pmatrix} a & c \\ b & d\end{pmatrix}$, expand $A^t A = 1$ into $a^2+b^2=1$, $c^2+d^2=1$, $ac+bd=0$, and use $\det A = ad - bc = 1$; multiply the determinant equation by $c$ and by $d$ and substitute to force $c = -b$, $d = a$.
   - *Why needed:* Without this normal form there is no angle to feed into $e^{i\varphi}$, and the domain of $\Phi$ is not understood.

2. **Describe $U(1)$ by Euler's formula.** Show $U(1) = \{z : |z| = 1\} = \{e^{i\varphi} : \varphi\in\mathbb{R}\}$ and that $e^{i\varphi} = e^{i\varphi'}$ if and only if $\varphi\equiv\varphi'\pmod{2\pi}$.
   - *Hint:* $\bar z z = |z|^2$, so the defining condition of $U(1)$ is $|z| = 1$; every unit complex number is $\cos\varphi + i\sin\varphi = e^{i\varphi}$ by polar form.
   - *Why needed:* It gives the codomain the same angular coordinate as the domain, so the two periodicities can be compared.

3. **Well-definedness of $\Phi$.** Show the rule $\Phi(R(\varphi)) = e^{i\varphi}$ does not depend on the choice of $\varphi$ representing a given matrix.
   - *Hint:* Combine the two "if and only if modulo $2\pi$" statements from subgoals 1 and 2: equal matrices give congruent angles, congruent angles give equal exponentials.
   - *Why needed:* Until this holds, $\Phi$ is not a function.

4. **Homomorphism.** Show $\Phi(AB) = \Phi(A)\Phi(B)$.
   - *Hint:* $R(\varphi)R(\psi) = R(\varphi+\psi)$ by the addition theorems; then $\Phi(R(\varphi)R(\psi)) = e^{i(\varphi+\psi)} = e^{i\varphi}e^{i\psi}$.
   - *Why needed:* An isomorphism of groups must preserve the operation.

5. **Bijectivity.** Exhibit a two-sided inverse.
   - *Hint:* Define $\Psi(x+iy) = \begin{pmatrix} x & -y \\ y & x\end{pmatrix}$ and check $\Psi\circ\Phi = \operatorname{id}_{SO(2)}$, $\Phi\circ\Psi = \operatorname{id}_{U(1)}$ on entries.
   - *Why needed:* An isomorphism is invertible.

6. **Smoothness of both directions.** Show $\Phi$ and $\Psi = \Phi^{-1}$ are smooth as maps of the embedded submanifolds $SO(2)\subset\mathbb{R}^4$ and $U(1)\subset\mathbb{R}^2$.
   - *Hint:* $\Phi$ is the restriction to $SO(2)$ of the linear map $\operatorname{Mat}(2\times 2;\mathbb{R})\to\mathbb{C}$, $A\mapsto A_{11} + iA_{21}$; $\Psi$ is the restriction to $U(1)$ of the linear map $\mathbb{C}\to\operatorname{Mat}(2\times 2;\mathbb{R})$, $x+iy\mapsto\begin{pmatrix} x & -y \\ y & x\end{pmatrix}$; use that a smooth ambient map restricts to a smooth map between embedded submanifolds when it carries one into the other.
   - *Why needed:* "Isomorphism of Lie groups" requires smoothness of the map and its inverse, not just of the underlying bijection.

7. **Diffeomorphic to $S^1$.** Conclude both groups are diffeomorphic to the standard circle.
   - *Hint:* $U(1) = \{x+iy : x^2+y^2 = 1\}$ is $S^1$ under $\mathbb{C}\cong\mathbb{R}^2$; compose with $\Phi$.
   - *Why needed:* It records the underlying smooth manifold, the datum used whenever these groups appear as fibres or structure groups later.

---

# Lemma Decomposition

> [!note]- Lemma 1: Every element of $SO(2)$ is a rotation, uniquely up to $2\pi$
> **Statement:** For $A\in\operatorname{Mat}(2\times 2;\mathbb{R})$ one has $A\in SO(2)$ if and only if $A = R(\varphi)$ for some $\varphi\in\mathbb{R}$; moreover $R(\varphi) = R(\varphi')$ if and only if $\varphi - \varphi'\in 2\pi\mathbb{Z}$.
>
> **Hint:** Expand $A^t A = 1$ and $\det A = 1$ into four scalar equations and solve; for uniqueness use that $(\cos,\sin)$ is injective on any half-open interval of length $2\pi$.
>
> **Why needed:** It fixes the domain of $\Phi$ as a circle of angles and supplies the "$2\pi$" ambiguity on the $SO(2)$ side.
>
> > [!note]- Full proof
> > **($\Leftarrow$) A rotation lies in $SO(2)$.** For any $\varphi$,
> > $$R(\varphi)^t R(\varphi) = \begin{pmatrix} \cos\varphi & \sin\varphi \\ -\sin\varphi & \cos\varphi \end{pmatrix}\begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix} = \begin{pmatrix} \cos^2\varphi + \sin^2\varphi & 0 \\ 0 & \sin^2\varphi + \cos^2\varphi \end{pmatrix} = 1 \qquad (\text{by } \cos^2\varphi + \sin^2\varphi = 1),$$
> > and $\det R(\varphi) = \cos\varphi\cdot\cos\varphi - (-\sin\varphi)\cdot\sin\varphi = \cos^2\varphi + \sin^2\varphi = 1$. Hence $R(\varphi)\in SO(2)$.
> >
> > **($\Rightarrow$) An element of $SO(2)$ is a rotation.** Write $A = \begin{pmatrix} a & c \\ b & d\end{pmatrix}$ with $a,b,c,d\in\mathbb{R}$ (the entries in reading order are $A_{11} = a$, $A_{12} = c$, $A_{21} = b$, $A_{22} = d$). The condition $A^t A = 1$ reads
> > $$\begin{pmatrix} a & b \\ c & d\end{pmatrix}\begin{pmatrix} a & c \\ b & d\end{pmatrix} = \begin{pmatrix} a^2 + b^2 & ac + bd \\ ac + bd & c^2 + d^2 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & 1\end{pmatrix},$$
> > giving the three scalar equations
> > $$a^2 + b^2 = 1 \tag{1.1}$$
> > $$c^2 + d^2 = 1 \tag{1.2}$$
> > $$ac + bd = 0. \tag{1.3}$$
> > The determinant condition is
> > $$\det A = ad - bc = 1. \tag{1.4}$$
> > Multiply $(1.4)$ by $c$: $\ acd - bc^2 = c$. By $(1.3)$, $ac = -bd$, so $acd = -bd^2$, giving $-bd^2 - bc^2 = c$, that is $-b(c^2 + d^2) = c$; by $(1.2)$, $c^2 + d^2 = 1$, so
> > $$c = -b \qquad (\text{by } (1.4),(1.3),(1.2)).$$
> > Multiply $(1.4)$ by $d$: $\ ad^2 - bcd = d$. By $(1.3)$, $bd = -ac$, so $bcd = -ac^2$, giving $ad^2 + ac^2 = d$, that is $a(c^2 + d^2) = d$; by $(1.2)$ again,
> > $$d = a \qquad (\text{by } (1.4),(1.3),(1.2)).$$
> > Substituting $c = -b$ and $d = a$ into $A$ gives $A = \begin{pmatrix} a & -b \\ b & a\end{pmatrix}$ with, by $(1.1)$, $a^2 + b^2 = 1$. A pair $(a,b)$ on the unit circle is $(\cos\varphi, \sin\varphi)$ for some $\varphi\in\mathbb{R}$ (polar coordinates on the unit circle: the continuous surjection $\varphi\mapsto(\cos\varphi,\sin\varphi)$ from $\mathbb{R}$ onto $\{(a,b):a^2+b^2=1\}$ hits every point). Then $A = R(\varphi)$.
> >
> > **Uniqueness up to $2\pi$.** If $R(\varphi) = R(\varphi')$ then in particular $\cos\varphi = \cos\varphi'$ and $\sin\varphi = \sin\varphi'$. Two reals with equal sine and equal cosine differ by a multiple of $2\pi$: the difference $\delta = \varphi - \varphi'$ satisfies $\cos\delta = \cos\varphi\cos\varphi' + \sin\varphi\sin\varphi' = \cos^2\varphi' + \sin^2\varphi' = 1$ (by the cosine subtraction formula and $\cos\varphi=\cos\varphi'$, $\sin\varphi=\sin\varphi'$), and $\cos\delta = 1$ holds if and only if $\delta\in 2\pi\mathbb{Z}$. Conversely, if $\varphi - \varphi'\in 2\pi\mathbb{Z}$ then $\cos$ and $\sin$, being $2\pi$-periodic, agree at $\varphi$ and $\varphi'$, so $R(\varphi) = R(\varphi')$. Therefore $R(\varphi) = R(\varphi')$ if and only if $\varphi\equiv\varphi'\pmod{2\pi}$. $\blacksquare$

> [!note]- Lemma 2: The circle group is the unit-modulus complex numbers, uniquely angled up to $2\pi$
> **Statement:** $U(1) = \{z\in\mathbb{C} : |z| = 1\} = \{e^{i\varphi} : \varphi\in\mathbb{R}\}$, and $e^{i\varphi} = e^{i\varphi'}$ if and only if $\varphi - \varphi'\in 2\pi\mathbb{Z}$.
>
> **Hint:** The defining relation $\bar z z = 1$ is $|z|^2 = 1$; then use the polar form and Euler's formula.
>
> **Why needed:** It equips the codomain of $\Phi$ with the same angular coordinate and the same $2\pi$-ambiguity as the domain, so that well-definedness can be checked by comparing the two.
>
> > [!note]- Full proof
> > **The defining relation is $|z| = 1$.** For $z\in\mathbb{C}$ we have $\bar z z = |z|^2\ge 0$, so the condition $\bar z z = 1$ defining $U(1)\subset GL(1;\mathbb{C})$ is equivalent to $|z|^2 = 1$, that is $|z| = 1$. Hence $U(1) = \{z : |z| = 1\}$.
> >
> > **Every unit complex number is $e^{i\varphi}$.** Let $z = x + iy$ with $x^2 + y^2 = |z|^2 = 1$. The point $(x,y)$ lies on the unit circle, so $(x, y) = (\cos\varphi, \sin\varphi)$ for some $\varphi\in\mathbb{R}$, whence $z = \cos\varphi + i\sin\varphi = e^{i\varphi}$ by Euler's formula. Conversely $|e^{i\varphi}|^2 = \cos^2\varphi + \sin^2\varphi = 1$, so every $e^{i\varphi}$ lies in $U(1)$. Therefore $U(1) = \{e^{i\varphi} : \varphi\in\mathbb{R}\}$.
> >
> > **Uniqueness up to $2\pi$.** $e^{i\varphi} = e^{i\varphi'}$ means $\cos\varphi = \cos\varphi'$ and $\sin\varphi = \sin\varphi'$ (equating real and imaginary parts), which by the same cosine-subtraction argument as in Lemma 1 holds if and only if $\varphi - \varphi'\in 2\pi\mathbb{Z}$. $\blacksquare$

> [!note]- Lemma 3: Rotations compose by adding angles
> **Statement:** For all $\varphi,\psi\in\mathbb{R}$, $\ R(\varphi)R(\psi) = R(\varphi + \psi)$.
>
> **Hint:** Multiply the two matrices and read the entries through the addition theorems $\cos(\varphi+\psi) = \cos\varphi\cos\psi - \sin\varphi\sin\psi$, $\sin(\varphi+\psi) = \sin\varphi\cos\psi + \cos\varphi\sin\psi$.
>
> **Why needed:** It is the identity that makes $\Phi$ a homomorphism, and it encodes the geometric fact that composing two rotations rotates by the sum of the angles.
>
> > [!note]- Full proof
> > Compute the product entry by entry:
> > $$R(\varphi)R(\psi) = \begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix}\begin{pmatrix} \cos\psi & -\sin\psi \\ \sin\psi & \cos\psi \end{pmatrix} = \begin{pmatrix} \cos\varphi\cos\psi - \sin\varphi\sin\psi & -\cos\varphi\sin\psi - \sin\varphi\cos\psi \\ \sin\varphi\cos\psi + \cos\varphi\sin\psi & -\sin\varphi\sin\psi + \cos\varphi\cos\psi \end{pmatrix}.$$
> > By the addition theorems for cosine and sine, the upper-left and lower-right entries are $\cos(\varphi+\psi)$, the lower-left entry is $\sin(\varphi+\psi)$, and the upper-right entry is $-\sin(\varphi+\psi)$. Hence
> > $$R(\varphi)R(\psi) = \begin{pmatrix} \cos(\varphi+\psi) & -\sin(\varphi+\psi) \\ \sin(\varphi+\psi) & \cos(\varphi+\psi) \end{pmatrix} = R(\varphi + \psi). \qquad \blacksquare$$

> [!note]- Lemma 4: A smooth ambient map restricts to a smooth map of embedded submanifolds
> **Statement:** Let $S\subseteq\mathbb{R}^N$ and $T\subseteq\mathbb{R}^M$ be [[Def - Embedded Submanifold|embedded submanifolds]], and let $F:\mathbb{R}^N\to\mathbb{R}^M$ be a smooth map with $F(S)\subseteq T$. Then the restriction $F|_S : S\to T$ is smooth as a map of manifolds.
>
> **Hint:** Use a slice chart for $T$: in it, the coordinate representation of $F|_S$ is obtained by composing $F$ with the slice chart and then discarding the (identically zero) transverse coordinates.
>
> **Why needed:** It is the tool that turns the manifest smoothness of the *linear* entry-formulas for $\Phi$ and $\Phi^{-1}$ into smoothness of $\Phi$, $\Phi^{-1}$ as maps of the manifolds $SO(2)$ and $U(1)$, avoiding any appeal to the angle as a coordinate.
>
> > [!note]- Full proof
> > Recall that, by definition of an [[Def - Embedded Submanifold|embedded submanifold]], every embedded $k$-submanifold $T\subseteq\mathbb{R}^M$ has, about each of its points $q$, a **slice chart**: an open set $V\subseteq\mathbb{R}^M$ containing $q$ and a diffeomorphism $\psi:V\to\widehat V$ onto an open $\widehat V\subseteq\mathbb{R}^M$ such that
> > $$\psi(V\cap T) = \{\, y\in\widehat V : y^{k+1} = \cdots = y^M = 0 \,\},$$
> > and the pair $(V\cap T,\ \tilde\psi)$ with $\tilde\psi := \pi_k\circ\psi|_{V\cap T}$ is a chart of $T$ about $q$, where $\pi_k:\mathbb{R}^M\to\mathbb{R}^k$ is the projection onto the first $k$ coordinates. The inclusion $\iota_S:S\hookrightarrow\mathbb{R}^N$ of an embedded submanifold is smooth (again by definition, a chart of $S$ extends to a slice chart of $\mathbb{R}^N$, in which $\iota_S$ is the inclusion of a coordinate subspace).
> >
> > **Smoothness at an arbitrary point.** Fix $p\in S$ and put $q := F(p)\in T$ (using $F(S)\subseteq T$). Choose a slice chart $(V,\psi)$ of $\mathbb{R}^M$ about $q$ as above and a chart $(W,\chi)$ of $S$ about $p$ with $F(\iota_S(W))\subseteq V$ (possible because $F\circ\iota_S$ is continuous and $V$ is open). On $W$ the coordinate representation of $F|_S:S\to T$ in the charts $\chi$ and $\tilde\psi$ is
> > $$\tilde\psi\circ (F|_S)\circ\chi^{-1} = \pi_k\circ\psi\circ F\circ\iota_S\circ\chi^{-1} \qquad (\text{by the definitions of } \tilde\psi \text{ and } F|_S = F\circ\iota_S).$$
> > Each factor on the right is smooth: $\chi^{-1}$ is smooth (chart inverse), $\iota_S$ is smooth (embedded inclusion), $F$ is smooth (hypothesis), $\psi$ is smooth (chart), and $\pi_k$ is linear hence smooth. A composite of smooth maps between open subsets of Euclidean spaces is smooth (chain rule), so $\tilde\psi\circ(F|_S)\circ\chi^{-1}$ is smooth on $\chi(W)$. As $p\in S$ was arbitrary, $F|_S:S\to T$ is smooth. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We must show four things: that the two displayed parametrisations of $SO(2)$ and $U(1)$ are correct; that $\Phi(R(\varphi)) = e^{i\varphi}$ is a well-defined bijective group homomorphism; that $\Phi$ and $\Phi^{-1}$ are smooth; and that both groups are diffeomorphic to $S^1$. We use Lemmas 1–4 throughout.
>
> **Step 0 — the objects are Lie groups and embedded submanifolds.** By **[[Def - Classical Matrix Groups]]**, $SO(2)$ is a closed subgroup of $GL(2;\mathbb{R})$ and $U(1)$ is a closed subgroup of $GL(1;\mathbb{C})$; each is therefore an [[Def - Embedded Submanifold|embedded submanifold]] of its ambient matrix space and a Lie group, with the smooth structure inherited from $\operatorname{Mat}(2\times 2;\mathbb{R})\cong\mathbb{R}^4$ and $\mathbb{C}\cong\mathbb{R}^2$ respectively. This is the precondition that lets us speak of smooth maps between them.
>
> **Step 1 — the parametrisations.** By Lemma 1, $SO(2) = \{R(\varphi) : \varphi\in\mathbb{R}\}$, and by Lemma 2, $U(1) = \{e^{i\varphi} : \varphi\in\mathbb{R}\} = \{z : |z| = 1\}$. This establishes the two displayed descriptions in the statement.
>
> **Step 1a — the two formulas for $\Phi$ agree.** For the rotation $R(\varphi) = \begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi\end{pmatrix}$ we have $R(\varphi)_{11} = \cos\varphi$ and $R(\varphi)_{21} = \sin\varphi$, so $R(\varphi)_{11} + iR(\varphi)_{21} = \cos\varphi + i\sin\varphi = e^{i\varphi}$ (Euler's formula). Thus the coordinate-free rule $A\mapsto A_{11} + iA_{21}$ agrees with $R(\varphi)\mapsto e^{i\varphi}$ on every element of $SO(2)$, and we may use whichever form is convenient. Writing a general element as $A = \begin{pmatrix} a & -b \\ b & a\end{pmatrix}$ (Lemma 1) the rule reads $\Phi(A) = a + ib$.
>
> **Step 2 — $\Phi$ is well-defined.** The rule $\Phi(R(\varphi)) = e^{i\varphi}$ names an angle representing the matrix, so we must check the output is independent of that name. Suppose $R(\varphi) = R(\varphi')$ represent the same element of $SO(2)$. By the uniqueness clause of Lemma 1, $\varphi\equiv\varphi'\pmod{2\pi}$. By the uniqueness clause of Lemma 2, $\varphi\equiv\varphi'\pmod{2\pi}$ gives $e^{i\varphi} = e^{i\varphi'}$. Hence $\Phi(R(\varphi)) = \Phi(R(\varphi'))$: the value does not depend on the chosen angle, and $\Phi:SO(2)\to U(1)$ is a well-defined function. (Equivalently, in the coordinate-free form $\Phi(A) = A_{11} + iA_{21}$, no choice is made and well-definedness is automatic; and $|A_{11} + iA_{21}|^2 = a^2 + b^2 = 1$ by Lemma 1, so $\Phi$ indeed lands in $U(1)$.)
>
> **Step 3 — $\Phi$ is a group homomorphism.** Let $A = R(\varphi)$ and $B = R(\psi)$ be elements of $SO(2)$. By Lemma 3, $AB = R(\varphi)R(\psi) = R(\varphi + \psi)$, so
> $$\Phi(AB) = \Phi(R(\varphi+\psi)) = e^{i(\varphi+\psi)} = e^{i\varphi}e^{i\psi} = \Phi(A)\,\Phi(B) \qquad (\text{by Lemma 3, the definition of } \Phi, \text{ and } e^{i(\varphi+\psi)} = e^{i\varphi}e^{i\psi}).$$
> Thus $\Phi$ preserves the group operation. (It also sends the identity $R(0) = 1_2$ to $e^{i0} = 1$, as any homomorphism must.)
>
> **Step 4 — $\Phi$ is a bijection.** Define
> $$\Psi : U(1)\longrightarrow SO(2), \qquad \Psi(x + iy) = \begin{pmatrix} x & -y \\ y & x \end{pmatrix},$$
> which does land in $SO(2)$: for $x + iy\in U(1)$ we have $x^2 + y^2 = 1$, so the matrix $\begin{pmatrix} x & -y \\ y & x\end{pmatrix}$ satisfies $A^t A = 1$ and $\det A = x^2 + y^2 = 1$ by the ($\Leftarrow$) computation of Lemma 1 with $a = x$, $b = y$. Now for $A = \begin{pmatrix} a & -b \\ b & a\end{pmatrix}\in SO(2)$,
> $$\Psi(\Phi(A)) = \Psi(a + ib) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix} = A \qquad (\text{by } \Phi(A) = a + ib \text{ from Step 1a and the definition of } \Psi),$$
> and for $z = x + iy\in U(1)$,
> $$\Phi(\Psi(z)) = \Phi\begin{pmatrix} x & -y \\ y & x \end{pmatrix} = x + iy = z \qquad (\text{by the definition of } \Psi \text{ and } \Phi(A) = A_{11} + iA_{21}).$$
> Since $\Psi\circ\Phi = \operatorname{id}_{SO(2)}$ and $\Phi\circ\Psi = \operatorname{id}_{U(1)}$, the map $\Phi$ is a bijection with inverse $\Phi^{-1} = \Psi$.
>
> **Step 5 — $\Phi$ and $\Phi^{-1}$ are smooth.** Let $L:\operatorname{Mat}(2\times 2;\mathbb{R})\to\mathbb{C}$ be the map $L(A) = A_{11} + iA_{21}$. In the real coordinates $(A_{11}, A_{12}, A_{21}, A_{22})$ on the domain and $(\operatorname{Re}, \operatorname{Im})$ on $\mathbb{C}\cong\mathbb{R}^2$, $L$ is $(A_{11}, A_{12}, A_{21}, A_{22})\mapsto(A_{11}, A_{21})$, a linear map, hence smooth. By Step 1a and Step 2, $L$ carries $SO(2)$ into $U(1)$ and $L|_{SO(2)} = \Phi$. Since $SO(2)\subset\mathbb{R}^4$ and $U(1)\subset\mathbb{R}^2$ are embedded submanifolds (Step 0), Lemma 4 applied to $F = L$, $S = SO(2)$, $T = U(1)$ shows $\Phi = L|_{SO(2)}$ is smooth.
>
> Likewise let $M:\mathbb{C}\to\operatorname{Mat}(2\times 2;\mathbb{R})$ be $M(x + iy) = \begin{pmatrix} x & -y \\ y & x\end{pmatrix}$, which in real coordinates is $(x, y)\mapsto(x, -y, y, x)$, a linear map, hence smooth. By Step 4, $M$ carries $U(1)$ into $SO(2)$ and $M|_{U(1)} = \Psi = \Phi^{-1}$. By Lemma 4 applied to $F = M$, $S = U(1)$, $T = SO(2)$, the map $\Phi^{-1} = M|_{U(1)}$ is smooth.
>
> Therefore $\Phi$ is a smooth group homomorphism with smooth inverse, that is, an isomorphism of Lie groups (**[[Def - Lie Group Homomorphism]]**), and $SO(2)\cong U(1)$.
>
> **Step 6 — both are diffeomorphic to $S^1$.** Consider the map $j:\mathbb{C}\to\mathbb{R}^2$, $x + iy\mapsto(x, y)$; it is a linear isomorphism, hence a diffeomorphism of $\mathbb{C}\cong\mathbb{R}^2$ with $\mathbb{R}^2$. It carries $U(1) = \{x + iy : x^2 + y^2 = 1\}$ onto $S^1 = \{(x,y) : x^2 + y^2 = 1\}$; since $U(1)$ and $S^1$ are embedded submanifolds and $j$ and $j^{-1}$ are (restrictions of) linear maps carrying one into the other, Lemma 4 applied in both directions shows $j|_{U(1)}:U(1)\to S^1$ is a diffeomorphism. Hence $U(1)$ is diffeomorphic to $S^1$, and composing with the diffeomorphism $\Phi:SO(2)\to U(1)$ of Step 5, so is $SO(2)$. Therefore both $SO(2)$ and $U(1)$ are diffeomorphic to the unit circle. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fourier analysis on the circle.** Regard a $2\pi$-periodic function $f:\mathbb{R}\to\mathbb{C}$ as a function on $U(1)$ via $f(e^{i\varphi})$, and its Fourier coefficients $\hat f(k) = \frac{1}{2\pi}\int_0^{2\pi} f(e^{i\varphi})e^{-ik\varphi}\,d\varphi$ as the components of $f$ along the characters $\varrho_k:z\mapsto z^k$. Through $\Phi$ these characters are the weight-$k$ rotation modes $R(\varphi)\mapsto e^{ik\varphi}$ of $SO(2)$, so a Fourier series *is* the decomposition of a function on the rotation group into its irreducible pieces. The theorem is what licenses moving freely between "periodic function of an angle" and "function on the group of planar rotations"; the application is non-obvious because harmonic analysis is usually taught with no reference to $SO(2)$ at all, yet the exponentials $e^{ik\varphi}$ are exactly the matrix coefficients of the rotation representations.

**Planar rigid-body kinematics.** The orientation of a rigid body confined to a plane is an element of $SO(2)$, and its angular configuration space is therefore a circle. Writing the orientation as a unit complex number $e^{i\theta(t)}$ rather than as a rotation matrix turns the kinematic equation $\dot R = R\,\Omega$ (with $\Omega = \begin{pmatrix} 0 & -\omega \\ \omega & 0\end{pmatrix}$ the angular-velocity matrix) into the scalar equation $\dot z = i\omega z$, which integrates immediately to $z(t) = e^{i\omega t}z(0)$. The theorem is what guarantees the two formulations describe the same motion; the application is non-obvious because the matrix form hides, behind a $2\times 2$ differential equation, what the complex form exposes as a one-line exponential.

**Winding numbers and the fundamental group.** A loop in the plane avoiding the origin has a winding number, computed as the degree of the induced map $S^1\to U(1)$, $t\mapsto\gamma(t)/|\gamma(t)|$. Because $U(1)\cong SO(2)$ is the circle, this degree is an element of $\pi_1(S^1) = \mathbb{Z}$, and the group structure of $U(1)$ is exactly what makes the winding number of a product of loops the sum of the winding numbers. The theorem supplies the identification of the target circle with a *group*, without which "winding number" would be a bare integer rather than a homomorphism $\pi_1\to\mathbb{Z}$; the application is non-obvious because topologists rarely emphasise that the circle they wind around is the same object as the rotation group.

---

# Bridges

- **[[Ex - S1 and SO(2) are homeomorphic as topological groups]]** — the topological predecessor. That exercise shows $S^1$ and $SO(2)$ are isomorphic as *topological* groups: a continuous group isomorphism with continuous inverse, built from the same angle parametrisation but asking only for continuity. The present theorem upgrades that homeomorphism to a *diffeomorphism* and an isomorphism of *Lie* groups, by supplying the smoothness of $\Phi$ and $\Phi^{-1}$ (Step 5) that the topological statement does not address. The construction is the identical map $R(\varphi)\leftrightarrow e^{i\varphi}$; only the category, and hence the regularity demanded of the maps, changes.

- **[[Def - Classical Matrix Groups]]** — the source of the objects. There $SO(2)$ and $U(1)$ are defined as closed subgroups and shown to be Lie groups and embedded submanifolds via the closed subgroup theorem; that page also records the elementary identity $U(1)\subset GL(1;\mathbb{C})$ is the unit circle, which this theorem promotes into a full group isomorphism with $SO(2)$. The bridge is that "closed subgroup, hence embedded submanifold" is precisely the input Step 0 needs before smoothness can even be discussed.

- **[[Thm - Ad is a Smooth Representation and its Differential is ad]]** — where the payoff is collected. Once $SO(2)\cong U(1)$ is known and $U(1)$ is seen to be abelian (complex multiplication commutes), that theorem's clause (iv) gives $\operatorname{Ad}_g = \operatorname{id}$ for every $g\in U(1)\cong SO(2)$: the adjoint representation is trivial. The construction here — transporting commutativity across $\Phi$ — is what feeds "abelian, so $\operatorname{Ad}$ trivial" into chapter IV, where the curvature of a $U(1)$-connection loses its bracket term.

- **[[Thm - Complex Representations of U(1) and SU(2)]]** — the representation-theoretic continuation. The characters $\varrho_k:z\mapsto z^k$ classified there are, through $\Phi$, the rotation modes $R(\varphi)\mapsto e^{ik\varphi}$ of $SO(2)$; the isomorphism of this theorem is what makes the abelian representation theory of the circle simultaneously the representation theory of planar rotations, so that the two need never be proved twice.

---

# Unlocked by This

> [!tip] The circle as $\mathbb{R}/2\pi\mathbb{Z}$ *(from Lie theory)*
> Combining this theorem with the exponential map $\theta\mapsto e^{i\theta}$ of $U(1)$, whose kernel is $2\pi\mathbb{Z}$, presents both $U(1)$ and $SO(2)$ as the quotient group $\mathbb{R}/2\pi\mathbb{Z}$. This is the abelian, one-dimensional model that **Ex - Products of Lie Groups and the Torus** generalises to the $n$-torus $T^n = \mathbb{R}^n/\mathbb{Z}^n = U(1)^n$.

> [!tip] $U(1)$-gauge theory as electromagnetism *(from mathematical physics)*
> Because $U(1)\cong SO(2)$ is abelian, a connection on a principal $U(1)$-bundle has curvature $F = dA$ with no self-interaction term, and this is exactly Maxwell's electromagnetism written in the language of connections. The identification made here is the reason the electromagnetic gauge group may be pictured indifferently as phase rotations $e^{i\varphi}$ or as planar rotations $R(\varphi)$.
