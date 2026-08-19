---
type: remark
subject: probability-geometry
prereqs:
  - "Thm - Fourier Inversion by Homology Class"
  - "Def - First Homology, Characters, and Finite Fourier Analysis"
tags: [paper, brownian-loops, homology, hodge-theory]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Remark 6.6"
---

# Notation

- $X$ a *closed* hyperbolic surface of genus $g \ge 2$ (Remark 6.6 is stated only in the closed case).
- $H_1(X, \mathbb{Z}) \cong \mathbb{Z}^{2g}$ the first (integer) homology group.
- $H^1_{\mathrm{dR}}(X, \mathbb{R})$ the (real) first de Rham cohomology; $\mathcal{H}^1(X)$ the space of real harmonic $1$-forms; $\mathcal{H}^1_{\mathbb{Z}}(X)$ the sublattice of harmonic $1$-forms with all periods integers.
- $\omega \in \mathcal{H}^1(X)$ a real harmonic $1$-form; $[\omega] \in \mathcal{H}^1(X)/\mathcal{H}^1_{\mathbb{Z}}(X)$ its class modulo integer-period forms.
- $\int_\beta \omega \in \mathbb{R}$ the *period* of $\omega$ around the cycle $\beta \in H_1(X, \mathbb{Z})$: the integral of $\omega$ along any smooth representative loop of $\beta$ (independent of representative because $\omega$ is closed).
- $\operatorname{Jac}(X)$ the *Jacobian variety* of $X$: a compact real torus of real dimension $2g$ (equivalently, a complex torus of complex dimension $g$ via the Hodge star).
- $d[\omega]$ the normalised Haar measure on $\operatorname{Jac}(X)$ (total mass $1$).
- $\chi_{[\omega]} : H_1(X, \mathbb{Z}) \to S^1$ the unitary character built from a harmonic form class $[\omega]$: $\chi_{[\omega]}(\beta) := e^{2\pi i \int_\beta \omega}$.
- $L_X(s, \chi)$ the Selberg $L$-function; $\mu^\kappa_X(\beta)$ the killed loop mass in homology class $\beta$.

> [!recall]- Harmonic $1$-forms $\mathcal{H}^1(X)$ and their periods $\int_\beta \omega$
> **Formally:** on a closed Riemannian surface $X$, a *real $1$-form* is a smooth section of the cotangent bundle — locally $\omega = f(x, y)\,dx + g(x, y)\,dy$; it is *harmonic* if $d\omega = 0$ and $d(*\omega) = 0$, where $d$ is the exterior derivative and $*$ the Hodge star; equivalently, $\omega$ is closed and co-closed. The space $\mathcal{H}^1(X)$ of real harmonic $1$-forms has real dimension $2g$ (Hodge theorem). For $\omega \in \mathcal{H}^1(X)$ and $\beta \in H_1(X, \mathbb{Z})$, the *period* $\int_\beta \omega := \int_c \omega$ (any smooth loop $c$ representing $\beta$) is a real number, independent of the representative by Stokes' theorem ($\omega$ closed).
> **In words:** harmonic $1$-forms are the smoothest possible $1$-forms — the "constant-slope" fields on the surface. The *period* around a cycle is the integrated flow along that cycle; because $\omega$ is closed, sliding the cycle within its homology class does not change the integral. The Hodge theorem says the space of such forms has the right dimension to identify with $H_1(X, \mathbb{R})$'s dual, so each harmonic form is a linear functional on cycles.
> **Concretely:** on the flat torus $T^2 = \mathbb{R}^2/\mathbb{Z}^2$, the constant $1$-forms $\omega_1 = dx$ and $\omega_2 = dy$ are harmonic and form a basis of $\mathcal{H}^1(T^2)$; periods are elementary: $\int_{(a,b)}(\alpha\,dx + \beta\,dy) = a\alpha + b\beta$. So an $\omega = \alpha\,dx + \beta\,dy$ has period vector $(\alpha, \beta) \in \mathbb{R}^2$; the corresponding character is $\chi_\omega((a, b)) = e^{2\pi i(a\alpha + b\beta)}$ — exactly the character parametrisation from [[Def - First Homology, Characters, and Finite Fourier Analysis]]. On a genus-$g$ closed surface, $\mathcal{H}^1$ has $2g$ generators (each harmonic form is determined by its $2g$ periods against a symplectic basis of $H_1$), and the Jacobian $\operatorname{Jac}(X) = \mathcal{H}^1/\mathcal{H}^1_{\mathbb{Z}}$ is a compact $2g$-torus with a complex structure inherited from $*$.

