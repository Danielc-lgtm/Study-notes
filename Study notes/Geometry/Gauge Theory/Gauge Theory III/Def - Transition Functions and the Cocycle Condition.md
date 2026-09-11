---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Def - Transition Function of a Vector Bundle"
  - "Def - Free, Transitive, Effective, and Proper Group Actions"
  - "Def - Frame Bundle of a Vector Bundle"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a [[Def - Lie Group|Lie group]] with identity element $e$, and $\pi\colon P\to M$ is a [[Def - Principal G-Bundle|principal $G$-bundle]] over a smooth manifold $M$. We follow the series convention that $G$ acts on $P$ on the **right**: the action is written $R_g(p) = p\cdot g$, it preserves fibres ($\pi(p\cdot g) = \pi(p)$), it is **free** (if $p\cdot g = p$ for some $p$ then $g = e$), and it is **transitive on each fibre** (for $p, q$ in the same fibre $P_x := \pi^{-1}(x)$ there is $g\in G$ with $q = p\cdot g$); these three properties are the substance of the definition of a principal bundle recalled at the point of use below. For $x\in M$, $P_x$ denotes the fibre over $x$. A **local section** over an open set $U\subseteq M$ is a smooth map $s\colon U\to P$ with $\pi\circ s = \operatorname{id}_U$; the [[Thm - Sections of a Principal Bundle and Triviality|section–triviality theorem]] shows local sections over $U$ correspond bijectively to $G$-equivariant local trivialisations over $U$, so a section exists over $U$ precisely when $P|_U := \pi^{-1}(U)$ is trivial.

We fix once and for all an open cover $\{U_\alpha\}_{\alpha\in A}$ of $M$ by sets over which $P$ is trivial, together with a choice of local section $s_\alpha\colon U_\alpha\to P$ for each $\alpha$. We abbreviate $U_{\alpha\beta} := U_\alpha\cap U_\beta$ and $U_{\alpha\beta\gamma} := U_\alpha\cap U_\beta\cap U_\gamma$. The symbol $g_{\alpha\beta}$ always denotes the transition function defined below, a smooth map $U_{\alpha\beta}\to G$; $h_\alpha$ always denotes a smooth map $U_\alpha\to G$ recording a change of local section; and $\bigsqcup$ denotes a disjoint union. Multiplication and inversion in $G$ are smooth because $G$ is a Lie group, a fact used whenever we assert that a $G$-valued map assembled from smooth pieces is again smooth.

> [!warning] Convention: which section is expressed in terms of which
> We adopt Bär's convention (Wernli's notes, §2.2), in which the transition function $g_{\alpha\beta}$ expresses the section $s_\beta$ in terms of the section $s_\alpha$:
> $$s_\beta = s_\alpha\cdot g_{\alpha\beta}\qquad\text{on }U_{\alpha\beta}.$$
> Haydys instead writes the change of local frame of a vector bundle as $e = e'\cdot g$ with $g\colon U\cap U'\to GL_k(\mathbb{R})$ (equation (6) of his notes), the new frame $e$ expressed through the old frame $e'$. **These are the same convention after renaming:** identify Haydys's primed frame $e'$ with $s_\alpha$ and his unprimed frame $e$ with $s_\beta$, and his $g$ becomes $g_{\alpha\beta}$, so that $e = e'\cdot g$ reads $s_\beta = s_\alpha\cdot g_{\alpha\beta}$. A reader coming from a source that writes $s_\alpha = s_\beta\cdot g_{\alpha\beta}$ (the opposite placement of indices) obtains our $g_{\alpha\beta}$ as their $g_{\beta\alpha}$; every formula below is stated in the $s_\beta = s_\alpha g_{\alpha\beta}$ convention and must be transposed accordingly.

This is a compound page. It defines four interlocking notions — the **transition functions** $g_{\alpha\beta}$ of a principal bundle relative to a choice of local sections, the **cocycle conditions** they satisfy, the **coboundary relation** between the transition functions of two different choices of sections, and the **reconstruction data** $\bigsqcup_\alpha U_\alpha\times G/\!\sim$ from which a bundle is rebuilt — because these are not four separate ideas but one idea seen from four sides: a principal bundle is a recipe for gluing trivial pieces $U_\alpha\times G$, the transition functions are that recipe, the cocycle conditions are exactly the constraints a recipe must meet, and the coboundary relation is what happens to the recipe when the bookkeeping (the choice of sections) changes.

---

# Axiom Motivation

We want to reduce a principal bundle, which is a global object, to a finite amount of local data that we can write down, compute with, and prescribe by hand. The model to imitate is the way a smooth manifold is captured by charts and their transition maps, or — closer to home — the way a [[Def - Vector Bundle|vector bundle]] is captured by its [[Def - Transition Function of a Vector Bundle|transition functions]]. In the vector-bundle case the data are the matrix-valued functions $\tau_{\alpha\beta}\colon U_{\alpha\beta}\to GL(k,\mathbb{R})$ that relate two local trivialisations on their overlap, and the whole bundle is recoverable from them. We ask for the principal-bundle analogue. The question is: **when two local sections of $P$ overlap, what relates them, and what constraints does that relating datum obey?**

Over $U_\alpha$ the bundle looks like the product $U_\alpha\times G$, and the section $s_\alpha$ names, at each point $x\in U_\alpha$, a preferred element $s_\alpha(x)$ of the fibre $P_x$ — a "local origin" or, in the language physicists use, a **local gauge**. Over the overlap $U_{\alpha\beta}$ we have two such preferred elements, $s_\alpha(x)$ and $s_\beta(x)$, both lying in the single fibre $P_x$. Because $G$ acts freely and transitively on $P_x$, that fibre is a **torsor**: it looks exactly like $G$, but with no distinguished identity element until a point is chosen as origin. Choosing $s_\alpha(x)$ as origin identifies $P_x$ with $G$; the other origin $s_\beta(x)$ then corresponds to a specific group element. That element is $g_{\alpha\beta}(x)$. So the transition function is forced upon us the moment we have two sections: it is the unique group element carrying one local origin to the other.

