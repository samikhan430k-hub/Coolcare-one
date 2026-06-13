import re
import os

files = [
    'coolcare_qatar_premium_hvac_services/code.html',
    'our_services_hvac_solutions_in_qatar/code.html',
    'faq_help_center_professional_hvac_support/code.html',
    'contact_us_coolcare_qatar_support/code.html'
]

# 1. Update Navbar logo across all files
nav_logo_old = """<a class="flex items-center gap-3 group transition-transform duration-300 hover:scale-102" href="../coolcare_qatar_premium_hvac_services/code.html">
                <img src="../assets/logo.png" class="h-[60px] md:h-[72px] w-auto object-contain transition-all duration-300" alt="CoolCare Qatar Logo" id="nav-logo"/>
                <span class="font-montserrat font-bold text-lg md:text-xl text-primary tracking-tight transition-colors duration-300 group-hover:text-secondary">CoolCare Qatar</span>
            </a>"""

nav_logo_new = """<a class="flex items-center gap-3 group transition-transform duration-300 hover:scale-102" href="../coolcare_qatar_premium_hvac_services/code.html">
                <div class="flex items-center justify-center p-1.5 md:p-0 bg-white/95 backdrop-blur-md rounded-2xl md:bg-transparent md:backdrop-blur-none shadow-sm md:shadow-none border border-slate-100/50 md:border-transparent transition-all duration-300">
                    <img src="../assets/logo.png" class="h-[55px] sm:h-[60px] md:h-[72px] w-auto object-contain transition-all duration-300" alt="CoolCare Qatar Logo" id="nav-logo"/>
                </div>
                <span class="font-montserrat font-bold text-lg md:text-xl text-primary tracking-tight transition-colors duration-300 group-hover:text-secondary">CoolCare Qatar</span>
            </a>"""

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # We replace nav logo exactly
    content = content.replace(nav_logo_old, nav_logo_new)
    
    # Let's write it back
    with open(f, 'w') as file:
        file.write(content)


# 2. Update Hero only on home page
home_file = files[0]
with open(home_file, 'r') as f:
    home_content = f.read()

hero_old = """<div class="inline-flex items-center gap-5 bg-white/5 backdrop-blur-md border border-white/10 rounded-2xl p-3 pr-6 mb-8 md:mb-12 select-none hero-animate-1 shadow-[0_8px_32px_rgba(0,0,0,0.12)] -ml-1">
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

hero_new = """<div class="inline-flex items-center gap-5 bg-white/20 backdrop-blur-xl border border-white/30 rounded-2xl p-4 md:p-3 pr-8 md:pr-6 mb-8 md:mb-12 select-none hero-animate-1 shadow-[0_8px_32px_rgba(0,0,0,0.2)] md:shadow-[0_8px_32px_rgba(0,0,0,0.12)] -ml-1">
                    <div class="relative flex items-center justify-center w-14 h-14 md:w-14 md:h-14 bg-white rounded-xl shadow-md p-2">
                        <!-- Premium Glow Backdrop -->
                        <div class="absolute inset-0 bg-gradient-to-tr from-secondary/50 to-primary/50 rounded-xl blur-md animate-pulse"></div>
                        <img src="../assets/logo.png" class="w-full h-full object-contain relative z-10 transition-transform duration-500 hover:scale-105" alt="CoolCare logo centerpiece"/>
                    </div>
                    <div class="flex flex-col justify-center drop-shadow-md">
                        <div class="h-6 md:h-5 flex items-center">
                            <span class="font-montserrat text-[13px] md:text-sm font-extrabold tracking-[0.25em] text-white uppercase tagline-reveal leading-tight" style="text-shadow: 0 2px 4px rgba(0,0,0,0.6);">BEAT THE HEAT</span>
                        </div>
                        <span class="font-montserrat text-[11px] md:text-[11px] font-bold tracking-widest text-blue-50 uppercase leading-tight mt-1" style="text-shadow: 0 1px 3px rgba(0,0,0,0.6);">CoolCare Qatar HVAC</span>
                    </div>
                </div>"""

# Ensure text is legible for h1 and p
h1_old = """<h1 class="font-montserrat font-bold text-3xl sm:text-4xl md:text-5xl lg:text-6xl text-white leading-[1.1] tracking-tight hero-animate-3">"""
h1_new = """<h1 class="font-montserrat font-bold text-3xl sm:text-4xl md:text-5xl lg:text-6xl text-white leading-[1.1] tracking-tight hero-animate-3 drop-shadow-md" style="text-shadow: 0 2px 8px rgba(0,0,0,0.4);">"""

p_old = """<p class="font-inter text-base md:text-lg text-white/95 font-semibold leading-[1.8] tracking-wide max-w-2xl hero-animate-4">"""
p_new = """<p class="font-inter text-base md:text-lg text-white font-semibold leading-[1.8] tracking-wide max-w-2xl hero-animate-4 drop-shadow-md" style="text-shadow: 0 1px 4px rgba(0,0,0,0.6);">"""

home_content = home_content.replace(hero_old, hero_new)
home_content = home_content.replace(h1_old, h1_new)
home_content = home_content.replace(p_old, p_new)

with open(home_file, 'w') as f:
    f.write(home_content)

print("Mobile styling enhancements applied.")
