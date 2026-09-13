---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Constructions on Representations"
  - "Def - Representation of a Lie Group"
  - "Def - Dual Space"
  - "Def - Dual Map"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $G$ be a Lie group, let $V$ be a finite-dimensional vector space over $\mathbb{K}$ (with $\mathbb{K}=\mathbb{R}$ or $\mathbb{K}=\mathbb{C}$), and let $\varrho\colon G\to\operatorname{Aut}(V)$ be a representation of $G$. Write $V^{*}=\operatorname{Hom}(V,\mathbb{K})$ for the dual space of $V$, and for a linear automorphism $A\colon V\to V$ write $A^{*}\colon V^{*}\to V^{*}$ for its dual (transpose) map, defined by $A^{*}(\lambda)=\lambda\circ A$ for $\lambda\in V^{*}$.

Prove the following three statements.

1. **The naive dual is an anti-homomorphism.** The assignment $g\mapsto\varrho(g)^{*}$ satisfies
$$\varrho(g_{1}g_{2})^{*}=\varrho(g_{2})^{*}\,\varrho(g_{1})^{*}\qquad\text{for all }g_{1},g_{2}\in G,$$
so it reverses the order of multiplication and is therefore not a representation in general.

2. **The inverse repairs it.** The assignment
$$\varrho^{*}\colon G\to\operatorname{Aut}(V^{*}),\qquad \varrho^{*}(g):=\varrho(g^{-1})^{*}$$
is a genuine representation of $G$ on $V^{*}$ — the **dual** (or **contragredient**) representation.

3. **Identification for the standard representation of $GL(n)$.** For $G=GL(n;\mathbb{K})$ and the standard representation $\varrho_{\mathrm{st}}=\operatorname{id}\colon GL(n;\mathbb{K})\to GL(n;\mathbb{K})$ on $V=\mathbb{K}^{n}$, the dual representation is, in the dual basis,
$$\varrho_{\mathrm{st}}^{*}(g)=\bigl(g^{-1}\bigr)^{t}=\bigl(g^{t}\bigr)^{-1}\qquad(g\in GL(n;\mathbb{K})).$$
Verify moreover that the natural evaluation pairing $\langle\,\cdot\,,\cdot\,\rangle\colon V^{*}\times V\to\mathbb{K}$, $\langle\lambda,v\rangle=\lambda(v)$, is $G$-invariant: $\langle\varrho^{*}(g)\lambda,\varrho(g)v\rangle=\langle\lambda,v\rangle$ for all $g\in G$, $\lambda\in V^{*}$, $v\in V$.

This is the exercise underlying B's Theorem 1.3.3 and Remark 1.3.3.

**Recall.**

The objects in play are a representation of a Lie group, the dual space and dual map of linear algebra, and the dual construction on representations.

