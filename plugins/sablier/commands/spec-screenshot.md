---
argument-hint: [--deep]
description: Analyze website screenshots and generate detailed implementation specs
---

## Context

- Current directory: !`pwd`
- Target output: !`test -f SPEC.md && echo "SPEC.md exists (will be overwritten)" || echo "Will create new SPEC.md"`
- Arguments: $ARGUMENTS
- Thinking mode:
  !`echo "$ARGUMENTS" | grep -q -i "\-\-deep\|deep" && echo "DEEP (sequential thinking enabled)" || echo "STANDARD (regular analysis)"`

## Your Task

### STEP 1: Validate prerequisites

CHECK for images in conversation history:

- SCAN recent messages for screenshots or images
- IF no images found: ERROR "No screenshots detected in conversation. Please paste website screenshots before running
  this command."
- IF images found: LOG "Found screenshots ready for analysis"

### STEP 2: Perform ultra-detailed analysis

DETERMINE thinking mode from arguments:

- IF `$ARGUMENTS` contains "deep" or "--deep": USE sequential thinking tool
  (`mcp__sequential-thinking__sequentialthinking`)
- ELSE (STANDARD mode): Perform regular analysis

**Analysis framework - cover ALL of these aspects:**

1. **Layout Architecture**

   - Overall page structure (header, navigation, hero, main content, sidebars, footer)
   - Grid system and column layouts
   - Container widths and max-widths
   - Section hierarchy and nesting

1. **Typography System**

   - Font families (identify primary, secondary, monospace)
   - Font sizes for each text level (h1-h6, body, small, etc.)
   - Font weights used (light, regular, medium, semibold, bold)
   - Line heights and letter spacing
   - Text colors and contrast ratios

1. **Color Palette**

   - Primary brand colors
   - Secondary/accent colors
   - Background colors (main, sections, cards)
   - Text colors (headings, body, muted, links)
   - Border colors
   - State colors (success, error, warning, info)
   - Color codes in hex/rgb (best approximation)

1. **Spacing System**

   - Margins between major sections
   - Padding within components
   - Gap spacing in flex/grid layouts
   - Consistent spacing scale (e.g., 4px, 8px, 16px, 24px, 32px)
   - Vertical rhythm patterns

1. **Component Inventory**

   - Buttons (styles, sizes, states)
   - Input fields and forms
   - Cards and containers
   - Navigation elements
   - Icons and their style
   - Badges, tags, labels
   - Modals, tooltips, dropdowns
   - List items and data tables

1. **Visual Design Details**

   - Border radius values
   - Shadow styles (box-shadow parameters)
   - Border styles and thicknesses
   - Background patterns or gradients
   - Opacity/transparency effects

1. **Images and Media**

   - Image locations and dimensions
   - Image aspect ratios
   - Icon sets (are they SVG, font icons, or images?)
   - Logo placement and size
   - Decorative vs content images
   - **Note**: Which images need to be sourced/created

1. **Interactive Elements** (if discernible)

   - Hover states visible
   - Active/focus states
   - Transition/animation hints
   - Interactive feedback patterns

1. **Responsive Design** (if multiple viewports shown)

   - Breakpoints observable
   - Layout changes per breakpoint
   - Component behavior changes
   - Mobile-specific patterns

1. **Accessibility Considerations**

   - Color contrast issues
   - Heading hierarchy
   - Interactive element sizes
   - Text readability

**Analysis process:**

- Start with high-level layout observations
- Progressively zoom into details
- Measure or estimate dimensions
- Identify patterns and systems
- Note uncertainties or assumptions
- Cross-reference across multiple screenshots if provided

**DEEP mode only:** Use sequential thinking to systematically work through each aspect above with thorough reasoning.
**STANDARD mode:** Analyze directly without sequential thinking tool.

### STEP 3: Generate comprehensive SPEC.md

**Output:** Always write to `./SPEC.md`

**Content structure for SPEC.md:**

