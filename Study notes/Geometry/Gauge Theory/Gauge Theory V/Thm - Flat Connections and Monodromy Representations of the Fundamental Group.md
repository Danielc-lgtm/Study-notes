---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop"
  - "Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group"
  - "Thm - Local Triviality of Flat Connections"
  - "Thm - Gauge Transformations Act on Connections and Curvature"
  - "Thm - Properties of Parallel Transport"
  - "Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles"
  - "Def - Associated Bundle"
  - "Def - Reduction and Extension of the Structure Group"
  - "Def - Flat Connection"
  - "Def - Holonomy Group of a Connection"
  - "Def - Parallel Transport in a Principal Bundle"
  - "Def - Principal G-Bundle"
  - "Def - Representation of a Lie Group"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a connected smooth manifold with a fixed base point $m\in M$, and $G$ is a Lie group acting on principal bundles on the **right**, $R_g(p)=p\cdot g$. We write $\Gamma:=\pi_1(M,m)$ for the [[Def - Path-Product and the Fundamental Group|fundamental group]] of $M$ at $m$, whose elements are homotopy classes $[\gamma]$ of loops at $m$, with product $[\gamma_1][\gamma_2]=[\gamma_1\ast\gamma_2]$ (the class of "$\gamma_1$ first, then $\gamma_2$"), identity $[c_m]$ (the constant loop), and inverse $[\gamma]^{-1}=[\bar\gamma]$ (the reversed loop). By [[Thm - The Fundamental Group is a Group|the theorem that π₁ is a group]], this is a group.

We write $q\colon\tilde M\to M$ for the [[Def - Universal Cover|universal cover]] of $M$, with a fixed lift $\tilde m\in q^{-1}(m)$ of the base point, and we take as given the structure theorem [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|of the universal cover]]: $\tilde M$ is a simply connected smooth manifold, $q$ is a smooth covering map, and $\Gamma$ acts on $\tilde M$ on the right, smoothly, freely and properly discontinuously, making $q\colon\tilde M\to M$ a **principal $\Gamma$-bundle for the discrete group $\Gamma$**. We write the deck action as $\tilde x\cdot[\gamma]$ and adopt the convention (fixed on that page) that the lift $\tilde\gamma$ of a loop $\gamma$ at $m$ representing $[\gamma]$, starting at $\tilde m$, ends at $\tilde\gamma(1)=\tilde m\cdot[\gamma]$.

A [[Def - Connection on a Principal Bundle|connection]] on a principal $G$-bundle $\pi\colon P\to M$ is a $\mathfrak g$-valued one-form $\omega\in\Omega^1(P;\mathfrak g)$ with $\omega(\xi_P)=\xi$ and $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$; its horizontal distribution is $H=\ker\omega$, a $G$-invariant complement to the vertical bundle. A connection is [[Def - Flat Connection|flat]] when its curvature $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$ vanishes; $\mathcal A^\flat(P)\subseteq\mathcal A(P)$ denotes the set of flat connections on $P$. For a piecewise smooth path $c\colon[0,1]\to M$ we write $\Gamma_c\colon P_{c(0)}\to P_{c(1)}$ for [[Def - Parallel Transport in a Principal Bundle|parallel transport]] along $c$ (the endpoint of the horizontal lift). For a loop $c$ at $m$ and $p\in P_m$, the [[Def - Holonomy Group of a Connection|holonomy]] $\operatorname{hol}_p(c)\in G$ is the unique group element with $\Gamma_c(p)=p\cdot\operatorname{hol}_p(c)$.

The [[Def - Gauge Transformation|gauge group]] $\mathcal G(P)$ is the group of $G$-equivariant diffeomorphisms $f\colon P\to P$ covering $\operatorname{id}_M$ (equivalently, the automorphisms of $P$ over the identity); it acts on connections on the right by $\omega\cdot f=f^*\omega$. We write $\mathcal M^\flat(P):=\mathcal A^\flat(P)/\mathcal G(P)$ for the moduli space of flat connections on a fixed bundle $P$, and, letting $P$ range over all isomorphism classes of principal $G$-bundles over $M$,
$$\mathcal M^\flat_G(M):=\{(P,\omega):P\to M\text{ a principal }G\text{-bundle},\ \omega\in\mathcal A^\flat(P)\}\big/\cong,$$
where $(P,\omega)\cong(P',\omega')$ means there is a bundle isomorphism $P\to P'$ over $\operatorname{id}_M$ carrying $\omega$ to $\omega'$. The **representation variety** is
$$\mathcal R(M;G):=\operatorname{Hom}(\Gamma,G)/\!\sim,\qquad \rho\sim\rho'\iff \rho'=a\,\rho(\cdot)\,a^{-1}\text{ for some }a\in G,$$
the set of group homomorphisms $\rho\colon\Gamma\to G$ modulo conjugation, and $[\rho]$ its classes. A [[Def - Representation of a Lie Group|representation]] here means only a group homomorphism into $G$; no continuity is imposed because $\Gamma$ is discrete.

Given a homomorphism $\rho\colon\Gamma\to G$, the **flat bundle of $\rho$** is the [[Def - Reduction and Extension of the Structure Group|extension of the structure group]] of the principal $\Gamma$-bundle $\tilde M$ along $\rho$, that is, the [[Def - Associated Bundle|associated bundle]]
$$P_\rho:=\tilde M\times_\rho G:=(\tilde M\times G)\big/\Gamma,\qquad (\tilde x\cdot[\gamma],\,g)\sim(\tilde x,\,\rho([\gamma])\,g)\ \ \forall[\gamma]\in\Gamma,$$
with class of $(\tilde x,g)$ written $[\tilde x,g]$, projection $[\tilde x,g]\mapsto q(\tilde x)$, and right $G$-action $[\tilde x,g]\cdot h:=[\tilde x,gh]$.

> [!warning] Convention: source typo in Haydys D3.3.6, and the deck/monodromy sign
> Haydys writes the input representation as "$\rho\colon\tilde M\to GL_k(\mathbb R)$" (Introduction to Gauge Theory, p. 33); this is a typo for $\rho\colon\pi_1(M)\to GL_k(\mathbb R)$, the domain being the fundamental group, and we use the corrected form. The deck-action convention above (lift of $[\gamma]$ from $\tilde m$ ends at $\tilde m\cdot[\gamma]$) is the one fixed on [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover page]] and is chosen compatibly with the path-product convention $[\gamma_1][\gamma_2]=[\gamma_1\ast\gamma_2]$ and with the holonomy convention $\Gamma_c(p)=p\cdot\operatorname{hol}_p(c)$, so that the monodromy $[\gamma]\mapsto\operatorname{hol}_p(c_{[\gamma]})$ is a genuine group homomorphism $\Gamma\to G$ (this is the content of [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|the homotopy-invariance theorem]]). The opposite choice of deck action replaces $\rho$ by $[\gamma]\mapsto\rho([\gamma]^{-1})$ throughout and changes nothing about the correspondence, since $\rho\mapsto\rho(\,\cdot^{-1})$ is a bijection of $\operatorname{Hom}(\Gamma,G)$ commuting with conjugation.

---

# Statement

