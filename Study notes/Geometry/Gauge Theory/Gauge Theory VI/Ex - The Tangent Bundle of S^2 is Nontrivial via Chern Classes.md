---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - First Chern Class of a Line Bundle from Curvature"
  - "Def - The Levi-Civita Connection Viewed as a Connection on TM"
  - "Ex - The Levi-Civita Connection of the Round Sphere as a Connection Matrix"
  - "Def - Chern Classes"
tags: [geometry, gauge-theory]
---

# Problem Statement

Show that the tangent bundle $TS^2$ of the round two-sphere is **not trivial**, using Chern classes. This is Haydys's Exercise 89.

Concretely, the intended route is: equip the oriented Riemannian surface $S^2$ with the rotation-by-ninety-degrees endomorphism $I$ of each tangent plane, which makes $(TS^2,I)$ a Hermitian complex line bundle; show that the Levi-Civita connection is a unitary connection on this line bundle; compute its curvature $F$ in terms of the Gauss curvature $K$ and the area form $dA$; integrate $\tfrac{i}{2\pi}F$ over $S^2$ to obtain the first Chern number
$$c_1(TS^2)[S^2]=\int_{S^2}\tfrac{i}{2\pi}F=\frac1{2\pi}\int_{S^2}K\,dA=2\neq0;$$
and conclude, since a trivial line bundle has vanishing first Chern class, that $(TS^2,I)$ — and hence $TS^2$ itself — is non-trivial.

Throughout, $S^2\subset\mathbb R^3$ is the unit sphere with the round metric $g$ (in the coordinates $(\theta,\varphi)$ of colatitude and longitude, $g=d\theta^2+\sin^2\theta\,d\varphi^2$) and the orientation for which a positively oriented tangent frame $(v_1,v_2)$ is one with $(\nu,v_1,v_2)$ positive in $\mathbb R^3$, where $\nu$ is the outward unit normal. Its Gauss curvature is $K\equiv1$ and its area is $\int_{S^2}dA=4\pi$.

**Recall:**

The exercise combines three ingredients: that the first Chern class of a Hermitian line bundle is $[\tfrac{i}{2\pi}F]$ and detects non-triviality; that the Levi-Civita connection is a connection on $TM$ whose curvature is the Riemann tensor; and the explicit round-sphere curvature.

