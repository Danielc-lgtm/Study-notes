---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Parallel Transport in a Principal Bundle"
  - "Def - Associated Bundle"
  - "Thm - Existence and Uniqueness of Horizontal Lifts"
  - "Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles"
  - "Def - Representation of a Lie Group"
  - "Def - Covariant Derivative along a Curve"
tags: [geometry, gauge-theory]
---

# Problem Statement

There are two ways to say what it means to carry a vector in a bundle "parallel to itself" along a curve, and this exercise reconciles them. Let $\pi\colon P\to M$ be a smooth principal $G$-bundle, let $\rho\colon G\to GL(V)$ be a representation of $G$ on a finite-dimensional real or complex vector space $V$, and let $E:=P\times_\rho V=(P\times V)/G$ be the **associated vector bundle**, whose points are equivalence classes $[p,v]$ under the right action $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$. Fix a connection on $P$ — a horizontal distribution $H\subset TP$ with connection form $\omega\in\Omega^1(P;\mathfrak g)$, $H=\ker\omega$ — and let $\nabla$ be the covariant derivative it induces on $E$.

Let $c\colon[t_0,t_1]\to M$ be a piecewise smooth curve. The connection on $P$ gives, for each starting point $p\in P_{c(t_0)}$, a **principal parallel transport** $\Gamma(c)\colon P_{c(t_0)}\to P_{c(t_1)}$, defined by $\Gamma(c)(p)=\tilde c(t_1)$ where $\tilde c$ is the horizontal lift of $c$ with $\tilde c(t_0)=p$. Using it, define a map on the associated bundle by transporting the frame and leaving the fibre coordinate fixed:
$$PT_c\colon E_{c(t_0)}\longrightarrow E_{c(t_1)},\qquad PT_c[p,v]:=[\Gamma(c)(p),v].$$

Prove the three facts that make this a good definition and tie it to the vector-bundle picture:

