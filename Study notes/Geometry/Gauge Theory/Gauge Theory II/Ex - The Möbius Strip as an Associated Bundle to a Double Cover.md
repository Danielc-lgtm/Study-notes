---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Associated Bundle"
  - "Def - Principal G-Bundle"
  - "Def - Fibre Bundle"
tags: [geometry, gauge-theory, associated-bundles]
---

# Problem Statement

Let $P = S^1$, with the principal $\mathbb{Z}/2$-bundle structure given by the connected double cover $\pi : S^1 \to S^1$, $z \mapsto z^2$ (in complex notation: $S^1 = \{e^{i\theta}\}$, $\pi(e^{i\theta}) = e^{2i\theta}$). Let $\mathbb{Z}/2 = \{\pm 1\}$ act on $\mathbb{R}$ by sign.

**Show:**

(a) The principal $\mathbb{Z}/2$-bundle $S^1 \to S^1$ is nontrivial (admits no global section).

(b) The associated bundle $S^1 \times_{\mathbb{Z}/2} \mathbb{R}$ is the **Möbius line bundle** — the unique nontrivial real line bundle over $S^1$.

(c) The associated bundle $S^1 \times_{\mathbb{Z}/2} \{*\}$ (where $\mathbb{Z}/2$ acts trivially on a single point) is the base $S^1$ itself.

**Recall:**

