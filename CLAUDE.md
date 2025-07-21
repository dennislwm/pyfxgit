# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python package called `pyfxgit` that provides financial charting utilities, specifically for creating OHLC (Open, High, Low, Close) candlestick charts with technical indicators. The package is designed for financial data analysis and visualization.

## Build and Development Commands

### Package Building
```bash
# Build and install the package locally
pip install -e .

# Build distribution packages
python setup.py sdist bdist_wheel

# Install from PyPI
pip install pyfxgit
```

### Dependencies Management
The project uses Pipenv for dependency management:
```bash
# Install dependencies
pipenv install

# Activate virtual environment
pipenv shell
```

### Package Upload
```bash
# Upload to PyPI (requires credentials)
twine upload dist/*
```

## Architecture

### Core Structure
- **pyfxgit/ChartCls.py**: Main charting class that provides financial chart creation functionality
- **setup.py**: Package configuration with dependencies: matplotlib==3.2.2, mpl_finance, numpy==1.18.5, pandas==1.3.0
- **pyfxgit/__init__.py**: Empty package initializer

### ChartCls Architecture
The `ChartCls` class is the primary component with these key responsibilities:

1. **Chart Layout Management**: Automatically calculates main and sub-chart positioning based on the number of sub-charts (max 3)
2. **OHLC Visualization**: Creates candlestick charts using mpl_finance with configurable colors
3. **Technical Indicators**: Builds oscillator charts with upper/lower bounds
4. **Tagging System**: Implements bull/bear market tagging based on oscillator values
5. **Span Overlays**: Adds colored background spans to highlight market conditions

### Key Data Flow
1. Input: pandas DataFrame with columns ['Open', 'High', 'Low', 'Close', 'Dbs', 'DbsMa']
2. Chart creation with main OHLC display and sub-charts for indicators
3. Tag generation for market condition identification
4. Output: PNG chart files saved locally

### Dependencies and Versions
- Python 3.9 (specified in Pipfile)
- matplotlib==3.2.2 for plotting
- mpl_finance for OHLC charts
- numpy==1.18.5 for numerical operations
- pandas==1.3.0 for data handling

## Package Structure
```
pyfxgit/
├── ChartCls.py          # Main charting functionality
├── __init__.py          # Package initializer (empty)
├── setup.cfg            # Metadata configuration
└── licence.txt          # MIT license
```

The package follows a simple single-module structure focused on the ChartCls functionality.

## GitHub CLI Integration

The project supports GitHub CLI (`gh`) for repository management and package distribution:

### Common GitHub CLI Commands

```bash
# Repository management
gh repo view                    # View current repository details
gh repo clone <repo>           # Clone a repository
gh repo create <name>          # Create new repository
gh repo fork                   # Fork current repository

# Release management for package distribution
gh release create v0.0.3      # Create new release tag
gh release list                # List all releases
gh release view v0.0.2        # View specific release details
gh release upload v0.0.3 dist/* # Upload package files to release

# Pull request management
gh pr create                   # Create new pull request
gh pr list                     # List pull requests
gh pr view <number>           # View PR details
gh pr checkout <number>       # Checkout PR locally

# Issue management
gh issue create               # Create new issue
gh issue list                 # List issues
gh issue view <number>        # View issue details

# Authentication
gh auth login                 # Login to GitHub
gh auth status               # Check authentication status
```

### Package Distribution Workflow

**Creating releases for PyPI packages**:
```bash
# Tag new version and create GitHub release
gh release create v0.0.3 --title "Release v0.0.3" --notes "Update pandas to 1.3.0"

# Upload distribution files to release
gh release upload v0.0.3 dist/pyfxgit-0.0.3.tar.gz dist/pyfxgit-0.0.3-py3-none-any.whl

# View release details
gh release view v0.0.3
```

**Repository maintenance**:
```bash
# Check repository status and recent activity
gh repo view --web            # Open repository in browser
gh issue list --state=open    # Check open issues
gh pr list --state=open       # Check open pull requests

# Create issues for package improvements
gh issue create --title "Update matplotlib dependency" --body "Consider updating matplotlib from 3.2.2 to latest stable version"
```

### Development Integration

**Collaborative development**:
```bash
# Fork repository for contributions
gh repo fork dennislwm/pyfxgit

# Create feature branch and PR
git checkout -b feature/update-dependencies
# ... make changes ...
gh pr create --title "Update dependencies" --body "Updates matplotlib and numpy to latest versions"

# Review PRs
gh pr view 1 --comments       # View PR with comments
gh pr checkout 1              # Checkout PR for local testing
```