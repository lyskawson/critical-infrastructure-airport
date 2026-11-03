# Overleaf - two workflows

Main file: **main.tex**. Compiler: **pdfLaTeX**. The project compiles with a typical TeX Live installation, without external drawing programs or shell escape.

## A. Import from GitHub

Requires premium GitHub Synchronization or an institutional entitlement.

1. Connect GitHub and Overleaf in account settings.
2. In Overleaf, choose **New Project → Import from GitHub**.
3. Select **critical-infrastructure-airport**.
4. Set main.tex as the main file and pdfLaTeX as compiler.
5. Compile and share with teammates within your plan limits.

Synchronisation is not automatic real-time sharing between GitHub and Overleaf. Use the synchronisation menu to pull GitHub changes and push approved Overleaf changes. Synchronise before switching tools to reduce conflicts.

Overleaf documentation describes creating a project from an existing repository or a new repository from a project; it does not directly connect two already existing independent projects.

## B. ZIP import

This option does not require Git synchronisation.

1. Obtain airport-overleaf.zip from `make overleaf` or GitHub build artifacts.
2. In Overleaf, choose **New Project → Upload Project** and select the ZIP.
3. Check main.tex and pdfLaTeX.
4. Edit metadata.tex, then files in sections/.

Changes in this workflow do not automatically reach GitHub. Export Overleaf sources and coordinate their integration; avoid editing the same chapters simultaneously in two places.

## Direct Overleaf Git

This is a separate premium feature. After project creation, Overleaf provides its own remote URL and token authentication. It can be added as a second local remote using the exact URL Overleaf supplies. A public GitHub repository alone does not enable this feature.

Verified 19 October 2026:

- [Git integration and GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization)
- [GitHub synchronization](https://docs.overleaf.com/integrations-and-add-ons/git-integration-and-github-synchronization/github-synchronization)
- [Git integration](https://www.overleaf.com/learn/how-to/Git_integration)
