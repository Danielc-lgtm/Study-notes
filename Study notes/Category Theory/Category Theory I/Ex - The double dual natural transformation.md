---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Natural Transformation"
  - "Def - Dual Space"
  - "Def - Dual Map"
tags: [category-theory, foundations]
---

# Problem Statement

Let $k$ be a field. Show that the **double-dual** assignment defines a [[Def - Natural Transformation|natural transformation]]
$$\eta : 1_{\mathbf{Vect}_k} \Longrightarrow (-)^{**}, \qquad \eta_V : V \to V^{**}, \quad \eta_V(v) = \mathrm{ev}_v,$$
where $\mathrm{ev}_v(\varphi) = \varphi(v)$ for $\varphi \in V^* = \mathrm{Hom}_k(V, k)$. That is, verify the naturality square commutes for every [[Def - Linear Map|linear map]] $f : V \to W$. Show that on [[Def - Vector Space|finite-dimensional]] spaces each $\eta_V$ is an isomorphism, so $\eta$ is a natural isomorphism $1 \cong (-)^{**}$ there. Finally, explain why there is no analogous *natural* isomorphism $1 \cong (-)^*$ to the single dual.

**Recall:**

The [[Def - Dual Space|dual space]] is $V^* = \mathrm{Hom}_k(V, k)$; the double dual is $V^{**} = (V^*)^*$. For $f : V \to W$ the [[Def - Dual Map|dual map]] is $f^* : W^* \to V^*$, $\psi \mapsto \psi \circ f$. The double-dual functor $(-)^{**} = ((-)^*)^*$ is covariant; its action on $f$ is $f^{**} = (f^*)^* : V^{**} \to W^{**}$. ![[Def - Natural Transformation#The Definition]]

---

# Convergent Strategy

**Problem class:** This is a "verify naturality and decide invertibility" exercise — the defining example of the subject. The route is to compute both legs of the naturality square on an element and observe they agree, then count dimensions for invertibility.

**Assumption pattern:** The crucial structural fact is that $(-)^{**}$ is *covariant* (a composite of two contravariant duals), so a candidate natural transformation $1 \Rightarrow (-)^{**}$ between covariant functors can be drawn; the single dual $(-)^*$ is contravariant, so the variances clash and no square against $1$ can even be formed.

**Theorem routing:** Naturality is a direct element computation: both routes around the square send $v$ to "evaluate-at-$f(v)$". Invertibility on finite-dimensional spaces is $\dim V = \dim V^* = \dim V^{**}$ plus injectivity of $\eta_V$. The non-naturality of the single dual is a variance argument.

**Key decision point:** The decisive realization is the *variance mismatch* for the single dual: naturality is not merely "hard to verify" for $1 \Rightarrow (-)^*$ — it is impossible to even state, because $(-)^*$ reverses arrows while $1$ does not, so the square cannot be drawn. This is *why* "$V \cong V^*$ is unnatural" and "$V \cong V^{**}$ is natural" are categorically different statements.

---

# Legal Operations Used

1. **Operation: verify a naturality square by chasing an element around both legs** (topic page, Legal Operation 10). Compute $f^{**} \circ \eta_V$ and $\eta_W \circ f$ on a vector $v$.

2. **Operation: prove a natural transformation is a natural iso by checking components are isos** (topic page, Legal Operation 10). Dimension count plus injectivity.

3. **Operation: diagnose variance to rule out a natural transformation** (topic page, Legal Operation 8). The single dual is contravariant, blocking any $1 \Rightarrow (-)^*$.

---

# Hints

> [!note]- Hint 1
> The naturality square for $f : V \to W$ has corners $V, V^{**}, W, W^{**}$, with $\eta_V, \eta_W$ on top/bottom and $f, f^{**}$ on the sides. Chase $v \in V$ around both ways and compare the resulting elements of $W^{**}$ (which are functionals on $W^*$).

> [!note]- Hint 2
> $f^{**}(\eta_V(v))$ is a functional on $W^*$; evaluate it at $\psi \in W^*$ using $f^{**} = (f^*)^*$, i.e. $f^{**}(\Phi) = \Phi \circ f^*$. And $\eta_W(f(v))$ evaluated at $\psi$ is $\psi(f(v))$. Show both equal $\psi(f(v))$.

> [!note]- Hint 3
> Finite-dimensional: $\dim V^{**} = \dim V$, and $\eta_V$ is injective (if $v \neq 0$, some functional $\varphi$ has $\varphi(v) \neq 0$, so $\eta_V(v) \neq 0$). Injective between equal finite dimensions ⟹ iso.

> [!note]- Hint 4
> Single dual: $(-)^*$ sends $f : V \to W$ to $f^* : W^* \to V^*$ — backwards. A natural transformation $1 \Rightarrow (-)^*$ would need a square with $1$ (covariant) and $(-)^*$ (contravariant). Can such a square even be drawn?

---

# Solution

The plan: chase $v$ around the naturality square and show both legs land on the functional "evaluate at $f(v)$"; conclude naturality. Then use $\dim V = \dim V^{**}$ and injectivity to get a natural iso in finite dimensions. Finally, argue the single dual's contravariance forbids a natural transformation from the identity.

**Step 1: Naturality of $\eta$.**

> [!note]- Derivation
> Fix a [[Def - Linear Map|linear map]] $f : V \to W$. The naturality square asserts $f^{**} \circ \eta_V = \eta_W \circ f$ as maps $V \to W^{**}$. Both sides send $v \in V$ to a functional on $W^*$; evaluate each at an arbitrary $\psi \in W^*$.
>
> Right-then-down ($\eta_W \circ f$): $\eta_W(f(v))$ is the evaluation functional $\mathrm{ev}_{f(v)}$, so $\big(\eta_W(f(v))\big)(\psi) = \psi(f(v))$.
>
> Down-then-right ($f^{**} \circ \eta_V$): by definition $f^{**} = (f^*)^*$, so $f^{**}(\Phi) = \Phi \circ f^*$ for $\Phi \in V^{**}$. With $\Phi = \eta_V(v) = \mathrm{ev}_v$,
> $$\big(f^{**}(\eta_V(v))\big)(\psi) = \big(\mathrm{ev}_v \circ f^*\big)(\psi) = \mathrm{ev}_v(f^*\psi) = \mathrm{ev}_v(\psi \circ f) = (\psi \circ f)(v) = \psi(f(v)).$$
> Both equal $\psi(f(v))$ for all $\psi$, so the functionals agree, and the square commutes — for *every* $f$, with *no choice of basis*. Hence $\eta : 1_{\mathbf{Vect}_k} \Rightarrow (-)^{**}$ is a [[Def - Natural Transformation|natural transformation]].

**Step 2: $\eta_V$ is an isomorphism in finite dimensions.**

> [!note]- Derivation
> For finite-dimensional $V$, $\dim V^* = \dim V$, hence $\dim V^{**} = \dim V$. The component $\eta_V$ is injective: if $v \neq 0$, extend $v$ to a basis and let $\varphi$ be the dual functional with $\varphi(v) = 1$; then $\eta_V(v)(\varphi) = \varphi(v) = 1 \neq 0$, so $\eta_V(v) \neq 0$. An injective linear map between spaces of equal finite dimension is an isomorphism. Therefore each $\eta_V$ is an iso, and $\eta$ is a [[Def - Natural Transformation|natural isomorphism]] $1 \cong (-)^{**}$ on $\mathbf{FinVect}_k$.

**Step 3: No natural isomorphism $1 \cong (-)^*$.**

> [!note]- Derivation
> The single-dual functor $(-)^* : \mathbf{Vect}_k^{\mathrm{op}} \to \mathbf{Vect}_k$ is **contravariant** (it sends $f : V \to W$ to $f^* : W^* \to V^*$, reversing direction). A [[Def - Natural Transformation|natural transformation]] $\alpha : 1_{\mathbf{Vect}_k} \Rightarrow (-)^*$ would require, for each $f : V \to W$, a commuting square with $\alpha_V : V \to V^*$, $\alpha_W : W \to W^*$, the covariant leg $f : V \to W$, and the dual leg $f^* : W^* \to V^*$. But these arrows do not assemble into a square: the would-be naturality condition $f^* \circ \alpha_W = \alpha_V \circ f$ has $f^* \circ \alpha_W : W \to V^*$ on one side and $\alpha_V \circ f : V \to V^*$ on the other — different domains. The square cannot be drawn, so no natural transformation $1 \Rightarrow (-)^*$ exists. (Even componentwise, choosing isomorphisms $V \cong V^*$ requires a basis, and no basis-free, morphism-compatible choice exists.) **This variance mismatch is exactly why $V \cong V^*$ is "unnatural" while $V \cong V^{**}$ is "natural".**

> [!note]- Complete formal solution
> *Naturality:* for $f : V \to W$, $\psi \in W^*$, $v \in V$: $(f^{**}\eta_V(v))(\psi) = (\mathrm{ev}_v \circ f^*)(\psi) = (\psi f)(v) = \psi(f(v)) = (\eta_W f(v))(\psi)$, so $f^{**}\eta_V = \eta_W f$.
>
> *Natural iso (finite dim):* $\dim V^{**} = \dim V$ and $\eta_V$ injective (a separating functional exists for each $v \neq 0$), so $\eta_V$ is an iso; $\eta$ is a natural iso on $\mathbf{FinVect}_k$.
>
> *No $1 \cong (-)^*$:* $(-)^*$ is contravariant, so the naturality square against the covariant $1$ has mismatched domains and cannot be formed. $\blacksquare$

---

# Key Takeaways

**"Natural" means the naturality square commutes — and this is the example that defines the word.** The double dual is the canonical witness that "natural" is a precise mathematical condition, not a feeling: the family $\eta_V$ is natural because pushing forward by $f$ commutes with evaluation, with no basis chosen anywhere. The reusable diagnostic is that a "canonical" or "basis-free" construction should always be checked by drawing its naturality square; if it commutes, the construction is genuinely natural, and if you needed a basis to define the components, suspect it does not. Eilenberg and Mac Lane invented categories precisely to make this distinction, and the double dual versus single dual is the example they had in mind.

**Variance must match before a natural transformation can even be contemplated.** The sharpest lesson is that the single dual fails to admit a natural transformation from the identity not because the squares fail to commute but because the squares *cannot be drawn*: the variances clash. Before checking naturality of any candidate family $\alpha_A : FA \to GA$, confirm $F$ and $G$ have the *same* variance — both covariant or both contravariant — or there is no naturality square to check. This is why double dual (covariant, a composite of two contravariant functors) works while single dual (contravariant) does not, and it is a fast first filter: mismatched variance rules out naturality immediately.

**Natural isomorphism on objects up to dimension, not on the nose.** Notice that $\eta$ is a natural *isomorphism* only on finite-dimensional spaces — in infinite dimensions $\eta_V$ is injective but not surjective ($V^{**}$ is genuinely larger). The transferable point: a natural transformation can be natural everywhere yet have invertible components only on a subcategory, and identifying that subcategory (here, finite dimension) is part of the content. When you build a natural transformation hoping for a natural isomorphism, check componentwise invertibility separately, because naturality of the family and invertibility of its components are independent conditions — naturality is structural, invertibility is pointwise.
