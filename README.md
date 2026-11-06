# Password strength CLI

A small, local password-strength checker using only the Python standard
library. It checks length, character variety, and a short built-in list of
common passwords. The checker is deliberately a heuristic, not a guarantee of
password security.

## Usage

Run the module and provide a password as an argument:

```bash
python -m password_strength "Correct-Horse-42!"
```

For better privacy, omit the argument and enter the password at a hidden
prompt:

```bash
python -m password_strength
```

Example output:

```text
Score: 5/5 (Strong)
Tips: Keep using unique passwords and a password manager.
```

The score considers:

- length (8 characters earns a point; 12 earns two),
- lowercase, uppercase, number, and symbol variety,
- whether the password appears in a small common-password list.

## Tests

Run the standard-library test suite from the project directory:

```bash
python -m unittest discover -s tests -v
```
