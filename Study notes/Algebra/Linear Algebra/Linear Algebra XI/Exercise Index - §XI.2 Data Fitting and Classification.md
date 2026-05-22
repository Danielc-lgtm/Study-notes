---
type: exercise-index
subject: linear-algebra
section: "XI.2"
tags: [algebra, linear-algebra, applied, data-fitting, machine-learning]
---

## §XI.2 Data Fitting and Classification — Exercises

The exercises in this section drill the application of LS to *data fitting* (continuous outcomes) and *classification* (discrete outcomes). The recurring skill is recognizing that *any* linear-in-parameters model — polynomial, sinusoidal, one-hot encoded categorical, neural-network-features — gives a LS problem with appropriate design matrix, and that the overfitting / underfitting diagnostic is the train/test error gap. These exercises also drill the validation discipline of holding out data and measuring generalization, which transfers to *any* model fit to data.

- [[Ex - Polynomial fitting and overfitting]] (⭐⭐) — Sweep polynomial degree, fit each by LS, evaluate on held-out test data; observe the U-shape on test error and identify the optimal degree. The canonical diagnostic of bias-variance tradeoff in practice ([[Def - Least Squares Data Fitting]], [[Def - Validation (Training and Test Error)]], [[Thm - Least Squares via QR Factorization]], [[Thm - Bias-Variance Tradeoff in Regularized LS]]).

- [[Ex - Binary classifier via least squares]] (⭐⭐) — Build an LS classifier on the Iris dataset, evaluate via confusion matrix and ROC curve, cross-validate. The skill is converting a classification problem to an LS regression on $\pm 1$ labels and thresholding the output ([[Def - Least Squares Classifier]], [[Def - Least Squares Data Fitting]], [[Def - Validation (Training and Test Error)]], [[Thm - Least Squares via QR Factorization]]).

- [[Ex - Tikhonov regularization is a multi-objective LS problem]] (⭐) — Verify that Tikhonov regularization is *literally* multi-objective LS with stacked matrices, deriving the standard $(A^T A + \lambda I)^{-1} A^T b$ formula from the stacked-matrix LS solution. The conceptual unification of regularization with the broader multi-objective LS framework ([[Def - Regularized Least Squares]], [[Def - Multi-Objective Least Squares]], [[Thm - Existence and Uniqueness of Least Squares Solution]]).
