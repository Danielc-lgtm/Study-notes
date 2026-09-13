---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - The Reduced Gauge Group Acts Freely on Connections"
  - "Def - Holonomy Group of a Connection"
  - "Thm - Properties of Parallel Transport"
  - "Def - Gauge Transformation"
  - "Def - Parallel Transport in a Principal Bundle"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\pi\colon P\to M$ be a principal $G$-bundle over a **connected** manifold $M$, let $b\in M$ be a base point, and fix a point $p\in P_b$ in the fibre over $b$. Let $\omega$ be a connection on $P$, and write
$$\operatorname{Stab}(\omega):=\{f\in\mathcal G(P):f^*\omega=\omega\}$$
for the stabiliser of $\omega$ inside the full gauge group $\mathcal G(P)$ under the right action $\omega\cdot f=f^*\omega$. Let $\operatorname{Hol}_p(\omega)\subseteq G$ be the holonomy group of $\omega$ based at $p$, and let
$$Z_G(H):=\{z\in G:zh=hz\ \text{for all}\ h\in H\}$$
denote the centraliser in $G$ of a subset $H\subseteq G$.

**Part (a).** Prove that the map
$$\Phi\colon\operatorname{Stab}(\omega)\longrightarrow G,\qquad \Phi(f)=z\ \text{ where }\ f(p)=p\cdot z,$$
is a well-defined injective group homomorphism whose image is exactly $Z_G(\operatorname{Hol}_p(\omega))$. Conclude that
$$\operatorname{Stab}(\omega)\ \cong\ Z_G\!\big(\operatorname{Hol}_p(\omega)\big).$$

**Part (b).** Deduce that a $U(1)$-connection always has stabiliser $U(1)$, realised by the constant gauge transformations, whatever its holonomy; and that an $SU(2)$-connection whose holonomy group is all of $SU(2)$ has stabiliser $\{\pm 1\}\cong\mathbb Z/2$.

This is the corollary drill of the freeness proposition B-T2.7.5 (Bär, Proposition 2.7.9); the source proves only the freeness of the reduced action, and asks the reader to draw the centraliser corollary, which we prove here in full for connected $M$.

**Recall.** We use the standing series conventions: $G$ acts on $P$ on the **right**, $R_g(q)=q\cdot g$; a gauge transformation is a fibre-preserving equivariant automorphism, and the gauge group acts on connections on the right by pullback. Parallel transport along a piecewise smooth curve $c$ is written $\Gamma_c$; the concatenation $c_2*c_1$ means "first $c_1$, then $c_2$"; the reversed curve is $\bar c$. The four recalled objects are the freeness proposition, the holonomy group, the properties of parallel transport, and the gauge group.

