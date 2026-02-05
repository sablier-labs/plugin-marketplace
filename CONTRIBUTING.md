## Contributing

### Prerequisites

- [ni](https://github.com/antfu-collective/ni) (package manager resolver)
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- [mdformat](https://github.com/hukkin/mdformat) (Markdown formatter)

### Setup

```bash
git clone https://github.com/sablier-labs/plugin-marketplace.git
cd plugin-marketplace
just install-deps
```

### Available Commands

Run `just --list` to show all available commands.

### Development Workflow

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `mdformat --check .` to verify formatting
5. Submit a pull request
