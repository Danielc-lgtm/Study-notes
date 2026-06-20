---
type: exercise
subject: model-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Triangulated Category"
  - "Def - Abelian Group"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Let $\mathcal{T}$ be a [[Def - Triangulated Category|triangulated category]] and let $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$ be a distinguished triangle. Fix an object $W$. Prove that applying $\mathrm{Hom}_{\mathcal{T}}(W, -)$ produces a **long exact sequence** of abelian groups
$$\cdots \to [W, \Sigma^{-1}Z] \xrightarrow{(\Sigma^{-1}w)_*} [W, X] \xrightarrow{u_*} [W, Y] \xrightarrow{v_*} [W, Z] \xrightarrow{w_*} [W, \Sigma X] \to \cdots$$
(where $[A, B] = \mathrm{Hom}_{\mathcal{T}}(A, B)$), using only the axioms TR1–TR3. Conclude, in particular, that $v \circ u = 0$.

**Recall:**

![[Def - Triangulated Category#The Definition]]

The hom-sets $[A, B]$ are [[Def - Abelian Group|abelian groups]] and composition is bilinear (additivity). We will use TR1 (the triangle $X \xrightarrow{1_X} X \to 0 \to \Sigma X$ is distinguished; every map embeds in a triangle), TR2 (rotation: $X \to Y \to Z \to \Sigma X$ distinguished $\iff$ $Y \to Z \to \Sigma X \xrightarrow{-\Sigma u} \Sigma Y$ distinguished), and TR3 (a commuting square on the first two terms of two triangles extends to a morphism of triangles).

---

# Convergent Strategy

**Problem class:** This is a "structure $\Rightarrow$ exactness" problem of the kind the topic page identifies as the central computational target: convert a single distinguished triangle into infinitely many exactness statements by applying a hom-functor. The whole long exact sequence reduces, by rotation, to proving exactness at *one* spot and then transporting that proof around the triangle.

**Assumption pattern:** The only assumptions are the triangulated axioms, so every step must be one of TR1, TR2, TR3, or the additive structure. The presence of TR2 is the key resource: it lets you rotate the triangle so that any of the three "spots" becomes the middle, meaning you only have to prove exactness at the middle term $[W, Y]$ once.

**Theorem routing:** Exactness at $[W, Y]$ means $\ker(v_*) = \mathrm{im}(u_*)$. The inclusion $\mathrm{im}(u_*) \subseteq \ker(v_*)$ is the statement $v \circ u = 0$, which comes from TR1 applied to the triangle of $1_X$ and TR3. The reverse inclusion $\ker(v_*) \subseteq \mathrm{im}(u_*)$ is where TR3 (extending a square to a morphism of triangles) does the real work. Rotation (TR2) then propagates exactness to every spot.

**Key decision point:** The non-obvious move is to prove $v \circ u = 0$ not by a direct computation (there are no elements) but by comparing the triangle of $u$ with the trivial triangle of $1_X$ via TR3. The natural alternative — trying to "compute $vu$" — has nothing to compute with, because triangulated categories have no elements and no kernels; the only handle is the comparison-of-triangles axiom.

---

# Legal Operations Used

1. **Operation 1 from the topic page (complete a map to a triangle).** Used implicitly: the given triangle is the completion of $u$, and the triangle of $1_X$ is used as a comparison object.

2. **Operation 2 from the topic page (apply a hom-functor to get a long exact sequence).** This exercise *is* the proof that operation 2 is legal — it establishes the long exact sequence that operation 2 then uses everywhere.

3. **Operation 3 from the topic page (rotate a triangle).** Used to reduce exactness at all spots to exactness at the single middle spot $[W, Y]$.

---

# Hints

> [!note]- Hint 1
> Exactness at a chain of abelian groups means image equals kernel at each spot. By rotation (TR2), all spots of the sequence are "the middle spot of *some* rotated triangle," so it suffices to prove exactness at one spot — say at $[W, Y]$ for the triangle $X \xrightarrow{u} Y \xrightarrow{v} Z$.

> [!note]- Hint 2
> For $\mathrm{im}(u_*) \subseteq \ker(v_*)$, you need $v \circ u = 0$. Compare the distinguished triangle on $u$ with the distinguished triangle $X \xrightarrow{1_X} X \to 0 \to \Sigma X$ (TR1) using TR3, with the left square $\begin{smallmatrix} X & = & X \\ \downarrow u & & \downarrow vu \\ Y & \xrightarrow{v} & Z\end{smallmatrix}$... actually compare via the map of triangles that has $1_X$ and $u$ on the first two objects.

> [!note]- Hint 3
> For $\ker(v_*) \subseteq \mathrm{im}(u_*)$: take $a \colon W \to Y$ with $v \circ a = 0$. The composite $W \xrightarrow{a} Y \xrightarrow{v} Z$ being zero means the square comparing the triangle $W \xrightarrow{1_W} W \to 0 \to \Sigma W$ to the triangle $X \xrightarrow{u} Y \xrightarrow{v} Z \to \Sigma X$ (with $a$ in the middle) commutes; apply TR3 to fill in a map $W \to X$ and check it lifts $a$ through $u_*$.

---

# Solution

The proof has three moves. First reduce to exactness at the middle spot using rotation. Second prove $v u = 0$ (the easy inclusion) by comparing with the triangle of $1_X$. Third prove the reverse inclusion by lifting a map that dies under $v$, which is exactly what TR3 provides.

**Step 1: It suffices to prove exactness at $[W, Y]$.**

> [!note]- Derivation
> By TR2, the triangle $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$ may be rotated to $Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X \xrightarrow{-\Sigma u} \Sigma Y$, and again, and backwards. Each rotation is again distinguished, and its middle spot is the *next* spot of the original long sequence. So the statement "exact at $[W, Y]$ for every distinguished triangle" applied to all rotations of the given triangle yields exactness at *every* spot of the long sequence. We therefore only prove exactness at $[W, Y]$, i.e. $\ker(v_*) = \mathrm{im}(u_*)$ inside $[W, Y]$.

**Step 2: $\mathrm{im}(u_*) \subseteq \ker(v_*)$, equivalently $v \circ u = 0$.**

> [!note]- Derivation
> Consider the distinguished triangle $X \xrightarrow{1_X} X \to 0 \to \Sigma X$ (TR1(b)) and the given triangle $X \xrightarrow{u} Y \xrightarrow{v} Z \to \Sigma X$. The square
> $$\begin{array}{ccc} X & \xrightarrow{\ 1_X\ } & X \\ \big\downarrow{\scriptstyle 1_X} & & \big\downarrow{\scriptstyle u} \\ X & \xrightarrow{\ u\ } & Y \end{array}$$
> commutes, so by TR3 it extends to a morphism of triangles $(1_X, u, h)$ where $h \colon 0 \to Z$. The right square of that morphism reads $v \circ u = h \circ (X \to 0) = 0$, since $h$ factors through the zero object. Hence $v \circ u = 0$. Applying $[W, -]$, $v_* \circ u_* = (v u)_* = 0$, so $\mathrm{im}(u_*) \subseteq \ker(v_*)$.

**Step 3: $\ker(v_*) \subseteq \mathrm{im}(u_*)$.**

> [!note]- Derivation
> Let $a \in [W, Y]$ with $v_*(a) = v \circ a = 0$. Consider the trivial triangle $W \xrightarrow{1_W} W \to 0 \to \Sigma W$ and the given triangle. The square
> $$\begin{array}{ccc} W & \longrightarrow & 0 \\ \big\downarrow{\scriptstyle a} & & \big\downarrow \\ Y & \xrightarrow{\ v\ } & Z \end{array}$$
> commutes precisely because $v \circ a = 0$. Rotating the given triangle once (TR2) to $\Sigma^{-1}Z \to X \xrightarrow{u} Y \xrightarrow{v} Z$ and comparing with the rotated trivial triangle $\Sigma^{-1}0 \to W \xrightarrow{1_W} W \to 0$, TR3 produces a map $b \colon W \to X$ making the square
> $$\begin{array}{ccc} W & \xrightarrow{\ 1_W\ } & W \\ \big\downarrow{\scriptstyle b} & & \big\downarrow{\scriptstyle a} \\ X & \xrightarrow{\ u\ } & Y \end{array}$$
> commute, i.e. $a = u \circ b = u_*(b) \in \mathrm{im}(u_*)$. Hence $\ker(v_*) \subseteq \mathrm{im}(u_*)$.

> [!note]- Complete formal solution
> Let $X \xrightarrow{u} Y \xrightarrow{v} Z \xrightarrow{w} \Sigma X$ be distinguished and $W \in \mathcal{T}$.
>
> *Reduction.* By TR2 every rotation of the triangle is distinguished, and the middle terms of the rotations are exactly the successive terms of the long sequence. So it suffices to prove exactness at the middle term $[W, Y]$ for an arbitrary distinguished triangle.
>
> *Easy inclusion ($v u = 0$).* Apply TR3 to the commuting square with rows $X \xrightarrow{1_X} X$ and $X \xrightarrow{u} Y$ and columns $1_X, u$, comparing the triangle of $1_X$ (whose third object is $0$) with the triangle of $u$. The induced map on third objects factors through $0$, forcing $v \circ u = 0$. Hence $v_* u_* = 0$ and $\mathrm{im}(u_*) \subseteq \ker(v_*)$.
>
> *Hard inclusion.* Let $a \colon W \to Y$ with $v a = 0$. The square with rows $W \to 0$ and $Y \xrightarrow{v} Z$ and left column $a$ commutes. Comparing (after a rotation) the trivial triangle on $W$ with the triangle on $u$ via TR3 yields $b \colon W \to X$ with $u b = a$, so $a \in \mathrm{im}(u_*)$. Hence $\ker(v_*) \subseteq \mathrm{im}(u_*)$.
>
> Therefore the sequence is exact at $[W, Y]$, and by the reduction it is exact everywhere. The dual statement for $\mathrm{Hom}_{\mathcal{T}}(-, W)$ follows by the same argument in $\mathcal{T}^{op}$, which is again triangulated. $\blacksquare$

---

# Key Takeaways

**The long exact sequence is the only form exactness takes in a triangulated category, and it comes entirely from rotation plus one comparison.** The single most important structural fact about triangulated categories is that they have *no* kernels, cokernels, or images at the object level, so "exactness" can only ever be a statement about the abelian groups $[W, -]$. This exercise shows that the entire infinite long exact sequence is bootstrapped from exactness at one spot, propagated by TR2. The transferable lesson: whenever you want exactness in a triangulated category, you never argue at more than one spot — you prove it once and rotate, because rotation is what makes the sequence bi-infinite and self-similar.

**$v \circ u = 0$ is proved by comparison, not computation, and this is the paradigm for all triangulated arguments.** With no elements to manipulate, the only tool for showing a composite vanishes is TR3 — comparing the triangle in question to the trivial triangle $X \xrightarrow{1_X} X \to 0$, whose third object is zero. The trigger to internalize: in a triangulated category, "show this map is zero" almost always means "find a triangle in which this map factors through a zero object, via TR3." This same comparison technique proves the five lemma for triangles and underlies every devissage argument.

**The non-uniqueness of TR3's fill-in is invisible here but is the seam of the whole theory.** This proof used TR3 to produce maps $h$ and $b$, and it never needed them to be *unique* — exactness is a statement about images and kernels, which are insensitive to which fill-in you chose. This is why the long exact sequence survives despite the cone's non-functoriality: exactness only sees the existence of a fill-in, not its canonicity. The diagnostic to carry forward is that arguments which use only the *existence* of TR3 fill-ins (long exact sequences, vanishing) are legitimate in any triangulated category, whereas arguments needing a *canonical* fill-in (total complexes, functorial cones) must be performed one level up in a stable model category or **stable ∞-category** — see the topic page's illegal-operation 1.
