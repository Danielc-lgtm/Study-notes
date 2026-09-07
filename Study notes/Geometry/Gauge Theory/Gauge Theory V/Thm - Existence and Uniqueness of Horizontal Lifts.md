---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Horizontal Subspace and Horizontal Lift"
  - "Def - Local Connection Form and Gauge Potential"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Thm - Existence and Uniqueness of Integral Curves"
  - "Def - The Maurer-Cartan Form"
  - "Def - Connection on a Principal Bundle"
  - "Def - Principal G-Bundle"
  - "Def - Fundamental Vector Field of a Group Action"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a smooth [[Def - Principal G-Bundle|principal $G$-bundle]]: $G$ is a Lie group with Lie algebra $\mathfrak{g}=T_eG$, acting on $P$ on the **right** by $R_g(p)=p\cdot g$, freely and transitively on each fibre $P_m=\pi^{-1}(m)$. The fibre $P_m$ is therefore a $G$-torsor: for any two points $q,q'\in P_m$ there is a **unique** $g\in G$ with $q'=q\cdot g$. We fix a [[Def - Connection on a Principal Bundle|connection]] $\omega\in\Omega^1(P;\mathfrak{g})$, a $\mathfrak{g}$-valued $1$-form satisfying the two axioms $\omega(\xi_P)=\xi$ for every $\xi\in\mathfrak{g}$ (axiom C1) and $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$ (axiom C2). Here $\xi_P$ is the [[Def - Fundamental Vector Field of a Group Action|fundamental vector field]] of $\xi$, namely $\xi_P(p)=\frac{d}{dt}\big|_{t=0}\,p\cdot\exp(t\xi)$, and $\operatorname{Ad}_g\colon\mathfrak{g}\to\mathfrak{g}$ is the adjoint representation, $\operatorname{Ad}_gX=gXg^{-1}$ for a matrix group. The **horizontal distribution** is $H:=\ker\omega$, so that $T_pP=H_p\oplus V_p$ with $V_p=\ker(d\pi_p)$ the vertical space; this is the content of [[Def - Horizontal Subspace and Horizontal Lift|the horizontal subspace]]. A tangent vector $v\in T_pP$ is **horizontal** if $v\in H_p$, equivalently $\omega(v)=0$.

A **curve** $c\colon I\to M$ is a map from a (possibly unbounded) interval $I\subseteq\mathbb{R}$; it is *piecewise smooth* if it is continuous and there is a locally finite partition of $I$ on each closed piece of which $c$ is $C^\infty$. We write $\dot c(t)=dc_t(\tfrac{d}{dt})\in T_{c(t)}M$ for its velocity. A **horizontal lift** of $c$ through $p\in P_{c(t_0)}$ is a curve $\tilde c\colon I\to P$ with $\pi\circ\tilde c=c$, with $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ wherever $\dot{\tilde c}$ is defined, and with $\tilde c(t_0)=p$; this is [[Def - Horizontal Subspace and Horizontal Lift|the horizontal lift]] whose existence and uniqueness we prove.

Over a trivialising open set $U_\alpha\subseteq M$ we fix a local section $s_\alpha\colon U_\alpha\to P$ (one exists precisely because $P|_{U_\alpha}$ is trivial, by [[Thm - Sections of a Principal Bundle and Triviality|the equivalence of sections and trivialisations]]) and write $A_\alpha:=s_\alpha^*\omega\in\Omega^1(U_\alpha;\mathfrak{g})$ for the [[Def - Local Connection Form and Gauge Potential|local connection form]] (gauge potential). The **left Maurer–Cartan form** $\theta\in\Omega^1(G;\mathfrak{g})$ of [[Def - The Maurer-Cartan Form|the Maurer–Cartan form]] is $\theta(w)=dL_{g^{-1}}(w)$ for $w\in T_gG$, where $L_g,R_g\colon G\to G$ denote left and right translation *within $G$*; for a matrix group $\theta=g^{-1}\,dg$. For $q\in P$ we write $L_q\colon G\to P$, $L_q(g)=q\cdot g$, for the **orbit map**; its differential at the identity is $d(L_q)_e(\xi)=\xi_P(q)$.

> [!warning] Convention: two source formulations
> Bär (§2.6, Lemma 2.6.1) states the theorem for the horizontal lift $\tilde c$ of a curve on the *principal* bundle $P$; this is the form we adopt and prove in full generality. Haydys (§3.3.1) states the parallel-transport case directly on an associated *vector* bundle $E$: in a trivialisation of the pullback $\gamma^*E$ over the interval, a parallel section solves the linear ordinary differential equation $\dot s+A(t)s(t)=0$, and its global solvability on $[0,1]$ is "the main theorem of ordinary differential equations". The two are the same statement: the principal ordinary differential equation (2.9) below, read in the standard representation of a matrix group, is exactly Haydys' $\dot s+A(t)s=0$. Where Haydys writes the trivialised connection as $\tfrac{d}{dt}+B(t)\,dt$ and then writes the equation with the letter $A$, the two letters denote the same matrix-valued coefficient — a typographical slip ($A=B$); we use a single symbol $A_\alpha(\dot c)$ throughout.

> [!warning] Convention: a source typo
> Bär's condition (i) is printed as "$c=\tilde c\circ\pi$", which does not typecheck ($\tilde c\circ\pi$ is a self-map of $P$). The intended and correct condition is $c=\pi\circ\tilde c$, i.e. $\tilde c$ is a lift of $c$; we use the corrected form.

---

# Statement

> **Theorem (Existence and uniqueness of horizontal lifts).** Let $\pi\colon P\to M$ be a principal $G$-bundle with a connection $\omega$, let $c\colon I\to M$ be a piecewise smooth curve on an interval $I\subseteq\mathbb{R}$, fix $t_0\in I$ and a point $p\in P_{c(t_0)}$. Then:
> 1. **(Existence and uniqueness.)** There is a unique piecewise smooth curve $\tilde c\colon I\to P$ with
>    $$\pi\circ\tilde c=c,\qquad \dot{\tilde c}(t)\in H_{\tilde c(t)}\ \text{ for all }t,\qquad \tilde c(t_0)=p.$$
>    This $\tilde c$ is the horizontal lift of $c$ through $p$.
> 2. **(Global existence.)** The lift $\tilde c$ is defined on *all* of $I$; it does not escape the total space in finite time.
> 3. **(Equivariance.)** For every $g\in G$, the curve $\tilde c\cdot g\colon t\mapsto\tilde c(t)\cdot g$ is the horizontal lift of $c$ through $p\cdot g$.

