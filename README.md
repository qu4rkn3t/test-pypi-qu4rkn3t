# Example Package

A simple example Python package for demonstrating PyPI publishing with GitHub Actions.

## Installation

```bash
pip install example-package
```

## Usage

```python
from example_package import greet

# Basic usage
print(greet())  # Output: Hello, World!

# Custom greeting
print(greet("Python"))  # Output: Hello, Python!
```

## Development

### Local Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/test-pypi-qu4rkn3t.git
cd test-pypi-qu4rkn3t

# Install in editable mode
pip install -e .
```

### Building the Package

```bash
pip install build
python -m build
```

## Publishing to PyPI

This package uses GitHub Actions to automatically publish to PyPI when a new release is created.

### Setup Instructions

1. Create a PyPI account at https://pypi.org
2. Generate an API token at https://pypi.org/manage/account/token/
3. Add the token as a GitHub secret named `PYPI_API_TOKEN`:
   - Go to your repository Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `PYPI_API_TOKEN`
   - Value: Your PyPI API token (including the `pypi-` prefix)

### Publishing a New Version

1. Update the version in `pyproject.toml` and `src/example_package/__init__.py`
2. Commit and push your changes
3. Create a new release on GitHub:
   - Go to Releases → Draft a new release
   - Create a new tag (e.g., `v0.1.0`)
   - Add release notes
   - Publish the release
4. GitHub Actions will automatically build and publish to PyPI

## License

MIT