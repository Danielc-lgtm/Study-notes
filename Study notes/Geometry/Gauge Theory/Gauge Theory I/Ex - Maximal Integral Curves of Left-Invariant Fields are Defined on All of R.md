---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Lie Group"
  - "Def - Left-Invariant Vector Field"
  - "Def - Integral Curve of a Vector Field"
  - "Thm - Existence and Uniqueness of Integral Curves"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $G$ be a Lie group with identity element $e$, and let $X$ be a left-invariant vector field on $G$. Prove:
$$\text{every maximal integral curve of } X \text{ is defined on all of } \mathbb{R}.$$

Equivalently, prove that **every left-invariant vector field on a Lie group is complete**: its flow is defined for all time. This is Exercise 1.4.1 of Bär's *Gauge Theory* (Potsdam, 2011), and it is the fact that makes the exponential map of a Lie group well-defined, because $\exp(X)$ is by definition the time-one value $\gamma_X(1)$ of the integral curve $\gamma_X$ of $X$ starting at $e$ — a value that only exists if the curve survives to time $1$.

The intended route is an **extension-by-translation** argument. The obstruction to a maximal integral curve reaching all of $\mathbb{R}$ is that it might "run out of time" at a finite endpoint. Left-invariance defeats this obstruction: it manufactures, from a single short integral curve through $e$, an integral curve of the *same fixed length* through every point of $G$. One then translates a copy of this uniform-length curve to the endpoint and glues it on, extending the curve past any purported finite boundary — a contradiction with maximality. Two elementary structural facts carry the argument: that left-translating an integral curve produces another integral curve (because $X$ is left-invariant), and that time-translating an integral curve produces another integral curve (because $X$ is autonomous, i.e. time-independent). Uniqueness of integral curves then lets the two pieces be glued.

**Recall.**

The objects in play are a Lie group, a left-invariant vector field, an integral curve, and the existence–uniqueness theorem for integral curves.