1. **Well-definedness.** $PT_c$ does not depend on the representative $(p,v)$ chosen for the class $[p,v]$: if $[p,v]=[p',v']$ then $[\Gamma(c)(p),v]=[\Gamma(c)(p'),v']$.
2. **Linearity.** $PT_c$ is a linear map between the fibres $E_{c(t_0)}$ and $E_{c(t_1)}$, and in fact a linear isomorphism.
3. **Agreement with the ODE definition.** The curve $t\mapsto[\tilde c(t),v]$ (with $v\in V$ fixed and $\tilde c$ the horizontal lift through $p$) is the section of $E$ along $c$ that is parallel for $\nabla$ with initial value $[p,v]$; equivalently, in a trivialisation of $c^*E$ furnished by the horizontal lift the parallel-transport ordinary differential equation $\dot s+B(t)\,s=0$ has vanishing coefficient matrix $B\equiv0$, so its solution through $v_0$ is the constant $v_0$. Consequently $PT_c$ coincides with the parallel transport $\mathrm{PT}_c$ defined by that ordinary differential equation.

Throughout, $\mathfrak g=T_eG$ is the Lie algebra of $G$, and $\rho_*:=d_e\rho\colon\mathfrak g\to\operatorname{End}(V)=\mathfrak{gl}(V)$ is the induced Lie-algebra representation, the differential of $\rho$ at the identity $e\in G$. A **horizontal lift** of $c$ is a curve $\tilde c$ in $P$ with $\pi\circ\tilde c=c$ and $\dot{\tilde c}(t)\in H_{\tilde c(t)}$, equivalently $\omega_{\tilde c(t)}(\dot{\tilde c}(t))=0$, for all $t$. The frame reading of a point $p\in P_m$ is the linear isomorphism $V\xrightarrow{\ \sim\ }E_m$, $v\mapsto[p,v]$; that this is a linear isomorphism, and that the resulting vector-space structure on $E_m$ does not depend on which $p\in P_m$ is used, is part of the construction of the associated bundle and is recalled below.

> [!warning] Convention: the two source notations, and Haydys's typo
> This exercise fuses Bär's principal-bundle description of parallel transport (Bär, *Gauge Theory*, Remark 2.6.3 and Definition 2.6.4, p. 67) with Haydys's vector-bundle description by an ordinary differential equation (Haydys, *Introduction to Gauge Theory*, Definition 100, p. 32). The series writes $\Gamma(c)$ for parallel transport on the total space $P$ and $PT_c$ for the induced map on the associated vector bundle $E$; Haydys writes $\mathrm{PT}_\gamma$ for the latter. Haydys trivialises $\gamma^*E$ and writes the connection as $\tfrac{d}{dt}+B(t)\,dt$ with $B\colon[0,1]\to M_k(\mathbb R)$, but then states the parallel-transport equation as $\dot s+A(t)s=0$; the matrix $A$ there is a typographical slip for the same $B$ (there is no independent $A$ in that passage). We use the corrected form $\dot s+B(t)\,s=0$ throughout.

**Recall.**

The objects in play are the associated vector bundle and its fibrewise vector-space structure, the connection form and horizontal lift, principal parallel transport, and the covariant derivative that the principal connection induces on the associated bundle.

![[Def - Associated Bundle#The Definition]]

The **[[Def - Associated Bundle|associated bundle]]** $E=P\times_\rho V$ is the quotient of $P\times V$ by the right $G$-action $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$; its point through $(p,v)$ is written $[p,v]$, and $[p,v]=[p',v']$ holds if and only if there is a group element $g\in G$ with $p'=p\cdot g$ and $v'=\rho(g^{-1})v$. The bundle projection $\pi_E\colon E\to M$ is $[p,v]\mapsto\pi(p)$. Over $m\in M$, fixing any $p\in P_m$ makes the frame reading $\iota_p\colon V\to E_m$, $\iota_p(v)=[p,v]$, a linear isomorphism, and the vector-space structure it puts on $E_m$ is the same for every choice of $p\in P_m$: replacing $p$ by $p\cdot g$ replaces $\iota_p$ by $\iota_{p\cdot g}=\iota_p\circ\rho(g)$, a linear reparametrisation, so the addition and scalar multiplication it induces are unchanged.

![[Def - Parallel Transport in a Principal Bundle#The Definition]]

For a curve $c\colon[t_0,t_1]\to M$ and $p\in P_{c(t_0)}$, the **[[Def - Parallel Transport in a Principal Bundle|principal parallel transport]]** is $\Gamma(c)(p)=\tilde c(t_1)$, where $\tilde c$ is the horizontal lift of $c$ with $\tilde c(t_0)=p$.

![[Thm - Existence and Uniqueness of Horizontal Lifts#Statement]]

The **[[Thm - Existence and Uniqueness of Horizontal Lifts|horizontal-lift theorem]]** guarantees that this $\tilde c$ exists, is unique, and is defined on the whole interval, and — the clause this exercise leans on — that horizontal lifts are equivariant: if $\tilde c$ is the horizontal lift through $p$, then $t\mapsto\tilde c(t)\cdot g=R_g(\tilde c(t))$ is the horizontal lift through $p\cdot g$. Restricting to the endpoint gives $\Gamma(c)(p\cdot g)=\tilde c(t_1)\cdot g=\Gamma(c)(p)\cdot g$, i.e. $\Gamma(c)\circ R_g=R_g\circ\Gamma(c)$.

![[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles#Statement]]

The connection on $P$ induces a covariant derivative $\nabla$ on $E=P\times_\rho V$, and the shape of that induced derivative along a curve is exactly what we need. Writing a section of $E$ along $c$ in the form $\sigma(t)=[\tilde\gamma(t),w(t)]$, where $\tilde\gamma$ is **any** smooth lift of $c$ to $P$ (not necessarily horizontal) and $w\colon[t_0,t_1]\to V$ is a smooth curve of fibre coordinates, the **[[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|induced covariant derivative]]** along $c$ is
$$\frac{\nabla\sigma}{dt}(t)=\Big[\tilde\gamma(t),\ \dot w(t)+\rho_*\big(\omega_{\tilde\gamma(t)}(\dot{\tilde\gamma}(t))\big)\,w(t)\Big].$$
This is the formula recorded in Bär's Remark 2.6.3; here $\rho_*\colon\mathfrak g\to\operatorname{End}(V)$ is the differential of $\rho$ at $e$, so $\rho_*\big(\omega(\dot{\tilde\gamma})\big)\in\operatorname{End}(V)$ acts on $w(t)\in V$. The covariant derivative along $c$ is the notion of [[Def - Covariant Derivative along a Curve|covariant derivative along a curve]]; a section $\sigma$ is **parallel along $c$** when $\tfrac{\nabla\sigma}{dt}\equiv0$.

---

# Convergent Strategy

**Problem class.** This is a *coherence* problem: two constructions of the same geometric operation — one on the principal bundle by horizontal lifting, one on the vector bundle by solving a linear ordinary differential equation — must be shown to describe a single, well-behaved linear map. Problems of this class are proved not by a computation but by *tracing definitions through a quotient*: the only real content is that the equivalence relation defining $E$ interacts correctly with the equivariance of the horizontal lift, and that the horizontal lift trivialises the induced connection so that its transport equation degenerates to $\dot v=0$.

**Assumption pattern.** Exactly two structural facts do all the work, and each is used once. The first is the *equivariance of horizontal lifts*, $\Gamma(c)\circ R_g=R_g\circ\Gamma(c)$: it is the unique property that lets the frame move $p\mapsto\Gamma(c)(p)$ commute past the group element relating two representatives of a class. The recognisable trigger for reaching for it is that we must compare the images of two representatives $(p,v)$ and $(p\cdot g,\rho(g^{-1})v)$ of the same class. The second is that *a horizontal lift kills the connection term*, $\omega_{\tilde c}(\dot{\tilde c})=0$: it is the unique property that makes the induced covariant derivative of $[\tilde c(t),v(t)]$ collapse to $[\tilde c(t),\dot v(t)]$. The trigger is that we want the transport equation's coefficient matrix to vanish.

**Theorem routing.** For well-definedness, route through the [[Thm - Existence and Uniqueness of Horizontal Lifts|horizontal-lift theorem]]'s equivariance clause: given $[p,v]=[p',v']$ with $p'=p\cdot g$, $v'=\rho(g^{-1})v$, compute $[\Gamma(c)(p'),v']=[\Gamma(c)(p)\cdot g,\rho(g^{-1})v]$ and recognise the right-hand side as the *same class* as $[\Gamma(c)(p),v]$ by the very relation defining $E$. For linearity, route through the [[Def - Associated Bundle|frame reading]] $\iota_p\colon V\to E_{c(t_0)}$: the map $PT_c$ is the composite $\iota_{\Gamma(c)(p)}\circ\iota_p^{-1}$ of two linear isomorphisms. For agreement with the ordinary differential equation, route through the [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|induced-connection formula]]: with the horizontal lift, $\tfrac{\nabla}{dt}[\tilde c(t),v]=[\tilde c(t),0]=0$, so the section is parallel; the horizontal lift then furnishes a trivialisation of $c^*E$ in which $B\equiv0$ and Haydys's equation reads $\dot v=0$.

**Key decision point.** The one move that is not purely formal is *choosing to write every section along $c$ in the moving frame supplied by the horizontal lift itself*. Nothing in Haydys's definition mentions the principal bundle, and nothing in Bär's definition mentions a trivialisation; the bridge is the observation that the horizontal lift $\tilde c$ is simultaneously (i) the object whose endpoint defines $\Gamma(c)$ and (ii) a moving frame that trivialises $c^*E$ with vanishing connection matrix. Recognising that a *single* horizontal lift plays both roles is what collapses two definitions into one line. The secondary decision — reading the identity $[\Gamma(c)(p)\cdot g,\rho(g^{-1})v]=[\Gamma(c)(p),v]$ off the defining relation rather than manipulating anything — is the habit of *checking well-definedness by exhibiting the equivalence, not by computing invariants*.

---

# Legal Operations Used

This solution deploys the following operations, each named descriptively (the topic page's numbered Legal Operations list will be reconciled to these when it is assembled):

1. **Compare two representatives of a quotient class to test well-definedness.** A map defined on classes $[p,v]$ by a formula in the representative $(p,v)$ is well defined precisely when two representatives of one class produce two representatives of one output class. Take the general relation $(p',v')=(p\cdot g,\rho(g^{-1})v)$ and push it through the formula.

2. **Move a frame past a group element using equivariance of the horizontal lift.** The clause $\Gamma(c)\circ R_g=R_g\circ\Gamma(c)$ of the [[Thm - Existence and Uniqueness of Horizontal Lifts|horizontal-lift theorem]] lets $\Gamma(c)$ commute with the right $G$-action, converting $\Gamma(c)(p\cdot g)$ into $\Gamma(c)(p)\cdot g$.

3. **Recognise the defining equivalence of the associated bundle.** The class equality $[q\cdot g,\rho(g^{-1})w]=[q,w]$ is not something to prove but the definition of $\sim$ on $P\times V$; reading it off closes the well-definedness check.

4. **Express a map between fibres as a composite of frame readings.** Fixing $p$ and $q=\Gamma(c)(p)$, the map $PT_c$ equals $\iota_q\circ\iota_p^{-1}$, where $\iota_p\colon V\to E_{c(t_0)}$ and $\iota_q\colon V\to E_{c(t_1)}$ are the linear frame readings from the associated-bundle construction; a composite of linear isomorphisms is a linear isomorphism.

5. **Trivialise a pulled-back connection by a horizontal moving frame.** The horizontal lift $\tilde c$ gives a smooth frame $t\mapsto\iota_{\tilde c(t)}$ of $c^*E$; in this frame the induced connection has connection matrix $B(t)=\rho_*(\omega_{\tilde c(t)}(\dot{\tilde c}(t)))$, which vanishes because $\tilde c$ is horizontal.

6. **Read off the solution of a degenerate linear ordinary differential equation.** With $B\equiv0$, the equation $\dot v+B(t)v=0$ becomes $\dot v=0$, whose unique solution through $v_0$ is the constant $v_0$; uniqueness for linear ordinary differential equations then identifies the ODE parallel transport with $[p,v_0]\mapsto[\Gamma(c)(p),v_0]$.

---

# Hints

> [!note]- Hint 1
> For well-definedness you must compare what the formula does to two representatives of the same class. Two representatives of $[p,v]$ differ by a group element: $(p',v')=(p\cdot g,\rho(g^{-1})v)$ for some $g\in G$. Apply the formula $PT_c[p',v']=[\Gamma(c)(p'),v']$ and ask what property of $\Gamma(c)$ would let you rewrite $\Gamma(c)(p\cdot g)$.

> [!note]- Hint 2
> The horizontal-lift theorem says the horizontal lift through $p\cdot g$ is $\tilde c\cdot g$, hence $\Gamma(c)(p\cdot g)=\Gamma(c)(p)\cdot g$. Substitute this. You are now looking at $[\Gamma(c)(p)\cdot g,\rho(g^{-1})v]$. Do not compute anything — compare this with the defining equivalence $(q\cdot g,\rho(g^{-1})w)\sim(q,w)$ of the associated bundle.

> [!note]- Hint 3
> For linearity, do not manipulate classes. Fix $p\in P_{c(t_0)}$ and set $q=\Gamma(c)(p)$. The maps $v\mapsto[p,v]$ and $v\mapsto[q,v]$ are the linear frame isomorphisms $\iota_p\colon V\to E_{c(t_0)}$ and $\iota_q\colon V\to E_{c(t_1)}$ from the associated-bundle construction. Express $PT_c$ in terms of $\iota_p$ and $\iota_q$.

> [!note]- Hint 4
> For the agreement with the ordinary differential equation, write the candidate section as $\sigma(t)=[\tilde c(t),v]$ with $\tilde c$ the horizontal lift and $v$ constant, and feed it into the induced-connection formula $\tfrac{\nabla\sigma}{dt}=[\tilde\gamma(t),\dot w+\rho_*(\omega(\dot{\tilde\gamma}))w]$ with $\tilde\gamma=\tilde c$, $w(t)=v$. Two terms appear; explain why each is zero. Then interpret $t\mapsto\iota_{\tilde c(t)}$ as a trivialisation of $c^*E$ and identify the connection matrix $B(t)$ appearing in Haydys's equation.

---

# Solution

The whole exercise is the statement that one horizontal lift does two jobs. As the *object whose endpoint is $\Gamma(c)(p)$* it drives the principal parallel transport; as a *moving frame along $c$* it trivialises the induced connection with vanishing connection matrix. Well-definedness is the equivariance of that lift read against the equivalence relation defining $E$; linearity is that the frame readings are linear isomorphisms; and agreement with Haydys's ordinary differential equation is that in the frame supplied by the lift the transport equation is literally $\dot v=0$.

**Step 1: $PT_c$ is well defined on classes.**

Two representatives of a single class $[p,v]$ differ by the $G$-action, and the equivariance of horizontal lifts makes the outputs differ by the same action, so they represent one output class.

> [!note]- Derivation
> Suppose $(p,v)$ and $(p',v')$ are two representatives of the same point of $E_{c(t_0)}$, that is $[p,v]=[p',v']$. By the defining equivalence of the [[Def - Associated Bundle|associated bundle]] $E=P\times_\rho V$ (recalled above: $[p,v]=[p',v']$ if and only if $p'=p\cdot g$ and $v'=\rho(g^{-1})v$ for some $g\in G$), there is $g\in G$ with
> $$p'=p\cdot g,\qquad v'=\rho(g^{-1})v\qquad\text{(defining equivalence of }P\times_\rho V\text{).}$$
> Note that $p'\in P_{c(t_0)}$ as well, since the right $G$-action preserves fibres, so $PT_c[p',v']$ is defined by the same rule. Apply the definition of $PT_c$ to the primed representative:
> $$PT_c[p',v']=[\Gamma(c)(p'),v']=[\Gamma(c)(p\cdot g),\rho(g^{-1})v]\qquad\text{(definition of }PT_c\text{; substituting }p'=p\cdot g,\ v'=\rho(g^{-1})v\text{).}$$
> Now invoke the equivariance clause of the [[Thm - Existence and Uniqueness of Horizontal Lifts|horizontal-lift theorem]]: the horizontal lift through $p\cdot g$ is $\tilde c\cdot g$, so $\Gamma(c)(p\cdot g)=\Gamma(c)(p)\cdot g$. Therefore
> $$PT_c[p',v']=[\Gamma(c)(p)\cdot g,\ \rho(g^{-1})v]\qquad\text{(by equivariance }\Gamma(c)(p\cdot g)=\Gamma(c)(p)\cdot g\text{).}$$
> Finally, apply the defining equivalence of $E$ once more, this time at the endpoint fibre $E_{c(t_1)}$ and to the point $q:=\Gamma(c)(p)\in P_{c(t_1)}$: for any $g\in G$ and $v\in V$, $(q\cdot g,\rho(g^{-1})v)\sim(q,v)$, that is $[q\cdot g,\rho(g^{-1})v]=[q,v]$. Hence
> $$PT_c[p',v']=[\Gamma(c)(p)\cdot g,\ \rho(g^{-1})v]=[\Gamma(c)(p),v]=PT_c[p,v]\qquad\text{(defining equivalence of }P\times_\rho V\text{ at the endpoint).}$$
> The value of $PT_c$ on the class $[p,v]$ is therefore independent of the chosen representative, so $PT_c\colon E_{c(t_0)}\to E_{c(t_1)}$ is a well-defined map.

**Step 2: $PT_c$ is a linear isomorphism.**

Fixing a single starting frame exhibits $PT_c$ as the composite of the two linear frame readings, hence linear and invertible.

> [!note]- Derivation
> Fix any $p\in P_{c(t_0)}$ and set $q:=\Gamma(c)(p)\in P_{c(t_1)}$. Recall the frame readings from the [[Def - Associated Bundle|associated-bundle construction]]:
> $$\iota_p\colon V\to E_{c(t_0)},\quad \iota_p(v)=[p,v];\qquad \iota_q\colon V\to E_{c(t_1)},\quad \iota_q(v)=[q,v],$$
> each of which is a linear isomorphism of vector spaces (this is exactly the statement that $p$, respectively $q$, is a frame; it is part of the construction recalled in the Recall section). Every element of $E_{c(t_0)}$ is $\iota_p(v)=[p,v]$ for a unique $v\in V$, namely $v=\iota_p^{-1}(\,\cdot\,)$. Apply $PT_c$, using its definition on the representative $(p,v)$:
> $$PT_c\big(\iota_p(v)\big)=PT_c[p,v]=[\Gamma(c)(p),v]=[q,v]=\iota_q(v)\qquad\text{(definition of }PT_c\text{; }q=\Gamma(c)(p)\text{; definition of }\iota_q\text{).}$$
> Since this holds for every $v\in V$, we have the identity of maps
> $$PT_c=\iota_q\circ\iota_p^{-1}\qquad\text{(the displayed equality holds for all }v=\iota_p^{-1}(x)\text{,}\ x\in E_{c(t_0)}\text{).}$$
> Both $\iota_q$ and $\iota_p^{-1}$ are linear isomorphisms (a linear isomorphism has a linear inverse), and a composite of linear isomorphisms is a linear isomorphism. Therefore $PT_c\colon E_{c(t_0)}\to E_{c(t_1)}$ is a linear isomorphism. Concretely, for scalars $\alpha,\beta$ (real or complex, matching $V$) and vectors $v,w\in V$,
> $$PT_c\big(\alpha[p,v]+\beta[p,w]\big)=PT_c[p,\alpha v+\beta w]=[q,\alpha v+\beta w]=\alpha[q,v]+\beta[q,w]=\alpha\,PT_c[p,v]+\beta\,PT_c[p,w],$$
> each equality holding because $\iota_p$ and $\iota_q$ are linear. The inverse is $PT_c^{-1}=\iota_p\circ\iota_q^{-1}\colon E_{c(t_1)}\to E_{c(t_0)}$.

**Step 3: $t\mapsto[\tilde c(t),v]$ is the parallel section, and the transport equation degenerates to $\dot v=0$.**

Feeding the horizontal lift into the induced-connection formula makes both terms vanish, so the moving frame $\iota_{\tilde c(t)}$ trivialises $c^*E$ with zero connection matrix.

> [!note]- Derivation
> Let $\tilde c$ be the horizontal lift of $c$ with $\tilde c(t_0)=p$, so that $\Gamma(c)(p)=\tilde c(t_1)$, and fix $v\in V$. Consider the section of $E$ along $c$
> $$\sigma(t):=[\tilde c(t),v],\qquad t\in[t_0,t_1],\qquad \sigma(t_0)=[p,v].$$
> This is of the form $[\tilde\gamma(t),w(t)]$ appearing in the [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|induced-connection formula]], with the lift $\tilde\gamma=\tilde c$ and the constant fibre curve $w(t)=v$. That formula gives the covariant derivative along $c$:
> $$\frac{\nabla\sigma}{dt}(t)=\Big[\tilde c(t),\ \dot w(t)+\rho_*\big(\omega_{\tilde c(t)}(\dot{\tilde c}(t))\big)\,w(t)\Big]\qquad\text{(induced-connection formula with }\tilde\gamma=\tilde c,\ w\equiv v\text{).}$$
> Examine the two terms in the fibre coordinate.
> - $\dot w(t)=0$, because $w(t)=v$ is constant in $t$ (differentiation of a constant curve).
> - $\omega_{\tilde c(t)}(\dot{\tilde c}(t))=0$, because $\tilde c$ is a **horizontal** lift: its velocity lies in $H_{\tilde c(t)}=\ker\omega_{\tilde c(t)}$ by the definition of horizontal lift, and $\omega$ annihilates $H$. Hence $\rho_*\big(\omega_{\tilde c(t)}(\dot{\tilde c}(t))\big)=\rho_*(0)=0$ (linearity of $\rho_*$), and the whole second term $\rho_*(\omega(\dot{\tilde c}))\,v$ is the zero endomorphism applied to $v$, namely $0\in V$.
>
> Substituting both,
> $$\frac{\nabla\sigma}{dt}(t)=[\tilde c(t),\,0+0]=[\tilde c(t),0]=0\in E_{c(t)}\qquad\text{(both fibre terms vanish; }[\tilde c(t),0]\text{ is the zero vector of }E_{c(t)}\text{).}$$
> Therefore $\sigma$ is **parallel along $c$** for $\nabla$: $\tfrac{\nabla\sigma}{dt}\equiv0$, with initial value $\sigma(t_0)=[p,v]$.
>
> To read this as Haydys's ordinary differential equation, use $\tilde c$ as a moving frame. The map
> $$\Phi\colon[t_0,t_1]\times V\to c^*E,\qquad \Phi(t,u)=[\tilde c(t),u]=\iota_{\tilde c(t)}(u),$$
> is smooth and, for each fixed $t$, is the linear frame isomorphism $\iota_{\tilde c(t)}\colon V\xrightarrow{\sim}E_{c(t)}$; it is therefore a trivialisation of the pulled-back bundle $c^*E$ over $[t_0,t_1]$. (Such a trivialisation exists on any bundle over an interval; here the horizontal lift produces a canonical one.) In this trivialisation a section $\sigma(t)=[\tilde c(t),v(t)]$ is represented by the plain curve $v(t)\in V$, and the computation above with $w(t)=v(t)$ gives, for a **general** fibre curve $v(t)$,
> $$\frac{\nabla\sigma}{dt}(t)=\Big[\tilde c(t),\ \dot v(t)+\rho_*\big(\omega_{\tilde c(t)}(\dot{\tilde c}(t))\big)v(t)\Big]=[\tilde c(t),\dot v(t)]\qquad\text{(the connection term vanishes as above).}$$
> Thus the covariant derivative $\tfrac{\nabla}{dt}$ becomes, in the frame $\Phi$, the operator $\tfrac{d}{dt}+B(t)$ with connection matrix
> $$B(t)=\rho_*\big(\omega_{\tilde c(t)}(\dot{\tilde c}(t))\big)=0\qquad\text{for all }t\qquad\text{(horizontality of }\tilde c\text{).}$$
> Haydys's parallel-transport equation $\dot v+B(t)\,v=0$ (Definition 100, in the corrected notation of the Convention callout) therefore reads
> $$\dot v(t)=0,$$
> whose unique solution with $v(t_0)=v_0$ is the constant $v(t)\equiv v_0$ (a curve with zero derivative on an interval is constant; uniqueness is the elementary case of the existence–uniqueness theorem for linear ordinary differential equations). This is precisely the fibre representation of $\sigma(t)=[\tilde c(t),v_0]$.

**Step 4: the two definitions of parallel transport coincide.**

The parallel section with a given initial value is unique, and it is the one produced in Step 3; evaluating it at $t_1$ identifies Haydys's $\mathrm{PT}_c$ with $PT_c$.

> [!note]- Derivation
> Haydys defines the parallel transport $\mathrm{PT}_c(x)$ of an initial vector $x\in E_{c(t_0)}$ to be $s(t_1)$, where $s$ is the section of $E$ along $c$ that is parallel for $\nabla$ with $s(t_0)=x$; existence and uniqueness of such $s$ is the existence–uniqueness statement for the linear equation $\dot v+B(t)v=0$ in any trivialisation of $c^*E$, and the resulting $\mathrm{PT}_c$ does not depend on the trivialisation because the parallel section $s$ is a trivialisation-free geometric object (it is characterised by $\tfrac{\nabla s}{dt}\equiv0$, a condition on $\nabla$ alone).
>
> Take $x=[p,v_0]\in E_{c(t_0)}$. By Step 3 the section $\sigma(t)=[\tilde c(t),v_0]$ is parallel with $\sigma(t_0)=[p,v_0]=x$. By uniqueness of the parallel section with this initial value, $s=\sigma$. Evaluating at the terminal time,
> $$\mathrm{PT}_c(x)=s(t_1)=\sigma(t_1)=[\tilde c(t_1),v_0]=[\Gamma(c)(p),v_0]\qquad\text{(}s=\sigma\text{ by uniqueness; }\Gamma(c)(p)=\tilde c(t_1)\text{).}$$
> The right-hand side is exactly $PT_c[p,v_0]$ by definition. Since every $x\in E_{c(t_0)}$ is of the form $[p,v_0]$ for the fixed $p$ (as $v_0$ ranges over $V$), we conclude
> $$\mathrm{PT}_c=PT_c\qquad\text{on }E_{c(t_0)}.$$
> The vector-bundle parallel transport defined by the ordinary differential equation and the principal-bundle parallel transport transported into $E$ are one and the same linear isomorphism.

> [!note]- Complete formal solution
> **Claim.** Let $P\to M$ be a principal $G$-bundle with a connection, $\rho\colon G\to GL(V)$ a representation, $E=P\times_\rho V$ the associated bundle with induced covariant derivative $\nabla$, and $c\colon[t_0,t_1]\to M$ a piecewise smooth curve. Then $PT_c[p,v]:=[\Gamma(c)(p),v]$ is a well-defined linear isomorphism $E_{c(t_0)}\to E_{c(t_1)}$ that equals the parallel transport $\mathrm{PT}_c$ defined by the equation $\dot v+B(t)v=0$ in a trivialisation of $c^*E$.
>
> *Well-definedness.* If $[p,v]=[p',v']$ then $p'=p\cdot g$, $v'=\rho(g^{-1})v$ for some $g\in G$. Using the definition of $PT_c$, the equivariance $\Gamma(c)(p\cdot g)=\Gamma(c)(p)\cdot g$ of horizontal lifts, and the defining equivalence of $P\times_\rho V$,
> $$PT_c[p',v']=[\Gamma(c)(p\cdot g),\rho(g^{-1})v]=[\Gamma(c)(p)\cdot g,\rho(g^{-1})v]=[\Gamma(c)(p),v]=PT_c[p,v].$$
> So $PT_c$ is well defined.
>
> *Linearity.* Fix $p\in P_{c(t_0)}$, put $q=\Gamma(c)(p)$, and let $\iota_p,\iota_q$ be the linear frame isomorphisms $u\mapsto[p,u]$, $u\mapsto[q,u]$. For every $u\in V$, $PT_c(\iota_p(u))=[q,u]=\iota_q(u)$, so $PT_c=\iota_q\circ\iota_p^{-1}$, a composite of linear isomorphisms; hence $PT_c$ is a linear isomorphism, with inverse $\iota_p\circ\iota_q^{-1}$.
>
> *Agreement with the ordinary differential equation.* Let $\tilde c$ be the horizontal lift through $p$ and fix $v_0\in V$. The section $\sigma(t)=[\tilde c(t),v_0]$ satisfies, by the induced-connection formula and horizontality $\omega_{\tilde c(t)}(\dot{\tilde c}(t))=0$,
> $$\frac{\nabla\sigma}{dt}=\big[\tilde c(t),\ \dot v_0+\rho_*(\omega_{\tilde c(t)}(\dot{\tilde c}(t)))v_0\big]=[\tilde c(t),0]=0,$$
> so $\sigma$ is parallel with $\sigma(t_0)=[p,v_0]$. The moving frame $t\mapsto\iota_{\tilde c(t)}$ trivialises $c^*E$; in it $\nabla$ becomes $\tfrac{d}{dt}+B(t)$ with $B(t)=\rho_*(\omega_{\tilde c(t)}(\dot{\tilde c}(t)))=0$, so the transport equation is $\dot v=0$ with constant solution $v\equiv v_0$. By uniqueness of the parallel section through a given initial vector, the ODE parallel transport of $[p,v_0]$ is $\sigma(t_1)=[\tilde c(t_1),v_0]=[\Gamma(c)(p),v_0]=PT_c[p,v_0]$. Hence $\mathrm{PT}_c=PT_c$. $\blacksquare$

> [!warning] Illegal but tempting route: "any lift $\tilde\gamma$ of $c$ makes $t\mapsto[\tilde\gamma(t),v]$ parallel"
> It is tempting to skip the horizontal lift and use an arbitrary smooth lift $\tilde\gamma$ of $c$, arguing that $v$ is constant so $[\tilde\gamma(t),v]$ "does not change". This is false: the induced-connection formula gives $\tfrac{\nabla}{dt}[\tilde\gamma(t),v]=[\tilde\gamma(t),\rho_*(\omega_{\tilde\gamma(t)}(\dot{\tilde\gamma}(t)))v]$, and for a non-horizontal lift $\omega_{\tilde\gamma}(\dot{\tilde\gamma})\neq0$, so this generally does **not** vanish — the section is not parallel. Concretely, for the trivial bundle $M\times G$ with a nonzero connection form and a lift that runs "up the fibre", the extra term is exactly the connection matrix that Haydys calls $B(t)$. The horizontality of $\tilde c$ is the hypothesis that makes $B\equiv0$; it is doing real work and cannot be dropped.

> [!note]- Independent sanity check: the product connection
> Take $P=M\times G$ with the product (flat) connection, whose horizontal spaces are the tangents to the $M$-slices, so that the horizontal lift of $c$ through $(c(t_0),g_0)$ is $\tilde c(t)=(c(t),g_0)$ and $\Gamma(c)(m,g_0)=(c(t_1),g_0)$. The associated bundle is the trivial bundle $E=M\times V$ via $[(m,g),v]\leftrightarrow(m,\rho(g)v)$, and $PT_c[(c(t_0),g_0),v]=[(c(t_1),g_0),v]$ corresponds to $(c(t_1),\rho(g_0)v)$ — the same fibre vector $\rho(g_0)v$ at the new base point. This is the identity map of $V$ read through the fixed frame $g_0$, matching $B\equiv0$ and $\dot v=0$: with a flat product connection nothing is transported nontrivially, exactly as the two definitions predict.

---

# Key Takeaways

**One horizontal lift plays two roles, and identifying them is the whole content of the proof.** The horizontal lift $\tilde c$ of a curve is, on one hand, the object whose terminal point *defines* principal parallel transport $\Gamma(c)(p)=\tilde c(t_1)$; on the other hand, read as a moving frame $t\mapsto\iota_{\tilde c(t)}$, it *trivialises* the pulled-back bundle $c^*E$ with a connection matrix that vanishes, because $\omega(\dot{\tilde c})=0$ is exactly the horizontality condition. Whenever two constructions of "the same" geometric operation must be reconciled — one on a total space by lifting, one on a base by an ordinary differential equation — look for the single object that simultaneously drives the lift and provides the frame in which the equation trivialises. The transferable diagnostic: if a transport equation $\dot v+B(t)v=0$ has a distinguished frame making $B\equiv0$, that frame is a horizontal (parallel) frame, and transport in it is the identity on coordinates. This is the same phenomenon as parallel transport along a geodesic being "coordinate-constant" in a parallel frame, and as the vanishing of Christoffel symbols along a curve in Fermi coordinates.

**Well-definedness on a quotient is checked by exhibiting the equivalence, never by computing an invariant.** A map defined on classes $[p,v]$ by a formula in a representative is well defined exactly when the *same group element* that relates two input representatives relates the two outputs. Here the relating element $g$ passes untouched from $(p,v)\mapsto(p\cdot g,\rho(g^{-1})v)$ through $\Gamma(c)$ — because horizontal lifts are equivariant, $\Gamma(c)(p\cdot g)=\Gamma(c)(p)\cdot g$ — and lands as the same $g$ relating $[\Gamma(c)(p)\cdot g,\rho(g^{-1})v]$ to $[\Gamma(c)(p),v]$. The trigger for this pattern is any construction on an associated bundle, quotient space, or set of equivalence classes: the equivariance of the ingredient with respect to the group defining the quotient is precisely the condition that descends the ingredient to the quotient. The same argument, verbatim, shows that a $G$-equivariant map $P\times V\to P'\times V'$ descends to a bundle map $P\times_\rho V\to P'\times_{\rho'}V'$, and that a metric or complex structure on $V$ invariant under $\rho(G)$ descends to a bundle metric or complex structure on $E$.

**Linearity of a fibre transport is the statement that it is a change of frame, not a computation with the connection.** Once a single starting frame $p$ is fixed and its transported frame $q=\Gamma(c)(p)$ is named, the transport map is forced to be $\iota_q\circ\iota_p^{-1}$, the composite of the two linear frame readings, and there is nothing left to prove about linearity — it is inherited from the linearity of the frame isomorphisms built into the associated-bundle construction. This is why parallel transport in *any* associated vector bundle is automatically linear, with no appeal to the specific connection: linearity comes from the associated-bundle structure, while the *particular* linear isomorphism (its holonomy content) comes from the connection. The diagnostic for reuse: to see that a transport, evaluation, or comparison map between fibres of an associated bundle is linear, exhibit it as $\iota_{q}\circ\iota_{p}^{-1}$ for appropriate frames; conversely, any nonlinearity signals that the map does not respect the frame structure and is not fibrewise of this form. This is the calculation-free companion to the exercise [[Ex - Horizontal Lifts in the Trivial Bundle with a Constant Connection]], where the same $PT_c$ is instead computed explicitly as $e^{-i(ax+by)}$ and its linearity is visible as multiplication by a scalar.
