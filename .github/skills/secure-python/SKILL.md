---
name: secure-python
description: Implements and validates small security-conscious Python changes.
---

# Secure Python Skill

Use this skill when a requested task creates or modifies Python code.

## Procedure

1. Read AGENTS.md.
2. Identify the smallest set of files required.
3. Read relevant source code, tests, and project configuration.
4. Check how external input is accepted and validated.
5. Implement the smallest safe change.
6. Add a focused test when behavior changes.
7. Run syntax validation:

   python -m compileall .

8. Run targeted tests when pytest is available:

   pytest -q

9. Review the patch for:
   - command injection;
   - code injection;
   - unsafe file operations;
   - secrets;
   - missing input validation.

10. Summarize:
    - files changed;
    - validation commands;
    - validation results;
    - security-review result;
    - remaining risks.

## Restrictions

- Do not modify unrelated files.
- Do not disable tests or security checks.
- Do not add a dependency unless the task requires it.
- Do not approve or merge a pull request.