![[Def - Associated Bundle#The Definition]]

![[Def - Principal G-Bundle#The Definition]]

A **double cover** of $S^1$: the map $\pi : S^1 \to S^1$, $z \mapsto z^2$, is a 2-to-1 covering map. The two preimages of any point are $\{z, -z\}$, exchanged by the $\mathbb{Z}/2$-action $z \mapsto -z$.

---

# Convergent Strategy

**Problem class:** This is a *bundle-construction-via-associated-bundle* problem. The topic-page strategy "build any fibre bundle with structure group $G$ from a principal $G$-bundle plus a $G$-space" applies, in the discrete setting $G = \mathbb{Z}/2$. The problem also illustrates that *non-orientation* of the Möbius strip is exactly $\mathbb{Z}/2$-bundle nontriviality.

**Assumption pattern:** The key assumption is that the double cover $S^1 \to S^1$ is **nontrivial** (the upper sheet does not connect back to itself after one trip around the base — it connects to the lower sheet, then back to itself after a second trip). This is what makes the $\mathbb{Z}/2$-action exchange the sheets and the associated bundle nontrivial.

**Theorem routing:** [[Thm - Associated-Bundle Construction Yields a Bundle]] gives the smoothness and bundle structure of $P \times_G F$ automatically; the explicit identification with the Möbius bundle requires a coordinate computation.

**Key decision point:** The non-obvious step is recognizing the nontrivial double cover correctly. The trivial double cover $S^1 \sqcup S^1 \to S^1$ (disjoint union of two circles) is *not* what we want — that would give the trivial bundle $S^1 \times \mathbb{R}$. The *connected* double cover $S^1 \to S^1$, $z \mapsto z^2$, is the one whose associated bundle is the Möbius strip.

---

# Legal Operations Used

1. **Operation 6 from the topic page (Construct/disprove a global section to detect triviality).** Show no global section of the double cover exists: such a section would be a continuous choice of one of the two preimages at every point, but the topology of the double cover (the two sheets are connected) precludes this.

2. **Operation 1 from the topic page (Pass between principal and associated bundle).** Apply the associated-bundle construction $P \times_G F$ with the principal $\mathbb{Z}/2$-bundle and the $\mathbb{Z}/2$-action on $\mathbb{R}$ to construct the Möbius bundle.

3. **Operation 2 of the meta-strategy: Identify the fibre and verify the structure-group action.** $\mathbb{Z}/2$ acting on $\mathbb{R}$ by sign gives the rank-1 vector bundle structure; the transition function on the overlap of two trivializing patches is $-1$.

---

# Hints

> [!note]- Hint 1
> To show the double cover has no global section, parameterize: a global section would be a continuous map $s : S^1 \to S^1$ with $s(z)^2 = z$ for all $z$. Write $z = e^{i\phi}$; $s(z) = e^{i\phi/2}$ would work on $\phi \in [0, 2\pi)$, but it doesn't extend continuously to $\phi = 2\pi$ (giving $s = -1$ vs $s = +1$ at the start).

> [!note]- Hint 2
> For the associated bundle, write a point as $[(z, v)]$ with $z \in S^1, v \in \mathbb{R}$, modulo $(z, v) \sim (-z, -v)$. The map $S^1 \times_{\mathbb{Z}/2} \mathbb{R} \to S^1$, $[(z, v)] \mapsto z^2$, has fibre $\{[(z, v)] : z^2 = w_0\}$ which is $\mathbb{R}$ (one of the two sheets gives $v$, the other gives $-v$, identified).

> [!note]- Hint 3
> Triviality of $S^1 \times_{\mathbb{Z}/2} \mathbb{R}$ would require a global frame, equivalently a nowhere-vanishing global section. The Möbius bundle does *not* admit one (the natural "section" from going around the strip ends up on the opposite side), so the bundle is nontrivial.

---

# Solution

The proof has three steps. Step 1 establishes the nontriviality of the principal $\mathbb{Z}/2$-bundle $S^1 \to S^1$. Step 2 constructs the Möbius line bundle as the associated bundle and identifies it explicitly. Step 3 verifies the trivial-action case. The non-obvious move is recognizing that the connected double cover, viewed as a principal $\mathbb{Z}/2$-bundle, encodes precisely the data needed to build the Möbius strip.

**Step 1: The principal $\mathbb{Z}/2$-bundle $S^1 \to S^1$ is nontrivial.**

A global section $s : S^1 \to S^1$ of the double cover would be a continuous map $s(z)$ with $s(z)^2 = z$ for all $z \in S^1$.

> [!note]- Derivation
> Suppose such an $s$ exists. Write $z = e^{i\phi}$ for $\phi \in \mathbb{R}/2\pi\mathbb{Z}$. Then $s(e^{i\phi}) = e^{i\psi(\phi)}$ with $2\psi(\phi) \equiv \phi \pmod{2\pi}$, hence $\psi(\phi) = \phi/2 + n(\phi)\pi$ for some integer $n(\phi)$. Continuity forces $n(\phi)$ to be locally constant, hence globally constant (by connectedness of $S^1$). So $\psi(\phi) = \phi/2 + n\pi$ for fixed $n$.
>
> But this map does not extend continuously around $S^1$: $\psi(\phi + 2\pi) = \phi/2 + \pi + n\pi$, which equals $\psi(\phi) + \pi$ — differing by $\pi$, not $0$ — so $s$ at $\phi + 2\pi$ and at $\phi$ differ by a sign. Hence $s$ cannot be globally continuous.
>
> So the principal $\mathbb{Z}/2$-bundle $S^1 \to S^1$ has no global section, hence is nontrivial. ∎

**Step 2: The associated bundle is the Möbius strip.**

The associated bundle $S^1 \times_{\mathbb{Z}/2}\mathbb{R}$ has fibre $\mathbb{R}$ and is a rank-1 real vector bundle over $S^1$.

> [!note]- Derivation
> By [[Thm - Associated-Bundle Construction Yields a Bundle]], $E := S^1 \times_{\mathbb{Z}/2}\mathbb{R}$ is a smooth rank-1 real vector bundle over $S^1$ with structure group $\mathbb{Z}/2$ acting on $\mathbb{R}$ by sign.
>
> **Explicit identification with the Möbius strip.** Parametrize $S^1 = [0, 2\pi]/(0 \sim 2\pi)$ in the *base*, and use $\theta = \phi/2 \in [0, \pi]$ in the total space coordinates. A point in $E$ is $[(e^{i\phi/2}, v)]$ modulo $(e^{i\phi/2}, v) \sim (-e^{i\phi/2}, -v) = (e^{i(\phi/2 + \pi)}, -v)$.
>
> Use the cover $\phi \in [0, 2\pi]$ of the base: the total space over this cover is $\{(e^{i\phi/2}, v) : \phi \in [0, 2\pi], v \in \mathbb{R}\}$, with identification at $\phi = 0$ and $\phi = 2\pi$. At $\phi = 0$: $(1, v) \sim (-1, -v) = (e^{i\pi}, -v)$. At $\phi = 2\pi$: $(e^{i\pi}, v) \sim (e^{i\pi + i\pi}, -v) = (1, -v)$. So the gluing $\phi = 0 \leftrightarrow \phi = 2\pi$ identifies $(1, v) \leftrightarrow (1, -v)$ — i.e., the fibre at the start identifies the fibre at the end with the opposite orientation.
>
> This is exactly the Möbius strip construction: take the strip $[0, 2\pi] \times \mathbb{R}$ and glue the ends with a flip. The total space is the open Möbius strip; the projection to the circle $S^1$ is the bundle map; the rank-1 vector-space structure on each fibre is the standard $\mathbb{R}$.
>
> **Verification via transition function.** Cover the base $S^1$ by two arcs $U_+ = \{e^{i\phi} : -\epsilon < \phi < \pi + \epsilon\}$ and $U_- = \{e^{i\phi} : \pi - \epsilon < \phi < 2\pi + \epsilon\}$. The associated bundle is trivial on each (since $\mathbb{Z}/2$-bundles on contractible bases are trivial), with the transition function on the overlap (two arcs $\phi \approx 0$ and $\phi \approx \pi$) being $+1$ on one component and $-1$ on the other. The $-1$ flip is what makes the bundle nontrivial — it cannot be unwound to give a global trivialization. ∎

**Step 3: The trivial-action associated bundle is the base.**

> [!note]- Derivation
> The associated bundle $S^1 \times_{\mathbb{Z}/2}\{*\}$ has fibre $\{*\}$ (a single point), trivial action. So $S^1 \times_{\mathbb{Z}/2}\{*\} = S^1/\mathbb{Z}/2 \times \{*\} \cong S^1$, the base itself. The bundle is a fibre bundle with point-fibre, hence equal to the base. ✓

> [!note]- Complete formal solution
> **Part (a):** The connected double cover $z \mapsto z^2$ on $S^1$ has no global section, since any candidate section $s(e^{i\phi}) = e^{i\phi/2 + n\pi}$ for locally constant integer $n$ fails to extend continuously around the circle (a $\pi$-shift accumulates). Hence the principal $\mathbb{Z}/2$-bundle is nontrivial (Step 1).
>
> **Part (b):** By [[Thm - Associated-Bundle Construction Yields a Bundle]], $S^1 \times_{\mathbb{Z}/2}\mathbb{R}$ is a rank-1 real vector bundle over $S^1$. Explicit identification (Step 2) with the Möbius strip via the gluing $(1, v) \sim (1, -v)$ around the circle confirms the construction yields the Möbius line bundle. The bundle is nontrivial because the transition function across the natural overlap is $-1$, not $+1$, in one component.
>
> **Part (c):** Trivial action gives the trivial fibre bundle $S^1 \times \{*\} = S^1$ (Step 3). ∎

> [!warning] Illegal but tempting alternative route
> One might be tempted to use the *disconnected* double cover $S^1 \sqcup S^1 \to S^1$ (two disjoint copies of $S^1$, each projecting identically) as the principal $\mathbb{Z}/2$-bundle. This *is* a principal $\mathbb{Z}/2$-bundle, but it is **trivial** (admits the global section "pick the top sheet"), and its associated bundle $(S^1 \sqcup S^1) \times_{\mathbb{Z}/2}\mathbb{R}$ is the trivial line bundle $S^1 \times \mathbb{R}$, *not* the Möbius strip. The nontriviality of the Möbius bundle comes from the *connectedness* of the double cover, which prevents the existence of a global section that distinguishes "top" from "bottom" sheet. The repair: always specify *connected* double cover.

---

# Key Takeaways

**Associated-bundle construction via $\mathbb{Z}/2$ gives all $\mathbb{Z}/2$-bundles their geometric content.** In the discrete case $G = \mathbb{Z}/2$, the associated-bundle construction $P \times_{\mathbb{Z}/2} F$ for various $\mathbb{Z}/2$-spaces $F$ generates: the Möbius line bundle ($F = \mathbb{R}$), the trivial circle bundle (trivial action), the orientation double cover (the principal bundle itself for $F = \mathbb{Z}/2$), and various "twisted" tensor bundles. The pattern: choose $F$ with a meaningful $\mathbb{Z}/2$-action, get a nontrivial bundle. The Möbius strip is the prototype of all nontrivial $\mathbb{Z}/2$-twisted bundles; higher cases include the orientation double covers of non-orientable manifolds and the spin double cover of unspun bundles.

**The Möbius bundle exhibits the first Stiefel-Whitney class.** The Möbius line bundle over $S^1$ is the realization of the nonzero element of $H^1(S^1; \mathbb{Z}/2) = \mathbb{Z}/2$ via the first **Stiefel-Whitney class** $w_1$. The class $w_1 \in H^1(M; \mathbb{Z}/2)$ is the obstruction to orientability of a real vector bundle, and the trivial-vs-Möbius bundle on $S^1$ is the simplest example: $w_1 = 0$ for the trivial bundle, $w_1 \neq 0$ for the Möbius bundle. The trigger-reaction pattern: "is this real line bundle orientable?" → "compute $w_1$; nonzero $\Leftrightarrow$ non-orientable $\Leftrightarrow$ Möbius-like".

**Connected vs disconnected covers distinguish nontriviality.** The same group $\mathbb{Z}/2$ can act on $S^1$ in two qualitatively different ways: as deck transformations of the *connected* double cover $z \mapsto z^2$ (nontrivial principal bundle) or as the trivial action on $S^1 \sqcup S^1$ (trivial principal bundle). The distinction is exactly the existence of a global section. This is the prototype of the general principle: classifying principal bundles by their connected components, or more precisely by the discrete data of how the structure group permutes the components of the total space. For discrete structure groups, this is the entire content of the classification.

This exercise prefigures [[Algebraic Topology II — Fundamental Group and Covering Spaces|Algebraic Topology II]], where the relation between covering spaces and subgroups of $\pi_1$ is developed in full. The connected double cover of $S^1$ corresponds to the subgroup $2\mathbb{Z} \leq \mathbb{Z} = \pi_1(S^1)$.