> **Theorem (flat connections and monodromy representations).** Let $M$ be a connected manifold with base point $m$, let $G$ be a Lie group, and let $q\colon\tilde M\to M$ be the universal cover carrying the right deck action of $\Gamma=\pi_1(M,m)$.
>
> **(a) Representations produce flat bundles.** For every homomorphism $\rho\colon\Gamma\to G$ the bundle $P_\rho=\tilde M\times_\rho G$ is a principal $G$-bundle over $M$, and it carries a canonical flat connection $\omega_\rho$, namely the descent of the product (Maurer–Cartan) connection on $\tilde M\times G\to\tilde M$; its horizontal curves are exactly the images of curves in $\tilde M\times\{g\}$. The monodromy representation of $\omega_\rho$ at the base point $p_0:=[\tilde m,e]\in(P_\rho)_m$ equals $\rho$:
> $$\operatorname{hol}_{p_0}(c_{[\gamma]})=\rho([\gamma])\qquad\text{for every loop }c_{[\gamma]}\text{ at }m\text{ with }[c_{[\gamma]}]=[\gamma].$$
> For a representation $V$ of $G$ (a homomorphism $G\to GL(V)$) the associated vector bundle $\tilde M\times_\rho V$ carries the induced flat covariant derivative, which is characterised by $\pi^\ast\nabla s=d\hat s$ for the $\Gamma$-equivariant map $\hat s\colon\tilde M\to V$ representing a section $s$ (Haydys' formula (47) with local connection form $a=0$).
>
> **(b) Flat connections come from their monodromy (developing map).** Conversely, let $\omega\in\mathcal A^\flat(P)$ be a flat connection on a principal $G$-bundle $P\to M$, fix $p\in P_m$, and let $\rho_\omega\colon\Gamma\to G$ be its monodromy representation at $p$. Then there is an isomorphism of principal $G$-bundles over $\operatorname{id}_M$,
> $$\Phi\colon P_{\rho_\omega}\xrightarrow{\ \cong\ }P,\qquad \Phi[\tilde x,g]=\Gamma_c(p)\cdot g,$$
> where $c$ is the $q$-projection of any path in $\tilde M$ from $\tilde m$ to $\tilde x$, and $\Phi$ carries $\omega_{\rho_\omega}$ to $\omega$. In particular $(P_{\rho_\omega},\omega_{\rho_\omega})\cong(P,\omega)$ as bundles with connection.
>
> **(c) Gauge equivalence corresponds to conjugation.** If $\omega,\omega'\in\mathcal A^\flat(P)$ are gauge equivalent, $\omega'=f^\ast\omega$ with $f\in\mathcal G(P)$, then $\rho_{\omega'}=s^{-1}\rho_\omega(\cdot)\,s$ for some $s\in G$; conjugate representations $\rho'=a\rho(\cdot)a^{-1}$ produce isomorphic flat bundles $(P_{\rho'},\omega_{\rho'})\cong(P_\rho,\omega_\rho)$.
>
> **(d) The bijection.** The assignment $[(P,\omega)]\mapsto[\rho_\omega]$ is a well-defined bijection
> $$\mathcal M^\flat_G(M)\ \xrightarrow{\ \cong\ }\ \mathcal R(M;G)=\operatorname{Hom}(\pi_1(M,m),G)/\text{conjugation}.$$
> For $G=GL_k(\mathbb R)$ this is the correspondence between flat rank-$k$ real vector bundles (all bundles at once) and $\mathcal R(M;GL_k(\mathbb R))$. For a fixed bundle $P$, $\mathcal M^\flat(P)=\mathcal A^\flat(P)/\mathcal G(P)$ is carried bijectively onto the subset of $\mathcal R(M;G)$ consisting of those $[\rho]$ whose flat bundle $P_\rho$ is isomorphic to $P$.

> **Corollary (compact and classical variants).** Restricting $G$ gives the same statement verbatim: with $G=O(k),U(k),SO(k),SU(k)$ one obtains bijections $\mathcal M^\flat_G(M)\cong\mathcal R(M;G)$, and for a Euclidean or Hermitian flat vector bundle the monodromy lands in $O(k)$ or $U(k)$. These are the special cases of the theorem for those Lie groups (Haydys, Remark 105).

The two statements are tied together by part (d): the corollary is the theorem applied to the subgroups $O(k),U(k),SO(k),SU(k)\subseteq GL_k(\mathbb C)$, using that parallel transport of a metric (respectively Hermitian) connection is orthogonal (respectively unitary).

---

# Motivation

A flat connection is, on its face, an analytic object: a solution of the nonlinear partial differential equation $F=0$ on a bundle, considered modulo the action of the infinite-dimensional gauge group. The moduli space $\mathcal M^\flat(P)=\mathcal A^\flat(P)/\mathcal G(P)$ is therefore the very first "space of solutions of a gauge-theoretic equation modulo gauge" that one meets, and the natural questions about it — is it compact, is it a manifold, what does it remember about $M$? — are the questions one will later ask about instanton and Seiberg–Witten moduli spaces, where they are hard. This theorem answers all of them at once for flat connections by translating the analytic object into a completely different, entirely algebraic and finite object: a homomorphism from the fundamental group into $G$, taken up to conjugacy.

The bridge is holonomy. A connection lets one transport a fibre along a path; when the connection is flat, [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|the transport around a loop depends only on the loop's homotopy class]], so the transport data collapses to one group element per element of $\pi_1(M,m)$. Composability of transport makes the assignment a homomorphism $\rho_\omega\colon\pi_1(M,m)\to G$. The theorem is the statement that this passage loses nothing and adds nothing: every homomorphism arises, two connections give conjugate homomorphisms exactly when they are gauge equivalent, and so the analytic moduli space $\mathcal M^\flat_G(M)$ and the algebraic representation variety $\mathcal R(M;G)$ are the same set.

Why should one believe an equivalence this strong? Because the universal cover $\tilde M$ is, tautologically, the space of homotopy classes of paths out of the base point, and $\pi_1(M,m)$ is the group of deck transformations that permutes the sheets. A flat connection that only sees homotopy classes of paths is therefore exactly the data of how to move between the sheets of $\tilde M$ — and moving between sheets is what a homomorphism $\rho\colon\Gamma\to G$ tells a $G$-bundle to do. The construction $P_\rho=\tilde M\times_\rho G$ realises this literally: it glues the trivial bundle over the sheets of $\tilde M$ using $\rho$ to jump across deck transformations, and the flat connection is nothing but "stay on your sheet". Part (b), the developing map, undoes the construction: it reconstructs the total space of $P$ by transporting a single chosen frame $p\in P_m$ out along all paths, using flatness to guarantee the answer is single-valued on $\tilde M$.

Concretely, the smallest interesting instance is $M=S^1$, $G=U(1)$. Here $\Gamma=\mathbb Z$, so $\operatorname{Hom}(\mathbb Z,U(1))=U(1)$ and conjugation is trivial (abelian $G$), giving $\mathcal R(S^1;U(1))=U(1)$. On the bundle side, a flat $U(1)$-connection on the trivial bundle over the circle is $A=ia\,d\theta$ up to gauge, and its holonomy around the circle is $e^{-2\pi i a}\in U(1)$; changing $a$ by an integer is a large gauge transformation and does not change the holonomy. The correspondence reads "the flat connection is completely remembered by the phase you pick up going around once", which is exactly $\rho(1)=e^{-2\pi i a}$. The theorem says the same thing for every $M$ and every $G$.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's stated hypothesis is a flat connection on a principal bundle, but the real skill is recognising when a problem hands you a flat connection or a representation without naming one.

A first disguised source is **a bundle equipped with a locally constant transition cocycle**, that is, a bundle whose structure "does not vary continuously". By [[Thm - Local Triviality of Flat Connections|the local-triviality theorem]] — a connection is flat if and only if there is a trivialising atlas whose transition functions $g_{\alpha\beta}$ are locally constant — such a bundle carries a canonical flat connection (the one that is the product connection in each of these charts). So any construction that produces a bundle by gluing trivial pieces with constant clutching data, for instance the tangent bundle of a flat torus or a bundle built from a covering space, is secretly an object of $\mathcal R(M;G)$. *Example problem:* the Möbius band is the real line bundle over $S^1$ glued by the constant map $-1\in O(1)$; recognising the constant cocycle exhibits it as the flat bundle of the sign representation $\rho\colon\mathbb Z\to O(1)$, $1\mapsto-1$, and the theorem then predicts its holonomy is $-1$ and it admits no flat connection with trivial holonomy.

A second disguised source is **a differential equation with a multivalued but locally single-valued solution**, whose "monodromy" is a representation of $\pi_1$ of the domain. A linear ordinary differential equation with regular singular points on a punctured Riemann surface, or a local system of solutions to a Fuchsian system, defines a flat connection on the bundle of solutions, and continuation around a loop is exactly parallel transport. The non-obvious bridge is that "how the solution basis is permuted after analytic continuation around a puncture" *is* the monodromy representation $\rho_\omega$ of a flat connection. *Example problem:* the hypergeometric equation on $\mathbb{CP}^1\setminus\{0,1,\infty\}$ has a rank-two solution bundle whose flat connection has monodromy in $GL_2(\mathbb C)$ around each puncture; the theorem places the whole equation into $\mathcal R(\mathbb{CP}^1\setminus\{0,1,\infty\};GL_2(\mathbb C))$.

A third disguised source is **a critical point of the Chern–Simons functional**. As computed in Haydys' Proposition 98, the critical points of the Chern–Simons functional $\vartheta$ on a three-manifold are precisely the flat connections, because $d\vartheta_A(a)=\tfrac1{4\pi^2}\int_M\operatorname{tr}(F_A\wedge a)$ vanishes for all $a$ if and only if $F_A=0$. Thus a variational problem whose Euler–Lagrange equation is $F=0$ delivers a flat connection, and this theorem turns the set of critical points modulo gauge into the representation variety. *Example problem:* enumerating the critical points of Chern–Simons theory on a three-manifold $Y$ (the input to the Casson invariant and to Floer homology) is the same as enumerating $\mathcal R(Y;SU(2))$, an algebraic problem about $\pi_1(Y)$.

**Targets (Output Amplification)**

Combine the bijection with **compactness of $G$**. When $G$ is compact, $\mathcal R(M;G)$ is a closed subset of a finite power of $G$ modulo conjugation and is therefore compact; through the theorem this proves that the moduli space of flat connections with compact structure group is compact, the first compactness result of gauge theory. The extra ingredient is finite generation of $\pi_1$ together with the compactness of $G$; the payoff is a topological finiteness statement about an infinite-dimensional analytic quotient, obtained without any analysis. This is developed on [[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact|the compactness page]].

Combine the bijection with **a presentation of $\pi_1(M,m)$**. If $\pi_1(M,m)=\langle\gamma_1,\dots,\gamma_N\mid r_1,\dots,r_k\rangle$, then $\operatorname{Hom}(\pi_1,G)=\{(g_1,\dots,g_N)\in G^N:r_j(g)=e\}$, an explicit algebraic subvariety of $G^N$, and $\mathcal M^\flat_G(M)$ is its quotient by diagonal conjugation. The extra ingredient is a group presentation; the payoff is coordinates on the moduli space. For a closed genus-$\gamma$ surface, $\pi_1=\langle a_i,b_i\mid\prod_i[a_i,b_i]=1\rangle$, so $\mathcal M^\flat_G(\Sigma_\gamma)=\{(A_i,B_i)\in G^{2\gamma}:\prod_i[A_i,B_i]=e\}/G$, the character variety that carries the Atiyah–Bott symplectic structure and, for $G=SL(n;\mathbb C)$, the theory of Higgs bundles.

Combine the bijection with **the classification of flat bundles by their underlying topological type**. For a fixed $G$, part (d) partitions $\mathcal R(M;G)$ according to which isomorphism class of principal bundle $P_\rho$ each representation produces; two representations give isomorphic underlying bundles exactly when their bundles are abstractly isomorphic (forgetting the flat connection). The extra ingredient is a bundle-classification theorem, for instance classification by the first Chern class for $U(1)$; the payoff is that a topological invariant of $P$ (a characteristic class) becomes computable as a locally constant function on the representation variety, and for a flat bundle every real characteristic class vanishes because $F=0$ makes every Chern–Weil form zero.

---

# Why Is It True

Strip away the constructions and ask what a flat connection actually is as a piece of transport data. A connection lets you carry the fibre $P_{c(0)}$ to the fibre $P_{c(1)}$ along a path $c$; in general the answer depends on the whole path. Flatness is exactly the statement that the answer depends only on the homotopy class of the path relative to its endpoints — this is [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|the homotopy-invariance theorem]], and geometrically it is because zero curvature makes the horizontal planes tangent to a foliation, so nearby homotopic paths lift to nearby leaves and reach the same point. A flat connection is therefore a rule that assigns to each homotopy class of paths an isomorphism of fibres, compatibly with concatenation.

Now recall what the universal cover is: a point of $\tilde M$ over $x\in M$ is a homotopy class of paths from $m$ to $x$, and the deck group $\Gamma=\pi_1(M,m)$ acts by pre-composing with loops at $m$, permuting the classes. So "a rule assigning an isomorphism of fibres to each homotopy class of paths" is the same as "a way of identifying all the fibres once you have chosen a sheet of $\tilde M$". The only freedom left is what happens when you change sheets, that is, when you act by a deck transformation $[\gamma]\in\Gamma$: the transport picks up a group element $\rho([\gamma])\in G$. Composability of transport forces $\rho$ to be a homomorphism. This is the whole content.

> **A flat connection is a rule for transporting fibres that sees only the homotopy class of the path; the universal cover is the space of homotopy classes of paths from the base point, so the transport data is exactly one group element of $G$ for each deck transformation — that is, a homomorphism $\rho\colon\pi_1(M,m)\to G$.**

The two constructions in the theorem are the two directions of this identification made concrete. Building $P_\rho=\tilde M\times_\rho G$ takes the trivial bundle over each sheet and, at each deck transformation, jumps by $\rho([\gamma])$; "stay on your sheet" is a horizontal distribution, and it is flat because on each sheet nothing is happening. Conversely the developing map $\Phi$ takes a genuine flat $(P,\omega)$ and reconstructs it by transporting one chosen frame $p\in P_m$ out to every point of $\tilde M$; flatness (homotopy invariance) is exactly what makes this single-valued on $\tilde M$, and the ambiguity across sheets is measured by the monodromy $\rho_\omega$, which is why $\Phi$ descends from $\tilde M\times G$ to $\tilde M\times_{\rho_\omega}G=P_{\rho_\omega}$. Finally, moving the chosen frame $p$ to $p\cdot s$ conjugates every holonomy by $s$, so only the conjugacy class of $\rho_\omega$ is intrinsic — which is why the target is $\operatorname{Hom}(\Gamma,G)/\text{conjugation}$ and not $\operatorname{Hom}(\Gamma,G)$ itself.

---

# What Makes This Hard

The subtle points are three, and each is a well-definedness question rather than a computation. First, the developing map $\Phi[\tilde x,g]=\Gamma_c(p)\cdot g$ is defined by choosing a path $c$; one must show the value is independent of the path, which is exactly where flatness enters through the homotopy-invariance theorem — and it is easy to invoke homotopy invariance for loops while forgetting that here the two competing paths in $\tilde M$ have the *same* endpoints precisely because $\tilde M$ is simply connected, so their projections are homotopic rel endpoints downstairs. Second, one must check that $\Phi$ is constant on $\Gamma$-orbits with the correct twist by $\rho_\omega$; the twist appears because transporting across a deck transformation contributes a holonomy factor, and getting the side (left versus right multiplication) and the direction of the concatenation right is where sign and ordering errors live. Third, the passage to conjugacy classes must be shown to be exactly the passage to gauge orbits in *both* directions: gauge-equivalent connections give conjugate representations (the easy direction) and, crucially, conjugate representations give isomorphic flat bundles and hence gauge-equivalent connections once the bundles are identified (the direction that makes the map injective). Overlooking either half collapses the bijection to a mere surjection.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build the two constructions — the flat bundle $P_\rho$ of a representation, and the developing map $\Phi$ of a flat connection — and show they are mutually inverse up to conjugation and gauge. Every step reduces to (i) the homotopy invariance of flat parallel transport, (ii) the description of $\tilde M$ as a principal $\Gamma$-bundle whose loops lift to deck transformations, and (iii) the equivariance and composition laws of parallel transport.

**Subgoal decomposition:**

1. **$P_\rho$ is a principal $G$-bundle.**
   - *Hint:* Over an evenly covered $U\subseteq M$, $q^{-1}(U)\cong U\times\Gamma$ as $\Gamma$-spaces; substitute into $\tilde M\times_\rho G$ and the $\Gamma$ collapses to give $U\times G$.
   - *Why needed:* Without knowing $P_\rho$ is a bundle there is nothing to put a connection on.

2. **The product connection descends to a flat $\omega_\rho$ on $P_\rho$.**
   - *Hint:* The product connection on $\tilde M\times G$ has horizontal distribution $T\tilde M\oplus 0$; check it is invariant under the diagonal $\Gamma$-action, which multiplies the $G$-factor on the left, and use left-invariance of the horizontal distribution.
   - *Why needed:* It is the canonical connection whose monodromy will be $\rho$, and flatness makes it an element of $\mathcal A^\flat(P_\rho)$.

3. **The monodromy of $\omega_\rho$ at $p_0=[\tilde m,e]$ is $\rho$.**
   - *Hint:* Lift a loop $c_{[\gamma]}$ to the sheet-curve $t\mapsto[\tilde\gamma(t),e]$, which is horizontal, and read off its endpoint using $\tilde\gamma(1)=\tilde m\cdot[\gamma]$ and the equivalence relation.
   - *Why needed:* It proves the construction of part (a) has the advertised monodromy, giving surjectivity of the final map.

4. **The developing map $\Phi$ is a well-defined, $G$-equivariant bundle map over $\operatorname{id}_M$.**
   - *Hint:* Well-definedness in the path uses simple-connectivity of $\tilde M$ plus homotopy invariance; $\Gamma$-equivariance with the twist $\rho_\omega$ uses that a deck transformation contributes one holonomy factor.
   - *Why needed:* It is the inverse construction; it reconstructs $P$ from $\rho_\omega$.

5. **$\Phi$ is an isomorphism carrying $\omega_{\rho_\omega}$ to $\omega$.**
   - *Hint:* A $G$-equivariant bundle map over the identity is automatically fibrewise bijective; it carries connections because it maps sheet-curves (the horizontal lifts upstairs) to $\omega$-horizontal lifts (parallel transports).
   - *Why needed:* It upgrades part (b) to an isomorphism of bundles with connection, which is what injectivity of the final map needs.

6. **Gauge equivalence $\Leftrightarrow$ conjugacy.**
   - *Hint:* If $\omega'=f^\ast\omega$ then $\Gamma^{\omega'}_c=f^{-1}\circ\Gamma^\omega_c\circ f$, and $f(p)=p\cdot s$ conjugates every holonomy by $s$; conversely $[\tilde x,g]\mapsto[\tilde x,ag]$ is an isomorphism $P_\rho\to P_{a\rho a^{-1}}$ of flat bundles.
   - *Why needed:* It makes $[(P,\omega)]\mapsto[\rho_\omega]$ well defined and injective, completing the bijection.

---

# Lemma Decomposition

> [!note]- Lemma 1: The flat bundle of a representation is a principal $G$-bundle
> **Statement:** For a homomorphism $\rho\colon\Gamma\to G$, the projection $\pi\colon P_\rho=\tilde M\times_\rho G\to M$, $[\tilde x,g]\mapsto q(\tilde x)$, is a principal $G$-bundle for the right action $[\tilde x,g]\cdot h=[\tilde x,gh]$.
>
> **Hint:** Use that $q\colon\tilde M\to M$ is a principal $\Gamma$-bundle: over an evenly covered $U$ a section of $q$ gives $q^{-1}(U)\cong U\times\Gamma$, and substituting collapses the $\Gamma$-quotient.
>
> **Why needed:** It is the object of part (a); a connection can only live on an actual bundle.
>
> > [!note]- Full proof
> > **Well-definedness of the projection and the action.** The map $\tilde M\times G\to M$, $(\tilde x,g)\mapsto q(\tilde x)$, is constant on equivalence classes: $q(\tilde x\cdot[\gamma])=q(\tilde x)$ because deck transformations cover the identity ($q\circ R_{[\gamma]}=q$ on $\tilde M$, from [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]]), so $\pi$ is well defined. The right $G$-action $(\tilde x,g)\cdot h=(\tilde x,gh)$ descends because it commutes with the relation: $(\tilde x\cdot[\gamma],g)\cdot h=(\tilde x\cdot[\gamma],gh)\sim(\tilde x,\rho([\gamma])gh)=(\tilde x,\rho([\gamma])g)\cdot h$ (since left multiplication by $\rho([\gamma])$ and right multiplication by $h$ on $G$ commute). Hence $[\tilde x,g]\cdot h:=[\tilde x,gh]$ is well defined.
> >
> > **The action is free and fibrewise transitive.** Fix $x\in M$ and $\tilde x\in q^{-1}(x)$. Every point of $\pi^{-1}(x)$ has a representative $(\tilde x,g)$ with this same first coordinate: given $[\tilde y,g']$ with $q(\tilde y)=x=q(\tilde x)$, transitivity of $\Gamma$ on the fibre $q^{-1}(x)$ gives $[\gamma]$ with $\tilde y\cdot[\gamma]=\tilde x$, so $[\tilde y,g']=[\tilde y\cdot[\gamma],\rho([\gamma])^{-1}g']=[\tilde x,\rho([\gamma])^{-1}g']$. Two such representatives $(\tilde x,g_1)$ and $(\tilde x,g_2)$ are equivalent only if $g_1=g_2$: if $(\tilde x,g_1)\sim(\tilde x,g_2)$ then $(\tilde x,g_1)=(\tilde x\cdot[\gamma],\ \cdot\,)$ forces $\tilde x=\tilde x\cdot[\gamma]$, hence $[\gamma]=e$ by freeness of the deck action, hence $g_1=g_2$. Thus $\pi^{-1}(x)=\{[\tilde x,g]:g\in G\}$ with $[\tilde x,g_1]=[\tilde x,g_2]\iff g_1=g_2$, and $[\tilde x,g]\cdot h=[\tilde x,gh]$ acts freely and transitively on it.
> >
> > **Local triviality.** Let $U\subseteq M$ be an open, path-connected, evenly covered set (these exist and cover $M$ because $q$ is a covering map). Choose a lift, that is, a continuous section $\sigma\colon U\to\tilde M$ of $q$; then $\{\sigma(U)\cdot[\gamma]\}_{[\gamma]\in\Gamma}$ are the sheets of $q^{-1}(U)$ and the map $U\times\Gamma\to q^{-1}(U)$, $(x,[\gamma])\mapsto\sigma(x)\cdot[\gamma]$, is a diffeomorphism (the trivialisation of the principal $\Gamma$-bundle $q$ over $U$). Define
> > $$\Psi_U\colon U\times G\to\pi^{-1}(U),\qquad \Psi_U(x,g):=[\sigma(x),g].$$
> > This is smooth, $G$-equivariant ($\Psi_U(x,gh)=[\sigma(x),gh]=[\sigma(x),g]\cdot h$), and covers $\operatorname{id}_U$. It is a bijection: injectivity holds because $[\sigma(x),g]=[\sigma(x'),g']$ forces $q(\sigma(x))=q(\sigma(x'))$, that is $x=x'$, and then $g=g'$ by the previous paragraph; surjectivity holds because any $[\tilde y,g']\in\pi^{-1}(U)$ has $\tilde y=\sigma(x)\cdot[\gamma]$ for a unique $(x,[\gamma])$, whence $[\tilde y,g']=[\sigma(x),\rho([\gamma])g']=\Psi_U(x,\rho([\gamma])g')$. Its inverse is smooth because in the chart $U\times\Gamma$ for $q^{-1}(U)$ it reads $[\sigma(x)\cdot[\gamma],g']\mapsto(x,\rho([\gamma])g')$, smooth in each sheet. On overlaps $U\cap U'$ the transition $\Psi_{U'}^{-1}\circ\Psi_U(x,g)=(x,\rho([\gamma_{U'U}(x)])\,g)$ is left multiplication by an element of $G$ depending only on which sheet $\sigma_U(x)$ sits in relative to $\sigma_{U'}$, hence is a smooth $G$-valued transition function. Therefore $P_\rho$ is a smooth principal $G$-bundle over $M$. $\blacksquare$

> [!note]- Lemma 2: The product connection descends to a flat connection $\omega_\rho$
> **Statement:** Let $\omega_0=\operatorname{pr}_G^\ast\theta\in\Omega^1(\tilde M\times G;\mathfrak g)$ be the product connection on the trivial principal $G$-bundle $\tilde M\times G\to\tilde M$, where $\theta$ is the left Maurer–Cartan form of $G$ and $\operatorname{pr}_G$ the projection to $G$; its horizontal distribution is $H_0=T\tilde M\oplus 0$. Then $\omega_0$ is invariant under the diagonal $\Gamma$-action defining $P_\rho$, and hence descends to a connection $\omega_\rho$ on $P_\rho$, which is flat. Its horizontal curves are precisely the images under $\tilde M\times G\to P_\rho$ of curves $t\mapsto(\tilde c(t),g)$ with $g\in G$ constant.
>
> **Hint:** The $\Gamma$-action multiplies the $G$-factor on the left by $\rho([\gamma])$; left-invariance of $\theta$ gives invariance of $\omega_0$. Flatness is local, and locally $\omega_\rho$ is the product connection.
>
> **Why needed:** It is the canonical flat connection of part (a).
>
> > [!note]- Full proof
> > **The relation as a group action.** Rewrite the defining relation of $P_\rho$ as the free left $\Gamma$-action on $\tilde M\times G$
> > $$[\gamma]\cdot(\tilde x,g):=(\tilde x\cdot[\gamma]^{-1},\ \rho([\gamma])\,g),$$
> > whose orbits are exactly the equivalence classes $[\tilde x,g]$ (indeed $(\tilde x\cdot[\gamma],g)$ and $(\tilde x,\rho([\gamma])g)$ lie in one orbit: apply $[\gamma]$ to $(\tilde x\cdot[\gamma],g)$ to get $(\tilde x,\rho([\gamma])g)$). This is a left action: $[\gamma_1]\cdot([\gamma_2]\cdot(\tilde x,g))=(\tilde x\cdot[\gamma_2]^{-1}[\gamma_1]^{-1},\rho([\gamma_1])\rho([\gamma_2])g)=([\gamma_1][\gamma_2])\cdot(\tilde x,g)$, using that $\rho$ is a homomorphism. Denote by $L_{[\gamma]}\colon\tilde M\times G\to\tilde M\times G$ this diffeomorphism.
> >
> > **Invariance of $\omega_0$.** On the $G$-factor, $L_{[\gamma]}$ acts by left translation $L_{\rho([\gamma])}$, and on the $\tilde M$-factor by the deck diffeomorphism $R_{[\gamma]^{-1}}$; that is, $\operatorname{pr}_G\circ L_{[\gamma]}=L_{\rho([\gamma])}\circ\operatorname{pr}_G$. Since the left Maurer–Cartan form is left-invariant, $L_a^\ast\theta=\theta$ for all $a\in G$, we compute
> > $$L_{[\gamma]}^\ast\omega_0=L_{[\gamma]}^\ast\operatorname{pr}_G^\ast\theta=(\operatorname{pr}_G\circ L_{[\gamma]})^\ast\theta=(L_{\rho([\gamma])}\circ\operatorname{pr}_G)^\ast\theta=\operatorname{pr}_G^\ast\,L_{\rho([\gamma])}^\ast\theta=\operatorname{pr}_G^\ast\theta=\omega_0\qquad(\text{left-invariance of }\theta).$$
> > So $\omega_0$ is $\Gamma$-invariant. Equivalently, its horizontal distribution $H_0=T\tilde M\oplus 0=\ker\omega_0$ is $\Gamma$-invariant: $d L_{[\gamma]}(v,0)=(dR_{[\gamma]^{-1}}v,\,0)\in H_0$ for $v\in T\tilde M$.
> >
> > **Descent to a connection.** The quotient map $\varpi\colon\tilde M\times G\to P_\rho$ is a covering map for the free, properly discontinuous $\Gamma$-action (properly discontinuous because the $\Gamma$-action on the $\tilde M$-factor is), and it intertwines the right $G$-actions ($\varpi((\tilde x,g)\cdot h)=\varpi(\tilde x,gh)=[\tilde x,g]\cdot h$). Because $\Gamma$ acts by principal-bundle automorphisms of $\tilde M\times G\to\tilde M$ that preserve $\omega_0$ and commute with the right $G$-action, the distribution $H_0$ pushes forward to a well-defined $G$-invariant horizontal distribution $H_\rho:=d\varpi(H_0)$ on $P_\rho$: at a point $[\tilde x,g]$ any two preimages differ by some $L_{[\gamma]}$, under which $H_0$ is invariant, so $d\varpi(H_0)$ is independent of the preimage. As $\varpi$ is a local diffeomorphism and $H_0$ is a $G$-invariant complement to the vertical bundle of $\tilde M\times G$, $H_\rho$ is a $G$-invariant complement to the vertical bundle of $P_\rho$, that is, a connection. Its connection one-form is the descent $\omega_\rho$ with $\varpi^\ast\omega_\rho=\omega_0$.
> >
> > **Flatness.** Curvature is local and $\varpi$ is a local diffeomorphism carrying $\omega_\rho$ to $\omega_0$, so $\varpi^\ast\Omega_{\omega_\rho}=\Omega_{\omega_0}$. The product connection $\omega_0=\operatorname{pr}_G^\ast\theta$ has curvature $\Omega_{\omega_0}=d\omega_0+\tfrac12[\omega_0\wedge\omega_0]=\operatorname{pr}_G^\ast\big(d\theta+\tfrac12[\theta\wedge\theta]\big)=0$ by the Maurer–Cartan equation $d\theta+\tfrac12[\theta\wedge\theta]=0$. Hence $\varpi^\ast\Omega_{\omega_\rho}=0$, and since $\varpi$ is a surjective local diffeomorphism, $\Omega_{\omega_\rho}=0$: $\omega_\rho$ is flat. (Alternatively, in the trivialisation $\Psi_U$ of Lemma 1 the section $x\mapsto[\sigma(x),e]$ has $\Psi_U$-connection form $A=0$ because it maps into the horizontal image of $\sigma(U)\times\{e\}$, so $F=dA+\tfrac12[A\wedge A]=0$ on $U$; this also proves $\omega_\rho$ is the product connection in each such chart, in accordance with [[Thm - Local Triviality of Flat Connections|the local-triviality theorem]].)
> >
> > **Horizontal curves.** A curve in $P_\rho$ is $\omega_\rho$-horizontal if and only if its velocity lies in $H_\rho=d\varpi(H_0)$ at each time; since $\varpi$ is a local diffeomorphism, this holds if and only if the curve locally lifts through $\varpi$ to an $\omega_0$-horizontal curve, and the $\omega_0$-horizontal curves are exactly $t\mapsto(\tilde c(t),g)$ with $g$ constant (velocity $(\dot{\tilde c}(t),0)\in H_0$). $\blacksquare$

> [!note]- Lemma 3: The monodromy of $\omega_\rho$ at the base point is $\rho$
> **Statement:** For the connection $\omega_\rho$ of Lemma 2 and the base point $p_0=[\tilde m,e]\in(P_\rho)_m$, every loop $c_{[\gamma]}$ at $m$ with homotopy class $[\gamma]\in\Gamma$ satisfies $\operatorname{hol}_{p_0}(c_{[\gamma]})=\rho([\gamma])$. Consequently the monodromy representation of $\omega_\rho$ at $p_0$ is $\rho$.
>
> **Hint:** Lift $c_{[\gamma]}$ to $\tilde M$ starting at $\tilde m$; its endpoint is $\tilde m\cdot[\gamma]$. The horizontal lift in $P_\rho$ is the image of the sheet-curve, whose endpoint you rewrite via the equivalence relation.
>
> **Why needed:** It certifies that part (a)'s construction realises the prescribed representation, hence surjectivity in part (d).
>
> > [!note]- Full proof
> > **Set-up.** Let $c:=c_{[\gamma]}\colon[0,1]\to M$ be a piecewise smooth loop at $m$ with $[c]=[\gamma]$. By path lifting for the covering $q$, there is a unique lift $\tilde c\colon[0,1]\to\tilde M$ with $q\circ\tilde c=c$ and $\tilde c(0)=\tilde m$; by the deck-action convention (from [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]]), $\tilde c(1)=\tilde m\cdot[\gamma]$.
> >
> > **The horizontal lift in $P_\rho$.** Consider the curve $\hat c(t):=[\tilde c(t),e]\in P_\rho$. It projects correctly, $\pi(\hat c(t))=q(\tilde c(t))=c(t)$, starts at $\hat c(0)=[\tilde m,e]=p_0$, and is $\omega_\rho$-horizontal by Lemma 2, being the image of the sheet-curve $t\mapsto(\tilde c(t),e)$ with constant $G$-coordinate. By uniqueness of horizontal lifts (from [[Thm - Existence and Uniqueness of Horizontal Lifts|the existence-and-uniqueness theorem]]), $\hat c$ is the horizontal lift of $c$ through $p_0$, so $\Gamma_c(p_0)=\hat c(1)=[\tilde c(1),e]=[\tilde m\cdot[\gamma],\,e]$.
> >
> > **Reading off the holonomy.** Apply the defining relation of $P_\rho$ with $\tilde x=\tilde m$ and $g=e$: $(\tilde m\cdot[\gamma],\,e)\sim(\tilde m,\,\rho([\gamma])\,e)=(\tilde m,\rho([\gamma]))$, so
> > $$\Gamma_c(p_0)=[\tilde m\cdot[\gamma],e]=[\tilde m,\rho([\gamma])]=[\tilde m,e]\cdot\rho([\gamma])=p_0\cdot\rho([\gamma])\qquad(\text{relation, then definition of the right }G\text{-action}).$$
> > By the definition $\Gamma_c(p_0)=p_0\cdot\operatorname{hol}_{p_0}(c)$ and freeness of the $G$-action on the fibre, $\operatorname{hol}_{p_0}(c)=\rho([\gamma])$.
> >
> > **Conclusion.** The value depends only on $[\gamma]$, as it must: $\omega_\rho$ is flat, so by [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|homotopy invariance]] the map $[\gamma]\mapsto\operatorname{hol}_{p_0}(c_{[\gamma]})$ is a well-defined homomorphism $\Gamma\to G$, the monodromy representation of $\omega_\rho$ at $p_0$; we have just shown it equals $\rho$ on every class. Therefore the monodromy representation of $\omega_\rho$ is $\rho$. $\blacksquare$

