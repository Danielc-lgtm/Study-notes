---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Hom-Functor and Representable Functor"
  - "Def - Ring"
  - "Def - Universal Element"
tags: [category-theory, foundations]
---

# Problem Statement

Fix a base ring $k$ (for instance $k = \mathbb{Z}$ or a field) and let $\mathbf{CRing}_k$ be the category of commutative $k$-algebras. Consider the functors
$$\mathbb{A}^1 : R \mapsto R \quad (\text{the underlying set}), \qquad \mathbb{G}_m : R \mapsto R^\times \quad (\text{the set of units}), \qquad \mathbb{A}^n : R \mapsto R^n.$$

1. Show $\mathbb{A}^1$ (the **affine line**) is representable by $k[x]$, identify its universal element, and explain why this is the categorical meaning of "the affine line".
2. Show $\mathbb{A}^n$ (**affine $n$-space**) is representable by $k[x_1, \dots, x_n]$.
3. Show $\mathbb{G}_m$ (the **multiplicative group**) is representable by $k[x, x^{-1}]$.

**Recall:**

![[Def - Hom-Functor and Representable Functor#The Definition]]

A functor $F : \mathbf{CRing}_k \to \mathbf{Set}$ is [[Def - Hom-Functor and Representable Functor|representable]] by $A$ if $\mathbf{CRing}_k(A, -) \cong F$ naturally; the [[Def - Universal Element|universal element]] is the image of the identity. A $k$-algebra is a [[Def - Ring|commutative ring]] $R$ with a structure map $k \to R$, and $k$-algebra homomorphisms commute with it.

> [!note]- Algebraic geometry background (self-contained)
> No prior algebraic geometry is assumed. A **commutative ring** has commutative associative $+, \times$ with $0, 1$, inverses for $+$, and distributivity (see [[Def - Ring]]). The **functor-of-points** idea is to record the solutions of a system of polynomial equations *in every ring at once*: a fixed system defines a functor $\mathbf{CRing}_k \to \mathbf{Set}$, $R \mapsto \{\text{solutions with coordinates in } R\}$, called its functor of points; the value $F(R)$ is the set of **$R$-points**. An **affine scheme** is by definition a representable such functor, and the representing $k$-algebra is its ring of functions. The simplest is the **affine line** $\mathbb{A}^1$, the functor $R \mapsto R$ — "a point of the line valued in $R$ is just an element of $R$". The multiplicative group $\mathbb{G}_m$ is $R \mapsto R^\times$, the units. These notes show all three are representable, hence are affine schemes.

---

# Convergent Strategy

**Problem class:** This is a representability exercise in the algebraic-geometry setting: show a functor of points is a hom-functor, i.e. an affine scheme. The routine, as for all representability problems, is to guess the universal element (here, the coordinate function(s)) and check that morphisms out of the candidate ring biject with $R$-points.

**Assumption pattern:** The decisive assumption is that the representing algebras are *free commutative $k$-algebras*: $k[x]$ is free on one generator, $k[x_1, \dots, x_n]$ on $n$ generators, and $k[x, x^{-1}]$ is free on one *invertible* generator. A $k$-algebra map out of a polynomial ring is a free choice of where to send each generator; the Laurent ring additionally forces the generator's image to be a unit.

**Theorem routing:** The route is the [[Def - Universal Element]] recipe: a $k$-algebra map $k[x] \to R$ is determined by $\varphi(x) \in R$, giving $\mathbf{CRing}_k(k[x], R) \cong R = \mathbb{A}^1(R)$; the universal element is $x$. For $\mathbb{G}_m$ the constraint "$x$ invertible $\Rightarrow$ image invertible" cuts the bijection down to units. Naturality is postcomposition, as in [[Ex - Representable forgetful functors]].

**Key decision point:** The subtle case is $\mathbb{G}_m$: one must see that adjoining a formal inverse $x^{-1}$ to $x$ in $k[x, x^{-1}]$ is exactly what forces a $k$-algebra map to send $x$ to a *unit* — because $x \cdot x^{-1} = 1$ must be preserved — and that conversely every unit is a legal image. Recognizing that "invertibility of the generator" is the algebraic encoding of "the image must be a unit" is the heart of the exercise.

---

# Legal Operations Used

1. **Operation 2 from the topic page (read off a morphism from generators).** A $k$-algebra map out of a (Laurent) polynomial ring is determined by the images of the generators, which are the coordinates of an $R$-point.

2. **Operation 3 from the topic page (build the representation via the universal element).** We take the universal element to be the coordinate function(s) $x$ (or $x_1, \dots, x_n$), and define the natural bijection by evaluation.

---

# Hints

> [!note]- Hint 1
> A $k$-algebra homomorphism $k[x] \to R$ is determined by, and free in, the image of $x$. What set does that image range over?

> [!note]- Hint 2
> For $\mathbb{A}^n$, a map out of $k[x_1, \dots, x_n]$ is an independent choice of images for each $x_i$ — an element of $R^n$.

> [!note]- Hint 3
> For $\mathbb{G}_m$: in $k[x, x^{-1}]$ the generator $x$ has an inverse. A ring map must send invertible elements to invertible elements, so $\varphi(x)$ must be a unit. Conversely, can you map $x$ to any unit?

> [!note]- Hint 4
> The universal element of $\mathbb{A}^1 = \mathbf{CRing}_k(k[x], -)$ is the coordinate $x \in k[x]$: every "value" $r \in R$ is the image of $x$ under the unique map sending $x \mapsto r$.

---

# Solution

The three cases follow the representable-forgetful-functor template, with the representing object a free commutative $k$-algebra. The only new wrinkle is $\mathbb{G}_m$, where invertibility of the formal generator pins the image to the units.

**Step 1: $\mathbb{A}^1$ represented by $k[x]$.**

> [!note]- Derivation
> A $k$-algebra homomorphism $\varphi : k[x] \to R$ is determined by $\varphi(x) =: r \in R$ (the structure map fixes the images of $k$, and then $\varphi$ of any polynomial is computed from $r$); and any $r \in R$ arises, since $x \mapsto r$ extends uniquely to a $k$-algebra map. So
> $$\mathbf{CRing}_k(k[x], R) \xrightarrow{\ \cong\ } R = \mathbb{A}^1(R), \qquad \varphi \mapsto \varphi(x),$$
> naturally in $R$ (postcomposition, exactly as in [[Ex - Representable forgetful functors]]). The universal element is $x \in \mathbb{A}^1(k[x]) = k[x]$. Categorically, "the affine line" *means* the representable functor $R \mapsto R$, and its ring of functions is $k[x]$: the line is the universal carrier of one coordinate.

**Step 2: $\mathbb{A}^n$ represented by $k[x_1, \dots, x_n]$.**

> [!note]- Derivation
> A $k$-algebra map $\varphi : k[x_1, \dots, x_n] \to R$ is an independent free choice of $\varphi(x_i) = r_i \in R$ for each $i$, i.e. a tuple $(r_1, \dots, r_n) \in R^n$, and every tuple arises. So $\mathbf{CRing}_k(k[x_1, \dots, x_n], R) \cong R^n = \mathbb{A}^n(R)$, naturally. The universal element is the tuple of coordinates $(x_1, \dots, x_n)$.

**Step 3: $\mathbb{G}_m$ represented by $k[x, x^{-1}]$.**

> [!note]- Derivation
> The ring $k[x, x^{-1}]$ is $k[x]$ with a formal inverse adjoined, so $x$ is a *unit*: $x \cdot x^{-1} = 1$. A $k$-algebra map $\varphi : k[x, x^{-1}] \to R$ must preserve this relation: $\varphi(x)\varphi(x^{-1}) = \varphi(1) = 1$, so $\varphi(x)$ is a unit of $R$, with inverse $\varphi(x^{-1})$. Conversely, for any unit $u \in R^\times$, the assignment $x \mapsto u$, $x^{-1} \mapsto u^{-1}$ extends uniquely to a $k$-algebra map (the relation is respected). Hence
> $$\mathbf{CRing}_k(k[x, x^{-1}], R) \xrightarrow{\ \cong\ } R^\times = \mathbb{G}_m(R), \qquad \varphi \mapsto \varphi(x),$$
> naturally. The universal element is $x \in k[x, x^{-1}]^\times$. So $\mathbb{G}_m$ is an affine scheme, $\mathbb{G}_m = \mathrm{Spec}\, k[x, x^{-1}]$.

> [!note]- Complete formal solution
> Each representing algebra is free (as a commutative $k$-algebra) on its generators, so a $k$-algebra map out of it is determined by, and free in, the images of the generators. For $k[x]$ that image is an element of $R$, giving $\mathbf{CRing}_k(k[x], -) \cong (R \mapsto R) = \mathbb{A}^1$ with universal element $x$. For $k[x_1, \dots, x_n]$ it is a tuple in $R^n$, giving $\mathbb{A}^n$. For $k[x, x^{-1}]$ the relation $x x^{-1} = 1$ forces the image of $x$ to be a unit and allows any unit, giving $\mathbf{CRing}_k(k[x, x^{-1}], -) \cong (R \mapsto R^\times) = \mathbb{G}_m$ with universal element $x$. Naturality is postcomposition in each case. Hence all three functors of points are representable — they are affine schemes. $\blacksquare$

---

# Key Takeaways

**An affine scheme is literally a representable functor on rings, and the universal element is its coordinate system.** This exercise is the concrete face of the slogan "affine scheme = representable functor $\mathbf{CRing} \to \mathbf{Set}$". The affine line is not a mysterious geometric object; it is the functor $R \mapsto R$, and its representing ring $k[x]$ is its ring of polynomial functions, with the universal element $x$ being the generic coordinate. The trigger to recognize an affine scheme is "a functor of points $R \mapsto \{\text{solutions in } R\}$"; the reaction is to find the representing ring as $k[\text{coordinates}]/(\text{equations})$ and read off the universal element as the tuple of coordinates. This is the bridge to the entire functor-of-points development in [[Ex - A scheme is determined by its functor of points]].

**Adjoining an inverse to a generator is the algebraic spelling of "the image must be a unit".** The $\mathbb{G}_m$ case teaches a transferable principle: imposing a relation on the representing ring imposes the corresponding constraint on the $R$-points. The relation $x x^{-1} = 1$ in $k[x, x^{-1}]$ forces every map to land $x$ in the units, which is exactly how the units functor gets represented. More generally, $R \mapsto \{r : p(r) = 0\}$ is represented by $k[x]/(p(x))$ — quotienting by an equation cuts the affine line down to its solution locus. Recognizing this dictionary, "relation in the ring $\leftrightarrow$ equation on the points", is the core skill of categorical algebraic geometry.

**Representability gives the geometry its functorial backbone for free.** Because $\mathbb{A}^1, \mathbb{A}^n, \mathbb{G}_m$ are representable, they automatically preserve all limits, so products of these schemes correspond to coproducts (tensor products) of their rings: $\mathbb{A}^m \times \mathbb{A}^n = \mathbb{A}^{m+n}$ corresponds to $k[x_1,\dots,x_m] \otimes_k k[y_1,\dots,y_n] = k[x_1,\dots,x_m,y_1,\dots,y_n]$. This is the seed of the rule "fibre products of affine schemes are tensor products of rings", and it follows with no extra work from the representability established here, illustrating why phrasing geometry through representable functors is so powerful.