The first desideratum is therefore that $g_{\alpha\beta}(x)$ **exist and be unique** — this is where freeness and transitivity earn their place in the definition of a principal bundle. Drop transitivity and there might be no $g$ with $s_\beta(x) = s_\alpha(x)\cdot g$ at all: the two origins could lie in different orbits, and the two sections would describe unrelated data with no comparison between them. Drop freeness and the $g$ carrying $s_\alpha(x)$ to $s_\beta(x)$ would not be unique: if some $g_0\neq e$ fixed $s_\alpha(x)$, then $g_{\alpha\beta}(x)$ and $g_{\alpha\beta}(x)g_0$ would both work, the transition function would not be well-defined, and none of the algebra below would close up. The two conditions are exactly the two halves of "the fibre is a torsor", and they are exactly what makes the comparison of local gauges a single, unambiguous group element.

The second desideratum is **smoothness**. A datum that jumped discontinuously as $x$ moved across $U_{\alpha\beta}$ would be useless for the differential-geometric constructions to come (connections, curvature, characteristic classes), each of which differentiates the transition functions. Smoothness cannot be assumed; it must follow from the smoothness already present in the sections and in the bundle's trivialisations. We shall see that it does, precisely because $G$ is a Lie group, so that multiplication and inversion — the operations that express $g_{\alpha\beta}$ in terms of the smooth sections — are themselves smooth.

The third and deepest desideratum is **consistency across overlaps**. The transition functions are not free to be arbitrary. On a single set $U_\alpha$ the section relates to itself by nothing at all, forcing $g_{\alpha\alpha} = e$. On a double overlap the comparison of $s_\alpha$ with $s_\beta$ must be the reverse of the comparison of $s_\beta$ with $s_\alpha$, forcing $g_{\alpha\beta} = g_{\beta\alpha}^{-1}$. On a triple overlap $U_{\alpha\beta\gamma}$ we may pass from the $\alpha$-gauge to the $\gamma$-gauge either directly or by going through the $\beta$-gauge, and the two routes must agree, forcing $g_{\alpha\beta}g_{\beta\gamma}g_{\gamma\alpha} = e$. These three constraints are the **cocycle conditions**. They are not extra axioms imposed for convenience; they are automatic consequences of the definition of $g_{\alpha\beta}$, and — this is the payoff, proved as the next theorem [[Thm - Principal Bundles are Classified by Cocycles|Principal Bundles are Classified by Cocycles]] — they are *exactly* the conditions under which a family of prescribed $G$-valued functions can be glued back into a bundle. Weaken the triple condition and the reconstructed gluing relation $\sim$ ceases to be transitive, so it is not an equivalence relation and there is no well-defined quotient space; the "bundle" fails to exist. This is the principal-bundle echo of the failure analysed for vector bundles on [[Def - Transition Function of a Vector Bundle|the vector-bundle transition-function page]], where a family with $\tau_{12} = \tau_{23} = +1$ but $\tau_{13} = -1$ violates the cocycle condition and refuses to assemble.

There is a fourth thing the definition must record, once we accept that the sections are a *choice*. Nothing distinguishes $s_\alpha$ from another section $\tilde s_\alpha$ over the same set; a different choice gives different transition functions $\tilde g_{\alpha\beta}$, and we must know how the two systems compare, or we will mistake bookkeeping for geometry. The comparison is governed by the maps $h_\alpha\colon U_\alpha\to G$ with $\tilde s_\alpha = s_\alpha h_\alpha$, and it takes the form $g_{\alpha\beta} = h_\alpha\tilde g_{\alpha\beta}h_\beta^{-1}$, the **coboundary relation**. Two systems related in this way are called *cohomologous*, and they encode the same bundle; the transition data of a bundle is well-defined only up to this equivalence. This is the exact analogue of the coboundary equivalence $\tau'_{\alpha\beta} = g_\alpha\tau_{\alpha\beta}g_\beta^{-1}$ for vector bundles, and it is what makes "the bundle is its cocycle" a statement about equivalence classes rather than about a single system of functions.

Could a reader who understood only these paragraphs reinvent the definition? The demand "compare two local gauges by a single group element" forces $g_{\alpha\beta}$; freeness and transitivity are exactly what make the comparison exist and be unique; the requirement that the comparisons on different overlaps agree forces the cocycle conditions; and the recognition that sections are a choice forces the coboundary relation. Everything below is the disciplined statement and proof of these forced facts.

---

# The Definition

Fix the principal $G$-bundle $\pi\colon P\to M$, the trivialising cover $\{U_\alpha\}_{\alpha\in A}$, and the local sections $s_\alpha\colon U_\alpha\to P$ of the Notation section.

## Transition functions

**Definition (transition functions).** For $\alpha,\beta\in A$ with $U_{\alpha\beta}\neq\emptyset$, the **transition function** from the section $s_\alpha$ to the section $s_\beta$ is the map
$$g_{\alpha\beta}\colon U_{\alpha\beta}\to G$$
characterised by
$$s_\beta(x) = s_\alpha(x)\cdot g_{\alpha\beta}(x)\qquad\text{for all }x\in U_{\alpha\beta}.$$
The collection $\{g_{\alpha\beta}\}_{\alpha,\beta\in A}$ is the **cocycle** of $P$ relative to the sections $\{s_\alpha\}$.

That this map exists, is unique, and is smooth is not part of the raw statement but must be established; we do so now, because a definition that named an object which might fail to exist or fail to be well-defined would be empty.

