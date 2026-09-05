#!/usr/bin/env bash
# Codex cloud environment setup script for Danielc-lgtm/Study-notes.
#
# Runs once per fresh container, BEFORE the agent phase, while (a) internet is on
# and (b) environment secrets are still present. Secrets are wiped before the agent
# starts, so this script persists the GitHub token into files that survive:
#   ~/.git-credentials      -> git push / fetch over HTTPS
#   ~/.config/gh/hosts.yml  -> gh pr create / gh pr merge
#
# Configure in ChatGPT -> Codex -> Environments -> (this repo) -> Setup script:
#     bash .codex/setup.sh
# and add a Secret named GH_TOKEN holding a fine-grained personal access token
# scoped to this repository (Contents: read/write, Pull requests: read/write).
# See .codex/README.md for the full checklist.

set -uo pipefail

log() { printf '[setup] %s\n' "$*"; }

# ---- 1. Git identity (override with env vars GIT_USER_NAME / GIT_USER_EMAIL) ----
git config --global user.name  "${GIT_USER_NAME:-Codex (Study-notes)}"
git config --global user.email "${GIT_USER_EMAIL:-codex@users.noreply.github.com}"
git config --global pull.rebase false
git config --global init.defaultBranch main

# ---- 2. Persist GitHub credentials for git ----
if [ -z "${GH_TOKEN:-}" ]; then
  log "WARNING: secret GH_TOKEN is not set. git push and gh will be unauthenticated."
  log "         Add it under Environment -> Secrets, then re-run setup."
else
  git config --global credential.helper store
  # Username is ignored by GitHub for PATs; the token is the password.
  printf 'https://x-access-token:%s@github.com\n' "$GH_TOKEN" > "$HOME/.git-credentials"
  chmod 600 "$HOME/.git-credentials"
  log "git credentials stored for github.com"
fi

# ---- 3. Install the GitHub CLI if the image lacks it ----
if ! command -v gh >/dev/null 2>&1; then
  log "gh not found; installing"
  SUDO=""; [ "$(id -u)" -ne 0 ] && command -v sudo >/dev/null 2>&1 && SUDO="sudo"
  if command -v apt-get >/dev/null 2>&1; then
    $SUDO mkdir -p -m 755 /etc/apt/keyrings
    curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
      | $SUDO tee /etc/apt/keyrings/githubcli-archive-keyring.gpg >/dev/null
    $SUDO chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" \
      | $SUDO tee /etc/apt/sources.list.d/github-cli.list >/dev/null
    $SUDO apt-get update -qq && $SUDO apt-get install -y -qq gh
  fi
  # Fallback: static binary from GitHub releases.
  if ! command -v gh >/dev/null 2>&1; then
    ARCH=$(uname -m); case "$ARCH" in x86_64) ARCH=amd64;; aarch64) ARCH=arm64;; esac
    VER=$(curl -fsSL https://api.github.com/repos/cli/cli/releases/latest | grep -o '"tag_name": *"v[^"]*"' | grep -o 'v[0-9.]*' | head -1)
    VER=${VER#v}
    curl -fsSL "https://github.com/cli/cli/releases/download/v${VER}/gh_${VER}_linux_${ARCH}.tar.gz" -o /tmp/gh.tgz
    mkdir -p "$HOME/.local/bin" && tar -xzf /tmp/gh.tgz -C /tmp \
      && cp "/tmp/gh_${VER}_linux_${ARCH}/bin/gh" "$HOME/.local/bin/gh" && chmod +x "$HOME/.local/bin/gh"
    # PATH edits in this script do not persist to the agent phase; symlink into a standard dir.
    $SUDO ln -sf "$HOME/.local/bin/gh" /usr/local/bin/gh 2>/dev/null || true
  fi
fi

# ---- 4. Log gh in from the token (persists to ~/.config/gh/hosts.yml) ----
# gh refuses to write hosts.yml while GH_TOKEN/GITHUB_TOKEN are in the environment
# (it would just use the variable), so unset them for these two calls only.
REDACT='s/\(gh[pousr]_\|github_pat_\)[A-Za-z0-9_]*/<redacted>/g'
if command -v gh >/dev/null 2>&1 && [ -n "${GH_TOKEN:-}" ]; then
  printf '%s\n' "$GH_TOKEN" | env -u GH_TOKEN -u GITHUB_TOKEN gh auth login --hostname github.com --with-token 2>&1 | sed "$REDACT"
  env -u GH_TOKEN -u GITHUB_TOKEN gh auth status 2>&1 | sed "$REDACT" || true
  if [ -s "$HOME/.config/gh/hosts.yml" ]; then
    log "gh login persisted to ~/.config/gh/hosts.yml"
  else
    # gh only writes hosts.yml after a successful online validation; write it
    # ourselves so a transient API hiccup here cannot leave the agent without gh.
    log "gh login did not persist; writing ~/.config/gh/hosts.yml directly"
    mkdir -p "$HOME/.config/gh"
    printf 'github.com:\n    user: %s\n    oauth_token: %s\n    git_protocol: https\n' \
      "${GH_USER:-Danielc-lgtm}" "$GH_TOKEN" > "$HOME/.config/gh/hosts.yml"
    chmod 600 "$HOME/.config/gh/hosts.yml"
  fi
fi

# ---- 5. Make sure the remote is plain HTTPS so the stored credential applies ----
if git -C "$(git rev-parse --show-toplevel 2>/dev/null || echo .)" remote get-url origin >/dev/null 2>&1; then
  git remote set-url origin https://github.com/Danielc-lgtm/Study-notes.git || true
  git fetch origin --prune --quiet || log "WARNING: fetch failed (check internet/allowlist and GH_TOKEN)"
fi

# ---- 6. Python for the vault audit scripts (stdlib only; nothing to install) ----
python3 --version || log "WARNING: python3 missing; the .claude/skills/polymath-notes/scripts audits need it"

log "done"
