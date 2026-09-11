---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Principal Bundles are Classified by Cocycles"
  - "Def - Transition Functions and the Cocycle Condition"
  - "Def - Frame Bundle of a Vector Bundle"
  - "Thm - Sections of a Principal Bundle and Triviality"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

The orthogonal group in one dimension is the discrete two-element group
$$O(1)=\{A\in GL_1(\mathbb{R}):A^{\mathsf T}A=1\}=\{+1,-1\}\cong\mathbb{Z}/2,$$
whose only smooth structure is the discrete one (a smooth map into $O(1)$ is the same thing as a locally constant map). Cover the circle $S^1=\mathbb{R}/2\pi\mathbb{Z}$ by the two arcs
$$U_1=S^1\setminus\{[\pi]\},\qquad U_2=S^1\setminus\{[0]\},\qquad U_{12}=U_1\cap U_2=V_+\sqcup V_-,$$
with $V_+=\{[\phi]:0<\phi<\pi\}$ and $V_-=\{[\phi]:\pi<\phi<2\pi\}$. Define the $O(1)$-cocycle
$$g_{12}\colon U_{12}\to O(1),\qquad g_{12}\big|_{V_+}\equiv +1,\qquad g_{12}\big|_{V_-}\equiv -1.$$

Prove:

1. **(Reconstruction)** $g_{12}$ is a genuine cocycle, and the principal $O(1)$-bundle $P$ it reconstructs is the orthonormal frame bundle $O(L)$ of the **Möbius line bundle** $L\to S^1$; concretely, $P$ is the connected double cover of $S^1$.
2. **(Non-triviality)** $g_{12}$ is **not** a coboundary: there are no smooth (equivalently, locally constant) maps $h_1\colon U_1\to O(1)$, $h_2\colon U_2\to O(1)$ with $g_{12}=h_1\,h_2^{-1}$ on $U_{12}$. Consequently $O(L)$ is a non-trivial principal $O(1)$-bundle, and $L$ is a non-trivial (non-orientable) line bundle.

This is the drill counterpart of the $U(1)$-over-$S^1$ computation in **[[Ex - Cohomologous Cocycles Give Isomorphic Bundles and Conversely]]**: the same two-arc cover, but a *disconnected* structure group, where the trivialising logarithm no longer exists.

**Recall:**

The tool is the reconstruction of a principal bundle from a cocycle and the equivalence "cohomologous $\iff$ isomorphic".

