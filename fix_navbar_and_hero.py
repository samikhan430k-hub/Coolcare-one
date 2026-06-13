import re
import os

files = [
    'coolcare_qatar_premium_hvac_services/code.html',
    'our_services_hvac_solutions_in_qatar/code.html',
    'faq_help_center_professional_hvac_support/code.html',
    'contact_us_coolcare_qatar_support/code.html'
]

NAV_TEMPLATE = """<nav class="fixed top-0 w-full z-50 glass-panel border-b border-outline-variant/30 shadow-sm transition-all duration-300 h-20 flex items-center" id="navbar">
        <div class="flex justify-between items-center px-6 md:px-[28px] lg:px-8 w-full">
            <!-- Brand Logo -->
            <a class="flex items-center gap-3 group transition-transform duration-300 hover:scale-102" href="../coolcare_qatar_premium_hvac_services/code.html">
                <img src="../assets/logo.png" class="h-[60px] md:h-[72px] w-auto object-contain transition-all duration-300" alt="CoolCare Qatar Logo" id="nav-logo"/>
                <span class="font-montserrat font-bold text-lg md:text-xl text-primary tracking-tight transition-colors duration-300 group-hover:text-secondary">CoolCare Qatar</span>
            </a>
            
            <!-- Desktop Navigation Links -->
            <div class="hidden lg:flex items-center space-x-1">
                <a class="font-montserrat text-sm font-semibold {HOME_CLASS} px-4 py-2 rounded-full transition-all duration-300" href="../coolcare_qatar_premium_hvac_services/code.html">Home</a>
                <a class="font-montserrat text-sm font-semibold {SERVICES_CLASS} px-4 py-2 rounded-full transition-all duration-300" href="../our_services_hvac_solutions_in_qatar/code.html">Services</a>
                <a class="font-montserrat text-sm font-semibold text-on-surface-variant hover:text-white hover:bg-secondary px-4 py-2 rounded-full transition-all duration-300" href="../coolcare_qatar_premium_hvac_services/code.html#about">About</a>
                <a class="font-montserrat text-sm font-semibold {FAQ_CLASS} px-4 py-2 rounded-full transition-all duration-300" href="../faq_help_center_professional_hvac_support/code.html">FAQ</a>
                <a class="font-montserrat text-sm font-semibold {CONTACT_CLASS} px-4 py-2 rounded-full transition-all duration-300" href="../contact_us_coolcare_qatar_support/code.html">Contact</a>
            </div>
            
            <!-- Desktop CTA Action Buttons -->
            <div class="hidden lg:flex items-center space-x-3">
                <a class="font-montserrat text-xs font-bold tracking-wider text-primary border-2 border-primary hover:bg-secondary hover:text-white hover:border-secondary hover:scale-[1.03] hover:shadow-md px-5 py-2.5 rounded-full transition-all duration-300 active:scale-95" href="../coolcare_qatar_premium_hvac_services/code.html#quote">
                    BOOK NOW
                </a>
                <a class="font-montserrat text-xs font-bold tracking-wider bg-secondary text-on-secondary hover:bg-secondary/95 hover:shadow-lg hover:shadow-secondary/20 hover:scale-[1.03] px-5 py-2.5 rounded-full transition-all duration-300 active:scale-95 flex items-center gap-2 relative" href="tel:31029734">
                    <span class="absolute w-2 h-2 bg-white rounded-full animate-ping left-3 top-3"></span>
                    <span class="material-symbols-outlined text-sm font-bold" style="font-variation-settings: 'FILL' 1;">emergency</span>
                    EMERGENCY SERVICE
                </a>
            </div>
            
            <!-- Mobile Menu Toggle -->
            <button class="lg:hidden text-primary p-2 focus:outline-none transition-transform active:scale-90" id="menu-toggle" aria-label="Toggle Navigation Menu">
                <div class="w-6 h-5 flex flex-col justify-between items-center relative">
                    <span class="w-full h-0.5 bg-current rounded transition-all duration-300 origin-left" id="hamburger-bar-1"></span>
                    <span class="w-full h-0.5 bg-current rounded transition-all duration-300" id="hamburger-bar-2"></span>
                    <span class="w-full h-0.5 bg-current rounded transition-all duration-300 origin-left" id="hamburger-bar-3"></span>
                </div>
            </button>
        </div>
    </nav>"""

