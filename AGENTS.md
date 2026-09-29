# Repository Agent Instructions

## Scope

- Make only the changes required by the requested task.
- Preserve existing interfaces unless the task explicitly requires a change.
- Do not modify GitHub workflow, security-policy, or dependency files unless requested.
- Never add credentials, tokens, passwords, or secrets.
- Prefer small and reviewable changes.

## Validation

For Python changes:

1. Run Python syntax validation.
2. Run relevant unit tests.
3. Run project linting when available.
4. Report all commands executed and their outcomes.

## Security

- Validate external input.
- Avoid command injection and unsafe code execution.
- Do not disable CodeQL, branch protection, rulesets, or security scanning.
- Do not suppress a security finding without an explanation.
- Never approve or merge the generated pull request.

## Pull Request Requirements

The pull request must include:

- requested task;
- implementation summary;
- files changed;
- tests and validation performed;
- security-review summary;
- known limitations.
