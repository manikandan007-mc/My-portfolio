import os

os.makedirs("assets", exist_ok=True)

# A funny "Mani Contacting" cartoon illustration
svg_contact = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="600" height="600">
  <defs>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="10" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Mani (Funny Contact Character) -->
  <g transform="translate(300, 300)">
    <!-- Head -->
    <circle r="120" fill="#FFDBAC" />
    <path d="M-100,-20 Q-120,-150 0,-170 T100,-20" fill="none" stroke="#2D3748" stroke-width="30" stroke-linecap="round" />
    
    <!-- Excited Eyes -->
    <circle cx="-50" cy="-20" r="25" fill="white" stroke="#2D3748" stroke-width="4" />
    <circle cx="50" cy="-20" r="25" fill="white" stroke="#2D3748" stroke-width="4" />
    <circle cx="-45" cy="-25" r="8" fill="#2D3748" />
    <circle cx="45" cy="-25" r="8" fill="#2D3748" />
    
    <!-- Big Hello Smile -->
    <path d="M-60,40 Q0,100 60,40" fill="none" stroke="#2D3748" stroke-width="8" stroke-linecap="round" />
    
    <!-- Holding Phone/Mail Symbol -->
    <g transform="translate(80, 50) rotate(15)">
      <rect width="80" height="140" rx="15" fill="#1A202C" />
      <rect x="5" y="10" width="70" height="120" rx="10" fill="#3B82F6" opacity="0.8" />
      <circle cx="40" cy="115" r="8" fill="white" opacity="0.3" />
    </g>
    
    <!-- Waving Hand -->
    <g transform="translate(-150, 20) rotate(-20)">
      <rect width="40" height="60" rx="15" fill="#FFDBAC" />
      <path d="M0,0 Q-30,-50 0,-100" fill="none" stroke="#FFDBAC" stroke-width="30" stroke-linecap="round" />
    </g>
    
    <!-- Floating Notification Dots -->
    <circle cx="-180" cy="-150" r="10" fill="#E53E3E" filter="url(#glow)">
        <animate attributeName="opacity" values="0.3;1;0.3" dur="1s" repeatCount="indefinite" />
    </circle>
    <circle cx="180" cy="-100" r="15" fill="#8B5CF6" filter="url(#glow)">
        <animate attributeName="opacity" values="0.3;1;0.3" dur="1.5s" repeatCount="indefinite" />
    </circle>
  </g>
</svg>"""

with open("assets/mani_contact.svg", "w") as f:
    f.write(svg_contact)

print("Contact catchy illustration 'mani_contact' created!")