> [!note]- Lemma 4: The developing map is a well-defined equivariant bundle map
> **Statement:** Let $\omega\in\mathcal A^\flat(P)$ be flat on a principal $G$-bundle $P\to M$, fix $p\in P_m$, and let $\rho_\omega\colon\Gamma\to G$ be its monodromy at $p$. The formula $\hat\Phi(\tilde x,g):=\Gamma_c(p)\cdot g$, where $c$ is the $q$-projection of any path in $\tilde M$ from $\tilde m$ to $\tilde x$, is a well-defined smooth map $\tilde M\times G\to P$ that is $G$-equivariant and satisfies $\hat\Phi(\tilde x\cdot[\gamma],g)=\hat\Phi(\tilde x,\rho_\omega([\gamma])\,g)$. Hence it descends to a smooth $G$-equivariant bundle map $\Phi\colon P_{\rho_\omega}\to P$ over $\operatorname{id}_M$, $\Phi[\tilde x,g]=\Gamma_c(p)\cdot g$.
>
> **Hint:** Independence of the path uses that $\tilde M$ is simply connected, so two paths with equal endpoints are homotopic rel endpoints, and their projections are too; then apply flat homotopy invariance. The twist $\rho_\omega$ comes from splitting a path to $\tilde x\cdot[\gamma]$ as a loop followed by a translate.
>
> **Why needed:** It is the reconstruction of part (b): it turns the monodromy back into the bundle.
>
> > [!note]- Full proof
> > **Independence of the path (well-definedness in $\tilde x$).** Let $\tilde c_0,\tilde c_1\colon[0,1]\to\tilde M$ be two piecewise smooth paths from $\tilde m$ to $\tilde x$. Because $\tilde M$ is simply connected, $\tilde c_0$ and $\tilde c_1$ are homotopic relative to their common endpoints, through a continuous homotopy $\tilde H\colon[0,1]^2\to\tilde M$. Composing with $q$ gives a homotopy $H=q\circ\tilde H$ relative to endpoints between the projections $c_0=q\circ\tilde c_0$ and $c_1=q\circ\tilde c_1$, which are piecewise smooth paths in $M$ from $m$ to $q(\tilde x)$. Since $\omega$ is flat, [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|the homotopy-invariance theorem]] — flat parallel transport along homotopic-rel-endpoints paths agrees — gives $\Gamma_{c_0}=\Gamma_{c_1}\colon P_m\to P_{q(\tilde x)}$, so $\Gamma_{c_0}(p)=\Gamma_{c_1}(p)$. Thus $\Gamma_c(p)$ depends only on $\tilde x$, and $\hat\Phi(\tilde x,g)=\Gamma_c(p)\cdot g$ is well defined. It is smooth because parallel transport of the fixed point $p$ depends smoothly on the endpoint (horizontal lifts depend smoothly on data, by [[Thm - Existence and Uniqueness of Horizontal Lifts|the existence-and-uniqueness theorem]]) and the right action is smooth.
> >
> > **$G$-equivariance.** For $h\in G$, $\hat\Phi(\tilde x,gh)=\Gamma_c(p)\cdot(gh)=(\Gamma_c(p)\cdot g)\cdot h=\hat\Phi(\tilde x,g)\cdot h$ (associativity of the right action).
> >
> > **The twist by $\rho_\omega$.** Fix $[\gamma]\in\Gamma$ and a path $\tilde c$ from $\tilde m$ to $\tilde x$; let $c=q\circ\tilde c$. Let $\tilde\ell$ be the lift from $\tilde m$ of a loop $\ell$ at $m$ representing $[\gamma]$, so $\tilde\ell(1)=\tilde m\cdot[\gamma]$, and let $(\tilde c)\!\cdot\![\gamma]$ denote the deck-translate of $\tilde c$, a path from $\tilde m\cdot[\gamma]$ to $\tilde x\cdot[\gamma]$. Their concatenation $\tilde\ell$-then-$(\tilde c)\!\cdot\![\gamma]$ is a path in $\tilde M$ from $\tilde m$ to $\tilde x\cdot[\gamma]$, with $q$-projection $\ell$-then-$c$ (because $q\circ((\tilde c)\!\cdot\![\gamma])=q\circ\tilde c=c$, deck transformations covering the identity). By the composition law of parallel transport (from [[Thm - Properties of Parallel Transport|the properties-of-parallel-transport theorem]]: $\Gamma_{c\ast\ell}=\Gamma_c\circ\Gamma_\ell$ for "$\ell$ first, then $c$") and its $G$-equivariance ($\Gamma_c\circ R_a=R_a\circ\Gamma_c$),
> > $$\hat\Phi(\tilde x\cdot[\gamma],g)=\Gamma_{c\ast\ell}(p)\cdot g=\Gamma_c\big(\Gamma_\ell(p)\big)\cdot g=\Gamma_c\big(p\cdot\operatorname{hol}_p(\ell)\big)\cdot g=\Gamma_c(p)\cdot\operatorname{hol}_p(\ell)\cdot g,$$
> > where the third equality is the definition of holonomy and the fourth is equivariance. Now $\operatorname{hol}_p(\ell)=\rho_\omega([\gamma])$ by definition of the monodromy representation, and the well-definedness just proved lets us use $c$ itself as a path to $\tilde x$ in evaluating $\hat\Phi(\tilde x,\cdot)$. Hence
> > $$\hat\Phi(\tilde x\cdot[\gamma],g)=\Gamma_c(p)\cdot\rho_\omega([\gamma])\,g=\hat\Phi(\tilde x,\rho_\omega([\gamma])\,g).$$
> >
> > **Descent.** The identity $\hat\Phi(\tilde x\cdot[\gamma],g)=\hat\Phi(\tilde x,\rho_\omega([\gamma])g)$ is exactly the statement that $\hat\Phi$ is constant on the equivalence classes defining $P_{\rho_\omega}$ (recall $(\tilde x\cdot[\gamma],g)\sim(\tilde x,\rho_\omega([\gamma])g)$). Therefore $\hat\Phi$ factors as $\Phi\circ\varpi$ for a unique map $\Phi\colon P_{\rho_\omega}\to P$, $\Phi[\tilde x,g]=\Gamma_c(p)\cdot g$, which is smooth (as $\varpi$ is a surjective local diffeomorphism and $\hat\Phi$ is smooth), $G$-equivariant (inherited from $\hat\Phi$), and covers $\operatorname{id}_M$ (both sides lie over $q(\tilde x)$). $\blacksquare$

