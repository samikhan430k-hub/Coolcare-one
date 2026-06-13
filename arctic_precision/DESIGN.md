---
name: Arctic Precision
colors:
  surface: '#f9f9fc'
  surface-dim: '#dadadc'
  surface-bright: '#f9f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f6'
  surface-container: '#eeeef0'
  surface-container-high: '#e8e8ea'
  surface-container-highest: '#e2e2e5'
  on-surface: '#1a1c1e'
  on-surface-variant: '#434751'
  inverse-surface: '#2f3133'
  inverse-on-surface: '#f0f0f3'
  outline: '#737783'
  outline-variant: '#c3c6d3'
  surface-tint: '#2e5cad'
  primary: '#003a85'
  on-primary: '#ffffff'
  primary-container: '#2152a3'
  on-primary-container: '#b3c9ff'
  inverse-primary: '#aec6ff'
  secondary: '#256d01'
  on-secondary: '#ffffff'
  secondary-container: '#a7f782'
  on-secondary-container: '#2b7309'
  tertiary: '#363f47'
  on-tertiary: '#ffffff'
  tertiary-container: '#4d565f'
  on-tertiary-container: '#c2cbd6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#aec6ff'
  on-primary-fixed: '#001a42'
  on-primary-fixed-variant: '#074394'
  secondary-fixed: '#a7f782'
  secondary-fixed-dim: '#8cda69'
  on-secondary-fixed: '#062100'
  on-secondary-fixed-variant: '#195200'
  tertiary-fixed: '#dae3ee'
  tertiary-fixed-dim: '#bec7d2'
  on-tertiary-fixed: '#141c24'
  on-tertiary-fixed-variant: '#3f4850'
  background: '#f9f9fc'
  on-background: '#1a1c1e'
  surface-variant: '#e2e2e5'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Montserrat
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  section-padding: 80px
---

## Brand & Style

This design system is engineered for a premium HVAC service provider in the Gulf region, where reliability and climate control are essential luxuries. The brand personality is **authoritative, refreshing, and technologically advanced**. It balances the "cool" technical side of air conditioning with the "green" aspect of sustainability and fresh air.

The visual style is **Corporate Modern with Glassmorphic accents**. It utilizes high-end "Gulf Corporate" aesthetics: expansive whitespace to simulate airiness, precise geometric alignment to signal engineering expertise, and subtle translucent layers that mimic the look of frosted glass or clean ice. The overall emotional response should be one of immediate relief and absolute trust in professional competence.

## Colors

The palette is derived directly from the cooling and growth metaphors of the brand.

- **Primary (Deep Professional Blue):** Used for headers, primary buttons, and navigational anchors to establish authority.
- **Secondary (Vibrant Growth Green):** Reserved for success states, sustainability callouts, and "Book Now" actions to drive conversion.
- **Tertiary (Cooling Ice Blue):** Used for large background sections and subtle UI containers to reduce visual heat.
- **Surface & Background:** A dominant use of pure white (#FFFFFF) ensures a "sterile" and clean professional environment.
- **Status Colors:** Use a refined palette for functional feedback: Error (Deep Red), Warning (Amber), and Info (the Primary Blue).

## Typography

The typography strategy pairs the geometric confidence of **Montserrat** for headings with the systematic clarity of **Inter** for functional text. 

Headlines use tight letter-spacing and bold weights to convey strength and "beat the heat" urgency. Body text is set with generous line-height to maintain the feeling of whitespace and breathability. For technical specs and labels, uppercase Inter with increased tracking is used to provide a professional, architectural feel.

## Layout & Spacing

The layout follows a **Fluid Grid** system within a max-width container to maintain a premium, structured appearance on large displays. 

- **Grid:** A 12-column grid for desktop, 8-column for tablet, and 4-column for mobile.
- **Rhythm:** An 8px linear scale governs all padding and margins. 
- **Sectioning:** Large vertical gaps (80px+) are used between homepage sections to reinforce the premium, airy aesthetic. 
- **Service Cards:** Use a 3-column layout on desktop, reflowing to a single column on mobile with horizontal scrolling for "Quick Actions."

## Elevation & Depth

This design system uses a combination of **Glassmorphism** and **Ambient Shadows** to create a sense of sophisticated layering.

1.  **Level 0 (Base):** Pure white or tertiary light blue background.
2.  **Level 1 (Cards):** Low-contrast outlines (1px solid #E2E8F0) with a very soft, high-diffusion shadow (0px 4px 20px rgba(33, 82, 163, 0.05)).
3.  **Level 2 (Navigation/Overlays):** Semi-transparent white (rgba(255, 255, 255, 0.8)) with a 12px backdrop-blur. This mimics frosted glass and is used for sticky headers and modal backgrounds.
4.  **Interaction:** Upon hover, cards should lift slightly (y-offset -4px) and shadow intensity should increase to signify interactivity.

## Shapes

The shape language is **Rounded**, striking a balance between technical precision and approachable service. 

- **Standard Elements:** Buttons, inputs, and cards use a 0.5rem (8px) radius.
- **Featured Containers:** Large service banners or image containers use a 1rem (16px) radius for a modern, high-end feel.
- **Iconography:** Use thick-stroke (2pt) icons with rounded terminals to match the font weight and corner radii of the UI elements.

## Components

### Buttons
- **Primary:** Deep blue fill, white text, Montserrat Bold. High-contrast and substantial.
- **Secondary/CTA:** Vibrant green fill. Reserved specifically for "Emergency Repair" or "Book Service."
- **Ghost:** Transparent background with Primary Blue border. Used for "Learn More" or secondary navigation.

### Service Cards
Cards are the cornerstone of this design system. They feature a white background, the Level 1 elevation shadow, and a subtle top-border in Secondary Green for "Available" services. Typography inside cards is highly structured, using Label-MD for categories.

### Input Fields
Inputs are minimalist: a bottom-border only or a light grey stroke. On focus, the border transitions to Primary Blue with a subtle 4px outer glow of the same color.

### Status Chips
Small, rounded-pill chips used for "24/7 Available," "Certified Technician," or "Express Service." These use low-opacity versions of the primary and secondary colors as backgrounds with high-contrast text.

### Professional Trust Elements
A specific component pattern for "Technician Profiles" featuring circular avatars with a green "online" status ring, reinforcing the human aspect of the premium service.