![[Thm - First Chern Class of a Line Bundle from Curvature#Statement]]

We use clause **(a)** ($c_1(L)=[\tfrac{i}{2\pi}F_A]$ for a Hermitian line bundle with unitary connection $A$, curvature $F_A\in\Omega^2(M;i\mathbb R)$) and clause **(c)** (if $c_1(L)\neq0$, equivalently if $\int_\Sigma F_A\neq0$ over a closed oriented surface, then $L$ is non-trivial).

![[Def - Chern Classes#The Definition]]

![[Def - The Levi-Civita Connection Viewed as a Connection on TM#The Definition]]

The Levi-Civita connection $\nabla$ of $(S^2,g)$ is the unique metric ($\nabla g=0$) torsion-free connection; regarded as a connection on the vector bundle $TS^2$, its curvature $F_\nabla\in\Omega^2(S^2;\operatorname{End}TS^2)$ is the Riemann curvature endomorphism, $F_\nabla(X,Y)=R(X,Y)$ with $R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z$.

From [[Ex - The Levi-Civita Connection of the Round Sphere as a Connection Matrix]] we recall the value of this curvature on the round sphere: in the coordinate frame $(\partial_\theta,\partial_\varphi)$,
$$R(\partial_\theta,\partial_\varphi)\partial_\varphi=\sin^2\theta\,\partial_\theta,$$
equivalently, in the oriented orthonormal frame $e_1=\partial_\theta$, $e_2=\tfrac1{\sin\theta}\partial_\varphi$, one has $R(e_1,e_2)e_2=e_1$, so the Gauss curvature is $K=g(R(e_1,e_2)e_2,e_1)=1$.

---

# Convergent Strategy

**Problem class.** This is a *non-triviality via a characteristic-number obstruction* problem: to prove a bundle is not trivial, exhibit a single characteristic number that is nonzero, since every characteristic number of a trivial bundle vanishes. The characteristic class must be one the bundle actually possesses; a real rank-$2$ bundle has no Chern classes on the nose, so the first move is to manufacture a complex structure and pass to a line bundle. The recognisable signature is "prove $E$ is non-trivial" together with enough geometry (a metric, an orientation) to compute curvature.

**Assumption pattern.** Two structural facts about a *surface* are doing the work, and both are special to real dimension two. First, an oriented Riemannian surface has a canonical complex structure $I$ (rotate each tangent vector by $+90^\circ$), turning the rank-$2$ real bundle $TS^2$ into a rank-$1$ complex bundle — this is what gives us a first Chern class to compute. Second, this $I$ is *parallel* for the Levi-Civita connection, because the holonomy of an oriented surface lies in $SO(2)$, which is abelian and commutes with $I$; parallelism of $I$ (together with $\nabla g=0$) is exactly what makes $\nabla$ a *unitary* connection, so that clause (a) of the first-Chern-class theorem applies. The trigger for the whole approach is: oriented Riemannian surface $\Rightarrow$ Hermitian line bundle with a distinguished unitary connection.

**Theorem routing.** Build $(TS^2,I,h)$; verify $\nabla$ is unitary (from $\nabla g=0$ and $\nabla I=0$); identify the curvature endomorphism $R(e_1,e_2)=-K\,I$ from [[Ex - The Levi-Civita Connection of the Round Sphere as a Connection Matrix|the round-sphere computation]] and metric skew-symmetry; translate the endomorphism $I$ into the complex scalar $i$ to read off the $i\mathbb R$-valued curvature $F=-iK\,dA$; apply [[Thm - First Chern Class of a Line Bundle from Curvature|clause (a)]] to get $c_1(TS^2)=[\tfrac{i}{2\pi}F]=[\tfrac1{2\pi}K\,dA]$ and integrate to $2$; then [[Thm - First Chern Class of a Line Bundle from Curvature|clause (c)]] gives non-triviality. Finally, a nowhere-vanishing real section is a nowhere-vanishing complex section, so non-triviality as a complex line bundle forces non-triviality as a real bundle.

**Key decision point.** The subtle move is the *identification of the real curvature endomorphism with a complex scalar*, because that is where the sign of the answer is decided. Once $TS^2$ is a complex line bundle, "multiplication by $i$" is by definition the operator $I$; so a curvature endomorphism of the form $c\,I$ (a real multiple of $I$) reads as the imaginary scalar $c\,i$. Getting the *direction* of $I$ right (rotate towards the orientation) and the *sign* of the Riemann endomorphism right (metric skew-symmetry sends $R(e_1,e_2)e_2=Ke_1$ to $R(e_1,e_2)e_1=-Ke_2$, i.e. $R(e_1,e_2)=-K I$) is what produces $c_1[S^2]=+2$ rather than $-2$. The absolute value already settles the exercise — any nonzero number proves non-triviality — but pinning the sign to $+2$ is what makes the answer agree with the Euler number $\chi(S^2)=2$.

---

# Legal Operations Used

1. **Turn an oriented Riemannian surface into a Hermitian line bundle.** Define $I$ by $I e_1=e_2$ on a positively oriented orthonormal frame; then $I^2=-1$, and $I$ is a metric-compatible complex structure, so $(TS^2,I)$ is a complex line bundle with Hermitian metric $h(v,w)=g(v,w)+i\,g(v,Iw)$.

2. **Use parallelism of the complex structure to certify a connection as unitary.** From $\nabla g=0$ and $\nabla I=0$ deduce $\nabla h=0$ and $\nabla(Iv)=I(\nabla v)$; a metric, complex-linear connection is unitary. This licenses the use of the first-Chern-class-from-curvature theorem.

3. **Import a known curvature and rewrite it via metric skew-symmetry.** Take $R(e_1,e_2)e_2=Ke_1$ from [[Ex - The Levi-Civita Connection of the Round Sphere as a Connection Matrix|the round-sphere connection-matrix exercise]] and use $g(R(X,Y)u,v)=-g(R(X,Y)v,u)$ to get the full endomorphism $R(e_1,e_2)=-KI$.

4. **Translate a real endomorphism into a complex scalar.** Under the complex structure $I\leftrightarrow i$, the skew endomorphism-valued curvature $-K\,dA\,I$ becomes the $i\mathbb R$-valued $2$-form $F=-iK\,dA$.

5. **Compute a first Chern number and read off non-triviality (clauses (a), (c)).** $c_1(TS^2)[S^2]=\int_{S^2}\tfrac{i}{2\pi}F$; a nonzero value forces the line bundle, hence the real bundle, to be non-trivial.

---

# Hints

> [!note]- Hint 1
> A real rank-$2$ bundle has no Chern classes as it stands. But $S^2$ is an *oriented Riemannian surface*: each tangent plane has a canonical rotation by $90^\circ$. What structure does that put on $TS^2$, and what invariant does that structure make available?

> [!note]- Hint 2
> Rotation by $90^\circ$ is a complex structure $I$ ($I^2=-1$), so $(TS^2,I)$ is a complex *line* bundle, and it has a first Chern class. To use $c_1=[\tfrac{i}{2\pi}F]$ you need a *unitary* connection. Why is the Levi-Civita connection unitary here? (Think about what $\nabla g=0$ gives, and whether $I$ is parallel.)

> [!note]- Hint 3
> In an oriented orthonormal frame the metric connection matrix is $\mathfrak{so}(2)$-valued and $I$ is the constant matrix $\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$; since $\mathfrak{so}(2)$ is abelian, $\nabla I=0$. Now compute the curvature. From the round-sphere exercise $R(e_1,e_2)e_2=Ke_1$ with $K=1$; use metric skew-symmetry to find $R(e_1,e_2)e_1$, and thereby the whole endomorphism $R(e_1,e_2)$ as a multiple of $I$.

> [!note]- Hint 4
> You should find $R(e_1,e_2)=-KI$, so as a $2$-form the curvature endomorphism is $-K\,dA\,I$. Since $I$ is "multiplication by $i$", the $i\mathbb R$-valued curvature is $F=-iK\,dA$. Then $\tfrac{i}{2\pi}F=\tfrac1{2\pi}K\,dA$; integrate over $S^2$ using $K\equiv1$ and $\int_{S^2}dA=4\pi$. A nonzero answer, together with clause (c), finishes it — but remember to argue that non-triviality as a complex line bundle implies non-triviality as a real bundle.

---

# Solution

The plan is to make $TS^2$ into a Hermitian line bundle by rotating each tangent plane by $90^\circ$, observe that the Levi-Civita connection is unitary for this structure because it is metric and the rotation is parallel, and then read the Riemann curvature — already known from the round-sphere computation — as an imaginary scalar $2$-form. Integrating $\tfrac{i}{2\pi}F$ gives the first Chern number $2$, which is nonzero, so the line bundle cannot be trivial; and a trivialisation of the real bundle would trivialise the line bundle, so $TS^2$ is non-trivial.

**Step 1: Make $TS^2$ a Hermitian complex line bundle.**

Rotation by $90^\circ$ defines a metric-compatible complex structure $I$ on $TS^2$, so $(TS^2,I)$ is a complex line bundle with Hermitian metric $h(v,w)=g(v,w)+i\,g(v,Iw)$.

> [!note]- Derivation
> Fix a point and a positively oriented orthonormal basis $(e_1,e_2)$ of the tangent plane (this exists locally as a smooth frame). Define $I$ by
> $$Ie_1=e_2,\qquad Ie_2=-e_1,$$
> that is, rotation by $+90^\circ$ in the direction of the orientation. This is independent of the oriented orthonormal frame chosen, because any two such frames differ by an element of $SO(2)$, which commutes with the rotation $I$; so $I$ is a globally well-defined bundle endomorphism of $TS^2$. It satisfies
> $$I^2 e_1=I e_2=-e_1,\qquad I^2 e_2=I(-e_1)=-e_2,\quad\text{so}\quad I^2=-\operatorname{id}.$$
> Hence $I$ is a complex structure, and declaring $i\cdot v:=Iv$ makes each fibre $T_pS^2$ a one-dimensional complex vector space: $(TS^2,I)$ is a complex line bundle.
>
> It is compatible with $g$: $I$ is an isometry, since on the orthonormal basis $g(Ie_1,Ie_2)=g(e_2,-e_1)=0=g(e_1,e_2)$ and $g(Ie_1,Ie_1)=g(e_2,e_2)=1=g(e_1,e_1)$, and by bilinearity $g(Iv,Iw)=g(v,w)$ for all $v,w$. Isometry with $I^2=-1$ gives skew-symmetry: replacing $w$ by $-I(Iw)=w$,
> $$g(Iv,w)=g\big(Iv,-I(Iw)\big)=-g\big(Iv,I(Iw)\big)=-g(v,Iw)\qquad\text{(by the isometry property)}.$$
> Define $h(v,w):=g(v,w)+i\,g(v,Iw)$. It is complex-linear in the first slot: using skew-symmetry $g(v,Iw)=-g(Iv,w)$,
> $$h(Iv,w)=g(Iv,w)+i\,g(Iv,Iw)=g(Iv,w)+i\,g(v,w),$$
> $$i\,h(v,w)=i\,g(v,w)+i^2 g(v,Iw)=i\,g(v,w)-g(v,Iw)=i\,g(v,w)+g(Iv,w),$$
> and the two right-hand sides agree, so $h(Iv,w)=i\,h(v,w)$. It is Hermitian, meaning $\overline{h(w,v)}=h(v,w)$: computing the left-hand side,
> $$\overline{h(w,v)}=\overline{g(w,v)+i\,g(w,Iv)}=g(w,v)-i\,g(w,Iv)=g(v,w)-i\,g(w,Iv)\qquad\text{(symmetry of }g\text{).}$$
> By skew-symmetry $g(v,Iw)=-g(Iv,w)$ together with the symmetry of $g$, we have $g(w,Iv)=g(Iv,w)=-g(v,Iw)$, so $-i\,g(w,Iv)=i\,g(v,Iw)$ and hence $\overline{h(w,v)}=g(v,w)+i\,g(v,Iw)=h(v,w)$, as required. It is positive-definite, since $h(v,v)=g(v,v)+i\,g(v,Iv)=g(v,v)>0$ for $v\neq0$ (using $g(v,Iv)=-g(Iv,v)=-g(v,Iv)$, so $g(v,Iv)=0$). Thus $h$ is a Hermitian structure with $|v|_h^2=g(v,v)$.

**Step 2: The Levi-Civita connection is unitary.**

Because $\nabla g=0$ and $\nabla I=0$, the Levi-Civita connection preserves $h$ and is complex-linear, hence is a unitary connection on $(TS^2,I,h)$.

> [!note]- Derivation
> Work in a *local oriented orthonormal frame* $(e_1,e_2)$. Because $\nabla$ is metric, its connection matrix in an orthonormal frame is skew-symmetric, i.e. $\mathfrak{so}(2)$-valued: $\nabla e=e\cdot A$ with
> $$A=\begin{pmatrix}0&-\alpha\\ \alpha&0\end{pmatrix},\qquad \alpha\in\Omega^1(U),$$
> for some real $1$-form $\alpha$ (this is the skew-symmetry of a metric connection in an orthonormal frame; see [[Def - The Levi-Civita Connection Viewed as a Connection on TM]]). In this frame $I$ is the *constant* matrix
> $$I=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}.$$
> The connection induced on $\operatorname{End}(TS^2)$ acts on a matrix-valued field $B$ by $\nabla B=dB+[A,B]$. Since $I$ has constant entries, $dI=0$; and since $A$ and $I$ are both multiples of the single generator $\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$ of the abelian Lie algebra $\mathfrak{so}(2)$, their commutator vanishes: $[A,I]=0$. Therefore
> $$\nabla I=dI+[A,I]=0.$$
> Equivalently, $\nabla(Iv)=I(\nabla v)$ for every section $v$: the connection is complex-linear. Together with $\nabla g=0$ (the defining metric property of the Levi-Civita connection) this gives, for the Hermitian metric $h(v,w)=g(v,w)+i\,g(v,Iw)$,
> $$\nabla h=\nabla g+i\,\nabla\big(g(\cdot,I\cdot)\big)=0,$$
> because $\nabla g=0$ and $\nabla I=0$ make $g(\cdot,I\cdot)$ parallel as well. A connection that is complex-linear and preserves the Hermitian metric is by definition a **unitary connection** on the Hermitian line bundle. Hence the hypotheses of clause (a) of the [[Thm - First Chern Class of a Line Bundle from Curvature|first-Chern-class theorem]] are met.

**Step 3: Identify the curvature as an imaginary-scalar 2-form.**

The curvature endomorphism is $R(e_1,e_2)=-K\,I$, so the $i\mathbb R$-valued curvature of the line bundle is $F=-iK\,dA$.

> [!note]- Derivation
> The curvature of $\nabla$ as a connection on $TS^2$ is the Riemann endomorphism $F_\nabla(X,Y)=R(X,Y)$. Evaluate on the oriented orthonormal frame $(e_1,e_2)$. From [[Ex - The Levi-Civita Connection of the Round Sphere as a Connection Matrix|the round-sphere computation]], $R(e_1,e_2)e_2=Ke_1$ with $K=1$. Using metric skew-symmetry of the curvature, $g(R(X,Y)u,v)=-g(R(X,Y)v,u)$ (a consequence of $\nabla g=0$), we determine the action on $e_1$:
> $$g\big(R(e_1,e_2)e_1,e_2\big)=-g\big(R(e_1,e_2)e_2,e_1\big)=-g(Ke_1,e_1)=-K,\qquad g\big(R(e_1,e_2)e_1,e_1\big)=0,$$
> so $R(e_1,e_2)e_1=-Ke_2$. The endomorphism $R(e_1,e_2)$ therefore acts by
> $$e_1\mapsto -Ke_2,\qquad e_2\mapsto Ke_1,$$
> which, compared with $I:e_1\mapsto e_2,\ e_2\mapsto -e_1$, is exactly $-K$ times $I$:
> $$R(e_1,e_2)=-K\,I.$$
> As a $2$-form on the surface, $F_\nabla=R(e_1,e_2)\,(e^1\wedge e^2)=R(e_1,e_2)\,dA$, where $dA=e^1\wedge e^2$ is the Riemannian area form (with $dA(e_1,e_2)=1$). Hence
> $$F_\nabla=-K\,dA\;I\quad\in\;\Omega^2\big(S^2;\operatorname{End}TS^2\big).$$
> Now pass to the complex description. On the line bundle, the skew-Hermitian endomorphisms are exactly the real multiples of $I$, and the identification "multiplication by $i$ is $I$" sends $I\mapsto i$. Therefore the endomorphism-valued curvature $-K\,dA\,I$ becomes the $i\mathbb R$-valued $2$-form
> $$F=-iK\,dA\quad\in\;\Omega^2(S^2;i\mathbb R),$$
> which is the curvature $F_A$ appearing in clause (a).

> [!warning] Convention: where the sign of $F$ comes from
> The overall sign of the imaginary curvature is fixed by two conventions and nothing else. First, the direction of the complex structure: we rotate *towards* the orientation, $Ie_1=e_2$, so that $I\leftrightarrow +i$; the opposite convention $Ie_1=-e_2$ would replace $I$ by $-I$ (the conjugate complex line bundle $\overline{TS^2}$) and flip the sign of $F$ and of $c_1$. Second, the Riemann-tensor sign, here $R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z$, which makes $K=+1$ for the round sphere. With the series conventions of conventions.md — $I$ compatible with the orientation, and this Riemann sign — the computation gives $F=-iK\,dA$ and $c_1(TS^2)[S^2]=+2$, matching $e(TS^2)[S^2]=\chi(S^2)=2$. The manifest's shorthand "$F=iK\,dA$" records the same $2$-form up to this identification of $I$ with $\pm i$; the invariant statement, and all that the exercise needs, is $|c_1(TS^2)[S^2]|=2\neq0$.

**Step 4: Compute the first Chern number.**

Integrating $\tfrac{i}{2\pi}F$ over $S^2$ gives $c_1(TS^2)[S^2]=2$.

> [!note]- Derivation
> By clause (a) of the [[Thm - First Chern Class of a Line Bundle from Curvature|first-Chern-class theorem]], the first Chern class of the Hermitian line bundle $(TS^2,I,h)$ with the unitary Levi-Civita connection is $c_1(TS^2)=\big[\tfrac{i}{2\pi}F\big]$. Substituting $F=-iK\,dA$ from Step 3,
> $$\tfrac{i}{2\pi}F=\tfrac{i}{2\pi}(-iK\,dA)=\tfrac{-i^2}{2\pi}K\,dA=\tfrac{1}{2\pi}K\,dA\qquad(\text{since }-i^2=1),$$
> a *real* closed $2$-form, as it must be for a first Chern class. The first Chern number is its integral over the fundamental class $[S^2]$:
> $$c_1(TS^2)[S^2]=\int_{S^2}\tfrac{i}{2\pi}F=\frac1{2\pi}\int_{S^2}K\,dA.$$
> On the unit round sphere $K\equiv1$, so $\int_{S^2}K\,dA=\int_{S^2}dA=\operatorname{area}(S^2)=4\pi$ (the area of the unit sphere; computed from the volume form in [[Ex - Volume of the n-Sphere via the Volume Form]]). Therefore
> $$c_1(TS^2)[S^2]=\frac1{2\pi}\cdot 4\pi=2.$$

**Step 5: Conclude non-triviality.**

Since $c_1(TS^2)[S^2]=2\neq0$, the class $c_1(TS^2)$ is nonzero, so $(TS^2,I)$ is a non-trivial complex line bundle; and a real trivialisation would give a complex trivialisation, so $TS^2$ is non-trivial.

> [!note]- Derivation
> The number $\int_{S^2}\tfrac{i}{2\pi}F=2$ is nonzero, so the cohomology class $c_1(TS^2)=[\tfrac{i}{2\pi}F]\in H^2_{\mathrm{dR}}(S^2)$ is nonzero (a class integrating to a nonzero number over $S^2$ cannot be the zero class). By clause (c) of the [[Thm - First Chern Class of a Line Bundle from Curvature|first-Chern-class theorem]] — if $\int_\Sigma F_A\neq0$ over a closed oriented surface then the line bundle is non-trivial — the complex line bundle $(TS^2,I)$ is **not trivial**.
>
> It remains to pass from the complex line bundle to the real bundle $TS^2$. Suppose, for contradiction, that $TS^2$ were trivial as a real vector bundle. A real trivialisation provides a nowhere-vanishing global section $s\in\Gamma(TS^2)$ (for instance the image of a constant nonzero vector). But a nowhere-vanishing section of $TS^2$ is, tautologically, a nowhere-vanishing section of the complex line bundle $(TS^2,I)$ (the underlying sets and fibres are the same), and a complex line bundle with a nowhere-vanishing section is trivial: $z\mapsto z\cdot s$ gives a bundle isomorphism $\underline{\mathbb C}\to(TS^2,I)$. This contradicts the non-triviality of $(TS^2,I)$ just established. Hence $TS^2$ is non-trivial as a real vector bundle. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** $TS^2$ is not a trivial vector bundle.
>
> Give $TS^2$ the complex structure $I$ (rotation by $+90^\circ$ towards the orientation), so $(TS^2,I)$ is a complex line bundle, with Hermitian metric $h(v,w)=g(v,w)+i\,g(v,Iw)$; here $g$ is the round metric.
>
> The Levi-Civita connection $\nabla$ is unitary for $(I,h)$: in an oriented orthonormal frame its connection matrix $A$ is $\mathfrak{so}(2)$-valued and $I$ is the constant generator $\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$, so $\nabla I=dI+[A,I]=0$ (as $dI=0$ and $\mathfrak{so}(2)$ is abelian); with $\nabla g=0$ this gives $\nabla h=0$.
>
> Its curvature endomorphism is $R(e_1,e_2)=-KI$: from $R(e_1,e_2)e_2=Ke_1$ (round-sphere computation, $K=1$) and metric skew-symmetry, $R(e_1,e_2)e_1=-Ke_2$, which is $-KI$. As a $2$-form, $F_\nabla=-K\,dA\,I$; under $I\leftrightarrow i$ this is the $i\mathbb R$-valued curvature $F=-iK\,dA$.
>
> By the first-Chern-class-from-curvature theorem (clause (a)), $c_1(TS^2)=[\tfrac{i}{2\pi}F]=[\tfrac1{2\pi}K\,dA]$, and
> $$c_1(TS^2)[S^2]=\frac1{2\pi}\int_{S^2}K\,dA=\frac1{2\pi}\int_{S^2}dA=\frac{4\pi}{2\pi}=2\neq0.$$
> Hence $c_1(TS^2)\neq0$, so by clause (c) the line bundle $(TS^2,I)$ is non-trivial. If $TS^2$ were trivial as a real bundle it would admit a nowhere-vanishing section, which is a nowhere-vanishing section of $(TS^2,I)$ and hence would trivialise the line bundle — a contradiction. Therefore $TS^2$ is non-trivial. $\blacksquare$

> [!warning] Illegal but tempting: quoting Gauss–Bonnet or $\chi(S^2)=2$ as the input
> A tempting shortcut is to write "$\int_{S^2}K\,dA=2\pi\chi(S^2)=4\pi$ by Gauss–Bonnet, done." That reverses the logic of this chapter. The series does **not** prove the general Gauss–Bonnet theorem $\int_\Sigma K\,dA=2\pi\chi(\Sigma)$ here; it proves $\int_{S^2}K\,dA=4\pi$ directly from $K\equiv1$ and the area of the sphere. Using $\chi(S^2)=2$ as a hypothesis would also be circular in spirit, since the non-triviality of $TS^2$ (equivalently $\chi(S^2)\neq0$, the hairy-ball phenomenon) is exactly what we are proving. The honest computation uses only the explicit round-sphere curvature and area; the connection to $\chi$ is a *consequence*, recorded in the Bridges below, not an input.

> [!note]- Independent sanity check via the Euler class
> The same number arises from the Euler class. For an oriented rank-$2$ real bundle, $e(E)=[\operatorname{Pf}(\tfrac F{2\pi})]$, and for the round sphere the endomorphism-valued curvature computed in Step 3 is $F_\nabla=-K\,dA\,I$; writing it as a matrix in the *positively oriented* orthonormal frame $(e_1,e_2)$, in which $I=\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$, gives the $\mathfrak{so}(2)$-valued curvature matrix $F=-K\,dA\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)=K\,dA\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$, whose Pfaffian is $\operatorname{Pf}(F)=K\,dA$ under the series normalisation $\operatorname{Pf}\left(\begin{smallmatrix}0&a\\-a&0\end{smallmatrix}\right)=a$ (see [[Def - Pfaffian]]); thus $e(TS^2)[S^2]=\tfrac1{2\pi}\int K\,dA=2$. Had we used the negatively oriented ordering, the matrix would read $K\,dA\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$ and the Pfaffian $-K\,dA$, returning $-2$; the positively oriented frame is what fixes the sign at $+2$. The identification $e(TS^2)=c_1(TS^2)$ for an oriented rank-$2$ bundle regarded as a Hermitian line bundle (see [[Def - Euler Class of an Oriented Vector Bundle]]) makes the two computations one and the same, and both give $2$, consistent with $\chi(S^2)=2$.

---

# Key Takeaways

**To prove a bundle is non-trivial, produce one nonzero characteristic number; to have a characteristic number at all, first install the right extra structure.** A trivial bundle has vanishing characteristic classes, so a single nonzero characteristic number is a complete obstruction to triviality. The catch is that the invariant must be one the bundle *carries*: the real rank-$2$ bundle $TS^2$ has no first Chern class until it is made complex. The reusable principle is therefore two-step — *enrich, then obstruct*: manufacture the structure (here a complex structure from metric plus orientation) that supplies a characteristic class, then compute that class and show it is nonzero. The trigger is any "prove $E$ is non-trivial" over a manifold carrying enough geometry to compute curvature; the reaction is to look for a canonical reduction of the structure group (complex, spin, symplectic) that unlocks a class to integrate. The same enrich-then-obstruct pattern is what powers Chern–Weil obstruction arguments throughout the chapter, for instance detecting the Hopf bundle by $\int_{\mathbb{CP}^1}c_1(\mathcal O(-1))=-1$.

**On an oriented Riemannian surface the tangent bundle is secretly a Hermitian line bundle, and its Levi-Civita connection is secretly a unitary connection whose curvature is $-iK\,dA$.** This is the transferable structural fact: real dimension two collapses the distinction between "oriented Riemannian rank-$2$ bundle with metric connection" and "Hermitian line bundle with unitary connection", because $SO(2)=U(1)$ and the rotation $I$ is parallel. Once this dictionary is in hand, every surface curvature computation is simultaneously a first-Chern-class computation: the Gauss curvature *is* (up to $-i$ and the area form) the curvature of a $U(1)$-connection, and the total curvature $\int K\,dA$ *is* $2\pi$ times a first Chern number. The diagnostic to carry away: whenever a real rank-$2$ oriented bundle appears with a metric connection, rewrite its curvature as $-iK\,dA$ and its Euler number as a first Chern number; the abelian structure group is what guarantees the connection is unitary, via $\nabla I=0$.

**The Euler number of a surface, the total Gauss curvature, and the first Chern number of the tangent bundle are three faces of one integer, and it is nonzero for $S^2$.** This exercise computes that integer for the sphere the hard, honest way — from $K\equiv1$ and area $4\pi$ — and finds $2$. The deeper content is that non-vanishing of this integer is exactly the obstruction to a nowhere-vanishing vector field (the hairy-ball theorem) and to triviality of $TS^2$: a nowhere-vanishing section would trivialise the line bundle and force $c_1=0$. That is why $c_1(TS^2)[S^2]=2\neq0$ settles the exercise. The general identity $\int_\Sigma K\,dA=2\pi\chi(\Sigma)$ (Gauss–Bonnet) and $e(T\Sigma)[\Sigma]=\chi(\Sigma)$ package this for all surfaces, but the sphere already exhibits the mechanism in full, and the reconstruction of the proof after months hinges on remembering the one dictionary entry "$F=-iK\,dA$".

---

# Bridges

1. **Gauss–Bonnet as the surface-wide statement of this computation.** What we proved for $S^2$ — that $\tfrac1{2\pi}\int_{S^2}K\,dA$ is an integer equal to a topological invariant — is the special case $\Sigma=S^2$ of the Gauss–Bonnet theorem $\int_\Sigma K\,dA=2\pi\chi(\Sigma)$, proved in Riemannian geometry as [[Thm - Gauss-Bonnet Theorem for Surfaces]]. The construction underlying the bridge is the identification of the Gaussian curvature $2$-form $K\,dA$ with the Chern–Weil representative $\tfrac{2\pi}{i}\cdot\tfrac{i}{2\pi}F$ of $2\pi\,c_1(T\Sigma)$: the left side is metric geometry, the right side is the characteristic class, and Chern–Weil theory is precisely the statement that they agree in cohomology. This chapter proves the sphere case from first principles and treats the general theorem as an external input.

2. **The Euler class and the top Chern class coincide for the tangent bundle of a surface.** For an oriented rank-$2$ real bundle made complex, $e(E)=c_1(E)$; the construction realising the bridge is the algebra isomorphism $\mathfrak{so}(2)\cong\mathfrak u(1)$ sending the skew generator $\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$ to $i$, under which the Pfaffian $\operatorname{Pf}(\tfrac F{2\pi})$ and the first Chern form $\tfrac{i}{2\pi}\operatorname{tr}F$ become the same real $2$-form. This is developed on [[Def - Euler Class of an Oriented Vector Bundle]], where $e(TS^2)[S^2]=2$ is verified from the same round-sphere curvature used here; the present exercise is the complex-line-bundle side of that identity.

3. **The hairy-ball theorem as the geometric reading.** The non-triviality obtained here is equivalent to the statement that $S^2$ admits no nowhere-vanishing vector field: the final step of the solution is exactly the observation that such a field would trivialise $(TS^2,I)$ and force $c_1=0$. The construction connecting the two is the correspondence "nowhere-vanishing section of a line bundle $\Leftrightarrow$ bundle isomorphism with the trivial bundle"; the nonzero Chern number obstructs the existence of the section. The Poincaré–Hopf and hairy-ball statements are treated in Riemannian geometry (see the bridge on [[Def - The Levi-Civita Connection Viewed as a Connection on TM]] to $TM$-topology); here they appear as a corollary of a curvature integral.
