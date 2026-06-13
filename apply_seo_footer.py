import re

files = {
    'coolcare_qatar_premium_hvac_services/code.html': 'https://www.coolcareqatar.com/coolcare_qatar_premium_hvac_services/code.html',
    'our_services_hvac_solutions_in_qatar/code.html': 'https://www.coolcareqatar.com/our_services_hvac_solutions_in_qatar/code.html',
    'faq_help_center_professional_hvac_support/code.html': 'https://www.coolcareqatar.com/faq_help_center_professional_hvac_support/code.html',
    'contact_us_coolcare_qatar_support/code.html': 'https://www.coolcareqatar.com/contact_us_coolcare_qatar_support/code.html'
}

FOOTER_TEMPLATE = """<footer class="bg-tertiary text-on-tertiary w-full pt-16 pb-6 border-t border-outline/10 font-inter">
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-12 gap-gutter px-margin-mobile md:px-margin-desktop max-w-container-max mx-auto mb-16 text-left">
            
            <!-- Column 1: Info and Brand description -->
            <div class="lg:col-span-3 space-y-6">
                <a class="flex items-center gap-3" href="../coolcare_qatar_premium_hvac_services/code.html">
                    <img src="../assets/logo.png" class="h-10 w-auto object-contain brightness-0 invert" alt="CoolCare logo footer" loading="lazy" decoding="async"/>
                    <span class="font-montserrat font-bold text-lg text-secondary-fixed">CoolCare Qatar</span>
                </a>
                <p class="text-tertiary-fixed-dim text-sm leading-relaxed max-w-xs">
                    Premium HVAC Solutions engineered for the extreme Gulf climate. Reliable, refreshing, and technologically advanced.
                </p>
            </div>
            
            <!-- Column 2: Services links -->
            <div class="lg:col-span-2">
                <h4 class="font-montserrat text-sm font-bold text-white tracking-wider uppercase mb-5">SERVICES</h4>
                <ul class="space-y-3 text-sm">
                    <li><a class="text-tertiary-fixed-dim hover:text-secondary-fixed transition-colors hover:underline" href="../our_services_hvac_solutions_in_qatar/code.html">AC Repair & Fixes</a></li>
                    <li><a class="text-tertiary-fixed-dim hover:text-secondary-fixed transition-colors hover:underline" href="../our_services_hvac_solutions_in_qatar/code.html">Preventative AMC</a></li>
                    <li><a class="text-tertiary-fixed-dim hover:text-secondary-fixed transition-colors hover:underline" href="../our_services_hvac_solutions_in_qatar/code.html">AC Installation</a></li>
                    <li><a class="text-tertiary-fixed-dim hover:text-secondary-fixed transition-colors hover:underline" href="../our_services_hvac_solutions_in_qatar/code.html">Duct Sanitization</a></li>
                </ul>
            </div>
            
            <!-- Column 3: Service Locations -->
            <div class="lg:col-span-2">
                <h4 class="font-montserrat text-sm font-bold text-white tracking-wider uppercase mb-5">LOCATIONS</h4>
                <ul class="space-y-3 text-sm">
                    <li class="text-tertiary-fixed-dim flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-secondary"></span>Doha</li>
                    <li class="text-tertiary-fixed-dim flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-secondary"></span>Al Wakrah</li>
                    <li class="text-tertiary-fixed-dim flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-secondary"></span>Lusail</li>
                    <li class="text-tertiary-fixed-dim flex items-center gap-2"><span class="w-1.5 h-1.5 rounded-full bg-secondary"></span>The Pearl</li>
                </ul>
            </div>
            
            <!-- Column 4: Location Address -->
            <div class="lg:col-span-3">
                <h4 class="font-montserrat text-sm font-bold text-white tracking-wider uppercase mb-5">OFFICE LOCATION</h4>
                <div class="text-tertiary-fixed-dim flex items-start gap-2 text-sm leading-relaxed">
                    <span class="material-symbols-outlined text-sm text-secondary mt-0.5">location_on</span>
                    <span>Al Rawabi Street, Muntazah,<br/>Doha, State of Qatar</span>
                </div>
            </div>

            <!-- Column 5: Contact Info -->
            <div class="lg:col-span-2">
                <h4 class="font-montserrat text-sm font-bold text-white tracking-wider uppercase mb-5">CONTACT</h4>
                <ul class="space-y-3 text-sm">
                    <li>
                        <a class="text-tertiary-fixed-dim hover:text-secondary-fixed transition-colors flex items-center gap-2" href="https://wa.me/97431029734" target="_blank" rel="noopener" aria-label="WhatsApp Us">
                            <span class="material-symbols-outlined text-sm text-secondary">chat</span>
                            WhatsApp Us
                        </a>
                    </li>
                    <li>
                        <div class="text-tertiary-fixed-dim flex items-start gap-2">
                            <span class="material-symbols-outlined text-sm text-secondary mt-0.5">phone</span>
                            <span class="leading-normal">
                                24/7 Hotline:<br/>
                                <a href="tel:31029734" class="hover:text-secondary-fixed hover:underline" aria-label="Call 3102-9734">3102-9734</a><br/>
                                <a href="tel:70410771" class="hover:text-secondary-fixed hover:underline" aria-label="Call 7041-0771">7041-0771</a>
                            </span>
                        </div>
                    </li>
                </ul>
            </div>
            
        </div>
        
        <div class="border-t border-outline/10 pt-6 px-margin-mobile text-center">
            <p class="text-tertiary-fixed-dim/40 text-xs">
                © 2026 CoolCare Qatar. All rights reserved. Premium HVAC Solutions. Engineered for Excellence in the Gulf.
            </p>
        </div>
    </footer>

    <!-- Floating WhatsApp Widget -->
    <a class="fixed bottom-6 right-6 z-50 bg-[#25D366] text-white p-4 rounded-full shadow-2xl hover:bg-[#20ba56] transition-all hover:scale-105 active:scale-95 group flex items-center justify-center pulse-ring" href="https://wa.me/97431029734" target="_blank" rel="noopener" aria-label="Chat with CoolCare Qatar on WhatsApp">
        <svg class="w-6 h-6 fill-current" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
            <path d="M.057 24l1.687-6.163c-1.041-1.804-1.588-3.849-1.587-5.946C.06 5.348 5.397.01 12.008.01c3.202.001 6.212 1.246 8.477 3.514 2.266 2.268 3.507 5.28 3.505 8.484-.004 6.657-5.34 11.997-11.953 11.997-2.005-.001-3.973-.502-5.724-1.458L0 24zm5.835-3.823c1.657.983 3.279 1.503 4.966 1.505 5.485.002 9.944-4.43 9.947-9.87.001-2.636-1.02-5.115-2.876-6.974S13.626 2.012 10.99 2.01c-5.49 0-9.948 4.433-9.95 9.87-.001 1.794.492 3.505 1.428 5.093L1.458 22.3l5.414-1.42.02-.003zM16.59 13.9c-.276-.14-1.636-.81-1.89-.9-.253-.09-.438-.14-.623.14-.184.28-.714.9-.874 1.08-.16.18-.32.2-.596.06-2.65-1.32-3.8-2.2-5.275-4.73-.255-.436.255-.404.73-.1.115-.07.23-.17.3-.25a.578.578 0 0 0 .1-.37c-.05-.28-.276-1.13-.378-1.37-.1-.24-.2-.2-.275-.2h-.26c-.1 0-.263.04-.4.19-.138.15-.53.52-.53 1.27s.54 1.48.617 1.59c.077.11 1.06 1.62 2.57 2.27.36.15.64.25.86.32.36.11.69.1 1.02.05.37-.05 1.636-.67 1.868-1.31.23-.64.23-1.19.16-1.31-.07-.12-.276-.19-.553-.33z"/>
        </svg>
        <span class="max-w-0 overflow-hidden group-hover:max-w-xs transition-all duration-300 ease-out font-montserrat text-xs font-bold tracking-wider group-hover:ml-2 whitespace-nowrap">WHATSAPP NOW</span>
    </a>"""