> [!recall]- Jacobian variety $\operatorname{Jac}(X)$ (closed-case identification with $\widehat{H_1}$)
> **Formally:** on a closed hyperbolic surface, the Hodge theorem gives $H^1_{\mathrm{dR}}(X, \mathbb{R}) \cong \mathcal{H}^1(X)$, a real vector space of dimension $2g$; the de Rham period map sends $H_1(X, \mathbb{Z}) \hookrightarrow \mathcal{H}^1(X)^*$ as a lattice of full rank (Poincaré duality). Dually, the sublattice $\mathcal{H}^1_{\mathbb{Z}}(X) := \{\omega \in \mathcal{H}^1(X) : \int_\beta \omega \in \mathbb{Z}\ \forall \beta \in H_1(X, \mathbb{Z})\}$ has full rank in $\mathcal{H}^1(X)$. The quotient torus $\operatorname{Jac}(X) := \mathcal{H}^1(X)/\mathcal{H}^1_{\mathbb{Z}}(X)$ is a *real* torus of dimension $2g$; the Hodge star $*$ (with $*^2 = -1$ on $1$-forms) gives $\mathcal{H}^1(X)$ a complex structure, making $\operatorname{Jac}(X)$ a *complex torus* of complex dimension $g$. The map $[\omega] \mapsto \chi_{[\omega]}$, $\chi_{[\omega]}(\beta) := e^{2\pi i \int_\beta \omega}$, gives an isomorphism $\operatorname{Jac}(X) \cong \widehat{H_1(X, \mathbb{Z})}$ of compact abelian groups (the character torus).
> **In words:** the Jacobian is a compact torus manufactured from the harmonic $1$-forms modulo those with integer periods; it is $2g$-dimensional over the reals and, thanks to the Hodge star acting like multiplication by $i$, admits a complex structure making it $g$-dimensional over $\mathbb{C}$. Each point of $\operatorname{Jac}(X)$ gives, via its harmonic-form representative $\omega$, a way of assigning a unit-modulus complex number to each homology class $\beta$ by exponentiating $2\pi i$ times its period $\int_\beta \omega$ — i.e. a unitary character of $H_1(X, \mathbb{Z})$. This identifies $\operatorname{Jac}(X)$ with the character torus $\widehat{H_1(X, \mathbb{Z})}$ (Pontryagin dual of $\mathbb{Z}^{2g}$), which is what makes it a natural domain for Fourier inversion.
> **Concretely:** on the flat torus $T^2 = \mathbb{R}^2/\mathbb{Z}^2$, $\mathcal{H}^1$ is spanned by $dx, dy$; $\mathcal{H}^1_{\mathbb{Z}}$ is the $\mathbb{Z}$-lattice they generate; the Jacobian is $\mathcal{H}^1/\mathcal{H}^1_{\mathbb{Z}} = \mathbb{R}^2/\mathbb{Z}^2 = T^2$ itself — the Jacobian of the flat torus is the torus. On a genus-$2$ closed surface, $\operatorname{Jac}(X)$ is a complex $2$-torus $\mathbb{C}^2/\Lambda$ for some rank-$4$ lattice $\Lambda \subset \mathbb{C}^2$; the character $\chi_{[\omega]}$ of $H_1(X, \mathbb{Z}) = \mathbb{Z}^4$ is $\chi_{[\omega]}(\beta) = e^{2\pi i \int_\beta \omega}$, with the integral running over any smooth representative of $\beta$. Standard reference: Farkas–Kra, *Riemann Surfaces*, Ch. III.

---

# Statement

> **Remark 6.6 (Jacobian form of the inversion, closed case; Belyaev–Huseynli).** On a *closed* hyperbolic surface $X$ (genus $g \ge 2$), the character torus is naturally identified with the Jacobian variety, $\widehat{H_1(X, \mathbb{Z})} \cong \operatorname{Jac}(X)$, via $[\omega] \mapsto \chi_{[\omega]}$, $\chi_{[\omega]}(\beta) = e^{2\pi i \int_\beta \omega}$. Under this identification, the [[Thm - Fourier Inversion by Homology Class|Theorem 6.5]] inversion formula for the mass in a homology class $\beta$ reads
> $$\mu^\kappa_X(\beta) = \int_{\operatorname{Jac}(X)}\big(-\log L_X(s, \chi_{[\omega]})\big)\,e^{-2\pi i \int_\beta \omega}\,d[\omega],$$
> where $d[\omega]$ is the normalised Haar measure on the Jacobian torus (which coincides with the pullback of the Haar measure $d\chi$ under the isomorphism $\operatorname{Jac}(X) \cong \widehat{H_1(X, \mathbb{Z})}$).

---

# In One Line