> [!note]- Lemma 5: An equivariant bundle map over the identity is an isomorphism, and $\Phi$ carries $\omega_{\rho_\omega}$ to $\omega$
> **Statement:** Any smooth $G$-equivariant map $\Phi\colon P'\to P$ between principal $G$-bundles over $M$ covering $\operatorname{id}_M$ is a bundle isomorphism. Moreover the developing map $\Phi$ of Lemma 4 satisfies $\Phi^\ast\omega=\omega_{\rho_\omega}$.
>
> **Hint:** Fibrewise, equivariance plus freeness and transitivity forces a bijection; smoothness of the inverse is local. For the connections, $\Phi$ maps the sheet-curves (horizontal for $\omega_{\rho_\omega}$) to parallel transports (horizontal for $\omega$).
>
> **Why needed:** It upgrades part (b) to an isomorphism of bundles with connection, giving injectivity in part (d).
>
> > [!note]- Full proof
> > **Fibrewise bijectivity.** Fix $x\in M$ and $p'_0\in P'_x$. For any $p'\in P'_x$ there is a unique $h\in G$ with $p'=p'_0\cdot h$ (the $G$-action on the fibre is free and transitive), and then $\Phi(p')=\Phi(p'_0\cdot h)=\Phi(p'_0)\cdot h$. Since $g\mapsto\Phi(p'_0)\cdot g$ is a bijection $G\to P_x$ (freeness and transitivity in $P$) and $h\mapsto p'_0\cdot h$ is a bijection $G\to P'_x$, the restriction $\Phi\colon P'_x\to P_x$ is a bijection. As $x$ was arbitrary and $\Phi$ covers $\operatorname{id}_M$, $\Phi$ is a bijection $P'\to P$.
> >
> > **Smoothness of the inverse.** Over an open $U\subseteq M$ trivialising both bundles, choose $G$-equivariant trivialisations $P'|_U\cong U\times G\cong P|_U$; in these, equivariance forces $\Phi(x,h)=(x,\phi(x)\,h)$ for a smooth map $\phi\colon U\to G$ (namely $\phi(x)$ is the $G$-coordinate of $\Phi(x,e)$, smooth in $x$). Its inverse is $(x,h)\mapsto(x,\phi(x)^{-1}h)$, smooth because inversion and multiplication in $G$ are smooth. Hence $\Phi^{-1}$ is smooth and $\Phi$ is a diffeomorphism, so a principal-bundle isomorphism.
> >
> > **$\Phi$ carries the connections.** By Lemma 2 the $\omega_{\rho_\omega}$-horizontal lift of a path $c$ in $M$ through the point $[\tilde m,e]$ is $t\mapsto[\tilde c(t),e]$, where $\tilde c$ is the lift of $c$ to $\tilde M$ from $\tilde m$. Applying $\Phi$ and writing $c_t:=c|_{[0,t]}$ (whose lift to $\tilde M$ from $\tilde m$ is $\tilde c|_{[0,t]}$, ending at $\tilde c(t)$),
> > $$\Phi[\tilde c(t),e]=\Gamma_{c_t}(p),$$
> > which is by definition the $\omega$-horizontal lift of $c$ through $p=\Phi[\tilde m,e]$. Thus $\Phi$ maps the $\omega_{\rho_\omega}$-horizontal lift of $c$ to the $\omega$-horizontal lift of $c$; differentiating at each $t$, $d\Phi$ maps the velocity of the former (which spans, as $c$ and its initial point vary, the horizontal distribution $H^{\omega_{\rho_\omega}}$) into the horizontal distribution $H^{\omega}$. By $G$-equivariance the same holds after right translation, so $d\Phi(H^{\omega_{\rho_\omega}}_{p'})\subseteq H^{\omega}_{\Phi(p')}$ for every $p'$; both distributions have rank $\dim M$ and $d\Phi$ is an isomorphism, so equality holds: $d\Phi(H^{\omega_{\rho_\omega}})=H^\omega$. A principal-bundle isomorphism carrying horizontal distribution to horizontal distribution carries connection form to connection form, that is $\Phi^\ast\omega=\omega_{\rho_\omega}$. $\blacksquare$

