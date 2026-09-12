---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - The Brouwer Degree is an Integer and a Homotopy Invariant"
  - "Ex - SU(2) is the Group of Unit Quaternions"
  - "Ex - Computing exp on su(2) via the Quaternion Formula"
  - "Def - Brouwer Degree of a Map"
  - "Def - Regular and Critical Points"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

For an integer $k\in\mathbb{Z}$, consider the two power maps of compact Lie groups:
$$p_k\colon S^1\to S^1,\quad z\mapsto z^k \qquad\text{and}\qquad P_k\colon S^3\to S^3,\quad q\mapsto q^k,$$
where $S^1=U(1)=\{z\in\mathbb{C}:|z|=1\}$ with its standard orientation, and $S^3=SU(2)=Sp(1)=\{q\in\mathbb{H}:|q|=1\}$ is the group of unit quaternions, oriented as the boundary of the closed unit ball in $\mathbb{H}=\mathbb{R}^4$ with standard orientation $(1,i,j,k)$. Prove that both maps have degree $k$:
$$\deg p_k = k \qquad\text{and}\qquad \deg P_k = k.$$

The intended route is a regular-value count. For the circle, count the $k$-th roots of a regular value and read the sign of the derivative. For $SU(2)$, show that $q_0=i$ is a regular value whose preimage is the $k$ points $e^{\theta_j i}=\cos\theta_j+i\sin\theta_j$ with
$$\theta_j=\frac{\pi/2+2\pi j}{k},\qquad j=0,1,\dots,k-1,$$
all lying on the circle $C=\{e^{\theta i}:\theta\in\mathbb{R}\}$ of unit quaternions commuting with $i$; then compute the Jacobian at each preimage using the quaternion exponential and read off that every sign is $+1$.

**Recall:**

The objects in play are the Brouwer degree and its regular-value formula, regular values and the sign of a Jacobian, the identification of $SU(2)$ with the unit quaternions, and the quaternion exponential formula.