MOBILE_MENU_TEMPLATE = """<div class="fixed inset-0 z-40 bg-slate-900/40 backdrop-blur-md hidden transition-opacity duration-300 opacity-0" id="mobile-menu-overlay"></div>
    <div class="fixed top-20 left-0 right-0 z-40 bg-white border-b border-outline-variant/30 shadow-lg hidden transform translate-y-[-100%] transition-transform duration-300" id="mobile-menu-drawer">
        <div class="px-6 py-8 flex flex-col space-y-6">
            <a class="font-montserrat text-base font-bold {HOME_MOB_CLASS} py-2 px-3 rounded-lg border-b border-gray-100 transition-all duration-300" href="../coolcare_qatar_premium_hvac_services/code.html">Home</a>
            <a class="font-montserrat text-base font-bold {SERVICES_MOB_CLASS} py-2 px-3 rounded-lg border-b border-gray-100 transition-all duration-300" href="../our_services_hvac_solutions_in_qatar/code.html">Services</a>
            <a class="font-montserrat text-base font-bold text-on-surface-variant hover:text-white hover:bg-secondary py-2 px-3 rounded-lg border-b border-gray-100 transition-all duration-300" href="../coolcare_qatar_premium_hvac_services/code.html#about">About</a>
            <a class="font-montserrat text-base font-bold {FAQ_MOB_CLASS} py-2 px-3 rounded-lg border-b border-gray-100 transition-all duration-300" href="../faq_help_center_professional_hvac_support/code.html">FAQ</a>
            <a class="font-montserrat text-base font-bold {CONTACT_MOB_CLASS} py-2 px-3 rounded-lg border-b border-gray-100 transition-all duration-300" href="../contact_us_coolcare_qatar_support/code.html">Contact</a>
            
            <div class="flex flex-col sm:flex-row gap-4 pt-4">
                <a class="text-center font-montserrat text-sm font-bold tracking-wider text-primary border-2 border-primary hover:bg-secondary hover:text-white hover:border-secondary py-3 px-6 rounded-full transition-all duration-300 active:scale-95 hover:scale-[1.03]" href="../coolcare_qatar_premium_hvac_services/code.html#quote">
                    BOOK NOW
                </a>
                <a class="text-center font-montserrat text-sm font-bold tracking-wider bg-secondary text-on-secondary hover:bg-secondary/95 py-3 px-6 rounded-full transition-all duration-300 active:scale-95 flex items-center justify-center gap-2 hover:scale-[1.03]" href="tel:31029734">
                    <span class="material-symbols-outlined text-sm font-bold">emergency</span>
                    EMERGENCY SERVICE
                </a>
            </div>
        </div>
    </div>"""

ACTIVE_CLASS = "text-white bg-secondary"
INACTIVE_CLASS = "text-on-surface-variant hover:text-white hover:bg-secondary"

JS_REGEX = r"(window\.addEventListener\('scroll', \(\) => \{\s*if \(window\.scrollY > 50\) \{\s*navbar\.classList\.remove\('h-20'\);\s*navbar\.classList\.add\('h-16'\);\s*navLogo\.classList\.remove\([^)]+\);\s*navLogo\.classList\.add\([^)]+\);\s*\} else \{\s*navbar\.classList\.remove\('h-16'\);\s*navbar\.classList\.add\('h-20'\);\s*navLogo\.classList\.remove\([^)]+\);\s*navLogo\.classList\.add\([^)]+\);\s*\}\s*\}\);)"
JS_REPLACEMENT = """window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.remove('h-20');
                navbar.classList.add('h-16');
                navLogo.classList.remove('h-[60px]', 'md:h-[72px]');
                navLogo.classList.add('h-10', 'md:h-12');
            } else {
                navbar.classList.remove('h-16');
                navbar.classList.add('h-20');
                navLogo.classList.remove('h-10', 'md:h-12');
                navLogo.classList.add('h-[60px]', 'md:h-[72px]');
            }
        });"""