for file_path, full_url in files.items():
    with open(file_path, 'r') as f:
        content = f.read()

    # Extract title and description
    title_match = re.search(r'<title>(.*?)</title>', content)
    desc_match = re.search(r'<meta name="description" content="(.*?)"/>', content)
    
    title = title_match.group(1) if title_match else "CoolCare Qatar - Premium Air Conditioning & HVAC Solutions"
    desc = desc_match.group(1) if desc_match else "Get premium climate control solutions in Qatar."

    # Build OG meta tags
    meta_tags = f"""<meta name="theme-color" content="#003a85">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{full_url}">
    <meta property="og:image" content="https://www.coolcareqatar.com/assets/logo.png">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="https://www.coolcareqatar.com/assets/logo.png">"""

    # Inject meta tags right before <script src="https://cdn.tailwindcss.com...
    if '<meta name="theme-color"' not in content:
        content = re.sub(r'(<script src="https://cdn\.tailwindcss\.com\?plugins=forms,container-queries"></script>)', 
                         lambda m: meta_tags + '\n    ' + m.group(1), 
                         content)

    # Replace footer and everything down to <script> with FOOTER_TEMPLATE + <script>
    # Be careful not to replace the main script, just replace footer and floating whatsapp widget.
    content = re.sub(r'<footer class="bg-tertiary.*?</a>\s*(<!-- Custom Script Logic -->)', FOOTER_TEMPLATE + '\n\n    \\1', content, flags=re.DOTALL)

    # Add loading="lazy" to watermark image
    content = re.sub(r'(<img src="\.\./assets/logo\.png"[^>]*?)alt="CoolCare logo background watermark"(.*?>)', 
                     r'\1alt="CoolCare logo background watermark" loading="lazy" decoding="async"\2', 
                     content)

    with open(file_path, 'w') as f:
        f.write(content)

print("SEO tags, footer sync, and accessibility optimizations applied successfully.")
