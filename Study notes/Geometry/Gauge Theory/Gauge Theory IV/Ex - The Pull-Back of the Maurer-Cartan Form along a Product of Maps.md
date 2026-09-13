---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - The Maurer-Cartan Form"
  - "Def - Left and Right Translations and Conjugation on a Lie Group"
  - "Thm - Ad is a Smooth Representation and its Differential is ad"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $G$ be a Lie group with Lie algebra $\mathfrak{g}=T_eG$, and let $\theta\in\Omega^1(G;\mathfrak{g})$ be its left Maurer–Cartan form, $\theta_a=d_aL_{a^{-1}}\colon T_aG\to T_eG=\mathfrak{g}$. Let $U$ be a smooth manifold (the reader may take $U\subseteq\mathbb{R}^n$ an open set on first reading) and let $g_1,g_2\colon U\to G$ be smooth maps. Write $g_1g_2\colon U\to G$ for the pointwise product $x\mapsto g_1(x)\cdot g_2(x)$, and $g^{-1}\colon U\to G$ for the pointwise inverse $x\mapsto g(x)^{-1}$.

Prove the two pull-back identities:
$$(g_1g_2)^*\theta=\operatorname{Ad}_{g_2^{-1}}\!\big(g_1^*\theta\big)+g_2^*\theta,\qquad\text{(product rule)}$$
$$(g^{-1})^*\theta=-\operatorname{Ad}_{g}\!\big(g^*\theta\big).\qquad\text{(inversion rule)}$$

Here $\operatorname{Ad}_{g_2^{-1}}(g_1^*\theta)$ denotes the $\mathfrak{g}$-valued $1$-form on $U$ whose value at $x\in U$ on a tangent vector $X\in T_xU$ is $\operatorname{Ad}_{g_2(x)^{-1}}\!\big((g_1^*\theta)_x(X)\big)$ — the adjoint action is applied pointwise, with the group element $g_2(x)^{-1}$ varying over $U$; likewise $\operatorname{Ad}_g(g^*\theta)$ at $x$ is $\operatorname{Ad}_{g(x)}\!\big((g^*\theta)_x(X)\big)$. Finally, verify both identities directly for a matrix group $G\subseteq GL(n;\mathbb{K})$, where $g^*\theta=g^{-1}\,dg$.

These are not results the two textbook sources isolate; they are the single computational identity underneath every local gauge-transformation law in the chapter. The product rule is exactly what makes the local connection form transform by $A_\beta=\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha+g_{\alpha\beta}^*\theta$ under a change of local section, and it is invoked at that point (Bär's Theorem 2.3.6 and Haydys's Theorem 2.2.5, Step 3). We isolate it once, prove it in full, and thereafter cite it.

**Recall:**

The objects in play are the Maurer–Cartan form, the left and right translations of $G$, the adjoint representation, and the pull-back of a Lie-algebra-valued form along a smooth map.

