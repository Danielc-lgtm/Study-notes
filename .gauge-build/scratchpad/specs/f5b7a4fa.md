# PAGE SPEC

- **Filename:** `Thm - Winding Number of a Map from the Circle to U(1).md`
- **Type:** theorem
- **Chapter:** Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles  (folder `Gauge Theory III/`)
- **Section:** §3.5 Smooth-Topological Tools — Generic Sections, Degree, and Homotopy Invariance of Bundles

## Spec (from the manifest)

type: theorem; source items: none of the sources directly (needed for B-T2.2.13's meaning, A-E2.4.1, A-R3.1.5, B-T2.5.8, and V's abelian holonomy); prereqs: [Thm - The Brouwer Degree is an Integer and a Homotopy Invariant, Thm - Stokes' Theorem on Manifolds]; statement: For smooth $g\colon S^1\to U(1)$ define $w(g):=\tfrac{1}{2\pi}\int_{S^1}g^*d\theta=\tfrac{1}{2\pi i}\int_{S^1}g^{-1}dg$. Then (a) $w(g)\in\mathbb Z$ and $w(g)=\deg g$; (b) $w(g_1g_2)=w(g_1)+w(g_2)$ and $w(g^{-1})=-w(g)$ (pointwise product); (c) $w$ is invariant under smooth homotopy; (d) $w(g)=0$ iff $g=e^{iu}$ for a smooth $u\colon S^1\to\mathbb R$ iff $g$ extends to a smooth map $D^2\to U(1)$; (e) $w(z\mapsto z^k)=k$; proof: (a) via the degree theorem ($d\theta/2\pi$ is a normalised volume form); (b) $d\theta$ is bi-invariant and $(g_1g_2)^*d\theta=g_1^*d\theta+g_2^*d\theta$ exactly (since $U(1)$ is abelian); (c) homotopy invariance; (d) $u(t):=\int_0^tg^*d\theta$ descends iff $w=0$; extension over the disc by $e^{iu(r,\theta)}$ with a cutoff, and conversely by Stokes; (e) direct; reference: Lee ISM 2e Ex. 17-? / Bott–Tu §?; AT II `Thm - Pi_1 of S^1 is Z` is a bridge (the same integer via lifts); spec: Targets: the Hopf transition function $z/|z|$ has $w=1$, so the Hopf bundle is nontrivial (exercise below); the degree of a line bundle over a surface (§3.6); abelian holonomy (V).