![[Thm - Principal Bundles are Classified by Cocycles#Statement]]

On a cover $\{U_\alpha\}$ with transition functions $g_{\alpha\beta}\colon U_{\alpha\beta}\to G$ satisfying the cocycle conditions $g_{\alpha\alpha}=e$, $g_{\alpha\beta}=g_{\beta\alpha}^{-1}$, $g_{\alpha\beta}g_{\beta\gamma}g_{\gamma\alpha}=e$, the **reconstructed bundle** is
$$P=\Big(\bigsqcup_\alpha U_\alpha\times G\Big)\Big/\sim,\qquad (x,g)_\alpha\sim(x,g')_\beta\iff x=x'\ \text{and}\ g=g_{\alpha\beta}(x)\,g',$$
with right action $[x,g]_\alpha\cdot k=[x,gk]_\alpha$ and canonical local sections $s_\alpha(x)=[x,e]_\alpha$ whose transition functions are the $g_{\alpha\beta}$ (part a). Every principal $G$-bundle with these transition functions is isomorphic to $P$ (part b), and two cocycles on the same cover reconstruct isomorphic bundles if and only if they are **cohomologous**, $g_{\alpha\beta}=h_\alpha\tilde g_{\alpha\beta}h_\beta^{-1}$ for smooth $h_\alpha\colon U_\alpha\to G$ (part c).

![[Def - Frame Bundle of a Vector Bundle#The Definition]]

For a Euclidean line bundle $L\to S^1$ the **orthonormal frame bundle** $O(L)$ has fibre $O(1)=\{\pm1\}$: over a point $x$ its fibre is the two unit vectors $\{\pm u\}$ of $L_x$, and the right $O(1)$-action is $u\cdot(\pm1)=\pm u$. A local orthonormal frame is a unit section $e_\alpha\colon U_\alpha\to L$, equivalently a local section $s_\alpha=e_\alpha$ of $O(L)$; the transition functions of $O(L)$ are the $\pm1$-valued functions relating $e_\alpha$ and $e_\beta$.

![[Thm - Sections of a Principal Bundle and Triviality#Statement]]

A principal $G$-bundle is trivial (isomorphic to $M\times G$) if and only if it admits a global smooth section. The product bundle $S^1\times O(1)$ is two disjoint copies of $S^1$ and has the global section $x\mapsto(x,+1)$.

The **Möbius line bundle** and its $\pm1$ transition functions are constructed in **[[Ex - The Möbius Bundle is Nontrivial]]**; its realisation as a mapping torus is **[[Ex - The Möbius Strip as a Mapping Torus is a Nontrivial Bundle]]**.

---

# Convergent Strategy

**Problem class.** This is a *construct-and-obstruct* problem: first identify a concretely defined bundle (the Möbius frame bundle) with the abstract reconstruction of a given cocycle, then prove a cohomological obstruction (the cocycle is not a coboundary) that certifies non-triviality. Both halves run through the classification theorem — part (b) for the identification, part (c) for the obstruction.

**Assumption pattern.** The decisive hypothesis is that the structure group $O(1)=\{\pm1\}$ is *discrete*. This enters twice. In the reconstruction it makes the total space a covering space: the gluing is a $\{\pm1\}$-permutation of two sheets, straight over $V_+$ and swapped over $V_-$, producing the connected double cover. In the obstruction it forces any smooth $h_\alpha\colon U_\alpha\to\{\pm1\}$ on the *connected* arc $U_\alpha$ to be *constant*, so a coboundary $h_1h_2^{-1}$ is a single constant on all of $U_{12}$ — which cannot match a $g_{12}$ that takes both values.

**Theorem routing.** For the reconstruction: verify the cocycle conditions (trivial on a two-set cover); write the gluing explicitly on the two components; match it, sheet by sheet, with the frame bundle $O(L)$ of the Möbius bundle by comparing transition functions and invoking part (b) of **[[Thm - Principal Bundles are Classified by Cocycles|the classification theorem]]**. For the obstruction: suppose a coboundary exists; use "continuous into discrete $\Rightarrow$ constant on connected sets" to reduce $h_1,h_2$ to constants; derive that $h_1h_2^{-1}$ is a single element of $\{\pm1\}$; contradict the fact that $g_{12}$ is $+1$ on $V_+$ and $-1$ on $V_-$. Then part (c) upgrades "not a coboundary" to "not isomorphic to the trivial bundle".

**Key decision point.** The only subtlety is recognising that *smoothness into a discrete group is local constancy*, and that the two arcs $U_1,U_2$ are each connected while the overlap $U_{12}$ is not. The obstruction lives exactly in this mismatch: the coboundary maps are pinned to be constant on each connected arc, but the cocycle they must reproduce distinguishes the two components of the overlap. This is the disconnected-group analogue of the failed logarithm in the $U(1)$ exercise, and naming that parallel is the fastest way to reconstruct the argument.

---

# Legal Operations Used

The topic page for §3.3 is not yet assembled; the operations are named descriptively and will be reconciled with its Legal Operations list.

1. **Verify the cocycle conditions on a two-set cover.** Check $g_{\alpha\alpha}=e$ and $g_{21}=g_{12}^{-1}$ (the triple condition being vacuous), so that $g_{12}$ defines a bundle at all.

2. **Reconstruct a bundle from a cocycle.** Form $(U_1\times O(1))\sqcup(U_2\times O(1))/\sim$ and describe the two sheets and how they are glued over each component of the overlap.

3. **Identify a reconstructed bundle with a concrete bundle by comparing transition functions.** Read off the transition function of the concrete orthonormal frame bundle $O(L)$ and match it with $g_{12}$, then invoke uniqueness up to isomorphism (part b).

4. **Reduce a smooth map into a discrete group to a constant on a connected set.** Use that the preimage of a point under a continuous map into a discrete space is open and closed to conclude $h_\alpha$ is constant on the connected arc $U_\alpha$.

5. **Obstruct a coboundary by a value mismatch.** Show that a constant coboundary $h_1h_2^{-1}$ cannot equal a transition function that takes two different values on the two components of the overlap.

6. **Upgrade a cohomological obstruction to non-triviality.** Apply part (c) of the classification theorem: not cohomologous to the trivial cocycle means not isomorphic to the product bundle.

---

# Hints

> [!note]- Hint 1
> First check that $g_{12}$ is a legitimate cocycle. On a two-set cover, which cocycle conditions are non-vacuous, and does a $\{\pm1\}$-valued $g_{12}$ automatically satisfy $g_{21}=g_{12}^{-1}$?

> [!note]- Hint 2
> Write out the reconstructed total space. Over $V_+$ the gluing $(x,a)_1\sim(x,b)_2$ with $a=g_{12}(x)b=(+1)b$ identifies the sheets straight; over $V_-$ it identifies them with $a=(-1)b$, a swap. Draw the two sheets over $S^1$: what covering space of $S^1$ do you get — two disjoint circles, or one circle wrapping twice?

> [!note]- Hint 3
> To identify $P$ with $O(L)$, recall that the Möbius bundle has unit sections $e_1,e_2$ over the two arcs that agree on one component of the overlap and differ by a sign on the other. Those unit sections are sections of $O(L)$; what is their transition function, and how does part (b) of the classification theorem finish the identification?

> [!note]- Hint 4
> For non-triviality, suppose $g_{12}=h_1h_2^{-1}$. Each $h_\alpha$ is smooth into the *discrete* group $\{\pm1\}$ and $U_\alpha$ is *connected* — so $h_\alpha$ is a constant $\varepsilon_\alpha\in\{\pm1\}$. Then $h_1h_2^{-1}\equiv\varepsilon_1\varepsilon_2$ is one fixed sign on all of $U_{12}$. Compare with $g_{12}$, which is $+1$ on $V_+$ and $-1$ on $V_-$.

---

# Solution

The reconstruction turns the $\pm1$ pattern into a permutation of two sheets — straight over one overlap component, swapped over the other — which is the connected double cover, i.e. the Möbius frame bundle. Non-triviality is then a counting statement about signs: a coboundary is forced to be a single constant sign, so it cannot reproduce a transition function that changes sign between the two components of the overlap.

**Step 1: $g_{12}$ is a cocycle.**

The map $g_{12}$ satisfies the cocycle conditions, so it reconstructs a principal $O(1)$-bundle.

> [!note]- Derivation
> On the two-set cover the conditions from **[[Def - Transition Functions and the Cocycle Condition|the cocycle identities]]** reduce to $g_{11}=g_{22}=e=+1$ (imposed by convention on each set alone) and $g_{21}=g_{12}^{-1}$; the triple-overlap identity $g_{\alpha\beta}g_{\beta\gamma}g_{\gamma\alpha}=e$ is vacuous, there being only two sets. Now $g_{12}$ takes values in $O(1)=\{\pm1\}$, and every element of $O(1)$ is its own inverse: $(+1)^{-1}=+1$, $(-1)^{-1}=-1$. Hence setting $g_{21}:=g_{12}$ gives $g_{21}=g_{12}^{-1}$ automatically. The map $g_{12}$ is smooth because it is locally constant (constant on each of the two components $V_\pm$ of its domain, which are disjoint open arcs). Therefore $g_{12}$ is a smooth cocycle and, by part (a) of **[[Thm - Principal Bundles are Classified by Cocycles|the classification theorem]]**, reconstructs a principal $O(1)$-bundle $P\to S^1$.

**Step 2: the reconstructed bundle is the connected double cover of $S^1$.**

Writing out the gluing shows $P$ is a single circle double-covering $S^1$, not two disjoint circles.

> [!note]- Derivation
> The total space is $P=\big((U_1\times\{\pm1\})\sqcup(U_2\times\{\pm1\})\big)/\sim$ with, by the reconstruction rule, $(x,a)_1\sim(x,b)_2\iff x\in U_{12}$ and $a=g_{12}(x)\,b$. Split by component of the overlap:
> $$\text{on }V_+:\ g_{12}=+1,\quad (x,+1)_1\sim(x,+1)_2,\ (x,-1)_1\sim(x,-1)_2\qquad\text{(sheets glued straight);}$$
> $$\text{on }V_-:\ g_{12}=-1,\quad (x,+1)_1\sim(x,-1)_2,\ (x,-1)_1\sim(x,+1)_2\qquad\text{(sheets swapped).}$$
> Consider the two "sheets" $S_1=\{[x,+1]_\alpha\}$ traced from $U_1\times\{+1\}$. Starting on the $+1$ sheet over $U_1$ and continuing through $V_+$ into $U_2$, we stay on the $U_2\times\{+1\}$ piece (straight gluing); continuing through $V_-$ back into $U_1$, the swap sends $U_2\times\{+1\}$ to $U_1\times\{-1\}$. Thus going once around the base carries the label $+1$ to $-1$: the two sheets are joined into a single connected component that projects to $S^1$ as a two-to-one covering. Concretely, $P\cong S^1$ with the projection $[\psi]\mapsto[2\psi]$ (the double cover), and the deck transformation is the right action of $-1\in O(1)$. This is the connected double cover of $S^1$; it is *not* the trivial bundle $S^1\times O(1)$, which is two disjoint circles.

**Step 3: $P$ is the orthonormal frame bundle of the Möbius line bundle.**

The Möbius line bundle $L$ has orthonormal frames over the two arcs with exactly the transition function $g_{12}$, so $O(L)\cong P$.

> [!note]- Derivation
> The Möbius line bundle $L\to S^1$ (constructed in **[[Ex - The Möbius Bundle is Nontrivial]]**) is a rank-one real bundle, trivial over each arc $U_\alpha$, with unit sections $e_1\colon U_1\to L$ and $e_2\colon U_2\to L$ that agree on one component of the overlap and differ by a sign on the other; with the arcs chosen as above the identification is $e_2=e_1$ on $V_+$ and $e_2=-e_1$ on $V_-$. Equip $L$ with a Euclidean metric so that $e_1,e_2$ are unit sections; they are then local sections $s_\alpha:=e_\alpha$ of the orthonormal frame bundle $O(L)$, whose fibre is $O(1)=\{\pm1\}$ (the two unit vectors in each fibre), as recalled above.
>
> The transition function of $O(L)$ with respect to $s_1,s_2$ is the unique $O(1)$-valued map with $s_2=s_1\cdot(\text{it})$: since $e_2=e_1$ on $V_+$ and $e_2=-e_1$ on $V_-$, it is $+1$ on $V_+$ and $-1$ on $V_-$ — exactly $g_{12}$. By part (b) of **[[Thm - Principal Bundles are Classified by Cocycles|the classification theorem]]** (every principal bundle with transition functions $\{g_{\alpha\beta}\}$ is isomorphic to the bundle reconstructed from them), $O(L)\cong P$. This matches Step 2: $O(L)$, the connected double cover, is the "orientation double cover" of the Möbius bundle.

**Step 4: $g_{12}$ is not a coboundary.**

No smooth $h_1,h_2$ trivialise $g_{12}$, because on the connected arcs $U_\alpha$ they must be constant.

> [!note]- Derivation
> The trivial $O(1)$-cocycle is $\tilde g_{12}\equiv +1$; a coboundary from it to $g_{12}$ is a pair of smooth maps $h_1\colon U_1\to O(1)$, $h_2\colon U_2\to O(1)$ with
> $$g_{12}=h_1\,\tilde g_{12}\,h_2^{-1}=h_1\,h_2^{-1}\qquad\text{on }U_{12}$$
> (using $\tilde g_{12}\equiv+1$; $O(1)$ is abelian, so the order is immaterial). Suppose such $h_1,h_2$ exist. A smooth map into the discrete group $O(1)=\{\pm1\}$ is continuous into a two-point space, so for each value $c\in\{\pm1\}$ the preimage $h_\alpha^{-1}(c)$ is both open (preimage of the open point $\{c\}$) and closed (preimage of the open complement $\{-c\}$) in $U_\alpha$. The arc $U_\alpha$ is connected, so one of these preimages is all of $U_\alpha$ and the other empty: $h_\alpha$ is a **constant** $\varepsilon_\alpha\in\{\pm1\}$.
>
> Then on all of $U_{12}$,
> $$h_1(x)\,h_2(x)^{-1}=\varepsilon_1\,\varepsilon_2^{-1}=\varepsilon_1\varepsilon_2\in\{\pm1\}\qquad\text{(a single fixed sign, since }\varepsilon_2^{-1}=\varepsilon_2\text{).}$$
> But $g_{12}$ is not constant on $U_{12}$: it equals $+1$ on $V_+$ and $-1$ on $V_-$. A single sign $\varepsilon_1\varepsilon_2$ cannot equal both $+1$ and $-1$, so the equation $g_{12}=h_1h_2^{-1}$ fails on at least one component. This contradicts the assumed existence of $h_1,h_2$. Hence $g_{12}$ is **not** a coboundary.

**Step 5: non-triviality of the bundle.**

By part (c) of the classification theorem, $P$ is not isomorphic to the trivial bundle; equivalently $L$ is non-orientable.

> [!note]- Derivation
> The trivial principal $O(1)$-bundle $S^1\times O(1)$ is the bundle reconstructed from the trivial cocycle $\tilde g_{12}\equiv+1$ (its canonical sections glue with $\tilde g_{12}\equiv e$, patch to a global section, and by **[[Thm - Sections of a Principal Bundle and Triviality|triviality via a global section]]** the bundle is the product). By part (c) of **[[Thm - Principal Bundles are Classified by Cocycles|the classification theorem]]**, $P\cong S^1\times O(1)$ would force $g_{12}$ and $\tilde g_{12}$ to be cohomologous — i.e. $g_{12}$ to be a coboundary. Step 4 rules this out. Therefore $P=O(L)$ is a non-trivial principal $O(1)$-bundle.
>
> Non-triviality of $O(L)$ means $O(L)$ has no global section, i.e. $L$ has no global unit section, i.e. $L$ is not orientable and hence not isomorphic to the trivial line bundle $S^1\times\mathbb{R}$ — the conclusion of **[[Ex - The Möbius Bundle is Nontrivial]]**, recovered here purely from the cocycle.

> [!note]- Complete formal solution
> **Claim.** The $O(1)$-cocycle $g_{12}$ on the two-arc cover of $S^1$, equal to $+1$ on $V_+$ and $-1$ on $V_-$, reconstructs the orthonormal frame bundle $O(L)$ of the Möbius line bundle, and is not a coboundary; hence $O(L)$ is non-trivial.
>
> *Cocycle.* On a two-set cover only $g_{\alpha\alpha}=e$ and $g_{21}=g_{12}^{-1}$ are non-vacuous; since every element of $O(1)=\{\pm1\}$ is self-inverse, $g_{21}:=g_{12}$ works, and $g_{12}$ is smooth (locally constant). So $g_{12}$ reconstructs a principal $O(1)$-bundle $P$.
>
> *Reconstruction.* $P=(U_1\times\{\pm1\})\sqcup(U_2\times\{\pm1\})/\sim$ with $(x,a)_1\sim(x,b)_2\iff a=g_{12}(x)b$: sheets glued straight over $V_+$ ($g_{12}=+1$) and swapped over $V_-$ ($g_{12}=-1$). Tracing a sheet once around the base sends label $+1$ to $-1$, so $P$ is connected and double-covers $S^1$.
>
> *Identification.* The Möbius bundle $L$ has unit sections $e_1,e_2$ over $U_1,U_2$ with $e_2=e_1$ on $V_+$ and $e_2=-e_1$ on $V_-$; as sections of $O(L)$ their transition function is $+1$ on $V_+$, $-1$ on $V_-$, i.e. $g_{12}$. By part (b) of the classification theorem $O(L)\cong P$.
>
> *No coboundary.* If $g_{12}=h_1h_2^{-1}$ with $h_\alpha\colon U_\alpha\to\{\pm1\}$ smooth, then each $h_\alpha$ is continuous into a discrete group on the connected arc $U_\alpha$, hence constant $\varepsilon_\alpha$; so $h_1h_2^{-1}\equiv\varepsilon_1\varepsilon_2$ is a single sign on $U_{12}$, contradicting $g_{12}=+1$ on $V_+$ and $-1$ on $V_-$. Thus $g_{12}$ is not a coboundary.
>
> *Non-triviality.* The trivial bundle $S^1\times O(1)$ comes from $\tilde g_{12}\equiv+1$; by part (c), $P\cong S^1\times O(1)$ iff $g_{12}$ is cohomologous to $\tilde g_{12}$, i.e. a coboundary — impossible. Hence $O(L)$ is non-trivial and $L$ is non-orientable. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to argue that $g_{12}$ is "obviously non-trivial because it takes the value $-1$". But value $-1$ alone means nothing: a coboundary $h_1h_2^{-1}$ can be $\equiv-1$ (take $h_1\equiv-1$, $h_2\equiv+1$), which is cohomologous to $+1$ and still reconstructs the *trivial* bundle. What matters is not the values but whether the two-component *pattern* $(+1,-1)$ can be produced by a constant, and the extra condition that makes non-triviality legitimate is precisely that $g_{12}$ takes **different** values on the two components — a single constant coboundary cannot straddle both. Over a connected structure group (the $U(1)$ case) even this pattern is a coboundary; disconnectedness of $O(1)$ is what makes the pattern an obstruction.

---

# Key Takeaways

**A discrete structure group turns a principal bundle over $S^1$ into a covering space, and the cocycle into a permutation-of-sheets recipe.** When $G$ is discrete the fibre is a finite set, the local trivialisations are sheets, and the transition function tells you how the sheets are permuted over each overlap component. For $O(1)=\{\pm1\}$ over the two-arc cover, "straight over $V_+$, swapped over $V_-$" is exactly the connected double cover; had the swap occurred over both components (or neither) the sheets would have closed up into two disjoint circles, the trivial bundle. The reusable principle is that principal $G$-bundles over $S^1$ with $G$ discrete are classified by the *net permutation accumulated once around the base*, an element of $G$ up to conjugacy — here the non-identity element $-1$, which is why the bundle is non-trivial. This is the bundle-theoretic face of the fact that connected coverings of $S^1$ are classified by the subgroups of $\mathbb{Z}=\pi_1(S^1)$.

**"Smooth into a discrete group" means "locally constant", and this is the entire obstruction.** The non-triviality proof uses no geometry beyond a single topological fact: a continuous map from a connected space into a discrete space is constant, because each fibre is open and closed. On the two-arc cover the coboundary maps $h_1,h_2$ live on the *connected* arcs, so they are constants, whereas the cocycle they would have to reproduce distinguishes the two *disconnected* components of the overlap. The mismatch between "connected domains for $h_\alpha$" and "disconnected domain for $g_{12}$" is the whole content. The transferable diagnostic: whenever the structure group is disconnected, look at the values of the transition function on the different components of the overlap modulo the constants available on each patch; what survives is the invariant. This is the direct analogue — and the failure mode — of the smooth-logarithm trivialisation available for the connected group $U(1)$ in **[[Ex - Cohomologous Cocycles Give Isomorphic Bundles and Conversely]]**.

**The pair of exercises isolates the single hypothesis that governs bundles over $S^1$: connectedness of $G$, i.e. $\pi_0(G)$.** Read side by side, the two computations use identical machinery — two arcs, one transition function, the coboundary test — and differ only in whether $G$ is connected. For $U(1)$ the transition function always has a logarithm and can be absorbed, so every bundle is trivial; for $O(1)$ the locally-constant constraint blocks absorption and the sign pattern is a genuine invariant. In general the isomorphism classes of principal $G$-bundles over $S^1$ are the conjugacy classes of $\pi_0(G)$: one class when $G$ is connected, and for $G=O(1)$ the two classes $\{+1\}$ and $\{-1\}$, the trivial bundle and the Möbius frame bundle. Carrying this one sentence — *bundles over the circle see only the components of the structure group* — lets you reconstruct both exercises and predict the answer for any $G$ before computing.
