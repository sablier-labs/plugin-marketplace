# Context

Claude Code plugin marketplace for Sablier projects.

See the [official Anthropic docs](https://code.claude.com/docs/en/plugin-marketplaces) for more information.

## Plugin Structure

Each plugin follows Claude Code conventions:

- **`.claude-plugin/plugin.json`** — Plugin manifest with name, version, description
- **`agents/`** — Subagent definitions (`.md` files)
- **`commands/`** — Slash commands (`.md` files with YAML frontmatter)
- **`hooks/`** — Event handlers (`hooks.json`)
- **`skills/`** — Auto-discovered skills (each in its own directory with `SKILL.md`)

Note that not all directories mentioned above may be present in every plugin.

## Formatting

Use `mdformat` for Markdown:

```bash
just mdformat-check
just mdformat-write
```

Use Prettier for JSON and YAML:

```bash
nlx prettier --write "**/*.{json,jsonc,yaml,yml}"
nlx prettier --check "**/*.{json,jsonc,yaml,yml}"
```

Make sure to run `just full-write` after editing files or generating new ones.
