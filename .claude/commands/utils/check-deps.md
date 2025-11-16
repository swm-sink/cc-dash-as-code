---
name: utils.check-deps
description: Validate dependencies, check for updates, and scan for security vulnerabilities
parameters: []
tools:
  - Bash
---

# /utils.check-deps

Validate dependencies, check for updates, and scan for security vulnerabilities.

## Usage

```
/utils.check-deps
```

## Purpose

Comprehensive dependency management:
- Validate requirements.txt format
- Check for outdated packages
- Scan for security vulnerabilities
- Provide update recommendations

## Behavior

1. **Activate venv**: Source venv/bin/activate
2. **Validate requirements.txt**: Check format and syntax
3. **Check for updates**: `pip list --outdated`
4. **Security scan**: `pip-audit` or `safety check` (if available)
5. **Generate report**: Show outdated packages and vulnerabilities

## Examples

### All Dependencies Current

```
/utils.check-deps
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Dependency Check
════════════════════════════════════════════════════════════════════════════

✅ requirements.txt: Valid format
✅ Outdated packages: None
✅ Security vulnerabilities: None

All dependencies are up to date and secure!

════════════════════════════════════════════════════════════════════════════
```

### Updates and Vulnerabilities Found

```
/utils.check-deps
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Dependency Check
════════════════════════════════════════════════════════════════════════════

✅ requirements.txt: Valid format (45 packages)

⚠️  Outdated Packages (5):

  Package       Current    Latest    Type
  ──────────────────────────────────────────
  dash          2.14.0     2.15.1    minor
  plotly        5.18.0     5.19.0    minor
  pandas        2.1.0      2.2.0     minor
  pytest        7.4.0      8.0.1     major
  black         23.10.0    24.1.0    major

❌ Security Vulnerabilities (2):

  HIGH: CVE-2024-12345 in requests==2.28.0
    Fixed in: 2.31.0
    Summary: Server-side request forgery vulnerability
    
  MEDIUM: CVE-2024-67890 in urllib3==1.26.0
    Fixed in: 1.26.18
    Summary: Certificate validation bypass

Recommendations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Update security-critical packages immediately:
   pip install requests==2.31.0 urllib3==1.26.18

2. Consider updating to latest versions:
   pip install --upgrade dash plotly pandas

3. Test after updates:
   /utils.test

4. Update requirements.txt:
   pip freeze > requirements.txt

════════════════════════════════════════════════════════════════════════════
```

## See Also

- `requirements.txt` - Dependency specifications