![[Def - The Maurer-Cartan Form#The Definition]]

We use three standing facts about $\theta$, all established on [[Def - The Maurer-Cartan Form|its definition page]]. First, $\theta$ is **left-invariant**: for every $h\in G$,
$$L_h^*\theta=\theta,\qquad\text{equivalently}\qquad\theta_{ha}\big(d_aL_h(v)\big)=\theta_a(v)\quad\text{for all }a\in G,\ v\in T_aG.$$
Second, under right translation $\theta$ transforms by the adjoint of the inverse: for every $h\in G$,
$$R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta,\qquad\text{equivalently}\qquad\theta_{ah}\big(d_aR_h(v)\big)=\operatorname{Ad}_{h^{-1}}\!\big(\theta_a(v)\big)\quad\text{for all }a\in G,\ v\in T_aG.$$
Third, for a matrix group $G\subseteq GL(n;\mathbb{K})$ one has $\theta_a(v)=a^{-1}v$ for $v\in T_aG\subseteq M_n(\mathbb{K})$, so that along a smooth map $g\colon U\to G$ the pull-back is $g^*\theta=g^{-1}\,dg$.

![[Def - Left and Right Translations and Conjugation on a Lie Group#The Definition]]

For $h\in G$ the **left translation** $L_h\colon G\to G$ is $L_h(a)=ha$ and the **right translation** $R_h\colon G\to G$ is $R_h(a)=ah$; both are diffeomorphisms, with $L_h^{-1}=L_{h^{-1}}$ and $R_h^{-1}=R_{h^{-1}}$. They satisfy $L_h\circ L_k=L_{hk}$ and $R_h\circ R_k=R_{kh}$, and left and right translations commute: $L_h\circ R_k=R_k\circ L_h$.

![[Thm - Ad is a Smooth Representation and its Differential is ad#Statement]]

The **adjoint representation** $\operatorname{Ad}\colon G\to GL(\mathfrak{g})$ is $\operatorname{Ad}_h=d_e\alpha_h$, the differential at the identity of the conjugation $\alpha_h=L_h\circ R_{h^{-1}}$; it is a representation, so $\operatorname{Ad}_{hk}=\operatorname{Ad}_h\operatorname{Ad}_k$ and $\operatorname{Ad}_{h^{-1}}=(\operatorname{Ad}_h)^{-1}$, and for a matrix group $\operatorname{Ad}_hX=hXh^{-1}$. See [[Thm - Ad is a Smooth Representation and its Differential is ad|the adjoint-representation theorem]].

The pull-back of a $\mathfrak{g}$-valued $1$-form is taken componentwise, as on [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|the Lie-algebra-valued forms page]]: for a smooth $g\colon U\to G$, the form $g^*\theta\in\Omega^1(U;\mathfrak{g})$ is defined by
$$(g^*\theta)_x(X)=\theta_{g(x)}\big(d_xg\,(X)\big)\in\mathfrak{g},\qquad x\in U,\ X\in T_xU.$$

---

# Convergent Strategy

**Problem class.** This is a *composite-map pull-back* problem: an identity relating the pull-back of a fixed form ($\theta$) along a map built out of two others (the product $g_1g_2$) to the pull-backs along the pieces. The universal method for such problems is to factor the composite map through a standard multiplication or evaluation map and apply the chain rule (functoriality of pull-back, $(F\circ H)^*=H^*\circ F^*$). Here the composite map is $g_1g_2=m\circ(g_1,g_2)$, where $m\colon G\times G\to G$ is group multiplication; the whole difficulty is compressed into one object, the differential of $m$.

**Assumption pattern.** The only structural input is that $\theta$ is *left-invariant* and *right-equivariant* under $\operatorname{Ad}$. These two properties are precisely tailored to the two terms that the differential of multiplication produces: $d_{(a,b)}m$ splits a tangent vector to $G\times G$ into a piece pushed forward by a left translation $L_a$ and a piece pushed forward by a right translation $R_b$. Left-invariance annihilates the first translation cleanly; right-equivariance turns the second into an $\operatorname{Ad}$. The recognisable trigger is: *a form pulled back along a product, whose defining property is invariance under one-sided translations*.

**Theorem routing.** The route is: (i) establish the product rule for the differential of multiplication, $d_{(a,b)}m(v,w)=d_aR_b(v)+d_bL_a(w)$, from the definitions of $L$ and $R$ and linearity of the differential; (ii) factor $g_1g_2=m\circ(g_1,g_2)$ and apply the chain rule to compute $d(g_1g_2)$; (iii) apply $\theta$ at the product point $g_1(x)g_2(x)$, split by linearity, and evaluate the two pieces using left-invariance ([[Def - The Maurer-Cartan Form|Maurer–Cartan form]], property $L_h^*\theta=\theta$) and right-equivariance (property $R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta$). The inversion rule is then not a separate computation: it is the product rule applied to $g_1=g$, $g_2=g^{-1}$, together with the observation that $gg^{-1}$ is the constant map $e$ and the pull-back of $\theta$ along a constant map vanishes.

**Key decision point.** Two moves carry the argument. The first is *factoring through the multiplication map* rather than trying to differentiate the product pointwise in $G$ — the abstract Lie group has no ambient linear structure in which "$d(g_1g_2)=(dg_1)g_2+g_1(dg_2)$" would make literal sense, so the product rule must be routed through $d_{(a,b)}m$. The second is *reading the inversion rule off the product rule*: rather than differentiate $x\mapsto g(x)^{-1}$ directly (which needs the differential of the inversion map), we exploit that the product rule is an identity of forms and specialise it to a product that collapses to a constant. This is the same economy by which, in a group, one derives the inverse-of-a-product rule $(ab)^{-1}=b^{-1}a^{-1}$ and then reads off $a^{-1}$ facts as special cases.

---

# Legal Operations Used

This solution deploys the following legal operations, which the topic page catalogues under its Legal Operations for §4.1:

1. **Factor a map built from group operations through the standard multiplication map.** Write $g_1g_2=m\circ(g_1,g_2)$ with $m\colon G\times G\to G$, $m(a,b)=ab$, and $(g_1,g_2)\colon U\to G\times G$, $x\mapsto(g_1(x),g_2(x))$. This exposes the group structure to the chain rule.

2. **Compute the differential of multiplication by the one-sided-translation product rule.** Use $d_{(a,b)}m(v,w)=d_aR_b(v)+d_bL_a(w)$, proved below from the definitions of $R_b$ and $L_a$ and the linearity of the tangent map on the two summands of $T_{(a,b)}(G\times G)=T_aG\oplus T_bG$.

3. **Push the Maurer–Cartan form through a left translation using left-invariance.** From $L_h^*\theta=\theta$, i.e. $\theta_{ha}(d_aL_h v)=\theta_a(v)$, collapse the $L_a$-term to $\theta$ evaluated at the untranslated point.

4. **Push the Maurer–Cartan form through a right translation using right-equivariance.** From $R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta$, i.e. $\theta_{ah}(d_aR_h v)=\operatorname{Ad}_{h^{-1}}(\theta_a(v))$, convert the $R_b$-term into an $\operatorname{Ad}_{b^{-1}}$ of $\theta$ at the untranslated point.

5. **Recognise the pull-back along a constant map as zero.** A constant map has zero differential, so its pull-back of any form vanishes; applied to $gg^{-1}\equiv e$ this kills the left-hand side of the specialised product rule.

6. **Specialise a form identity to extract a corollary.** Rather than re-run the computation for inversion, substitute $g_1=g$, $g_2=g^{-1}$ into the product rule and solve the resulting equation for $(g^{-1})^*\theta$.

7. **Verify an abstract identity in the matrix model.** For $G\subseteq GL(n;\mathbb{K})$ use $\theta_a(v)=a^{-1}v$, $\operatorname{Ad}_hX=hXh^{-1}$, and the entrywise Leibniz rule for the matrix product to recover both identities by direct computation with $g^{-1}\,dg$.

---

# Hints

> [!note]- Hint 1
> The map $x\mapsto g_1(x)g_2(x)$ is the composition of $x\mapsto(g_1(x),g_2(x))$ with the multiplication map $m\colon G\times G\to G$. Pull-back is contravariantly functorial: $(m\circ(g_1,g_2))^*=(g_1,g_2)^*\circ m^*$. So the whole problem reduces to understanding $\theta$ pulled back by $m$, which reduces to understanding the differential of $m$.

> [!note]- Hint 2
> The differential of multiplication splits a tangent vector at $(a,b)$ into a left-translation part and a right-translation part: $d_{(a,b)}m(v,w)=d_aR_b(v)+d_bL_a(w)$. Prove this by freezing one coordinate at a time — freezing $b$ turns $m(\cdot,b)$ into $R_b$, freezing $a$ turns $m(a,\cdot)$ into $L_a$ — and adding, using that the differential is linear on $T_aG\oplus T_bG$.

> [!note]- Hint 3
> Now apply $\theta$ at the point $g_1(x)g_2(x)$ to the two pieces. The piece coming from $L_{g_1(x)}$ is handled by *left-invariance* $L_h^*\theta=\theta$: it collapses to $\theta$ evaluated on $dg_2$, i.e. to $g_2^*\theta$. The piece coming from $R_{g_2(x)}$ is handled by *right-equivariance* $R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta$: it becomes $\operatorname{Ad}_{g_2(x)^{-1}}$ applied to $\theta$ evaluated on $dg_1$, i.e. to $\operatorname{Ad}_{g_2^{-1}}(g_1^*\theta)$. Add the two pieces.

> [!note]- Hint 4
> For the inversion rule do not compute afresh. Put $g_1=g$ and $g_2=g^{-1}$ in the product rule. Then $g_1g_2=gg^{-1}$ is the *constant* map $e$, whose pull-back of $\theta$ is $0$ (a constant map has zero differential). The product rule becomes $0=\operatorname{Ad}_{(g^{-1})^{-1}}(g^*\theta)+(g^{-1})^*\theta=\operatorname{Ad}_g(g^*\theta)+(g^{-1})^*\theta$; solve for $(g^{-1})^*\theta$.

> [!note]- Hint 5
> For the matrix check, recall $\theta=g^{-1}\,dg$ and $\operatorname{Ad}_hX=hXh^{-1}$. Expand $(g_1g_2)^{-1}\,d(g_1g_2)$ with the Leibniz rule $d(g_1g_2)=(dg_1)g_2+g_1\,dg_2$ and $(g_1g_2)^{-1}=g_2^{-1}g_1^{-1}$; for inversion differentiate $g^{-1}g=\mathbb{1}$ to get $d(g^{-1})=-g^{-1}(dg)g^{-1}$.

---

# Solution

The engine is the differential of the multiplication map, which resolves any tangent vector to $G\times G$ into a left part and a right part. The Maurer–Cartan form is built to react to exactly these two motions: left-invariance disposes of the left part and right-equivariance turns the right part into an adjoint action. We prove the product rule this way, then obtain the inversion rule as its specialisation to a product that collapses to the identity, and finally confirm both against the matrix model where $\theta=g^{-1}\,dg$.

**Step 0: The differential of the multiplication map is $d_{(a,b)}m(v,w)=d_aR_b(v)+d_bL_a(w)$.**

Let $m\colon G\times G\to G$, $m(a,b)=ab$, be group multiplication; it is smooth by the axioms of a Lie group. Fix $(a,b)\in G\times G$ and a tangent vector $(v,w)\in T_{(a,b)}(G\times G)=T_aG\oplus T_bG$, so $v\in T_aG$ and $w\in T_bG$.

> [!note]- Derivation
> The canonical isomorphism $T_{(a,b)}(G\times G)\cong T_aG\oplus T_bG$ decomposes $(v,w)=(v,0)+(0,w)$, and the differential $d_{(a,b)}m$ is linear, so
> $$d_{(a,b)}m(v,w)=d_{(a,b)}m(v,0)+d_{(a,b)}m(0,w)\qquad\text{(linearity of the tangent map).}$$
>
> **Evaluate the first summand by freezing the second coordinate.** Choose a smooth curve $\alpha\colon(-\varepsilon,\varepsilon)\to G$ with $\alpha(0)=a$ and $\dot\alpha(0)=v$. The curve $t\mapsto(\alpha(t),b)$ in $G\times G$ has velocity $(v,0)$ at $t=0$, and
> $$m\big(\alpha(t),b\big)=\alpha(t)\,b=R_b\big(\alpha(t)\big)\qquad\text{(definition of }m\text{ and of the right translation }R_b\text{).}$$
> Differentiating at $t=0$ and using that the differential of a map applied to a curve's velocity is the velocity of the image curve,
> $$d_{(a,b)}m(v,0)=\tfrac{d}{dt}\Big|_{0}R_b\big(\alpha(t)\big)=d_aR_b(v)\qquad\text{(chain rule; }\alpha(0)=a,\ \dot\alpha(0)=v\text{).}$$
>
> **Evaluate the second summand by freezing the first coordinate.** Choose a smooth curve $\beta\colon(-\varepsilon,\varepsilon)\to G$ with $\beta(0)=b$ and $\dot\beta(0)=w$. The curve $t\mapsto(a,\beta(t))$ has velocity $(0,w)$ at $t=0$, and
> $$m\big(a,\beta(t)\big)=a\,\beta(t)=L_a\big(\beta(t)\big)\qquad\text{(definition of }m\text{ and of the left translation }L_a\text{).}$$
> Differentiating at $t=0$,
> $$d_{(a,b)}m(0,w)=\tfrac{d}{dt}\Big|_{0}L_a\big(\beta(t)\big)=d_bL_a(w)\qquad\text{(chain rule; }\beta(0)=b,\ \dot\beta(0)=w\text{).}$$
>
> **Add the two summands.** Combining the three displayed lines,
> $$d_{(a,b)}m(v,w)=d_aR_b(v)+d_bL_a(w).$$
> This is the product rule for the differential of multiplication, the tangent-space form of "the derivative of a product is the derivative of the first times the second plus the first times the derivative of the second"; the two summands live in $T_{ab}G$, since $R_b\colon G\to G$ and $L_a\colon G\to G$ both map into $G$ and send $a\mapsto ab$, $b\mapsto ab$ respectively.

**Step 1: Differentiate the product map $g_1g_2$.**

Write $g_1g_2=m\circ\Delta$, where $\Delta:=(g_1,g_2)\colon U\to G\times G$ is $x\mapsto(g_1(x),g_2(x))$. Fix $x\in U$ and $X\in T_xU$, and abbreviate $a:=g_1(x)$, $b:=g_2(x)$.

> [!note]- Derivation
> The differential of $\Delta$ is the pair of differentials,
> $$d_x\Delta(X)=\big(d_xg_1(X),\,d_xg_2(X)\big)\in T_aG\oplus T_bG\qquad\text{(differential of a map into a product is the product of the differentials).}$$
> By the chain rule and Step 0,
> $$d_x(g_1g_2)(X)=d_{(a,b)}m\big(d_x\Delta(X)\big)=d_{(a,b)}m\big(d_xg_1(X),\,d_xg_2(X)\big)\qquad\text{(chain rule for }g_1g_2=m\circ\Delta\text{)}$$
> $$=d_aR_b\big(d_xg_1(X)\big)+d_bL_a\big(d_xg_2(X)\big)\qquad\text{(Step 0, with }v=d_xg_1(X),\ w=d_xg_2(X)\text{).}$$
> Both summands lie in $T_{ab}G=T_{g_1(x)g_2(x)}G$, which is exactly the tangent space at which $\theta$ will be evaluated in the next step.

**Step 2: Apply $\theta$ and split into the left and right pieces.**

Applying $\theta$ at the point $g_1(x)g_2(x)=ab$ to the vector computed in Step 1 and using linearity of $\theta_{ab}$ splits the pull-back into two terms, which left-invariance and right-equivariance evaluate separately.

> [!note]- Derivation
> By the definition of the pull-back and Step 1,
> $$\big((g_1g_2)^*\theta\big)_x(X)=\theta_{ab}\Big(d_x(g_1g_2)(X)\Big)=\theta_{ab}\Big(d_aR_b\big(d_xg_1(X)\big)+d_bL_a\big(d_xg_2(X)\big)\Big)$$
> $$=\underbrace{\theta_{ab}\Big(d_aR_b\big(d_xg_1(X)\big)\Big)}_{\text{right piece}}+\underbrace{\theta_{ab}\Big(d_bL_a\big(d_xg_2(X)\big)\Big)}_{\text{left piece}}\qquad\text{(}\theta_{ab}\text{ is linear).}$$
>
> **Evaluate the right piece by right-equivariance.** Set $v:=d_xg_1(X)\in T_aG$. Recall the [[Def - The Maurer-Cartan Form|Maurer–Cartan form]] satisfies $R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta$, that is $\theta_{ah}(d_aR_h(v))=\operatorname{Ad}_{h^{-1}}(\theta_a(v))$; take $h=b$ (so $ah=ab$):
> $$\theta_{ab}\Big(d_aR_b(v)\Big)=\operatorname{Ad}_{b^{-1}}\!\big(\theta_a(v)\big)=\operatorname{Ad}_{g_2(x)^{-1}}\!\Big(\theta_{g_1(x)}\big(d_xg_1(X)\big)\Big)\qquad\text{(right-equivariance }R_b^*\theta=\operatorname{Ad}_{b^{-1}}\theta\text{).}$$
> By the definition of the pull-back, $\theta_{g_1(x)}(d_xg_1(X))=(g_1^*\theta)_x(X)$, so the right piece equals $\operatorname{Ad}_{g_2(x)^{-1}}\!\big((g_1^*\theta)_x(X)\big)$, which is by definition $\big(\operatorname{Ad}_{g_2^{-1}}(g_1^*\theta)\big)_x(X)$.
>
> **Evaluate the left piece by left-invariance.** Set $w:=d_xg_2(X)\in T_bG$. Recall $\theta$ is left-invariant, $L_h^*\theta=\theta$, that is $\theta_{hb}(d_bL_h(w))=\theta_b(w)$; take $h=a$ (so $hb=ab$):
> $$\theta_{ab}\Big(d_bL_a(w)\Big)=\theta_b(w)=\theta_{g_2(x)}\big(d_xg_2(X)\big)=(g_2^*\theta)_x(X)\qquad\text{(left-invariance }L_a^*\theta=\theta\text{; then definition of the pull-back).}$$
>
> **Recombine.** Adding the two evaluated pieces,
> $$\big((g_1g_2)^*\theta\big)_x(X)=\operatorname{Ad}_{g_2(x)^{-1}}\!\big((g_1^*\theta)_x(X)\big)+(g_2^*\theta)_x(X).$$

**Step 3: Conclude the product rule.**

Since $x\in U$ and $X\in T_xU$ were arbitrary, the equality of Step 2 holds pointwise on all of $U$ and on every tangent vector, hence is an equality of $\mathfrak{g}$-valued $1$-forms:
$$(g_1g_2)^*\theta=\operatorname{Ad}_{g_2^{-1}}\!\big(g_1^*\theta\big)+g_2^*\theta.$$

**Step 4: Read off the inversion rule from the product rule.**

Apply the product rule with the choice $g_1=g$ and $g_2=g^{-1}$; the product $g\cdot g^{-1}$ is the constant map, whose pull-back is zero, and the equation solves for $(g^{-1})^*\theta$.

> [!note]- Derivation
> Take $g_1:=g$ and $g_2:=g^{-1}$ in Step 3. Their pointwise product is
> $$(g_1g_2)(x)=g(x)\,g(x)^{-1}=e\quad\text{for every }x\in U,$$
> so $g_1g_2\equiv e$ is the constant map. A constant map $c\colon U\to G$ has $d_xc=0$ at every $x$, hence
> $$\big((g_1g_2)^*\theta\big)_x(X)=\theta_{e}\big(d_x(g_1g_2)(X)\big)=\theta_e(0)=0\qquad\text{(the differential of a constant map is }0\text{; }\theta_e\text{ is linear).}$$
> The right-hand side of Step 3, with $g_2=g^{-1}$ so that $g_2^{-1}=g$ and $g_1^*\theta=g^*\theta$, is
> $$\operatorname{Ad}_{(g^{-1})^{-1}}\!\big(g^*\theta\big)+(g^{-1})^*\theta=\operatorname{Ad}_{g}\!\big(g^*\theta\big)+(g^{-1})^*\theta.$$
> Equating the two sides of Step 3 therefore gives
> $$0=\operatorname{Ad}_{g}\!\big(g^*\theta\big)+(g^{-1})^*\theta,$$
> and solving for the second summand,
> $$(g^{-1})^*\theta=-\operatorname{Ad}_{g}\!\big(g^*\theta\big).$$
> This is the inversion rule. No new differentiation was required: the identity of forms in Step 3 already contains it.

**Step 5: Verify both identities in the matrix model.**

Let $G\subseteq GL(n;\mathbb{K})$ be a matrix group, so that tangent vectors are matrices, $\theta_a(v)=a^{-1}v$, $\operatorname{Ad}_hX=hXh^{-1}$, and $g^*\theta=g^{-1}\,dg$ for a smooth $g\colon U\to G$ (each entry of $dg$ is the ordinary differential of the corresponding entry of $g$).

> [!note]- Derivation
> **Product rule.** The pull-back along the matrix product is
> $$(g_1g_2)^*\theta=(g_1g_2)^{-1}\,d(g_1g_2)=g_2^{-1}g_1^{-1}\,d(g_1g_2)\qquad\text{(}\theta=g^{-1}dg\text{; }(g_1g_2)^{-1}=g_2^{-1}g_1^{-1}\text{).}$$
> The entrywise Leibniz rule for the matrix product gives $d(g_1g_2)=(dg_1)\,g_2+g_1\,(dg_2)$, so
> $$(g_1g_2)^*\theta=g_2^{-1}g_1^{-1}\big((dg_1)g_2+g_1\,dg_2\big)=g_2^{-1}\big(g_1^{-1}\,dg_1\big)g_2+g_2^{-1}g_1^{-1}g_1\,dg_2\qquad\text{(distribute and regroup).}$$
> The first term is $g_2^{-1}(g_1^{-1}dg_1)g_2=\operatorname{Ad}_{g_2^{-1}}(g_1^{-1}dg_1)$ since $\operatorname{Ad}_{g_2^{-1}}X=g_2^{-1}Xg_2$; the second collapses to $g_2^{-1}\,dg_2$ because $g_1^{-1}g_1=\mathbb{1}$. Hence
> $$(g_1g_2)^*\theta=\operatorname{Ad}_{g_2^{-1}}\!\big(g_1^{-1}dg_1\big)+g_2^{-1}dg_2=\operatorname{Ad}_{g_2^{-1}}\!\big(g_1^*\theta\big)+g_2^*\theta,$$
> matching Step 3.
>
> **Inversion rule.** Differentiating the constant identity $g^{-1}g=\mathbb{1}$ by the Leibniz rule, $d(g^{-1})\,g+g^{-1}\,dg=0$, so
> $$d(g^{-1})=-g^{-1}\,(dg)\,g^{-1}\qquad\text{(right-multiply by }g^{-1}\text{).}$$
> Therefore
> $$(g^{-1})^*\theta=(g^{-1})^{-1}\,d(g^{-1})=g\,\big(-g^{-1}(dg)g^{-1}\big)=-(dg)\,g^{-1}\qquad\text{(}\theta=g^{-1}dg\text{ applied to }g^{-1}\text{; then }gg^{-1}=\mathbb{1}\text{).}$$
> On the other side, $-\operatorname{Ad}_{g}(g^*\theta)=-g\,(g^{-1}dg)\,g^{-1}=-(dg)\,g^{-1}$ as well, using $g g^{-1}=\mathbb{1}$. The two agree, matching Step 4. (Both equal $-(dg)g^{-1}$, minus the *right* Maurer–Cartan form $dg\,g^{-1}$ — consistent with the fact that $dg\,g^{-1}$, not $g^{-1}dg$, is the right-invariant form.)

> [!note]- Complete formal solution
> **Claim.** For smooth maps $g_1,g_2,g\colon U\to G$ into a Lie group $G$ with left Maurer–Cartan form $\theta$,
> $$(g_1g_2)^*\theta=\operatorname{Ad}_{g_2^{-1}}(g_1^*\theta)+g_2^*\theta,\qquad(g^{-1})^*\theta=-\operatorname{Ad}_{g}(g^*\theta).$$
>
> *Proof.* Let $m\colon G\times G\to G$, $m(a,b)=ab$, be multiplication. For $(v,w)\in T_aG\oplus T_bG$, writing $(v,w)=(v,0)+(0,w)$ and using linearity of the differential together with $m(\cdot,b)=R_b$ and $m(a,\cdot)=L_a$,
> $$d_{(a,b)}m(v,w)=d_aR_b(v)+d_bL_a(w).\tag{1}$$
>
> Fix $x\in U$, $X\in T_xU$, and set $a=g_1(x)$, $b=g_2(x)$. Since $g_1g_2=m\circ(g_1,g_2)$, the chain rule and $(1)$ give
> $$d_x(g_1g_2)(X)=d_aR_b\big(d_xg_1(X)\big)+d_bL_a\big(d_xg_2(X)\big).$$
> Apply $\theta_{ab}$ (linear) and evaluate the two pieces. By right-equivariance $R_b^*\theta=\operatorname{Ad}_{b^{-1}}\theta$,
> $$\theta_{ab}\big(d_aR_b(d_xg_1(X))\big)=\operatorname{Ad}_{b^{-1}}\big(\theta_a(d_xg_1(X))\big)=\operatorname{Ad}_{g_2(x)^{-1}}\big((g_1^*\theta)_x(X)\big);$$
> by left-invariance $L_a^*\theta=\theta$,
> $$\theta_{ab}\big(d_bL_a(d_xg_2(X))\big)=\theta_b\big(d_xg_2(X)\big)=(g_2^*\theta)_x(X).$$
> Adding and letting $x,X$ vary proves the product rule.
>
> For the inversion rule, put $g_1=g$, $g_2=g^{-1}$ in the product rule. Then $g_1g_2\equiv e$ is constant, so $(g_1g_2)^*\theta=0$ (zero differential), while the right-hand side is $\operatorname{Ad}_{g}(g^*\theta)+(g^{-1})^*\theta$. Hence $0=\operatorname{Ad}_{g}(g^*\theta)+(g^{-1})^*\theta$, i.e. $(g^{-1})^*\theta=-\operatorname{Ad}_{g}(g^*\theta)$.
>
> Matrix verification: with $\theta=g^{-1}dg$ and $\operatorname{Ad}_hX=hXh^{-1}$, the Leibniz rule gives $(g_1g_2)^{-1}d(g_1g_2)=g_2^{-1}(g_1^{-1}dg_1)g_2+g_2^{-1}dg_2$ and, from $d(g^{-1})=-g^{-1}(dg)g^{-1}$, $(g^{-1})^{-1}d(g^{-1})=-(dg)g^{-1}=-g(g^{-1}dg)g^{-1}$, reproducing both identities. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> One is tempted to "differentiate the product pointwise in $G$" and write $d(g_1g_2)=(dg_1)g_2+g_1(dg_2)$ for a general Lie group, then divide by $g_1g_2$ on the left. This is meaningless unless $G$ sits inside a matrix algebra: on an abstract Lie group there is no ambient multiplication of a tangent vector $d_xg_1(X)\in T_{g_1(x)}G$ by the element $g_2(x)$, and no "left division". The correct replacement is Step 0: the two would-be terms $(dg_1)g_2$ and $g_1(dg_2)$ are the intrinsic objects $d_aR_b(d_xg_1(X))$ and $d_bL_a(d_xg_2(X))$, and it is left-invariance and right-equivariance, not division, that turn them into $g_2^*\theta$ and $\operatorname{Ad}_{g_2^{-1}}(g_1^*\theta)$. The matrix computation in Step 5 is legitimate precisely because there the tangent spaces are honest matrix spaces and $R_b$, $L_a$ are right and left multiplication by matrices.

---

# Key Takeaways

**To pull a bi-invariant-type form back along a product, factor through the multiplication map and let the invariance properties absorb the two one-sided translations.** The single reusable principle here is that any map assembled from group operations — a product $g_1g_2$, an inverse $g^{-1}$, a conjugate $g_1g_2g_1^{-1}$ — should be written as a composition with the standard maps $m\colon G\times G\to G$ and inversion $\iota\colon G\to G$, so that the chain rule and the known differentials $d_{(a,b)}m(v,w)=d_aR_b(v)+d_bL_a(w)$ do the work. The Maurer–Cartan form is the paradigm target because its two defining behaviours, left-invariance ($L_h^*\theta=\theta$) and right-equivariance ($R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta$), are exactly matched to the two summands the multiplication differential produces. The trigger condition to recognise in future problems is: *a form with a one-sided invariance, pulled back along a product-type map*; the reaction is *factor through $m$, split, and apply the invariance to each piece*. The diagnostic that you have done it correctly is that the inhomogeneous (additive) term always attaches to the rightmost factor $g_2$, while the leftmost factor $g_1$ is conjugated by $\operatorname{Ad}_{g_2^{-1}}$ — the pure-gauge term "belongs to" whichever factor sits on the side matching the form's invariance.

**The inversion rule is free once the product rule is a form identity: specialise to a product that collapses to a constant.** A recurring economy across group theory and its differential-geometric shadows is that facts about inverses need not be proved separately; they fall out of the multiplicative fact by setting the product equal to the identity. Here, substituting $g_2=g^{-1}$ turns $g_1g_2$ into the constant map $e$, whose pull-back vanishes because a constant map has zero differential, and the product rule immediately yields $(g^{-1})^*\theta=-\operatorname{Ad}_g(g^*\theta)$. The transferable lesson: whenever you have an identity for a binary operation and you want the corresponding statement for the unary inverse, look for the specialisation in which the binary output degenerates. This is the same move as deriving $(ab)^{-1}=b^{-1}a^{-1}$ from associativity, or reading off the derivative of $x^{-1}$ from the product rule and $x\cdot x^{-1}=1$; the appearance of the constant $e$ and the vanishing pull-back is its geometric incarnation. Note also the sign and the $\operatorname{Ad}_g$ (not $\operatorname{Ad}_{g^{-1}}$): both are forced by the algebra and are easy to misremember, so the constant-collapse derivation is worth keeping as the reliable way to reconstruct them.

**This one identity is the source of every local gauge-transformation law in the chapter, which is why it is proved once and cited thereafter.** When a connection's local form $A_s=s^*\omega$ is recomputed for a new local section $s'=s\cdot g$, the change of section moves the evaluation point along the fibre by the group-valued function $g$, and the resulting transformation $A_{s'}=\operatorname{Ad}_{g^{-1}}A_s+g^*\theta$ carries an inhomogeneous term $g^*\theta$ that is exactly the pull-back of the Maurer–Cartan form; the consistency of such transformations across triple overlaps of trivialisations is precisely the product rule proved here, applied to a cocycle relation $g_{\alpha\gamma}=g_{\alpha\beta}g_{\beta\gamma}$. So the payoff of isolating this exercise is that [[Thm - Transformation of Local Connection and Curvature Forms|the transformation theorem for local connection and curvature forms]] (Bär's Theorem 2.3.6, Haydys's Theorem 2.2.5) can invoke "$(g_1g_2)^*\theta=\operatorname{Ad}_{g_2^{-1}}(g_1^*\theta)+g_2^*\theta$" as a named lemma rather than re-deriving the differential of multiplication inside each proof. The same identity reappears whenever gauge transformations compose (the reduced gauge group acts on connections by this rule) and is the algebraic root of why the space of connections is affine rather than linear: the pull-back of $\theta$ is the affine offset. A companion computation is [[Ex - The Differential of the Right Action Map|the differential of the right action map on a principal bundle]], which is the same product-rule mechanism carried out for the action map $\hat R\colon P\times G\to P$ instead of $m\colon G\times G\to G$.
