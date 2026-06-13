import re
import os

files = [
    'coolcare_qatar_premium_hvac_services/code.html',
    'our_services_hvac_solutions_in_qatar/code.html',
    'faq_help_center_professional_hvac_support/code.html',
    'contact_us_coolcare_qatar_support/code.html'
]

logo_old_regex = r'<a class="flex items-center gap-3 group transition-transform duration-300 hover:scale-102" href="\.\./coolcare_qatar_premium_hvac_services/code\.html">.*?</a>'

logo_new = """<a class="flex items-center gap-2 md:gap-3 group transition-transform duration-300 hover:scale-102" href="../coolcare_qatar_premium_hvac_services/code.html">
                <div id="nav-logo-container" class="flex items-center justify-center p-1 md:p-0 bg-white/95 backdrop-blur-md rounded-[14px] md:bg-transparent md:backdrop-blur-none shadow-sm md:shadow-none border border-slate-100/50 md:border-transparent transition-all duration-300">
                    <img src="../assets/logo.png" class="h-9 sm:h-10 md:h-[72px] w-auto object-contain transition-all duration-300" alt="CoolCare Qatar Logo" id="nav-logo"/>
                </div>
                <span class="font-montserrat font-bold text-[17px] sm:text-lg md:text-xl text-primary tracking-tight transition-colors duration-300 group-hover:text-secondary">CoolCare Qatar</span>
            </a>"""

js_old_regex = r'window\.addEventListener\(\'scroll\', \(\) => \{\s*if \(window\.scrollY > 50\) \{.*?\}\s*\}\);'

js_new = """window.addEventListener('scroll', () => {
            const navLogoContainer = document.getElementById('nav-logo-container');
            if (window.scrollY > 50) {
                navbar.classList.remove('h-20');
                navbar.classList.add('h-16');
                navLogo.className = 'h-8 md:h-12 w-auto object-contain transition-all duration-300';
                if (navLogoContainer) {
                    navLogoContainer.classList.remove('p-1');
                    navLogoContainer.classList.add('p-0.5');
                }
            } else {
                navbar.classList.remove('h-16');
                navbar.classList.add('h-20');
                navLogo.className = 'h-9 sm:h-10 md:h-[72px] w-auto object-contain transition-all duration-300';
                if (navLogoContainer) {
                    navLogoContainer.classList.remove('p-0.5');
                    navLogoContainer.classList.add('p-1');
                }
            }
        });"""

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Replace logo
    content = re.sub(logo_old_regex, logo_new, content, flags=re.DOTALL)
    
    # Replace JS
    content = re.sub(js_old_regex, js_new, content, flags=re.DOTALL)
    
    with open(f, 'w') as file:
        file.write(content)

print("Logo and JS scroll logic fixed.")