![[Def - Representation of a Lie Group#The Definition]]

A [[Def - Representation of a Lie Group|representation]] of $G$ is a Lie group homomorphism $\varrho\colon G\to\operatorname{Aut}(V)$; in particular $\varrho(g_{1}g_{2})=\varrho(g_{1})\varrho(g_{2})$ and $\varrho(e)=\operatorname{id}_{V}$, so also $\varrho(g^{-1})=\varrho(g)^{-1}$.

![[Def - Constructions on Representations#The Definition]]

The relevant construction is the **dual representation** $\varrho^{*}(g)=\varrho(g^{-1})^{*}$; the whole point of this exercise is to see why the inverse is forced.

For the **dual space** and the **dual map** we recall the two facts from linear algebra that the argument uses. First, for the dual map $A^{*}(\lambda)=\lambda\circ A$ the dual construction is **contravariant**: for linear maps $A,B\colon V\to V$,
$$(AB)^{*}=B^{*}A^{*},\qquad\text{and}\qquad(\operatorname{id}_{V})^{*}=\operatorname{id}_{V^{*}}.$$
Both are recalled with proof in [[Def - Dual Map|the dual-map page]] and are re-derived in Step 0 below so this page stands alone. Second, in a basis $e_{1},\dots,e_{n}$ of $V=\mathbb{K}^{n}$ with **dual basis** $e^{1},\dots,e^{n}$ (characterised by $e^{i}(e_{j})=\delta^{i}_{j}$), the matrix of $A^{*}$ is the transpose of the matrix of $A$: if $A e_{j}=\sum_{i}A_{ij}e_{i}$ then $A^{*}e^{j}=\sum_{i}A_{ji}e^{i}$; see [[Def - Dual Basis|the dual-basis page]]. This too is verified in Step 0.

---

# Convergent Strategy

**Problem class.** This is a *repair-the-homomorphism* problem: a natural-looking construction (send each operator to its dual) is built out of a functor that reverses composition, and we must diagnose the reversal and cancel it. The deliverable is not a hard computation but a precise bookkeeping of *which maps are covariant and which are contravariant*, so the whole exercise is an application of the identity $(AB)^{*}=B^{*}A^{*}$ read against the group law $\varrho(g_{1}g_{2})=\varrho(g_{1})\varrho(g_{2})$.

**Assumption pattern.** The single structural fact used is that the dual construction on linear maps is *contravariant* — it turns a product $AB$ into the reversed product $B^{*}A^{*}$. Anything contravariant composed with the *anti*-automorphism $g\mapsto g^{-1}$ of the group (which also reverses order, $(g_{1}g_{2})^{-1}=g_{2}^{-1}g_{1}^{-1}$) becomes *covariant* again: two order-reversals compose to an order-preservation. Recognising this "two wrongs make a right" is the entire content.

**Theorem routing.** For part 1, expand $\varrho(g_{1}g_{2})^{*}$ using the homomorphism property of $\varrho$ and then the contravariance $(AB)^{*}=B^{*}A^{*}$. For part 2, apply part 1 to $g\mapsto\varrho(g^{-1})^{*}$ and use $(g_{1}g_{2})^{-1}=g_{2}^{-1}g_{1}^{-1}$ so the two reversals cancel; then check the identity and smoothness clauses that promote a group homomorphism to a representation. For part 3, pass to matrices through the dual-basis rule $[A^{*}]=[A]^{t}$ and substitute $A=g^{-1}$.

**Key decision point.** The one genuine decision is *not* to try to fix the naive dual by any device other than the group inverse. One might hope that transposing differently, or conjugating, would restore a homomorphism; the exercise shows that the obstruction is exactly one order-reversal, and the group already carries a canonical order-reversing operation — inversion — so composing with it is both the simplest and the only natural cure. Everything else is substitution.

---

# Legal Operations Used

1. **Expanding a representation across a product** (the homomorphism defining property of a representation, operation "unfold $\varrho(g_{1}g_{2})=\varrho(g_{1})\varrho(g_{2})$" from the [[Def - Representation of a Lie Group|representation]] page). *Trigger:* an expression $\varrho(g_{1}g_{2})$ appears. *Pattern:* replace it by $\varrho(g_{1})\varrho(g_{2})$ to expose the two factors on which the dual will act.

2. **Contravariance of the dual map** ($(AB)^{*}=B^{*}A^{*}$, from the [[Def - Dual Map|dual-map]] page; re-proved in Step 0). *Trigger:* the dual of a composite operator. *Pattern:* split the dual of a product into the product of duals *in reversed order*.

3. **Inversion reverses order in a group** ($(g_{1}g_{2})^{-1}=g_{2}^{-1}g_{1}^{-1}$, a group axiom consequence). *Trigger:* an inverse of a product. *Pattern:* distribute the inverse across the product with the factors swapped; this is the second order-reversal that cancels the first.

4. **The dual-basis transpose rule** ($[A^{*}]=[A]^{t}$ in dual bases, from [[Def - Dual Basis]]; re-proved in Step 0). *Trigger:* one wants the matrix of a dual map. *Pattern:* transpose the matrix of the original map.

---

# Hints

> [!note]- Hint 1
> Write out $\varrho(g_{1}g_{2})^{*}$ by first using that $\varrho$ is a homomorphism, and only then applying the rule for the dual of a product. Keep careful track of the *order* of the two factors before and after each step.

> [!note]- Hint 2
> For part 2, do not start from scratch: apply the result of part 1 to the map $g\mapsto\varrho(g^{-1})^{*}$. The extra ingredient you need is how the group inverse interacts with a product of two elements.

> [!note]- Hint 3
> For part 3, everything reduces to the single linear-algebra fact that, in dual bases, the matrix of $A^{*}$ is the transpose of the matrix of $A$. Apply it with $A=\varrho_{\mathrm{st}}(g^{-1})=g^{-1}$.

> [!note]- Hint 4
> The invariance of the pairing is a one-line computation: unwind $\langle\varrho^{*}(g)\lambda,\varrho(g)v\rangle$ using the definitions $\varrho^{*}(g)=\varrho(g^{-1})^{*}$ and $A^{*}(\lambda)=\lambda\circ A$, and use that $\varrho(g^{-1})\varrho(g)=\operatorname{id}_{V}$.

---

# Solution

The plan is to establish the two linear-algebra facts we depend on (Step 0), then read off part 1 as a direct combination of the homomorphism property and contravariance, promote it to part 2 by cancelling the two order-reversals and checking the remaining representation clauses, and finally specialise to matrices for part 3, closing with the invariance of the pairing.

**Step 0: The two linear-algebra facts. — establishes contravariance $(AB)^{*}=B^{*}A^{*}$ and the transpose rule $[A^{*}]=[A]^{t}$, so the page is self-contained.**

> [!note]- Derivation
> Let $A,B\colon V\to V$ be linear and $\lambda\in V^{*}$. By the definition of the dual map, for every $\lambda$,
> $$(AB)^{*}(\lambda)=\lambda\circ(AB)\qquad\text{(definition } C^{*}(\lambda)=\lambda\circ C\text{ with }C=AB),$$
> $$=(\lambda\circ A)\circ B\qquad\text{(associativity of composition of maps)},$$
> $$=B^{*}(\lambda\circ A)\qquad\text{(definition of }B^{*}\text{ applied to the functional }\lambda\circ A),$$
> $$=B^{*}\bigl(A^{*}(\lambda)\bigr)=\bigl(B^{*}A^{*}\bigr)(\lambda)\qquad\text{(definition of }A^{*}\text{, then composition of }B^{*}\text{ after }A^{*}).$$
> Since this holds for every $\lambda\in V^{*}$, we conclude $(AB)^{*}=B^{*}A^{*}$. Taking $A=B=\operatorname{id}_{V}$, or directly, $(\operatorname{id}_{V})^{*}(\lambda)=\lambda\circ\operatorname{id}_{V}=\lambda$, so $(\operatorname{id}_{V})^{*}=\operatorname{id}_{V^{*}}$.
>
> For the transpose rule, fix a basis $e_{1},\dots,e_{n}$ of $V$ with dual basis $e^{1},\dots,e^{n}$, $e^{i}(e_{j})=\delta^{i}_{j}$, and let $A$ have matrix $A_{ij}$, meaning $Ae_{j}=\sum_{i}A_{ij}e_{i}$. Then, evaluating the functional $A^{*}(e^{k})=e^{k}\circ A$ on the basis vector $e_{j}$,
> $$\bigl(A^{*}e^{k}\bigr)(e_{j})=e^{k}(Ae_{j})=e^{k}\Bigl(\textstyle\sum_{i}A_{ij}e_{i}\Bigr)=\sum_{i}A_{ij}\,e^{k}(e_{i})=A_{kj}\qquad\text{(linearity of }e^{k}\text{ and }e^{k}(e_{i})=\delta^{k}_{i}).$$
> A functional on $V$ is determined by its values on the basis $e_{1},\dots,e_{n}$, and $\sum_{i}A_{ki}e^{i}$ takes the value $A_{kj}$ on $e_{j}$; hence $A^{*}e^{k}=\sum_{i}A_{ki}e^{i}$. The matrix of $A^{*}$ in the dual basis therefore has $(i,k)$ entry $A_{ki}$, that is $[A^{*}]=[A]^{t}$.

**Step 1: The naive dual reverses order (part 1). — proves $\varrho(g_{1}g_{2})^{*}=\varrho(g_{2})^{*}\varrho(g_{1})^{*}$.**

> [!note]- Derivation
> Fix $g_{1},g_{2}\in G$. Then
> $$\varrho(g_{1}g_{2})^{*}=\bigl(\varrho(g_{1})\,\varrho(g_{2})\bigr)^{*}\qquad\text{(}\varrho\text{ is a homomorphism, operation 1)}$$
> $$=\varrho(g_{2})^{*}\,\varrho(g_{1})^{*}\qquad\text{(contravariance }(AB)^{*}=B^{*}A^{*}\text{ from Step 0, with }A=\varrho(g_{1}),\ B=\varrho(g_{2})\text{; operation 2).}$$
> The factors have swapped order. Thus $g\mapsto\varrho(g)^{*}$ satisfies $\varrho(g_{1}g_{2})^{*}=\varrho(g_{2})^{*}\varrho(g_{1})^{*}$, which is the defining relation of an *anti*-homomorphism. Unless $\varrho(g_{1})^{*}$ and $\varrho(g_{2})^{*}$ commute for all $g_{1},g_{2}$ — which fails whenever the image of $\varrho$ is non-abelian — this is *not* the homomorphism relation $\varrho(g_{1}g_{2})^{*}=\varrho(g_{1})^{*}\varrho(g_{2})^{*}$, so $g\mapsto\varrho(g)^{*}$ is not a representation.

**Step 2: The inverse cancels the reversal (part 2). — proves $\varrho^{*}(g)=\varrho(g^{-1})^{*}$ is a representation.**

> [!note]- Derivation
> Define $\varrho^{*}(g)=\varrho(g^{-1})^{*}$. First, each $\varrho^{*}(g)$ is an automorphism of $V^{*}$: $\varrho(g^{-1})\in\operatorname{Aut}(V)$, and the dual of an invertible map is invertible (its inverse is $(\varrho(g^{-1})^{-1})^{*}=\varrho(g)^{*}$, using Step 0 with $(\varrho(g^{-1})^{-1})^{*}\varrho(g^{-1})^{*}=(\varrho(g^{-1})\varrho(g^{-1})^{-1})^{*}=(\operatorname{id})^{*}=\operatorname{id}$), so $\varrho^{*}(g)\in\operatorname{Aut}(V^{*})$.
>
> Now the homomorphism property. For $g_{1},g_{2}\in G$,
> $$\varrho^{*}(g_{1}g_{2})=\varrho\bigl((g_{1}g_{2})^{-1}\bigr)^{*}=\varrho\bigl(g_{2}^{-1}g_{1}^{-1}\bigr)^{*}\qquad\text{((}g_{1}g_{2}\text{)}^{-1}=g_{2}^{-1}g_{1}^{-1}\text{, operation 3)}$$
> $$=\varrho\bigl(g_{1}^{-1}\bigr)^{*}\,\varrho\bigl(g_{2}^{-1}\bigr)^{*}\qquad\text{(Step 1 applied to the pair }g_{2}^{-1},g_{1}^{-1}\text{: }\varrho(g_{2}^{-1}g_{1}^{-1})^{*}=\varrho(g_{1}^{-1})^{*}\varrho(g_{2}^{-1})^{*}\text{)}$$
> $$=\varrho^{*}(g_{1})\,\varrho^{*}(g_{2})\qquad\text{(definition of }\varrho^{*}\text{).}$$
> The two order-reversals — the one from inversion in operation 3, and the one from contravariance inside Step 1 — have cancelled, restoring the correct order. Next, the identity:
> $$\varrho^{*}(e)=\varrho(e^{-1})^{*}=\varrho(e)^{*}=(\operatorname{id}_{V})^{*}=\operatorname{id}_{V^{*}}\qquad\text{(}\varrho(e)=\operatorname{id}_{V}\text{ since }\varrho\text{ is a homomorphism, then Step 0).}$$
> Finally, smoothness. The inversion map $\iota\colon G\to G$, $g\mapsto g^{-1}$, is smooth (a Lie group axiom); $\varrho\colon G\to\operatorname{Aut}(V)$ is smooth (it is a representation); and the dual map $\operatorname{Aut}(V)\to\operatorname{Aut}(V^{*})$, $A\mapsto A^{*}$, is smooth because in fixed dual bases it is the linear map "transpose", $[A^{*}]=[A]^{t}$ (Step 0), whose matrix entries are (linear, hence smooth) functions of the entries of $A$. The composite $\varrho^{*}=(\,\cdot\,)^{*}\circ\varrho\circ\iota$ is therefore smooth. A smooth group homomorphism $G\to\operatorname{Aut}(V^{*})$ is exactly a representation, so $\varrho^{*}$ is a representation of $G$ on $V^{*}$.

**Step 3: The dual of the standard representation of $GL(n)$ (part 3). — identifies $\varrho_{\mathrm{st}}^{*}(g)=(g^{-1})^{t}$ and checks pairing-invariance.**

> [!note]- Derivation
> Take $G=GL(n;\mathbb{K})$, $V=\mathbb{K}^{n}$ with its standard basis $e_{1},\dots,e_{n}$, and $\varrho_{\mathrm{st}}=\operatorname{id}$, so $\varrho_{\mathrm{st}}(g)=g$ acts as the matrix $g$. Then, using the definition of the dual representation and the transpose rule of Step 0 in the dual basis,
> $$\varrho_{\mathrm{st}}^{*}(g)=\varrho_{\mathrm{st}}(g^{-1})^{*}=\bigl(g^{-1}\bigr)^{*}\quad\Longrightarrow\quad\bigl[\varrho_{\mathrm{st}}^{*}(g)\bigr]=\bigl[g^{-1}\bigr]^{t}=\bigl(g^{-1}\bigr)^{t}\qquad\text{(}[A^{*}]=[A]^{t}\text{ with }A=g^{-1}\text{).}$$
> Since transpose and inverse commute, $(g^{-1})^{t}=(g^{t})^{-1}$; either form is the matrix of $\varrho_{\mathrm{st}}^{*}(g)$. As an independent check that this is a homomorphism, compute directly
> $$\bigl((g_{1}g_{2})^{-1}\bigr)^{t}=\bigl(g_{2}^{-1}g_{1}^{-1}\bigr)^{t}=\bigl(g_{1}^{-1}\bigr)^{t}\bigl(g_{2}^{-1}\bigr)^{t}\qquad\text{((}XY\text{)}^{t}=Y^{t}X^{t}\text{ and (}g_{1}g_{2}\text{)}^{-1}=g_{2}^{-1}g_{1}^{-1}\text{),}$$
> which is $\varrho_{\mathrm{st}}^{*}(g_{1})\,\varrho_{\mathrm{st}}^{*}(g_{2})$: the two transposition-reversals again cancel, in matrix form.
>
> Invariance of the pairing. For $g\in G$, $\lambda\in V^{*}$, $v\in V$,
> $$\langle\varrho^{*}(g)\lambda,\varrho(g)v\rangle=\bigl(\varrho(g^{-1})^{*}\lambda\bigr)\bigl(\varrho(g)v\bigr)\qquad\text{(definitions of the pairing and of }\varrho^{*}(g)=\varrho(g^{-1})^{*}\text{)}$$
> $$=\bigl(\lambda\circ\varrho(g^{-1})\bigr)\bigl(\varrho(g)v\bigr)\qquad\text{(definition }A^{*}(\lambda)=\lambda\circ A\text{ with }A=\varrho(g^{-1})\text{)}$$
> $$=\lambda\bigl(\varrho(g^{-1})\varrho(g)v\bigr)=\lambda\bigl(\varrho(g^{-1}g)v\bigr)=\lambda(v)=\langle\lambda,v\rangle\qquad\text{(}\varrho\text{ homomorphism, }g^{-1}g=e\text{, }\varrho(e)=\operatorname{id}_{V}\text{).}$$
> Thus the evaluation pairing is $G$-invariant. This is in fact the *defining* property of the dual representation: $\varrho^{*}$ is the unique representation on $V^{*}$ making $\langle\,\cdot\,,\cdot\,\rangle$ invariant, and demanding invariance forces precisely the factor $\varrho(g^{-1})$.

> [!note]- Complete formal solution
> Let $G$ be a Lie group, $V$ a finite-dimensional $\mathbb{K}$-vector space, and $\varrho\colon G\to\operatorname{Aut}(V)$ a representation. For a linear $A\colon V\to V$ let $A^{*}\colon V^{*}\to V^{*}$, $A^{*}(\lambda)=\lambda\circ A$.
>
> *Preliminaries.* For linear $A,B\colon V\to V$ and $\lambda\in V^{*}$, $(AB)^{*}(\lambda)=\lambda\circ AB=(\lambda\circ A)\circ B=B^{*}(\lambda\circ A)=B^{*}A^{*}(\lambda)$, so $(AB)^{*}=B^{*}A^{*}$; and $(\operatorname{id}_{V})^{*}(\lambda)=\lambda$, so $(\operatorname{id}_{V})^{*}=\operatorname{id}_{V^{*}}$. In dual bases $e_{i},e^{j}$ with $e^{i}(e_{j})=\delta^{i}_{j}$: if $Ae_{j}=\sum_{i}A_{ij}e_{i}$ then $(A^{*}e^{k})(e_{j})=e^{k}(Ae_{j})=A_{kj}$, so $A^{*}e^{k}=\sum_{i}A_{ki}e^{i}$ and $[A^{*}]=[A]^{t}$.
>
> *Part 1.* For $g_{1},g_{2}\in G$: $\varrho(g_{1}g_{2})^{*}=(\varrho(g_{1})\varrho(g_{2}))^{*}=\varrho(g_{2})^{*}\varrho(g_{1})^{*}$, using that $\varrho$ is a homomorphism and then $(AB)^{*}=B^{*}A^{*}$. Hence $g\mapsto\varrho(g)^{*}$ is an anti-homomorphism; because the order is reversed, it is not a homomorphism unless the image is abelian, so it is not a representation in general.
>
> *Part 2.* Set $\varrho^{*}(g)=\varrho(g^{-1})^{*}$. Each $\varrho^{*}(g)\in\operatorname{Aut}(V^{*})$ since the dual of an invertible map is invertible. For $g_{1},g_{2}\in G$,
> $$\varrho^{*}(g_{1}g_{2})=\varrho((g_{1}g_{2})^{-1})^{*}=\varrho(g_{2}^{-1}g_{1}^{-1})^{*}=\varrho(g_{1}^{-1})^{*}\varrho(g_{2}^{-1})^{*}=\varrho^{*}(g_{1})\varrho^{*}(g_{2}),$$
> where the third equality is Part 1 applied to the pair $(g_{2}^{-1},g_{1}^{-1})$ and the second is $(g_{1}g_{2})^{-1}=g_{2}^{-1}g_{1}^{-1}$. Also $\varrho^{*}(e)=(\operatorname{id}_{V})^{*}=\operatorname{id}_{V^{*}}$. Smoothness: $\varrho^{*}=(\,\cdot\,)^{*}\circ\varrho\circ\iota$ with $\iota(g)=g^{-1}$ smooth, $\varrho$ smooth, and $A\mapsto A^{*}$ smooth (it is the linear "transpose" in fixed dual bases). Therefore $\varrho^{*}$ is a representation.
>
> *Part 3.* For $G=GL(n;\mathbb{K})$, $\varrho_{\mathrm{st}}=\operatorname{id}$ on $\mathbb{K}^{n}$: $\varrho_{\mathrm{st}}^{*}(g)=(g^{-1})^{*}$ has matrix $[g^{-1}]^{t}=(g^{-1})^{t}=(g^{t})^{-1}$ in the dual basis. Directly, $((g_{1}g_{2})^{-1})^{t}=(g_{2}^{-1}g_{1}^{-1})^{t}=(g_{1}^{-1})^{t}(g_{2}^{-1})^{t}$, confirming the homomorphism property. Finally, for all $g,\lambda,v$,
> $$\langle\varrho^{*}(g)\lambda,\varrho(g)v\rangle=(\lambda\circ\varrho(g^{-1}))(\varrho(g)v)=\lambda(\varrho(g^{-1}g)v)=\lambda(v),$$
> so the evaluation pairing is $G$-invariant. $\blacksquare$

> [!warning] Illegal but tempting route
> One is tempted to declare $\varrho^{\vee}(g):=\varrho(g)^{*}$ "the" dual representation and to *hope* it is a homomorphism, or to patch it by transposing in the other index order. Neither works: the obstruction computed in Step 1 is a genuine reversal of multiplication order, present for every non-abelian image, and no relabelling of indices removes it. The only structure-respecting cure is to feed in $g^{-1}$, because inversion is the canonical order-reversing map on the group and its reversal exactly annihilates the reversal coming from the dual. The naive assignment $g\mapsto\varrho(g)^{*}$ does happen to be a homomorphism precisely when $\varrho$ has abelian image — for instance for any representation of $U(1)$ — because there the anti-homomorphism relation $\varrho(g_{1}g_{2})^{*}=\varrho(g_{2})^{*}\varrho(g_{1})^{*}$ collapses to the homomorphism relation once the two factors commute, so the order-reversal is harmless. Even then it is not the same representation as the contragredient $\varrho^{*}(g)=\varrho(g^{-1})^{*}$ — the two differ by the substitution $g\mapsto g^{-1}$, and for $U(1)$ acting by $z\mapsto z^{k}$ they are the genuinely distinct representations $z\mapsto z^{k}$ and $z\mapsto z^{-k}$. As a *general* definition, valid on every group, only $\varrho(g^{-1})^{*}$ is correct.

---

# Key Takeaways

The reusable principle is that *the dual construction on linear maps is contravariant, and contravariance composed with a second order-reversal becomes covariant.* Whenever a natural map is built by dualising (or, more generally, by any operation that turns $AB$ into $B^{*}A^{*}$ — pullback of functions, adjoint of operators, transpose of matrices, opposite of a category), a bare assignment $g\mapsto(\text{dual of }\varrho(g))$ will be an anti-homomorphism, and the fix is always to precompose with the group inverse. The trigger to watch for is the phrase "the dual/adjoint/transpose of a representation": it is never $\varrho(g)^{*}$, always $\varrho(g^{-1})^{*}$, and forgetting the inverse silently produces an object that fails to be a representation on every non-abelian group.

A second, transferable diagnostic is the *invariant-pairing characterisation*. Rather than memorising where the inverse goes, one can derive it: demand that the canonical pairing $\langle\lambda,v\rangle=\lambda(v)$ between $V^{*}$ and $V$ be $G$-invariant, $\langle\varrho^{*}(g)\lambda,\varrho(g)v\rangle=\langle\lambda,v\rangle$, and solve for $\varrho^{*}(g)$; invariance forces $\varrho^{*}(g)=\varrho(g^{-1})^{*}$ uniquely. This is the same move that later fixes the transformation law of covectors under a change of frame, the contragredient action on sections of a dual bundle, and the way structure groups act on associated bundles built from $V^{*}$: the pairing that must survive dictates the inverse. Carrying the *reason* (an invariant pairing) rather than the *formula* (an inverse) is what makes the rule transfer without error.

Finally, the matrix shadow $\varrho_{\mathrm{st}}^{*}(g)=(g^{-1})^{t}=(g^{t})^{-1}$ is worth keeping in the hand. It is the concrete face of the contragredient representation and it reappears constantly: it is how $GL(n)$ acts on row vectors versus column vectors, and how the cotangent bundle transforms against the tangent bundle. Restricted to the orthogonal subgroup, where $g^{-1}=g^{t}$, it gives $\varrho_{\mathrm{st}}^{*}(g)=(g^{-1})^{t}=g$, so the standard representation of $O(n)$ is *self-dual*; restricted to the unitary subgroup, where $g^{-1}=g^{*}$ (the conjugate transpose), it gives $\varrho_{\mathrm{st}}^{*}(g)=(g^{-1})^{t}=\overline{g}$, so the dual of the standard representation of $U(n)$ is its *complex conjugate* representation rather than itself. Companion exercises in this section that lean on the same construction are [[Ex - Tensor Products and Duals of the Representations of U(1)]], where $\varrho_{k}^{*}\cong\varrho_{-k}$ is exactly this inverse showing up as $z\mapsto z^{-k}$, and [[Ex - rho_2 of SU(2) is the Complexified Adjoint Representation]], where self-duality of $\varrho_{2}$ is one reading of why the adjoint representation is real.
