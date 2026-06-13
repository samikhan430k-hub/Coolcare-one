import re

files = [
    'coolcare_qatar_premium_hvac_services/code.html',
    'our_services_hvac_solutions_in_qatar/code.html',
    'faq_help_center_professional_hvac_support/code.html',
    'contact_us_coolcare_qatar_support/code.html'
]

with open(files[0], 'r') as f:
    content = f.read()

logo_match = re.search(r'<a class="flex items-center gap-3 group transition-transform duration-300 hover:scale-102" href="\.\./coolcare_qatar_premium_hvac_services/code\.html">.*?</a>', content, flags=re.DOTALL)
print("LOGO MATCH:", logo_match is not None)

js_match = re.search(r'window\.addEventListener\(\'scroll\', \(\) => \{(.*?)\}\);', content, flags=re.DOTALL)
print("JS MATCH:", js_match is not None)
