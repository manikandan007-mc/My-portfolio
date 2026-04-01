import os

os.makedirs("assets", exist_ok=True)

svg_template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 500" width="800" height="500">
  <defs>
    <linearGradient id="grad1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{color1};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{color2};stop-opacity:1" />
    </linearGradient>
    <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="30" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.07)" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="800" height="500" fill="#0F0F12" />
  <rect width="800" height="500" fill="url(#grid)" />
  
  <!-- Background Ambient Glow -->
  <circle cx="200" cy="100" r="300" fill="{color1}" opacity="0.15" filter="url(#glow)"/>
  <circle cx="600" cy="400" r="300" fill="{color2}" opacity="0.15" filter="url(#glow)"/>

  <g transform="translate(400, 250)">
    {shapes}
  </g>
  
  <!-- Content Overlay Gradient (for text readability) -->
  <rect x="0" y="300" width="800" height="200" fill="url(#textGrad)" opacity="0.8">
    <defs>
      <linearGradient id="textGrad" x1="0%" y1="0%" x2="0%" y2="100%">
        <stop offset="0%" style="stop-color:transparent;stop-opacity:0" />
        <stop offset="100%" style="stop-color:#000000;stop-opacity:1" />
      </linearGradient>
    </defs>
  </rect>
</svg>"""

projects = [
    ("bg_2d_animation.svg", "#8B5CF6", "#06B6D4", 
     '<path d="M-300,-150 L300,-150 L300,150 L-300,150 Z" fill="url(#grad1)" opacity="0.05"/>'
     '<circle r="150" fill="url(#grad1)" filter="url(#glow)" opacity="0.6"/>'
     '<g transform="scale(1.2)">'
     '<path d="M-60,-40 L60,-40 L60,40 L-60,40 Z" fill="white" opacity="0.3"/>'
     '<circle cx="-40" cy="-20" r="10" fill="white"/>'
     '<circle cx="40" cy="-20" r="10" fill="white"/>'
     '<path d="M-30,20 Q0,45 30,20" fill="none" stroke="white" stroke-width="10" stroke-linecap="round"/>'
     '</g>'),
    
    ("bg_video_editing.svg", "#EC4899", "#8B5CF6", 
     '<rect x="-400" y="-250" width="800" height="500" fill="url(#grad1)" opacity="0.1"/>'
     '<rect x="-200" y="-130" width="400" height="260" rx="40" fill="url(#grad1)" filter="url(#glow)"/>'
     '<path d="M-50,-60 L70,0 L-50,60 Z" fill="white" opacity="0.9"/>'
     '<rect x="-220" y="-150" width="440" height="20" fill="white" opacity="0.1"/>'
     '<rect x="-220" y="130" width="440" height="20" fill="white" opacity="0.1"/>'),

    ("bg_motion_graphic.svg", "#10B981", "#3B82F6", 
     '<circle r="250" fill="none" stroke="url(#grad1)" stroke-width="2" opacity="0.2"/>'
     '<circle r="180" fill="none" stroke="url(#grad1)" stroke-width="4" stroke-dasharray="20,20" opacity="0.3"/>'
     '<circle r="100" fill="url(#grad1)" filter="url(#glow)" opacity="0.7"/>'
     '<rect x="-100" y="-5" width="200" height="10" fill="white" opacity="0.8"/>'
     '<rect x="-5" y="-100" width="10" height="200" fill="white" opacity="0.8"/>'),

    ("bg_ui_design.svg", "#3B82F6", "#8B5CF6", 
     '<rect x="-400" y="-250" width="800" height="500" fill="url(#grad1)" opacity="0.05"/>'
     '<rect x="-180" y="-220" width="360" height="440" rx="30" fill="#1A1A24" stroke="url(#grad1)" stroke-width="12" filter="url(#glow)"/>'
     '<rect x="-140" y="-170" width="280" height="50" rx="15" fill="url(#grad1)"/>'
     '<rect x="-140" y="-90" width="280" height="120" rx="15" fill="rgba(255,255,255,0.05)"/>'
     '<rect x="-140" y="60" width="130" height="120" rx="15" fill="rgba(255,255,255,0.05)"/>'
     '<rect x="10" y="60" width="130" height="120" rx="15" fill="rgba(255,255,255,0.05)"/>'),

    ("bg_color_grading.svg", "#F59E0B", "#EF4444", 
     '<circle cx="-120" cy="0" r="180" fill="#EF4444" opacity="0.5" filter="url(#glow)"/>'
     '<circle cx="120" cy="0" r="180" fill="#3B82F6" opacity="0.5" filter="url(#glow)"/>'
     '<circle cx="0" cy="-120" r="180" fill="#10B981" opacity="0.5" filter="url(#glow)"/>'
     '<circle r="60" fill="white" opacity="0.9" filter="url(#glow)"/>'),

    ("bg_ai_story.svg", "#6366F1", "#EC4899", 
     '<polygon points="-250,150 250,150 0,-250" fill="url(#grad1)" opacity="0.1"/>'
     '<path d="M0,-200 L180,100 L-180,100 Z" fill="url(#grad1)" filter="url(#glow)" opacity="0.7"/>'
     '<circle r="80" fill="#0A0A0C" stroke="white" stroke-width="6"/>'
     '<g transform="translate(0, -10)">'
     '<path d="M-25,10 Q0,40 25,10" fill="none" stroke="white" stroke-width="6" stroke-linecap="round"/>'
     '<circle cx="-20" cy="-10" r="8" fill="white"/><circle cx="20" cy="-10" r="8" fill="white"/>'
     '</g>'),

    ("bg_masking.svg", "#0ea5e9", "#10b981", 
     '<rect x="-400" y="-250" width="800" height="500" fill="url(#grad1)" opacity="0.05"/>'
     '<path d="M-200,-140 L200,-140 L200,140 L-200,140 Z" fill="none" stroke="white" stroke-dasharray="20,15" stroke-width="6" filter="url(#glow)"/>'
     '<circle cx="-200" cy="-140" r="15" fill="white"/><circle cx="200" cy="-140" r="15" fill="white"/>'
     '<circle cx="200" cy="140" r="15" fill="white"/><circle cx="-200" cy="140" r="15" fill="white"/>'
     '<path d="M-120,0 Q0,150 120,0 T300,0" fill="none" stroke="url(#grad1)" stroke-width="18" opacity="0.7"/>'),

    ("bg_logo_design.svg", "#f43f5e", "#8b5cf6", 
     '<rect x="-150" y="-150" width="300" height="300" rx="60" transform="rotate(45)" fill="url(#grad1)" filter="url(#glow)"/>'
     '<circle r="80" fill="#0F0F12"/>'
     '<path d="M-30,-30 L30,30 M-30,30 L30,-30" stroke="white" stroke-width="15" stroke-linecap="round"/>'
     '<circle r="120" fill="none" stroke="white" stroke-width="2" opacity="0.2"/>'),

    ("bg_motion_tracking.svg", "#8b5cf6", "#ec4899", 
     '<line x1="-400" y1="0" x2="400" y2="0" stroke="url(#grad1)" stroke-width="6" filter="url(#glow)"/>'
     '<line x1="0" y1="-250" x2="0" y2="250" stroke="url(#grad1)" stroke-width="6" filter="url(#glow)"/>'
     '<circle r="100" fill="none" stroke="white" stroke-width="3" stroke-dasharray="15,10"/>'
     '<rect x="-25" y="-25" width="50" height="50" fill="white" filter="url(#glow)"/>'
     '<circle r="200" fill="none" stroke="white" stroke-width="1" opacity="0.1"/>'),

    ("bg_camera_tracking.svg", "#14b8a6", "#3b82f6", 
     '<rect x="-220" y="-140" width="440" height="280" rx="25" fill="none" stroke="url(#grad1)" stroke-width="12" filter="url(#glow)"/>'
     '<circle cx="-130" cy="0" r="60" fill="url(#grad1)" opacity="0.5"/>'
     '<circle cx="130" cy="0" r="60" fill="url(#grad1)" opacity="0.5"/>'
     '<path d="M-60,80 L60,80 L0,-10 Z" fill="white" opacity="0.9"/>'
     '<path d="M-300,-180 L300,180" stroke="white" stroke-width="1" opacity="0.1"/>')
]

for filename, c1, c2, shapes in projects:
    content = svg_template.format(color1=c1, color2=c2, shapes=shapes)
    with open(os.path.join("assets", filename), "w") as f:
        f.write(content)

print("Full-box catchy visuals redefined!")