![[Def - Left-Invariant Vector Field#The Definition]]

Write $L_g\colon G\to G$, $L_g(h)=gh$, for **left translation** by $g\in G$; it is a diffeomorphism with inverse $L_{g^{-1}}$, and its differential at a point $h$ is the linear isomorphism $d(L_g)_h\colon T_hG\to T_{gh}G$. A vector field $X$ on $G$ is [[Def - Left-Invariant Vector Field|left-invariant]] when it is $L_g$-related to itself for every $g$, that is
$$X(gh)=d(L_g)_h\big(X(h)\big)\qquad\text{for all }g,h\in G. \tag{LI}$$
In particular, putting $h=e$, a left-invariant field is determined by its single value $X(e)\in T_eG=\mathfrak{g}$ through $X(g)=d(L_g)_e(X(e))$; left-invariant fields are automatically smooth.

![[Def - Integral Curve of a Vector Field#The Definition]]

An [[Def - Integral Curve of a Vector Field|integral curve]] of a vector field $X$ is a smooth curve $\gamma\colon J\to G$, defined on an open interval $J\subseteq\mathbb{R}$, satisfying the autonomous ordinary differential equation
$$\dot\gamma(t)=X\big(\gamma(t)\big)\qquad\text{for all }t\in J. \tag{IC}$$
It is called **maximal** if its interval $J$ is not a proper subinterval of the interval of any other integral curve of $X$ that agrees with it where both are defined; equivalently, $J$ is the maximal interval on which the solution to (IC) with the given initial value exists.

![[Thm - Existence and Uniqueness of Integral Curves#Statement]]

Two consequences of this theorem are used repeatedly below and stated here explicitly. First, **uniqueness**: two integral curves of $X$ that agree at one instant agree on the entire intersection of their domains. Second, **local existence with an initial value**: for every $p\in G$ there is an $\varepsilon>0$ and an integral curve $\theta\colon(-\varepsilon,\varepsilon)\to G$ of $X$ with $\theta(0)=p$.

---

# Convergent Strategy

**Problem class.** This is a *completeness* problem: show that the maximal domain of a flow is all of $\mathbb{R}$. Completeness is *not* automatic — on a general manifold an integral curve can escape to infinity in finite time (the field $\partial_x$ scaled by $x^2$ on $\mathbb{R}$, whose integral curve $t\mapsto 1/(c-t)$ blows up at $t=c$). What one must exploit is extra structure that forbids the escape. Here the structure is the transitive symmetry of a Lie group: $G$ looks the same near every point because left translation carries any point to any other, and it carries $X$ to itself. The recognisable trigger for this whole method is the pairing "*complete field* wanted $+$ *a symmetry group acting transitively and preserving the field*".

**Assumption pattern.** The hypothesis "$X$ is left-invariant" is used in exactly one structural way, isolated in Lemma A below: it guarantees that the diffeomorphism $L_g$ sends integral curves of $X$ to integral curves of $X$. The hypothesis "$G$ is a Lie group" enters only through the smoothness of multiplication (so that $L_g$ is a diffeomorphism and (LI) makes sense) and through the existence of the identity $e$, which serves as the single base point from which one short curve is transported everywhere. No completeness input is assumed; it is what we prove.

**Theorem routing.** The route is: invoke [[Thm - Existence and Uniqueness of Integral Curves|existence–uniqueness]] once at $e$ to obtain a short integral curve $\theta\colon(-\varepsilon,\varepsilon)\to G$ with $\theta(0)=e$; use **left-invariance** (Lemma A) to transport $\theta$ to a length-$2\varepsilon$ integral curve $L_g\circ\theta$ through *any* $g$, giving a *uniform* existence time $\varepsilon$ independent of the starting point; use **time-translation** (Lemma B, valid because (IC) is autonomous) and **uniqueness** (Lemma C, the gluing lemma) to splice such a uniform-length curve onto the end of the maximal curve; conclude by contradiction that the maximal interval has no finite endpoint. Finally, reduce every maximal integral curve to the one through $e$ by a single left translation.

**Key decision point.** The one genuinely non-obvious move is to prove *uniform* local existence — an existence time $\varepsilon$ that works simultaneously at every point of $G$ — rather than a point-dependent one. For a general vector field, uniform existence over a non-compact manifold can fail, and that failure is exactly how finite-time blow-up happens. Left-invariance hands us uniformity for free: one $\varepsilon$ obtained at the single point $e$ propagates to all of $G$ by translation. Once uniformity is in hand, the extension is forced: an integral curve approaching a finite endpoint $b$ still has, at any interior time within $\varepsilon$ of $b$, a fresh integral curve of full length $\varepsilon$ emanating from its current position, and that fresh curve reaches past $b$.

---

# Legal Operations Used

The solution deploys the following operations; when the chapter's topic page is assembled, these are the Legal Operations it will list for §1.4, and the numbering will be reconciled to it.

1. **Transport an integral curve by a symmetry that preserves the field (left-translation of solutions).** Given an integral curve $\gamma$ of the left-invariant field $X$ and any $g\in G$, form $L_g\circ\gamma$; because $X$ is left-invariant, this is again an integral curve of $X$. This is the operation that turns one solution into a whole $G$-indexed family of solutions.

2. **Time-shift an integral curve (autonomy of the equation).** Given an integral curve $\gamma$ of $X$ and a constant $c\in\mathbb{R}$, form $t\mapsto\gamma(t+c)$; because the defining equation (IC) has no explicit time dependence, this is again an integral curve of $X$. This repositions a solution's initial instant without changing its shape.

3. **Glue two integral curves that agree at a point (uniqueness).** If two integral curves take the same value at a common time, [[Thm - Existence and Uniqueness of Integral Curves|uniqueness]] forces them to coincide on the overlap of their domains, so their union is a single integral curve on the union of the domains.

4. **Manufacture uniform local existence from one base-point solution.** Combine operation 1 with a single application of local existence at $e$ to obtain one existence time $\varepsilon>0$ valid at every point of $G$ simultaneously.

5. **Extend a maximal solution to a contradiction.** Splice a uniform-length curve (operations 1–3) onto a maximal curve that is assumed to have a finite endpoint, producing an integral curve on a strictly larger interval and contradicting maximality.

6. **Reduce the general point to the identity by translation.** Prove completeness for the curve through $e$, then obtain every other maximal integral curve as a left translate of it (operation 1), so the conclusion transfers to all of $G$.

---

# Hints

> [!note]- Hint 1
> Completeness cannot come from the general existence–uniqueness theorem alone — that theorem only guarantees *some* interval of existence, possibly tiny and possibly shrinking as the starting point varies. You must use the hypothesis that $X$ is *left-invariant*. Ask: if $\gamma$ is an integral curve of a left-invariant $X$ and you left-translate it by a fixed $g$, is $t\mapsto g\gamma(t)$ still an integral curve?

> [!note]- Hint 2
> Compute $\frac{d}{dt}\big(g\gamma(t)\big)$ by the chain rule and compare it to $X\big(g\gamma(t)\big)$ using the left-invariance identity $X(gh)=d(L_g)_h(X(h))$. You should find they are equal. Conclusion: left translation carries integral curves of $X$ to integral curves of $X$, and it does so *without changing the length of the time interval*. This is the source of *uniform* local existence.

> [!note]- Hint 3
> Apply local existence just once, at the identity, to get an integral curve $\theta\colon(-\varepsilon,\varepsilon)\to G$ with $\theta(0)=e$. Now, for any point $p\in G$, what integral curve of length $2\varepsilon$ starts at $p$? Use Hint 2. You now have a *single* $\varepsilon$ that works at every point.

> [!note]- Hint 4
> Suppose the maximal integral curve $\gamma$ through $e$ were defined only on $(a,b)$ with $b<\infty$. Pick a time $s\in(b-\varepsilon,b)$. At the point $\gamma(s)$ you have (Hint 3) a fresh integral curve of length $2\varepsilon$; time-shift it so that it passes through $\gamma(s)$ at time $s$. It agrees with $\gamma$ at $t=s$. Now use uniqueness to glue. Where does the glued curve reach? Since $s+\varepsilon>b$, you have extended $\gamma$ beyond $b$ — contradicting that $b$ was the endpoint. Do the same on the left for $a$.

---

# Solution

The plan is to isolate three one-line structural lemmas — left translation preserves integral curves (Lemma A), time translation preserves them (Lemma B), and coincidence at a point forces gluing (Lemma C) — and then to run the extension-by-translation argument. Lemma A converts a single short curve at $e$ into a uniform existence time $\varepsilon$ valid everywhere on $G$; Lemmas B and C splice a full-length copy of that curve onto the end of a maximal curve; the splice reaches past any finite endpoint, so no finite endpoint can exist. A closing translation transfers the conclusion from the curve through $e$ to every integral curve.

**Step 1: Left translation carries integral curves of $X$ to integral curves of $X$ (Lemma A).**

Let $\gamma\colon J\to G$ be an integral curve of the left-invariant field $X$ and let $g\in G$. Then $L_g\circ\gamma\colon J\to G$, $t\mapsto g\,\gamma(t)$, is an integral curve of $X$ on the *same* interval $J$, with initial point $g\,\gamma(0)$.

> [!note]- Derivation
> Fix $g\in G$ and write $\sigma:=L_g\circ\gamma$, so $\sigma(t)=g\,\gamma(t)$. Since $L_g$ is smooth and $\gamma$ is smooth, $\sigma$ is smooth. Differentiate by the chain rule, using that the velocity of $L_g\circ\gamma$ is the differential of $L_g$ applied to the velocity of $\gamma$:
> $$\dot\sigma(t)=d(L_g)_{\gamma(t)}\big(\dot\gamma(t)\big)\qquad\text{(chain rule for the differentiable map }L_g\text{).}$$
> Because $\gamma$ is an integral curve of $X$, its velocity is $\dot\gamma(t)=X(\gamma(t))$ (by (IC)); substituting,
> $$\dot\sigma(t)=d(L_g)_{\gamma(t)}\big(X(\gamma(t))\big)\qquad\text{(by (IC) applied to }\gamma\text{).}$$
> Now invoke **left-invariance of $X$**: the identity (LI) with $h=\gamma(t)$ reads $X(g\,\gamma(t))=d(L_g)_{\gamma(t)}\big(X(\gamma(t))\big)$. Hence
> $$\dot\sigma(t)=X\big(g\,\gamma(t)\big)=X\big(\sigma(t)\big)\qquad\text{(by (LI) with }h=\gamma(t)\text{).}$$
> Thus $\sigma$ satisfies (IC), so it is an integral curve of $X$ on $J$, with $\sigma(0)=g\,\gamma(0)$. The domain $J$ is unchanged because $L_g$ is defined on all of $G$ and introduces no restriction on $t$.

**Step 2: Time translation carries integral curves of $X$ to integral curves of $X$ (Lemma B).**

Let $\gamma\colon J\to G$ be an integral curve of $X$ and $c\in\mathbb{R}$. Then $\gamma_c\colon J-c\to G$, $\gamma_c(t):=\gamma(t+c)$, is an integral curve of $X$ on the shifted interval $J-c=\{t:t+c\in J\}$.

> [!note]- Derivation
> The map $t\mapsto t+c$ is a smooth diffeomorphism of $\mathbb{R}$ carrying $J-c$ onto $J$, so $\gamma_c$ is smooth. Differentiate:
> $$\dot\gamma_c(t)=\frac{d}{dt}\gamma(t+c)=\dot\gamma(t+c)\qquad\text{(chain rule; the inner derivative }\tfrac{d}{dt}(t+c)=1\text{).}$$
> Since $\gamma$ is an integral curve of $X$, $\dot\gamma(t+c)=X(\gamma(t+c))$ (by (IC) evaluated at time $t+c$), and $\gamma(t+c)=\gamma_c(t)$ by definition. Therefore
> $$\dot\gamma_c(t)=X\big(\gamma(t+c)\big)=X\big(\gamma_c(t)\big)\qquad\text{(by (IC) at }t+c\text{, then the definition of }\gamma_c\text{).}$$
> So $\gamma_c$ satisfies (IC). The crucial point is that the vector field $X$ carries **no explicit dependence on $t$** — the equation (IC) is autonomous — which is exactly why the shifted curve solves the *same* equation rather than a modified one.

**Step 3: Two integral curves agreeing at a point glue into one (Lemma C).**

Let $\gamma_1\colon J_1\to G$ and $\gamma_2\colon J_2\to G$ be integral curves of $X$, and suppose there is a time $t_*\in J_1\cap J_2$ with $\gamma_1(t_*)=\gamma_2(t_*)$. Then $\gamma_1=\gamma_2$ on $J_1\cap J_2$, and the common map
$$\gamma\colon J_1\cup J_2\to G,\qquad \gamma|_{J_1}=\gamma_1,\quad \gamma|_{J_2}=\gamma_2,$$
is a well-defined integral curve of $X$ on $J_1\cup J_2$ (which is again an interval, since $J_1$ and $J_2$ are intervals with the common point $t_*$).

> [!note]- Derivation
> Both $\gamma_1$ and $\gamma_2$ are integral curves of $X$ and they take the same value $\gamma_1(t_*)=\gamma_2(t_*)$ at the common time $t_*\in J_1\cap J_2$. By the **uniqueness** clause of [[Thm - Existence and Uniqueness of Integral Curves|the existence–uniqueness theorem]] — restated here: *two integral curves of a smooth vector field that agree at one point of the intersection of their (interval) domains agree on the whole intersection* — we conclude
> $$\gamma_1(t)=\gamma_2(t)\qquad\text{for all }t\in J_1\cap J_2\qquad\text{(by uniqueness of integral curves).}$$
> Therefore the piecewise definition of $\gamma$ is unambiguous: on the overlap the two prescriptions coincide, so $\gamma$ is a single well-defined map. It is smooth because it is smooth on each of the open intervals $J_1$ and $J_2$ whose union it is defined on, and it satisfies (IC) at every point because near any $t\in J_1\cup J_2$ it agrees with one of the integral curves $\gamma_1,\gamma_2$. The union $J_1\cup J_2$ is an interval because two intervals sharing the point $t_*$ have connected union. Hence $\gamma$ is an integral curve of $X$ on $J_1\cup J_2$.

**Step 4: A uniform existence time $\varepsilon$ valid at every point of $G$.**

There is an $\varepsilon>0$ and, for every $p\in G$, an integral curve $\theta_p\colon(-\varepsilon,\varepsilon)\to G$ of $X$ with $\theta_p(0)=p$.

> [!note]- Derivation
> Apply the **local existence** clause of the existence–uniqueness theorem *once*, at the identity $e$: there is an $\varepsilon>0$ and an integral curve
> $$\theta\colon(-\varepsilon,\varepsilon)\to G,\qquad \dot\theta(t)=X(\theta(t)),\quad \theta(0)=e.$$
> Fix this $\varepsilon$. Now let $p\in G$ be arbitrary and set $\theta_p:=L_p\circ\theta$, that is $\theta_p(t)=p\,\theta(t)$. By **Lemma A (Step 1)**, $\theta_p$ is an integral curve of $X$ on the same interval $(-\varepsilon,\varepsilon)$, and its initial value is
> $$\theta_p(0)=p\,\theta(0)=p\,e=p\qquad\text{(by Step 1 and }\theta(0)=e\text{).}$$
> Thus the single number $\varepsilon$, extracted at $e$, provides an integral curve of length $2\varepsilon$ through *every* point $p$. This uniformity — the same $\varepsilon$ for all starting points — is the whole payoff of left-invariance, and it is what a general vector field on a non-compact manifold cannot supply.

**Step 5: The maximal integral curve through $e$ is defined on all of $\mathbb{R}$.**

Let $\gamma\colon(a,b)\to G$ be the maximal integral curve of $X$ with $\gamma(0)=e$, where $-\infty\le a<0<b\le+\infty$. We show $b=+\infty$ and $a=-\infty$.

> [!note]- Derivation
> **Suppose, for contradiction, that $b<+\infty$.** Choose a time
> $$s\in(b-\varepsilon,\,b),$$
> which is possible because $b-\varepsilon<b$ and $s$ lies in the domain $(a,b)$ of $\gamma$ (as $s<b$, and $s>b-\varepsilon$; if $b-\varepsilon\le 0$ take any $s\in(0,b)$, which still satisfies $s>b-\varepsilon$). Let $\varepsilon$ and $\theta_{\gamma(s)}$ be as in **Step 4**, so $\theta_{\gamma(s)}\colon(-\varepsilon,\varepsilon)\to G$ is an integral curve of $X$ with $\theta_{\gamma(s)}(0)=\gamma(s)$.
>
> **Reposition it in time to pass through $\gamma(s)$ at time $s$.** By **Lemma B (Step 2)** with $c=-s$, the curve
> $$\eta\colon(s-\varepsilon,\,s+\varepsilon)\to G,\qquad \eta(t):=\theta_{\gamma(s)}(t-s),$$
> is an integral curve of $X$, and
> $$\eta(s)=\theta_{\gamma(s)}(0)=\gamma(s)\qquad\text{(by Step 2 and Step 4).}$$
> **Glue.** The two integral curves $\gamma$ and $\eta$ take the same value $\gamma(s)=\eta(s)$ at the common time $s\in(a,b)\cap(s-\varepsilon,s+\varepsilon)$. By **Lemma C (Step 3)** they glue to an integral curve
> $$\widehat\gamma\colon(a,b)\cup(s-\varepsilon,s+\varepsilon)\to G$$
> extending $\gamma$. But since $s>b-\varepsilon$, the right endpoint of the glued interval satisfies
> $$s+\varepsilon>(b-\varepsilon)+\varepsilon=b,$$
> so $(a,b)\cup(s-\varepsilon,s+\varepsilon)=(a,\,s+\varepsilon)$ is a *strictly larger* interval than $(a,b)$, and $\widehat\gamma$ agrees with $\gamma$ on $(a,b)$. This contradicts the **maximality** of $\gamma$: $\gamma$ was assumed to have the largest possible domain, yet $\widehat\gamma$ extends it. The contradiction shows $b=+\infty$.
>
> **The left endpoint.** The identical argument applied to a time $s\in(a,a+\varepsilon)$ produces a curve extending $\gamma$ below $a$, contradicting maximality unless $a=-\infty$. (Concretely: choose $s\in(a,a+\varepsilon)$, glue $\eta(t)=\theta_{\gamma(s)}(t-s)$ on $(s-\varepsilon,s+\varepsilon)$; here $s-\varepsilon<(a+\varepsilon)-\varepsilon=a$, so the glued interval $(s-\varepsilon,b)$ extends below $a$.) Hence $a=-\infty$.
>
> Therefore the maximal interval is $(a,b)=(-\infty,+\infty)=\mathbb{R}$: the maximal integral curve through $e$ is defined on all of $\mathbb{R}$.

**Step 6: Every maximal integral curve of $X$ is defined on all of $\mathbb{R}$.**

Let $\gamma_e\colon\mathbb{R}\to G$ be the maximal integral curve through $e$ from Step 5, and let $\delta$ be the maximal integral curve of $X$ with $\delta(0)=p$ for an arbitrary $p\in G$. Then $\delta=L_p\circ\gamma_e$, and in particular $\delta$ is defined on all of $\mathbb{R}$.

> [!note]- Derivation
> By **Lemma A (Step 1)**, the curve $L_p\circ\gamma_e\colon\mathbb{R}\to G$, $t\mapsto p\,\gamma_e(t)$, is an integral curve of $X$, defined on all of $\mathbb{R}$, with initial value
> $$(L_p\circ\gamma_e)(0)=p\,\gamma_e(0)=p\,e=p\qquad\text{(by Step 1 and }\gamma_e(0)=e\text{).}$$
> Thus $L_p\circ\gamma_e$ and $\delta$ are both integral curves of $X$ with the same value $p$ at time $0$. By **uniqueness** ([[Thm - Existence and Uniqueness of Integral Curves|existence–uniqueness]], restated: integral curves agreeing at one instant agree on their common domain) they coincide wherever both are defined; and since $L_p\circ\gamma_e$ is defined on all of $\mathbb{R}$, the maximal curve $\delta$ cannot have a smaller domain, so its domain is all of $\mathbb{R}$ and $\delta=L_p\circ\gamma_e$. As $p$ was arbitrary, every maximal integral curve of $X$ is defined on all of $\mathbb{R}$. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** Every left-invariant vector field $X$ on a Lie group $G$ is complete: each of its maximal integral curves is defined on all of $\mathbb{R}$.
>
> *Lemma A (left translation preserves integral curves).* If $\gamma\colon J\to G$ is an integral curve of $X$ and $g\in G$, then $L_g\circ\gamma$ is an integral curve of $X$ on $J$. Indeed $\frac{d}{dt}(g\gamma(t))=d(L_g)_{\gamma(t)}(\dot\gamma(t))=d(L_g)_{\gamma(t)}(X(\gamma(t)))=X(g\gamma(t))$, the last equality by left-invariance (LI).
>
> *Lemma B (time translation preserves integral curves).* If $\gamma\colon J\to G$ is an integral curve and $c\in\mathbb{R}$, then $t\mapsto\gamma(t+c)$ is an integral curve on $J-c$, because $\frac{d}{dt}\gamma(t+c)=\dot\gamma(t+c)=X(\gamma(t+c))$; here autonomy of (IC) is used.
>
> *Lemma C (gluing).* If two integral curves of $X$ agree at one common time, they agree on the overlap of their domains (uniqueness), hence glue to an integral curve on the union.
>
> *Uniform existence.* By local existence there is $\varepsilon>0$ and an integral curve $\theta\colon(-\varepsilon,\varepsilon)\to G$ with $\theta(0)=e$. For any $p\in G$, Lemma A gives the integral curve $L_p\circ\theta\colon(-\varepsilon,\varepsilon)\to G$ through $p$. So $\varepsilon$ is a uniform existence time.
>
> *Completeness at $e$.* Let $\gamma\colon(a,b)\to G$ be maximal with $\gamma(0)=e$. If $b<\infty$, pick $s\in(b-\varepsilon,b)$; the curve $\eta(t):=(L_{\gamma(s)}\circ\theta)(t-s)$ (Lemmas A, B) is an integral curve on $(s-\varepsilon,s+\varepsilon)$ with $\eta(s)=\gamma(s)$. By Lemma C, $\gamma$ and $\eta$ glue to an integral curve on $(a,b)\cup(s-\varepsilon,s+\varepsilon)=(a,s+\varepsilon)$ with $s+\varepsilon>b$, contradicting maximality. Hence $b=\infty$; the same construction run at a time $s\in(a,a+\varepsilon)$ — for which $s-\varepsilon<(a+\varepsilon)-\varepsilon=a$, so the glued interval $(s-\varepsilon,b)$ reaches below $a$ — contradicts maximality unless $a=-\infty$. So $\gamma\colon\mathbb{R}\to G$.
>
> *Every point.* For arbitrary $p$, Lemma A makes $L_p\circ\gamma\colon\mathbb{R}\to G$ an integral curve with initial value $p$; by uniqueness it is the maximal integral curve through $p$, defined on all of $\mathbb{R}$.
>
> Therefore every maximal integral curve of $X$ is defined on all of $\mathbb{R}$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: quoting a completeness theorem for compact manifolds
> A frequent reflex is: "vector fields on compact manifolds are complete, and $SO(n)$, $SU(n)$, tori are compact, so we are done." This proves nothing in general, because a Lie group need not be compact — $GL(n;\mathbb{R})$, the Heisenberg group, $\mathbb{R}^n$ as a group, all carry left-invariant fields and none is compact. Compactness would give completeness of *all* smooth fields, not just left-invariant ones, and it is unavailable here. The correct engine is left-invariance, which supplies a *uniform* existence time on any Lie group, compact or not; that uniform time is exactly what compactness would have supplied by a covering argument, and it is precisely what forbids finite-time escape.

> [!note]- Independent sanity check on the abelian model $G=(\mathbb{R}^n,+)$
> Take $G=\mathbb{R}^n$ with addition, $e=0$; left translation is $L_g(h)=g+h$, whose differential is the identity, so a left-invariant field is a *constant* field $X\equiv v$ for a fixed $v\in\mathbb{R}^n=\mathfrak{g}$. Its integral curve through $p$ solves $\dot\gamma=v$, $\gamma(0)=p$, giving $\gamma(t)=p+tv$ — a straight line defined for all $t\in\mathbb{R}$, consistent with the theorem. The extension-by-translation argument specialises here to the obvious fact that a line of any length can always be prolonged, and the "uniform $\varepsilon$" is the trivial observation that a constant field has the same solution shape everywhere.

---

# Key Takeaways

**Left-invariance is a completeness engine because it upgrades local existence at one point into uniform local existence everywhere.** The general existence–uniqueness theorem only promises *some* interval of existence, and on a non-compact manifold that interval can shrink to nothing as the base point wanders off to infinity — which is precisely the mechanism of finite-time blow-up. A left-invariant field is immune: because the symmetry $L_g$ preserves the field, one integral curve of length $2\varepsilon$ obtained at the identity translates to a curve of the *same* length through every point, so the existence time $\varepsilon$ is a single constant valid on all of $G$. Uniform existence time is exactly the hypothesis that prohibits escape in finite time, and this is why the argument never needs compactness. Whenever you must prove a flow is complete and the manifold is non-compact, the productive question is: *is there a symmetry group acting transitively and preserving the field?* If so, transport a single short solution and read off the uniform time.

**The extension-by-translation contradiction is the standard finish for a completeness proof, and its shape is worth memorising.** Assume the maximal interval has a finite endpoint $b$; land at a time $s$ within one uniform existence-time of $b$; grow a fresh full-length integral curve out of the current position $\gamma(s)$ using autonomy (time-shift) and the uniform time; glue it to the old curve by uniqueness; observe that the fresh curve reaches past $b$; conclude the endpoint was not maximal after all. The three ingredients — a *uniform* existence time, *autonomy* of the equation (to reposition a solution in time without deforming it), and *uniqueness* (to glue) — appear in every proof of this kind, from the completeness of geodesic flows on compact Riemannian manifolds to the completeness of fields with bounded support. If you reconstruct this proof months later, anchor it on the phrase "grow a uniform-length curve at the endpoint and glue," and the rest follows.

**This result is the hidden precondition that makes the exponential map exist, and it is where the special role of the identity enters.** The exponential map is defined by $\exp(X)=\gamma_X(1)$, the value at time $1$ of the integral curve of the left-invariant field $X$ starting at $e$; this only makes sense once $\gamma_X$ is known to reach time $1$, which is exactly the present completeness statement (see [[Thm - One-Parameter Subgroups are the Integral Curves of Left-Invariant Vector Fields|the theorem identifying one-parameter subgroups with integral curves of left-invariant fields]], where this exercise is the completeness input). Notice the economy of the argument: local existence is invoked *once*, at the identity, and translation does the rest — the identity is the single privileged base point of a Lie group, and every structural fact about left-invariant fields is ultimately a statement transported from $e$. The transferable diagnostic is that on a homogeneous space (a manifold with a transitive symmetry group), a property that holds at one point and is preserved by the symmetry holds everywhere; completeness of an invariant field is the archetype, and the same "prove it at the base point, translate it out" pattern recurs throughout the theory of Lie groups and their actions.