for f in files:
    with open(f, 'r') as file:
        content = file.read()
        
    page_id = f.split('/')[0]
    is_home = page_id == 'coolcare_qatar_premium_hvac_services'
    is_services = page_id == 'our_services_hvac_solutions_in_qatar'
    is_faq = page_id == 'faq_help_center_professional_hvac_support'
    is_contact = page_id == 'contact_us_coolcare_qatar_support'
    
    nav_str = NAV_TEMPLATE.format(
        HOME_CLASS=ACTIVE_CLASS if is_home else INACTIVE_CLASS,
        SERVICES_CLASS=ACTIVE_CLASS if is_services else INACTIVE_CLASS,
        FAQ_CLASS=ACTIVE_CLASS if is_faq else INACTIVE_CLASS,
        CONTACT_CLASS=ACTIVE_CLASS if is_contact else INACTIVE_CLASS
    )
    
    mobile_str = MOBILE_MENU_TEMPLATE.format(
        HOME_MOB_CLASS=ACTIVE_CLASS if is_home else INACTIVE_CLASS,
        SERVICES_MOB_CLASS=ACTIVE_CLASS if is_services else INACTIVE_CLASS,
        FAQ_MOB_CLASS=ACTIVE_CLASS if is_faq else INACTIVE_CLASS,
        CONTACT_MOB_CLASS=ACTIVE_CLASS if is_contact else INACTIVE_CLASS
    )
    
    # Replace navbar
    content = re.sub(r'<nav.*?id="navbar".*?</nav>', nav_str, content, flags=re.DOTALL)
    
    # Replace mobile drawer
    content = re.sub(r'<div class="fixed inset-0[^>]*id="mobile-menu-overlay"></div>\s*<div[^>]*id="mobile-menu-drawer".*?</div>\s*</div>', mobile_str, content, flags=re.DOTALL)
    
    # Replace JS
    content = re.sub(JS_REGEX, JS_REPLACEMENT, content)
    
    with open(f, 'w') as file:
        file.write(content)

# Now fix the Hero Section on the Home Page
with open(files[0], 'r') as f:
    home_content = f.read()

hero_old = """<div class="flex items-center gap-4 mb-8 md:mb-12 select-none hero-animate-1">
                    <div class="relative flex items-center justify-center w-14 h-14 md:w-16 md:h-16">
                        <!-- Premium Glow Backdrop -->
                        <div class="absolute inset-0 bg-gradient-to-tr from-secondary/20 to-primary/40 rounded-xl blur-md animate-pulse"></div>
                        <img src="../assets/logo.png" class="w-full h-full object-contain relative z-10 transition-transform duration-500 hover:scale-105" alt="CoolCare logo centerpiece"/>
                    </div>
                    <div class="flex flex-col">
                        <div class="h-5 flex items-center">
                            <span class="font-montserrat text-xs md:text-sm font-extrabold tracking-[0.3em] text-secondary-fixed uppercase tagline-reveal">BEAT THE HEAT</span>
                        </div>
                        <span class="font-montserrat text-[10px] md:text-[11px] font-bold tracking-wider text-slate-300/90 uppercase mt-0.5">CoolCare Qatar HVAC</span>
                    </div>
                </div>"""

hero_new = """<div class="inline-flex items-center gap-5 bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-3 pr-6 mb-8 md:mb-12 select-none hero-animate-1 shadow-[0_8px_32px_rgba(0,0,0,0.12)] -ml-1">
                    <div class="relative flex items-center justify-center w-12 h-12 md:w-14 md:h-14 bg-white rounded-xl shadow-inner p-2">
                        <!-- Premium Glow Backdrop -->
                        <div class="absolute inset-0 bg-gradient-to-tr from-secondary/20 to-primary/40 rounded-xl blur-md animate-pulse"></div>
                        <img src="../assets/logo.png" class="w-full h-full object-contain relative z-10 transition-transform duration-500 hover:scale-105" alt="CoolCare logo centerpiece"/>
                    </div>
                    <div class="flex flex-col justify-center">
                        <div class="h-5 flex items-center">
                            <span class="font-montserrat text-xs md:text-sm font-extrabold tracking-[0.25em] text-secondary-fixed uppercase tagline-reveal leading-tight">BEAT THE HEAT</span>
                        </div>
                        <span class="font-montserrat text-[10px] md:text-[11px] font-bold tracking-widest text-slate-300 uppercase leading-tight mt-0.5">CoolCare Qatar HVAC</span>
                    </div>
                </div>"""

home_content = home_content.replace(hero_old, hero_new)

desc_old = """Reliable Installation, Maintenance, Repair, Gas Refilling & Commercial HVAC Solutions engineered for the challenging Gulf climate."""
desc_old_tag = f"""<p class="font-inter text-base md:text-lg text-slate-100 font-medium leading-[1.7] max-w-2xl hero-animate-4">
                            {desc_old}
                        </p>"""

desc_new_tag = f"""<p class="font-inter text-base md:text-lg text-white/95 font-semibold leading-[1.8] tracking-wide max-w-2xl hero-animate-4">
                            {desc_old}
                        </p>"""

home_content = home_content.replace(desc_old_tag, desc_new_tag)

with open(files[0], 'w') as f:
    f.write(home_content)

print("Updates applied successfully.")
