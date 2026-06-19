---
type: definition
subject: model-categories
prereqs:
  - "Def - Model Category"
  - "Def - Lifting Property and the Retract Argument"
  - "Def - Initial and Terminal Object"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $\mathcal{M}$ is a model category with weak equivalences $\mathcal{W}$, cofibrations (written $\rightarrowtail$), and fibrations (written $\twoheadrightarrow$); $\varnothing$ is the initial object and $*$ the terminal object. A trivial fibration is written $\xrightarrow{\sim}\twoheadrightarrow$ and a trivial cofibration $\xrightarrow{\sim}\rightarrowtail$. We write $QX$ for a cofibrant replacement of $X$ and $RX$ for a fibrant replacement. The full symbol registry is on [[Model Categories — Quillen's Axiomatization of Homotopy Theory]].

---

# Axiom Motivation

The motivation here is a single recurring frustration: most constructions in homotopy theory only behave well on *some* objects, and you need a systematic way to replace a bad object by a good one without changing its homotopy type. Cofibrant and fibrant objects are the names of the two flavours of "good," and (co)fibrant replacement is the systematic fix.

To see why two flavours are needed, recall the two things that can go wrong. When you apply a left adjoint (or take a colimit), the construction respects weak equivalences only on objects "built freely from below," and those are the **cofibrant** ones — the objects $X$ for which the map $\varnothing \to X$ from nothing is a cofibration, meaning $X$ is assembled by attaching cells starting from the empty object. When you apply a right adjoint (or take a limit), the construction respects weak equivalences only on objects "with enough room above," the **fibrant** ones — the objects $X$ for which $X \to *$ is a fibration. The asymmetry is real and unavoidable: a left adjoint wants cofibrant input, a right adjoint wants fibrant input, and the homotopy relation wants *both*.

Why define cofibrant via the map *from the initial object* specifically? Because that map is the universal "build $X$ from scratch." Saying $\varnothing \to X$ is a cofibration says $X$ is obtained from the initial object by a good inclusion — in $\mathbf{Top}$, that $X$ is a retract of a cell complex; in $\mathbf{Ch}(R)$, that $X$ is a complex of projectives. If you instead asked some other map to be a cofibration, you would be making a claim about $X$ *relative to* something, not an intrinsic property. The map from $\varnothing$ is the only canonical map *into* $X$ that every object possesses, so it is the only candidate for an intrinsic cofibrancy condition. Dually, $X \to *$ is the only canonical map *out of* $X$, so fibrancy is its mirror.

The payoff is (co)fibrant replacement, and it is forced by factorization (MC5). To replace $X$ by a cofibrant object, factor the map $\varnothing \to X$ as $\varnothing \rightarrowtail QX \xrightarrow{\sim} X$: the first factor makes $QX$ cofibrant, the second is a weak equivalence so $QX$ has the same homotopy type as $X$. Dually, factor $X \to *$ as $X \xrightarrow{\sim} RX \twoheadrightarrow *$ to make $RX$ fibrant. Drop MC5 and these replacements do not exist, and then derived functors and the homotopy category — both of which run on replacement — collapse. So the definitions of cofibrant and fibrant are not free-floating; they are exactly the conditions that the factorization axiom is built to supply.

---

# The Definition

Let $\mathcal{M}$ be a model category with initial object $\varnothing$ and terminal object $*$.

- An object $X$ is **cofibrant** if the unique map $\varnothing \to X$ is a cofibration.
- An object $X$ is **fibrant** if the unique map $X \to *$ is a fibration.
- An object is **bifibrant** (or *fibrant–cofibrant*) if it is both cofibrant and fibrant.

**Cofibrant replacement.** By the factorization axiom MC5, the map $\varnothing \to X$ factors as
$$\varnothing \;\rightarrowtail\; QX \;\xrightarrow{\ \sim\ }\; X,$$
a cofibration followed by a trivial fibration. The object $QX$ is cofibrant and the structure map $q_X : QX \xrightarrow{\sim} X$ is a trivial fibration. We call $QX$ a **cofibrant replacement** of $X$.

**Fibrant replacement.** Dually, the map $X \to *$ factors as
$$X \;\xrightarrow{\ \sim\ }\; RX \;\twoheadrightarrow\; *,$$
a trivial cofibration followed by a fibration. The object $RX$ is fibrant and the structure map $r_X : X \xrightarrow{\sim} RX$ is a trivial cofibration. We call $RX$ a **fibrant replacement** of $X$.

When the factorizations are functorial (Hovey's formulation), $Q$ and $R$ are functors $\mathcal{M} \to \mathcal{M}$ and $q$, $r$ are natural transformations. To make a bifibrant replacement, apply both: $QRX$ (first fibrant-replace, then cofibrant-replace) or $RQX$ is bifibrant and weakly equivalent to $X$.

---

# Relate to Other Fields / Compression

The cofibrant–fibrant dichotomy is the abstract form of the resolution dichotomy in homological algebra. In $\mathbf{Ch}(R)$ with the projective model structure, **cofibrant replacement is projective resolution**: a cofibrant replacement of a module $M$ (viewed as a complex concentrated in degree zero) is a projective resolution $\cdots \to P_1 \to P_0 \to 0$ quasi-isomorphic to $M$. Dually, in the *injective* model structure, fibrant replacement is **injective resolution**. The two flavours of derived functor you learned — left-derived functors via projective resolutions ($\mathbf{Tor}$), right-derived via injective resolutions ($\mathbf{Ext}$) — are exactly the two flavours of replacement, cofibrant for left-derived, fibrant for right-derived. The asymmetry "left adjoint wants cofibrant, right adjoint wants fibrant" *is* the asymmetry "$\mathbf{Tor}$ wants projectives, $\mathbf{Ext}$ wants injectives."

In topology the compression is to CW approximation: a cofibrant replacement of a space is a CW complex weakly equivalent to it (CW approximation), the construction that lets you prove theorems about CW complexes and conclude them for all spaces. Every space being fibrant in $\mathbf{Top}$ is why you rarely hear about fibrant replacement of spaces — but the moment you pass to a setting where not everything is fibrant (pointed spaces, spectra), it returns.

**True name:** a cofibrant object is **"built from nothing by attaching cells"** and a fibrant object is **"has the homotopy lifting / extension room to be a target."** When you see "cofibrant," picture a CW complex or a complex of projectives; when you see "fibrant," picture a Kan complex or an injective object.

---

# Examples / Corollaries

**Is an instance — every CW complex is cofibrant in $\mathbf{Top}$.** A CW complex is built from $\varnothing$ by attaching cells $D^n$ along their boundaries $S^{n-1}$, so $\varnothing \to X$ is a relative cell complex, hence a cofibration. More generally the cofibrant objects of $\mathbf{Top}$ are exactly the retracts of cell complexes.

**Is an instance — every space is fibrant in $\mathbf{Top}$.** The map $X \to *$ is always a Serre fibration (the homotopy lifting property against disks holds trivially when the target is a point), so every topological space is fibrant. This is the structural reason classical homotopy theory rarely mentions fibrant replacement of spaces.

**Is an instance — projective modules give cofibrant complexes.** In $\mathbf{Ch}(R)$, a bounded-below complex of projective $R$-modules is cofibrant, and a cofibrant replacement of a module $M$ is a projective resolution of $M$. A free $R$-module is the simplest cofibrant object.

**Is an instance — every simplicial set is cofibrant.** In the Kan–Quillen model structure on $\mathbf{sSet}$, cofibrations are the monomorphisms and $\varnothing \to X$ is always a monomorphism, so every [[Def - Simplicial Set|simplicial set]] is cofibrant. The fibrant objects are precisely the [[Def - Kan Complex and the Nerve|Kan complexes]], so here it is fibrant replacement (a "Kan-ification") that does the work.

**Is NOT an instance — a non-Kan simplicial set is not fibrant.** The standard simplex $\Delta^1$ (the nerve of the arrow category $\bullet \to \bullet$) is *not* a Kan complex, because the horn $\Lambda^2_0 \to \Delta^1$ has no filler — there is no inverse to the arrow. So $\Delta^1$ is cofibrant (every simplicial set is) but not fibrant; its fibrant replacement is a Kan complex modelling the same homotopy type, which here is contractible. This is the cleanest example of an object that needs replacement on one side only.

**Is NOT an instance — a generic module is not cofibrant in $\mathbf{Ch}(R)$.** The $\mathbb{Z}$-module $\mathbb{Z}/2$, viewed as a complex in degree zero, is not cofibrant, because it is not projective; its cofibrant replacement is the projective resolution $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to 0$. Applying $-\otimes \mathbb{Z}/2$ to $\mathbb{Z}/2$ directly gives the wrong (un-derived) answer; applying it to the resolution computes $\mathrm{Tor}$.

**Calibration check.** Verify that the initial object $\varnothing$ is always cofibrant and the terminal object $*$ always fibrant (the relevant maps are identities, which lie in every class). Verify that the cofibrant replacement map $q_X : QX \to X$ is a weak equivalence by definition (it is a trivial fibration). If you can explain *why* one needs both $QX$ and $RX$ to form $\mathrm{Ho}(\mathcal{M})$ — because homotopy of maps is well-behaved only between bifibrant objects, per [[Def - Cylinder Object, Path Object, and Homotopy]] — you have understood the role of these objects.

---

# Unlocked by This

> [!tip] The Homotopy Category via Bifibrant Replacement *(from this chapter)*
> [[Thm - The Homotopy Category of a Model Category]] computes $\mathrm{Ho}(\mathcal{M})(X,Y)$ as homotopy classes $\pi(QRX, QRY)$ of maps between bifibrant replacements — the entire localization is computed on bifibrant objects, which is why these definitions are indispensable.

> [!tip] Derived Functors as Functors-After-Replacement *(from this chapter)*
> The total derived functors $\mathbf{L}F = F \circ Q$ and $\mathbf{R}U = U \circ R$ of [[Thm - Quillen Adjunctions Descend to Derived Adjunctions]] are nothing but "apply the functor after the appropriate replacement." Specializing to $\mathbf{Ch}(R)$ recovers **Tor** (left-derived, cofibrant/projective replacement) and **Ext** (right-derived, fibrant/injective replacement).

> [!tip] CW Approximation and Whitehead's Theorem *(from Algebraic Topology)*
> Cofibrant replacement in $\mathbf{Top}$ is **CW approximation**, and the fact that a weak equivalence between bifibrant (here: CW) objects is a homotopy equivalence is **Whitehead's theorem** — a special case of the general model-categorical principle that weak equivalences between bifibrant objects are homotopy equivalences.