The local reduction underlying the proof is the first-order ordinary differential equation, on a subinterval $I'\subseteq I$ with $c(I')\subseteq U_\alpha$ and $\tilde c(t)=s_\alpha(c(t))\cdot h(t)$,
$$\dot h(t)=-\,dR_{h(t)}\big(A_\alpha(\dot c(t))\big),\tag{2.9}$$
where $R_{h}\colon G\to G$ is right translation and $A_\alpha=s_\alpha^*\omega$; for a matrix group $G\subseteq GL(n;\mathbb{K})$ this is the linear equation
$$\dot h(t)=-\,A_\alpha(\dot c(t))\,h(t).\tag{2.9$'$}$$

---

# Motivation

Everything one does with a connection on a principal bundle — parallel transport, holonomy, the monodromy of a flat connection, the free action of the reduced gauge group — rests on being able to *drag a point of the total space along a curve in the base while staying horizontal*. The connection prescribes, at every point $p\in P$, which infinitesimal directions count as "not moving within the fibre": the horizontal ones. Given a curve $c$ downstairs and a starting point $p$ upstairs, the horizontal lift is the unique way to trace out a curve $\tilde c$ upstairs that always moves horizontally and always sits over $c$. It is the geometric object that turns the *infinitesimal* datum of a connection (a choice of horizontal directions) into a *finite* datum (a rule transporting whole fibres from one point of $M$ to another).

The question the theorem answers is whether this dragging is well defined and unobstructed. Three things could go wrong, and the theorem says none of them do. First, existence: does a horizontal curve over $c$ starting at $p$ exist at all? Second, uniqueness: could there be two different horizontal lifts through the same $p$, so that "drag $p$ along $c$" is ambiguous? Third — and this is the subtle one — global existence: even granting a lift for a short time, could it run off to infinity in the fibre before $c$ finishes, leaving the transport undefined past some interior time? For a non-compact structure group such as $GL(n;\mathbb{R})$ the fibre coordinate lives in a non-compact space, and finite-time escape is a genuine a priori danger that the usual local existence theorem for ordinary differential equations does not rule out.

The mechanism that resolves all three is a single observation. In a local trivialisation the lift is forced to have the form $\tilde c(t)=s_\alpha(c(t))\cdot h(t)$, where the only freedom is the fibre coordinate $h(t)\in G$; horizontality then becomes a first-order ordinary differential equation (2.9) for $h$, driven by the local connection form evaluated along the curve. Existence and uniqueness of the lift *are* existence and uniqueness for this ordinary differential equation, and global existence is the statement that its solution never blows up — which we establish, for every Lie group $G$, by an equivariance argument that no linearity is required for.

The associated-bundle shadow of this is worth keeping in view, because it is the version most often met first. On a vector bundle $E=P\times_\rho V$ with the induced connection $\nabla$, a section parallel along $c$ satisfies, in any trivialisation of the pullback bundle over the interval, the linear ordinary differential equation $\dot s+A(t)s=0$ (Haydys §3.3.1); because $[0,1]$ is contractible the pullback bundle is trivial, so such a trivialisation always exists, and the "main theorem of ordinary differential equations" gives a unique solution on the whole interval. That linear equation is precisely (2.9$'$) read in the representation $\rho$, and the reader who has met parallel transport on a vector bundle has already met this theorem in that special case. The content added here is that the same conclusion holds on the principal bundle for an arbitrary — possibly non-abelian, possibly non-matrix — structure group.

We assume the reader is fluent with connections on principal bundles (the two axioms C1, C2 and the horizontal distribution $H=\ker\omega$), with the free transitive right action on fibres, and with the local existence and uniqueness theorem for ordinary differential equations on manifolds in the form of [[Thm - Existence and Uniqueness of Integral Curves|the existence and uniqueness of integral curves]]. Everything else is built here.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is "a principal connection $\omega$ and a piecewise smooth curve". The connection is often not handed to us as a $\mathfrak{g}$-valued $1$-form; recognising the disguises is what lets the theorem be applied.

The first disguised source is **a $G$-invariant horizontal distribution given geometrically**, that is, a smooth field $p\mapsto H_p\subseteq T_pP$ of complements to the vertical spaces with $H_{pg}=dR_g(H_p)$, presented without any $1$-form. The bridge is that such a distribution *is* a connection: define $\omega_p$ to be the projection $T_pP\to V_p\cong\mathfrak{g}$ along $H_p$, followed by the canonical isomorphism $V_p\cong\mathfrak{g}$, $\xi_P(p)\mapsto\xi$; one checks C1 and C2 from the invariance of $H$, so $\ker\omega=H$ and the theorem applies verbatim. The step is non-obvious because a "distribution of planes" looks like weaker data than a "Lie-algebra-valued form", yet the invariance recovers the form exactly. *Example problem:* on the Hopf bundle $S^3\to S^2$, take $H_p$ to be the orthogonal complement of the fibre for the round metric; this is $U(1)$-invariant, hence a connection, and its horizontal lifts of great circles are the object one actually computes.

The second disguised source is **a covariant derivative $\nabla$ on a vector bundle $E$**, with no principal bundle in sight. The bridge runs through the frame bundle: $\nabla$ determines a connection on the frame bundle $\operatorname{Fr}(E)$ whose horizontal lift of $c$ is exactly the moving frame that is $\nabla$-parallel along $c$, and $E\cong\operatorname{Fr}(E)\times_{\rho_{\mathrm{std}}}\mathbb{K}^n$ recovers $E$ as an associated bundle. So a theorem stated only in terms of a covariant derivative on sections is really this theorem on $\operatorname{Fr}(E)$. The non-obviousness is that "differentiating sections" and "lifting curves horizontally" are the same operation seen through the frame bundle. *Example problem:* the parallel transport of a tangent vector on a Riemannian manifold along a geodesic is the horizontal lift of that geodesic in the orthonormal frame bundle.

The third disguised source is **a family of local gauge potentials $A_\alpha\in\Omega^1(U_\alpha;\mathfrak{g})$ obeying the transformation rule** $A_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha+g_{\alpha\beta}^*\theta$ across overlaps. The bridge is that such a compatible family patches to a single global connection form $\omega$ on $P$ (this is exactly the content of the gauge-transformation law for connection forms). Given only the local potentials, one can therefore still speak of *the* horizontal lift, and solve (2.9) chart by chart, patching by the theorem's uniqueness clause. The step is non-obvious because the potentials are frame-dependent and look like different objects in different charts; the transformation rule is precisely the compatibility that makes them one connection. *Example problem:* a Yang–Mills field is usually specified by its potentials $A_\mu$ in coordinate patches, and computing a Wilson line is solving (2.9$'$) patchwise.

**Targets (Output Amplification).** A single horizontal lift is a curve; combined with further structure it becomes the workhorse constructions of the chapter.

Combine the lift with **the operation of evaluating at the endpoint** of a curve $c\colon[t_0,t_1]\to M$. Sending $p\mapsto\tilde c(t_1)$, where $\tilde c$ is the horizontal lift through $p$, produces the **parallel transport map** $\Gamma(c)\colon P_{c(t_0)}\to P_{c(t_1)}$ of [[Def - Parallel Transport in a Principal Bundle|parallel transport in a principal bundle]]; existence and uniqueness are exactly what make $\Gamma(c)$ a well-defined map, and part 3 (equivariance) is what makes it commute with the right action, $\Gamma(c)\circ R_g=R_g\circ\Gamma(c)$. The payoff is that a connection now transports whole fibres, not just infinitesimal directions.

Combine the lift with **the group structure of loops at a point**. For loops $c$ based at $m$, transitivity of the fibre lets us write $\Gamma(c)(p)=p\cdot\operatorname{hol}_p(c)$ for a unique $\operatorname{hol}_p(c)\in G$; concatenation and reversal of loops turn the set of these elements into the **holonomy group** $\operatorname{Hol}_p(\omega)\subseteq G$ of [[Def - Holonomy Group of a Connection|the holonomy group]]. Here the extra ingredient is the concatenation law for lifts (our Lemma 3), and the payoff is a subgroup of $G$ measuring the curvature seen by the connection.

Combine the lift with **connectedness of the base and the freeness of the action**. If a gauge transformation fixes a connection and fixes one point of a fibre over a base point, then following horizontal lifts of paths out of that point shows it fixes every point, because a gauge transformation preserving $\omega$ preserves horizontal lifts; on a connected base it is therefore the identity. This is the freeness of the action of [[Thm - The Reduced Gauge Group Acts Freely on Connections|the reduced gauge group on connections]]. The extra ingredient is that the base is path-connected, and the payoff is that the quotient $\mathcal{A}/\mathcal{G}_b$ is a reasonable space, the starting point for gauge-theoretic moduli.

There is, finally, a target we mention but do not pursue: parallel transport gives an alternative proof of the homotopy invariance of the isomorphism class of a bundle with connection along a homotopy of maps, by transporting fibres across the homotopy. This route is not needed in the series, which obtains the classification results by other means.

---

# Why Is It True

Strip away the trivialisations and picture the total space $P$ as a bundle of fibres, each a copy of the group $G$, sitting over the base. A connection is a rule that, at each point $p$, tilts a horizontal plane $H_p$ through $p$, transverse to the fibre and moving equivariantly as we slide across the fibre by the group. To lift $c$ horizontally starting at $p$ is to release a bead at $p$ and let it ride over $c$ while always moving *inside these tilted planes* — never straight up or down the fibre unless the planes tell it to. Because at each point exactly one horizontal direction lies over each base direction $\dot c(t)$ (the horizontal plane is a graph over the base tangent space, since $H_p\cap V_p=0$ and $d\pi_p$ maps $H_p$ isomorphically to $T_{c(t)}M$), the bead has no choice about where to go: its motion is completely determined. That is uniqueness, and it is also existence in the small — the determined direction is a vector field, and following it is solving an ordinary differential equation.

Made local, the determined direction is the coefficient of (2.9). Once we fix a section $s_\alpha$, every lift over $c$ reads $\tilde c(t)=s_\alpha(c(t))\cdot h(t)$: the section supplies a reference point in each fibre and $h(t)\in G$ records how far the bead has drifted around the fibre relative to that reference. Horizontality, $\omega(\dot{\tilde c})=0$, splits the velocity into a "the reference point is itself moving" part and a "the bead is drifting" part, and demands that the drift exactly cancel the horizontal component of the reference motion. That cancellation is the equation $\dot h=-dR_h(A_\alpha(\dot c))$: the drift rate of $h$ is the local connection form fed the base velocity. For a matrix group the drift is linear, $\dot h=-A_\alpha(\dot c)h$, which is the parallel-transport equation one meets on vector bundles.

> **Mechanism.** Horizontality is a first-order ordinary differential equation for the fibre coordinate, driven by the local connection form along the curve; existence, uniqueness, and non-escape of its solution are existence, uniqueness, and global definedness of the lift.

The only part that is not immediate from the local ordinary differential equation is that the bead cannot escape to infinity in the fibre in finite time. For a matrix group this is visible: the linear equation (2.9$'$) has solutions bounded by $\|h_0\|\exp(\int\|A\|)$, so nothing blows up on a compact time interval. For a general Lie group the equation is not linear and no such bound is available, but the equivariance of the connection saves us: if a lift were to stop existing at an interior time $t_1$, we could produce a *fresh* horizontal lift on a neighbourhood of $t_1$ (short-time existence, which always holds), slide it around the fibre by the unique group element that makes it agree with the original lift just before $t_1$, and — because a group-translate of a horizontal curve is again horizontal — glue it on to continue the original past $t_1$. The supposed obstruction is dissolved by the group action, not by any estimate. This is the inheritance at the heart of the theorem: the fibre is homogeneous, so "getting stuck" at one point of the fibre is the same as getting stuck at every point, and a lift that exists somewhere near $t_1$ can be moved to exist through $t_1$.

---

# What Makes This Hard

The non-obvious step is **global existence**, and the trap is to think it is free. The elementary existence and uniqueness theorem for ordinary differential equations gives only a *local* solution of (2.9): a solution on some possibly tiny interval around each time. Concluding that the lift exists on all of $I$ requires ruling out finite-time escape of $h(t)$ to infinity in $G$, and for non-compact $G$ this does not follow from local theory — the standard Picard–Lindelöf theorem is silent about it, as Bär explicitly notes (Remark 2.6.2). The common error is to invoke "existence and uniqueness of solutions" and declare the lift global; that is correct only for the linear (matrix-group) case, where an a priori bound prevents escape. The general case needs the equivariance-shift argument, whose one delicate point is that the extending curve must be shown to *agree* with the original on the overlap, which is where uniqueness is used a second time. A secondary difficulty is bookkeeping across trivialising charts and across the break-points of a piecewise smooth curve: one must check that the lifts built on adjacent pieces glue continuously and that the result is independent of the partition chosen.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Reduce horizontality in a trivialising chart to the ordinary differential equation (2.9) for the fibre coordinate; solve that equation globally on each chart-piece (linearly for matrix groups, by an equivariance-shift for general $G$); patch the chart-pieces of a compact subinterval together using uniqueness; exhaust a general interval by compact pieces; and read off the equivariance from the $G$-invariance of the horizontal distribution.

**Subgoal decomposition:**

1. **Local reduction.** On a subinterval $I'$ with $c(I')\subseteq U_\alpha$, write $\tilde c=s_\alpha(c)\cdot h$ and show horizontality $\iff$ equation (2.9).
   - *Hint:* Differentiate $t\mapsto s_\alpha(c(t))h(t)$ with the Leibniz rule for the action; the fibre-drift term is a fundamental vector field, so axiom C1 evaluates it, and axiom C2 evaluates the reference-motion term.
   - *Why needed:* It converts a geometric condition on $P$ into a solvable ordinary differential equation on $G$.

2. **Global solvability of (2.9) on a chart-piece.** Show (2.9) has a unique solution on the whole closed piece for the given initial value.
   - *Hint:* For matrix groups the equation is linear; use Picard iteration and a Grönwall bound. For general $G$, get short-time solutions from the integral-curve theorem and rule out finite-time escape by the equivariance-shift.
   - *Why needed:* This is where global existence lives; it is the only step the local ordinary differential equation theory does not hand you.

3. **Equivariance.** Show that if $\tilde c$ is horizontal then so is $\tilde c\cdot g$, and it lifts $c$ through $p\cdot g$.
   - *Hint:* $\frac{d}{dt}(\tilde c\cdot g)=dR_g(\dot{\tilde c})$ and $H_{pg}=dR_g(H_p)$.
   - *Why needed:* It is part 3 of the theorem and is used inside subgoal 2 for general $G$.

4. **Patching and uniqueness on all of $I$.** Cover a compact subinterval by finitely many chart-pieces, glue the local lifts, exhaust $I$, and prove global uniqueness by a connectedness argument.
   - *Hint:* A Lebesgue number gives a partition with each piece inside one $U_\alpha$; glue by using the endpoint of one lift as the initial point of the next; for uniqueness, the agreement set is nonempty, open, and closed.
   - *Why needed:* It assembles the chart-local results into the global statement for piecewise smooth curves on any interval.

---

# Lemma Decomposition

> [!note]- Lemma 1: Horizontality reduces to the ordinary differential equation (2.9)
> **Statement:** Let $I'\subseteq I$ be a subinterval with $c|_{I'}$ smooth and $c(I')\subseteq U_\alpha$, with local section $s_\alpha$ and $A_\alpha=s_\alpha^*\omega$. A smooth curve $\tilde c\colon I'\to P$ with $\pi\circ\tilde c=c$ has the form $\tilde c(t)=s_\alpha(c(t))\cdot h(t)$ for a unique smooth $h\colon I'\to G$, and $\tilde c$ is horizontal if and only if $h$ solves $\dot h(t)=-dR_{h(t)}\big(A_\alpha(\dot c(t))\big)$ (equation (2.9)). For a matrix group $G\subseteq GL(n;\mathbb{K})$ this reads $\dot h=-A_\alpha(\dot c)\,h$ (equation (2.9$'$)).
>
> **Hint:** Split $\dot{\tilde c}$ by the Leibniz rule for the smooth action into a horizontal-reference part $dR_h(\dot\sigma)$ and a fibre-drift part that is a fundamental vector field; apply $\omega$ and use C1 and C2.
>
> **Why needed:** It is the entire local content of the theorem: it turns "$\dot{\tilde c}$ is horizontal" into an ordinary differential equation for $h$, whose solutions are the lifts.
>
> > [!note]- Full proof
> > **Step 0 — the form of a lift.** Because $\pi\circ\tilde c=c$ and $\tilde c(t)\in P_{c(t)}$ lies in the same fibre as the reference point $\sigma(t):=s_\alpha(c(t))$, and $G$ acts freely and transitively on that fibre (as $P$ is a principal bundle), there is a **unique** $h(t)\in G$ with
> > $$\tilde c(t)=\sigma(t)\cdot h(t)=s_\alpha(c(t))\cdot h(t).$$
> > Smoothness of $h$ follows because $t\mapsto(\sigma(t),\tilde c(t))$ is smooth into the pullback where the free action admits a smooth "division" map $(q,q')\mapsto g$ with $q'=qg$ (available on a principal bundle); we take this smoothness as given from the principal-bundle structure.
> >
> > **Step 1 — differentiate the product.** Fix $t\in I'$ and abbreviate $\sigma=\sigma(t)$, $h=h(t)$. The action map $\mu\colon P\times G\to P$, $\mu(q,g)=q\cdot g$, is smooth, and $\tilde c=\mu\circ(\sigma,h)$. By the Leibniz rule for a smooth map of two arguments,
> > $$\dot{\tilde c}(t)=d\mu_{(\sigma,h)}\big(\dot\sigma(t),\dot h(t)\big)=dR_{h}\big(\dot\sigma(t)\big)+d(L_{\sigma})_{h}\big(\dot h(t)\big)\qquad(\text{freezing the second, then the first argument}),$$
> > where $R_h(q)=q\cdot h$ and $L_\sigma(g)=\sigma\cdot g$ is the orbit map.
> >
> > **Step 2 — the fibre-drift term is a fundamental vector field.** Write $\xi:=dL_{h^{-1}}\big(\dot h(t)\big)=\theta\big(\dot h(t)\big)\in\mathfrak{g}$, the value of the Maurer–Cartan form on $\dot h(t)$ (here $L_{h^{-1}}$ is left translation in $G$). Then $\dot h(t)=d(L^G_{h})_e(\xi)$, where $L^G_h(g)=hg$, and since $L_\sigma\circ L^G_h=L_{\sigma h}$ (both send $g\mapsto\sigma hg$),
> > $$d(L_\sigma)_{h}\big(\dot h(t)\big)=d(L_\sigma\circ L^G_h)_e(\xi)=d(L_{\sigma h})_e(\xi)=\xi_P(\sigma h)=\xi_P(\tilde c(t))\qquad(\text{definition of the fundamental vector field}).$$
> > Applying $\omega$ and using **axiom C1** ($\omega(\xi_P)=\xi$),
> > $$\omega\big(d(L_\sigma)_h(\dot h(t))\big)=\omega\big(\xi_P(\tilde c(t))\big)=\xi=dL_{h^{-1}}\big(\dot h(t)\big).\tag{$*$}$$
> >
> > **Step 3 — the reference-motion term.** Since $\dot\sigma(t)=\frac{d}{dt}s_\alpha(c(t))=d(s_\alpha)_{c(t)}(\dot c(t))$, we have $\omega(\dot\sigma(t))=(s_\alpha^*\omega)(\dot c(t))=A_\alpha(\dot c(t))$. Using **axiom C2** ($R_h^*\omega=\operatorname{Ad}_{h^{-1}}\omega$),
> > $$\omega\big(dR_h(\dot\sigma(t))\big)=(R_h^*\omega)(\dot\sigma(t))=\operatorname{Ad}_{h^{-1}}\big(\omega(\dot\sigma(t))\big)=\operatorname{Ad}_{h^{-1}}\big(A_\alpha(\dot c(t))\big).\tag{$**$}$$
> >
> > **Step 4 — assemble horizontality.** Applying $\omega$ to the Step 1 decomposition and inserting $(*)$ and $(**)$,
> > $$\omega\big(\dot{\tilde c}(t)\big)=\operatorname{Ad}_{h^{-1}}\big(A_\alpha(\dot c(t))\big)+dL_{h^{-1}}\big(\dot h(t)\big).$$
> > Horizontality is $\omega(\dot{\tilde c}(t))=0$ for all $t$, i.e.
> > $$dL_{h^{-1}}\big(\dot h(t)\big)=-\operatorname{Ad}_{h^{-1}}\big(A_\alpha(\dot c(t))\big).$$
> > Apply the linear isomorphism $dL_{h}=\big(dL_{h^{-1}}\big)^{-1}$ to both sides. On the left this gives $\dot h(t)$. On the right, use the identity $dL_h\circ\operatorname{Ad}_{h^{-1}}=dR_h$ on $\mathfrak{g}$, which holds because $\operatorname{Ad}_{h^{-1}}=dL_{h^{-1}}\circ dR_{h}$ at $e$ (differentiate the conjugation $c_{h^{-1}}=L_{h^{-1}}\circ R_{h}$), whence $dL_h\circ\operatorname{Ad}_{h^{-1}}=dL_h\circ dL_{h^{-1}}\circ dR_h=dR_h$. Therefore
> > $$\dot h(t)=-dR_{h(t)}\big(A_\alpha(\dot c(t))\big),$$
> > which is (2.9). Conversely, every step is an equivalence, so a solution of (2.9) yields a horizontal $\tilde c$.
> >
> > **Step 5 — the matrix case.** If $G\subseteq GL(n;\mathbb{K})$ is a matrix group, right translation $R_h(g)=gh$ is the restriction of a linear map, so $dR_h(X)=Xh$ for $X\in\mathfrak{g}\subseteq\operatorname{Mat}(n;\mathbb{K})$. Hence (2.9) becomes $\dot h=-A_\alpha(\dot c)\,h$, which is (2.9$'$). Equivalently $h^{-1}\dot h=\theta(\dot h)=-\operatorname{Ad}_{h^{-1}}A_\alpha(\dot c)=-h^{-1}A_\alpha(\dot c)h$, the same equation. This is exactly the parallel-transport equation $\dot s+A(t)s=0$ read in the standard representation. $\blacksquare$

> [!note]- Lemma 2: Global existence and uniqueness of the solution of (2.9) on a chart-piece
> **Statement:** Let $[a,b]\subseteq I$ be compact with $c|_{[a,b]}$ smooth and $c([a,b])\subseteq U_\alpha$. For every $t_\ast\in[a,b]$ and $h_\ast\in G$ there is a unique smooth solution $h\colon[a,b]\to G$ of (2.9) with $h(t_\ast)=h_\ast$; in particular the solution does not leave $G$ in finite time.
>
> **Hint:** Local existence and uniqueness come from the integral-curve theorem applied to the smooth time-dependent vector field defining (2.9). Rule out finite-time escape by the equivariance-shift argument (matrix case: a Grönwall bound, in Lemma 2a).
>
> **Why needed:** It supplies the global (whole-piece) lift; this is the step where the theorem goes beyond elementary local ordinary differential equation theory.
>
> > [!note]- Full proof
> > **Step 0 — recast as an integral curve.** The right-hand side of (2.9) is $F(t,h):=-dR_h\big(A_\alpha(\dot c(t))\big)\in T_hG$. Because $c|_{[a,b]}$ is smooth, $t\mapsto A_\alpha(\dot c(t))\in\mathfrak{g}$ is smooth, and $(t,h)\mapsto dR_h(X)$ is smooth in $(h,X)$; hence $F$ is smooth in $(t,h)$. Define the smooth vector field $Y$ on the manifold $J\times G$, where $J$ is an open interval containing $[a,b]$ in $I$, by $Y(t,h)=\big(1,\,F(t,h)\big)\in\mathbb{R}\times T_hG$. A curve $t\mapsto(t,h(t))$ is an integral curve of $Y$ if and only if $h$ solves (2.9).
> >
> > **Step 1 — local existence and uniqueness.** By [[Thm - Existence and Uniqueness of Integral Curves|the existence and uniqueness of integral curves]] — for a smooth vector field $Y$ on a manifold and any initial point there is an open interval on which a unique integral curve with that initial point exists — there is, for the initial point $(t_\ast,h_\ast)$, a maximal open interval $(t_-,t_+)\ni t_\ast$ (relative to $J$) carrying a unique solution $h$ of (2.9) with $h(t_\ast)=h_\ast$. Uniqueness on overlaps is part of that theorem.
> >
> > **Step 2 — no escape on the right.** Suppose, for contradiction, that $t_+\le b$, so the maximal solution fails to reach past $t_+$ while $t_+$ is still interior to $[a,b]$. Consider the base point $c(t_+)\in U_\alpha$. Pick any point $q_+\in P_{c(t_+)}$ and, applying **Step 1 to the initial point $(t_+,\,\text{fibre coordinate of }q_+)$**, obtain a horizontal lift $\hat c$ of $c$ — equivalently a solution $\hat h$ of (2.9) — defined on an open interval $(t_+-\delta,t_+ +\delta)$ for some $\delta>0$ (intersected with $J$). Choose $\tau\in(t_+-\delta,t_+)\cap(t_-,t_+)$, a time at which **both** the maximal lift $\tilde c(\tau)=s_\alpha(c(\tau))h(\tau)$ and $\hat c(\tau)$ are defined; both lie in the fibre $P_{c(\tau)}$. Because the action is free and transitive on the fibre, there is a unique $g\in G$ with
> > $$\tilde c(\tau)=\hat c(\tau)\cdot g.$$
> > By **Lemma 4** (equivariance), $\bar c:=\hat c\cdot g$ is again a horizontal lift of $c$ on $(t_+-\delta,t_+ +\delta)$, and $\bar c(\tau)=\hat c(\tau)\cdot g=\tilde c(\tau)$. On the overlap $(t_+-\delta,t_+)\cap(t_-,t_+)$ the curves $\bar c$ and $\tilde c$ are two horizontal lifts of $c$ agreeing at $\tau$; by the uniqueness of Step 1 they coincide there. Hence $\bar c$ agrees with $\tilde c$ up to $t_+$ and is defined past $t_+$, so the curve equal to $\tilde c$ before $\tau$ and to $\bar c$ after is a solution of (2.9) extending $h$ strictly beyond $t_+$. This contradicts the maximality of $t_+$. Therefore $t_+>b$, and symmetrically $t_-<a$, so the solution exists on all of $[a,b]$.
> >
> > **Step 3 — the solution stays in $G$.** By construction $h$ takes values in the manifold $G$ throughout its interval of definition (it is an integral curve on $J\times G$); there is no ambient space to escape into, and Step 2 shows the interval covers $[a,b]$. This proves global existence and uniqueness on the piece.
> >
> > > [!note]- Lemma 2a: the matrix case by Picard iteration and Grönwall (concrete reproof and a priori bound)
> > > **Statement:** For $G\subseteq GL(n;\mathbb{K})$ and continuous $A\colon[a,b]\to\operatorname{Mat}(n\times n;\mathbb{K})$, the linear initial value problem $\dot h(t)=-A(t)h(t)$, $h(t_\ast)=h_\ast$, has a unique solution on all of $[a,b]$, and it obeys the bound $\|h(t)\|\le\|h_\ast\|\exp\!\big(\int_{t_\ast}^{t}\|A(\tau)\|\,d\tau\big)$ in any submultiplicative matrix norm; if $h_\ast\in G$ then $h(t)\in G$ for all $t$.
> > >
> > > *Proof.* Write $M:=\sup_{[a,b]}\|A\|<\infty$ (a continuous function on a compact interval is bounded) and $L:=b-a$. Recast the problem as the integral equation $h(t)=h_\ast-\int_{t_\ast}^t A(\tau)h(\tau)\,d\tau$, and define the Picard iterates $h_0(t):=h_\ast$ and $h_{k+1}(t):=h_\ast-\int_{t_\ast}^t A(\tau)h_k(\tau)\,d\tau$ in the Banach space $C^0([a,b];\operatorname{Mat}(n;\mathbb{K}))$ with the supremum norm. By induction on $k$, for all $t\in[a,b]$,
> > > $$\big\|h_{k+1}(t)-h_k(t)\big\|\le\frac{\big(M\,|t-t_\ast|\big)^{k+1}}{(k+1)!}\,\|h_\ast\|,$$
> > > the base case being $\|h_1(t)-h_0(t)\|=\|\int_{t_\ast}^t A h_\ast\|\le M|t-t_\ast|\,\|h_\ast\|$ and the inductive step following from $\|h_{k+1}(t)-h_k(t)\|\le\int_{t_\ast}^t\|A(\tau)\|\,\|h_k(\tau)-h_{k-1}(\tau)\|\,d\tau$ (**since** the norm is submultiplicative and integration is monotone). Because $\sum_k (ML)^{k+1}/(k+1)!=e^{ML}-1<\infty$, the series $\sum_k(h_{k+1}-h_k)$ converges absolutely and uniformly on $[a,b]$ (**by the Weierstrass $M$-test**), so $h_k\to h$ uniformly to a continuous limit; passing to the limit in the integral equation (**licensed by uniform convergence, which permits the interchange of limit and integral** on the compact interval) shows $h$ solves the integral equation, hence is $C^1$ and solves the differential equation on all of $[a,b]$.
> > >
> > > *Uniqueness and the bound.* If $h,\hat h$ both solve the problem, put $u(t):=\|h(t)-\hat h(t)\|$; then $u(t)\le\int_{t_\ast}^t M\,u(\tau)\,d\tau$ for $t\ge t_\ast$, and **Grönwall's inequality** (if $u(t)\le\int_{t_\ast}^t M u$, and $u\ge0$ continuous, then $u\equiv0$) gives $u\equiv0$, so $h=\hat h$. The same integral inequality applied to $\|h(t)\|\le\|h_\ast\|+\int_{t_\ast}^t\|A\|\,\|h\|$ yields, by Grönwall, $\|h(t)\|\le\|h_\ast\|\exp(\int_{t_\ast}^t\|A\|)$, the claimed a priori bound; in particular $h$ is bounded on $[a,b]$, confirming no finite-time escape. Finally, the intrinsic solution of (2.9) on $G$ from Lemma 2 coincides with this linear solution on their common interval (both solve (2.9$'$), which has a unique solution); since the intrinsic solution stays in $G$ and the linear solution is global, they agree on all of $[a,b]$, so $h(t)\in G$ throughout. $\square$
>
> The full proof above is complete for every Lie group $G$; Lemma 2a re-establishes the matrix case concretely and supplies the norm bound used later by the Dyson series.