![[Thm - The Reduced Gauge Group Acts Freely on Connections#Statement]]

The **freeness proposition**, in the form used below: for $M$ connected and $b\in M$, the reduced gauge group $\mathcal G_b(P)=\{f\in\mathcal G(P):f|_{P_b}=\operatorname{id}_{P_b}\}$ acts freely on the space of connections $\mathcal A(P)$; that is, if $f\in\mathcal G_b(P)$ and $f^*\omega=\omega$, then $f=\operatorname{id}_P$. Its complete proof is on **[[Thm - The Reduced Gauge Group Acts Freely on Connections]]**; we invoke it, not reprove it.

![[Def - Holonomy Group of a Connection#The Definition]]

The **holonomy** of a loop $c$ based at $m=\pi(p)$ at the point $p$ is the unique $\operatorname{hol}_p(c)\in G$ with $\Gamma_c(p)=p\cdot\operatorname{hol}_p(c)$ (unique because $G$ acts freely and transitively on the fibre $P_m$); the **holonomy group** based at $p$ is $\operatorname{Hol}_p(\omega)=\{\operatorname{hol}_p(c):c\text{ a piecewise smooth loop at }m\}\subseteq G$, a subgroup of $G$.

![[Def - Gauge Transformation#The Definition]]

A **gauge transformation** $f\in\mathcal G(P)$ is a diffeomorphism $f\colon P\to P$ that is $G$-equivariant, $f(q\cdot g)=f(q)\cdot g$, and covers the identity of $M$, $\pi\circ f=\pi$. Equivariance and fibre-preservation together say that for each $q$ there is a unique $\tau(q)\in G$ with $f(q)=q\cdot\tau(q)$, and $\tau(q\cdot g)=g^{-1}\tau(q)\,g$; the group operation on $\mathcal G(P)$ is composition of maps.

![[Thm - Properties of Parallel Transport#Statement]]

The two **properties of parallel transport** we lean on are: property (4), the concatenation law $\Gamma_{c_2*c_1}=\Gamma_{c_2}\circ\Gamma_{c_1}$; and property (5), equivariance $\Gamma_c(q\cdot g)=\Gamma_c(q)\cdot g$. From property (3), orientation reversal, $\Gamma_{\bar c}=\Gamma_c^{-1}$. Their complete proofs are on **[[Thm - Properties of Parallel Transport]]**.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-symmetry-group* problem: we are handed one specific object (the connection $\omega$) and asked to name its symmetry group inside a large transformation group ($\mathcal G(P)$), and to do so by transporting the question into a *finite-dimensional* group ($G$) where it becomes tractable. Problems of this shape are solved by finding a faithful "value at a point" homomorphism from the infinite-dimensional group to the finite-dimensional one and computing its image. The payoff is structural: the stabiliser controls whether $\omega$ is a *reducible* connection and, downstream, whether the moduli space $\mathcal A(P)/\mathcal G(P)$ is a manifold near $[\omega]$ or has an orbifold singularity.

**Assumption pattern.** Two hypotheses do all the work, each exactly once. *Connectedness of $M$* is used to join any point of $M$ to the base point $b$ by a curve, so that parallel transport of the fixed frame $p$ reaches every fibre; it is what lets a single group element $z\in G$ propagate into a global gauge transformation. *Freeness of the reduced gauge action* (the invoked proposition) is used to kill the kernel of the evaluation map: a gauge transformation that fixes $\omega$ and fixes the fibre over $b$ must be the identity. Recognise the pattern "symmetry that fixes a base fibre is trivial" as the injectivity engine, and "connected base + parallel transport" as the surjectivity engine.

**Theorem routing.** The route for Part (a) is: define $\Phi(f)=z$ by evaluating at the fixed frame $p$; check $\Phi$ is a homomorphism by composing at $p$; get injectivity from the *freeness proposition* (kernel $=\operatorname{Stab}(\omega)\cap\mathcal G_b(P)=\{\operatorname{id}\}$); get "image $\subseteq$ centraliser" from the fact that a stabilising $f$ *commutes with parallel transport* (which follows from $f^*\omega=\omega$ preserving horizontal spaces) together with equivariance (property (5)); get "centraliser $\subseteq$ image" by *constructing* a gauge transformation from a central element, using connectedness and parallel transport, where the centraliser condition is precisely what makes the construction independent of the connecting curve. Part (b) then routes through two elementary group-theory computations: $Z_{U(1)}(\cdot)=U(1)$ because $U(1)$ is abelian, and $Z_{SU(2)}(SU(2))=\{\pm I\}$ because the only matrices commuting with all of $SU(2)$ are scalars.

**Key decision point.** The single non-obvious move is to read "$f$ stabilises $\omega$" as "$f$ commutes with every parallel transport". Nothing in the definition of the pullback action mentions holonomy; the bridge is Bär's observation that $\omega(df\,X)=(f^*\omega)(X)$, so $f^*\omega=\omega$ is equivalent to $df$ preserving the horizontal distribution, which is equivalent to $f$ carrying horizontal lifts to horizontal lifts, which is exactly commutation with parallel transport. Once that translation is made, the holonomy appears on its own: evaluating the commutation on a loop and cancelling by the free fibre action produces $za=az$ for every holonomy element $a$, and the whole problem collapses to a centraliser computation. The second, subtler decision is realising that the well-definedness of the *inverse* construction — building $f$ from $z$ — is not automatic: two curves from $b$ to a point differ by a loop, and the two candidate values of $f$ differ by exactly the commutator obstruction $za$ versus $az$, so they agree if and only if $z$ centralises the holonomy.

---

# Legal Operations Used

This solution deploys the following legal operations, in the sense of the [[Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections#Legal Operations|topic page's Legal Operations]]; where a number is given it refers to that list, and each is spelled out here in the form it takes for this problem.

1. **Evaluate an equivariant map at one frame to read off a group element.** A gauge transformation is determined on the fibre $P_b$ by its value at the single point $p$: $f(p)=p\cdot z$ with $z\in G$ unique. This turns the infinite-dimensional $f$ into the finite datum $z$.

2. **Translate "$f^*\omega=\omega$" into "$df$ preserves horizontal spaces".** Because $\omega(df\,X)=(f^*\omega)(X)=\omega(X)$, a stabilising $f$ sends horizontal vectors to horizontal vectors; combined with equivariance on the vertical part this is an if-and-only-if.

3. **Convert preservation of horizontal spaces into commutation with parallel transport.** If $df$ preserves horizontality then $f$ carries horizontal lifts to horizontal lifts covering the same base curve, so $f\circ\Gamma_c=\Gamma_c\circ f$ for every curve $c$.

4. **Cancel a free fibre action to extract a group identity.** From $p\cdot(za)=p\cdot(az)$ deduce $za=az$, because $G$ acts freely on the fibre.

5. **Kill a kernel with the freeness proposition.** A stabilising $f$ with $f(p)=p$ lies in $\mathcal G_b(P)$; by [[Thm - The Reduced Gauge Group Acts Freely on Connections|freeness of the reduced gauge action]] it is the identity, so $\Phi$ is injective.

6. **Parallel-transport a frame across a connected base to globalise a local datum.** For $M$ connected, join $b$ to any $m$ by a curve $c$ and transport $p$ to $\Gamma_c(p)\in P_m$; this spreads the single element $z$ into a value of $f$ on every fibre.

7. **Detect a well-definedness obstruction and discharge it with the centraliser hypothesis.** Changing the connecting curve changes $\Gamma_c(p)$ by a holonomy element $a$; the two candidate values of $f$ agree if and only if $za=az$, i.e. exactly when $z\in Z_G(\operatorname{Hol}_p(\omega))$.

8. **Compute a centraliser inside a concrete Lie group.** For Part (b), use abelianness of $U(1)$ and the scalar-matrix characterisation of $Z(SU(2))$.

---

# Hints

> [!note]- Hint 1
> A gauge transformation $f$ is equivariant and fixes each fibre, so on $P_b$ it is completely determined by the one element $z\in G$ with $f(p)=p\cdot z$. Define $\Phi(f)=z$. Check first that $\Phi$ is a group homomorphism by composing two gauge transformations *at the point $p$*.

> [!note]- Hint 2
> Injectivity: what does $\Phi(f)=e$ say about $f$ on the whole fibre $P_b$? Which subgroup of $\mathcal G(P)$ does $f$ then lie in, and what theorem tells you a stabilising element of that subgroup is trivial?

> [!note]- Hint 3
> The bridge to holonomy is: $\omega(df\,X)=(f^*\omega)(X)$. So if $f^*\omega=\omega$, then $df$ sends horizontal vectors to horizontal vectors, hence $f$ takes horizontal lifts to horizontal lifts and therefore commutes with every parallel transport, $f\circ\Gamma_c=\Gamma_c\circ f$.

> [!note]- Hint 4
> Apply the commutation to a loop $c$ at $b$ with $\Gamma_c(p)=p\cdot a$, $a\in\operatorname{Hol}_p(\omega)$. Using $f(p)=p\cdot z$ and property (5) ($\Gamma_c(q\cdot g)=\Gamma_c(q)\cdot g$), compute both sides of $f(\Gamma_c(p))=\Gamma_c(f(p))$ and cancel $p$ by freeness. You should land on $za=az$.

> [!note]- Hint 5
> Surjectivity: given $z\in Z_G(\operatorname{Hol}_p(\omega))$, build $f$. For $q\in P$ with $\pi(q)=m$, pick a curve $c$ from $b$ to $m$, write $q=\Gamma_c(p)\cdot h$, and set $f(q)=\Gamma_c(p)\cdot z\cdot h$. The one thing to verify carefully is independence of the choice of $c$: two curves differ by a loop, and the loop's holonomy $a$ makes the two answers differ by $za$ versus $az$.

> [!note]- Hint 6
> For Part (b): $U(1)$ is abelian, so its centraliser of anything is all of $U(1)$; the corresponding gauge transformations are the constant ones $f(q)=q\cdot z$. For $SU(2)$, a matrix commuting with both $\operatorname{diag}(i,-i)$ and $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ must be scalar; combine with $\det=1$.

---

# Solution

The proof builds a single homomorphism $\Phi$ from the (infinite-dimensional) stabiliser to the (finite-dimensional) group $G$, evaluating a gauge transformation at the fixed frame $p$, and then identifies its kernel and image. The kernel is trivial by the freeness proposition, so $\Phi$ is injective. The image lands inside the centraliser of the holonomy because a stabilising gauge transformation commutes with parallel transport, and evaluating that commutation on loops forces the value $z$ to commute with every holonomy element. Conversely every centralising $z$ produces a stabilising gauge transformation by parallel-transporting the frame across the connected base, the centraliser condition being exactly what makes the construction well defined. Part (b) is then two short centraliser computations.

**Step 0: $\operatorname{Stab}(\omega)$ is a subgroup and $\Phi$ is a well-defined map.**

Before anything else we record that the objects exist and $\Phi$ makes sense.

> [!note]- Derivation
> **$\operatorname{Stab}(\omega)$ is a subgroup of $\mathcal G(P)$.** The gauge group acts on connections on the right by $\omega\cdot f=f^*\omega$; concretely, for $f_1,f_2\in\mathcal G(P)$, $(f_1\circ f_2)^*\omega=f_2^*(f_1^*\omega)$ (contravariance of pullback under composition). If $f_1^*\omega=\omega$ and $f_2^*\omega=\omega$, then $(f_1\circ f_2)^*\omega=f_2^*\omega=\omega$ (substituting the two hypotheses in turn), so $\operatorname{Stab}(\omega)$ is closed under composition. It contains $\operatorname{id}_P$ since $\operatorname{id}^*\omega=\omega$. It is closed under inverses: from $f^*\omega=\omega$, apply $(f^{-1})^*$ to both sides to get $(f^{-1})^*f^*\omega=(f^{-1})^*\omega$, and the left side is $(f\circ f^{-1})^*\omega=\operatorname{id}^*\omega=\omega$, so $(f^{-1})^*\omega=\omega$. Hence $\operatorname{Stab}(\omega)\le\mathcal G(P)$.
>
> **$\Phi$ is well defined.** For $f\in\operatorname{Stab}(\omega)\subseteq\mathcal G(P)$, the point $f(p)$ lies in the same fibre as $p$ because $f$ covers the identity, $\pi(f(p))=\pi(p)=b$. The right $G$-action on the fibre $P_b$ is **transitive**, so $f(p)=p\cdot z$ for some $z\in G$, and it is **free**, so $z$ is unique. Set $\Phi(f):=z$. Uniqueness makes $\Phi$ single-valued.

**Step 1: $\Phi$ is a group homomorphism.**

Composition of gauge transformations corresponds to multiplication in $G$ of their values at $p$.

> [!note]- Derivation
> Let $f_1,f_2\in\operatorname{Stab}(\omega)$ with $f_i(p)=p\cdot z_i$, that is $z_i=\Phi(f_i)$. Then
> $$(f_1\circ f_2)(p)=f_1\big(f_2(p)\big)=f_1(p\cdot z_2)\qquad\text{(definition of }f_2(p))$$
> $$=f_1(p)\cdot z_2\qquad\text{(equivariance of }f_1\text{: }f_1(q\cdot g)=f_1(q)\cdot g)$$
> $$=(p\cdot z_1)\cdot z_2=p\cdot(z_1 z_2)\qquad\text{(definition of }f_1(p)\text{, associativity of the action).}$$
> By uniqueness of the fibre coordinate (Step 0), $\Phi(f_1\circ f_2)=z_1 z_2=\Phi(f_1)\Phi(f_2)$. Thus $\Phi$ is a homomorphism from $(\operatorname{Stab}(\omega),\circ)$ to $(G,\cdot)$.

**Step 2: $\Phi$ is injective.**

The kernel of $\Phi$ is the stabiliser inside the reduced gauge group, which is trivial by the freeness proposition.

> [!note]- Derivation
> Suppose $\Phi(f)=e$, so $f(p)=p\cdot e=p$. By equivariance, for every $g\in G$,
> $$f(p\cdot g)=f(p)\cdot g=p\cdot g\qquad\text{(equivariance; }f(p)=p).$$
> Since $G$ acts transitively on $P_b$, every point of $P_b$ has the form $p\cdot g$, so $f|_{P_b}=\operatorname{id}_{P_b}$. By definition this means $f\in\mathcal G_b(P)$, the reduced gauge group based at $b$. But $f\in\operatorname{Stab}(\omega)$ as well, so $f^*\omega=\omega$ with $f\in\mathcal G_b(P)$.
>
> Now invoke the [[Thm - The Reduced Gauge Group Acts Freely on Connections|freeness of the reduced gauge action]]: *for $M$ connected and $b\in M$, if $f\in\mathcal G_b(P)$ satisfies $f^*\omega=\omega$ then $f=\operatorname{id}_P$.* (This is exactly the hypothesis we have assembled; connectedness of $M$ is one of its standing hypotheses and holds here.) Therefore $f=\operatorname{id}_P$, so $\ker\Phi=\{\operatorname{id}_P\}$ and $\Phi$ is injective.

**Step 3: a stabilising gauge transformation commutes with parallel transport.**

This is the bridge that brings holonomy into a statement that mentions only the pullback of $\omega$.

> [!note]- Derivation
> Let $f\in\operatorname{Stab}(\omega)$, so $f^*\omega=\omega$. We show $df$ preserves the horizontal distribution $H^\omega=\ker\omega$, and hence $f\circ\Gamma_c=\Gamma_c\circ f$ for every curve $c$.
>
> **Verticals are preserved automatically.** For $\xi\in\mathfrak g$ the fundamental vector field is $\xi_P(q)=\frac{d}{dt}\big|_{0}q\cdot\exp(t\xi)$. By equivariance $f\circ R_{\exp(t\xi)}=R_{\exp(t\xi)}\circ f$, so
> $$df\big(\xi_P(q)\big)=\tfrac{d}{dt}\big|_{0}f\big(q\cdot\exp(t\xi)\big)=\tfrac{d}{dt}\big|_{0}f(q)\cdot\exp(t\xi)=\xi_P\big(f(q)\big)\qquad\text{(equivariance of }f).$$
> Hence $\omega\big(df\,\xi_P(q)\big)=\omega\big(\xi_P(f(q))\big)=\xi=\omega\big(\xi_P(q)\big)$ (the defining property $\omega(\xi_P)=\xi$ of a principal connection, used twice); so $f^*\omega=\omega$ holds on vertical vectors with no assumption.
>
> **Horizontals are preserved.** For any tangent vector $X$ at $q$,
> $$\omega\big(df\,X\big)=(f^*\omega)(X)=\omega(X)\qquad\text{(definition of pullback; }f^*\omega=\omega).$$
> If $X\in H^\omega_q=\ker\omega_q$ then $\omega(df\,X)=\omega(X)=0$, so $df\,X\in H^\omega_{f(q)}=\ker\omega_{f(q)}$. Thus $df(H^\omega_q)\subseteq H^\omega_{f(q)}$; since $f$ is a diffeomorphism $df$ is an isomorphism and $\dim H^\omega_q=\dim M=\dim H^\omega_{f(q)}$, so in fact $df(H^\omega_q)=H^\omega_{f(q)}$.
>
> **Commutation with parallel transport.** Let $c$ be a piecewise smooth curve and $\tilde c$ the $\omega$-horizontal lift with $\tilde c(t_0)=q_0$. The curve $f\circ\tilde c$ has velocity $df(\dot{\tilde c})$, which is horizontal by the previous paragraph, and it covers $c$ because $\pi\circ f\circ\tilde c=\pi\circ\tilde c=c$ (as $f$ covers the identity). Hence $f\circ\tilde c$ is the horizontal lift of $c$ with initial point $f(q_0)$, that is $f\circ\tilde c=\widetilde{c}^{\,f(q_0)}$. Evaluating at the endpoint $t_1$,
> $$f\big(\Gamma_c(q_0)\big)=f\big(\tilde c(t_1)\big)=(f\circ\tilde c)(t_1)=\Gamma_c\big(f(q_0)\big)\qquad\text{(uniqueness of horizontal lifts).}$$
> Since $q_0$ was arbitrary, $f\circ\Gamma_c=\Gamma_c\circ f$ for every curve $c$.

**Step 4: the image of $\Phi$ lies in the centraliser of the holonomy.**

Evaluating the commutation of Step 3 on loops turns it into the assertion that $z$ centralises every holonomy element.

> [!note]- Derivation
> Let $f\in\operatorname{Stab}(\omega)$ with $z=\Phi(f)$, so $f(p)=p\cdot z$. Take any loop $c$ based at $b$ and let $a:=\operatorname{hol}_p(c)\in\operatorname{Hol}_p(\omega)$, so that $\Gamma_c(p)=p\cdot a$ (definition of holonomy). Apply the commutation identity of Step 3 at $q_0=p$:
> $$f\big(\Gamma_c(p)\big)=\Gamma_c\big(f(p)\big).$$
> Compute the left side:
> $$f\big(\Gamma_c(p)\big)=f(p\cdot a)=f(p)\cdot a=(p\cdot z)\cdot a=p\cdot(za)\qquad\text{(}\Gamma_c(p)=p\cdot a\text{; equivariance of }f\text{; }f(p)=p\cdot z).$$
> Compute the right side, using property (5) of parallel transport, $\Gamma_c(q\cdot g)=\Gamma_c(q)\cdot g$:
> $$\Gamma_c\big(f(p)\big)=\Gamma_c(p\cdot z)=\Gamma_c(p)\cdot z=(p\cdot a)\cdot z=p\cdot(az)\qquad\text{(}f(p)=p\cdot z\text{; property (5); }\Gamma_c(p)=p\cdot a).$$
> Equating the two, $p\cdot(za)=p\cdot(az)$. The right action of $G$ on the fibre $P_b$ is **free**, so we may cancel $p$:
> $$za=az.$$
> As $c$ ranged over all loops at $b$, the element $a$ ranged over all of $\operatorname{Hol}_p(\omega)$, so $z$ commutes with every element of the holonomy group: $z\in Z_G(\operatorname{Hol}_p(\omega))$. Therefore $\Phi\big(\operatorname{Stab}(\omega)\big)\subseteq Z_G(\operatorname{Hol}_p(\omega))$.

**Step 5: the image of $\Phi$ contains the centraliser.**

Given a central element $z$, we construct a stabilising gauge transformation $f$ with $\Phi(f)=z$ by parallel-transporting the frame $p$ across the connected base; the centraliser condition is precisely what makes the construction independent of the connecting curve.

> [!note]- Derivation
> Fix $z\in Z_G(\operatorname{Hol}_p(\omega))$. Define $f\colon P\to P$ as follows. Given $q\in P$, put $m=\pi(q)$; since $M$ is **connected**, choose a piecewise smooth curve $c$ from $b$ to $m$ (connectedness of a manifold gives path-connectedness). Let $\tilde c$ be the $\omega$-horizontal lift with $\tilde c(0)=p$, so $\tilde c(1)=\Gamma_c(p)\in P_m$. Because $G$ acts transitively and freely on $P_m$, there is a unique $h\in G$ with $q=\Gamma_c(p)\cdot h$. Set
> $$f(q):=\Gamma_c(p)\cdot(z\,h).$$
>
> **Well-definedness (independence of $c$).** Let $c_1,c_2$ be two curves from $b$ to $m$, with $q=\Gamma_{c_1}(p)\cdot h_1=\Gamma_{c_2}(p)\cdot h_2$. The concatenation $\bar c_2*c_1$ (first $c_1$ from $b$ to $m$, then $\bar c_2$ from $m$ back to $b$) is a loop at $b$; let $a:=\operatorname{hol}_p(\bar c_2*c_1)\in\operatorname{Hol}_p(\omega)$. Then
> $$\Gamma_{\bar c_2*c_1}(p)=\Gamma_{\bar c_2}\big(\Gamma_{c_1}(p)\big)=\Gamma_{c_2}^{-1}\big(\Gamma_{c_1}(p)\big)\qquad\text{(property (4) concatenation; property (3) reversal, }\Gamma_{\bar c_2}=\Gamma_{c_2}^{-1}),$$
> and by definition of holonomy $\Gamma_{\bar c_2*c_1}(p)=p\cdot a$, so $\Gamma_{c_2}^{-1}(\Gamma_{c_1}(p))=p\cdot a$, i.e.
> $$\Gamma_{c_1}(p)=\Gamma_{c_2}(p\cdot a)=\Gamma_{c_2}(p)\cdot a\qquad\text{(property (5) equivariance).}$$
> Substituting into $q=\Gamma_{c_1}(p)\cdot h_1=\Gamma_{c_2}(p)\cdot h_2$ gives $\Gamma_{c_2}(p)\cdot(a h_1)=\Gamma_{c_2}(p)\cdot h_2$, so $h_2=a h_1$ (freeness). Now compare the two candidate values of $f(q)$:
> $$\text{via }c_1:\quad \Gamma_{c_1}(p)\cdot(z h_1)=\Gamma_{c_2}(p)\cdot(a z h_1)\qquad(\Gamma_{c_1}(p)=\Gamma_{c_2}(p)\cdot a),$$
> $$\text{via }c_2:\quad \Gamma_{c_2}(p)\cdot(z h_2)=\Gamma_{c_2}(p)\cdot(z a h_1)\qquad(h_2=a h_1).$$
> These agree if and only if $a z=z a$, which holds because $a\in\operatorname{Hol}_p(\omega)$ and $z\in Z_G(\operatorname{Hol}_p(\omega))$. This is the only place the centraliser hypothesis is used, and it is exactly what the construction demands. Hence $f(q)$ does not depend on the choice of $c$.
>
> **$f$ covers the identity and $\Phi(f)=z$.** By construction $\pi(f(q))=\pi(\Gamma_c(p)\cdot zh)=\pi(\Gamma_c(p))=m=\pi(q)$, so $\pi\circ f=\pi$. Taking $q=p$ (so $m=b$, the constant curve $c\equiv b$, $\Gamma_c=\operatorname{id}$ by property (1), and $h=e$) gives $f(p)=p\cdot(z e)=p\cdot z$, so $\Phi(f)=z$ once we know $f\in\mathcal G(P)$.
>
> **Equivariance.** If $q=\Gamma_c(p)\cdot h$ then $q\cdot g=\Gamma_c(p)\cdot(hg)$, so
> $$f(q\cdot g)=\Gamma_c(p)\cdot\big(z(hg)\big)=\big(\Gamma_c(p)\cdot(zh)\big)\cdot g=f(q)\cdot g\qquad\text{(associativity of the action).}$$
>
> **Smoothness and the diffeomorphism property.** Fix $q_0$ with $m_0=\pi(q_0)$, choose one curve $c_0$ from $b$ to $m_0$, and take a trivialising neighbourhood $U$ of $m_0$ with a smooth family of short curves $s_m$ from $m_0$ to $m\in U$ depending smoothly on $m$ (for instance straight segments in a chart). For $m\in U$ use $c_m:=s_m*c_0$; then $m\mapsto\Gamma_{c_m}(p)=\Gamma_{s_m}\big(\Gamma_{c_0}(p)\big)$ is a smooth local section $\sigma$ of $P$ over $U$, because horizontal lifts solve a first-order ordinary differential equation whose solution depends smoothly on the endpoint of the driving curve — the standard smooth dependence of solutions of ordinary differential equations on parameters, applied to the horizontal-lift equation of [[Thm - Existence and Uniqueness of Horizontal Lifts|the horizontal-lift theorem]]. Writing $q=\sigma(\pi q)\cdot\kappa(q)$ in this local trivialisation, with $\kappa\colon P|_U\to G$ smooth, the formula becomes $f(q)=\sigma(\pi q)\cdot\big(z\,\kappa(q)\big)$, which is smooth. Since $q_0$ was arbitrary, $f$ is smooth. The same construction with $z^{-1}\in Z_G(\operatorname{Hol}_p(\omega))$ (the centraliser is a subgroup) yields a smooth gauge transformation $f'$; composing at any point, $\Phi(f\circ f')=z z^{-1}=e$ and $\Phi(f'\circ f)=e$, and by the injectivity of Step 2 applied to the (already established) stabilising elements — or directly, since a map with a two-sided smooth inverse is a diffeomorphism — $f'=f^{-1}$. Thus $f\in\mathcal G(P)$.
>
> **$f$ stabilises $\omega$.** The construction makes $f$ commute with parallel transport: for a curve $\gamma$ from $m_0$ to $m_1$ and $q_0\in P_{m_0}$, choose $c$ from $b$ to $m_0$ and write $q_0=\Gamma_c(p)\cdot h$; then
> $$\Gamma_\gamma(q_0)=\Gamma_\gamma\big(\Gamma_c(p)\big)\cdot h=\Gamma_{\gamma*c}(p)\cdot h\qquad\text{(property (5); property (4)),}$$
> so, evaluating $f$ on $\Gamma_\gamma(q_0)$ through the curve $\gamma*c$,
> $$f\big(\Gamma_\gamma(q_0)\big)=\Gamma_{\gamma*c}(p)\cdot(zh)=\Gamma_\gamma\big(\Gamma_c(p)\big)\cdot(zh)=\Gamma_\gamma\big(\Gamma_c(p)\cdot(zh)\big)=\Gamma_\gamma\big(f(q_0)\big)\qquad\text{(property (4); property (5); definition of }f(q_0)).$$
> Hence $f\circ\Gamma_\gamma=\Gamma_\gamma\circ f$ for every $\gamma$. Consequently $f$ carries horizontal lifts to horizontal lifts (the image of a horizontal lift $\tilde\gamma$ under $f$ is $t\mapsto f(\Gamma_{\gamma|_{[0,t]}}(q_0))=\Gamma_{\gamma|_{[0,t]}}(f(q_0))$, a horizontal lift), so $df$ maps each horizontal space into a horizontal space; and $df$ maps fundamental fields to fundamental fields by equivariance, exactly as in Step 3. Reading Step 3 in reverse, $\omega(df\,X)=\omega(X)$ on both a vertical and a horizontal spanning set, hence on all of $TP$, so $f^*\omega=\omega$ and $f\in\operatorname{Stab}(\omega)$.
>
> Therefore $z=\Phi(f)$ lies in the image of $\Phi$, and $Z_G(\operatorname{Hol}_p(\omega))\subseteq\Phi(\operatorname{Stab}(\omega))$.

**Step 6: conclude Part (a).**

Steps 1–2 make $\Phi$ an injective homomorphism, and Steps 4–5 identify its image as $Z_G(\operatorname{Hol}_p(\omega))$. Hence $\Phi$ restricts to a group isomorphism onto its image, and
$$\operatorname{Stab}(\omega)\ \cong\ Z_G\!\big(\operatorname{Hol}_p(\omega)\big).$$
Replacing $p$ by $p\cdot g$ changes the holonomy group by conjugation, $\operatorname{Hol}_{p\cdot g}(\omega)=g^{-1}\operatorname{Hol}_p(\omega)\,g$ (the change-of-frame corollary on the holonomy page, [[Ex - Holonomy Groups at Different Base Points are Conjugate|holonomy at conjugate frames]]), and centraliser commutes with conjugation, $Z_G(g^{-1}Hg)=g^{-1}Z_G(H)g$, so the isomorphism type of the right-hand side is independent of the choice of $p$; connectedness makes it independent of $b$ likewise.

**Step 7: Part (b), the two special cases.**

> [!note]- Derivation
> **The $U(1)$ case.** Let $G=U(1)$. Since $U(1)$ is **abelian**, every element commutes with every other, so for any subgroup $H\subseteq U(1)$ the centraliser is the whole group, $Z_{U(1)}(H)=U(1)$. Applying Part (a) with $H=\operatorname{Hol}_p(\omega)$,
> $$\operatorname{Stab}(\omega)\cong Z_{U(1)}\big(\operatorname{Hol}_p(\omega)\big)=U(1),$$
> whatever the holonomy is. Concretely, the isomorphism sends $z\in U(1)$ to the **constant** gauge transformation $f_z(q)=q\cdot z$: this is a gauge transformation because for abelian $G$ a constant map $M\to G$ gives an equivariant fibre-preserving automorphism (the corresponding equivariant function is $\tau\equiv z$, and $\tau(q\cdot g)=g^{-1}zg=z$ holds since $G$ is abelian), and it stabilises *every* connection because under it the local connection form transforms by $A\mapsto\operatorname{Ad}_{z^{-1}}A+z^{-1}dz=A+0=A$ (the adjoint action is trivial for abelian $G$ and $dz=0$ for constant $z$). Thus the stabiliser of a $U(1)$-connection is exactly the circle of constant gauge transformations, $U(1)$.
>
> **The $SU(2)$ case.** Let $G=SU(2)$ and suppose $\operatorname{Hol}_p(\omega)=SU(2)$ (the connection has *full* holonomy). Then Part (a) gives
> $$\operatorname{Stab}(\omega)\cong Z_{SU(2)}(SU(2))=Z(SU(2)),$$
> the centre of $SU(2)$. We compute this centre by hand. A matrix $z\in SU(2)$ lies in the centre iff it commutes with every element of $SU(2)$; in particular with the two elements
> $$D=\begin{pmatrix}i&0\\0&-i\end{pmatrix}\in SU(2)\qquad(\det D=1,\ D^\dagger D=I),\qquad J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\in SU(2)\qquad(\det J=1,\ J^\dagger J=I).$$
> Write $z=\left(\begin{smallmatrix}\alpha&\beta\\\gamma&\delta\end{smallmatrix}\right)$. Commuting with $D$: $zD=Dz$ reads
> $$\begin{pmatrix}i\alpha&-i\beta\\ i\gamma&-i\delta\end{pmatrix}=\begin{pmatrix}i\alpha&i\beta\\ -i\gamma&-i\delta\end{pmatrix},$$
> forcing $\beta=\gamma=0$, so $z=\operatorname{diag}(\alpha,\delta)$. Commuting with $J$: $zJ=Jz$ reads
> $$\begin{pmatrix}0&\alpha\\-\delta&0\end{pmatrix}=\begin{pmatrix}0&\delta\\-\alpha&0\end{pmatrix},$$
> forcing $\alpha=\delta$. Hence $z=\alpha I$ is a scalar matrix. The constraints $z\in SU(2)$ give $\det z=\alpha^2=1$ and unitarity $|\alpha|=1$; the equation $\alpha^2=1$ has the two solutions $\alpha=\pm1$, both of modulus one. Therefore
> $$Z(SU(2))=\{+I,-I\}=\{\pm 1\}\cong\mathbb Z/2,$$
> and the stabiliser of a full-holonomy $SU(2)$-connection is $\{\pm 1\}$, realised by the two constant gauge transformations $f=\pm\operatorname{id}_P$ (that is, $q\mapsto q\cdot(\pm I)$).

> [!note]- Complete formal solution
> **Claim.** Let $\pi\colon P\to M$ be a principal $G$-bundle over a connected manifold $M$, $b\in M$, $p\in P_b$, and $\omega$ a connection. Then $\Phi\colon\operatorname{Stab}(\omega)\to G$, $\Phi(f)=z$ with $f(p)=p\cdot z$, is a well-defined injective homomorphism with image $Z_G(\operatorname{Hol}_p(\omega))$; hence $\operatorname{Stab}(\omega)\cong Z_G(\operatorname{Hol}_p(\omega))$. Consequently a $U(1)$-connection has stabiliser $U(1)$, and an $SU(2)$-connection with full holonomy has stabiliser $\{\pm1\}$.
>
> *Proof.* The set $\operatorname{Stab}(\omega)=\{f:f^*\omega=\omega\}$ is a subgroup, since $(f_1\circ f_2)^*\omega=f_2^*f_1^*\omega$ and pullback by inverses returns $\omega$. For $f\in\operatorname{Stab}(\omega)$, $f(p)$ lies in $P_b$ (as $f$ covers $\operatorname{id}_M$), and the free transitive $G$-action on $P_b$ gives a unique $z$ with $f(p)=p\cdot z$; define $\Phi(f)=z$.
>
> $\Phi$ is a homomorphism: $(f_1\circ f_2)(p)=f_1(p\cdot z_2)=f_1(p)\cdot z_2=p\cdot z_1z_2$, so $\Phi(f_1\circ f_2)=z_1z_2$.
>
> $\Phi$ is injective: if $\Phi(f)=e$ then $f(p)=p$, so by equivariance $f|_{P_b}=\operatorname{id}$ and $f\in\mathcal G_b(P)$; as $f^*\omega=\omega$ and $M$ is connected, the freeness of the reduced gauge action ([[Thm - The Reduced Gauge Group Acts Freely on Connections|freeness proposition]]) gives $f=\operatorname{id}$.
>
> A stabilising $f$ commutes with parallel transport: from $\omega(df\,X)=(f^*\omega)(X)=\omega(X)$, $df$ preserves horizontal spaces (on verticals $df$ preserves fundamental fields by equivariance), so $f$ sends horizontal lifts to horizontal lifts covering the same base curve, whence $f\circ\Gamma_c=\Gamma_c\circ f$.
>
> Image $\subseteq$ centraliser: for a loop $c$ at $b$ with $a=\operatorname{hol}_p(c)$, $f(\Gamma_c(p))=\Gamma_c(f(p))$ becomes $p\cdot(za)=p\cdot(az)$ (using $\Gamma_c(p)=p\cdot a$, equivariance of $f$, and property (5) $\Gamma_c(p\cdot z)=\Gamma_c(p)\cdot z$), so $za=az$ by freeness; as $a$ ranges over $\operatorname{Hol}_p(\omega)$, $z\in Z_G(\operatorname{Hol}_p(\omega))$.
>
> Image $\supseteq$ centraliser: given $z\in Z_G(\operatorname{Hol}_p(\omega))$ define, for $q$ with $\pi(q)=m$, a curve $c$ from $b$ to $m$ (connectedness), $q=\Gamma_c(p)\cdot h$, and $f(q)=\Gamma_c(p)\cdot(zh)$. Two curves $c_1,c_2$ from $b$ to $m$ satisfy $\Gamma_{c_1}(p)=\Gamma_{c_2}(p)\cdot a$ with $a=\operatorname{hol}_p(\bar c_2*c_1)\in\operatorname{Hol}_p(\omega)$ and $h_2=ah_1$; the two values of $f(q)$ are $\Gamma_{c_2}(p)\cdot(azh_1)$ and $\Gamma_{c_2}(p)\cdot(zah_1)$, equal because $az=za$. Thus $f$ is well defined; it is equivariant, covers $\operatorname{id}_M$, is smooth (parallel transport depends smoothly on the endpoint), has smooth inverse built from $z^{-1}$, and commutes with parallel transport, hence $f^*\omega=\omega$. Since $f(p)=p\cdot z$, $\Phi(f)=z$.
>
> Therefore $\Phi$ is an isomorphism onto $Z_G(\operatorname{Hol}_p(\omega))$, and $\operatorname{Stab}(\omega)\cong Z_G(\operatorname{Hol}_p(\omega))$.
>
> For $G=U(1)$, abelianness gives $Z_{U(1)}(H)=U(1)$ for any $H$, so $\operatorname{Stab}(\omega)\cong U(1)$, realised by the constant gauge transformations (which fix every connection because $\operatorname{Ad}$ is trivial and $dz=0$). For $G=SU(2)$ with $\operatorname{Hol}_p(\omega)=SU(2)$, a matrix commuting with $\operatorname{diag}(i,-i)$ and with $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ is a scalar $\alpha I$ with $\alpha^2=1$, so $Z(SU(2))=\{\pm I\}$ and $\operatorname{Stab}(\omega)\cong\{\pm1\}\cong\mathbb Z/2$. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to define $\Phi$ on the *whole* gauge group $\mathcal G(P)$ by $f\mapsto z$ with $f(p)=p\cdot z$ and claim it is a homomorphism onto $G$ with kernel the reduced gauge group, giving $\mathcal G(P)/\mathcal G_b(P)\cong G$. This is **false in general**: for $f\in\mathcal G(P)$ the value $f(p)=p\cdot\tau(p)$ is well defined, but the assignment $f\mapsto\tau(p)$ is a homomorphism only *after restricting to a subgroup where composition multiplies the values at $p$ without the twisting $\tau(q\cdot g)=g^{-1}\tau(q)g$ intervening*. The restriction to $\operatorname{Stab}(\omega)$ works precisely because a stabilising $f$ commutes with parallel transport, which is what pins its value at every other point to its value at $p$; a general gauge transformation has an independent value in each fibre and no such rigidity. The extra condition that rescues the naive map is exactly "$f^*\omega=\omega$".

---

# Key Takeaways

**The symmetry group of a geometric object is computed by evaluating symmetries at one point and identifying which finite datum they leave.** The whole proof is an instance of a recurring move: an infinite-dimensional symmetry group (here $\operatorname{Stab}(\omega)\subseteq\mathcal G(P)$) is understood by an evaluation homomorphism into a finite-dimensional group (here $\Phi$ into $G$), after which the problem becomes the twin questions "what is the kernel?" and "what is the image?". The kernel measures symmetries invisible at the chosen point — killed here by a rigidity theorem (freeness) — and the image measures which point-values are actually achievable — constrained here by a compatibility condition (centralising the holonomy). The trigger for this strategy is any question of the form "how large is the symmetry group of this specific structure?", especially when the symmetries are rigid enough that their value at one point determines them elsewhere. The same pattern computes isometry groups of homogeneous spaces (evaluate at a point, land in the isotropy group) and automorphism groups of covering spaces (evaluate at one lift, land in the deck group).

**A connection's stabiliser sees only the holonomy, because stabilising the connection is the same as commuting with parallel transport.** The conceptual heart is the equivalence, for a gauge transformation $f$: $f^*\omega=\omega\iff df$ preserves the horizontal distribution $\iff f$ carries horizontal lifts to horizontal lifts $\iff f\circ\Gamma_c=\Gamma_c\circ f$ for every curve. Once a symmetry commutes with all parallel transports, its interaction with the connection is entirely encoded by how its value at one frame interacts with the loop-transports, i.e. with the holonomy group. This is the precise sense in which "the holonomy group is the reduced-in-one-point form of the connection": everything about $\omega$ that a gauge symmetry can feel is contained in $\operatorname{Hol}_p(\omega)\subseteq G$. The diagnostic to carry away: whenever a computation involves a symmetry of a connection, replace the differential-geometric condition $f^*\omega=\omega$ by the algebraic condition "commutes with parallel transport", and then specialise to loops to bring the holonomy on stage.

**The size of the stabiliser is the reducibility of the connection, and this is what makes the moduli space singular.** The centraliser $Z_G(\operatorname{Hol}_p(\omega))$ is small exactly when the holonomy is large. At one extreme, if $\operatorname{Hol}_p(\omega)=G$ the stabiliser is the centre $Z(G)$ — the smallest it can be — and the connection is called *irreducible*; at the other extreme, if the holonomy reduces into a proper subgroup the centraliser grows and the connection is *reducible*. Part (b) is the two archetypes: an $SU(2)$-connection with full holonomy has stabiliser the centre $\{\pm1\}$, the generic irreducible case; every $U(1)$-connection has stabiliser all of $U(1)$, the maximally reducible abelian case, because an abelian structure group can never distinguish points of its own conjugation orbits. This is not a curiosity: the gauge group $\mathcal G(P)$ acts on the space of connections $\mathcal A(P)$ with these stabilisers as isotropy groups, so the quotient $\mathcal A(P)/\mathcal G(P)$ is a smooth manifold near irreducible connections (free-modulo-centre action) but has orbifold or cone singularities at reducible ones. In Donaldson theory it is exactly the reducible $SU(2)$-connections, whose holonomy sits inside a $U(1)$ and whose stabiliser jumps from $\{\pm1\}$ up to a circle, that produce the singular points of the instanton moduli space whose counting drives the diagonalisation theorem; recognising a stabiliser larger than the centre is the signal that one has landed on such a reducible, and the trigger to switch from the smooth to the singular local model.
