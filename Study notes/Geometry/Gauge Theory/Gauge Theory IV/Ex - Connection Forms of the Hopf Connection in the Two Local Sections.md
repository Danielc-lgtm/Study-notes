---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - The Standard Connection on the Hopf Bundle"
  - "Thm - Transformation of Local Connection and Curvature Forms"
  - "Def - Local Connection Form and Gauge Potential"
  - "Def - The Maurer-Cartan Form"
  - "Def - The Hopf Bundle"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Consider the **Hopf bundle** $S^3\to S^2$, the principal $U(1)$-bundle with total space the unit sphere
$$S^3=\{\,p=(w_1,w_2)\in\mathbb{C}^2:|w_1|^2+|w_2|^2=1\,\},$$
structure group $G=U(1)=\{z\in\mathbb{C}:|z|=1\}$ acting on the right by scalar multiplication $p\cdot z=(w_1z,w_2z)$, Lie algebra $\mathfrak{g}=\mathfrak{u}(1)=i\mathbb{R}$, and projection the Hopf map
$$h\colon S^3\to S^2\subset\mathbb{C}\times\mathbb{R},\qquad h(w_1,w_2)=\bigl(2w_1\overline{w_2},\ |w_1|^2-|w_2|^2\bigr).$$
A point of the base $S^2$ is written $(z,t)$ with $z\in\mathbb{C}$, $t\in[-1,1]$, and $|z|^2+t^2=1$, so that $|z|^2=1-t^2=(1-t)(1+t)$. Equip $S^3$ with the **standard Hopf connection**, the $\mathfrak{u}(1)$-valued $1$-form
$$a_p(Y):=i\,\langle Y,\ i p\rangle,\qquad Y\in T_pS^3\subset\mathbb{R}^4,$$
where $\langle\cdot,\cdot\rangle$ is the real inner product on $\mathbb{C}^2\cong\mathbb{R}^4$ and $ip=(iw_1,iw_2)$ is the fundamental vector generating the $U(1)$-action.

Take the two hemisphere sections
$$
s_1\colon U_1\to S^3,\quad s_1(z,t)=\Bigl(\sqrt{\tfrac{1+t}{2}}\,,\ \sqrt{\tfrac{1-t}{2}}\,\tfrac{\overline z}{|z|}\Bigr),\qquad U_1:=S^2\setminus\{(0,-1)\},
$$
$$
s_2\colon U_2\to S^3,\quad s_2(z,t)=\Bigl(\sqrt{\tfrac{1+t}{2}}\,\tfrac{z}{|z|}\,,\ \sqrt{\tfrac{1-t}{2}}\Bigr),\qquad U_2:=S^2\setminus\{(0,1)\}.
$$

Prove all of the following.

1. **They are sections.** Each $s_j$ lands in $S^3$ and satisfies $h\circ s_j=\operatorname{id}$ on its domain; $s_1$ is smooth away from the south pole $(0,-1)$ and $s_2$ away from the north pole $(0,1)$.

2. **The transition function is $g_{12}=z/|z|$.** On the overlap $U_{12}:=U_1\cap U_2=S^2\setminus\{(0,\pm1)\}$ one has $s_2=s_1\cdot g_{12}$ with
$$g_{12}\colon U_{12}\to U(1),\qquad g_{12}(z,t)=\frac{z}{|z|}.$$

3. **The two gauge potentials.** With $\varphi:=\arg z$ (so that $d\varphi=d\arg z$ is a well-defined closed $1$-form on $U_{12}$),
$$A_1:=s_1^{*}a=-\,i\,\frac{1-t}{2}\,d\arg z,\qquad A_2:=s_2^{*}a=+\,i\,\frac{1+t}{2}\,d\arg z.$$

4. **The transformation law holds.** On $U_{12}$,
$$A_2=A_1+g_{12}^{*}\theta=A_1+g_{12}^{-1}\,dg_{12}=A_1+i\,d\arg z,$$
where $\theta=z^{-1}dz$ is the Maurer–Cartan form of $U(1)$.

**Recall:**

The objects in play are the Hopf bundle and its $U(1)$-action, the standard Hopf connection form, the gauge potential (local connection form) of a connection in a section, the transition function relating two sections, the Maurer–Cartan form of $U(1)$, and the transformation law for gauge potentials.