> [!note]- Lemma 3: Patching and global uniqueness for piecewise smooth curves
> **Statement:** Let $c\colon I\to M$ be piecewise smooth, $t_0\in I$, $p\in P_{c(t_0)}$. Then there exists a horizontal lift $\tilde c\colon I\to P$ with $\tilde c(t_0)=p$, it is unique, and it is independent of the choices of partition and trivialising sets used to build it.
>
> **Hint:** Cover a compact subinterval by finitely many chart-pieces via a Lebesgue number; glue the chart-local lifts of Lemma 2 by matching endpoints; exhaust $I$; prove uniqueness by an open–closed connectedness argument.
>
> **Why needed:** Lemmas 1–2 solve the problem inside one trivialising chart on a compact piece; this lemma globalises to arbitrary piecewise smooth curves on any interval.
>
> > [!note]- Full proof
> > **Step 0 — partition a compact subinterval.** Let $[a,b]\subseteq I$ be any compact subinterval containing $t_0$. The images of the trivialising sets, together with the images of the break-points of $c$, cover $c([a,b])$; the open sets $\{c^{-1}(U_\alpha)\}$ cover the compact interval $[a,b]$, so they have a **Lebesgue number** $\lambda>0$: every subinterval of length $<\lambda$ maps into a single $U_\alpha$. Choose a partition $a=r_0<r_1<\dots<r_N=b$ with each $r_{i+1}-r_i<\lambda$ and refined so that every break-point of $c$ is a node $r_i$. Then $c([r_i,r_{i+1}])\subseteq U_{\alpha_i}$ for some index $\alpha_i$, and $c$ is smooth on each $[r_i,r_{i+1}]$.
> >
> > **Step 1 — glue chart-local lifts.** Suppose $t_0=r_j$ for some $j$ (if not, insert it as a node). Build the lift outward from $t_0$. On the piece containing $t_0$, Lemma 2 gives the unique horizontal lift $\tilde c$ with $\tilde c(t_0)=p$; it exists on the whole closed piece. Take the value of $\tilde c$ at the shared endpoint $r_{j+1}$ as the initial point for the next piece $[r_{j+1},r_{j+2}]$, apply Lemma 2 again, and continue to $r_N=b$; proceed symmetrically toward $r_0=a$. The pieces agree at each shared node by construction (the value carried over is the initial condition of the next piece), so the concatenation is a continuous curve $\tilde c\colon[a,b]\to P$. It lifts $c$ (each piece does), it is horizontal on the interior of each piece (Lemma 2), and at an interior node the one-sided velocities are horizontal, so $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ wherever defined. It is smooth on each $[r_i,r_{i+1}]$, hence piecewise smooth.
> >
> > **Step 2 — exhaust $I$.** Write $I$ as an increasing union of compact subintervals $[a_k,b_k]$ with $t_0\in[a_k,b_k]$ and $\bigcup_k[a_k,b_k]=I$. Building the lift on each $[a_k,b_k]$ with initial condition $\tilde c(t_0)=p$ gives curves that agree on overlaps by the uniqueness proved in Step 3; their common extension is a horizontal lift on all of $I$. (If $I$ is compact this step is vacuous.)
> >
> > **Step 3 — global uniqueness.** Let $\tilde c_1,\tilde c_2\colon I\to P$ be horizontal lifts of $c$ with $\tilde c_1(t_0)=\tilde c_2(t_0)=p$. Let $S:=\{t\in I:\tilde c_1(t)=\tilde c_2(t)\}$. Then $S$ is **nonempty** ($t_0\in S$) and **closed** in $I$ (both curves are continuous, so $S$ is the preimage of the diagonal under $t\mapsto(\tilde c_1(t),\tilde c_2(t))$, and the diagonal of the Hausdorff space $P\times P$ is closed). It is also **open**: if $t_\ast\in S$, pick a chart-piece $[r_i,r_{i+1}]$ around $t_\ast$ with $c([r_i,r_{i+1}])\subseteq U_{\alpha_i}$; on it both lifts solve (2.9) with the same value at $t_\ast$, so by the uniqueness in Lemma 2 they coincide on the whole piece, giving a neighbourhood of $t_\ast$ inside $S$. Since $I$ is connected and $S$ is nonempty, open, and closed, $S=I$, so $\tilde c_1=\tilde c_2$.
> >
> > **Step 4 — independence of choices.** Any two admissible partitions have a common refinement (their union of nodes), and any two admissible choices of trivialising sets over a common finer partition produce, on each small piece, horizontal lifts with the same initial value, hence the same lift by Step 3 applied piecewise. Therefore the glued lift depends only on $c$, $t_0$, and $p$. $\blacksquare$

