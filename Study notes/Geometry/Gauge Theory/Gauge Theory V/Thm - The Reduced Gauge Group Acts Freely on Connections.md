---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Gauge Transformation"
  - "Thm - Gauge Transformations Act on Connections and Curvature"
  - "Thm - Existence and Uniqueness of Horizontal Lifts"
  - "Def - Holonomy Group of a Connection"
  - "Thm - Properties of Parallel Transport"
  - "Def - Connection on a Principal Bundle"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a Lie group, $\pi\colon P\to M$ is a smooth [[Def - Principal G-Bundle|principal $G$-bundle]] over a connected base manifold $M$, and $G$ acts on $P$ on the **right**, $R_g(p)=p\cdot g$, freely and transitively on each fibre $P_x=\pi^{-1}(x)$. A point $b\in M$ is fixed once and for all as the base point. We write $\mathfrak{g}=T_eG$ for the Lie algebra and, for $\xi\in\mathfrak{g}$, $\xi_P(p)=\frac{d}{dt}\big|_{t=0}\,p\cdot\exp(t\xi)$ for the fundamental vector field; the vertical subspace at $p$ is $V_p=\ker d\pi_p=\{\xi_P(p):\xi\in\mathfrak{g}\}$.

A [[Def - Connection on a Principal Bundle|connection on the principal bundle]] is a $\mathfrak{g}$-valued one-form $\omega\in\Omega^1(P;\mathfrak{g})$ with $\omega(\xi_P)=\xi$ and $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$; equivalently it is the $G$-invariant horizontal distribution $H=\ker\omega$, so that $T_pP=H_p\oplus V_p$ and $\dim H_p=\dim M$ at every $p$. We write $\mathcal{A}(P)$ for the set of all connections on $P$.

A [[Def - Gauge Transformation|gauge transformation]] is an automorphism $f\colon P\to P$ of the principal bundle — a diffeomorphism with $f(p\cdot g)=f(p)\cdot g$ for all $p\in P$, $g\in G$ — whose induced base map $\bar f\colon M\to M$ (the unique smooth map with $\pi\circ f=\bar f\circ\pi$) is the identity. The group of all such is the **gauge group** $\mathcal{G}(P)$; it acts on $\mathcal{A}(P)$ on the right by pull-back, $\omega\cdot f:=f^*\omega$. For the fixed base point $b$, the **reduced gauge group** is
$$\mathcal{G}_b(P):=\{f\in\mathcal{G}(P):f|_{P_b}=\operatorname{id}_{P_b}\}=\ker\big(\mathcal{G}(P)\to\operatorname{Diff}(P_b),\ f\mapsto f|_{P_b}\big),$$
the gauge transformations that restrict to the identity on the single fibre over $b$.

For a connection $\omega$ and a piecewise smooth curve $c\colon[0,1]\to M$, $\Gamma_c\colon P_{c(0)}\to P_{c(1)}$ denotes [[Def - Parallel Transport in a Principal Bundle|parallel transport]], the map $p\mapsto\tilde c(1)$ where $\tilde c$ is the $\omega$-horizontal lift of $c$ with $\tilde c(0)=p$. For a loop $c$ based at $x=\pi(p)$, the [[Def - Holonomy Group of a Connection|holonomy]] $\operatorname{hol}_p(c)\in G$ is defined by $\Gamma_c(p)=p\cdot\operatorname{hol}_p(c)$, and $\operatorname{Hol}_p(\omega)=\{\operatorname{hol}_p(c):c\text{ a loop at }x\}\subseteq G$ is the holonomy group at $p$. For a subset $S\subseteq G$, its **centraliser** in $G$ is $Z_G(S)=\{z\in G:zs=sz\text{ for all }s\in S\}$; the centre of $G$ is $Z(G)=Z_G(G)$.

> [!warning] Convention: base and connection space
> Bär (*Gauge Theory*, §2.7) writes $B$ for the base manifold and $\mathcal{C}(P)$ for the space of connection one-forms. This series writes $M$ for the base and $\mathcal{A}(P)$ for the connection space, following Haydys and the standard gauge-theory literature; the objects are identical. Bär also writes the concatenation $c_2*c_1$ for "first traverse $c_1$, then $c_2$", so that $\Gamma_{c_2*c_1}=\Gamma_{c_2}\circ\Gamma_{c_1}$, and $\bar c$ for the reversed curve; we adopt both.

The full symbol registry for the chapter is on the topic page [[Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections]].

---

# Statement

> **Proposition (freeness of the reduced gauge action).** Let $\pi\colon P\to M$ be a principal $G$-bundle over a **connected** manifold $M$, and let $b\in M$. Then the right action of the reduced gauge group $\mathcal{G}_b(P)$ on the space of connections $\mathcal{A}(P)$ is **free**: if $f\in\mathcal{G}_b(P)$ and $\omega\in\mathcal{A}(P)$ satisfy $f^*\omega=\omega$, then $f=\operatorname{id}_P$. Equivalently, the stabiliser of every connection $\omega$ inside $\mathcal{G}_b(P)$ is trivial.

The companion result identifies the full stabiliser inside the whole gauge group. It is the statement Donaldson and Kronheimer use to describe the reducible connections and the singularities of the moduli space.

> **Corollary (the stabiliser is a centraliser of the holonomy).** With $M$ connected and $b\in M$, fix a point $p\in P_b$. For a connection $\omega\in\mathcal{A}(P)$ let
> $$\operatorname{Stab}(\omega):=\{f\in\mathcal{G}(P):f^*\omega=\omega\}$$
> denote its stabiliser inside the full gauge group. Then the map
> $$\Phi\colon\operatorname{Stab}(\omega)\longrightarrow G,\qquad \Phi(f)=z\ \text{ where }\ f(p)=p\cdot z,$$
> is a well-defined injective group homomorphism whose image is exactly the centraliser $Z_G(\operatorname{Hol}_p(\omega))$. Hence
> $$\operatorname{Stab}(\omega)\ \cong\ Z_G\!\big(\operatorname{Hol}_p(\omega)\big).$$
> The isomorphism type of the right-hand side is independent of the choices of $b$ and $p$: replacing $p$ by $p\cdot g$ replaces the holonomy group by $g^{-1}\operatorname{Hol}_p(\omega)\,g$ and hence the centraliser by its conjugate $g^{-1}Z_G(\operatorname{Hol}_p(\omega))\,g$.

The two statements are two readings of one mechanism, and the corollary contains the proposition: the reduced gauge group $\mathcal{G}_b(P)$ consists of the $f$ with $f|_{P_b}=\operatorname{id}$, in particular $f(p)=p$, so its intersection with $\operatorname{Stab}(\omega)$ is exactly $\ker\Phi$, which the corollary shows is trivial.

---

# Motivation

The central objects of gauge theory are not individual connections but the orbit space $\mathcal{A}(P)/\mathcal{G}(P)$ — the set of connections *modulo* the gauge symmetry, on which the Yang–Mills functional, the Chern–Simons functional, and the Seiberg–Witten equations actually descend to well-posed problems. One would like this quotient to be a smooth manifold, or at least smooth away from a small bad locus, so that the machinery of transversality, Fredholm theory, and cobordism can be brought to bear. The obstruction to smoothness of a quotient $X/H$ by a group action is always the same: **points with nontrivial stabiliser**. Where the action is free, the quotient inherits a manifold structure from a slice; where a stabiliser jumps up, the quotient has an orbifold or conical singularity. So before one can say anything about the geometry of $\mathcal{A}/\mathcal{G}$, one must understand the stabilisers of the gauge action, and that is exactly what this page computes.

