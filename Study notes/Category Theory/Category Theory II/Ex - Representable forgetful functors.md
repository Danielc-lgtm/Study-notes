---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Hom-Functor and Representable Functor"
  - "Def - Group"
  - "Def - Ring"
  - "Def - Topological Space"
tags: [category-theory, foundations]
---

# Problem Statement

Show that the following forgetful functors are representable, and identify the representing object and the universal element in each case.

1. $U : \mathbf{Grp} \to \mathbf{Set}$, represented by $\mathbb{Z}$.
2. $U : \mathbf{Ring} \to \mathbf{Set}$, represented by $\mathbb{Z}[x]$.
3. $U : \mathbf{Top} \to \mathbf{Set}$, represented by the one-point space $*$.

In each case exhibit the natural isomorphism $\mathcal{C}(A, -) \cong U$ explicitly and verify naturality.

**Recall:**

![[Def - Hom-Functor and Representable Functor#The Definition]]

A functor $F : \mathcal{C} \to \mathbf{Set}$ is [[Def - Hom-Functor and Representable Functor|representable]] by $A$ if there is a natural isomorphism $\eta : \mathcal{C}(A, -) \xrightarrow{\cong} F$; the [[Def - Universal Element|universal element]] is $u = \eta_A(1_A) \in F(A)$. The objects $\mathbb{Z}$ (see [[Def - Group]]) and $\mathbb{Z}[x]$ (see [[Def - Ring]]) are free on one generator in their categories.

---

# Convergent Strategy

**Problem class:** This is the standard "exhibit a representation" exercise: produce a natural bijection between a hom-functor and a given $\mathbf{Set}$-valued functor. The topic page's strategy is to find the *universal element* first — the generic element the representing object carries — and let the bijection be "evaluate a morphism at the universal element".

**Assumption pattern:** Each representing object is *free on one generator*: $\mathbb{Z}$ is the free group on one generator, $\mathbb{Z}[x]$ the free ring on one generator, $*$ the free space on one point. The defining assumption is therefore "a morphism out of $A$ is determined by, and free to choose, the image of the generator". That image is an element of the target's underlying set, which is exactly what makes the hom-set biject with the underlying set.

**Theorem routing:** The route is uniform: a morphism $A \to X$ is determined by where it sends the distinguished generator $u \in U(A)$; the assignment $\varphi \mapsto U(\varphi)(u)$ is the natural bijection $\mathcal{C}(A, X) \cong U(X)$. Naturality is checked against postcomposition. The universal element $u$ is the generator. This is the [[Def - Universal Element]] form of representability.

**Key decision point:** The non-obvious recognition is *which* element is the universal one. For $\mathbf{Grp}$ it is the generator $1 \in \mathbb{Z}$; for $\mathbf{Ring}$ it is the indeterminate $x \in \mathbb{Z}[x]$; for $\mathbf{Top}$ it is the single point. Choosing the universal element correctly makes the bijection write itself; choosing wrongly leaves you proving naturality by brute force.

---

# Legal Operations Used

1. **Operation 2 from the topic page (read off a morphism from generators).** In each case a morphism out of the free object is determined by the image of its single generator, which is the universal element.

2. **Operation 3 from the topic page (build the representation via the universal element).** We define the natural isomorphism as evaluation at the universal element, the [[Def - Universal Element]] recipe.

---

# Hints

> [!note]- Hint 1
> A homomorphism $\mathbb{Z} \to G$ is determined by the image of $1$. A ring map $\mathbb{Z}[x] \to R$ by the image of $x$. A continuous map $* \to X$ by the image of the point. In each case "image of the generator" is an element of the underlying set.

> [!note]- Hint 2
> Define $\eta_X : \mathcal{C}(A, X) \to U(X)$ by $\varphi \mapsto U(\varphi)(u)$, where $u$ is the generator. Show it is a bijection: surjective because any element is a legal image, injective because the morphism is determined by it.

> [!note]- Hint 3
> Naturality: for $f : X \to Y$, check $\eta_Y \circ \mathcal{C}(A, f) = U(f) \circ \eta_X$. Both send $\varphi$ to $U(f \circ \varphi)(u) = U(f)(U(\varphi)(u))$.

---

# Solution

The three cases are one argument: identify the single generator of the free representing object, declare the bijection to be "evaluate at the generator", and check that postcomposition makes it natural. The universal element is the generator each time.

**Step 1: $U : \mathbf{Grp} \to \mathbf{Set}$ represented by $\mathbb{Z}$.**

> [!note]- Derivation
> A homomorphism $\varphi : \mathbb{Z} \to G$ is determined by $\varphi(1) =: g$, since $\varphi(n) = g^n$, and any $g \in G$ arises (set $\varphi(n) = g^n$, a homomorphism). Define $\eta_G : \mathbf{Grp}(\mathbb{Z}, G) \to U(G)$, $\varphi \mapsto \varphi(1)$. It is a bijection by the previous sentence. The universal element is $1 \in U(\mathbb{Z})$ (it is $\eta_{\mathbb{Z}}(1_{\mathbb{Z}}) = 1_{\mathbb{Z}}(1) = 1$). So $\mathbf{Grp}(\mathbb{Z}, -) \cong U$, witnessing that $\mathbb{Z}$ is the [[Def - Free Group and Free Product|free group on one generator]].

**Step 2: $U : \mathbf{Ring} \to \mathbf{Set}$ represented by $\mathbb{Z}[x]$.**

> [!note]- Derivation
> A ring homomorphism $\varphi : \mathbb{Z}[x] \to R$ is determined by $\varphi(x) =: r$ (the image of $1$ is forced to $1_R$, and then $\varphi$ of any polynomial is computed from $r$), and any $r \in R$ arises. Define $\eta_R : \mathbf{Ring}(\mathbb{Z}[x], R) \to U(R)$, $\varphi \mapsto \varphi(x)$, a bijection. The universal element is the indeterminate $x \in U(\mathbb{Z}[x])$. So $\mathbf{Ring}(\mathbb{Z}[x], -) \cong U$, and $\mathbb{Z}[x]$ is the free ring on one generator (see [[Def - Ring]]).

**Step 3: $U : \mathbf{Top} \to \mathbf{Set}$ represented by the one-point space.**

> [!note]- Derivation
> A continuous map $\varphi : * \to X$ from the one-point space picks out a point $\varphi(\bullet) \in X$, and any point arises (a map from a one-point space is automatically continuous). Define $\eta_X : \mathbf{Top}(*, X) \to U(X)$, $\varphi \mapsto \varphi(\bullet)$, a bijection. The universal element is the unique point $\bullet \in U(*)$. So $\mathbf{Top}(*, -) \cong U$.

**Step 4: Naturality (uniform).**

> [!note]- Derivation
> In each case, for $f : X \to Y$ in $\mathcal{C}$ we must check $\eta_Y \circ \mathcal{C}(A, f) = U(f) \circ \eta_X$. The left side sends $\varphi : A \to X$ to $\eta_Y(f \circ \varphi) = U(f \circ \varphi)(u) = U(f)(U(\varphi)(u))$ (functoriality of $U$). The right side sends $\varphi$ to $U(f)(\eta_X(\varphi)) = U(f)(U(\varphi)(u))$. They agree, so $\eta$ is a natural isomorphism.

> [!note]- Complete formal solution
> In each category the representing object is free on one generator, so a morphism out of it is determined by — and free in — the image of that generator, an element of the target's underlying set. Define $\eta_X(\varphi) = U(\varphi)(u)$ with $u$ the generator ($1 \in \mathbb{Z}$, $x \in \mathbb{Z}[x]$, $\bullet \in *$). Each $\eta_X$ is a bijection (surjective: any element is a legal generator image; injective: the morphism is determined by it), so $\mathcal{C}(A, -) \cong U$, with universal element $u$. Naturality holds because both legs of the square send $\varphi$ to $U(f)(U(\varphi)(u))$ by functoriality of $U$. $\blacksquare$

---

# Key Takeaways

**"Free on one generator" is the same statement as "the underlying-set functor is represented by me".** The thread tying all three cases together is that a free object on one generator $A$ satisfies $\mathcal{C}(A, X) \cong U(X)$ naturally — and conversely, the representing object of a forgetful functor *is* the free object on one generator. This is the cleanest dictionary entry between [[Def - Universal Property and Universal Arrow|universal arrows]] (free constructions) and [[Def - Hom-Functor and Representable Functor|representability]]: a left adjoint to $U$ evaluated at the one-point set is the representing object. The trigger is "a morphism out of $A$ is determined by one piece of data living in the target", and the reaction is "$U$ is representable by $A$, with that piece of data as the universal element".

**The universal element is always the generic generator, and naming it correctly trivializes the proof.** Finding the representation is finding the universal element: $1 \in \mathbb{Z}$, $x \in \mathbb{Z}[x]$, the point of $*$. Once named, the natural isomorphism is forced to be "evaluate the morphism at the universal element", and naturality is the single computation $U(f)(U(\varphi)(u)) = U(f \circ \varphi)(u)$, which is just functoriality. The practical lesson, used constantly in algebraic geometry, is: *to prove representability, guess the universal element*, do not chase the natural isomorphism abstractly.

**Representable forgetful functors are the rule, not the exception, and this is why "underlying set" is so well-behaved.** That $U$ is representable means it preserves all limits (a representable functor is continuous), which is the abstract reason underlying-set functors preserve products, equalizers, and limits — the underlying set of a product of groups is the product of underlying sets, and so on. When you later meet a forgetful functor that does *not* preserve some limit or colimit, that is a signal it may fail to be representable, and the contrast with these clean examples is the diagnostic. Compare [[Ex - A non-representable functor]], where preservation fails.