> [!note]- Well-posedness of $g_{\alpha\beta}$: existence, uniqueness, smoothness (full proof)
> We must show three things: for each $x\in U_{\alpha\beta}$ there is at least one $g\in G$ with $s_\beta(x) = s_\alpha(x)\cdot g$ (existence); there is at most one (uniqueness), so that $g_{\alpha\beta}(x)$ is well-defined; and the resulting map $x\mapsto g_{\alpha\beta}(x)$ is smooth.
>
> **Step 0 — the two sections land in one fibre.** For $x\in U_{\alpha\beta}$ we have $\pi(s_\alpha(x)) = x = \pi(s_\beta(x))$ (since each $s_\gamma$ is a section, $\pi\circ s_\gamma = \operatorname{id}$), so both $s_\alpha(x)$ and $s_\beta(x)$ lie in the single fibre $P_x = \pi^{-1}(x)$. The comparison therefore takes place inside one orbit of the $G$-action, which is where the torsor property applies.
>
> **Existence.** By the definition of a [[Def - Principal G-Bundle|principal $G$-bundle]], the right $G$-action is **transitive on each fibre**: for any two points $p, q\in P_x$ there exists $g\in G$ with $q = p\cdot g$. Applying this with $p = s_\alpha(x)$ and $q = s_\beta(x)$ (both in $P_x$ by Step 0) yields a $g\in G$ with $s_\beta(x) = s_\alpha(x)\cdot g$ (by transitivity on the fibre $P_x$). Set $g_{\alpha\beta}(x) := g$.
>
> **Uniqueness.** Suppose $g, g'\in G$ both satisfy $s_\alpha(x)\cdot g = s_\beta(x) = s_\alpha(x)\cdot g'$. Then $s_\alpha(x)\cdot g = s_\alpha(x)\cdot g'$, and acting on the right by $g'^{-1}$ gives $s_\alpha(x)\cdot(g g'^{-1}) = s_\alpha(x)$ (since $(p\cdot a)\cdot b = p\cdot(ab)$ for a right action, and $g'g'^{-1}=e$ on the right factor). By the **freeness** of the action (if $p\cdot a = p$ then $a = e$), applied to $p = s_\alpha(x)$ and $a = gg'^{-1}$, we conclude $gg'^{-1} = e$, that is $g = g'$ (by freeness of the $G$-action). Hence $g_{\alpha\beta}(x)$ is unambiguously defined.
>
> **Smoothness.** Since $P|_{U_\alpha}$ is trivial and carries the section $s_\alpha$, the [[Thm - Sections of a Principal Bundle and Triviality|section–triviality theorem]] — *for a principal $G$-bundle, local sections over $U$ correspond bijectively to $G$-equivariant local trivialisations over $U$* — provides a $G$-equivariant smooth trivialisation
> $$\psi_\alpha\colon P|_{U_\alpha}\xrightarrow{\ \cong\ } U_\alpha\times G,\qquad \psi_\alpha(p) = \big(\pi(p),\varphi_\alpha(p)\big),$$
> whose second component $\varphi_\alpha\colon P|_{U_\alpha}\to G$ is smooth and equivariant, $\varphi_\alpha(p\cdot g) = \varphi_\alpha(p)\,g$ (this equivariance is exactly the statement $\psi_\alpha(p\cdot g) = \psi_\alpha(p)\cdot g$ that defines a principal-bundle trivialisation). Apply $\varphi_\alpha$ to the defining equation $s_\beta(x) = s_\alpha(x)\cdot g_{\alpha\beta}(x)$:
> $$\varphi_\alpha\big(s_\beta(x)\big) = \varphi_\alpha\big(s_\alpha(x)\cdot g_{\alpha\beta}(x)\big) = \varphi_\alpha\big(s_\alpha(x)\big)\cdot g_{\alpha\beta}(x)\qquad\text{(equivariance of }\varphi_\alpha\text{).}$$
> Solving for $g_{\alpha\beta}(x)$ by left-multiplying with the inverse of $\varphi_\alpha(s_\alpha(x))$ in $G$,
> $$g_{\alpha\beta}(x) = \varphi_\alpha\big(s_\alpha(x)\big)^{-1}\,\varphi_\alpha\big(s_\beta(x)\big)\qquad\text{(group axioms in }G\text{).}$$
> The two maps $x\mapsto \varphi_\alpha(s_\alpha(x))$ and $x\mapsto \varphi_\alpha(s_\beta(x))$ are smooth on $U_{\alpha\beta}$, being composites of the smooth sections $s_\alpha, s_\beta$ with the smooth map $\varphi_\alpha$. Because $G$ is a [[Def - Lie Group|Lie group]], the inversion map $G\to G$ and the multiplication map $G\times G\to G$ are smooth. Therefore $g_{\alpha\beta}$, being built from these smooth maps by inversion and multiplication, is smooth (composition of smooth maps). This completes the well-posedness of $g_{\alpha\beta}$. $\blacksquare$

## The cocycle conditions

The transition functions are not independent: they satisfy three algebraic identities, forced by the definition together with the freeness of the action. These are Bär's Theorem 2.2.10 (Wernli §2.2), which we prove in full.

**Proposition (cocycle conditions).** The transition functions satisfy
$$\text{(1)}\quad g_{\alpha\alpha} = e\ \text{ on }U_\alpha;\qquad \text{(2)}\quad g_{\alpha\beta} = g_{\beta\alpha}^{-1}\ \text{ on }U_{\alpha\beta};\qquad \text{(3)}\quad g_{\alpha\beta}\,g_{\beta\gamma}\,g_{\gamma\alpha} = e\ \text{ on }U_{\alpha\beta\gamma}.$$
Here $e$ denotes the constant map with value the identity of $G$, and all products are pointwise products of $G$-valued functions.

> [!note]- Full proof of the cocycle conditions
> Fix a point $x$ in the relevant intersection throughout; every equation is an equation in the group $G$, and every use of freeness is the implication "$p\cdot a = p\cdot b\Rightarrow a = b$", which is the uniqueness clause established in the well-posedness proof above (from $p\cdot(ab^{-1}) = p$ and freeness).
>
> **Identity, condition (1).** Taking $\beta = \alpha$ in the defining equation gives $s_\alpha(x) = s_\alpha(x)\cdot g_{\alpha\alpha}(x)$ (definition of $g_{\alpha\alpha}$). Comparing with the trivial identity $s_\alpha(x) = s_\alpha(x)\cdot e$ (the identity acts trivially), and cancelling the common left factor $s_\alpha(x)$ by **freeness**, we get $g_{\alpha\alpha}(x) = e$ (by freeness of the action). Since $x\in U_\alpha$ was arbitrary, $g_{\alpha\alpha} = e$.
>
> **Inverse, condition (2).** By the definitions of $g_{\alpha\beta}$ and $g_{\beta\alpha}$ on $U_{\alpha\beta}$,
> $$s_\beta(x) = s_\alpha(x)\cdot g_{\alpha\beta}(x)\qquad\text{and}\qquad s_\alpha(x) = s_\beta(x)\cdot g_{\beta\alpha}(x).$$
> Substituting the first into the second,
> $$s_\alpha(x) = \big(s_\alpha(x)\cdot g_{\alpha\beta}(x)\big)\cdot g_{\beta\alpha}(x) = s_\alpha(x)\cdot\big(g_{\alpha\beta}(x)\,g_{\beta\alpha}(x)\big)\qquad\text{(associativity of the right action, }(p\cdot a)\cdot b = p\cdot(ab)\text{).}$$
> Comparing with $s_\alpha(x) = s_\alpha(x)\cdot e$ and cancelling $s_\alpha(x)$ by **freeness** gives $g_{\alpha\beta}(x)\,g_{\beta\alpha}(x) = e$ (by freeness), that is $g_{\alpha\beta}(x) = g_{\beta\alpha}(x)^{-1}$ (definition of inverse in $G$). Hence $g_{\alpha\beta} = g_{\beta\alpha}^{-1}$.
>
> **Cocycle, condition (3).** Let $x\in U_{\alpha\beta\gamma}$, so all of $s_\alpha(x), s_\beta(x), s_\gamma(x)$ lie in $P_x$ and the three double transition functions are defined at $x$. Chaining the defining equations,
> $$s_\gamma(x) = s_\beta(x)\cdot g_{\beta\gamma}(x)\qquad\text{(definition of }g_{\beta\gamma}\text{)},$$
> and $s_\beta(x) = s_\alpha(x)\cdot g_{\alpha\beta}(x)$ (definition of $g_{\alpha\beta}$), so substituting,
> $$s_\gamma(x) = \big(s_\alpha(x)\cdot g_{\alpha\beta}(x)\big)\cdot g_{\beta\gamma}(x) = s_\alpha(x)\cdot\big(g_{\alpha\beta}(x)\,g_{\beta\gamma}(x)\big)\qquad\text{(associativity of the right action).}$$
> On the other hand, directly $s_\gamma(x) = s_\alpha(x)\cdot g_{\alpha\gamma}(x)$ (definition of $g_{\alpha\gamma}$). Comparing the two expressions for $s_\gamma(x)$ and cancelling $s_\alpha(x)$ by **freeness**,
> $$g_{\alpha\gamma}(x) = g_{\alpha\beta}(x)\,g_{\beta\gamma}(x)\qquad\text{(by freeness).}\tag{$*$}$$
> This is the multiplicative form of the cocycle condition. To obtain the symmetric form stated, right-multiply $(*)$ by $g_{\gamma\alpha}(x)$:
> $$g_{\alpha\beta}(x)\,g_{\beta\gamma}(x)\,g_{\gamma\alpha}(x) = g_{\alpha\gamma}(x)\,g_{\gamma\alpha}(x) = e\qquad\text{(by }(*)\text{, then by condition (2) with the pair }\alpha,\gamma\text{, which gives }g_{\alpha\gamma}g_{\gamma\alpha}=e\text{).}$$
> Since $x\in U_{\alpha\beta\gamma}$ was arbitrary, $g_{\alpha\beta}\,g_{\beta\gamma}\,g_{\gamma\alpha} = e$. Therefore all three cocycle conditions hold. $\blacksquare$

The multiplicative form $(*)$, $g_{\alpha\gamma} = g_{\alpha\beta}\,g_{\beta\gamma}$, is the one to remember: it says "$\alpha$-to-$\gamma$ equals $\alpha$-to-$\beta$ followed by $\beta$-to-$\gamma$", and it coincides exactly with the cocycle identity $\tau_{\alpha\gamma} = \tau_{\alpha\beta}\tau_{\beta\gamma}$ on the [[Def - Transition Function of a Vector Bundle|vector-bundle transition-function page]].

## The coboundary relation

Suppose we replace the sections $\{s_\alpha\}$ by a second system $\{\tilde s_\alpha\}$ over the same cover, obtaining transition functions $\{\tilde g_{\alpha\beta}\}$. On each $U_\alpha$ the two sections $s_\alpha, \tilde s_\alpha$ take values in the same fibre over each point, so by the existence–uniqueness argument above there is a unique smooth map $h_\alpha\colon U_\alpha\to G$ with $\tilde s_\alpha = s_\alpha\cdot h_\alpha$. This is Bär's equation (2.1) / Theorem 2.2.11 (Wernli §2.2).

**Proposition (coboundary relation).** With $\tilde s_\alpha = s_\alpha\, h_\alpha$ and $\tilde s_\beta = s_\beta\, h_\beta$ for smooth $h_\alpha, h_\beta\colon U_\alpha, U_\beta\to G$, the two systems of transition functions are related on $U_{\alpha\beta}$ by
$$g_{\alpha\beta} = h_\alpha\,\tilde g_{\alpha\beta}\,h_\beta^{-1},\qquad\text{equivalently}\qquad \tilde g_{\alpha\beta} = h_\alpha^{-1}\,g_{\alpha\beta}\,h_\beta.$$
Two systems $\{g_{\alpha\beta}\}$, $\{\tilde g_{\alpha\beta}\}$ so related by a family $\{h_\alpha\}$ are called **cohomologous**.

> [!note]- Full proof of the coboundary relation
> Fix $x\in U_{\alpha\beta}$; every equality is in $G$, and all products are the group products of the values at $x$, which we suppress for readability.
>
> **Assemble the four defining relations.** By the definitions of $\tilde g_{\alpha\beta}$ (for the tilde system) and of $h_\alpha, h_\beta$,
> $$\tilde s_\beta = \tilde s_\alpha\cdot\tilde g_{\alpha\beta}\quad\text{(definition of }\tilde g_{\alpha\beta}\text{)},\qquad \tilde s_\alpha = s_\alpha\cdot h_\alpha,\qquad \tilde s_\beta = s_\beta\cdot h_\beta,$$
> and by the definition of $g_{\alpha\beta}$ (for the original system), $s_\beta = s_\alpha\cdot g_{\alpha\beta}$.
>
> **Compute $\tilde s_\beta$ two ways.** On one hand, using $\tilde s_\beta = \tilde s_\alpha\cdot\tilde g_{\alpha\beta}$ and then $\tilde s_\alpha = s_\alpha\cdot h_\alpha$,
> $$\tilde s_\beta = (s_\alpha\cdot h_\alpha)\cdot\tilde g_{\alpha\beta} = s_\alpha\cdot\big(h_\alpha\,\tilde g_{\alpha\beta}\big)\qquad\text{(substitution, then associativity of the right action).}$$
> On the other hand, using $\tilde s_\beta = s_\beta\cdot h_\beta$ and then $s_\beta = s_\alpha\cdot g_{\alpha\beta}$,
> $$\tilde s_\beta = (s_\alpha\cdot g_{\alpha\beta})\cdot h_\beta = s_\alpha\cdot\big(g_{\alpha\beta}\,h_\beta\big)\qquad\text{(substitution, then associativity of the right action).}$$
>
> **Cancel by freeness.** The two computations give $s_\alpha\cdot(h_\alpha\,\tilde g_{\alpha\beta}) = s_\alpha\cdot(g_{\alpha\beta}\,h_\beta)$. Cancelling the common left factor $s_\alpha(x)$ by the **freeness** of the action (the cancellation law established above),
> $$h_\alpha\,\tilde g_{\alpha\beta} = g_{\alpha\beta}\,h_\beta\qquad\text{(by freeness).}$$
> **Solve for $g_{\alpha\beta}$.** Right-multiplying by $h_\beta^{-1}$ gives $g_{\alpha\beta} = h_\alpha\,\tilde g_{\alpha\beta}\,h_\beta^{-1}$; left-multiplying the same identity by $h_\alpha^{-1}$ and right-multiplying by $h_\beta^{-1}$ gives the equivalent form $\tilde g_{\alpha\beta} = h_\alpha^{-1}\,g_{\alpha\beta}\,h_\beta$ (group axioms in $G$). Since $x\in U_{\alpha\beta}$ was arbitrary, the identities hold as equalities of $G$-valued functions on $U_{\alpha\beta}$. Therefore the two systems are cohomologous with cochain $\{h_\alpha\}$. $\blacksquare$

Bär records the intermediate identity in the equivalent shape $h_\beta = g_{\beta\alpha}\,h_\alpha\,\tilde g_{\alpha\beta}$; left-multiplying $h_\alpha\,\tilde g_{\alpha\beta} = g_{\alpha\beta}\,h_\beta$ by $g_{\beta\alpha} = g_{\alpha\beta}^{-1}$ (cocycle condition (2)) reproduces it, so the two presentations are the same relation.

## The reconstruction data

The three preceding results say what a bundle's sections *produce*. The converse construction — starting from prescribed $G$-valued functions and building a bundle — is the content of the next theorem, [[Thm - Principal Bundles are Classified by Cocycles|Principal Bundles are Classified by Cocycles]]. We record here only the **data** and the **gluing relation**, and prove the one structural fact needed to make sense of the quotient; that the quotient is in fact a principal bundle is proved on the theorem page and is not claimed here.

**Definition (reconstruction data).** Let $B$ be a smooth manifold, $\{U_\alpha\}_{\alpha\in A}$ an open cover, and $\{g_{\alpha\beta}\colon U_{\alpha\beta}\to G\}$ a family of smooth maps satisfying the cocycle conditions (1)–(3). On the disjoint union $\bigsqcup_{\alpha\in A}(U_\alpha\times G)$ define a relation $\sim$ by declaring, for $(x,g)\in U_\alpha\times G$ and $(x',g')\in U_\beta\times G$,
$$(x,g)\sim(x',g')\quad:\Longleftrightarrow\quad x = x'\ \text{and}\ g = g_{\alpha\beta}(x)\,g'.$$
The **reconstruction space** is the quotient set
$$P := \Big(\bigsqcup_{\alpha\in A} U_\alpha\times G\Big)\Big/\!\sim,\qquad \pi\big([x,g]\big) := x,$$
and the class of $(x,g)\in U_\alpha\times G$ is written $[x,g]_\alpha$ (the subscript records which chart the representative comes from, since the relation depends on it).

The gluing rule is not arbitrary. It is forced by insisting that, in the bundle we are trying to rebuild, the point represented by $(x,g)$ in the $\alpha$-chart is $s_\alpha(x)\cdot g$ and the point represented by $(x',g')$ in the $\beta$-chart is $s_\beta(x')\cdot g'$, and that these agree. Using $s_\beta = s_\alpha g_{\alpha\beta}$, equivalently $s_\alpha = s_\beta g_{\beta\alpha}$, the demand $s_\alpha(x)\cdot g = s_\beta(x)\cdot g'$ becomes $s_\beta(x)\,g_{\beta\alpha}(x)\,g = s_\beta(x)\,g'$, and cancelling $s_\beta(x)$ by freeness gives $g' = g_{\beta\alpha}(x)\,g$, that is $g = g_{\alpha\beta}(x)\,g'$ — exactly clause (ii) of the relation. This is Bär's motivating computation on page 48 of Wernli's notes.

> [!note]- Proof that $\sim$ is an equivalence relation (each clause uses one cocycle condition)
> This is the one fact we must establish before a quotient can even be formed; that $P$ is a smooth manifold and a principal bundle is proved separately on [[Thm - Principal Bundles are Classified by Cocycles|the reconstruction theorem page]]. We verify reflexivity, symmetry, and transitivity clause by clause, in the manner of a well-definedness check, and note which cocycle condition each one consumes.
>
> **Reflexivity (uses condition (1), $g_{\alpha\alpha}=e$).** For $(x,g)\in U_\alpha\times G$, the relation $(x,g)\sim(x,g)$ within the same chart $\alpha$ requires $g = g_{\alpha\alpha}(x)\,g$. Since $g_{\alpha\alpha}(x) = e$ (condition (1)), the right-hand side is $e\cdot g = g$ (identity axiom in $G$), so the requirement holds and $(x,g)\sim(x,g)$.
>
> **Symmetry (uses condition (2), $g_{\alpha\beta}=g_{\beta\alpha}^{-1}$).** Suppose $(x,g)\in U_\alpha\times G$ and $(x,g')\in U_\beta\times G$ satisfy $(x,g)\sim(x,g')$, that is $g = g_{\alpha\beta}(x)\,g'$. Left-multiplying by $g_{\alpha\beta}(x)^{-1}$ gives $g' = g_{\alpha\beta}(x)^{-1}\,g = g_{\beta\alpha}(x)\,g$ (using condition (2), $g_{\alpha\beta}^{-1} = g_{\beta\alpha}$). This last equation is precisely the statement $(x,g')\sim(x,g)$ read from the $\beta$-chart to the $\alpha$-chart. Hence $\sim$ is symmetric.
>
> **Transitivity (uses condition (3) in the form $(*)$, $g_{\alpha\gamma}=g_{\alpha\beta}g_{\beta\gamma}$).** Suppose $(x,g)\in U_\alpha\times G$, $(x,g')\in U_\beta\times G$, $(x,g'')\in U_\gamma\times G$ with $(x,g)\sim(x,g')$ and $(x,g')\sim(x,g'')$; the base points already agree at the common value $x\in U_{\alpha\beta\gamma}$. The two relations read $g = g_{\alpha\beta}(x)\,g'$ and $g' = g_{\beta\gamma}(x)\,g''$. Substituting the second into the first,
> $$g = g_{\alpha\beta}(x)\,\big(g_{\beta\gamma}(x)\,g''\big) = \big(g_{\alpha\beta}(x)\,g_{\beta\gamma}(x)\big)\,g'' = g_{\alpha\gamma}(x)\,g''\qquad\text{(associativity in }G\text{, then }(*)\text{).}$$
> This is exactly $(x,g)\sim(x,g'')$ from the $\alpha$-chart to the $\gamma$-chart. Hence $\sim$ is transitive.
>
> All three clauses hold, so $\sim$ is an equivalence relation and the quotient set $P$ is well-defined. The cocycle conditions are used one apiece, which is why all three are needed: drop any one and the corresponding clause fails, so no quotient exists. $\blacksquare$

---

# Categorical / Structural Definition

A principal bundle presented by transition functions is, in the exact technical sense, a **nonabelian Čech $1$-cocycle** on $M$ with coefficients in the sheaf $\underline{G}$ of smooth $G$-valued functions. To an open cover $\mathcal{U} = \{U_\alpha\}$ one attaches the pointed set $Z^1(\mathcal{U};\underline{G})$ of families $\{g_{\alpha\beta}\colon U_{\alpha\beta}\to G\}$ satisfying the cocycle conditions $g_{\alpha\alpha} = e$, $g_{\beta\alpha} = g_{\alpha\beta}^{-1}$, and $g_{\alpha\gamma} = g_{\alpha\beta}\,g_{\beta\gamma}$ on triple overlaps. The coboundary relation defines an equivalence on this set: two cocycles are equivalent when they differ by a $0$-cochain $\{h_\alpha\colon U_\alpha\to G\}$ through $g_{\alpha\beta} = h_\alpha\,\tilde g_{\alpha\beta}\,h_\beta^{-1}$. The quotient is the first Čech cohomology "set" (it is only a pointed set, not a group, when $G$ is nonabelian),
$$\check{H}^1(\mathcal{U};\underline{G}) := Z^1(\mathcal{U};\underline{G})\big/\sim,$$
and passing to the direct limit over refinements of the cover gives $\check{H}^1(M;\underline{G})$. The content of the next theorem, [[Thm - Principal Bundles are Classified by Cocycles|Principal Bundles are Classified by Cocycles]], is that isomorphism classes of principal $G$-bundles over $M$ are in bijection with $\check{H}^1(M;\underline{G})$: a bundle produces a cocycle (this page), a cocycle produces a bundle (that page), and cohomologous cocycles produce isomorphic bundles (that page). The distinguished basepoint — the class of the constant cocycle $g_{\alpha\beta}\equiv e$ — corresponds to the trivial bundle $M\times G$.

The same structure sits one level down for [[Def - Vector Bundle|vector bundles]], where $G = GL(k,\mathbb{R})$ and the classifying set is $\check{H}^1(M;\underline{GL(k,\mathbb{R})})$, and one level down again for smooth manifolds themselves, whose chart transition maps are a cocycle valued in the pseudogroup of local diffeomorphisms. The single organising idea is: **a locally trivial object is nothing more than a rule for gluing standard pieces, the rule is a $1$-cocycle, and the object up to isomorphism is the cohomology class of the rule.** The reconstruction data $\bigsqcup_\alpha U_\alpha\times G/\!\sim$ is the concrete functor from cocycles back to bundles that makes the bijection an equivalence rather than a mere counting statement.

---

# Relate to Other Fields / Compression

**Gauge theory (physics).** In the physicist's dictionary a local section $s_\alpha$ is a **choice of gauge** over the region $U_\alpha$, and the transition function $g_{\alpha\beta}$ is the **gauge transformation** relating two overlapping gauges. The coboundary relation $g_{\alpha\beta} = h_\alpha\tilde g_{\alpha\beta}h_\beta^{-1}$ is the statement that physical content is unchanged by a local change of gauge $h_\alpha$; only the cohomology class of the cocycle — the bundle itself — is gauge-invariant. When the structure group is abelian, for instance $G = U(1)$ in electromagnetism, the conjugation $h_\alpha\tilde g_{\alpha\beta}h_\beta^{-1}$ collapses to $\tilde g_{\alpha\beta}\,h_\alpha h_\beta^{-1}$ and $\check{H}^1(M;\underline{U(1)})$ becomes an honest abelian group, the group of isomorphism classes of principal $U(1)$-bundles (equivalently Hermitian line bundles), later identified with a first Chern class.

**True name.** Stripped of formalism, a transition function is **a smoothly varying group element that translates one local trivialisation of the bundle into another** — the principal-bundle version of a change-of-basis matrix. On the [[Def - Transition Function of a Vector Bundle|vector-bundle page]] the "true name" was "a smoothly varying change-of-basis matrix between two local frames"; here the frame is replaced by a torsor origin and the matrix by a group element, but the operational meaning is identical. The definition is already operational: to compute $g_{\alpha\beta}(x)$ one need only solve the single equation $s_\beta(x) = s_\alpha(x)\cdot g_{\alpha\beta}(x)$ in the group.

**Compression.** The four notions of this page compress to one slogan and its qualifier: *the bundle is its cocycle, up to coboundary.* The transition functions are a complete invariant (the reconstruction theorem recovers the bundle from them), a minimal one (nothing smaller than the cohomology class survives a change of sections), and a computable one (each $g_{\alpha\beta}$ is a concrete $G$-valued function one can write down, as the Hopf and frame-bundle examples show).

---

# Examples / Corollaries

**Is an instance — the trivial bundle with its global section has all transition functions equal to $e$.** Let $P = M\times G$ with $\pi(x,g) = x$ and right action $(x,g)\cdot g_0 = (x, g g_0)$; this is the trivial principal $G$-bundle. Take the cover to be the single set $U = M$ (or any cover) and the section $s(x) = (x,e)$; on any two charts use the same section $s_\alpha = s_\beta = s$. Then the defining equation $s_\beta(x) = s_\alpha(x)\cdot g_{\alpha\beta}(x)$ reads $(x,e) = (x,e)\cdot g_{\alpha\beta}(x) = (x, g_{\alpha\beta}(x))$, whose second coordinate forces $g_{\alpha\beta}(x) = e$ for all $x$ (equality in $G$). So every transition function is the constant $e$, the cocycle conditions hold trivially, and the cohomology class is the basepoint of $\check{H}^1(M;\underline{G})$. Conversely, a bundle whose transition functions can all be made $e$ by a suitable choice of sections is trivial: the sections $s_\alpha$ then satisfy $s_\beta = s_\alpha$ on overlaps, hence patch to a single global section, and a principal bundle with a global section is trivial by the [[Thm - Sections of a Principal Bundle and Triviality|section–triviality theorem]]. Every clause checks: the action is free and transitive on fibres $\{x\}\times G$, the section is smooth, and the computed $g_{\alpha\beta}\equiv e$ satisfies (1)–(3).

**Is an instance — the frame bundle of $TM$ in two coordinate charts has the Jacobians as transition functions.** Let $E = TM$ with $\dim M = n$, and let $P = \operatorname{Fr}(E)$ be its [[Def - Frame Bundle of a Vector Bundle|frame bundle]], a principal $GL(n,\mathbb{R})$-bundle whose fibre over $x$ is the set of ordered bases (equivalently, of linear isomorphisms $\mathbb{R}^n\to T_xM$) with right action $e\cdot h = e\circ h$. Given two coordinate charts $(U_\alpha, x^i)$ and $(U_\beta,\tilde x^j)$, the coordinate frames $s_\alpha := (\partial/\partial x^1,\dots,\partial/\partial x^n)$ and $s_\beta := (\partial/\partial\tilde x^1,\dots,\partial/\partial\tilde x^n)$ are local sections of $\operatorname{Fr}(TM)$. The chain rule expresses one coordinate frame in terms of the other:
$$\frac{\partial}{\partial\tilde x^j} = \sum_{i=1}^n \frac{\partial x^i}{\partial\tilde x^j}\,\frac{\partial}{\partial x^i},$$
so, writing frames as rows and letting a matrix act on the right, $s_\beta = s_\alpha\cdot J$ with $J(x) = \big(\partial x^i/\partial\tilde x^j\big)_{i,j}$ the Jacobian matrix of the coordinate change. Comparing with $s_\beta = s_\alpha\cdot g_{\alpha\beta}$ and cancelling by freeness of the $GL(n,\mathbb{R})$-action gives
$$g_{\alpha\beta}(x) = \Big(\frac{\partial x^i}{\partial\tilde x^j}(x)\Big)_{i,j}\in GL(n,\mathbb{R}),$$
the Jacobian of $\varphi_\alpha\circ\varphi_\beta^{-1}$. Every clause checks: $J(x)$ is invertible because the coordinate change is a diffeomorphism (its Jacobian is nonsingular), it varies smoothly with $x$, and — as the reader may confirm on a triple chart overlap — the chain rule $\partial x^i/\partial\hat x^\ell = \sum_j (\partial x^i/\partial\tilde x^j)(\partial\tilde x^j/\partial\hat x^\ell)$ is exactly the cocycle condition $(*)$ for these Jacobians.

**Corollary — for a frame bundle the principal transition functions coincide with the vector-bundle transition functions.** Let $E\to M$ be a rank-$k$ [[Def - Vector Bundle|vector bundle]] with [[Def - Frame Bundle of a Vector Bundle|frame bundle]] $\operatorname{Fr}(E)$, and let $\Phi_\alpha,\Phi_\beta$ be two [[Def - Local Trivialization|local trivialisations]] of $E$ with vector-bundle [[Def - Transition Function of a Vector Bundle|transition function]] $\tau_{\alpha\beta}\colon U_{\alpha\beta}\to GL(k,\mathbb{R})$ defined by $(\Phi_\alpha\circ\Phi_\beta^{-1})(p,v) = (p,\tau_{\alpha\beta}(p)\,v)$. Then, for the sections of $\operatorname{Fr}(E)$ induced by these trivialisations, the principal transition function equals the vector-bundle transition function: $g_{\alpha\beta} = \tau_{\alpha\beta}$.

> [!note]- Proof of the coincidence
> **Set up the induced frames.** Each trivialisation $\Phi_\alpha\colon E|_{U_\alpha}\to U_\alpha\times\mathbb{R}^k$ induces a local frame, that is a local section $e_\alpha$ of $\operatorname{Fr}(E)$, by
> $$e_\alpha(x) := \Phi_\alpha^{-1}(x,\cdot)\colon \mathbb{R}^k\to E_x,\qquad v\mapsto \Phi_\alpha^{-1}(x,v),$$
> a linear isomorphism, hence a point of the fibre $\operatorname{Fr}(E)_x$; likewise $e_\beta(x) = \Phi_\beta^{-1}(x,\cdot)$. Take $s_\alpha := e_\alpha$ and $s_\beta := e_\beta$ as the sections of the principal bundle $\operatorname{Fr}(E)$.
>
> **Compute the composite $e_\alpha(x)^{-1}\circ e_\beta(x)$.** For $v\in\mathbb{R}^k$,
> $$e_\alpha(x)^{-1}\big(e_\beta(x)\,v\big) = e_\alpha(x)^{-1}\big(\Phi_\beta^{-1}(x,v)\big) = \operatorname{pr}_2\,\Phi_\alpha\big(\Phi_\beta^{-1}(x,v)\big)\qquad\text{(}e_\alpha(x)^{-1}\text{ is the }\mathbb{R}^k\text{-component of }\Phi_\alpha\text{),}$$
> where $\operatorname{pr}_2\colon U_\alpha\times\mathbb{R}^k\to\mathbb{R}^k$ is the projection. By the definition of $\tau_{\alpha\beta}$, $\Phi_\alpha(\Phi_\beta^{-1}(x,v)) = (x,\tau_{\alpha\beta}(x)\,v)$, so the right-hand side is $\tau_{\alpha\beta}(x)\,v$ (definition of $\tau_{\alpha\beta}$). As this holds for all $v$,
> $$e_\alpha(x)^{-1}\circ e_\beta(x) = \tau_{\alpha\beta}(x).$$
> **Rewrite as a right action.** Composing on the left with $e_\alpha(x)$ gives $e_\beta(x) = e_\alpha(x)\circ\tau_{\alpha\beta}(x) = e_\alpha(x)\cdot\tau_{\alpha\beta}(x)$, because the right $GL(k,\mathbb{R})$-action on $\operatorname{Fr}(E)$ is precomposition, $e\cdot h = e\circ h$ (definition of the frame-bundle action).
>
> **Cancel by freeness.** Comparing $e_\beta(x) = e_\alpha(x)\cdot\tau_{\alpha\beta}(x)$ with the defining equation $e_\beta(x) = e_\alpha(x)\cdot g_{\alpha\beta}(x)$ of the principal transition function, and cancelling $e_\alpha(x)$ by the **freeness** of the $GL(k,\mathbb{R})$-action, we obtain $g_{\alpha\beta}(x) = \tau_{\alpha\beta}(x)$ for every $x\in U_{\alpha\beta}$. Therefore the two notions of transition function agree for the frame bundle. $\blacksquare$

This corollary is the precise sense in which the principal-bundle theory extends, rather than replaces, the vector-bundle theory of [[Def - Transition Function of a Vector Bundle|Differential Geometry VI]]: passing from $E$ to $\operatorname{Fr}(E)$ forgets the fibre $\mathbb{R}^k$ but keeps the cocycle, and the cocycle is literally the same family of $GL(k,\mathbb{R})$-valued functions.

**Is an instance (forward reference) — the Hopf bundle has transition function $z/|z|$.** For the [[Def - The Hopf Bundle|Hopf bundle]] $S^3\to S^2$ with structure group $U(1)$, the two explicit sections over $U_1 = S^2\setminus\{(0,-1)\}$ and $U_2 = S^2\setminus\{(0,1)\}$ satisfy $s_1\cdot(z/|z|) = s_2$, so the transition function is $g_{12}(z,t) = z/|z|\in U(1)$ on the overlap $U_{12} = S^2\setminus\{(0,\pm1)\}$. The full computation is carried out on **[[Ex - Explicit Local Sections and the Transition Function of the Hopf Bundle]]**; it is the first genuinely non-constant cocycle in the series and the source of the Hopf bundle's nontriviality.

**Is NOT an instance — a smooth family violating the cocycle condition assembles no bundle.** Cover $M = S^1$ by three open arcs $U_1, U_2, U_3$ chosen so that all three meet in a small triple overlap $U_{123}\neq\emptyset$, and propose $G = U(1)$-valued functions $g_{12}\equiv 1$, $g_{23}\equiv 1$, $g_{13}\equiv -1$ (constant, hence smooth, and each valued in $U(1)$). Each individual function is a perfectly good smooth $U(1)$-valued map, so this passes every test except the deepest one. On the triple overlap the multiplicative cocycle condition $(*)$ demands $g_{13} = g_{12}\,g_{23} = 1\cdot 1 = 1$, whereas we posited $g_{13} = -1$; since $1\neq -1$ in $U(1)$, condition (3) fails. By the equivalence-relation proof above, the corresponding relation $\sim$ on $\bigsqcup U_\alpha\times U(1)$ is not transitive — one finds points $[x,g]_1\sim[x,g']_2\sim[x,g'']_3$ with $[x,g]_1\not\sim[x,g'']_3$ — so there is no quotient bundle. This is the principal-bundle mirror of the non-example on the [[Def - Transition Function of a Vector Bundle|vector-bundle transition-function page]], and it shows concretely that the cocycle conditions are a real constraint, not a formality.

**Calibration check.** First, confirm that on any nonempty double overlap the two identities $g_{\alpha\alpha}=e$ and $g_{\alpha\beta}g_{\beta\alpha}=e$ hold for the trivial bundle example, and that $g_{12}g_{21} = (z/|z|)(\overline{z}/|z|) = |z|^2/|z|^2 = 1$ for the Hopf transition function, verifying condition (2) there. Second, for the frame bundle of $TM$, check that the passage from the tangent bundle to the cotangent bundle sends the cocycle $\{J_{\alpha\beta}\}$ of Jacobians to the cocycle $\{(J_{\alpha\beta}^{-1})^{\mathsf T}\}$ of inverse-transpose Jacobians, matching the covector transformation law recorded on the vector-bundle page. Third, verify from the equivalence-relation proof that dropping condition (1) breaks reflexivity, dropping (2) breaks symmetry, and dropping (3) breaks transitivity — so the three cocycle conditions are used exactly once each and none is redundant.

---

# Unlocked by This

> [!tip] Reconstruction of a Bundle from a Cocycle *(from this chapter)*
> The reconstruction data $\bigsqcup_\alpha U_\alpha\times G/\!\sim$ defined above is assembled into an honest principal $G$-bundle, and the correspondence "bundle $\leftrightarrow$ cocycle up to coboundary" is proved to be a bijection, on **[[Thm - Principal Bundles are Classified by Cocycles]]**. That theorem is the reason transition functions matter: they are a complete and computable invariant of the bundle.

> [!tip] The Hopf Bundle and its Nontriviality *(from this chapter)*
> With transition functions in hand, the [[Def - The Hopf Bundle|Hopf bundle]] can be described by the single non-constant cocycle $g_{12} = z/|z|$, and its nontriviality is read off from the winding number of that map, on **[[Thm - The Hopf Bundle is Nontrivial]]** and **[[Ex - The Hopf Bundle is Nontrivial via the Winding Number of its Transition Function]]**.

> [!tip] Associated Bundles and their Cocycles *(from this chapter)*
> Applying a representation $\rho\colon G\to GL(V)$ to a cocycle $\{g_{\alpha\beta}\}$ produces the cocycle $\{\rho\circ g_{\alpha\beta}\}$ of the associated vector bundle, and applying a homomorphism $\varphi\colon G\to H$ produces the cocycle $\{\varphi\circ g_{\alpha\beta}\}$ of the extension. This functoriality of the cocycle is developed on **[[Def - Associated Bundle]]** and the classification theorem.