> [!note]- Lemma 4: Equivariance of horizontal lifts
> **Statement:** If $\tilde c\colon I\to P$ is a horizontal lift of $c$ and $g\in G$, then $\tilde c\cdot g\colon t\mapsto\tilde c(t)\cdot g$ is a horizontal lift of $c$, and $(\tilde c\cdot g)(t_0)=\tilde c(t_0)\cdot g$. In particular the horizontal lift through $p\cdot g$ is $\tilde c\cdot g$, where $\tilde c$ is the horizontal lift through $p$.
>
> **Hint:** Right translation preserves fibres and, by axiom C2, preserves the horizontal distribution: $H_{pg}=dR_g(H_p)$.
>
> **Why needed:** It is part 3 of the theorem, and it is the geometric fact that powers the no-escape argument of Lemma 2 (Step 2).
>
> > [!note]- Full proof
> > **Step 0 — invariance of $H$.** For $p\in P$, $g\in G$, and $v\in T_pP$, axiom C2 gives $\omega_{pg}(dR_g v)=(R_g^*\omega)_p(v)=\operatorname{Ad}_{g^{-1}}\big(\omega_p(v)\big)$. Since $\operatorname{Ad}_{g^{-1}}$ is a linear isomorphism of $\mathfrak{g}$, we have $\omega_p(v)=0\iff\omega_{pg}(dR_g v)=0$, that is $v\in H_p\iff dR_g v\in H_{pg}$. Hence $H_{pg}=dR_g(H_p)$: **right translation carries horizontal vectors to horizontal vectors.**
> >
> > **Step 1 — the translate is a horizontal lift.** Set $\bar c:=R_g\circ\tilde c$, so $\bar c(t)=\tilde c(t)\cdot g$. It projects correctly: $\pi(\bar c(t))=\pi(\tilde c(t))=c(t)$ (the right action is fibre-preserving on a principal bundle). Its velocity is $\dot{\bar c}(t)=dR_g\big(\dot{\tilde c}(t)\big)$ (chain rule). Since $\dot{\tilde c}(t)\in H_{\tilde c(t)}$ (as $\tilde c$ is horizontal), Step 0 gives $dR_g(\dot{\tilde c}(t))\in H_{\tilde c(t)g}=H_{\bar c(t)}$, so $\bar c$ is horizontal. Finally $\bar c(t_0)=\tilde c(t_0)\cdot g$.
> >
> > **Step 2 — identification.** Taking $\tilde c$ to be the horizontal lift through $p$ (so $\tilde c(t_0)=p$), $\bar c=\tilde c\cdot g$ is a horizontal lift through $p\cdot g$; by the uniqueness of Lemma 3 it *is* the horizontal lift through $p\cdot g$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\pi\colon P\to M$ be a principal $G$-bundle with connection $\omega$, $c\colon I\to M$ piecewise smooth, $t_0\in I$, $p\in P_{c(t_0)}$. We prove parts 1–3 of the theorem.
>
> **Step 0 — well-posedness of the data.** The fibres of $P$ are $G$-torsors (free transitive right action), so the "fibre coordinate" $h$ in a local trivialisation is unambiguously defined once a local section is fixed; the connection provides, at each point, the horizontal complement $H_p=\ker\omega_p$ with $T_pP=H_p\oplus V_p$, and by axiom C2 this distribution is $G$-invariant (Lemma 4, Step 0). Trivialising sets with local sections exist by [[Thm - Sections of a Principal Bundle and Triviality|the equivalence of local sections and local trivialisations]]. These are the preconditions used below.
>
> **Step 1 — existence and uniqueness on all of $I$ (part 1 and part 2).** By **Lemma 3** there exists a horizontal lift $\tilde c\colon I\to P$ with $\tilde c(t_0)=p$, and it is unique among horizontal lifts through $p$. Lemma 3 builds it by covering compact subintervals with finitely many trivialising chart-pieces (a Lebesgue-number argument), solving the local ordinary differential equation (2.9) on each piece by **Lemma 2**, gluing the pieces by matching endpoints, and exhausting $I$ by compact subintervals; the reduction of horizontality to (2.9) is **Lemma 1**. Crucially, Lemma 2 provides the solution of (2.9) on each *entire* closed piece — this is the global existence asserted in part 2 — either by the equivariance-shift argument valid for every Lie group $G$ or, for a matrix group, by the linear estimate of **Lemma 2a**; in neither case does $\tilde c$ escape $P$ at an interior time. The curve $\tilde c$ is piecewise smooth because it is smooth on each chart-piece $[r_i,r_{i+1}]$ (a solution of the smooth ordinary differential equation (2.9)) and continuous at the finitely many nodes. Global uniqueness is Step 3 of Lemma 3: the set where two lifts through $p$ agree is nonempty, open, and closed, hence all of the connected interval $I$.
>
> **Step 2 — equivariance (part 3).** Let $g\in G$. By **Lemma 4**, the curve $\tilde c\cdot g$ is a horizontal lift of $c$ with $(\tilde c\cdot g)(t_0)=p\cdot g$; by the uniqueness of part 1 it is *the* horizontal lift of $c$ through $p\cdot g$. Thus the horizontal lift through $p\cdot g$ is the right translate by $g$ of the horizontal lift through $p$.
>
> **Conclusion.** For every piecewise smooth curve $c$, every $t_0\in I$, and every $p\in P_{c(t_0)}$, there is one and only one horizontal lift $\tilde c$ of $c$ through $p$; it is defined on all of $I$; and horizontal lifts transform equivariantly under the right action, $\widetilde{c}$ through $pg$ equals $\tilde c\cdot g$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian parallel transport as a horizontal lift (differential geometry).** On a Riemannian manifold, the Levi-Civita parallel transport of a tangent vector along a curve, met classically as the solution of $\frac{\nabla}{dt}V=0$, is the horizontal lift of the curve in the orthonormal frame bundle $\operatorname{Fr}(TM)$ with structure group $O(n)$. The theorem applies because the Levi-Civita connection is a principal connection on $\operatorname{Fr}(TM)$; it is non-obvious because the classical formulation never mentions a bundle over the base, yet the moving orthonormal frame $\tilde c(t)=(e_1(t),\dots,e_n(t))$ is precisely a horizontal lift, and $O(n)$ being compact makes global existence transparent. This connects the theorem to [[Def - Parallel Transport|parallel transport]] and to [[Ex - Parallel Transport around a Geodesic Triangle on the Sphere|the geodesic-triangle computation on the sphere]].

