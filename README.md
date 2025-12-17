# HTTP Security Header Checker

A Python command-line tool that analyzes website security by checking for critical HTTP security headers and identifying potential vulnerabilities.

## 🔍 What It Does

This tool evaluates whether websites implement important security headers that protect against common web attacks. It checks for five critical headers and provides detailed feedback about their presence, purpose, and associated security risks.

## 🛡️ Security Headers Checked

| Header | Purpose |
|--------|---------|
| **Strict-Transport-Security (HSTS)** | Forces browsers to use HTTPS, preventing downgrade attacks |
| **X-Content-Type-Options** | Prevents browsers from MIME-sniffing, reducing XSS risk |
| **X-Frame-Options** | Blocks clickjacking by preventing the site from being embedded in frames |
| **Content-Security-Policy (CSP)** | Restricts resource loading to prevent XSS and injection attacks |
| **X-XSS-Protection** | Enables the browser's built-in XSS filter |

## 📋 Requirements

- Python 3.6 or higher
- `requests` library

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/SuperZhantor/security-header-checker.git
cd security-header-checker
```

2. Install the required library:
```bash
pip install requests
```

## 💻 Usage

Run the script:
```bash
python header_checker.py
```

When prompted, enter a website URL (e.g., `google.com` or `https://example.com`)

## 📊 Example Output

```
============================================================
HTTP Security Header Checker
============================================================

Enter a website URL: github.com

Checking security headers for: https://github.com
============================================================

✓ Strict-Transport-Security: PRESENT
  Value: max-age=31536000; includeSubdomains; preload
  Purpose: Forces HTTPS connections (prevents downgrade attacks)

✓ X-Content-Type-Options: PRESENT
  Value: nosniff
  Purpose: Prevents MIME-type sniffing attacks

✓ X-Frame-Options: PRESENT
  Value: deny
  Purpose: Prevents clickjacking attacks

✓ Content-Security-Policy: PRESENT
  Value: default-src 'none'; base-uri 'self'...
  Purpose: Prevents XSS and code injection attacks

✗ X-XSS-Protection: MISSING
  Purpose: Enables browser XSS filter
  Risk: Website may be vulnerable to related attacks

============================================================
Summary: 4/5 security headers present
⚠ Good, but some security headers are missing.
============================================================
```

## 🎯 Features

- ✅ Validates and formats URLs automatically
- ✅ Checks five critical security headers
- ✅ Displays header values and explanations
- ✅ Provides security risk assessment
- ✅ Comprehensive error handling
- ✅ Clear summary with visual indicators (✓/✗)

## 🔧 How It Works

1. **User Input**: Accepts a website URL from the user
2. **URL Validation**: Ensures the URL is properly formatted (adds https:// if needed)
3. **HTTP Request**: Sends a GET request to fetch HTTP headers
4. **Header Analysis**: Checks for presence of security headers
5. **Results Display**: Shows which headers are present/missing with explanations
6. **Summary**: Provides an overall security assessment

## 📚 Learning Outcomes

This project demonstrates:
- HTTP protocol fundamentals
- Web security best practices (OWASP guidelines)
- Python programming (requests library, error handling, dictionaries)
- Security header implementation and purposes
- Defensive security principles
- Vulnerability assessment concepts

## 🚧 Limitations

- Only checks for header presence, not validity of values
- Does not perform deep content security policy analysis
- Limited to publicly accessible websites
- Cannot detect all security misconfigurations
- Does not check redirect chains

## 🔮 Future Improvements

- [ ] Add GUI interface using Tkinter
- [ ] Generate PDF or HTML reports
- [ ] Check additional security headers (Referrer-Policy, Permissions-Policy)
- [ ] Validate header values (not just presence)
- [ ] Batch checking for multiple URLs from a file
- [ ] Security score calculation (A-F grade)
- [ ] Compare against industry security standards
- [ ] Integration with security APIs

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome!

## 📝 License

This project is open source and available for educational purposes.

## 👤 Author

**Zhantore Shaikenov**  
Cybersecurity Student | Western New England University  
[LinkedIn](https://linkedin.com/in/zhantore-shaikenov-7a32aa32b) | [GitHub](https://github.com/SuperZhantor)  
📧 zhantore321@gmail.com
---

*This tool is for educational purposes and security research only. Always obtain permission before testing websites you don't own.*