The proposition answers the question in its cleanest form. It says that if we cut the gauge group down to the *reduced* gauge group — the transformations pinned to the identity over one point $b$ — then the action becomes literally free, with no fixed points at all. Geometrically, pinning $f$ over a single fibre is the same as **framing** the bundle at $b$: a choice of identification $P_b\cong G$, together with the demand that $f$ respect it. The proposition is therefore the statement that the *framed* configuration space $\mathcal{A}(P)/\mathcal{G}_b(P)$ has no isotropy, which is why framed moduli spaces (Haydys's §1 scheme, and the framed instanton spaces of Donaldson theory) are manifolds where the unframed ones may not be.

The corollary explains what happens without framing. The full gauge group can have a nontrivial stabiliser, but that stabiliser is never mysterious: it is precisely the centraliser in $G$ of the holonomy group of $\omega$. This turns a question about an infinite-dimensional symmetry group into a finite-dimensional computation in the structure group $G$. Two extreme cases make the content vivid. If the connection is **irreducible** — its holonomy group fills out $G$, or at least is not contained in any proper subgroup whose centraliser exceeds the centre — then $Z_G(\operatorname{Hol}_p(\omega))=Z(G)$, the centre, and the stabiliser is as small as the group law permits; the effective symmetry group $\mathcal{G}(P)/Z(G)$ then acts freely on the irreducible connections $\mathcal{A}^*(P)$, and the irreducible quotient $\mathcal{B}^*=\mathcal{A}^*/\mathcal{G}$ is smooth. If the connection is **reducible** — its holonomy sits inside a proper subgroup $H\subsetneq G$ — then the centraliser is strictly larger than the centre, the stabiliser jumps, and the corresponding point of $\mathcal{B}=\mathcal{A}/\mathcal{G}$ is a singularity. The reducible locus, computed this way, is exactly the cone points that drive Donaldson's diagonalisation argument.

We assume the reader knows what a principal connection is, how horizontal lifts and parallel transport are constructed from it, and what the holonomy group is; all three are developed earlier in this chapter and restated at the point of use below.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of the proposition is mild — a connected base, a principal connection, and the reduced gauge group — so the real question is: when does a problem hand us a connection-preserving automorphism, or force a particular stabiliser, without naming one?

The first disguised source is **a symmetry of a field configuration**. Suppose a physical or geometric problem produces a connection $\omega$ together with a group $\Sigma$ of symmetries of the bundle that leave $\omega$ invariant — the isometries of the base that lift to $P$ and fix the Yang–Mills field, say, or the residual symmetries of a monopole or instanton. Each such symmetry that covers the identity on $M$ is by definition an element of $\operatorname{Stab}(\omega)$, so the bridge $\Sigma\Rightarrow\Sigma\subseteq\operatorname{Stab}(\omega)=Z_G(\operatorname{Hol}_p(\omega))$ turns an assumed symmetry into a constraint on the holonomy: the holonomy of a symmetric connection must commute with the whole symmetry group. The non-obvious content is that a symmetry which looks like an infinite-dimensional object (a bundle automorphism) is pinned down by a single element $z\in G$. *Example problem:* show that a $G$-connection admitting a gauge symmetry of order $n$ not in the centre must be reducible, because its holonomy is confined to the centraliser of a non-central element.

The second disguised source is **reducibility of the connection**, however it is packaged. A connection is called reducible when its holonomy group is conjugate into a proper closed subgroup $H\subsetneq G$; this happens, for instance, whenever the bundle splits as a direct sum, or admits a parallel section of an associated bundle, or is pulled back from a bundle with smaller structure group. Any of these hypotheses is a bridge to "$\operatorname{Hol}_p(\omega)\subseteq H$", and the corollary then reads off $\operatorname{Stab}(\omega)=Z_G(\operatorname{Hol}_p(\omega))\supseteq Z_G(H)\supsetneq Z(G)$: the stabiliser is strictly larger than the centre. The non-obvious step is that a *global* splitting of the bundle registers as a *pointwise* commutation relation in $G$. *Example problem:* for a rank-two Hermitian bundle that splits as a sum of line bundles, show that the $U(2)$-connection has stabiliser containing the diagonal torus, hence is reducible.

The third disguised source is **a framing, or any choice that rigidifies a single fibre**. Whenever a construction fixes an identification of $P_b$ with $G$ — a marked point in the fibre, an evaluation map, a boundary condition at a puncture — the transformations that are allowed to move things are exactly the reduced gauge group $\mathcal{G}_b(P)$. The bridge "framing $\Rightarrow$ the acting group is $\mathcal{G}_b(P)$" makes the proposition available and tells us the framed action is free, so the framed quotient is a manifold with no isotropy to worry about. The non-obviousness is that adding one finite-dimensional piece of data (the framing at $b$) removes *all* the isotropy of the infinite-dimensional action at once. *Example problem:* identify the framed moduli space of flat connections on a surface with a smooth representation variety, using freeness of the reduced gauge action to avoid the singularities of the unframed character variety.

**Targets (Output Amplification)**

The bare outputs are "the action is free" and "$\operatorname{Stab}(\omega)\cong Z_G(\operatorname{Hol}_p(\omega))$"; combined with other facts they yield the smoothness of moduli spaces.

Combine the proposition with **a proper action and a Banach-manifold model of $\mathcal{A}(P)$**. Freeness alone is not enough for a smooth quotient; but a free *and* proper action of a Banach Lie group on a Banach manifold admits local slices, so the quotient is a smooth Banach manifold. The extra ingredient is the properness of the gauge action (proved via the Sobolev completions of chapters IX and XI) together with the Banach Lie group structure on $\mathcal{G}_b(P)$. The payoff is that the framed configuration space $\mathcal{A}(P)/\mathcal{G}_b(P)$ is a smooth manifold, the ambient space in which framed instanton and Seiberg–Witten moduli spaces live as cut-out subsets.

Combine the corollary with **irreducibility**. If $\operatorname{Hol}_p(\omega)$ is not contained in any proper subgroup with an oversized centraliser — the working definition of an irreducible connection — then $Z_G(\operatorname{Hol}_p(\omega))=Z(G)$, and the stabiliser of $\omega$ in $\mathcal{G}(P)$ is the constant central gauge transformations. The extra ingredient is the classification of centralisers in the specific structure group; for $G=SU(n)$ the centre is the group of $n$-th roots of unity times the identity. The payoff is that on the irreducible locus $\mathcal{A}^*(P)$ the quotient group $\mathcal{G}(P)/Z(G)$ acts freely, so $\mathcal{B}^*(P)=\mathcal{A}^*(P)/\mathcal{G}(P)$ is smooth — the basic manifold of Yang–Mills theory (chapter VII) and of the Seiberg–Witten construction (chapter XI).

Combine the corollary with **the structure of a specific low-rank group**. For $G=U(1)$, abelian, every element commutes with everything, so $Z_{U(1)}(\operatorname{Hol}_p(\omega))=U(1)$ for every connection: an abelian connection always has stabiliser the full constant gauge group $U(1)$, and there is no irreducible locus. For $G=SU(2)$ with holonomy all of $SU(2)$, the centraliser is $Z(SU(2))=\{\pm\mathbf 1\}$, so the stabiliser is $\{\pm\mathbf 1\}$. The extra ingredient is the representation theory that distinguishes these cases; the payoff is the precise reducible locus of $SU(2)$-gauge theory, where the holonomy sits in a maximal torus $U(1)\subset SU(2)$ and the stabiliser jumps to that torus — the cone-on-$\mathbb{CP}^2$ singularities of Donaldson's moduli space (chapter XIII).

---

# Why Is It True

Forget the formalism and picture a gauge transformation $f$ that preserves the connection $\omega$. To preserve $\omega$ is to preserve its horizontal distribution $H=\ker\omega$, because a diffeomorphism sends $\ker\omega$ to $\ker(f^*\omega)$ and here $f^*\omega=\omega$. But the horizontal distribution is exactly the data that defines parallel transport: a horizontal curve is one whose velocity lies in $H$ at each instant, and parallel transport moves a point along the horizontal lift of a base curve. A map that preserves $H$ therefore carries horizontal curves to horizontal curves, which means it **commutes with parallel transport**: transporting and then applying $f$ gives the same result as applying $f$ and then transporting.

Now use connectedness. Because $M$ is connected, every point of the base — and hence, after one group shift in the fibre, every point of the total space $P$ — can be reached from the base point $b$ by parallel transport along some curve. So a connection-preserving $f$ is completely determined by what it does over the single fibre $P_b$: its value everywhere else is forced by "transport across, then $f$ equals $f$, then transport across". If $f$ is the identity on $P_b$ (the reduced gauge condition), it is forced to be the identity everywhere. That is the proposition.

**A connection-preserving gauge transformation is rigid: it commutes with parallel transport, and parallel transport out of one fibre reaches the whole connected bundle, so $f$ is determined by its restriction to that one fibre.**

The corollary is the same idea counted more carefully. Over the base fibre $P_b$, an $\omega$-preserving $f$ is $f(p)=p\cdot z$ for a single group element $z$, and this $z$ is the *only* freedom. But not every $z$ is allowed: transporting around a loop at $b$ multiplies $p$ on the right by a holonomy element $a=\operatorname{hol}_p(c)$, and the demand that $f$ commute with this transport forces $z$ and $a$ to commute in $G$. Ranging over all loops, $z$ must commute with the entire holonomy group; conversely any such $z$ defines a consistent, connection-preserving $f$ by transporting it out from $b$. Thus the stabiliser is exactly the centraliser of the holonomy — the connection remembers, in its holonomy group, precisely which fibre-symmetries it will tolerate.

---

# What Makes This Hard

The one genuinely non-obvious step is the translation "$f^*\omega=\omega$ $\iff$ $df$ preserves the horizontal distribution $H=\ker\omega$", and its consequence that $f$ carries $\omega$-horizontal lifts to $\omega$-horizontal lifts. Everything else is bookkeeping with the uniqueness of horizontal lifts, but this step is what converts the algebraic hypothesis into the dynamical statement that makes the argument run. A reader who tries to prove the proposition by manipulating the one-form $\omega$ directly, rather than passing to horizontal curves and lifts, will not find the argument.

Two errors are common. The first is to drop connectedness: on a disconnected base the reduced gauge group only controls the component containing $b$, and $f$ can be an arbitrary connection-preserving automorphism over the other components, so the action is *not* free — the hypothesis "$M$ connected" is used exactly once, to join $b$ to an arbitrary point by a curve, and cannot be removed. The second, in the corollary, is to check only that $z$ must centralise the holonomy (the easy inclusion) and to forget that one must also *construct* an $f$ from each centralising $z$ and prove it is well-defined independently of the connecting curve; the well-definedness is precisely where the centraliser condition is consumed a second time.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Convert the algebraic hypothesis $f^*\omega=\omega$ into the geometric statement that $f$ preserves the horizontal distribution, hence maps horizontal lifts to horizontal lifts, hence commutes with parallel transport. Then exploit connectedness: parallel transport out of the fibre $P_b$ reaches all of $P$, so $f$ is determined by $f|_{P_b}$; if $f|_{P_b}=\operatorname{id}$ we get $f=\operatorname{id}$ (the proposition), and in general $f|_{P_b}$ is a single group element $z$ constrained to centralise the holonomy (the corollary).

**Subgoal decomposition:**

1. **Any two points of $M$ are joined by a piecewise smooth curve.**
   - *Hint:* The relation "joined by a piecewise smooth curve" is an equivalence relation; each class is open because charts contain straight segments, so each class is also closed, and connectedness forces a single class.
   - *Why needed:* The horizontal lift theorem needs a piecewise smooth curve from $b$ to the target point; this is where "$M$ connected" enters.

2. **If $f^*\omega=\omega$ then $df_q(H_q)=H_{f(q)}$ for all $q$, and consequently $f\circ\tilde c$ is $\omega$-horizontal whenever $\tilde c$ is.**
   - *Hint:* For $X\in H_q=\ker\omega_q$, compute $\omega_{f(q)}(df_qX)=(f^*\omega)_q(X)=\omega_q(X)=0$; then match dimensions using that $df_q$ is an isomorphism.
   - *Why needed:* This is the bridge from the algebraic hypothesis to horizontal lifts; it powers both the proposition and the corollary.

3. **A connection-preserving automorphism commutes with parallel transport: $f\circ\Gamma_c=\Gamma_c\circ f$.**
   - *Hint:* $f\circ\tilde c$ is a horizontal lift of $c$ (subgoal 2) starting at $f(\tilde c(0))$; by uniqueness it is *the* horizontal lift through that point, so evaluating at $t=1$ gives the identity.
   - *Why needed:* It is the exact statement "transport and $f$ commute" used to propagate $f$ out from $P_b$.

4. **Proposition.** With $f\in\mathcal{G}_b(P)$ and $f^*\omega=\omega$, show $f(p)=p$ for arbitrary $p$.
   - *Hint:* Join $b$ to $\pi(p)$ by a curve $c$; lift horizontally to $\tilde c$ with $\tilde c(1)=p$; then $f\circ\tilde c$ is a horizontal lift agreeing with $\tilde c$ at $t=0$ (because $\tilde c(0)\in P_b$ and $f|_{P_b}=\operatorname{id}$), hence equal to $\tilde c$; read off $f(p)=p$.
   - *Why needed:* This is the theorem.

5. **Corollary, injectivity and the centraliser condition.** For $f\in\operatorname{Stab}(\omega)$ write $f(p)=p\cdot z$; show $f$ is determined by $z$ (injectivity) and that $z$ centralises $\operatorname{Hol}_p(\omega)$.
   - *Hint:* Injectivity from subgoal 3 as in subgoal 4 with $\tilde c(0)=p$; the centraliser condition from applying subgoal 3 to a loop, using $\Gamma_c(p)=p\cdot\operatorname{hol}_p(c)$ and $\Gamma_c\circ R_g=R_g\circ\Gamma_c$.
   - *Why needed:* It shows $\Phi$ is an injective homomorphism into the centraliser.

6. **Corollary, surjectivity.** Given $z\in Z_G(\operatorname{Hol}_p(\omega))$, build $f_z$ by transporting $z$ out from $b$; prove it is well-defined (independent of the connecting curve, using the centraliser condition), smooth, equivariant, covers the identity, and preserves $\omega$.
   - *Hint:* Set $f_z(q)=\Gamma_c(p)\cdot z\cdot h$ where $q=\Gamma_c(p)\cdot h$; two curves differ by a holonomy element, which $z$ commutes past.
   - *Why needed:* It shows $\Phi$ is onto the centraliser, completing the isomorphism.

---

# Lemma Decomposition

> [!note]- Lemma 1: A connected manifold is piecewise-smoothly path-connected
> **Statement:** If $M$ is a connected smooth manifold, then any two points $x,y\in M$ are joined by a piecewise smooth curve $c\colon[0,1]\to M$ with $c(0)=x$, $c(1)=y$.
>
> **Hint:** Show the relation "joined by a piecewise smooth curve" has open equivalence classes; open classes in a connected space that partition it force a single class.
>
> **Why needed:** The horizontal lift theorem is stated for piecewise smooth curves, and the proof must join the base point $b$ to an arbitrary point of $M$ by such a curve. This is the only place the hypothesis "$M$ connected" is used.
>
> > [!note]- Full proof
> > Define a relation on $M$ by declaring $x\sim y$ when there is a piecewise smooth curve from $x$ to $y$. This is an equivalence relation: **reflexivity** holds via the constant curve $c\equiv x$, which is smooth; **symmetry** holds because if $c$ runs from $x$ to $y$ then the reversed curve $\bar c(t)=c(1-t)$ is piecewise smooth and runs from $y$ to $x$; **transitivity** holds because if $c_1$ runs from $x$ to $y$ and $c_2$ from $y$ to $z$, the concatenation $t\mapsto c_1(2t)$ for $t\in[0,\tfrac12]$ and $t\mapsto c_2(2t-1)$ for $t\in[\tfrac12,1]$ is piecewise smooth (each piece is smooth and they meet at $y$) and runs from $x$ to $z$.
> >
> > **Each equivalence class is open.** Let $x_0\in M$ and let $[x_0]$ be its class. Choose a smooth chart $\varphi\colon U\to \varphi(U)\subseteq\mathbb{R}^n$ with $x_0\in U$ and $\varphi(U)$ an open ball (such a chart exists because $M$ is a smooth manifold and every point has a Euclidean chart neighbourhood, which we may shrink to a ball). For any $x\in U$, the segment $t\mapsto\varphi^{-1}\big((1-t)\varphi(x_0)+t\varphi(x)\big)$ is a smooth curve inside $U$ from $x_0$ to $x$ (the straight segment between two points of a ball stays in the ball), so $x\sim x_0$ and $x\in[x_0]$. Hence $U\subseteq[x_0]$, and $[x_0]$ is open.
> >
> > **Conclusion.** The equivalence classes are disjoint, non-empty, open, and cover $M$. If there were two or more classes, then a single class $[x]$ and the union of all the others would be two disjoint non-empty open sets covering $M$, contradicting connectedness of $M$. Therefore there is exactly one class, so any two points $x,y\in M$ satisfy $x\sim y$; that is, they are joined by a piecewise smooth curve. $\blacksquare$

> [!note]- Lemma 2: A connection-preserving automorphism preserves the horizontal distribution
> **Statement:** Let $\omega\in\mathcal{A}(P)$ with horizontal distribution $H=\ker\omega$, and let $f\in\operatorname{Aut}(P)$ satisfy $f^*\omega=\omega$. Then for every $q\in P$ one has $df_q(H_q)=H_{f(q)}$. Consequently, if $\tilde c\colon[0,1]\to P$ is an $\omega$-horizontal lift of a piecewise smooth curve $c$ in $M$, then $f\circ\tilde c$ is an $\omega$-horizontal lift of $\bar f\circ c$.
>
> **Hint:** Test membership of $\ker\omega$ before and after $df$; the hypothesis $f^*\omega=\omega$ makes the two kernels correspond, and a dimension count upgrades the inclusion to equality.
>
> **Why needed:** It is the bridge from the algebraic hypothesis $f^*\omega=\omega$ to the geometric statement that $f$ maps horizontal lifts to horizontal lifts, on which the whole argument turns.
>
> > [!note]- Full proof
> > **The inclusion $df_q(H_q)\subseteq H_{f(q)}$.** Recall that the horizontal distribution of a connection is $H_r=\ker\omega_r$ at each $r\in P$ ([[Def - Connection on a Principal Bundle|definition of a principal connection]]: $H=\ker\omega$, and $T_rP=H_r\oplus V_r$ with $\dim H_r=\dim M$). Let $X\in H_q$, so $\omega_q(X)=0$. Using the definition of the pull-back one-form and the hypothesis $f^*\omega=\omega$,
> > $$\omega_{f(q)}\big(df_q(X)\big)=(f^*\omega)_q(X)\qquad\text{(definition of pull-back: }(f^*\omega)_q(X)=\omega_{f(q)}(df_qX)\text{)}$$
> > $$=\omega_q(X)\qquad\text{(hypothesis }f^*\omega=\omega\text{)}$$
> > $$=0\qquad\text{(since }X\in H_q=\ker\omega_q\text{)}.$$
> > Hence $df_q(X)\in\ker\omega_{f(q)}=H_{f(q)}$, proving $df_q(H_q)\subseteq H_{f(q)}$.
> >
> > **Upgrade to equality.** Because $f$ is a diffeomorphism, its differential $df_q\colon T_qP\to T_{f(q)}P$ is a linear isomorphism, so it is injective on $H_q$ and therefore $\dim df_q(H_q)=\dim H_q=\dim M$. By the connection axioms $\dim H_{f(q)}=\dim M$ as well. A subspace of dimension $\dim M$ contained in a subspace of the same dimension $\dim M$ must equal it; hence $df_q(H_q)=H_{f(q)}$.
> >
> > **Horizontal lifts map to horizontal lifts.** Let $\tilde c$ be an $\omega$-horizontal lift of $c$, meaning $\pi\circ\tilde c=c$ and $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ for all $t$ (at the finitely many non-smooth instants, the one-sided velocities). Set $\hat c:=f\circ\tilde c$. Then $\hat c$ is piecewise smooth (composition of the piecewise smooth $\tilde c$ with the smooth $f$), and $\pi\circ\hat c=\pi\circ f\circ\tilde c=\bar f\circ\pi\circ\tilde c=\bar f\circ c$ (definition of the induced base map $\bar f$). Its velocity is
> > $$\dot{\hat c}(t)=df_{\tilde c(t)}\big(\dot{\tilde c}(t)\big)\in df_{\tilde c(t)}\big(H_{\tilde c(t)}\big)=H_{f(\tilde c(t))}=H_{\hat c(t)}\qquad\text{(chain rule; then }\dot{\tilde c}(t)\in H_{\tilde c(t)}\text{ and }df(H)=H\text{ just proved).}$$
> > So $\hat c$ is horizontal, that is, an $\omega$-horizontal lift of $\bar f\circ c$. $\blacksquare$

> [!note]- Lemma 3: Connection-preserving automorphisms commute with parallel transport
> **Statement:** Let $\omega\in\mathcal{A}(P)$, let $f\in\operatorname{Aut}(P)$ satisfy $f^*\omega=\omega$, and let $c\colon[0,1]\to M$ be piecewise smooth. Then on the fibre $P_{c(0)}$,
> $$f\circ\Gamma_c=\Gamma_{\bar f\circ c}\circ f.$$
> In particular, if $f$ is a gauge transformation (so $\bar f=\operatorname{id}$ and $\bar f\circ c=c$), then $f\circ\Gamma_c=\Gamma_c\circ f$ as maps $P_{c(0)}\to P_{c(1)}$.
>
> **Hint:** Apply $f$ to the horizontal lift through a point $q$; by Lemma 2 the result is the horizontal lift through $f(q)$, so its endpoint is $\Gamma_{\bar f\circ c}(f(q))$.
>
> **Why needed:** It packages the rigidity of $\omega$-preserving automorphisms into a single clean identity, used to propagate $f$ out of the base fibre in both the proposition and the corollary, and to derive the centraliser condition.
>
> > [!note]- Full proof
> > We use the **existence, uniqueness and equivariance of horizontal lifts**, restated here: for a connection $\omega$, a piecewise smooth curve $c$, an instant $t_0\in[0,1]$ and a point $q\in P_{c(t_0)}$, there is a unique $\omega$-horizontal lift $\tilde c_q$ of $c$ with $\tilde c_q(t_0)=q$, defined on all of $[0,1]$ ([[Thm - Existence and Uniqueness of Horizontal Lifts|existence and uniqueness of horizontal lifts]]). Parallel transport is $\Gamma_c(q)=\tilde c_q(1)$ where $\tilde c_q(0)=q$.
> >
> > Fix $q\in P_{c(0)}$ and let $\tilde c_q$ be the $\omega$-horizontal lift of $c$ with $\tilde c_q(0)=q$, so $\Gamma_c(q)=\tilde c_q(1)$. By **Lemma 2**, $f\circ\tilde c_q$ is an $\omega$-horizontal lift of $\bar f\circ c$; its value at $t=0$ is $f(\tilde c_q(0))=f(q)$. By the **uniqueness** clause of the horizontal lift theorem, $f\circ\tilde c_q$ is *the* horizontal lift of $\bar f\circ c$ through $f(q)$ at $t=0$; that is, $f\circ\tilde c_q=\widetilde{(\bar f\circ c)}_{f(q)}$. Evaluating both sides at $t=1$,
> > $$f\big(\Gamma_c(q)\big)=f\big(\tilde c_q(1)\big)=\widetilde{(\bar f\circ c)}_{f(q)}(1)=\Gamma_{\bar f\circ c}\big(f(q)\big)\qquad\text{(definition of }\Gamma\text{ as endpoint of the horizontal lift).}$$
> > Since $q\in P_{c(0)}$ was arbitrary, $f\circ\Gamma_c=\Gamma_{\bar f\circ c}\circ f$ on $P_{c(0)}$. When $f\in\mathcal{G}(P)$ we have $\bar f=\operatorname{id}$, so $\bar f\circ c=c$ and the identity reads $f\circ\Gamma_c=\Gamma_c\circ f$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Throughout, $M$ is connected, $b\in M$ is fixed, and $\omega\in\mathcal{A}(P)$. We use the following restated facts about the tools involved.
> - **Horizontal lifts** ([[Thm - Existence and Uniqueness of Horizontal Lifts|existence and uniqueness of horizontal lifts]]): for a piecewise smooth $c$ and $q\in P_{c(t_0)}$ there is a unique $\omega$-horizontal lift $\tilde c_q$ with $\tilde c_q(t_0)=q$; and the horizontal lift through $q\cdot g$ is $\tilde c_q\cdot g$ (equivariance).
> - **Properties of parallel transport** ([[Thm - Properties of Parallel Transport|properties of parallel transport]]): $\Gamma_c$ is a diffeomorphism $P_{c(0)}\to P_{c(1)}$; it is equivariant, $\Gamma_c\circ R_g=R_g\circ\Gamma_c$; it composes, $\Gamma_{c_2*c_1}=\Gamma_{c_2}\circ\Gamma_{c_1}$; and reversal inverts it, $\Gamma_{\bar c}=\Gamma_c^{-1}$.
> - **Holonomy** ([[Def - Holonomy Group of a Connection|holonomy group of a connection]]): for a loop $c$ at $x=\pi(q)$, $\Gamma_c(q)=q\cdot\operatorname{hol}_q(c)$; the set $\operatorname{Hol}_q(\omega)=\{\operatorname{hol}_q(c)\}$ is a subgroup of $G$ (closed under products by concatenation and under inverses by reversal); and $\operatorname{Hol}_{q\cdot g}(\omega)=g^{-1}\operatorname{Hol}_q(\omega)\,g$.
> - **The gauge action** ([[Thm - Gauge Transformations Act on Connections and Curvature|gauge transformations act on connections and curvature]]): for $f\in\operatorname{Aut}(P)$ and $\omega\in\mathcal{A}(P)$, the pull-back $f^*\omega$ is again a connection, and $(\omega,f)\mapsto f^*\omega$ is a right action; every $f\in\operatorname{Aut}(P)$ carries fibres to fibres and covers a unique smooth $\bar f$, with $\bar f=\operatorname{id}$ for $f\in\mathcal{G}(P)$.
>
> ## Part I — freeness of the reduced gauge action
>
> **Step 0 — reduce to a fixed-point statement.** A right action is free precisely when the only group element fixing any point is the identity. So we must show: if $f\in\mathcal{G}_b(P)$ satisfies $\omega\cdot f=f^*\omega=\omega$, then $f=\operatorname{id}_P$. Assume such an $f$; we show $f(p)=p$ for an arbitrary $p\in P$.
>
> **Step 1 — join $b$ to $\pi(p)$.** Since $M$ is connected, by **Lemma 1** there is a piecewise smooth curve $c\colon[0,1]\to M$ with $c(0)=b$ and $c(1)=\pi(p)$.
>
> **Step 2 — lift horizontally through $p$.** Let $\tilde c\colon[0,1]\to P$ be the unique $\omega$-horizontal lift of $c$ with $\tilde c(1)=p$ (existence and uniqueness of horizontal lifts, with initial instant $t_0=1$). Then $\tilde c(0)\in P_{c(0)}=P_b$.
>
> **Step 3 — apply $f$ and recognise a horizontal lift.** Put $\hat c:=f\circ\tilde c$. Because $f\in\mathcal{G}_b(P)\subseteq\mathcal{G}(P)$ satisfies $f^*\omega=\omega$, **Lemma 2** shows $\hat c$ is an $\omega$-horizontal lift of $\bar f\circ c=c$ (here $\bar f=\operatorname{id}$ as $f$ is a gauge transformation).
>
> **Step 4 — match initial conditions.** Evaluate $\hat c$ at $t=0$:
> $$\hat c(0)=f\big(\tilde c(0)\big)=\tilde c(0)\qquad\text{(since }\tilde c(0)\in P_b\text{ and }f|_{P_b}=\operatorname{id}_{P_b}\text{, the defining property of }\mathcal{G}_b(P)\text{).}$$
> Thus $\hat c$ and $\tilde c$ are both $\omega$-horizontal lifts of the same curve $c$ with the same value $\tilde c(0)$ at $t=0$. By the **uniqueness** clause of the horizontal lift theorem, $\hat c=\tilde c$ on all of $[0,1]$.
>
> **Step 5 — read off the fixed point.** Evaluating the equality $\hat c=\tilde c$ at $t=1$,
> $$f(p)=f\big(\tilde c(1)\big)=\hat c(1)=\tilde c(1)=p.$$
> As $p\in P$ was arbitrary, $f=\operatorname{id}_P$. Therefore the stabiliser of $\omega$ in $\mathcal{G}_b(P)$ is trivial for every $\omega$, and the action of $\mathcal{G}_b(P)$ on $\mathcal{A}(P)$ is free.
>
> ## Part II — the stabiliser is the centraliser of the holonomy
>
> Fix $p\in P_b$ and abbreviate $\mathcal{S}:=\operatorname{Stab}(\omega)=\{f\in\mathcal{G}(P):f^*\omega=\omega\}$ and $\operatorname{Hol}:=\operatorname{Hol}_p(\omega)$.
>
> **Step 0 — the map $\Phi$ is defined.** For $f\in\mathcal{S}\subseteq\mathcal{G}(P)$, $f$ covers the identity, so $f$ maps the fibre $P_b$ to itself; hence $f(p)\in P_b$. Because the right $G$-action on the fibre $P_b$ is free and transitive (principal bundle axiom), there is a unique $z=z(f)\in G$ with $f(p)=p\cdot z$. Define $\Phi(f):=z(f)$.
>
> **Step 1 — $\Phi$ is a group homomorphism.** The group operation on $\mathcal{G}(P)$ is composition. For $f_1,f_2\in\mathcal{S}$,
> $$(f_1\circ f_2)(p)=f_1\big(f_2(p)\big)=f_1\big(p\cdot z(f_2)\big)=f_1(p)\cdot z(f_2)=\big(p\cdot z(f_1)\big)\cdot z(f_2)=p\cdot\big(z(f_1)z(f_2)\big),$$
> using the equivariance $f_1(p\cdot g)=f_1(p)\cdot g$ in the middle step. By uniqueness of the fibre coordinate, $z(f_1\circ f_2)=z(f_1)z(f_2)$, so $\Phi(f_1\circ f_2)=\Phi(f_1)\Phi(f_2)$.
>
> **Step 2 — the image lies in the centraliser $Z_G(\operatorname{Hol})$.** Let $f\in\mathcal{S}$ with $z=\Phi(f)$, and let $c$ be a loop at $b$ with $a:=\operatorname{hol}_p(c)\in\operatorname{Hol}$, so $\Gamma_c(p)=p\cdot a$. By **Lemma 3** (applicable since $f^*\omega=\omega$ and $f\in\mathcal{G}(P)$), $f\circ\Gamma_c=\Gamma_c\circ f$ on $P_b$. Evaluate at $p$ and expand both sides:
> $$f\big(\Gamma_c(p)\big)=f(p\cdot a)=f(p)\cdot a=(p\cdot z)\cdot a=p\cdot(za)\qquad\text{(holonomy }\Gamma_c(p)=p\cdot a\text{; equivariance of }f\text{),}$$
> $$\Gamma_c\big(f(p)\big)=\Gamma_c(p\cdot z)=\Gamma_c(p)\cdot z=(p\cdot a)\cdot z=p\cdot(az)\qquad\text{(equivariance }\Gamma_c\circ R_z=R_z\circ\Gamma_c\text{; holonomy).}$$
> Since the two left-hand sides are equal, $p\cdot(za)=p\cdot(az)$, and the free action on the fibre gives $za=az$. As $a$ ranges over all of $\operatorname{Hol}$, this says $z\in Z_G(\operatorname{Hol})$. Hence $\Phi(\mathcal{S})\subseteq Z_G(\operatorname{Hol})$.
>
> **Step 3 — $\Phi$ is injective.** Suppose $f\in\mathcal{S}$ with $\Phi(f)=e$, that is $f(p)=p$. Let $q\in P$ be arbitrary. By **Lemma 1** choose a piecewise smooth $c$ from $b$ to $\pi(q)$; since $\Gamma_c(p)\in P_{\pi(q)}$ and the fibre action is transitive, write $q=\Gamma_c(p)\cdot h$ for a unique $h\in G$. Then
> $$f(q)=f\big(\Gamma_c(p)\cdot h\big)=f\big(\Gamma_c(p)\big)\cdot h=\Gamma_c\big(f(p)\big)\cdot h=\Gamma_c(p)\cdot h=q,$$
> using equivariance of $f$, then **Lemma 3** ($f\circ\Gamma_c=\Gamma_c\circ f$), then $f(p)=p$. As $q$ was arbitrary, $f=\operatorname{id}_P$, so $\ker\Phi$ is trivial and $\Phi$ is injective. (This also re-proves Part I: an $f\in\mathcal{G}_b(P)\cap\mathcal{S}$ has $f(p)=p$, hence $\Phi(f)=e$, hence $f=\operatorname{id}$.)
>
> **Step 4 — $\Phi$ is surjective onto $Z_G(\operatorname{Hol})$.** Let $z\in Z_G(\operatorname{Hol})$ be given. We construct $f_z\in\mathcal{S}$ with $\Phi(f_z)=z$.
>
> *Construction.* For $q\in P$, choose (Lemma 1) a piecewise smooth curve $c$ from $b$ to $\pi(q)$, write $q=\Gamma_c(p)\cdot h$ with $h\in G$ unique, and set
> $$f_z(q):=\Gamma_c(p)\cdot z\cdot h=q\cdot(h^{-1}zh).$$
>
> *Well-definedness (independence of the curve).* Let $c_0,c_1$ be two piecewise smooth curves from $b$ to $x:=\pi(q)$, giving $q=\Gamma_{c_0}(p)\cdot h_0=\Gamma_{c_1}(p)\cdot h_1$. Write $\Gamma_{c_1}(p)=\Gamma_{c_0}(p)\cdot k$ for the unique $k\in G$ (both points lie in $P_x$). Consider the loop $\ell:=\bar c_1*c_0$ at $b$ (first $c_0$ from $b$ to $x$, then $\bar c_1$ from $x$ back to $b$). Using the composition and reversal properties of parallel transport,
> $$\Gamma_\ell(p)=\Gamma_{\bar c_1}\big(\Gamma_{c_0}(p)\big)=\Gamma_{c_1}^{-1}\big(\Gamma_{c_0}(p)\big)\qquad(\Gamma_{c_2*c_1}=\Gamma_{c_2}\circ\Gamma_{c_1}\text{ and }\Gamma_{\bar c_1}=\Gamma_{c_1}^{-1}).$$
> Now $\Gamma_{c_1}(p)=\Gamma_{c_0}(p)\cdot k$ gives $\Gamma_{c_0}(p)=\Gamma_{c_1}(p)\cdot k^{-1}$, so by equivariance of $\Gamma_{c_1}^{-1}$,
> $$\Gamma_{c_1}^{-1}\big(\Gamma_{c_0}(p)\big)=\Gamma_{c_1}^{-1}\big(\Gamma_{c_1}(p)\cdot k^{-1}\big)=\Gamma_{c_1}^{-1}\big(\Gamma_{c_1}(p)\big)\cdot k^{-1}=p\cdot k^{-1}.$$
> Comparing with $\Gamma_\ell(p)=p\cdot\operatorname{hol}_p(\ell)$ and the free fibre action, $\operatorname{hol}_p(\ell)=k^{-1}$; in particular $k^{-1}\in\operatorname{Hol}$, hence also $k\in\operatorname{Hol}$ (the holonomy group is closed under inverses). Next, from $q=\Gamma_{c_0}(p)\cdot h_0=\Gamma_{c_1}(p)\cdot h_1=\Gamma_{c_0}(p)\cdot(kh_1)$ and the free action, $h_0=kh_1$. Now compare the two candidate values of $f_z(q)$:
> $$\Gamma_{c_1}(p)\cdot z\cdot h_1=\Gamma_{c_0}(p)\cdot k\cdot z\cdot h_1=\Gamma_{c_0}(p)\cdot z\cdot k\cdot h_1=\Gamma_{c_0}(p)\cdot z\cdot h_0,$$
> where the middle equality uses $kz=zk$, valid because $k\in\operatorname{Hol}$ and $z\in Z_G(\operatorname{Hol})$, and the last uses $h_0=kh_1$. So the value via $c_1$ equals the value via $c_0$, and $f_z$ is well-defined.
>
> *Equivariance.* For $g\in G$, using the same curve $c$ for $q$ and $q\cdot g$ (then $q\cdot g=\Gamma_c(p)\cdot(hg)$),
> $$f_z(q\cdot g)=\Gamma_c(p)\cdot z\cdot(hg)=\big(\Gamma_c(p)\cdot z\cdot h\big)\cdot g=f_z(q)\cdot g.$$
>
> *Covers the identity.* $\pi\big(f_z(q)\big)=\pi\big(\Gamma_c(p)\cdot zh\big)=\pi\big(\Gamma_c(p)\big)=\pi(q)$, so $f_z$ maps each fibre to itself and $\bar f_z=\operatorname{id}$.
>
> *Value at $p$ and inverse.* Taking $q=p$ with the constant curve $c\equiv b$ (so $\Gamma_c=\operatorname{id}_{P_b}$ and $h=e$) gives $f_z(p)=p\cdot z$. The same construction with $z$ replaced by $e$ gives $f_e(q)=\Gamma_c(p)\cdot h=q$, so $f_e=\operatorname{id}_P$; and the pointwise formula $f_z(q)=q\cdot(h^{-1}zh)$ shows $f_{z'}\circ f_z=f_{z'z}$ by the same computation as Step 1, so $f_z\circ f_{z^{-1}}=f_e=\operatorname{id}_P=f_{z^{-1}}\circ f_z$. Thus $f_z$ is a bijection with inverse $f_{z^{-1}}$.
>
> *Smoothness.* Fix $q_0\in P$ and $x_0=\pi(q_0)$. Choose a chart $\varphi\colon U\to\mathbb{R}^n$ around $x_0$ with $\varphi(U)$ a ball and a fixed curve $c_0$ from $b$ to $x_0$. For $x\in U$ let $\eta_x$ be the smooth curve $t\mapsto\varphi^{-1}\big((1-t)\varphi(x_0)+t\varphi(x)\big)$ from $x_0$ to $x$, depending smoothly on $x$. Then $s(x):=\Gamma_{\eta_x}\big(\Gamma_{c_0}(p)\big)$ is a smooth local section of $P$ over $U$: parallel transport depends smoothly on the endpoint of the curve because the horizontal lift solves an ordinary differential equation whose right-hand side and initial data depend smoothly on parameters ([[Thm - Existence and Uniqueness of Horizontal Lifts|smooth dependence in the horizontal lift theorem]]). Using the curve $\eta_x*c_0$ from $b$ to $x$ in the construction (in the convention $c_2*c_1$ = "first $c_1$, then $c_2$", so $\eta_x*c_0$ traverses $c_0$ then $\eta_x$), $\Gamma_{\eta_x*c_0}(p)=\Gamma_{\eta_x}\big(\Gamma_{c_0}(p)\big)=s(x)$, so for $q\in\pi^{-1}(U)$ we may write $q=s(\pi(q))\cdot\rho(q)$ with $\rho\colon\pi^{-1}(U)\to G$ smooth (the fibre coordinate relative to the smooth section $s$), and then, by well-definedness,
> $$f_z(q)=s(\pi(q))\cdot z\cdot\rho(q).$$
> The right-hand side is a composition of the smooth maps $q\mapsto(s(\pi(q)),\rho(q))$, right multiplication by $z$, and the smooth $G$-action on $P$, hence smooth on $\pi^{-1}(U)$. As $q_0$ was arbitrary, $f_z$ is smooth; its inverse $f_{z^{-1}}$ is smooth by the same argument, so $f_z$ is a diffeomorphism.
>
> *$f_z$ is a gauge transformation.* We have shown $f_z$ is an equivariant diffeomorphism ($f_z(qg)=f_z(q)g$) covering $\bar f_z=\operatorname{id}$; that is exactly the definition of an element of $\mathcal{G}(P)$.
>
> *$f_z$ preserves $\omega$.* We show $f_z$ maps $\omega$-horizontal curves to $\omega$-horizontal curves, then conclude $f_z^*\omega=\omega$. Let $\tilde\gamma\colon[0,1]\to P$ be an $\omega$-horizontal lift of a curve $\gamma$ in $M$; fix a curve $c$ from $b$ to $\gamma(0)$. For each $t$, the concatenation $\gamma|_{[0,t]}*c$ runs from $b$ to $\gamma(t)$, and $\Gamma_{\gamma|_{[0,t]}*c}(p)=\Gamma_{\gamma|_{[0,t]}}\big(\Gamma_c(p)\big)=:\sigma(t)$, where $\sigma$ is the $\omega$-horizontal lift of $\gamma$ with $\sigma(0)=\Gamma_c(p)$. Both $\tilde\gamma$ and $\sigma$ are horizontal lifts of $\gamma$; the horizontal lift through $\sigma(0)\cdot h_0$, where $h_0$ is defined by $\tilde\gamma(0)=\sigma(0)\cdot h_0$, is $\sigma\cdot h_0$ by equivariance, and it agrees with $\tilde\gamma$ at $t=0$, so by uniqueness $\tilde\gamma(t)=\sigma(t)\cdot h_0$ for all $t$; in particular the fibre coordinate $h(t)\equiv h_0$ is constant. Therefore, by the construction of $f_z$ with the curve $\gamma|_{[0,t]}*c$,
> $$f_z\big(\tilde\gamma(t)\big)=\sigma(t)\cdot z\cdot h_0=\sigma(t)\cdot(zh_0).$$
> The curve $t\mapsto\sigma(t)$ is $\omega$-horizontal, and right translation by the fixed element $zh_0$ carries $\omega$-horizontal curves to $\omega$-horizontal curves, because the horizontal distribution is $G$-invariant, $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$ giving $dR_g(H)=H$ ([[Def - Connection on a Principal Bundle|$G$-invariance of the horizontal distribution]]). Hence $t\mapsto f_z(\tilde\gamma(t))=\sigma(t)\cdot(zh_0)$ is $\omega$-horizontal; that is, $f_z\circ\tilde\gamma$ is horizontal. Consequently $df_z$ maps every horizontal velocity to a horizontal velocity, so $df_z(H_q)\subseteq H_{f_z(q)}$, and by the dimension count of **Lemma 2** (with the roles of the two connections read off), $df_z(H_q)=H_{f_z(q)}$: the connection $f_z^*\omega$ (a genuine connection, since $f_z\in\operatorname{Aut}(P)$, by the gauge-action theorem) has the same horizontal distribution as $\omega$, namely $\ker(f_z^*\omega)_q=df_z^{-1}(H_{f_z(q)})=H_q=\ker\omega_q$. Two principal connections with the same horizontal distribution are equal: on the vertical part $V_q$ both send $\xi_P(q)\mapsto\xi$ (the reproducing property $\omega(\xi_P)=\xi$ holds for every connection form), and on the horizontal part $H_q=\ker$ both vanish, and $T_qP=H_q\oplus V_q$; so $(f_z^*\omega)_q=\omega_q$ for every $q$, i.e. $f_z^*\omega=\omega$. Thus $f_z\in\mathcal{S}$.
>
> Finally $\Phi(f_z)=z$ because $f_z(p)=p\cdot z$. Hence every $z\in Z_G(\operatorname{Hol})$ is in the image of $\Phi$, proving surjectivity onto $Z_G(\operatorname{Hol})$.
>
> **Step 5 — assemble.** By Steps 1–4, $\Phi\colon\mathcal{S}\to Z_G(\operatorname{Hol})$ is a bijective group homomorphism, hence a group isomorphism:
> $$\operatorname{Stab}(\omega)=\mathcal{S}\ \cong\ Z_G\big(\operatorname{Hol}_p(\omega)\big).$$
>
> **Step 6 — independence of the base point.** Replacing $p$ by $p\cdot g$ ($g\in G$) replaces the holonomy group by $\operatorname{Hol}_{p\cdot g}(\omega)=g^{-1}\operatorname{Hol}_p(\omega)\,g$ (holonomy at a shifted point, from the holonomy definition), hence the centraliser by $Z_G(g^{-1}\operatorname{Hol}_p(\omega)\,g)=g^{-1}Z_G(\operatorname{Hol}_p(\omega))\,g$, which is isomorphic to $Z_G(\operatorname{Hol}_p(\omega))$ via conjugation by $g$. Since $\operatorname{Stab}(\omega)$ is defined intrinsically (without reference to $p$), the isomorphism class of the centraliser is independent of the choice of $p\in P_b$; and as $M$ is connected, transporting along a curve from $b$ to another base point $b'$ conjugates the holonomy likewise, so the class is independent of $b$ too. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian holonomy and the de Rham decomposition.** Take $P=\operatorname{Fr}(TM)$, the orthonormal frame bundle of a Riemannian manifold, with $\omega$ the Levi-Civita connection and $G=O(n)$. The corollary says the stabiliser of $\omega$ inside the gauge group is the centraliser of the Riemannian holonomy group $\operatorname{Hol}_p\subseteq O(n)$. When the holonomy is reducible — the tangent bundle splits into parallel subbundles — the centraliser is a product of orthogonal groups, and the reader can match this to the block structure of the de Rham splitting. The application is non-obvious because it recovers a purely metric decomposition (parallel distributions) from a gauge-theoretic stabiliser computation.

**Constant-holonomy connections and character varieties.** For a flat connection on a bundle over a surface, the holonomy group is the image of the monodromy representation $\rho\colon\pi_1(\Sigma)\to G$ (chapter §5.4). The corollary then identifies the stabiliser of the flat connection with $Z_G(\operatorname{im}\rho)$, the centraliser of the image of the representation. This is exactly the isotropy that makes the character variety $\operatorname{Hom}(\pi_1(\Sigma),G)/G$ singular at reducible representations, and the exercise is to see that freeness of the reduced gauge action corresponds to passing to *framed* (pointed) representations, where $G$ acts freely on the irreducible ones. The theorem applies because a flat connection is a connection like any other; the non-obviousness is that its stabiliser is computed by a finite group-theoretic centraliser rather than by any analysis.

**Physics: residual gauge symmetry of a background field.** In Yang–Mills theory a chosen background gauge field $\omega$ has a residual gauge symmetry group — the gauge transformations leaving it fixed — which is the stabiliser $\operatorname{Stab}(\omega)$. The corollary computes it as the centraliser of the holonomy, so for a genuinely non-abelian background (holonomy filling $SU(n)$) only the constant central transformations survive, whereas a background reducible to a $U(1)$ subgroup retains a large residual symmetry. The exercise is to reconcile this with the counting of would-be Goldstone / ghost modes in the physics literature; the theorem applies verbatim, and the non-obvious point is that the "unbroken subgroup" of the physicists is precisely a centraliser of holonomy.

---

# Bridges

- **From the horizontal lift theorem to rigidity.** The entire argument is built on one construction from §5.1: the unique horizontal lift of a curve through a prescribed point, and its equivariance. The bridge is that preserving the connection one-form is the same as preserving the horizontal distribution (Lemma 2), which turns the static hypothesis $f^*\omega=\omega$ into the dynamic statement that $f$ intertwines parallel transport (Lemma 3); the uniqueness of lifts then makes $f$ rigid. This is the same mechanism by which parallel transport pins down a connection: nothing that preserves the transport can wiggle.

- **To the irreducible quotient $\mathcal{B}^*$.** Combining the corollary with the notion of an irreducible connection (holonomy whose centraliser is only the centre) shows that $\mathcal{G}(P)/Z(G)$ acts freely on the irreducible connections $\mathcal{A}^*(P)$. Together with the properness of the action and the Banach-manifold model built in chapters IX and XI, this makes $\mathcal{B}^*(P)=\mathcal{A}^*(P)/\mathcal{G}(P)$ a smooth (infinite-dimensional) manifold — the arena in which the Yang–Mills and Seiberg–Witten moduli spaces are carved out as finite-dimensional cut-out subsets. The bridge is: freeness (this page) $+$ properness $+$ slice theorem $\Rightarrow$ smooth quotient.

- **To reducibles and the singularities of the moduli space.** When the holonomy sits in a proper subgroup, the centraliser exceeds the centre, the stabiliser jumps, and the corresponding point of $\mathcal{B}(P)$ is not a manifold point but a cone. Donaldson's diagonalisation theorem (chapter XIII) counts exactly these reducible points; the bridge from this page is that the corollary *identifies and computes* the stabiliser at each reducible, so the local model near it (a cone on $\mathbb{CP}^2$ in the $SU(2)$ case, where the stabiliser is a circle) can be written down.

- **To framed moduli spaces.** The proposition says the reduced gauge group acts freely, so the framed configuration space $\mathcal{A}(P)/\mathcal{G}_b(P)$ has no isotropy whatever. This is the technical foundation of the framed moduli spaces that appear in Haydys's §1 scheme and in the ADHM description of instantons: by adding the finite-dimensional framing datum one trades a singular quotient for a smooth one, at the cost of a residual $G$-action (the framing rotations) that one later quotients or keeps as extra structure.

---

# Unlocked by This

> [!tip] Irreducible Connections and $\mathcal{B}^*$ *(from Yang–Mills theory, chapter VII)*
> A connection is **irreducible** when its holonomy centraliser is just the centre $Z(G)$. By the corollary this is the same as saying its stabiliser in $\mathcal{G}(P)$ is the smallest possible, so the effective gauge group acts freely on the irreducibles and the quotient $\mathcal{B}^*=\mathcal{A}^*/\mathcal{G}$ is a smooth manifold. See the forthcoming **Def - Irreducible Connection** and **Thm - The Irreducible Configuration Space is a Banach Manifold**.

> [!tip] Stabiliser of a Connection is the Centraliser of its Holonomy *(exercise, §5.3)*
> The corollary is drilled in [[Ex - Stabiliser of a Connection is the Centraliser of its Holonomy]]: prove $\operatorname{Stab}(\omega)\cong Z_G(\operatorname{Hol}_p(\omega))$ in full for connected $M$, then deduce that a $U(1)$-connection always has stabiliser $U(1)$ (constant gauge transformations) while an $SU(2)$-connection with holonomy all of $SU(2)$ has stabiliser $\{\pm\mathbf 1\}$.
