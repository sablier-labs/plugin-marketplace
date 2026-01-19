set allow-duplicate-variables
set allow-duplicate-recipes
set shell := ["bash", "-euo", "pipefail", "-c"]
set unstable

# ---------------------------------------------------------------------------- #
#                                    RECIPES                                   #
# ---------------------------------------------------------------------------- #

# Show available commands
default:
    @just --list

# Install dependencies
install-deps:
    just install-uv
    just install-mdformat
    just install-ni
alias id := install-deps

# Install mdformat
install-mdformat:
    uv tool install mdformat --with mdformat-frontmatter --with mdformat-gfm
alias im := install-mdformat

# Install ni
install-ni:
    npm i -g @antfu/ni
alias in := install-ni

# Install uv on macOS and Linux
install-uv:
    curl -LsSf https://astral.sh/uv/install.sh | sh
alias iu := install-uv

# Set up git hooks (run once after cloning)
setup-hooks:
    git config core.hooksPath .husky
alias sh := setup-hooks

# ---------------------------------------------------------------------------- #
#                                    CHECKS                                    #
# ---------------------------------------------------------------------------- #

# Run all code checks
[group("checks")]
@full-check:
    just _run-with-status mdformat-check
    echo ""
    echo -e '{{ GREEN }}All code checks passed!{{ NORMAL }}'
alias fc := full-check

# Run all code fixes
[group("checks")]
@full-write:
    just _run-with-status mdformat-write
    echo ""
    echo -e '{{ GREEN }}All code fixes applied!{{ NORMAL }}'
alias fw := full-write

# Check mdformat formatting
[group("checks")]
@mdformat-check +paths=".":
    mdformat --check {{ paths }}
alias mc := mdformat-check

# Format using mdformat
[group("checks")]
@mdformat-write +paths=".":
    mdformat {{ paths }}
alias mw := mdformat-write

# ---------------------------------------------------------------------------- #
#                                   UTILITIES                                  #
# ---------------------------------------------------------------------------- #

# Private recipe to run a check with formatted output
@_run-with-status recipe:
    echo ""
    echo -e '{{ CYAN }}→ Running {{ recipe }}...{{ NORMAL }}'
    just {{ recipe }}
    echo -e '{{ GREEN }}✓ {{ recipe }} completed{{ NORMAL }}'