**Adiabatic quantum evolution and Berry phase (mathematical physics).** For a family of Hamiltonians $H(t)$ with a spectral gap, the adiabatic transport of an eigenstate around a loop in parameter space is the horizontal lift in a $U(1)$- (or $U(k)$-) bundle over the parameter manifold, whose connection is the Berry connection; the accumulated Berry phase is the holonomy. The theorem applies because the Berry connection is a principal $U(1)$-connection, and the horizontal-lift equation is the projected Schrödinger equation. The non-obvious point is that a physical evolution law is literally the ordinary differential equation (2.9$'$), so the mathematical guarantee of a unique global lift is the physical statement that the adiabatic phase is well defined.

**Wilson lines in lattice and continuum gauge theory (theoretical physics).** A Wilson line along a path is the path-ordered exponential of the gauge potential, which is exactly the parallel-transport operator obtained by solving (2.9$'$) with $A_\alpha=A_\mu\,dx^\mu$. Applying the theorem across coordinate patches (using the third disguised source above) shows the Wilson line is a well-defined element of $G$ independent of how the path is broken into pieces — a fact physicists use implicitly. The subtlety it addresses is that for a non-compact gauge group the ordered exponential could in principle fail to exist over a finite path; the theorem certifies it always does. This connects to [[Def - Path-Ordered Exponential|the path-ordered exponential]].

---

# Bridges

- **[[Def - Parallel Transport in a Principal Bundle|Parallel transport in a principal bundle]]** — the immediate construction. Fixing the endpoints of $c\colon[t_0,t_1]\to M$ and sending $p\mapsto\tilde c(t_1)$ defines the parallel-transport map $\Gamma(c)\colon P_{c(t_0)}\to P_{c(t_1)}$; existence and uniqueness are what make it a map at all, and Lemma 4 is what makes it $G$-equivariant, $\Gamma(c)\circ R_g=R_g\circ\Gamma(c)$. On an associated vector bundle $E=P\times_\rho V$ this induces the linear parallel transport $[p,v]\mapsto[\Gamma(c)p,v]$, whose trivialised form is Haydys' $\dot s+A(t)s=0$.

- **[[Def - Holonomy Group of a Connection|The holonomy group]]** — built from lifts of loops. For a loop $c$ at $m$, transitivity of the fibre gives $\Gamma(c)(p)=p\cdot\operatorname{hol}_p(c)$ for a unique $\operatorname{hol}_p(c)\in G$; the concatenation law $\Gamma(c_2*c_1)=\Gamma(c_2)\circ\Gamma(c_1)$ (from the gluing of lifts in Lemma 3) makes $\{\operatorname{hol}_p(c)\}$ a subgroup of $G$. The horizontal-lift theorem is the foundation on which the entire holonomy formalism, and the later small-loop expansion "curvature is infinitesimal holonomy", is erected.

- **[[Thm - The Reduced Gauge Group Acts Freely on Connections|Freeness of the reduced gauge group]]** — a rigidity consequence. A gauge transformation fixing $\omega$ preserves horizontal lifts (it maps a horizontal lift of $c$ to a horizontal lift of $c$); if it also fixes one point of the fibre over a base point, then following the horizontal lifts of paths out of that point — which exist and are unique by this theorem — shows it fixes the fibre over every point of a connected base, so it is the identity. Global existence and uniqueness of lifts is exactly the input that propagates "fixes here" to "fixes everywhere".

- **[[Ex - Global Existence for Linear ODEs via Gronwall|Global existence for linear ordinary differential equations]]** — the matrix-group heart of Lemma 2a, isolated as a drill. Grönwall's inequality both forces uniqueness and provides the a priori bound that forbids finite-time escape, which is the special-case reason the horizontal lift is global for a matrix structure group; the general Lie-group case replaces the estimate by the equivariance-shift of Lemma 2.

---

# Unlocked by This

> [!tip] Path-ordered exponential *(from Gauge Theory / Mathematical Physics)*
> Solving (2.9$'$) explicitly for a matrix group leads to the ordered exponential $\mathcal{P}\exp(-\int A)$, whose Dyson-series and ordered-product forms, and whose reduction to $\exp(-\int A)$ in the commuting case, are the content of **[[Def - Path-Ordered Exponential]]** and **[[Thm - The Path-Ordered Exponential Solves the Linear Parallel-Transport Equation]]**. The a priori norm bound of Lemma 2a is exactly what makes the Dyson series converge.

> [!tip] Monodromy of a flat connection *(from Gauge Theory / Topology)*
> When $\omega$ is flat, the horizontal lift of a loop depends only on the loop's homotopy class, so horizontal lifting descends to a representation $\pi_1(M)\to G$; this is the monodromy correspondence of **[[Thm - Flat Connections and Monodromy Representations of the Fundamental Group]]**, and its very first ingredient is the existence and uniqueness proved here.