> [!note]- Lemma 6: Gauge equivalence corresponds to conjugation, in both directions
> **Statement:** (i) If $\omega,\omega'\in\mathcal A^\flat(P)$ satisfy $\omega'=f^\ast\omega$ for some $f\in\mathcal G(P)$, then $\rho_{\omega'}=s^{-1}\rho_\omega(\cdot)\,s$ where $s\in G$ is determined by $f(p)=p\cdot s$. (ii) If $\rho'=a\rho(\cdot)a^{-1}$ for some $a\in G$, then $\Theta_a\colon P_\rho\to P_{\rho'}$, $[\tilde x,g]\mapsto[\tilde x,ag]$, is an isomorphism of principal $G$-bundles over $\operatorname{id}_M$ carrying $\omega_\rho$ to $\omega_{\rho'}$.
>
> **Hint:** For (i), $f$ maps $\omega'$-horizontal vectors to $\omega$-horizontal vectors, so $\Gamma^{\omega'}_c=f^{-1}\circ\Gamma^\omega_c\circ f$; evaluate at $p$ using $f(p)=p\cdot s$. For (ii), check $\Theta_a$ is well defined against the relation, and that it sends sheet-curves to sheet-curves.
>
> **Why needed:** Part (i) is Haydys' Exercise 104; together (i) and (ii) make $[(P,\omega)]\mapsto[\rho_\omega]$ well defined and injective.
>
> > [!note]- Full proof
> > **(i) Gauge equivalent $\Rightarrow$ conjugate.** Let $f\in\mathcal G(P)$ with $\omega'=f^\ast\omega$. Because $f^\ast\omega=\omega'$, the diffeomorphism $f$ maps $\ker\omega'=H^{\omega'}$ onto $\ker\omega=H^{\omega}$; and $f$ covers $\operatorname{id}_M$, so $q_P\circ f=q_P$. Hence if $\tilde c$ is an $\omega'$-horizontal lift of a path $c$, then $f\circ\tilde c$ is an $\omega$-horizontal lift of $c$; comparing endpoints,
> > $$\Gamma^{\omega}_c\big(f(p')\big)=f\big(\Gamma^{\omega'}_c(p')\big)\quad\text{for all }p'\in P_{c(0)},\qquad\text{i.e.}\qquad \Gamma^{\omega'}_c=f^{-1}\circ\Gamma^{\omega}_c\circ f.$$
> > Write $f(p)=p\cdot s$ with $s:=\hat f(p)\in G$ (using that $f\in\mathcal G(P)$ acts on the fibre $P_m$ by a group element); by right-equivariance of $f$, $f^{-1}(p)=p\cdot s^{-1}$. For a loop $c$ at $m$,
> > $$\Gamma^{\omega'}_c(p)=f^{-1}\Big(\Gamma^{\omega}_c\big(p\cdot s\big)\Big)=f^{-1}\Big(\Gamma^{\omega}_c(p)\cdot s\Big)=f^{-1}\Big(p\cdot\operatorname{hol}^{\omega}_p(c)\,s\Big)=p\cdot s^{-1}\operatorname{hol}^{\omega}_p(c)\,s,$$
> > using in turn $f(p)=p\cdot s$, equivariance of $\Gamma^\omega_c$, the definition of holonomy, and right-equivariance of $f^{-1}$ (which sends $p\cdot k\mapsto f^{-1}(p)\cdot k=p\cdot s^{-1}k$). Comparing with $\Gamma^{\omega'}_c(p)=p\cdot\operatorname{hol}^{\omega'}_p(c)$ and cancelling the free action, $\operatorname{hol}^{\omega'}_p(c)=s^{-1}\operatorname{hol}^{\omega}_p(c)\,s$, i.e. $\rho_{\omega'}=s^{-1}\rho_\omega(\cdot)\,s$.
> >
> > **(ii) Conjugate $\Rightarrow$ isomorphic flat bundles.** Suppose $\rho'=a\rho(\cdot)a^{-1}$. The map $\Theta_a[\tilde x,g]:=[\tilde x,ag]$ is well defined: for the $\rho$-relation representatives,
> > $$\Theta_a[\tilde x\cdot[\gamma],g]=[\tilde x\cdot[\gamma],ag]_{\rho'}=[\tilde x,\rho'([\gamma])ag]_{\rho'}=[\tilde x,a\rho([\gamma])a^{-1}ag]_{\rho'}=[\tilde x,a\rho([\gamma])g]_{\rho'},$$
> > while $\Theta_a[\tilde x,\rho([\gamma])g]=[\tilde x,a\rho([\gamma])g]_{\rho'}$; the two agree, so $\Theta_a$ respects the relation and is well defined, where the subscript records which bundle a class lives in. It covers $\operatorname{id}_M$ and is $G$-equivariant: $\Theta_a([\tilde x,g]\cdot h)=\Theta_a[\tilde x,gh]=[\tilde x,agh]=[\tilde x,ag]\cdot h=\Theta_a[\tilde x,g]\cdot h$. By Lemma 5 it is therefore a bundle isomorphism. It carries connections: the $\omega_\rho$-horizontal curves are the images of sheet-curves $t\mapsto[\tilde c(t),g]$ (Lemma 2), and $\Theta_a[\tilde c(t),g]=[\tilde c(t),ag]$ is again a sheet-curve, hence $\omega_{\rho'}$-horizontal; so $\Theta_a$ maps horizontal to horizontal and $\Theta_a^\ast\omega_{\rho'}=\omega_\rho$. In particular $(P_{\rho'},\omega_{\rho'})\cong(P_\rho,\omega_\rho)$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the four parts in turn, then assemble the bijection and record the specialisations. Throughout, $\varpi\colon\tilde M\times G\to P_\rho$ denotes the quotient projection, $\theta$ the left Maurer–Cartan form of $G$, and $p_0=[\tilde m,e]$.
>
> **Step 0 — the standing objects exist.** By [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|the universal-cover theorem]], the universal cover $q\colon\tilde M\to M$ exists, is a smooth principal $\Gamma$-bundle with $\Gamma=\pi_1(M,m)$ discrete acting on the right, with the lift of a loop of class $[\gamma]$ from $\tilde m$ ending at $\tilde m\cdot[\gamma]$; and $\Gamma$ is countable. For a flat $\omega$ its monodromy $\rho_\omega\colon\Gamma\to G$ is a well-defined homomorphism by [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|the homotopy-invariance theorem]]. These are the inputs used below.
>
> **Part (a).** Let $\rho\colon\Gamma\to G$ be a homomorphism. By **Lemma 1**, $P_\rho=\tilde M\times_\rho G$ is a principal $G$-bundle over $M$. By **Lemma 2**, the product connection $\omega_0=\operatorname{pr}_G^\ast\theta$ on $\tilde M\times G$ is $\Gamma$-invariant and descends to a flat connection $\omega_\rho$ on $P_\rho$, whose horizontal curves are the images of constant-$G$ curves. By **Lemma 3**, the monodromy of $\omega_\rho$ at $p_0$ equals $\rho$.
>
> For the vector-bundle formulation, let $\varrho\colon G\to GL(V)$ be a finite-dimensional [[Def - Representation of a Lie Group|representation]] and form $E:=\tilde M\times_{\varrho\circ\rho}V=P_\rho\times_\varrho V$. By [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|the theorem that principal connections induce covariant derivatives on associated bundles]], $\omega_\rho$ induces a covariant derivative $\nabla$ on $E$; a section $s\in\Gamma(E)$ corresponds to a $\Gamma$-equivariant map $\hat s\colon\tilde M\to V$ with $\hat s(\tilde x\cdot[\gamma])=(\varrho\circ\rho)([\gamma])^{-1}\hat s(\tilde x)$. In the flat local gauge over an evenly covered $U$ furnished by the section $x\mapsto[\sigma(x),e]$ of Lemma 2, the connection matrix of $\omega_\rho$ is $A=0$, so the induced covariant derivative reads $\nabla s=d\hat s$ in the pulled-back trivialisation, i.e. $\pi^\ast\nabla s=d\hat s$ on $\tilde M$ (Haydys' formula (47) specialised to $a=0$). This is the induced flat covariant derivative, proving the vector-bundle clause.
>
> **Part (b).** Let $\omega\in\mathcal A^\flat(P)$, fix $p\in P_m$, and let $\rho_\omega$ be its monodromy at $p$. By **Lemma 4**, the developing map $\Phi\colon P_{\rho_\omega}\to P$, $\Phi[\tilde x,g]=\Gamma_c(p)\cdot g$, is a well-defined smooth $G$-equivariant bundle map over $\operatorname{id}_M$. By **Lemma 5**, $\Phi$ is a principal-bundle isomorphism and $\Phi^\ast\omega=\omega_{\rho_\omega}$. Hence $(P_{\rho_\omega},\omega_{\rho_\omega})\cong(P,\omega)$ as bundles with connection, which is the claim.
>
> **Part (c).** Both directions are **Lemma 6**: (i) if $\omega'=f^\ast\omega$ with $f\in\mathcal G(P)$ then $\rho_{\omega'}=s^{-1}\rho_\omega(\cdot)s$ with $f(p)=p\cdot s$, so $[\rho_{\omega'}]=[\rho_\omega]$; and (ii) if $\rho'=a\rho(\cdot)a^{-1}$ then $(P_{\rho'},\omega_{\rho'})\cong(P_\rho,\omega_\rho)$ via $\Theta_a$.
>
> **Part (d) — the bijection.** Define $\Xi\colon\mathcal M^\flat_G(M)\to\mathcal R(M;G)$ by $\Xi[(P,\omega)]=[\rho_\omega]$, where $\rho_\omega$ is the monodromy at any chosen $p\in P_m$.
>
> *Well-defined.* First, changing the base frame from $p$ to $p\cdot s$ conjugates the monodromy by $s$: for a loop $c$, $\Gamma_c(p\cdot s)=\Gamma_c(p)\cdot s=p\cdot\operatorname{hol}_p(c)\,s=(p\cdot s)\cdot(s^{-1}\operatorname{hol}_p(c)\,s)$, so $\operatorname{hol}_{p\cdot s}(c)=s^{-1}\operatorname{hol}_p(c)\,s$; thus $[\rho_\omega]\in\mathcal R(M;G)$ is independent of the frame. Second, if $(P,\omega)\cong(P',\omega')$ via an isomorphism $\psi\colon P\to P'$ over $\operatorname{id}_M$ with $\psi^\ast\omega'=\omega$, then $\psi$ carries $\omega$-horizontal lifts to $\omega'$-horizontal lifts (as $\psi_\ast H^\omega=H^{\omega'}$), so for $p\in P_m$ and a loop $c$, $\Gamma^{\omega'}_c(\psi(p))=\psi(\Gamma^\omega_c(p))=\psi(p\cdot\operatorname{hol}^\omega_p(c))=\psi(p)\cdot\operatorname{hol}^\omega_p(c)$; hence $\rho_{\omega'}$ at $\psi(p)$ equals $\rho_\omega$ at $p$, so $[\rho_{\omega'}]=[\rho_\omega]$. Combining with part (c)(i) for the case $P=P'$, $\Xi$ depends only on the isomorphism class $[(P,\omega)]$.
>
> *Surjective.* Given $[\rho]\in\mathcal R(M;G)$, part (a) produces $(P_\rho,\omega_\rho)$ with monodromy $\rho$ at $p_0$, so $\Xi[(P_\rho,\omega_\rho)]=[\rho]$.
>
> *Injective.* Suppose $\Xi[(P,\omega)]=\Xi[(P',\omega')]$, that is $[\rho_\omega]=[\rho_{\omega'}]$, so $\rho_{\omega'}=a\rho_\omega(\cdot)a^{-1}$ for some $a\in G$. By part (b), $(P,\omega)\cong(P_{\rho_\omega},\omega_{\rho_\omega})$ and $(P',\omega')\cong(P_{\rho_{\omega'}},\omega_{\rho_{\omega'}})$. By part (c)(ii), $(P_{\rho_{\omega'}},\omega_{\rho_{\omega'}})=(P_{a\rho_\omega a^{-1}},\omega_{a\rho_\omega a^{-1}})\cong(P_{\rho_\omega},\omega_{\rho_\omega})$. Chaining the three isomorphisms, $(P,\omega)\cong(P',\omega')$, so $[(P,\omega)]=[(P',\omega')]$. Hence $\Xi$ is injective, and therefore a bijection.
>
> **The fixed-bundle statement.** Fix a principal $G$-bundle $P$. An isomorphism $(P,\omega)\to(P,\omega')$ over $\operatorname{id}_M$ is by definition a $G$-equivariant diffeomorphism of $P$ covering $\operatorname{id}_M$ carrying $\omega$ to $\omega'$, that is, precisely an element $f\in\mathcal G(P)$ with $f^\ast\omega=\omega'$; so the isomorphism classes of flat connections *supported on the fixed $P$* are exactly the gauge orbits, and $\mathcal M^\flat(P)=\mathcal A^\flat(P)/\mathcal G(P)$ embeds into $\mathcal M^\flat_G(M)$ as the classes $[(P,\omega)]$ with underlying bundle $P$. Under $\Xi$ these map to those $[\rho]$ with $P_\rho\cong P$: indeed $\Xi[(P,\omega)]=[\rho_\omega]$ and $P\cong P_{\rho_\omega}$ by part (b); conversely if $P_\rho\cong P$ then $[\rho]=\Xi[(P_\rho,\omega_\rho)]$ arises from a flat connection on (a bundle isomorphic to) $P$. Thus $\mathcal M^\flat(P)$ is carried bijectively onto $\{[\rho]\in\mathcal R(M;G):P_\rho\cong P\}$.
>
> **The $GL_k(\mathbb R)$ (vector-bundle) specialisation.** Take $G=GL_k(\mathbb R)$. A rank-$k$ real vector bundle $E\to M$ has [[Def - Frame Bundle of a Vector Bundle|frame bundle]] $\operatorname{Fr}(E)$, a principal $GL_k(\mathbb R)$-bundle with $E=\operatorname{Fr}(E)\times_{GL_k(\mathbb R)}\mathbb R^k$; a connection $\nabla$ on $E$ corresponds to a principal connection $\omega$ on $\operatorname{Fr}(E)$, flat if and only if $\nabla$ is flat, and the two have the same monodromy $\rho_\nabla=\rho_\omega\colon\Gamma\to GL_k(\mathbb R)$. Applying the bijection $\Xi$ with $P$ ranging over all $\operatorname{Fr}(E)$, that is over all rank-$k$ bundles at once, gives the correspondence between flat rank-$k$ real vector bundles up to isomorphism and $\mathcal R(M;GL_k(\mathbb R))$, which is Haydys' Theorem of §3.3 (unlabelled, p. 34). In this language part (a)'s $\pi^\ast\nabla s=d\hat s$ is the standard description of the flat bundle $\tilde M\times_\rho\mathbb R^k$ of a representation.
>
> This establishes all clauses. $\blacksquare$

> [!note]- Corollary proof: the $O(k),U(k),SO(k),SU(k)$ variants
> Let $G$ be any of $O(k),U(k),SO(k),SU(k)$, viewed as a closed subgroup of $GL_k(\mathbb C)$ (or $GL_k(\mathbb R)$). The theorem was proved for an arbitrary Lie group $G$, so it holds verbatim for these, giving $\mathcal M^\flat_G(M)\cong\mathcal R(M;G)$. For the vector-bundle reading: a metric connection on a Euclidean bundle has orthogonal parallel transport, and a Hermitian connection on a complex bundle has unitary parallel transport (by [[Thm - Properties of Parallel Transport|the properties-of-parallel-transport theorem]], clause (6), because parallel transport preserves the fibre inner product), so its monodromy lands in $O(k)$ respectively $U(k)$; imposing in addition an orientation or a trivialised determinant restricts to $SO(k)$ respectively $SU(k)$. These are the cases of the general theorem for the corresponding structure group, as recorded in Haydys' Remark 105. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemann–Hilbert and Fuchsian systems (complex analysis / differential equations).** On a punctured Riemann surface $X=\overline X\setminus\{x_1,\dots,x_n\}$, a Fuchsian linear system $\tfrac{d}{dz}Y=\big(\sum_j\tfrac{B_j}{z-x_j}\big)Y$ defines a flat connection $\nabla=d-\sum_j\tfrac{B_j}{z-x_j}dz$ on the trivial rank-$k$ bundle, and analytic continuation of a fundamental solution around a loop is parallel transport. The theorem identifies the system, up to gauge, with its monodromy $[\rho]\in\mathcal R(X;GL_k(\mathbb C))$; the Riemann–Hilbert problem asks for the reverse construction, which is exactly part (a) made analytic. The application is non-obvious because the "connection" is hidden inside an ordinary differential equation and the fundamental group of a punctured surface must be recognised as the source of the monodromy.

**Character varieties and $2+1$ topological field theory (low-dimensional topology).** For a closed oriented surface $\Sigma_\gamma$ and a compact $G$, the theorem turns the analytic space $\mathcal A^\flat(P)/\mathcal G(P)$ into the character variety $\{(A_i,B_i):\prod_i[A_i,B_i]=e\}/G$. This is the phase space of Chern–Simons theory on $\Sigma_\gamma\times\mathbb R$ and carries the Atiyah–Bott–Goldman symplectic form; quantising it produces the Witten–Reshetikhin–Turaev invariants. The theorem is what licenses replacing an infinite-dimensional symplectic quotient by a finite-dimensional algebraic one — non-obvious because the symplectic structure is defined on the connection side but computed on the representation side.

**Bloch electrons and the Aharonov–Bohm effect (mathematical physics).** A charged quantum particle on a manifold with a flat $U(1)$-connection (a magnetic potential with zero field strength, as outside an idealised solenoid) has holonomy $e^{-i\oint A}$ around a loop, an observable phase depending only on the loop's homotopy class. The theorem says the physics is completely encoded by $[\rho]\in\mathcal R(M;U(1))=\operatorname{Hom}(\pi_1(M),U(1))$. For $M=\mathbb R^2\setminus\{0\}$ this is the Aharonov–Bohm phase; the application is non-obvious because a vanishing field can still produce a measurable effect, and the theorem explains why: the effect is the monodromy, not the curvature.

---

# Bridges

- **From the local to the global picture of flatness.** [[Thm - Local Triviality of Flat Connections|Local triviality]] says a flat connection is *locally* the product connection, with locally constant transition functions $g_{\alpha\beta}$. The present theorem is the global upgrade: assembling the locally constant cocycle over the universal cover produces a single global datum, the monodromy $\rho\colon\pi_1(M,m)\to G$. Concretely, the locally constant transition functions descend from the constant "jumps" $\rho([\gamma])$ across the deck transformations of $\tilde M$, so the theorem exhibits $\rho$ as the total holonomy of the flat cocycle.

- **From holonomy to representation.** [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|Homotopy invariance of flat holonomy]] provides the map $[\gamma]\mapsto\operatorname{hol}_p(\ell_\gamma)$ and shows it is a homomorphism; this theorem shows the homomorphism determines everything, by reconstructing the bundle-with-connection through the developing map. The bridge is the developing map $\Phi[\tilde x,g]=\Gamma_c(p)\cdot g$: it is the concrete inverse to "take the monodromy", built by transporting one frame out to every homotopy class of paths, and it is well defined precisely because $\tilde M$ has no loops.

- **From the universal cover to the flat bundle.** [[Thm - Existence of the Universal Cover and the Deck Action of the Fundamental Group|The universal-cover theorem]] presents $\tilde M$ as a principal $\pi_1(M,m)$-bundle for the discrete group. Extending its structure group along $\rho$ ([[Def - Reduction and Extension of the Structure Group|extension of the structure group]]) produces $P_\rho=\tilde M\times_\rho G$; this theorem endows the extension with its canonical flat connection and identifies its monodromy. The bridge is that "extension of a discrete-group principal bundle along a representation" is exactly the associated-bundle construction $\tilde M\times_\rho G$, so the machinery of associated bundles from chapter III is what turns a homomorphism into a bundle.

- **From flat moduli to the representation variety as a moduli space.** The bijection $\mathcal M^\flat_G(M)\cong\mathcal R(M;G)$ turns the analytic quotient $\mathcal A^\flat(P)/\mathcal G(P)$ into an algebraic object. This is the bridge to [[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact|the compactness theorem]], which then proves $\mathcal R(M;G)$ compact for compact $G$ by a purely algebraic argument on $\operatorname{Hom}(\pi_1,G)\subseteq G^N$, and to the Chern–Simons story of chapter VI, where flat connections reappear as the critical points of $\vartheta$ and the representation variety is the critical set.

---

# Unlocked by This

> [!tip] Compactness of the flat moduli space *(from Gauge Theory)*
> With this bijection in hand, the compactness of $\mathcal M^\flat_G(M)$ for compact $G$ becomes a statement about $\operatorname{Hom}(\pi_1(M),G)\subseteq G^N$ modulo conjugation, proved without analysis. See **Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact**.

> [!tip] Flat $U(1)$-bundles and the first cohomology *(from Algebraic Topology)*
> For $G=U(1)$ the correspondence reads $\mathcal M^\flat_{U(1)}(M)=\operatorname{Hom}(\pi_1(M),U(1))=\operatorname{Hom}(H_1(M;\mathbb Z),U(1))$, since $U(1)$ is abelian and factors through the abelianisation $H_1$. This identifies flat line bundles with a group built from $H^1(M;U(1))$, the beginning of the Hodge-theoretic description of the Jacobian for surfaces.

> [!tip] Chern–Simons critical points *(from Gauge Theory)*
> On a three-manifold, the critical points of the Chern–Simons functional are the flat connections, so their gauge-equivalence classes are $\mathcal R(Y;SU(2))$; enumerating them is the algebraic input to the Casson invariant and to instanton Floer homology. See **Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional**.