```markdown
# Website Implementation Specification

> Generated from screenshot analysis on [DATE]

## Overview

[2-3 sentence summary of the website's purpose and design style]

## Layout Architecture

### Page Structure

- [Describe overall layout]
- [Container constraints]
- [Section breakdown]

### Grid System

- [Grid configuration]
- [Column structure]
- [Responsive behavior]

## Typography

### Font Families

[List font families observed]

- Primary: [e.g., Inter, system-ui, sans-serif]
- Secondary: [if different font used for specific elements]
- Monospace: [if code/technical content visible]

### Text Styles

[List all distinct text styles from largest to smallest with their properties and usage. Use descriptive names based on
what you observe.]

**Example approach:**

- **Hero headline**: 72px, weight 800, line-height 1.1, #000000 - Main landing page headline
- **Section title**: 48px, weight 700, line-height 1.2, #1A1A1A - Major section headings
- **Card heading**: 24px, weight 600, line-height 1.3, #333333 - Component titles
- **Body text**: 16px, weight 400, line-height 1.6, #666666 - Paragraph content
- **Button label**: 16px, weight 600, line-height 1.2, #FFFFFF - All button text
- **Caption**: 14px, weight 400, line-height 1.4, #999999 - Image captions, footnotes

[If semantic HTML hierarchy is observable, note it. Otherwise, use functional names like above.]

### Text Styling Patterns

- Letter spacing: [any notable letter-spacing usage]
- Text transforms: [uppercase labels, capitalization patterns]
- Special effects: [gradients, shadows, outlines if visible]

## Color System

[Observe all distinct colors in the design. Group them by actual usage patterns, not predetermined categories. Name
groups based on what you see.]

**Example: Minimal palette**

- #2E5BFF - Brand color, all CTAs and interactive elements
- #1A1A1A - All text (headings and body)
- #F7F7F7 - Page background
- #FFFFFF - Card/component backgrounds

**Example: Rich color system**

**Brand Colors:**

- #FF6B35 - Primary brand (CTAs, key highlights)
- #004E89 - Secondary brand (headings, navigation)
- #FFD23F - Accent (decorative elements, highlights)

**Neutrals:**

- #FFFFFF - White (cards, backgrounds)
- #F5F5F5 - Light gray (alternate backgrounds)
- #E0E0E0 - Medium gray (borders)
- #666666 - Dark gray (body text)
- #000000 - Black (headings)

**Semantic Colors:** (only if visible)

- #00C853 - Success indicators
- #FF3B30 - Error states
- #FFC107 - Warning states

**Color Relationships:** [Note any observable patterns: tints, shades, complementary colors, or systematic variations]

## Spacing System

[Identify all distinct spacing values used. List from smallest to largest. Note whether they follow a systematic pattern
or appear ad-hoc.]

**Observed Spacing Values:** [Example: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px]

**Usage by Value:**

- 4px: [where this spacing is used]
- 8px: [where this spacing is used]
- 16px: [where this spacing is used]
- 24px: [where this spacing is used]
- [continue for all observed values]

**Pattern Analysis:**

[Choose the description that matches your observation]

**Example: Systematic scale**

- Follows 8px base unit scale (4, 8, 16, 24, 32, 48, 64)
- Consistent application across similar contexts
- Clear spacing hierarchy

**Example: Ad-hoc spacing**

- No obvious systematic scale detected
- Values vary: 5px, 12px, 18px, 22px, 37px observed
- Inconsistent spacing between similar elements
- May need design system standardization

**Common Patterns:**

- Section vertical spacing: [observed values]
- Card/component padding: [observed values]
- Element gaps (flex/grid): [observed values]
- Text block margins: [observed values]

## Component Inventory

[Document each distinct component with properties relevant to that specific component type. Different components need
different details.]

### [Component Name]

**Example: Button**

- Padding: 16px horizontal, 10px vertical
- Border radius: 8px
- Typography: 16px, weight 600
- Primary variant: #0066FF background, white text
- Secondary variant: white background, #0066FF text, 1px border
- Hover state: Subtle shadow (0 4px 8px rgba(0,0,0,0.1))
- Sizes observed: Small (12px padding), Default (16px), Large (20px)

**Example: Card**

- Background: white (#FFFFFF)
- Border: 1px solid #E5E5E5
- Border radius: 12px
- Padding: 24px
- Shadow: 0 2px 4px rgba(0,0,0,0.05)
- Hover: Lifts with increased shadow (0 8px 16px rgba(0,0,0,0.1))
- Typical content: Icon/image at top, heading, body text, optional CTA

**Example: Navigation Bar**

- Height: 64px
- Background: white with 1px bottom border (#E5E5E5)
- Logo: left side, ~120x40px
- Nav items: 16px text, 500 weight, ~24px horizontal spacing
- Right section: user avatar (32px) and notification icon

**Example: Input Field**

- Height: 44px
- Padding: 12px horizontal
- Border: 1px solid #D0D0D0, 6px radius
- Typography: 16px, weight 400
- Focus state: #0066FF border, subtle glow shadow
- Error state: #FF3B30 border, error message below in same color

[Continue with all components observed, adapting details to component type]

## Images and Assets

[List all visual assets observed in the design with relevant details. Group by type or location as appropriate.]

**Logo:** [Example]

- Location: Top-left navigation
- Approximate size: 120x40px
- Appears vector-based (crisp edges suggest SVG)
- Recommend: SVG format for scalability

**Hero/Feature Images:** [Example]

- Full-width hero background: ~1440x600px (2.4:1 aspect ratio)
- Content: Abstract gradient with geometric shapes
- Three product screenshots: ~400x300px each (4:3 ratio), in MacBook mockup frames
- Recommend: WebP format, optimized for web

**Icons:** [Example]

- Approximately 18-24 icons throughout design
- Style: Outline/stroke-based, consistent ~2px stroke width
- Primary size: 24x24px
- Locations: Navigation, feature cards, footer
- Style resembles: Heroicons/Feather Icons (or describe custom style)
- Recommend: Inline SVG or SVG sprite for performance

**Decorative Elements:** [Example]

- Background gradient orbs (3 visible, ~200-400px diameter)
- Abstract blob shapes behind cards
- Note: These may be CSS-generated (gradients + border-radius) rather than image files

**User-Generated Content:** [Example]

- Avatar placeholders: 40px diameter circles
- Thumbnail images in list items: 80x80px squares

[List any other visual assets: illustrations, patterns, textures, etc.]

## Responsive Behavior

[Document responsive patterns only if multiple viewports are shown. If only one viewport, note the limitation.]

### Viewports Analyzed

[Example: Desktop (~1440px), Tablet (~768px), Mobile (~375px)]

### Observable Layout Adaptations

[If multiple viewports visible, describe changes:]

**Desktop (>=992px):**

- Multi-column grid (3 columns for cards)
- Side navigation visible
- Horizontal button groups

**Tablet (>=576px, <992px):**

- Two-column grid
- Side navigation collapses to icon-only or hamburger
- Buttons maintain horizontal layout

**Mobile (<576px):**

- Single column layout
- Hamburger menu
- Stacked buttons
- Reduced padding/margins

### Inferred Breakpoints

[Based on observable layout changes]

- Mobile/tablet transition: ~576px
- Tablet/desktop transition: ~992px

**If only one viewport provided:**

- Only [desktop/mobile] view available
- Responsive behavior cannot be fully specified
- Recommend: [Provide tablet and mobile screenshots for complete specification]

### Responsive Patterns Observed

- [Grid column changes, navigation patterns, typography scaling, spacing adjustments]

## Interactive Elements and States

[Document only interactive elements and states actually visible in the screenshots. Different states may be shown across
multiple screenshots.]

### [Element Name]

[Only include sections for elements you can actually observe]

**Example: Buttons**

- Default: Solid blue background (#0066FF), white text
- Hover: Appears to add subtle shadow (visible in one screenshot)
- Estimated transition: ~200-300ms ease

**Example: Dropdown Menu**

- Closed and open states both visible in screenshots
- Opens downward, white background, subtle shadow (0 4px 8px rgba(0,0,0,0.15))
- Menu items: 16px text, 12px vertical padding, hover background #F5F5F5

**Example: Navigation Links**

- Default: Medium gray (#666666)
- Active/current: Bold weight + primary color (#0066FF) + bottom border
- Hover: Primary color (#0066FF)

### States Not Visible in Screenshots

[Be explicit about interactive states that cannot be determined from static images]

- Form input focus states (no active form inputs shown)
- Button disabled appearance
- Error validation styling
- Loading states
- Tooltip/popover behavior
- Animation durations and easing
- Mobile menu open/close transition

## Implementation Considerations

### Design Complexity Assessment

[Objective assessment of visual complexity based on observables]

- Component count: ~[X] distinct component types
- Layout complexity: [Simple/Medium/High] - [brief description]
- Interaction richness: [forms, dropdowns, modals, etc. observed]
- Animation requirements: [subtle/moderate/heavy based on visible hints]

### Observable Technical Requirements

[Only technical needs directly observable from the design]

**Asset Optimization:**

- Large hero images present (optimization important)
- [x] icons needed (consistent [outline/filled] style)
- [Note if image-heavy or lightweight]

**Icon System:**

- Approximately [X] icons observed
- Style: [outline/filled/mixed]
- Suggest: Find matching icon set ([Heroicons/Feather/etc.] or similar style)

**Responsive Implementation:**

- [Simple/Complex] responsive grid required
- [Specific layout patterns to handle]

**Form Requirements:** (if applicable)

- Validation states needed (not all shown in screenshots)
- Error messaging patterns
- Input types: [text, email, select, etc. observed]

### Accessibility Observations

[Observable accessibility considerations]

- Color contrast: [Appears adequate/May need verification for small text]
- Interactive element sizing: [Buttons appear >44px / Some elements may be undersized]
- Text readability: [Body text appears 16px+ / Small text may be <16px]
- Heading hierarchy: [Should be verified during implementation]

### Cannot Determine from Screenshots

[Be explicit about limitations]

- Framework requirements (React/Vue/vanilla JS)
- State management needs
- API integration patterns
- Animation/transition specifications beyond visible hints
- Performance requirements
- Build tool preferences
- Specific library dependencies beyond icon sets

## Open Questions / Assumptions

- [List any uncertainties]
- [Areas needing clarification]
- [Assumptions made during analysis]

## Next Steps

1. [Verification tasks]
2. [Asset procurement tasks]
3. [Implementation phases]

---

_Note: All measurements are approximations based on screenshot analysis. Verify exact values during implementation._
```