![[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant#Statement]]

We use clause **(b)**: *for closed oriented $n$-manifolds $M,N$ with $N$ connected and a smooth $f\colon M\to N$, every regular value $y$ satisfies*
$$\deg f = \sum_{x\in f^{-1}(y)}\operatorname{sign}\det df_x,$$
*and this is an integer independent of the regular value.* We also use clause **(e)**, multiplicativity $\deg(g\circ f)=\deg g\cdot\deg f$, and clause **(d)**, that a non-surjective map has degree $0$; and, for orientation bookkeeping, the definition of degree from [[Def - Brouwer Degree of a Map]].

![[Def - Regular and Critical Points#The Definition]]

A point $x\in M$ is a **regular point** of a smooth map $f\colon M\to N$ between manifolds of the same dimension if $df_x\colon T_xM\to T_{f(x)}N$ is an isomorphism; $y\in N$ is a **regular value** if every $x\in f^{-1}(y)$ is a regular point (vacuously so if $y\notin f(M)$).

![[Ex - SU(2) is the Group of Unit Quaternions#Problem Statement]]

The quaternions are $\mathbb{H}=\{a+bi+cj+dk:a,b,c,d\in\mathbb{R}\}$ with $i^2=j^2=k^2=-1$, $ij=k=-ji$, $jk=i=-kj$, $ki=j=-ik$, conjugate $\overline{a+bi+cj+dk}=a-bi-cj-dk$, and norm $|q|^2=q\bar q=a^2+b^2+c^2+d^2$. The group $Sp(1)$ of unit quaternions is a Lie group under quaternion multiplication, diffeomorphic and isomorphic to $SU(2)$ and, as a manifold, to $S^3\subset\mathbb{R}^4$. Its Lie algebra is the space of imaginary quaternions $\operatorname{Im}\mathbb{H}=\{bi+cj+dk\}=T_1 S^3$, with bracket the commutator.

![[Ex - Computing exp on su(2) via the Quaternion Formula#Problem Statement]]

For a *unit* imaginary quaternion $u$ (so $u\in\operatorname{Im}\mathbb{H}$, $|u|=1$, hence $u^2=-1$) and $\theta\in\mathbb{R}$, the exponential is
$$\exp(\theta u)=\cos\theta+u\sin\theta,$$
and every unit quaternion is of this form. In particular $t\mapsto\exp(tu)$ is a one-parameter subgroup, so $\exp(\theta u)^k=\exp(k\theta u)=\cos(k\theta)+u\sin(k\theta)$.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-degree-by-counting-preimages* problem, the canonical use of clause (b) of the degree theorem. The whole content is: choose a convenient regular value, list its preimages, and add up the signs of the Jacobian determinant at each. The circle case is the toy model in which every ingredient is visible on a one-dimensional tangent space; the $SU(2)$ case is the same computation carried out on the three-dimensional tangent space of $S^3$, where the only extra labour is a $3\times 3$ determinant, and even that collapses to a $1\times 1$ times a $2\times 2$ block once we exploit that all preimages sit on a single circle.

**Assumption pattern.** The recognisable signal that a regular-value count is the right tool is that the map is *algebraic and explicit* (here a power in a group), so that both the preimages of a point and the derivative can be written down in closed form. The second signal is that the group structure lets us trivialise the tangent bundle by left translation: a Lie group carries a global frame $g\mapsto\{g\xi_1,g\xi_2,\dots\}$ obtained by left-translating a basis of the Lie algebra, and in this frame the derivative of the $k$-th power map has a clean product-rule expression $dP_k{}_g(g\xi)=\sum_{m=1}^{k}g^m\xi g^{k-m}$. The third signal, specific to $SU(2)$, is that the chosen regular value $i$ has a large centraliser, forcing all preimages onto the maximal torus $C=\{e^{\theta i}\}$; this is what reduces a computation on $S^3$ to a computation essentially on a circle.

**Theorem routing.** For $S^1$: pick the regular value $1$; solve $z^k=1$ to get the $k$-th roots of unity; in the angle coordinate $\theta\mapsto e^{i\theta}$ the map is $\theta\mapsto k\theta$, derivative $k$, sign $\operatorname{sign}(k)$; apply clause (b), $\deg p_k=\sum\operatorname{sign}(k)=k$ (for $k\ge1$), and clauses (d)/(e) for $k\le 0$. For $S^3$: pick $q_0=i$; show every preimage commutes with $i$ hence lies on $C=\{e^{\theta i}\}$; solve on $C$ to get the $k$ points $\theta_j=(\pi/2+2\pi j)/k$; compute $dP_k$ at each in the left-invariant frame $\{qi,qj,qk\}$ using the product rule and the exponential formula; find the Jacobian block-diagonal with blocks $[k]$ and a rotation-scaling of positive determinant, so its determinant has sign $\operatorname{sign}(k)$; conclude $i$ is a regular value and $\deg P_k=k$ by clause (b). Clauses (d)/(e) again cover $k\le 0$.

**Key decision point.** Three choices carry the proof. First, *use the angle/left-invariant coordinates*, not the ambient $\mathbb{R}^2$ or $\mathbb{R}^4$ coordinates, so that the derivative is a genuine endomorphism of the tangent space of the sphere and its determinant is meaningful. Second, on $S^3$, *choose the regular value $i$ rather than $1$*: the value $1=P_k(1)$ has the awkward preimage $1$ where the whole maximal torus is nearly fixed and the count is degenerate, whereas $i$ is not a $k$-th power of a real point and its preimages are cleanly spread around the torus. Third, *do not try to pin the global orientation of the left-invariant frame*: because $dP_k$ maps $T_qS^3$ to $T_iS^3$ and we express both in the same global left-invariant frame, an overall orientation sign of that frame appears once at the source and once at the target and cancels, so the sign of the determinant in the left-invariant frame already equals the sign relative to the true orientation. Recognising this cancellation saves the entire bookkeeping of the $S^3=\partial B^4$ orientation.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles#Legal Operations|the topic page's Legal Operations]]:

1. **Compute a degree by the signed regular-value count.** Apply clause (b) of the degree theorem: choose a regular value $y$ and evaluate $\deg f=\sum_{x\in f^{-1}(y)}\operatorname{sign}\det df_x$. Legal because $f$ is smooth between closed oriented equidimensional manifolds and $y$ is verified regular.

2. **Solve the fibre of a group power map by roots.** List $f^{-1}(y)$ explicitly by solving $z^k=y$ (roots of unity times a particular root) on $S^1$, and $q^k=i$ on $S^3$.

3. **Confine preimages to a maximal torus via the centraliser.** On $S^3$, observe that any $q$ with $q^k=i$ commutes with $i$, and the centraliser of $i$ in $Sp(1)$ is the circle $C=\{e^{\theta i}\}$; hence all preimages lie on $C$, reducing the fibre to a one-variable equation.

4. **Trivialise the tangent bundle of a Lie group by left translation, and differentiate the power map by the product rule.** Use the global frame $q\mapsto\{qi,qj,qk\}$ and the identity $dP_k{}_q(q\xi)=\sum_{m=1}^{k}q^m\xi\,q^{k-m}$ obtained from the product rule for $q\mapsto q^k$.

5. **Read the sign of a Jacobian in a global frame, using that the frame's orientation cancels between source and target.** Because $dP_k$ has the same manifold with the same orientation as source and target and both are expressed in the same left-invariant frame, $\operatorname{sign}\det dP_k$ in that frame equals its sign relative to the chosen orientation.

6. **Extend from positive $k$ to all integers by multiplicativity and non-surjectivity.** Use clause (e), $\deg(f\circ g)=\deg f\cdot\deg g$, with the degree $-1$ of quaternion conjugation $q\mapsto\bar q=q^{-1}$, and clause (d) for the constant map $k=0$.

---

# Hints

> [!note]- Hint 1
> Both maps are smooth self-maps of a closed oriented manifold with itself, so clause (b) of the degree theorem applies: $\deg f=\sum_{x\in f^{-1}(y)}\operatorname{sign}\det df_x$ for any regular value $y$. For the circle, take $y=1$ and solve $z^k=1$. How many solutions, and what is the derivative of $z\mapsto z^k$ in the angle coordinate?

> [!note]- Hint 2
> On $S^1$, write $z=e^{i\theta}$; then $p_k(e^{i\theta})=e^{ik\theta}$, so in the angle coordinate $p_k$ is $\theta\mapsto k\theta$ with derivative $k$ everywhere. There are $|k|$ preimages of $1$ (the $k$-th roots of unity), each contributing $\operatorname{sign}(k)$. Sum to get $\deg p_k=k$ for $k\ge1$; handle $k\le0$ by multiplicativity ($p_{-1}=$ conjugation, degree $-1$) and $k=0$ by non-surjectivity.

> [!note]- Hint 3
> On $S^3$, choose the regular value $q_0=i$. If $q^k=i$ then $q$ commutes with $q^k=i$. Which unit quaternions commute with $i$? Show they are exactly $\{a+bi\}$, the circle $C=\{e^{\theta i}\}$. So the equation $q^k=i$ becomes $e^{ik\theta}=e^{i\pi/2}$ on $C$, giving $\theta_j=(\pi/2+2\pi j)/k$, $j=0,\dots,k-1$: exactly $k$ preimages.

> [!note]- Hint 4
> Differentiate the power map by the product rule: with the left-invariant frame $q\xi$ ($\xi\in\{i,j,k\}$), $dP_k{}_q(q\xi)=\sum_{m=1}^{k}q^m\xi\,q^{k-m}$. At $q=e^{i\theta_j}$ use that $i$ commutes with $q$ but $j,k$ anticommute with $i$ (so $j\,e^{i\alpha}=e^{-i\alpha}j$). You will find $dP_k(qi)=-k$ (a multiple of $e_1$ at $i$) and that $qj,qk$ map into the $j,k$-plane by a matrix whose determinant is $|S|^2>0$ with $S=\sum_{m=1}^{k}e^{i(2m-k)\theta_j}\ne0$. Hence $\det dP_k=k\,|S|^2$, sign $=\operatorname{sign}(k)$, so $i$ is regular and $\deg P_k=\sum_{j}(+1)=k$.

---

# Solution

The plan is one regular-value count on each manifold. On $S^1$ everything is one-dimensional: $z\mapsto z^k$ is $\theta\mapsto k\theta$ in the angle coordinate, so at each of the $k$ preimages of $1$ the derivative is $k$ and the degree is $k$. On $S^3$ the same idea runs on the three-dimensional tangent space: the regular value $i$ has all its preimages on the circle $C=\{e^{\theta i}\}$ of quaternions commuting with $i$ (there are $k$ of them), and a product-rule computation of the differential in a left-invariant frame shows the Jacobian at each is block-diagonal with positive-sign determinant, so again the degree is $k$. Both extend to negative $k$ by composing with quaternion conjugation, which has degree $-1$.

## Part I — the circle, $\deg p_k=k$

**Step 1: The angle coordinate turns $p_k$ into $\theta\mapsto k\theta$; $1$ is a regular value with $|k|$ preimages.**

Assume first $k\ge1$. In the coordinate $\theta\mapsto e^{i\theta}$ the map is $e^{i\theta}\mapsto e^{ik\theta}$; the value $1$ is regular with preimage the $k$-th roots of unity.

> [!note]- Derivation
> Parametrise $S^1$ by the orientation-preserving local coordinate $\theta\mapsto e^{i\theta}$; the standard orientation of $S^1=U(1)$ is the one for which $\partial_\theta$ is positive, i.e. the boundary orientation of the unit disc. In this coordinate
> $$p_k(e^{i\theta}) = (e^{i\theta})^k = e^{ik\theta},$$
> so $p_k$ is represented by the map $\theta\mapsto k\theta$ (mod $2\pi$). Its derivative in the coordinate is the constant
> $$\frac{d}{d\theta}(k\theta) = k \neq 0,$$
> so every point is regular and hence **every** value is regular; in particular $y=1$ is a regular value. Its preimage is the solution set of $e^{ik\theta}=1$, that is $k\theta\in2\pi\mathbb{Z}$, giving on the circle the $k$ distinct points
> $$z_j = e^{2\pi i j/k},\qquad j=0,1,\dots,k-1.$$
> These are the $k$-th roots of unity, and there are exactly $k$ of them.

**Step 2: Each preimage contributes $+1$; sum to $k$.**

The derivative $k>0$ has positive sign at every preimage, so clause (b) gives $\deg p_k=\sum_{j}(+1)=k$.

> [!note]- Derivation
> At each $z_j$ the source and target of $d(p_k)_{z_j}$ are the same oriented line $T_{z_j}S^1\to T_1S^1$, both trivialised by $\partial_\theta$, and the derivative is multiplication by $k$. Hence for $k\ge1$
> $$\operatorname{sign}\det d(p_k)_{z_j} = \operatorname{sign}(k) = +1 \qquad(j=0,\dots,k-1).$$
> By clause **(b)** of [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]], evaluated at the regular value $1$,
> $$\deg p_k = \sum_{j=0}^{k-1}\operatorname{sign}\det d(p_k)_{z_j} = \sum_{j=0}^{k-1}(+1) = k.$$

**Step 3: Extend to all integers $k$.**

For $k=0$ the map is constant, degree $0$; for $k<0$ use that conjugation $z\mapsto\bar z=z^{-1}$ has degree $-1$ and multiplicativity.

> [!note]- Derivation
> If $k=0$ then $p_0\equiv1$ is constant, hence not surjective onto the connected $1$-manifold $S^1$, so $\deg p_0=0$ by clause **(d)**; and indeed $0=k$.
>
> If $k<0$, write $k=-|k|$ and factor $p_k=p_{|k|}\circ\iota$ where $\iota(z)=z^{-1}=\bar z$, since $\iota(z)^{|k|}=z^{-|k|}=z^k$. The map $\iota\colon S^1\to S^1$, $e^{i\theta}\mapsto e^{-i\theta}$, is the reflection $\theta\mapsto-\theta$; in the angle coordinate its derivative is $-1$ at the single regular preimage of any point, so $\deg\iota=-1$. By clause **(e)** (multiplicativity of the degree),
> $$\deg p_k = \deg\big(p_{|k|}\circ\iota\big) = \deg p_{|k|}\cdot\deg\iota = |k|\cdot(-1) = -|k| = k.$$
> Thus $\deg p_k=k$ for every $k\in\mathbb{Z}$.

## Part II — the sphere, $\deg P_k=k$

Throughout Part II assume $k\ge1$; the case $k\le0$ is disposed of at the end exactly as in Step 3.

**Step 4: The differential of the power map in a left-invariant frame.**

Left-translating a basis of $\operatorname{Im}\mathbb{H}$ gives a global frame; in it, $dP_k{}_q(q\xi)=\sum_{m=1}^{k}q^m\xi\,q^{k-m}$.

> [!note]- Derivation
> For $q\in S^3$ the tangent space is $T_qS^3=\{v\in\mathbb{H}:\operatorname{Re}(\bar q v)=0\}=q\cdot\operatorname{Im}\mathbb{H}$, since $v=q\xi$ with $\xi\in\operatorname{Im}\mathbb{H}$ satisfies $\operatorname{Re}(\bar q\,q\xi)=|q|^2\operatorname{Re}(\xi)=0$ and $\dim(q\operatorname{Im}\mathbb{H})=3$. Thus $q\mapsto(qi,qj,qk)$ is a global frame of $TS^3$ obtained by left translation of the basis $(i,j,k)$ of $\operatorname{Im}\mathbb{H}=T_1S^3$.
>
> To differentiate $P_k(q)=q^k$ at $q$ in the direction $q\xi$, take the curve $h(t)=q\exp(t\xi)$ on $S^3$, with $h(0)=q$ and $h'(0)=q\xi$ (by the exponential formula, $\frac{d}{dt}\big|_0\exp(t\xi)=\xi$). Then $P_k(h(t))=h(t)^k$, and the product rule for the $k$-fold product $h(t)^k=h(t)\cdots h(t)$ gives
> $$\frac{d}{dt}\Big|_0 h(t)^k = \sum_{m=0}^{k-1} h(0)^m\,h'(0)\,h(0)^{k-1-m} = \sum_{m=0}^{k-1} q^m\,(q\xi)\,q^{k-1-m} = \sum_{m=1}^{k} q^m\,\xi\,q^{k-m}.$$
> (The only fact used is that quaternion multiplication is bilinear and associative, so the Leibniz rule holds slot by slot; no commutativity is assumed.) Hence
> $$dP_k{}_q(q\xi) = \sum_{m=1}^{k} q^m\,\xi\,q^{k-m},\qquad \xi\in\{i,j,k\}.$$
> As a check, $k=1$ gives $dP_1{}_q(q\xi)=q\xi$, correct since $P_1=\operatorname{id}$.

**Step 5: The regular value $i$ and its $k$ preimages on the circle $C=\{e^{\theta i}\}$.**

Any $q$ with $q^k=i$ commutes with $i$, hence lies on $C$; on $C$ the equation is $e^{ik\theta}=i$, giving $\theta_j=(\pi/2+2\pi j)/k$, $j=0,\dots,k-1$.

> [!note]- Derivation
> **All preimages commute with $i$.** If $P_k(q)=q^k=i$, then $q$ commutes with its own power $q^k$, so $qi=iq$.
>
> **The centraliser of $i$ is the circle $C$.** Write $q=a+bi+cj+dk$. Using $ij=k,\ ji=-k,\ ik=-j,\ ki=j$,
> $$qi = (a+bi+cj+dk)i = ai - b + c(ji) + d(ki) = -b + ai - ck + dj,$$
> $$iq = i(a+bi+cj+dk) = ai - b + c(ij) + d(ik) = -b + ai + ck - dj.$$
> Equating, $qi=iq$ forces $-ck+dj=ck-dj$, i.e. $c=d=0$. Thus $q=a+bi\in\mathbb{C}\subset\mathbb{H}$, and being a unit quaternion, $a^2+b^2=1$, so
> $$q\in C:=\{e^{\theta i}=\cos\theta+i\sin\theta:\theta\in\mathbb{R}\},$$
> the maximal torus through $i$. Every preimage of $i$ therefore lies on $C$.
>
> **Solving on $C$.** For $q=e^{\theta i}$, $q^k=e^{ik\theta}$ (Step for the exponential; on $C$ quaternion multiplication is ordinary complex multiplication). The equation $q^k=i=e^{i\pi/2}$ is $e^{ik\theta}=e^{i\pi/2}$, i.e.
> $$k\theta \equiv \tfrac{\pi}{2}\pmod{2\pi}\quad\Longleftrightarrow\quad \theta = \theta_j:=\frac{\pi/2+2\pi j}{k},\qquad j=0,1,\dots,k-1,$$
> which are $k$ distinct points of $C$ modulo $2\pi$. Hence
> $$P_k^{-1}(i) = \{\,q_j = e^{\theta_j i}: j=0,\dots,k-1\,\},\qquad |P_k^{-1}(i)|=k.$$
> Regularity of $i$ is verified in Step 6 by showing $\det dP_k{}_{q_j}\ne0$ at each $q_j$.

**Step 6: The Jacobian at each $q_j$ is block-diagonal with determinant $k\,|S_j|^2>0$.**

Computing $dP_k{}_{q_j}$ on the frame $(q_ji,q_jj,q_jk)$ and reading it in the target frame at $i$ gives a block form $\operatorname{diag}\big(k,\ R\big)$ with $R$ the $2\times2$ block $\left(\begin{smallmatrix}\beta&\alpha\\-\alpha&\beta\end{smallmatrix}\right)$ and $\alpha+i\beta=S_j\ne0$.

> [!note]- Derivation
> Abbreviate $q=q_j=e^{\theta i}$ with $\theta=\theta_j$, so $q^m=e^{im\theta}$ and $q^k=i$. Recall two algebraic facts on $C$: $i$ commutes with $e^{i\alpha}$; and $j,k$ *anticommute* with $i$, so
> $$j\,e^{i\alpha} = e^{-i\alpha}\,j,\qquad k\,e^{i\alpha} = e^{-i\alpha}\,k \qquad\text{(since }ji=-ij,\ ki=-ik\text{).}$$
> Apply the differential formula of Step 4 to each basis direction.
>
> **Direction $\xi=i$.** Since $i$ commutes with each $e^{im\theta}$,
> $$dP_k{}_q(qi) = \sum_{m=1}^{k} e^{im\theta}\,i\,e^{i(k-m)\theta} = \sum_{m=1}^{k} i\,e^{ik\theta} = \sum_{m=1}^{k} i\cdot i = \sum_{m=1}^{k}(-1) = -k .$$
> So $dP_k{}_q(qi)=-k$, the real quaternion $-k\cdot1$.
>
> **Direction $\xi=j$.** Moving each $e^{im\theta}$ to the right past $j$ flips its sign in the exponent:
> $$dP_k{}_q(qj) = \sum_{m=1}^{k} e^{im\theta}\,j\,e^{i(k-m)\theta} = \sum_{m=1}^{k} e^{im\theta}e^{-i(k-m)\theta}\,j = \Big(\sum_{m=1}^{k} e^{i(2m-k)\theta}\Big)j =: S_j\,j,$$
> where $S_j:=\sum_{m=1}^{k}e^{i(2m-k)\theta}\in\mathbb{C}$. Write $S_j=\alpha+i\beta$ with $\alpha,\beta\in\mathbb{R}$; then $S_j j=(\alpha+i\beta)j=\alpha j+\beta(ij)=\alpha j+\beta k$.
>
> **Direction $\xi=k$.** Identically (the same anticommutation), $dP_k{}_q(qk)=S_j\,k=\alpha k+\beta(ik)=\alpha k-\beta j$.
>
> **The target frame at $i$.** The left-invariant frame at the image point $i$ is $(i\cdot i,\ i\cdot j,\ i\cdot k)=(-1,\ k,\ -j)$; call these $e_1,e_2,e_3$. Read the three images in this frame:
> $$dP_k{}_q(qi) = -k\cdot 1 = k\cdot(-1) = k\,e_1,$$
> $$dP_k{}_q(qj) = \alpha j+\beta k = \beta e_2 - \alpha e_3 \qquad(\text{using }k=e_2,\ j=-e_3),$$
> $$dP_k{}_q(qk) = \alpha k-\beta j = \alpha e_2 + \beta e_3 .$$
> Thus in the ordered bases $(qi,qj,qk)\to(e_1,e_2,e_3)$ the matrix of $dP_k{}_q$ is block-diagonal,
> $$[dP_k{}_q] = \begin{pmatrix} k & 0 & 0\\ 0 & \beta & \alpha\\ 0 & -\alpha & \beta \end{pmatrix},$$
> with determinant
> $$\det[dP_k{}_q] = k\cdot\det\begin{pmatrix}\beta & \alpha\\ -\alpha & \beta\end{pmatrix} = k\,(\beta^2+\alpha^2) = k\,|S_j|^2 .$$
>
> **$S_j\ne0$, so $i$ is regular.** Summing the geometric series (valid since $e^{2i\theta}\ne1$, verified below),
> $$S_j = \sum_{m=1}^{k}e^{i(2m-k)\theta} = e^{-ik\theta}\sum_{m=1}^{k}e^{2im\theta} = e^{-ik\theta}\,e^{2i\theta}\,\frac{e^{2ik\theta}-1}{e^{2i\theta}-1}.$$
> Now $e^{ik\theta}=e^{i\pi/2}=i$ gives $e^{-ik\theta}=-i$ and $e^{2ik\theta}=i^2=-1$, so $e^{2ik\theta}-1=-2$ and
> $$S_j = (-i)\,e^{2i\theta}\,\frac{-2}{e^{2i\theta}-1} = \frac{2i\,e^{2i\theta}}{e^{2i\theta}-1}\neq 0,$$
> the numerator being nonzero. The denominator is nonzero because $e^{2i\theta}=1$ would force $\theta\in\pi\mathbb{Z}$, whence $k\theta\in k\pi\mathbb{Z}\subset\pi\mathbb{Z}$; but $k\theta=\pi/2+2\pi j$ is an odd multiple of $\pi/2$, never a multiple of $\pi$. Hence $|S_j|^2>0$, $\det[dP_k{}_q]=k|S_j|^2\ne0$, so $q_j$ is a regular point; as this holds for every $j$, the value $i$ is regular.

**Step 7: Every sign is $+1$; the frame orientation cancels; $\deg P_k=k$.**

The determinant sign in the left-invariant frame equals the sign relative to the true orientation because the frame's global orientation appears identically at source and target; hence each preimage contributes $\operatorname{sign}(k)=+1$ and $\deg P_k=k$.

> [!note]- Derivation
> The left-invariant frame $E=(gi,gj,gk)$ is a *global* frame on the connected manifold $S^3$, so its orientation relative to the fixed orientation (the $S^3=\partial B^4$ boundary orientation) is a single sign $\varepsilon\in\{+1,-1\}$, the same at every point $g$. For a linear isomorphism $L=dP_k{}_{q_j}\colon T_{q_j}S^3\to T_iS^3$, the sign of its determinant relative to the chosen orientations equals
> $$\operatorname{sign}\det L\big|_{\text{oriented}} = \operatorname{sign}\det[L]_{E\to E}\cdot\varepsilon_{\text{target}}\cdot\varepsilon_{\text{source}},$$
> where $[L]_{E\to E}$ is the matrix in the left-invariant frames and $\varepsilon_{\text{source}}=\varepsilon_{\text{target}}=\varepsilon$ because source and target are the same manifold $S^3$ with the same orientation and the same global frame. Since $\varepsilon^2=+1$,
> $$\operatorname{sign}\det L\big|_{\text{oriented}} = \operatorname{sign}\det[dP_k{}_{q_j}]_{E\to E} = \operatorname{sign}\big(k\,|S_j|^2\big) = \operatorname{sign}(k) = +1 \qquad(k\ge1).$$
> This is why we never needed to determine $\varepsilon$ itself. By clause **(b)** of [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]] at the regular value $i$,
> $$\deg P_k = \sum_{j=0}^{k-1}\operatorname{sign}\det dP_k{}_{q_j} = \sum_{j=0}^{k-1}(+1) = k .$$

**Step 8: All integers $k$.**

Conjugation $q\mapsto\bar q=q^{-1}$ has degree $-1$; multiplicativity and non-surjectivity give the remaining cases.

> [!note]- Derivation
> For $k=0$, $P_0\equiv1$ is constant, not surjective onto the connected $3$-manifold $S^3$, so $\deg P_0=0=k$ by clause **(d)**.
>
> For $k<0$, factor $P_k=P_{|k|}\circ\operatorname{inv}$ with $\operatorname{inv}(q)=q^{-1}=\bar q$ (unit quaternions have $q^{-1}=\bar q$), since $\operatorname{inv}(q)^{|k|}=q^{-|k|}=q^k$. Quaternion conjugation $q=a+bi+cj+dk\mapsto\bar q=a-bi-cj-dk$ is the restriction to $S^3$ of the linear map $\operatorname{diag}(1,-1,-1,-1)$ on $\mathbb{R}^4=\mathbb{H}$, which is an orthogonal transformation of determinant $-1$, i.e. orientation-reversing on $\mathbb{R}^4$; it therefore reverses the boundary orientation of $S^3$, so $\deg\operatorname{inv}=-1$ (equivalently, by [[Ex - The Antipodal Map of S^n has Degree Minus One to the Power n plus 1|the reflection/antipode count]], a single reflection has degree $-1$). By clause **(e)**,
> $$\deg P_k = \deg P_{|k|}\cdot\deg\operatorname{inv} = |k|\cdot(-1) = -|k| = k .$$
> Hence $\deg P_k=k$ for every $k\in\mathbb{Z}$, completing Part II.

> [!note]- Complete formal solution
> **Claim.** $\deg(z\mapsto z^k)=k$ on $S^1$ and $\deg(q\mapsto q^k)=k$ on $S^3=Sp(1)$, for every $k\in\mathbb{Z}$.
>
> *Circle.* For $k\ge1$, in the coordinate $\theta\mapsto e^{i\theta}$ the map is $\theta\mapsto k\theta$, derivative $k\ne0$, so every value is regular; $1$ has the $k$ preimages $e^{2\pi ij/k}$ ($j=0,\dots,k-1$), each with $\operatorname{sign}\det=\operatorname{sign}(k)=+1$. By the regular-value formula (clause (b)), $\deg p_k=k$. For $k=0$, $p_0$ is constant, degree $0$ (clause (d)); for $k<0$, $p_k=p_{|k|}\circ(z\mapsto\bar z)$ and $z\mapsto\bar z$ has degree $-1$, so $\deg p_k=-|k|=k$ (clause (e)).
>
> *Sphere.* For $k\ge1$, take the value $i$. Any $q$ with $q^k=i$ commutes with $i$; the centraliser of $i$ in $Sp(1)$ is $C=\{e^{\theta i}\}$, so all preimages lie on $C$, where $q^k=e^{ik\theta}=i$ gives the $k$ points $q_j=e^{\theta_j i}$, $\theta_j=(\pi/2+2\pi j)/k$. Using the left-invariant frame $(qi,qj,qk)$ and $dP_k{}_q(q\xi)=\sum_{m=1}^{k}q^m\xi q^{k-m}$ together with $ie^{i\alpha}=e^{i\alpha}i$ and $\{j,k\}e^{i\alpha}=e^{-i\alpha}\{j,k\}$, one finds at each $q_j$
> $$dP_k{}_{q_j}(qi)=-k=k\,e_1,\quad dP_k{}_{q_j}(qj)=S_j j=\beta e_2-\alpha e_3,\quad dP_k{}_{q_j}(qk)=S_j k=\alpha e_2+\beta e_3,$$
> with $(e_1,e_2,e_3)=(i^2,ij,ik)$ the target frame and $S_j=\alpha+i\beta=\sum_{m=1}^{k}e^{i(2m-k)\theta_j}=\dfrac{2ie^{2i\theta_j}}{e^{2i\theta_j}-1}\ne0$. Thus $\det[dP_k{}_{q_j}]=k|S_j|^2\ne0$, so $i$ is a regular value, and since source and target carry the same orientation and the same global frame the sign is $\operatorname{sign}(k)=+1$ at each of the $k$ preimages. By clause (b), $\deg P_k=k$. The cases $k\le0$ follow from $\deg\operatorname{inv}=-1$ (conjugation is orientation-reversing) and clauses (d),(e) exactly as on the circle. $\blacksquare$

> [!warning] Illegal but tempting shortcut: "$\det dP_k=k^3$ because the derivative multiplies each of the three directions by $k$."
> On the circle the derivative genuinely is multiplication by $k$, and one is tempted to guess that on $S^3$ the power map multiplies each tangent direction by $k$, giving $\det=k^3$ and hence $|k^3|$ preimages worth of... — this is wrong twice over. First, the differential is *not* scalar: only the $i$-direction (the tangent to the maximal torus $C$) is scaled by $k$; the $j,k$-directions are rotated and scaled by the complex number $S_j$, whose modulus is generally not $k$. Second, the degree is the *signed count at one regular value*, not $\det dP_k$ at a single point — the value $|S_j|^2$ enters only through its sign, and the number of preimages is $k$, not $k^3$. The scalar guess would also contradict the fact that $\deg$ must be linear in the winding, which the correct computation confirms: exactly $k$ preimages each of sign $+1$. The condition under which a "multiply each direction by $k$" picture *is* correct is the abelian case $C$ itself (or $S^1$), where the group is one-dimensional and there are no transverse directions to rotate.

> [!note]- Independent check via the additive winding functional (alternative route)
> There is a second, coordinate-free proof of $\deg P_k=k$ on $S^3$ that the classification page will use. For smooth $g\colon S^3\to SU(2)$ put $W(g):=\frac{1}{24\pi^2}\int_{S^3}\operatorname{tr}\big((g^{-1}dg)^{\wedge3}\big)$. On [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|the SU(2)-classification page]] it is proved (Lemma A) that $W(g_1g_2)=W(g_1)+W(g_2)$ for the pointwise product, and (Lemma B) that $W(g)=\deg g$. Taking $g_1=g_2=\cdots=$ the identity map $\operatorname{id}\colon S^3\to SU(2)$ and $g=\operatorname{id}^{\,k}=P_k$ (pointwise $k$-th power), additivity gives $W(P_k)=k\,W(\operatorname{id})=k\cdot1=k$, hence $\deg P_k=k$. This agrees with the regular-value count above and is recorded here only as a cross-check; the primary proof is the direct count, which needs nothing from §3.6.

---

# Key Takeaways

**A degree is a signed count at one regular value, and the entire skill is choosing the value and the coordinates that make the count transparent.** The regular-value formula $\deg f=\sum_{x\in f^{-1}(y)}\operatorname{sign}\det df_x$ converts a global invariant into a finite piece of local linear algebra, but only after two choices are made well: a regular value whose fibre is easy to list, and coordinates in which $df$ is easy to write. Here the group structure supplies both — the fibre is a set of roots, and left translation gives a global frame in which the power map differentiates by a product rule. The transferable reflex: whenever a self-map of a compact manifold is given by an explicit algebraic formula, do not integrate a pulled-back form; instead pick the cleanest value in the image, solve for its preimages exactly, and differentiate in the most symmetric available frame. The circle is the one-line rehearsal of exactly the manoeuvre the sphere then repeats in three dimensions.

**On a Lie group, left translation trivialises the tangent bundle and turns the power map's derivative into $\sum_{m=1}^{k}g^m\xi g^{k-m}$ — a formula whose non-commutativity is the whole story.** The identity $dP_k{}_g(g\xi)=\sum_{m=1}^k g^m\xi g^{k-m}$ is worth remembering in its own right; it is the Leibniz rule for a $k$-fold product read in the moving frame $g\xi$. When $g$ lies on a maximal torus and $\xi$ is tangent to that torus, every term commutes and the sum is simply $k\,g^k\xi$ — the "scalar $k$" behaviour, which is why the torus direction contributes the factor $k$ to the Jacobian. In the transverse directions $\xi$ *anticommutes* with the torus generator, each term picks up an alternating phase, and the sum becomes a geometric series $S_j$; its non-vanishing is what makes the value regular, and its modulus is invisible to the degree because only signs are counted. The lesson for spaced recall: on a nonabelian group the derivative of a power map is diagonal only relative to the splitting tangent-to-the-torus $\oplus$ transverse, and the two blocks behave completely differently — the torus block carries the winding, the transverse block carries only regularity.

**Signs of Jacobians can be computed in any convenient global frame, because a global frame's orientation cancels between source and target of an endomorphism.** This is a small but repeatedly useful principle: to find $\operatorname{sign}\det df_x$ for a self-map $f$ of an oriented manifold, one may use *any* smooth global frame — even one whose orientation relative to the manifold's is unknown — provided the same frame is used at $x$ and at $f(x)$, since the unknown sign appears squared and drops out. It saved us the entire computation of how the left-invariant frame $(gi,gj,gk)$ sits relative to the $S^3=\partial B^4$ orientation. The condition for the trick is exactly that source and target be the same oriented manifold with the same global frame; it fails for maps between different manifolds, or when only local frames of differing orientation are available, and there one must track the orientation honestly. Together with the companion result [[Ex - A Map Extending over a Bounding Manifold has Degree Zero|that a map extending over a filling has degree zero]], this exercise equips the clutching classification of §3.6 with both halves it needs: the power maps $z^d$ and $q^k$ realise every integer as a clutching degree, while the bounding-manifold vanishing shows that degree is the only invariant of the clutching function.