![[Thm - The Standard Connection on the Hopf Bundle#Statement]]

The **[[Thm - The Standard Connection on the Hopf Bundle|standard Hopf connection]]** is $a_p(Y)=i\langle Y,ip\rangle$, $Y\in T_pS^3$; it is a connection $1$-form with horizontal subspace $H_p=\ker a_p=(ip)^{\perp}$. Because $U(1)$ is abelian its adjoint action is trivial, so the equivariance condition reads $R_z^{\,*}a=a$; and since $a(ip)=i\langle ip,ip\rangle=i|p|^2=i$ on $S^3$ (where $|p|=1$), the form $a$ reproduces the generator $i\in\mathfrak{u}(1)$ on the fundamental field.

![[Def - Local Connection Form and Gauge Potential#The Definition]]

The **[[Def - Local Connection Form and Gauge Potential|gauge potential]]** of a connection $a$ in a local section $s$ is $A_s:=s^{*}a\in\Omega^1(U;\mathfrak{g})$, $A_s(v)=a(ds(v))$.

![[Thm - Transformation of Local Connection and Curvature Forms#Statement]]

The **[[Thm - Transformation of Local Connection and Curvature Forms|transformation law]]** states: if $s_\beta=s_\alpha\cdot g_{\alpha\beta}$ are two local sections with transition function $g_{\alpha\beta}$, then their gauge potentials satisfy
$$A_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha+g_{\alpha\beta}^{*}\theta,$$
and for an abelian group (where $\operatorname{Ad}$ is trivial) this reduces to $A_\beta=A_\alpha+g_{\alpha\beta}^{*}\theta=A_\alpha+g_{\alpha\beta}^{-1}\,dg_{\alpha\beta}$.

![[Def - The Maurer-Cartan Form#The Definition]]

The **[[Def - The Maurer-Cartan Form|Maurer–Cartan form]]** of $U(1)$ is $\theta=z^{-1}dz$; writing $z=e^{i\varphi}$ on $U(1)$ gives $\theta=e^{-i\varphi}\,d(e^{i\varphi})=i\,d\varphi$. For a map $g\colon U\to U(1)$, the pullback is $g^{*}\theta=g^{-1}\,dg$.

> [!warning] Convention: source normalisation and conjugation typos
> Bär (*Gauge Theory*, Ex. 2.2.17 and 2.3.5–2.3.6) uses a rescaled Hopf map $\operatorname{Hopf}(w_1,w_2)=(4w_1\overline{w_2},\,4|w_2|^2-|w_1|^2)/(4|w_2|^2+|w_1|^2)$ and correspondingly rescaled section formulas. That rescaling changes the intermediate radial coefficients (Bär's $s_1$ carries the normalising factor $(4|z|^2/(1+t)^2+1)^{-1/2}$) but leaves the base $S^2$, the connection on $S^3$, the transition function $g_{12}=z/|z|$, and the final identity $A_2=A_1+i\,d\arg z$ unchanged, because $\arg z$ — the argument of the first Hopf coordinate — is the same under both normalisations. We use the round Hopf map $h(w)=(2w_1\overline{w_2},|w_1|^2-|w_2|^2)$, for which the sections and potentials take the clean form above. Bär's printed section formulas additionally contain conjugation slips (his transition-function computation prints both "$z/|z|$" and "$|z|/z$", noted in the source's own errata; the two are complex conjugates on $U(1)$), so we work from the corrected, internally consistent sections and confirm the boxed result $g_{12}=z/|z|$, $A_2=A_1+i\,d\arg z$.

---

# Convergent Strategy

**Problem class.** This is a *coordinate-computation* exercise on the archetypal non-trivial bundle: pull the intrinsic connection form back through two explicit charts and watch the transformation law reproduce a pure-gauge difference. It is the concrete counterpoint to the trivial-bundle drill [[Ex - The Product Connection on a Trivial Bundle and Pure Gauge Potentials]]: there the two potentials of a *flat* connection differed by $g^{*}\theta$ with one of them zero; here neither potential is zero, the bundle is non-trivial, yet the difference is still exactly the pure-gauge term $g_{12}^{-1}dg_{12}$.

**Assumption pattern.** The computation would be forbidding if attacked head-on (differentiating the messy $\sqrt{(1\pm t)/2}$ normalisations and the phase factors along curves in $S^2$). The enabling observation is a single algebraic identity: for *any* section $s=(s^1,s^2)\colon U\to S^3$ into the unit sphere, the pulled-back Hopf connection collapses to
$$s^{*}a=\sum_{k}\overline{s^k}\,ds^k,$$
a purely imaginary $1$-form, because $|s|^2\equiv1$ forces $\sum_k \overline{s^k}\,ds^k$ to be imaginary and the connection form $a_p(Y)=i\langle Y,ip\rangle$ is precisely the imaginary-part functional. This master formula turns each pullback into a two-term algebraic computation with no curves.

**Theorem routing.** The route is: (i) establish the master formula $s^{*}a=\sum_k\overline{s^k}\,ds^k$ from the definition of [[Thm - The Standard Connection on the Hopf Bundle|the Hopf connection]]; (ii) apply it to $s_1$ and $s_2$, isolating the phase factor $\overline z/|z|$ or $z/|z|$, whose logarithmic derivative produces $\pm i\,d\arg z$ with the radial coefficient $(1\mp t)/2$; (iii) compute $g_{12}=z/|z|$ from $s_2=s_1\cdot g_{12}$; (iv) confirm $A_2-A_1=i\,d\arg z=g_{12}^{-1}dg_{12}$ against [[Thm - Transformation of Local Connection and Curvature Forms|the transformation law]]. Step (iv) is guaranteed by the theorem, so it doubles as an independent check on steps (ii)–(iii).

**Key decision point.** The one move that makes the exercise tractable is deriving and trusting the master formula $s^{*}a=\sum_k\overline{s^k}\,ds^k$ before touching the explicit sections. Its two ingredients — that $\langle V,iW\rangle=\operatorname{Im}\sum_k V_k\overline{W_k}$ and that $|s|^2=1$ makes $\sum_k\overline{s^k}\,ds^k$ imaginary — are exactly what remove all the analysis from the problem. The secondary decision is bookkeeping: which section is regular at which pole, so that the phase $\overline z/|z|$ (singular at $z=0$) is multiplied by a coefficient that vanishes there, keeping the section smooth on its stated domain.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory IV — Connections and Curvature on Principal Bundles#Legal Operations|the topic page's Legal Operations]]; where the topic page is not yet assembled, each is named descriptively.

1. **Reduce a connection pullback to an algebraic master formula using the unit-sphere constraint.** From $|s|^2\equiv1$ and the form $a_p(Y)=i\langle Y,ip\rangle$, derive $s^{*}a=\sum_k\overline{s^k}\,ds^k$, eliminating curve computations.

2. **Extract a logarithmic derivative from a pure phase.** For a unit-modulus factor $u=e^{i\varphi}$, use $\overline u\,du=i\,d\varphi$ to turn the phase part of a section into the $d\arg z$ contribution.

3. **Separate radial and angular parts and discard exact real pieces.** Split each pulled-back form into a real part $\tfrac12 d(\text{modulus}^2)=0$ and an imaginary angular part, using $f\,df+\rho\,d\rho=\tfrac12 d(f^2+\rho^2)$ with $f^2+\rho^2=1$.

4. **Compute a transition function componentwise as a ratio of sections.** From $s_2=s_1\cdot g_{12}$ read $g_{12}$ off either component and check the other agrees.

5. **Verify a computed difference against the transformation law.** Confirm $A_2-A_1=g_{12}^{-1}dg_{12}$ using [[Thm - Transformation of Local Connection and Curvature Forms|the abelian transformation law]], turning the theorem into a consistency check.

---

# Hints

> [!note]- Hint 1
> Do not differentiate the sections along curves. First prove a master formula: for any smooth $s=(s^1,s^2)\colon U\to S^3\subset\mathbb{C}^2$, show $s^{*}a=\sum_k\overline{s^k}\,ds^k$. Two facts do it — write $\langle V,iW\rangle$ for the real inner product in terms of $\operatorname{Im}\sum_k V_k\overline{W_k}$, and differentiate the constraint $\sum_k|s^k|^2=1$.

> [!note]- Hint 2
> For the real inner product on $\mathbb{C}^2$, $\langle V,iW\rangle=\operatorname{Re}\sum_k V_k\overline{iW_k}=\operatorname{Re}\sum_k V_k(-i)\overline{W_k}=\operatorname{Im}\sum_k V_k\overline{W_k}$. So $a_s(ds\,v)=i\operatorname{Im}\sum_k ds^k(v)\,\overline{s^k}$. Now $0=d(\sum_k|s^k|^2)=2\operatorname{Re}\sum_k ds^k\,\overline{s^k}$, so $\sum_k ds^k\overline{s^k}$ is purely imaginary and equals $i$ times its imaginary part.

> [!note]- Hint 3
> Apply the master formula to $s_1=(f,\,\rho\,\overline z/|z|)$ with $f=\sqrt{(1+t)/2}$, $\rho=\sqrt{(1-t)/2}$ (both real; $\rho$ is used for the radial coefficient because $h$ already denotes the Hopf map). The first term $\overline{s_1^1}\,ds_1^1=f\,df$ is real; the second is $\overline{\rho u}\,d(\rho u)$ with $u=\overline z/|z|=e^{-i\arg z}$. Expand it and use $\overline u\,du=-\,i\,d\arg z$. The real parts $f\,df+\rho\,d\rho$ combine to $\tfrac12 d(f^2+\rho^2)=\tfrac12 d(1)=0$.

> [!note]- Hint 4
> For $g_{12}$: you need $s_2=s_1\cdot g_{12}$, i.e. $s_2^k=g_{12}\,s_1^k$ for both $k$. Take the ratio in the first component: $s_2^1/s_1^1=(f\,z/|z|)/f=z/|z|$. Then check the second component gives the same, using $|z|/\overline z=z/|z|$.

> [!note]- Hint 5
> Finally, the abelian transformation law says $A_2=A_1+g_{12}^{-1}dg_{12}$. Compute $g_{12}^{-1}dg_{12}$ for $g_{12}=z/|z|=e^{i\arg z}$: it is $e^{-i\arg z}d(e^{i\arg z})=i\,d\arg z$. Compare with your $A_2-A_1=i\tfrac{1+t}{2}d\arg z+i\tfrac{1-t}{2}d\arg z$.

---

# Solution

The whole computation rests on one algebraic reduction: because the Hopf connection is $a_p(Y)=i\langle Y,ip\rangle$ and every section lands in the unit sphere, the pullback $s^{*}a$ is nothing but $\sum_k\overline{s^k}\,ds^k$. Once that is in hand, each gauge potential is a two-line expansion in which the radial factors contribute an exact real form (which vanishes, since the radii square to $1$) and the pure phase contributes $\pm i\,d\arg z$. The transition function is a ratio of the two sections, and the transformation law then reads off as an internal consistency check.

**Step 0: The master formula $s^{*}a=\sum_k\overline{s^k}\,ds^k$.**

For every smooth $s=(s^1,s^2)\colon U\to S^3\subset\mathbb{C}^2$, the pullback of the Hopf connection is the purely imaginary $1$-form $s^{*}a=\overline{s^1}\,ds^1+\overline{s^2}\,ds^2$.

> [!note]- Derivation
> Fix $x\in U$ and $v\in T_xU$. By the definition of the gauge potential and of [[Thm - The Standard Connection on the Hopf Bundle|the Hopf connection form]],
> $$(s^{*}a)_x(v)=a_{s(x)}\bigl(ds_x(v)\bigr)=i\,\bigl\langle ds_x(v),\ i\,s(x)\bigr\rangle\qquad\text{(definition of }a_p(Y)=i\langle Y,ip\rangle\text{).}$$
> Write $V=ds_x(v)\in\mathbb{C}^2$ and $W=s(x)\in\mathbb{C}^2$. For the real inner product $\langle A,B\rangle=\operatorname{Re}\sum_k A_k\overline{B_k}$ on $\mathbb{C}^2\cong\mathbb{R}^4$,
> $$\langle V,iW\rangle=\operatorname{Re}\sum_k V_k\,\overline{iW_k}=\operatorname{Re}\sum_k V_k(-i)\overline{W_k}=\operatorname{Re}\Bigl(-i\sum_k V_k\overline{W_k}\Bigr)=\operatorname{Im}\sum_k V_k\overline{W_k}\qquad\text{(since }\operatorname{Re}(-iz)=\operatorname{Im}z\text{).}$$
> Therefore $(s^{*}a)_x(v)=i\operatorname{Im}\sum_k ds^k(v)\,\overline{s^k}$, that is
> $$s^{*}a=i\operatorname{Im}\Bigl(\sum_k \overline{s^k}\,ds^k\Bigr)\qquad(\ast)$$
> as $\mathfrak{u}(1)$-valued forms. It remains to see that $\sum_k\overline{s^k}\,ds^k$ is already purely imaginary. Differentiating the constraint $\sum_k|s^k|^2=\sum_k s^k\overline{s^k}\equiv1$,
> $$0=d\Bigl(\sum_k s^k\overline{s^k}\Bigr)=\sum_k\bigl(\overline{s^k}\,ds^k+s^k\,d\overline{s^k}\bigr)=\sum_k\overline{s^k}\,ds^k+\overline{\sum_k\overline{s^k}\,ds^k}=2\operatorname{Re}\sum_k\overline{s^k}\,ds^k,$$
> so $\operatorname{Re}\sum_k\overline{s^k}\,ds^k=0$; the form $\sum_k\overline{s^k}\,ds^k$ is purely imaginary and hence equals $i$ times its own imaginary part. Substituting into $(\ast)$,
> $$s^{*}a=i\operatorname{Im}\Bigl(\sum_k\overline{s^k}\,ds^k\Bigr)=\sum_k\overline{s^k}\,ds^k,$$
> a purely imaginary ($\mathfrak{u}(1)$-valued) $1$-form. This is the master formula.

**Step 1: The $s_j$ are sections, regular off the opposite pole.**

Each $s_j$ maps into $S^3$ and projects by $h$ to $(z,t)$; $s_1$ is smooth on $U_1=S^2\setminus\{(0,-1)\}$ and $s_2$ on $U_2=S^2\setminus\{(0,1)\}$.

> [!note]- Derivation
> Write $f=\sqrt{(1+t)/2}$ and $\rho=\sqrt{(1-t)/2}$, both real and non-negative for $t\in[-1,1]$ (we use $\rho$ for the second radial coefficient because $h$ already names the Hopf map), with $f^2+\rho^2=\tfrac{1+t}{2}+\tfrac{1-t}{2}=1$ and $2f\rho=2\sqrt{\tfrac{1+t}{2}\cdot\tfrac{1-t}{2}}=\sqrt{1-t^2}=|z|$ (using $|z|^2=1-t^2$).
>
> *Unit length.* For $s_1=(f,\ \rho\,\overline z/|z|)$: $|s_1|^2=f^2+\rho^2\,|\overline z/|z||^2=f^2+\rho^2=1$, since $|\overline z/|z||=1$. Likewise $|s_2|^2=f^2\,|z/|z||^2+\rho^2=f^2+\rho^2=1$. Both land in $S^3$.
>
> *Projection.* Applying $h(w)=(2w_1\overline{w_2},|w_1|^2-|w_2|^2)$ to $s_1$: the first coordinate is
> $$2\,f\cdot\overline{\rho\,\overline z/|z|}=2f\rho\cdot\frac{z}{|z|}=|z|\cdot\frac{z}{|z|}=z\qquad\text{(using }\overline{\overline z}=z,\ 2f\rho=|z|\text{),}$$
> and the second is $f^2-\rho^2=\tfrac{1+t}{2}-\tfrac{1-t}{2}=t$. So $h\circ s_1=(z,t)=\operatorname{id}$. The same computation for $s_2$ gives first coordinate $2\,(f\,z/|z|)\,\overline\rho=2f\rho\,z/|z|=z$ and second $f^2-\rho^2=t$. Both are sections.
>
> *Regularity.* The only non-smooth ingredient is the phase $\overline z/|z|$ (respectively $z/|z|$), undefined where $z=0$, i.e. at the two poles $(0,\pm1)$. In $s_1$ the phase multiplies $\rho=\sqrt{(1-t)/2}$, which vanishes at the north pole $t=1$; there $s_1=(1,0)$ extends smoothly, and $s_1$ is singular only at the south pole $(0,-1)$ (where $t=-1$, $\rho=1$). Hence $s_1$ is smooth on $U_1=S^2\setminus\{(0,-1)\}$. Symmetrically, in $s_2$ the phase multiplies $f=\sqrt{(1+t)/2}$, vanishing at the south pole $t=-1$; there $s_2=(0,1)$ extends smoothly, and $s_2$ is smooth on $U_2=S^2\setminus\{(0,1)\}$. This proves part 1.

**Step 2: The transition function is $g_{12}=z/|z|$.**

On $U_{12}$, $s_2=s_1\cdot g_{12}$ with $g_{12}=z/|z|$.

> [!note]- Derivation
> Two sections over the same base point differ by the (unique, since the action is free) element of $U(1)$ carrying one to the other: $s_2=s_1\cdot g_{12}$ means $s_2^k=g_{12}\,s_1^k$ for $k=1,2$. Reading the first component,
> $$g_{12}=\frac{s_2^1}{s_1^1}=\frac{f\,z/|z|}{f}=\frac{z}{|z|}\qquad(f\neq0\text{ on }U_{12}\text{, where }t>-1\text{).}$$
> The second component must give the same value, and does:
> $$\frac{s_2^2}{s_1^2}=\frac{\rho}{\rho\,\overline z/|z|}=\frac{|z|}{\overline z}=\frac{|z|\,z}{\overline z\,z}=\frac{|z|\,z}{|z|^2}=\frac{z}{|z|}\qquad(\rho\neq0\text{ on }U_{12}\text{, where }t<1\text{).}$$
> Both components agree, so $g_{12}(z,t)=z/|z|\in U(1)$, a smooth map $U_{12}\to U(1)$. This proves part 2 and confirms the source's boxed value (against its conjugation typo, which would give the reciprocal $|z|/z$).

**Step 3: The gauge potential $A_1=s_1^{*}a$.**

$A_1=-\,i\,\dfrac{1-t}{2}\,d\arg z$.

> [!note]- Derivation
> Apply the master formula of Step 0 to $s_1=(f,\ \rho\,u)$, where $u:=\overline z/|z|=e^{-i\varphi}$ and $\varphi=\arg z$ (so $u$ has unit modulus, $\overline u u=1$):
> $$A_1=\overline{s_1^1}\,ds_1^1+\overline{s_1^2}\,ds_1^2=f\,df+\overline{\rho u}\,d(\rho u)\qquad\text{(master formula; }f,\rho\text{ real).}$$
> Expand the second term with the Leibniz rule, using $\overline{\rho u}=\rho\,\overline u$ and $d(\rho u)=d\rho\,u+\rho\,du$:
> $$\overline{\rho u}\,d(\rho u)=\rho\overline u\,(d\rho\,u+\rho\,du)=\rho\,d\rho\,(\overline u u)+\rho^2\,\overline u\,du=\rho\,d\rho+\rho^2\,\overline u\,du\qquad(\overline u u=1).$$
> The logarithmic derivative of the pure phase is $\overline u\,du=e^{i\varphi}\,d(e^{-i\varphi})=e^{i\varphi}(-i\,e^{-i\varphi}\,d\varphi)=-\,i\,d\varphi$. Hence
> $$A_1=f\,df+\rho\,d\rho-\,i\,\rho^2\,d\varphi.$$
> The real part is exact and vanishes: $f\,df+\rho\,d\rho=\tfrac12\,d(f^2+\rho^2)=\tfrac12\,d(1)=0$ (by $f^2+\rho^2=1$ from Step 1). With $\rho^2=(1-t)/2$ and $\varphi=\arg z$,
> $$A_1=-\,i\,\rho^2\,d\varphi=-\,i\,\frac{1-t}{2}\,d\arg z.$$
> This is purely imaginary, as a $\mathfrak{u}(1)$-valued form must be.

**Step 4: The gauge potential $A_2=s_2^{*}a$.**

$A_2=+\,i\,\dfrac{1+t}{2}\,d\arg z$.

> [!note]- Derivation
> Now $s_2=(f\,v,\ \rho)$ with $v:=z/|z|=e^{i\varphi}$, $\varphi=\arg z$, $\overline v v=1$. By the master formula,
> $$A_2=\overline{s_2^1}\,ds_2^1+\overline{s_2^2}\,ds_2^2=\overline{f v}\,d(f v)+\rho\,d\rho\qquad\text{(master formula; }f,\rho\text{ real).}$$
> Expanding the first term with $\overline{fv}=f\overline v$ and $d(fv)=df\,v+f\,dv$:
> $$\overline{fv}\,d(fv)=f\overline v(df\,v+f\,dv)=f\,df\,(\overline v v)+f^2\,\overline v\,dv=f\,df+f^2\,\overline v\,dv.$$
> The phase derivative is $\overline v\,dv=e^{-i\varphi}\,d(e^{i\varphi})=e^{-i\varphi}(i\,e^{i\varphi}\,d\varphi)=+\,i\,d\varphi$. Hence
> $$A_2=f\,df+\rho\,d\rho+i\,f^2\,d\varphi=0+i\,\frac{1+t}{2}\,d\varphi=+\,i\,\frac{1+t}{2}\,d\arg z,$$
> again using $f\,df+\rho\,d\rho=0$ and $f^2=(1+t)/2$. This proves the two potential formulas of part 3.

**Step 5: The transformation law $A_2=A_1+g_{12}^{-1}dg_{12}=A_1+i\,d\arg z$.**

The computed difference matches the pure-gauge term of $g_{12}$.

> [!note]- Derivation
> Compute the difference from Steps 3–4:
> $$A_2-A_1=i\,\frac{1+t}{2}\,d\arg z-\Bigl(-\,i\,\frac{1-t}{2}\,d\arg z\Bigr)=i\,\frac{(1+t)+(1-t)}{2}\,d\arg z=i\,d\arg z.$$
> Independently, compute the pure-gauge term from $g_{12}=z/|z|=e^{i\varphi}$, $\varphi=\arg z$. Its Maurer–Cartan pullback is
> $$g_{12}^{*}\theta=g_{12}^{-1}\,dg_{12}=e^{-i\varphi}\,d(e^{i\varphi})=e^{-i\varphi}\,(i\,e^{i\varphi}\,d\varphi)=i\,d\varphi=i\,d\arg z\qquad\text{(definition of }\theta=z^{-1}dz\text{ for }U(1)\text{).}$$
> Since $U(1)$ is abelian, [[Thm - Transformation of Local Connection and Curvature Forms|the transformation law]] $A_2=\operatorname{Ad}_{g_{12}^{-1}}A_1+g_{12}^{*}\theta$ reduces to $A_2=A_1+g_{12}^{-1}dg_{12}$; and indeed
> $$A_1+g_{12}^{-1}dg_{12}=-\,i\,\frac{1-t}{2}\,d\arg z+i\,d\arg z=i\,\frac{-(1-t)+2}{2}\,d\arg z=i\,\frac{1+t}{2}\,d\arg z=A_2.$$
> The direct computation and the transformation law agree, proving part 4. The two potentials $A_1,A_2$ therefore differ by exactly the pure-gauge $1$-form $i\,d\arg z$, which is *not* globally exact on $U_{12}$ — this failure of $d\arg z$ to be exact around the equator is the manifestation, at the level of gauge potentials, of the non-triviality of the Hopf bundle.

> [!note]- Complete formal solution
> **Claim.** For the Hopf bundle $S^3\to S^2$ with standard connection $a_p(Y)=i\langle Y,ip\rangle$ and the sections $s_1,s_2$ above: $g_{12}=z/|z|$, $A_1=s_1^{*}a=-i\tfrac{1-t}{2}d\arg z$, $A_2=s_2^{*}a=+i\tfrac{1+t}{2}d\arg z$, and $A_2=A_1+g_{12}^{-1}dg_{12}=A_1+i\,d\arg z$.
>
> *Master formula.* For any $s=(s^1,s^2)\colon U\to S^3$, $\langle V,iW\rangle=\operatorname{Im}\sum_k V_k\overline{W_k}$ gives $s^{*}a=i\operatorname{Im}\sum_k\overline{s^k}ds^k$; and $d(\sum_k|s^k|^2)=0$ forces $\sum_k\overline{s^k}ds^k$ to be imaginary, so $s^{*}a=\sum_k\overline{s^k}ds^k$.
>
> *Sections.* With $f=\sqrt{(1+t)/2}$, $\rho=\sqrt{(1-t)/2}$ (the radial coefficient is $\rho$, since $h$ denotes the Hopf map): $f^2+\rho^2=1$, $2f\rho=|z|$. Then $|s_j|=1$ and $h\circ s_j=(z,t)$ by direct substitution into $h(w)=(2w_1\overline{w_2},|w_1|^2-|w_2|^2)$; the phase singularity of $s_1$ (resp. $s_2$) sits at the pole where its real coefficient $\rho$ (resp. $f$) vanishes, so $s_1$ is smooth on $S^2\setminus\{(0,-1)\}$ and $s_2$ on $S^2\setminus\{(0,1)\}$.
>
> *Transition.* $s_2=s_1\cdot g_{12}$ gives $g_{12}=s_2^1/s_1^1=z/|z|$, and $s_2^2/s_1^2=|z|/\overline z=z/|z|$ agrees.
>
> *Potentials.* With $u=\overline z/|z|=e^{-i\arg z}$, $\overline u du=-i\,d\arg z$, so $A_1=f\,df+\rho\,d\rho-i\,\rho^2 d\arg z=-i\tfrac{1-t}{2}d\arg z$ (the real part $f\,df+\rho\,d\rho=\tfrac12 d(f^2+\rho^2)=0$). With $v=z/|z|=e^{i\arg z}$, $\overline v dv=+i\,d\arg z$, so $A_2=f\,df+\rho\,d\rho+i\,f^2 d\arg z=+i\tfrac{1+t}{2}d\arg z$.
>
> *Transformation law.* $A_2-A_1=i\tfrac{(1+t)+(1-t)}{2}d\arg z=i\,d\arg z$, and $g_{12}^{-1}dg_{12}=e^{-i\arg z}d(e^{i\arg z})=i\,d\arg z$; since $U(1)$ is abelian, [[Thm - Transformation of Local Connection and Curvature Forms|the transformation law]] gives $A_2=A_1+g_{12}^{-1}dg_{12}$, confirmed. $\blacksquare$

> [!warning] Illegal but tempting route: differentiating along curves in the base
> One is tempted to compute $s_j^{*}a$ by picking a curve $c(\tau)$ in $S^2$, forming $s_j(c(\tau))$, and evaluating $a$ on its velocity. This is legitimate but drowns the computation in derivatives of $\sqrt{(1\pm t)/2}$ and of the phase, and it obscures why the radial parts cancel. The master formula $s^{*}a=\sum_k\overline{s^k}\,ds^k$ is what makes the cancellation structural: the radial contribution is always the exact form $\tfrac12 d|s|^2=0$, so only the phase survives. Skipping the master formula is not wrong, only needlessly hard; the extra condition that would make the curve method clean is precisely the observation, packaged in the master formula, that $\operatorname{Re}\sum_k\overline{s^k}ds^k=0$.

> [!note]- Independent sanity check: curvature descends without an inhomogeneous term
> The two potentials must have equal exterior derivatives up to the (closed) gauge term, since $F=dA_j$ for abelian $G$ and $F$ is globally defined. Indeed $dA_1=-\tfrac{i}{2}d(1-t)\wedge d\arg z=+\tfrac{i}{2}dt\wedge d\arg z$ and $dA_2=+\tfrac{i}{2}d(1+t)\wedge d\arg z=+\tfrac{i}{2}dt\wedge d\arg z$, so $dA_1=dA_2$ on $U_{12}$, consistent with $A_2-A_1=i\,d\arg z$ being closed ($d(d\arg z)=0$). The common value $F=\tfrac{i}{2}\,dt\wedge d\arg z$ is (up to the area form of $S^2$) the standard Hopf curvature $2i\,\mathrm{vol}$ computed in [[Ex - Curvature of the Standard Hopf Connection]].

---

# Key Takeaways

**On a non-trivial bundle, two local gauge potentials cannot both vanish, and their difference is forced to be a pure-gauge $1$-form that fails to be exact — that failure is the topology.** The Hopf bundle admits no global section, so no single gauge covers all of $S^2$; the equator carries two potentials $A_1,A_2$, and the transformation law pins their difference to $g_{12}^{-1}dg_{12}=i\,d\arg z$. The crucial point is that $d\arg z$ is *closed but not exact* on the punctured base $U_{12}$ (its integral around the equator is $2\pi$), so the two potentials cannot be reconciled by a globally defined gauge change. This is the local shadow of the first Chern number: integrating the common curvature $F=dA_j$ over $S^2$ (splitting into the two hemispheres and applying Stokes on each, the boundary terms contributing exactly the winding of $g_{12}$) yields a nonzero integer. The reusable principle: *when a bundle is non-trivial, the obstruction shows up as a transition-function winding that no choice of local gauges can remove*, and one detects it precisely by comparing gauge potentials across a chart overlap.

**The unit-sphere master formula $s^{*}a=\sum_k\overline{s^k}\,ds^k$ is the reusable engine behind every explicit connection computation on a sphere bundle, and it works because the connection form is the "imaginary part" functional.** The derivation used only two inputs: the algebraic identity $\langle V,iW\rangle=\operatorname{Im}\sum_k V_k\overline{W_k}$ and the constraint derivative $\operatorname{Re}\sum_k\overline{s^k}ds^k=\tfrac12 d|s|^2=0$. The same pattern recurs for the tautological line bundle $\mathcal{O}(-1)\to\mathbb{CP}^n$ (the associated bundle of this very Hopf bundle), where the induced connection is $\nabla s=\operatorname{pr}(ds)$ and its potential in a holomorphic frame is again $\overline{\sigma}\,d\sigma/|\sigma|^2$ — see [[Ex - The Induced Connection on the Tautological Bundle from the Hopf Connection]]. The transferable diagnostic: *whenever a connection is defined as "$i$ times the projection onto the fibre direction" and the sections satisfy a quadratic constraint, the pullback is the logarithmic derivative $\overline{s}\,ds$, and the modulus contributes an exact real form that drops out.* Recognising this converts a curve-chasing analysis problem into two lines of algebra.

**The transformation law is best used as a self-checking device: compute both potentials and both sides of $A_2=A_1+g_{12}^{-1}dg_{12}$ independently, and let their agreement certify the computation.** Here the difference $A_2-A_1=i\,d\arg z$ came out of two separate pullbacks (Steps 3–4), while $g_{12}^{-1}dg_{12}=i\,d\arg z$ came out of the transition function (Step 2); their coincidence is not a tautology but a consistency test that would have caught any sign error in the sections, the phase conventions, or the connection. This mirrors the trivial-bundle case [[Ex - The Product Connection on a Trivial Bundle and Pure Gauge Potentials]], where one potential was zero and the other was exactly $g^{*}\theta$: there the pure-gauge term stood alone; here it is the *difference* of two genuinely nonzero potentials on a bundle that admits none globally. The trigger to run this check is any explicit multi-chart connection computation — compute one more thing than you strictly need (the transition function, or the second potential) and use the transformation law to close the loop. Companion computation: [[Ex - Curvature of the Standard Hopf Connection]] takes $F=dA_j$ and evaluates the curvature that these potentials share.
