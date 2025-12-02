# plugin-marketplace

Official Sablier plugin marketplace for AI agents like Claude Code.

See Anthropic's [official docs](https://code.claude.com/docs/en/plugin-marketplaces) for more guidance on plugins.

## Plugins

### sablier

General-purpose development tools for TypeScript, React, and Next.js projects.

**Skills:**

- `sablier` — Sablier protocol overview: token vesting, airdrops, and onchain payroll
- `design` — Sablier dark-theme aesthetic and production-grade React interfaces
- `effect-ts` — Effect-TS functional programming patterns
- `effect-ts-next` — Effect-ts + Next.js patterns
- `etherscan-api` — Etherscan API V2 for blockchain balance queries
- `tailwind-v4` — Tailwind CSS v4 rules and tailwind-variants
- `vitest-v4` — Vitest v4 testing patterns for TypeScript React/Next.js
- `zustand` — Zustand state management with TypeScript

**Commands:**

- `/spec-screenshot` — Analyze screenshots and generate `SPEC.md` implementation specs

## Installation

> [!IMPORTANT]
>
> To be able to use the plugins, you must have [ni](https://github.com/antfu-collective/ni) installed globally.

```bash
npm i -g @antfu/ni
```

Then, run these commands in a Claude Code chat:

```
# Add this repository as a marketplace
/plugin marketplace add sablier-labs/plugin-marketplace

# Install the plugin
/plugin install sablier@plugin-marketplace
```

Restart Claude Code, then verify with `/plugin browse` to confirm skills and commands are loaded.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
