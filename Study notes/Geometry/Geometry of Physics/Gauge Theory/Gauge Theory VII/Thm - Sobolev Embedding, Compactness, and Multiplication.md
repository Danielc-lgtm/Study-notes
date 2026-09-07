---
type: theorem
subject: gauge-theory
prereqs: ["Def - Sobolev Space of Bundle Sections"]
tags: [gauge-theory, sobolev-embedding, rellich, multiplication]
---

# Prerequisite Concepts

- [[Def - Sobolev Space of Bundle Sections]]

# Statement

> [!theorem] Sobolev package on a compact $n$-manifold
> The inclusion $W^{k,p}(E)\hookrightarrow W^{m,q}(E)$ is continuous when $k\ge m$ and $k-n/p\ge m-n/q$, and compact when both inequalities are strict. If $k-n/p>r$, then $W^{k,p}\hookrightarrow C^r$. If $kp>n$, $W^{k,p}(M)$ is a Banach algebra. More generally, multiplication is continuous into $W^{k,p}$ whenever the Sobolev orders satisfy the standard summed-order inequality and avoid the endpoint exceptions.

# Proof Architecture

> [!proof]- Formal Proof
> Choose finitely many coordinate charts trivializing $E$ and a subordinate partition of unity. Multiplication by each cutoff and coordinate pullback are bounded on every Sobolev space under consideration, so it suffices to prove the Euclidean compact-support statements.
>
> For the continuous embedding, write derivatives of order at most $m$ and apply the Euclidean Sobolev inequality iteratively to the derivatives of order $m$; scaling forces the index condition $k-n/p\ge m-n/q$. Summing over the finite atlas gives the global estimate.
>
> For compactness, boundedness in $W^{k,p}$ gives uniform translation control of all derivatives through order $m$ and tight support after applying chart cutoffs. The Fréchet–Kolmogorov criterion gives a convergent subsequence in $W^{m,q}$ when the index and derivative losses are strict. A diagonal subsequence over the finite atlas patches globally.
>
> If $k-n/p>r$, apply the embedding to every derivative through order $r$ with a Hölder target; the resulting representatives and derivatives are continuous. For multiplication, use Leibniz, place each factor in the Lebesgue space supplied by Sobolev embedding, and apply Hölder to every term. When $kp>n$, one factor may always be placed in $L^\infty$, proving the algebra estimate.

# Sharpness

The quantity $k-n/p$ is invariant under Euclidean dilation and therefore measures effective regularity. At equality, continuity may hold into a finite $L^q$ space but compactness generally fails through concentration or oscillation.

