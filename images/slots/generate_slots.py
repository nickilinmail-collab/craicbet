import os

slots = {
    "gates-of-olympus": {
        "bg1": "#1a237e", "bg2": "#0d47a1",
        "elements": '''
    <!-- Zeus lightning bolts & columns -->
    <rect x="30" y="80" width="16" height="120" rx="4" fill="rgba(255,215,0,0.3)"/>
    <rect x="254" y="80" width="16" height="120" rx="4" fill="rgba(255,215,0,0.3)"/>
    <!-- Lightning -->
    <polygon points="150,20 130,90 155,85 125,170 175,80 150,85" fill="#FFD700" opacity="0.9"/>
    <polygon points="160,30 145,80 165,77 140,150 180,72 160,77" fill="#FFF59D" opacity="0.5"/>
    <!-- Clouds -->
    <ellipse cx="80" cy="50" rx="50" ry="25" fill="rgba(255,255,255,0.15)"/>
    <ellipse cx="220" cy="40" rx="45" ry="20" fill="rgba(255,255,255,0.1)"/>
    <!-- Multiplier orbs -->
    <circle cx="70" cy="140" r="18" fill="rgba(255,215,0,0.2)" stroke="#FFD700" stroke-width="1.5"/>
    <text x="70" y="145" text-anchor="middle" font-size="12" font-weight="bold" fill="#FFD700">5x</text>
    <circle cx="230" cy="130" r="18" fill="rgba(255,215,0,0.2)" stroke="#FFD700" stroke-width="1.5"/>
    <text x="230" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="#FFD700">500x</text>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="serif" font-size="20" font-weight="bold" fill="#FFD700" letter-spacing="2">GATES OF OLYMPUS</text>'''
    },
    "sweet-bonanza": {
        "bg1": "#E91E63", "bg2": "#880E4F",
        "elements": '''
    <!-- Candy/fruit elements -->
    <circle cx="60" cy="60" r="22" fill="#FF5252"/>
    <circle cx="55" cy="55" r="5" fill="rgba(255,255,255,0.4)"/>
    <circle cx="200" cy="50" r="18" fill="#7C4DFF"/>
    <circle cx="196" cy="46" r="4" fill="rgba(255,255,255,0.4)"/>
    <circle cx="130" cy="80" r="20" fill="#69F0AE"/>
    <circle cx="126" cy="76" r="4" fill="rgba(255,255,255,0.4)"/>
    <!-- Lollipop -->
    <circle cx="250" cy="120" r="20" fill="#FFAB40" stroke="#FF6D00" stroke-width="2"/>
    <path d="M240,115 Q250,125 260,115" stroke="white" stroke-width="2" fill="none" opacity="0.5"/>
    <rect x="248" y="140" width="4" height="40" rx="2" fill="#BCAAA4"/>
    <!-- Banana -->
    <path d="M40,140 Q70,110 90,140 Q70,155 40,140Z" fill="#FFD54F"/>
    <!-- Bomb multiplier -->
    <circle cx="150" cy="140" r="22" fill="#37474F"/>
    <circle cx="150" cy="140" r="18" fill="#455A64"/>
    <text x="150" y="146" text-anchor="middle" font-size="16" font-weight="bold" fill="#FFD700">100x</text>
    <path d="M160,120 Q170,105 165,100" stroke="#FF6D00" stroke-width="2" fill="none"/>
    <circle cx="165" cy="98" r="4" fill="#FF6D00"/>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="sans-serif" font-size="20" font-weight="bold" fill="white">SWEET BONANZA</text>'''
    },
    "big-bass-bonanza": {
        "bg1": "#1565C0", "bg2": "#0D47A1",
        "elements": '''
    <!-- Water waves -->
    <path d="M0,160 Q40,145 80,160 Q120,175 160,160 Q200,145 240,160 Q280,175 300,160" stroke="rgba(255,255,255,0.2)" stroke-width="2" fill="none"/>
    <path d="M0,170 Q40,155 80,170 Q120,185 160,170 Q200,155 240,170 Q280,185 300,170" stroke="rgba(255,255,255,0.15)" stroke-width="2" fill="none"/>
    <!-- Fish -->
    <g transform="translate(150,110) rotate(-10)">
      <ellipse cx="0" cy="0" rx="40" ry="22" fill="#4CAF50"/>
      <polygon points="35,-15 55,0 35,15" fill="#388E3C"/>
      <circle cx="-20" cy="-5" r="4" fill="white"/>
      <circle cx="-20" cy="-5" r="2" fill="#1B5E20"/>
      <path d="M-30,5 Q-20,12 -10,5" stroke="#1B5E20" stroke-width="1.5" fill="none"/>
      <text x="5" y="5" font-size="14" font-weight="bold" fill="#FFD700">$</text>
    </g>
    <!-- Fishing rod -->
    <path d="M60,20 Q80,30 100,80 Q110,100 120,105" stroke="#8D6E63" stroke-width="2.5" fill="none"/>
    <line x1="120" y1="105" x2="120" y2="130" stroke="#BDBDBD" stroke-width="1" stroke-dasharray="3,3"/>
    <!-- Hook -->
    <path d="M118,128 Q115,138 120,140 Q125,138 122,128" stroke="#BDBDBD" stroke-width="1.5" fill="none"/>
    <!-- Coins -->
    <circle cx="220" cy="80" r="12" fill="#FFD700" stroke="#FFA000" stroke-width="1.5"/>
    <text x="220" y="85" text-anchor="middle" font-size="10" font-weight="bold" fill="#E65100">€</text>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="sans-serif" font-size="18" font-weight="bold" fill="white">BIG BASS BONANZA</text>'''
    },
    "book-of-dead": {
        "bg1": "#795548", "bg2": "#3E2723",
        "elements": '''
    <!-- Egyptian pyramid background -->
    <polygon points="150,30 60,180 240,180" fill="rgba(255,193,7,0.15)" stroke="rgba(255,193,7,0.3)" stroke-width="1"/>
    <!-- Book -->
    <g transform="translate(110,70)">
      <rect x="0" y="0" width="80" height="60" rx="3" fill="#D4A017" stroke="#B8860B" stroke-width="2"/>
      <rect x="5" y="5" width="70" height="50" fill="#F5DEB3"/>
      <line x1="40" y1="5" x2="40" y2="55" stroke="#D4A017" stroke-width="2"/>
      <!-- Hieroglyphs -->
      <text x="20" y="25" font-size="10" fill="#8B4513">&#9760;</text>
      <text x="20" y="42" font-size="10" fill="#8B4513">&#9765;</text>
      <text x="55" y="25" font-size="10" fill="#8B4513">&#9764;</text>
      <text x="55" y="42" font-size="10" fill="#8B4513">&#9768;</text>
    </g>
    <!-- Ankh symbol -->
    <g transform="translate(60,100)">
      <circle cx="0" cy="-8" r="8" fill="none" stroke="#FFD700" stroke-width="2.5"/>
      <line x1="0" y1="0" x2="0" y2="30" stroke="#FFD700" stroke-width="2.5"/>
      <line x1="-10" y1="10" x2="10" y2="10" stroke="#FFD700" stroke-width="2.5"/>
    </g>
    <!-- Eye of Horus -->
    <g transform="translate(230,90)">
      <ellipse cx="0" cy="0" rx="15" ry="8" fill="none" stroke="#FFD700" stroke-width="2"/>
      <circle cx="0" cy="0" r="5" fill="#FFD700"/>
      <path d="M-15,0 Q-20,15 -10,25" stroke="#FFD700" stroke-width="2" fill="none"/>
    </g>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="serif" font-size="20" font-weight="bold" fill="#FFD700" letter-spacing="2">BOOK OF DEAD</text>'''
    },
    "starburst": {
        "bg1": "#4A148C", "bg2": "#1A237E",
        "elements": '''
    <!-- Star burst rays -->
    <g transform="translate(150,110)">
      <line x1="0" y1="-80" x2="0" y2="80" stroke="rgba(255,255,255,0.1)" stroke-width="20"/>
      <line x1="-80" y1="0" x2="80" y2="0" stroke="rgba(255,255,255,0.1)" stroke-width="20"/>
      <line x1="-60" y1="-60" x2="60" y2="60" stroke="rgba(255,255,255,0.07)" stroke-width="15"/>
      <line x1="60" y1="-60" x2="-60" y2="60" stroke="rgba(255,255,255,0.07)" stroke-width="15"/>
    </g>
    <!-- Central star -->
    <polygon points="150,50 160,90 200,90 168,115 178,155 150,130 122,155 132,115 100,90 140,90" fill="#FFD700" opacity="0.9"/>
    <polygon points="150,65 157,90 180,90 162,108 168,135 150,118 132,135 138,108 120,90 143,90" fill="#FFF9C4"/>
    <!-- Gems -->
    <polygon points="70,60 80,45 90,60 80,75" fill="#E040FB" opacity="0.8"/>
    <polygon points="230,70 240,55 250,70 240,85" fill="#00E5FF" opacity="0.8"/>
    <polygon points="80,150 90,135 100,150 90,165" fill="#76FF03" opacity="0.8"/>
    <polygon points="220,150 230,135 240,150 230,165" fill="#FF6D00" opacity="0.8"/>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="sans-serif" font-size="22" font-weight="bold" fill="white" letter-spacing="3">STARBURST</text>'''
    },
    "crazy-time": {
        "bg1": "#FF6F00", "bg2": "#E65100",
        "elements": '''
    <!-- Wheel -->
    <circle cx="150" cy="110" r="70" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="4"/>
    <circle cx="150" cy="110" r="65" fill="none" stroke="rgba(255,255,255,0.15)" stroke-width="25"/>
    <!-- Wheel segments -->
    <path d="M150,45 L150,110 L215,110" fill="rgba(255,0,0,0.3)" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <path d="M150,110 L215,110 L150,175" fill="rgba(0,100,255,0.3)" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <path d="M150,110 L150,175 L85,110" fill="rgba(0,200,0,0.3)" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <path d="M150,110 L85,110 L150,45" fill="rgba(255,215,0,0.3)" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <!-- Center -->
    <circle cx="150" cy="110" r="15" fill="#FFD700"/>
    <text x="150" y="116" text-anchor="middle" font-size="14" font-weight="bold" fill="#E65100">CT</text>
    <!-- Pointer -->
    <polygon points="150,35 145,25 155,25" fill="white"/>
    <!-- Multipliers -->
    <text x="180" y="80" font-size="11" font-weight="bold" fill="white">25x</text>
    <text x="180" y="145" font-size="11" font-weight="bold" fill="white">50x</text>
    <text x="110" y="80" font-size="11" font-weight="bold" fill="white">10x</text>
    <text x="110" y="145" font-size="11" font-weight="bold" fill="white">5x</text>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="sans-serif" font-size="22" font-weight="bold" fill="white" letter-spacing="2">CRAZY TIME</text>'''
    },
    "mega-moolah": {
        "bg1": "#FF8F00", "bg2": "#E65100",
        "elements": '''
    <!-- Safari scene -->
    <!-- Sun -->
    <circle cx="220" cy="50" r="25" fill="#FFD54F" opacity="0.8"/>
    <!-- Grass -->
    <rect x="0" y="160" width="300" height="70" fill="#33691E" opacity="0.5"/>
    <!-- Lion silhouette -->
    <g transform="translate(100,100)">
      <!-- Body -->
      <ellipse cx="0" cy="20" rx="35" ry="20" fill="#F57F17"/>
      <!-- Mane -->
      <circle cx="-15" cy="5" r="25" fill="#E65100" opacity="0.8"/>
      <!-- Head -->
      <circle cx="-25" cy="5" r="15" fill="#F57F17"/>
      <!-- Eye -->
      <circle cx="-30" cy="2" r="2" fill="white"/>
      <circle cx="-30" cy="2" r="1" fill="black"/>
      <!-- Ears -->
      <circle cx="-20" cy="-8" r="5" fill="#E65100"/>
      <circle cx="-30" cy="-6" r="5" fill="#E65100"/>
      <!-- Tail -->
      <path d="M35,15 Q50,0 45,20" stroke="#F57F17" stroke-width="3" fill="none"/>
      <!-- Legs -->
      <rect x="-15" y="35" width="6" height="20" rx="3" fill="#F57F17"/>
      <rect x="10" y="35" width="6" height="20" rx="3" fill="#F57F17"/>
    </g>
    <!-- Jackpot text -->
    <text x="150" y="60" text-anchor="middle" font-size="14" font-weight="bold" fill="#FFD700">JACKPOT</text>
    <text x="150" y="80" text-anchor="middle" font-size="11" fill="white" opacity="0.8">€10M+</text>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="serif" font-size="20" font-weight="bold" fill="white">MEGA MOOLAH</text>'''
    },
    "starlight-princess": {
        "bg1": "#E91E63", "bg2": "#AD1457",
        "elements": '''
    <!-- Stars background -->
    <circle cx="50" cy="40" r="2" fill="white" opacity="0.8"/>
    <circle cx="100" cy="30" r="1.5" fill="white" opacity="0.6"/>
    <circle cx="200" cy="50" r="2" fill="white" opacity="0.7"/>
    <circle cx="250" cy="35" r="1.5" fill="white" opacity="0.5"/>
    <circle cx="270" cy="80" r="1" fill="white" opacity="0.6"/>
    <!-- Princess wand -->
    <line x1="150" y1="40" x2="150" y2="140" stroke="#FFD700" stroke-width="3"/>
    <polygon points="150,30 140,50 160,50" fill="#FFD700"/>
    <!-- Star on wand -->
    <polygon points="150,25 153,32 161,32 155,37 157,45 150,40 143,45 145,37 139,32 147,32" fill="#FFF9C4"/>
    <!-- Sparkles -->
    <text x="120" y="70" font-size="16" fill="#FFD700" opacity="0.8">&#10022;</text>
    <text x="180" y="90" font-size="12" fill="#FF80AB" opacity="0.8">&#10022;</text>
    <text x="90" y="120" font-size="10" fill="white" opacity="0.6">&#10022;</text>
    <text x="210" y="60" font-size="14" fill="#FFD700" opacity="0.7">&#10022;</text>
    <!-- Crown -->
    <g transform="translate(125,150)">
      <polygon points="0,20 5,0 15,12 25,0 35,12 45,0 50,20" fill="#FFD700" stroke="#FFA000" stroke-width="1"/>
      <circle cx="5" cy="5" r="3" fill="#E040FB"/>
      <circle cx="25" cy="0" r="3" fill="#E040FB"/>
      <circle cx="45" cy="5" r="3" fill="#E040FB"/>
    </g>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="serif" font-size="18" font-weight="bold" fill="white">STARLIGHT PRINCESS</text>'''
    },
    "wolf-gold": {
        "bg1": "#E65100", "bg2": "#BF360C",
        "elements": '''
    <!-- Moon -->
    <circle cx="220" cy="50" r="30" fill="#FFF9C4" opacity="0.9"/>
    <circle cx="230" cy="45" r="28" fill="#E65100"/>
    <!-- Wolf silhouette howling at moon -->
    <g transform="translate(100,60)">
      <!-- Body -->
      <path d="M0,80 Q10,50 30,40 Q40,35 45,25 L50,15 L48,30 Q55,35 60,45 Q70,55 80,80 Z" fill="#37474F"/>
      <!-- Tail -->
      <path d="M0,75 Q-15,55 -5,45" stroke="#37474F" stroke-width="5" fill="none" stroke-linecap="round"/>
      <!-- Ear -->
      <polygon points="42,28 38,15 48,22" fill="#455A64"/>
    </g>
    <!-- Stars -->
    <circle cx="50" cy="30" r="1.5" fill="#FFF9C4"/>
    <circle cx="80" cy="45" r="1" fill="#FFF9C4" opacity="0.7"/>
    <circle cx="270" cy="70" r="1.5" fill="#FFF9C4"/>
    <!-- Gold coins at bottom -->
    <circle cx="80" cy="170" r="10" fill="#FFD700" stroke="#FFA000" stroke-width="1"/>
    <circle cx="100" cy="175" r="10" fill="#FFD700" stroke="#FFA000" stroke-width="1"/>
    <circle cx="200" cy="172" r="10" fill="#FFD700" stroke="#FFA000" stroke-width="1"/>
    <circle cx="220" cy="168" r="10" fill="#FFD700" stroke="#FFA000" stroke-width="1"/>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="serif" font-size="22" font-weight="bold" fill="#FFD700" letter-spacing="2">WOLF GOLD</text>'''
    },
    "gonzos-quest": {
        "bg1": "#2E7D32", "bg2": "#1B5E20",
        "elements": '''
    <!-- Jungle vines -->
    <path d="M30,0 Q40,40 20,80 Q10,120 30,160" stroke="#4CAF50" stroke-width="3" fill="none"/>
    <path d="M270,0 Q260,50 280,100 Q270,140 260,180" stroke="#4CAF50" stroke-width="3" fill="none"/>
    <!-- Stone blocks (avalanche reels) -->
    <rect x="80" y="50" width="40" height="35" rx="4" fill="#8D6E63" stroke="#6D4C41" stroke-width="1.5"/>
    <rect x="130" y="50" width="40" height="35" rx="4" fill="#A1887F" stroke="#6D4C41" stroke-width="1.5"/>
    <rect x="180" y="50" width="40" height="35" rx="4" fill="#8D6E63" stroke="#6D4C41" stroke-width="1.5"/>
    <rect x="80" y="95" width="40" height="35" rx="4" fill="#A1887F" stroke="#6D4C41" stroke-width="1.5"/>
    <rect x="130" y="95" width="40" height="35" rx="4" fill="#8D6E63" stroke="#6D4C41" stroke-width="1.5"/>
    <rect x="180" y="95" width="40" height="35" rx="4" fill="#A1887F" stroke="#6D4C41" stroke-width="1.5"/>
    <!-- Face symbols on blocks -->
    <text x="100" y="75" text-anchor="middle" font-size="18">&#128163;</text>
    <text x="150" y="75" text-anchor="middle" font-size="18">&#127942;</text>
    <text x="200" y="75" text-anchor="middle" font-size="18">&#128142;</text>
    <!-- Gold mask -->
    <g transform="translate(150,155)">
      <ellipse cx="0" cy="0" rx="20" ry="15" fill="#FFD700" stroke="#FFA000" stroke-width="1.5"/>
      <circle cx="-7" cy="-3" r="3" fill="#3E2723"/>
      <circle cx="7" cy="-3" r="3" fill="#3E2723"/>
      <path d="M-6,5 Q0,10 6,5" stroke="#3E2723" stroke-width="1.5" fill="none"/>
    </g>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="sans-serif" font-size="20" font-weight="bold" fill="#FFD700">GONZO&#39;S QUEST</text>'''
    },
    "reactoonz": {
        "bg1": "#6A1B9A", "bg2": "#4A148C",
        "elements": '''
    <!-- Grid background -->
    <g opacity="0.15">
      <line x1="60" y1="30" x2="60" y2="190" stroke="white" stroke-width="1"/>
      <line x1="120" y1="30" x2="120" y2="190" stroke="white" stroke-width="1"/>
      <line x1="180" y1="30" x2="180" y2="190" stroke="white" stroke-width="1"/>
      <line x1="240" y1="30" x2="240" y2="190" stroke="white" stroke-width="1"/>
    </g>
    <!-- Alien blobs -->
    <circle cx="90" cy="70" r="22" fill="#E040FB"/>
    <circle cx="82" cy="64" r="5" fill="white"/>
    <circle cx="98" cy="64" r="5" fill="white"/>
    <circle cx="82" cy="64" r="2.5" fill="#1A237E"/>
    <circle cx="98" cy="64" r="2.5" fill="#1A237E"/>
    <path d="M82,78 Q90,85 98,78" stroke="#1A237E" stroke-width="1.5" fill="none"/>
    
    <circle cx="170" cy="80" r="20" fill="#00E676"/>
    <circle cx="163" cy="74" r="4" fill="white"/>
    <circle cx="177" cy="74" r="4" fill="white"/>
    <circle cx="163" cy="74" r="2" fill="#1A237E"/>
    <circle cx="177" cy="74" r="2" fill="#1A237E"/>
    <path d="M163,86 Q170,92 177,86" stroke="#1A237E" stroke-width="1.5" fill="none"/>
    
    <circle cx="130" cy="130" r="24" fill="#FFAB40"/>
    <circle cx="122" cy="124" r="5" fill="white"/>
    <circle cx="138" cy="124" r="5" fill="white"/>
    <circle cx="122" cy="124" r="2.5" fill="#1A237E"/>
    <circle cx="138" cy="124" r="2.5" fill="#1A237E"/>
    <path d="M122,138 Q130,146 138,138" stroke="#1A237E" stroke-width="1.5" fill="none"/>
    
    <circle cx="220" cy="120" r="18" fill="#40C4FF"/>
    <circle cx="214" cy="115" r="4" fill="white"/>
    <circle cx="226" cy="115" r="4" fill="white"/>
    <circle cx="214" cy="115" r="2" fill="#1A237E"/>
    <circle cx="226" cy="115" r="2" fill="#1A237E"/>
    <!-- Electric sparkles -->
    <text x="60" y="130" font-size="14" fill="#E040FB">&#9889;</text>
    <text x="240" y="70" font-size="14" fill="#40C4FF">&#9889;</text>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="sans-serif" font-size="20" font-weight="bold" fill="white">REACTOONZ</text>'''
    },
    "fire-joker": {
        "bg1": "#D84315", "bg2": "#BF360C",
        "elements": '''
    <!-- Flames -->
    <path d="M60,180 Q50,120 70,100 Q60,80 80,50 Q90,80 85,100 Q100,120 90,180Z" fill="#FF6D00" opacity="0.6"/>
    <path d="M200,180 Q190,130 210,110 Q200,90 220,60 Q230,90 225,110 Q240,130 230,180Z" fill="#FF6D00" opacity="0.6"/>
    <!-- Center fire -->
    <path d="M120,180 Q110,130 130,100 Q120,70 150,30 Q180,70 170,100 Q190,130 180,180Z" fill="#FFAB00" opacity="0.7"/>
    <path d="M130,180 Q125,140 140,115 Q135,90 150,55 Q165,90 160,115 Q175,140 170,180Z" fill="#FFD54F" opacity="0.8"/>
    <!-- Joker hat -->
    <g transform="translate(150,80)">
      <path d="M-25,0 Q-30,-30 -15,-25 Q0,-40 15,-25 Q30,-30 25,0Z" fill="#D50000" stroke="#B71C1C" stroke-width="1"/>
      <circle cx="-15" cy="-27" r="4" fill="#FFD700"/>
      <circle cx="15" cy="-27" r="4" fill="#FFD700"/>
      <circle cx="0" cy="-42" r="4" fill="#FFD700"/>
    </g>
    <!-- Joker face -->
    <circle cx="150" cy="100" r="18" fill="#FFF9C4"/>
    <path d="M142,95 L145,92 L148,95" stroke="#D50000" stroke-width="1.5" fill="none"/>
    <path d="M152,95 L155,92 L158,95" stroke="#D50000" stroke-width="1.5" fill="none"/>
    <path d="M142,105 Q150,115 158,105" stroke="#D50000" stroke-width="2" fill="#D50000" fill-opacity="0.3"/>
    <!-- 3x3 grid hint -->
    <text x="150" y="160" text-anchor="middle" font-size="11" fill="white" opacity="0.7">3x3 CLASSIC</text>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="sans-serif" font-size="22" font-weight="bold" fill="#FFD700">FIRE JOKER</text>'''
    },
    "aviator": {
        "bg1": "#1A1A2E", "bg2": "#0F0F23",
        "elements": '''
    <!-- Graph line -->
    <path d="M30,170 Q80,165 120,140 Q160,110 190,60 Q210,30 230,20" stroke="#FF1744" stroke-width="3" fill="none"/>
    <!-- Fill under curve -->
    <path d="M30,170 Q80,165 120,140 Q160,110 190,60 Q210,30 230,20 L230,170 Z" fill="rgba(255,23,68,0.15)"/>
    <!-- Plane -->
    <g transform="translate(225,18) rotate(-20)">
      <polygon points="0,0 -20,8 -20,-8" fill="#FF1744"/>
      <polygon points="-15,-8 -25,0 -15,0" fill="white" opacity="0.3"/>
      <rect x="-25" y="-2" width="8" height="4" fill="#FF1744"/>
    </g>
    <!-- Multiplier -->
    <text x="180" y="100" font-size="32" font-weight="bold" fill="#FF1744" font-family="monospace">7.42x</text>
    <!-- Grid lines -->
    <line x1="30" y1="170" x2="270" y2="170" stroke="rgba(255,255,255,0.1)" stroke-width="1"/>
    <line x1="30" y1="130" x2="270" y2="130" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
    <line x1="30" y1="90" x2="270" y2="90" stroke="rgba(255,255,255,0.05)" stroke-width="1"/>
    <!-- Cash out button hint -->
    <rect x="100" y="150" width="100" height="25" rx="12" fill="#FF1744" opacity="0.8"/>
    <text x="150" y="167" text-anchor="middle" font-size="11" font-weight="bold" fill="white">CASH OUT</text>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="monospace" font-size="22" font-weight="bold" fill="#FF1744">AVIATOR</text>'''
    },
    "sugar-rush": {
        "bg1": "#EC407A", "bg2": "#C2185B",
        "elements": '''
    <!-- Candy land -->
    <circle cx="60" cy="50" r="20" fill="#AB47BC" opacity="0.7"/>
    <circle cx="60" cy="50" r="12" fill="#CE93D8" opacity="0.5"/>
    <rect x="80" y="120" width="20" height="60" rx="5" fill="#FF7043"/>
    <circle cx="90" cy="115" r="15" fill="#FF5722" opacity="0.8"/>
    <rect x="200" y="100" width="18" height="70" rx="5" fill="#66BB6A"/>
    <circle cx="209" cy="95" r="14" fill="#43A047" opacity="0.8"/>
    <!-- Gummy bears -->
    <g transform="translate(150,80)">
      <ellipse cx="0" cy="0" rx="15" ry="18" fill="#F44336" opacity="0.8"/>
      <circle cx="-5" cy="-5" r="2" fill="white" opacity="0.8"/>
      <circle cx="5" cy="-5" r="2" fill="white" opacity="0.8"/>
      <ellipse cx="-8" cy="8" rx="5" ry="8" fill="#F44336" opacity="0.6"/>
      <ellipse cx="8" cy="8" rx="5" ry="8" fill="#F44336" opacity="0.6"/>
    </g>
    <!-- Multiplier tumble -->
    <text x="230" y="60" font-size="14" font-weight="bold" fill="#FFD700">x2</text>
    <text x="250" y="80" font-size="16" font-weight="bold" fill="#FFD700">x4</text>
    <text x="240" y="100" font-size="18" font-weight="bold" fill="#FFD700">x8</text>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="sans-serif" font-size="22" font-weight="bold" fill="white">SUGAR RUSH</text>'''
    },
    "razor-shark": {
        "bg1": "#00838F", "bg2": "#006064",
        "elements": '''
    <!-- Bubbles -->
    <circle cx="50" cy="60" r="6" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="1"/>
    <circle cx="70" cy="40" r="4" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <circle cx="240" cy="50" r="5" fill="none" stroke="rgba(255,255,255,0.25)" stroke-width="1"/>
    <circle cx="260" cy="80" r="3" fill="none" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <!-- Shark -->
    <g transform="translate(150,100)">
      <ellipse cx="0" cy="0" rx="55" ry="25" fill="#546E7A"/>
      <polygon points="50,-5 80,0 50,5" fill="#455A64"/>
      <polygon points="0,-25 10,-45 20,-25" fill="#546E7A"/>
      <!-- Shark eye -->
      <circle cx="-30" cy="-5" r="4" fill="white"/>
      <circle cx="-30" cy="-5" r="2" fill="#1A237E"/>
      <!-- Teeth -->
      <path d="M-50,5 L-45,12 L-40,5 L-35,12 L-30,5 L-25,12 L-20,5" stroke="white" stroke-width="1.5" fill="none"/>
      <!-- Gills -->
      <line x1="-10" y1="-8" x2="-5" y2="0" stroke="#455A64" stroke-width="1.5"/>
      <line x1="-5" y1="-8" x2="0" y2="0" stroke="#455A64" stroke-width="1.5"/>
    </g>
    <!-- Seaweed -->
    <path d="M40,180 Q35,140 45,120 Q40,100 50,80" stroke="#2E7D32" stroke-width="3" fill="none"/>
    <path d="M260,180 Q255,150 265,130 Q260,110 270,90" stroke="#2E7D32" stroke-width="3" fill="none"/>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="sans-serif" font-size="22" font-weight="bold" fill="white">RAZOR SHARK</text>'''
    },
    "buffalo-king": {
        "bg1": "#E65100", "bg2": "#BF360C",
        "elements": '''
    <!-- Prairie sunset -->
    <circle cx="150" cy="60" r="35" fill="#FFB74D" opacity="0.5"/>
    <!-- Buffalo -->
    <g transform="translate(100,90)">
      <!-- Body -->
      <ellipse cx="50" cy="30" rx="50" ry="28" fill="#4E342E"/>
      <!-- Hump -->
      <ellipse cx="25" cy="10" rx="25" ry="22" fill="#5D4037"/>
      <!-- Head -->
      <circle cx="0" cy="20" r="18" fill="#4E342E"/>
      <!-- Horns -->
      <path d="M-5,5 Q-20,-10 -15,-20" stroke="#D7CCC8" stroke-width="3" fill="none" stroke-linecap="round"/>
      <path d="M5,5 Q20,-10 15,-20" stroke="#D7CCC8" stroke-width="3" fill="none" stroke-linecap="round"/>
      <!-- Eye -->
      <circle cx="-5" cy="18" r="3" fill="white"/>
      <circle cx="-5" cy="18" r="1.5" fill="black"/>
      <!-- Nose -->
      <ellipse cx="0" cy="28" rx="6" ry="4" fill="#3E2723"/>
      <!-- Legs -->
      <rect x="25" y="55" width="8" height="25" rx="3" fill="#4E342E"/>
      <rect x="65" y="55" width="8" height="25" rx="3" fill="#4E342E"/>
    </g>
    <!-- Grass -->
    <path d="M0,180 Q50,170 100,180 Q150,170 200,180 Q250,170 300,180" stroke="#8BC34A" stroke-width="2" fill="none"/>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="serif" font-size="22" font-weight="bold" fill="#FFD700">BUFFALO KING</text>'''
    },
    "the-dog-house": {
        "bg1": "#1565C0", "bg2": "#0D47A1",
        "elements": '''
    <!-- Dog house -->
    <g transform="translate(105,60)">
      <polygon points="45,0 0,35 90,35" fill="#D32F2F"/>
      <rect x="10" y="35" width="70" height="55" fill="#F44336"/>
      <rect x="30" y="50" width="30" height="40" rx="15" fill="#3E2723"/>
      <!-- Bone above door -->
      <g transform="translate(45,42)">
        <rect x="-10" y="-2" width="20" height="4" rx="2" fill="#EFEBE9"/>
        <circle cx="-10" cy="0" r="3" fill="#EFEBE9"/>
        <circle cx="10" cy="0" r="3" fill="#EFEBE9"/>
      </g>
    </g>
    <!-- Dog face peeking out -->
    <g transform="translate(150,118)">
      <circle cx="0" cy="0" r="12" fill="#8D6E63"/>
      <ellipse cx="-4" cy="-2" rx="2.5" ry="3" fill="white"/>
      <ellipse cx="4" cy="-2" rx="2.5" ry="3" fill="white"/>
      <circle cx="-4" cy="-1.5" r="1.5" fill="#3E2723"/>
      <circle cx="4" cy="-1.5" r="1.5" fill="#3E2723"/>
      <ellipse cx="0" cy="4" rx="4" ry="3" fill="#5D4037"/>
      <circle cx="0" cy="3" r="2" fill="black"/>
      <path d="M-3,8 Q0,11 3,8" stroke="#5D4037" stroke-width="1" fill="none"/>
      <!-- Ears -->
      <ellipse cx="-12" cy="-5" rx="6" ry="10" fill="#6D4C41" transform="rotate(-15 -12 -5)"/>
      <ellipse cx="12" cy="-5" rx="6" ry="10" fill="#6D4C41" transform="rotate(15 12 -5)"/>
    </g>
    <!-- Paw prints -->
    <g transform="translate(60,160)" opacity="0.4" fill="white">
      <circle cx="0" cy="0" r="5"/><circle cx="-4" cy="-6" r="2.5"/><circle cx="4" cy="-6" r="2.5"/>
    </g>
    <g transform="translate(240,155)" opacity="0.3" fill="white">
      <circle cx="0" cy="0" r="5"/><circle cx="-4" cy="-6" r="2.5"/><circle cx="4" cy="-6" r="2.5"/>
    </g>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="sans-serif" font-size="20" font-weight="bold" fill="white">THE DOG HOUSE</text>'''
    },
    "dead-or-alive-2": {
        "bg1": "#795548", "bg2": "#4E342E",
        "elements": '''
    <!-- Desert sunset -->
    <circle cx="250" cy="50" r="30" fill="#FFB74D" opacity="0.4"/>
    <!-- Cactus -->
    <rect x="50" y="80" width="12" height="80" rx="6" fill="#2E7D32"/>
    <rect x="38" y="100" width="12" height="40" rx="6" fill="#388E3C" transform="rotate(-10 44 120)"/>
    <rect x="62" y="90" width="10" height="35" rx="5" fill="#388E3C" transform="rotate(10 67 107)"/>
    <!-- Wanted poster -->
    <g transform="translate(120,40)">
      <rect x="0" y="0" width="70" height="90" fill="#F5DEB3" rx="2"/>
      <rect x="3" y="3" width="64" height="84" fill="none" stroke="#8D6E63" stroke-width="1"/>
      <text x="35" y="18" text-anchor="middle" font-size="10" font-weight="bold" fill="#4E342E" font-family="serif">WANTED</text>
      <text x="35" y="30" text-anchor="middle" font-size="6" fill="#8D6E63">DEAD OR ALIVE</text>
      <rect x="15" y="35" width="40" height="30" fill="#D7CCC8"/>
      <text x="35" y="55" text-anchor="middle" font-size="14" fill="#4E342E">&#129312;</text>
      <text x="35" y="80" text-anchor="middle" font-size="8" font-weight="bold" fill="#4E342E">$10,000</text>
    </g>
    <!-- Crossed revolvers -->
    <g transform="translate(230,120)" opacity="0.7">
      <rect x="-20" y="-3" width="40" height="6" rx="2" fill="#9E9E9E" transform="rotate(30)"/>
      <rect x="-20" y="-3" width="40" height="6" rx="2" fill="#9E9E9E" transform="rotate(-30)"/>
    </g>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="serif" font-size="18" font-weight="bold" fill="#FFD700">DEAD OR ALIVE 2</text>'''
    },
    "da-vinci-diamonds": {
        "bg1": "#1A237E", "bg2": "#0D47A1",
        "elements": '''
    <!-- Diamond shapes -->
    <polygon points="150,30 180,80 150,130 120,80" fill="none" stroke="rgba(255,255,255,0.3)" stroke-width="2"/>
    <polygon points="150,40 172,80 150,120 128,80" fill="rgba(100,200,255,0.2)"/>
    <!-- Inner diamond facets -->
    <line x1="150" y1="40" x2="128" y2="80" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <line x1="150" y1="40" x2="172" y2="80" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <line x1="128" y1="80" x2="150" y2="120" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <line x1="172" y1="80" x2="150" y2="120" stroke="rgba(255,255,255,0.2)" stroke-width="1"/>
    <line x1="128" y1="80" x2="172" y2="80" stroke="rgba(255,255,255,0.15)" stroke-width="1"/>
    <!-- Small diamonds -->
    <polygon points="60,100 75,120 60,140 45,120" fill="rgba(255,50,50,0.3)" stroke="#E57373" stroke-width="1"/>
    <polygon points="240,90 255,110 240,130 225,110" fill="rgba(50,255,50,0.3)" stroke="#81C784" stroke-width="1"/>
    <!-- Mona Lisa frame -->
    <rect x="70" y="50" width="30" height="40" fill="#5D4037" rx="2"/>
    <rect x="73" y="53" width="24" height="34" fill="#BCAAA4"/>
    <text x="85" y="77" text-anchor="middle" font-size="18">&#128444;</text>
    <!-- Sparkles -->
    <text x="190" y="60" font-size="12" fill="#64B5F6">&#10022;</text>
    <text x="100" y="140" font-size="10" fill="#E57373">&#10022;</text>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="serif" font-size="17" font-weight="bold" fill="white">DA VINCI DIAMONDS</text>'''
    },
    "bonanza-billion": {
        "bg1": "#F57F17", "bg2": "#E65100",
        "elements": '''
    <!-- Mining theme -->
    <!-- Mountain/mine entrance -->
    <polygon points="80,170 150,50 220,170" fill="rgba(0,0,0,0.2)"/>
    <rect x="120" y="110" width="60" height="60" rx="5" fill="#3E2723"/>
    <rect x="125" y="115" width="50" height="55" fill="#1A1A1A"/>
    <!-- Mine cart -->
    <g transform="translate(150,145)">
      <polygon points="-20,0 20,0 15,-15 -15,-15" fill="#757575"/>
      <circle cx="-12" cy="5" r="5" fill="#424242" stroke="#616161" stroke-width="1"/>
      <circle cx="12" cy="5" r="5" fill="#424242" stroke="#616161" stroke-width="1"/>
      <!-- Gold in cart -->
      <circle cx="-5" cy="-8" r="5" fill="#FFD700"/>
      <circle cx="5" cy="-10" r="5" fill="#FFD700"/>
      <circle cx="0" cy="-5" r="5" fill="#FFC107"/>
    </g>
    <!-- Gems -->
    <polygon points="60,80 70,65 80,80 70,95" fill="#E040FB" opacity="0.7"/>
    <polygon points="230,70 240,55 250,70 240,85" fill="#00E5FF" opacity="0.7"/>
    <polygon points="250,130 258,120 266,130 258,140" fill="#76FF03" opacity="0.7"/>
    <!-- Dynamite -->
    <rect x="50" y="130" width="8" height="30" rx="2" fill="#F44336"/>
    <line x1="54" y1="130" x2="54" y2="120" stroke="#FFC107" stroke-width="1.5"/>
    <circle cx="54" cy="118" r="4" fill="#FF6D00" opacity="0.8"/>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="sans-serif" font-size="19" font-weight="bold" fill="white">BONANZA BILLION</text>'''
    },
    "big-bass-splash": {
        "bg1": "#0277BD", "bg2": "#01579B",
        "elements": '''
    <!-- Water splash -->
    <path d="M70,100 Q80,70 100,85 Q110,60 130,80 Q140,50 160,75 Q170,55 190,80 Q200,60 220,85 Q230,70 240,100" stroke="rgba(255,255,255,0.4)" stroke-width="2" fill="none"/>
    <!-- Splash drops -->
    <ellipse cx="90" cy="55" rx="4" ry="7" fill="rgba(255,255,255,0.3)"/>
    <ellipse cx="160" cy="40" rx="3" ry="6" fill="rgba(255,255,255,0.25)"/>
    <ellipse cx="210" cy="50" rx="3.5" ry="6" fill="rgba(255,255,255,0.2)"/>
    <!-- Fish jumping -->
    <g transform="translate(150,90) rotate(-30)">
      <ellipse cx="0" cy="0" rx="30" ry="15" fill="#4CAF50"/>
      <polygon points="25,-10 45,0 25,10" fill="#388E3C"/>
      <circle cx="-15" cy="-3" r="3" fill="white"/>
      <circle cx="-15" cy="-3" r="1.5" fill="#1B5E20"/>
      <text x="0" y="5" font-size="12" font-weight="bold" fill="#FFD700" text-anchor="middle">$</text>
    </g>
    <!-- Fishing reel -->
    <circle cx="60" cy="150" r="18" fill="none" stroke="#BDBDBD" stroke-width="2"/>
    <circle cx="60" cy="150" r="8" fill="#757575"/>
    <line x1="78" y1="150" x2="120" y2="100" stroke="#BDBDBD" stroke-width="1.5"/>
    <!-- More fish -->
    <g transform="translate(230,140)">
      <ellipse cx="0" cy="0" rx="18" ry="10" fill="#FF9800"/>
      <polygon points="15,-6 25,0 15,6" fill="#F57C00"/>
    </g>
    <!-- Title -->
    <text x="150" y="210" text-anchor="middle" font-family="sans-serif" font-size="19" font-weight="bold" fill="white">BIG BASS SPLASH</text>'''
    },
}

for name, data in slots.items():
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 230">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{data["bg1"]}"/>
      <stop offset="100%" stop-color="{data["bg2"]}"/>
    </linearGradient>
  </defs>
  <rect width="300" height="230" rx="12" fill="url(#bg)"/>
  {data["elements"]}
</svg>'''
    
    filepath = f"slots/{name}.svg"
    with open(filepath, 'w') as f:
        f.write(svg)
    print(f"Created {filepath}")

print(f"\nTotal: {len(slots)} slot images created")
