# Day 9 — Decorators & Context Managers

## What I learned
- How decorators work mechanically
- Built a timer decorator with @wraps
- Built a database context manager two ways

## Files
- `decorators.py` — timer decorator with @wraps
- `context_manager.py` — DatabaseConnection class + contextlib version

## Key concepts
- `@decorator` is shorthand for `func = decorator(func)`
- `@wraps` preserves original function metadata
- Context managers guarantee open/close even when errors occur

## LeetCode
- Problem: Best Time to Buy and Sell Stock #121