WRITE the file to `./SPEC.md` with comprehensive, specific details from your analysis.

CONFIRM write operation:

- IF successful: LOG "Written to SPEC.md"
- IF failed: ERROR "Failed to write file: [reason]" and suggest fix

### STEP 4: Present summary to user

DISPLAY concise summary (NOT the full spec):

```
## Screenshot Analysis Complete

### Overview
[1-2 sentence description]

### Key Findings
- **Layout**: [brief description]
- **Components**: [count] distinct components identified
- **Color Palette**: [count] colors in system
- **Typography**: [primary font family], [count] type levels
- **Spacing**: [spacing scale summary]
- **Assets**: [count] images/icons to source

### Output
Full specification: `SPEC.md`

### Recommendations
[1-2 key technical recommendations]
```

## Examples

**Basic usage (standard mode, default output):**

```
/spec-screenshot
```

**Deep mode (with sequential thinking):**

```
/spec-screenshot --deep
```

**Multi-screenshot workflow:**

```
1. Paste multiple screenshots (desktop, tablet, mobile)
2. Run: /spec-screenshot --deep
3. Review SPEC.md for comprehensive breakdown
```

## Notes

- **Thinking modes**:
  - **STANDARD** (default): Fast analysis with direct reasoning
  - **DEEP**: Uses sequential thinking tool for thorough, step-by-step analysis (slower but more comprehensive)
- **Approximations**: All measurements are best-effort approximations; verify during implementation
- **Image sourcing**: Command explicitly notes which images need to be obtained or created
- **Overwrite behavior**: Running command multiple times will overwrite existing SPEC.md
- **Context efficiency**: Only summary shown in chat; full spec written to file
- **Multi-screenshot support**: Analyzes all images in conversation context
- **Best results**: Higher resolution screenshots provide more accurate measurements
- **When to use deep mode**: Complex designs, large component libraries, or when you need extremely thorough analysis