For a closed surface, the character torus $\widehat{H_1(X, \mathbb{Z})}$ is the Jacobian $\operatorname{Jac}(X)$ (a compact $g$-dimensional complex torus of harmonic-form classes), so the Fourier-inversion formula for $\mu^\kappa_X(\beta)$ becomes an integral over the Jacobian against the unitary holonomy $e^{-2\pi i\int_\beta \omega}$.

---

# Unpacking

**The identification $\widehat{H_1} \cong \operatorname{Jac}$ is *only* available in the closed case.** For a geometrically finite non-compact surface (cusps, funnels, or both), the Hodge theorem in the form used above requires care — square-integrable harmonic forms exist but the correspondence with $H^1_{\mathrm{dR}}$ needs additional cohomology (parabolic cohomology, weighted Hodge theory, etc.). The paper says explicitly: "In the geometrically finite non-compact case the identification with the Jacobian is not available; while partial analogues exist, they require much more Hodge-theoretic machinery than we would like to invoke in this paper." So Theorem 6.5 is the general statement (works for closed *and* non-compact geometrically finite), and Remark 6.6 is its *Hodge-theoretic reformulation* in the closed case where the character torus can be pictured as a concrete complex torus of harmonic forms.

**Same identity, different coordinates.** The Jacobian formula is not a new theorem beyond Theorem 6.5 — it is the same equation, rewritten in the coordinates that make the characters explicit periods of harmonic forms. Concretely, the isomorphism $\operatorname{Jac}(X) \ni [\omega] \mapsto \chi_{[\omega]} \in \widehat{H_1}$ sends $d[\omega] \mapsto d\chi$ (both are the normalised Haar measures on isomorphic compact tori, uniquely determined by translation invariance and total mass $1$), and $e^{-2\pi i \int_\beta \omega} = \overline{\chi_{[\omega]}(\beta)}$. So plugging into Theorem 6.5's inversion formula gives Remark 6.6 verbatim. The value of the reformulation is expository, not additional content: it lets one *see* the character torus as the natural moduli space of unitary line bundles / periods of harmonic forms — a picture familiar from classical algebraic geometry.

**Concretely, on the flat torus (as an illustrative special case).** For $T^2 = \mathbb{R}^2/\mathbb{Z}^2$ (which is not hyperbolic but the identification is the same), $\mathcal H^1$ is spanned by $dx, dy$; $\operatorname{Jac}(T^2) = T^2$; a harmonic form is $\omega = u\,dx + v\,dy$ and its period along the cycle $\beta = (a, b) \in \mathbb{Z}^2$ is $\int_\beta \omega = au + bv$; the character is $\chi_\omega((a, b)) = e^{2\pi i(au + bv)}$. The Jacobian form of the inversion then reads
$$\mu^\kappa_{T^2}((a, b)) = \int_0^1\!\int_0^1(-\log L_{T^2}(s, \chi_{(u,v)}))\,e^{-2\pi i(au + bv)}\,du\,dv$$
— an ordinary $2$-D Fourier coefficient extraction on the unit square, dressed in harmonic-form language.

**Why the closed case is "cleaner".** On a closed surface, $\operatorname{Jac}(X)$ is a well-understood object: a principally polarised abelian variety of complex dimension $g$, carrying the intersection pairing as its polarisation. The pairing $\langle \beta, [\omega]\rangle = \int_\beta \omega \pmod{\mathbb{Z}}$ that defines $\chi_{[\omega]}$ is the *canonical* pairing between $H_1$ and its dual (via the Poincaré dual identification with $H^1$), so the Fourier-inversion identity acquires a natural geometric interpretation: integrate the log $L$-function over the moduli of unitary line bundles. In the non-compact case none of that classical structure survives without extra work, which is why the paper leaves it to Remark 6.6.

**Intuition-not-proof flag.** ⚠️ The Hodge-theoretic identification $\widehat{H_1(X, \mathbb{Z})} \cong \operatorname{Jac}(X)$ is recalled here at the compact-abelian-group level; the full statement (with the complex structure, the principal polarisation, and the compatibility with the intersection pairing) is used in the remark's phrasing but is not re-derived in these notes. It is standard (see Farkas–Kra, *Riemann Surfaces*, Ch. III; Griffiths–Harris, *Principles of Algebraic Geometry*, Ch. 2 §2). The paper takes it as given, and so do the notes.

---

# Where the paper uses this

Stated as an aside to [[Thm - Fourier Inversion by Homology Class|Theorem 6.5]] in [[Paper - Brownian Loops — Homotopy and Homology — §6 A Probability Measure on Classes|§6.2]]; not used structurally elsewhere in the paper. Its value is that it identifies the character torus with a classical object (the Jacobian) in the closed case, connecting the analytic Fourier inversion to Hodge theory and providing the natural coordinates for the closed-surface reader.
