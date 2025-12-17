import requests
from urllib.parse import urlparse

def validate_url(url):
    """Validate and format the URL"""
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def check_security_headers(url):
    """Check for important security headers"""
    
    # Important security headers and their purposes
    security_headers = {
        'Strict-Transport-Security': 'Forces HTTPS connections (prevents downgrade attacks)',
        'X-Content-Type-Options': 'Prevents MIME-type sniffing attacks',
        'X-Frame-Options': 'Prevents clickjacking attacks',
        'Content-Security-Policy': 'Prevents XSS and code injection attacks',
        'X-XSS-Protection': 'Enables browser XSS filter'
    }
    
    try:
        print(f"\nChecking security headers for: {url}")
        print("=" * 60)
        
        # Fetch headers with timeout
        response = requests.get(url, timeout=5, allow_redirects=True)
        headers = response.headers
        
        present_count = 0
        missing_count = 0
        
        # Check each security header
        for header, description in security_headers.items():
            if header in headers:
                print(f"\n✓ {header}: PRESENT")
                print(f"  Value: {headers[header][:50]}...")  
                print(f"  Purpose: {description}")
                present_count += 1
            else:
                print(f"\n✗ {header}: MISSING")
                print(f"  Purpose: {description}")
                print(f"  Risk: Website may be vulnerable to related attacks")
                missing_count += 1
        
        # Summary
        print("\n" + "=" * 60)
        print(f"Summary: {present_count}/{len(security_headers)} security headers present")
        
        if missing_count == 0:
            print("✓ Excellent! All critical security headers are configured.")
        elif missing_count <= 2:
            print("⚠ Good, but some security headers are missing.")
        else:
            print("✗ Warning: Multiple security headers are missing.")
        
    except requests.exceptions.Timeout:
        print("✗ Error: Request timed out. The website took too long to respond.")
    except requests.exceptions.ConnectionError:
        print("✗ Error: Could not connect to the website. Check the URL and your internet connection.")
    except requests.exceptions.RequestException as e:
        print(f"✗ Error: {e}")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def main():
    """Main function"""
    print("=" * 60)
    print("HTTP Security Header Checker")
    print("=" * 60)
    
    url = input("\nEnter a website URL (e.g., google.com or https://google.com): ").strip()
    
    # Validate URL
    if not url:
        print("✗ Error: URL cannot be empty")
        return
    
    # Add https:// if missing
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    if not validate_url(url):
        print("✗ Error: Invalid URL format")
        return
    
    check_security_headers(url)
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()