---
argument-hint: '[repo-name] [description] [--check]'
description: Create a GitHub issue in a sablier-labs repository
model: opus
---

## Context

- GitHub CLI auth: !`gh auth status 2>&1 | rg -q "Logged in" && echo "authenticated" || echo "not authenticated"`
- Arguments: $ARGUMENTS

## Skills

Activate the `gh-cli` skill for this command.

## Your Task

### STEP 1: Validate prerequisites

IF not authenticated: ERROR "Run `gh auth login` first"

### STEP 2: Parse repository argument

The **first token** in $ARGUMENTS is the repository name (without the org prefix).

- Extract the first token as `repo_name`
- Set `repository = sablier-labs/{repo_name}`
- Remove the first token from $ARGUMENTS (remaining text is the issue description)

Example: `/sablier:create-issue lockup "Bug in cliff streams"` -> `repository = sablier-labs/lockup`

### STEP 2.5: Parse optional flags

IF `$ARGUMENTS` contains `--check`:

- Remove `--check` from `$ARGUMENTS`
- Set `check_mode = true`
- Continue to STEP 2.6

ELSE:

- Set `check_mode = false`
- Skip STEP 2.6 and continue to STEP 3

### STEP 2.6: Check for similar issues (if `--check` flag present)

**ONLY if `check_mode = true`:**

1. Extract key terms from the remaining `$ARGUMENTS` (issue description)

1. Search for similar open issues (full-text search across title and body):

   ```bash
   gh search issues "{key_terms}" --repo "sablier-labs/{repo_name}" --state open --limit 10 --json number,title,url
   ```

1. **IF similar issues found:**

   - Display the list of potentially related issues to the user
   - Use `AskUserQuestion` to prompt: "Similar issues found. Do you want to proceed with creating a new issue?"
     - Options: "Yes, create new issue" / "No, cancel"
   - IF user selects "No": Exit command with message "Issue creation cancelled"
   - IF user selects "Yes": Continue to STEP 3

1. **IF no similar issues found:**

   - Inform user: "No similar issues found. Proceeding with issue creation."
   - Continue to STEP 3

### STEP 3: Apply labels

From content analysis, determine:

- **Type**: Primary category (bug, feature, docs, etc.)
- **Work**: Complexity via Cynefin (clear, complicated, complex, chaotic)
- **Priority**: Urgency (0=critical to 3=nice-to-have)
- **Effort**: Size (low, medium, high, epic)
- **Scope**: Domain area (only for sablier-labs/command-center)

### STEP 4: Generate title and body

From remaining $ARGUMENTS, create:

- **Title**: Clear, concise summary (5-10 words)
- **Body**: Use this template:

```
## Problem

[Extracted from user description]

## Solution

[If provided, otherwise "TBD"]

## Files Affected

<details><summary>Toggle to see affected files</summary>
<p>

- [{filename1}](https://github.com/sablier-labs/{repo_name}/blob/main/{path1})
- [{filename2}](https://github.com/sablier-labs/{repo_name}/blob/main/{path2})

</p>
</details>
```

**Admonitions**: Add GitHub-style admonitions when appropriate:

- `> [!NOTE]` - For context, dependencies, or implementation details users should notice
- `> [!TIP]` - For suggestions on testing, workarounds, or best practices
- `> [!IMPORTANT]` - For breaking changes, required migrations, or critical setup steps
- `> [!WARNING]` - For potential risks, known issues, or things that could go wrong
- `> [!CAUTION]` - For deprecated features, temporary solutions, or things to avoid

Place admonitions after the relevant section.

File links:

- **MUST** use markdown format: `[{filename}](https://github.com/sablier-labs/{repo_name}/blob/main/{path})`
- **Link text** should be the relative file path (e.g., `src/file.ts`, `docusaurus.config.ts`)
- **URL** must be the full GitHub URL
- List one per line if multiple files
- **OMIT the entire "## Files Affected" section** if no files are specified (e.g., for feature requests or planning issues)

### STEP 5: Create the issue

```bash
gh issue create \
  --repo "sablier-labs/{repo_name}" \
  --title "$title" \
  --body "$body" \
  --label "label1,label2,label3"
```

Display: "Created issue: $URL"

On failure: show specific error and fix

## Label Reference

### Type

- `type: bug` - Something isn't working
- `type: feature` - New feature or request
- `type: perf` - Performance or UX improvement
- `type: docs` - Documentation
- `type: test` - Test changes
- `type: refactor` - Code restructuring
- `type: build` - Build system or dependencies
- `type: ci` - CI configuration
- `type: chore` - Maintenance work
- `type: style` - Code style changes

### Work (Cynefin)

- `work: clear` - Known solution
- `work: complicated` - Requires analysis but solvable
- `work: complex` - Experimental, unclear outcome
- `work: chaotic` - Crisis mode

### Priority

- `priority: 0` - Critical blocker
- `priority: 1` - Important
- `priority: 2` - Standard work
- `priority: 3` - Nice-to-have

### Effort

- `effort: low` - \<1 day
- `effort: medium` - 1-3 days
- `effort: high` - Several days
- `effort: epic` - Weeks, multiple PRs

### Scope (sablier-labs/command-center only)

- `scope: frontend`
- `scope: backend`
- `scope: evm`
- `scope: solana`
- `scope: data`
- `scope: devops`
- `scope: integrations`
- `scope: marketing`
- `scope: business`
- `scope: other`

## Examples

```bash
/sablier:create-issue lockup "Bug in stream creation for cliff durations"
/sablier:create-issue command-center "Add dark mode toggle to dashboard"
/sablier:create-issue lockup --check "Support dynamic durations"
/sablier:create-issue docs "Update integration guide for v2.2"
```
