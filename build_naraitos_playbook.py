# Python script to build the complete, production-grade Naraito's Playbook single-page application
import os

with open(r'D:\us-remote-engineering-playbook\curated_leads.js', 'r', encoding='utf-8') as f:
    curated_leads_content = f.read()

with open(r'D:\us-remote-engineering-playbook\app.js', 'r', encoding='utf-8') as f:
    app_js_content = f.read()

html_content = f"""<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Naraito's Playbook | Mastering US Remote Engineering Jobs</title>
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      darkMode: 'class',
      theme: {{
        extend: {{
          colors: {{
            brand: {{
              50: '#f5f3ff',
              100: '#ede9fe',
              400: '#818cf8',
              500: '#6C63FF', // Primary Accent
              600: '#584fe6',
              700: '#4338ca',
            }},
            teal: {{
              400: '#2dd4bf',
              500: '#00D4AA', // Secondary Accent
              600: '#0d9488',
            }},
            bg: {{
              dark: '#0A0A0F',
              surface: '#13131A',
              card: '#1C1C27',
              border: '#2A2A3A',
              muted: '#8888A8',
            }}
          }},
          fontFamily: {{
            sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
            heading: ['Space Grotesk', 'Inter', 'sans-serif'],
            mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
          }}
        }}
      }}
    }}
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <!-- Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

  <!-- Google Fonts: Space Grotesk & Inter & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

  <style>
    /* Baseline 8px Typography & Layout System */
    :root {{
      --bg-dark: #0A0A0F;
      --bg-surface: #13131A;
      --bg-card: #1C1C27;
      --border-subtle: #2A2A3A;
      --text-muted: #8888A8;
      --accent-primary: #6C63FF;
      --accent-secondary: #00D4AA;
    }}

    body {{
      background-color: var(--bg-dark);
      color: #F1F1F5;
      font-family: 'Inter', sans-serif;
      font-feature-settings: "cv02", "cv03", "cv04", "cv11";
    }}

    h1, h2, h3, h4, .font-heading {{
      font-family: 'Space Grotesk', sans-serif;
    }}

    /* Custom Scrollbar */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: #0A0A0F;
    }}
    ::-webkit-scrollbar-thumb {{
      background: #2A2A3A;
      border-radius: 4px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #6C63FF;
    }}

    /* Line Length Constraint for Readability */
    p, li, .text-prose {{
      max-width: 76ch;
    }}

    /* Clean Card Surfaces */
    .card-surface {{
      background: #1C1C27;
      border: 1px solid #2A2A3A;
      border-radius: 0.75rem;
      transition: border-color 0.2s ease, transform 0.2s ease;
    }}
    .card-surface:hover {{
      border-color: rgba(108, 99, 255, 0.4);
    }}

    /* Pill Navigation Links */
    .nav-pill {{
      transition: all 0.15s ease;
      white-space: nowrap;
    }}
    .nav-pill:hover {{
      color: #FFFFFF;
      background: #1C1C27;
      border-color: #6C63FF;
    }}
    .nav-pill.active {{
      background: #6C63FF;
      color: #FFFFFF;
      font-weight: 600;
      border-color: #6C63FF;
    }}

    /* Interactive Tab Buttons */
    .tab-btn {{
      transition: all 0.15s ease-in-out;
    }}

    /* Table Styles */
    table th, table td {{
      border-bottom: 1px solid #2A2A3A;
    }}
    tr:last-child td {{
      border-bottom: none;
    }}

    /* Form Controls */
    input[type="range"]::-webkit-slider-thumb {{
      appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #6C63FF;
      cursor: pointer;
    }}

    /* Reduced Motion */
    @media (prefers-reduced-motion: reduce) {{
      * {{
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }}
    }}
  </style>
</head>
<body class="bg-[#0A0A0F] text-[#F1F1F5] min-h-screen flex flex-col antialiased selection:bg-[#6C63FF] selection:text-white">

  <!-- TOP HEADER / BRAND & GLOBAL ACTIONS -->
  <header class="sticky top-0 z-50 bg-[#0A0A0F]/95 backdrop-blur-md border-b border-[#2A2A3A]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between gap-4">
      
      <!-- Brand / Logo -->
      <div class="flex items-center gap-3 shrink-0">
        <a href="#start-here" class="flex items-center gap-2.5 group">
          <div class="w-8 h-8 rounded-lg bg-[#6C63FF] flex items-center justify-center font-heading font-bold text-white shadow-sm">
            N
          </div>
          <div>
            <div class="font-heading font-bold text-sm sm:text-base text-white flex items-center gap-2">
              Naraito's Playbook
              <span class="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded bg-[#6C63FF]/20 text-[#6C63FF] border border-[#6C63FF]/30 font-medium">0 EXP EDITION</span>
            </div>
            <p class="text-[11px] text-[#8888A8] hidden sm:block">Mastering US Remote Engineering Jobs ($60K–$120K)</p>
          </div>
        </a>
      </div>

      <!-- Quick Actions, Audio & Progress -->
      <div class="flex items-center gap-3 sm:gap-5">
        
        <!-- Overall Roadmap Progress -->
        <div class="flex items-center gap-2.5">
          <div class="text-right hidden md:block">
            <div class="text-[10px] uppercase font-mono text-[#8888A8]">Roadmap Progress</div>
            <div id="header-progress-text" class="text-xs font-mono font-bold text-[#00D4AA]">0% (0/24 tasks)</div>
          </div>
          <div class="w-20 sm:w-28 bg-[#13131A] h-2 rounded-full overflow-hidden border border-[#2A2A3A]">
            <div id="header-progress-bar" class="bg-[#00D4AA] h-full rounded-full transition-all duration-500" style="width: 0%"></div>
          </div>
        </div>

        <!-- Sound FX toggle button -->
        <button id="audio-toggle-btn" onclick="toggleAudio()" title="Sound Effects" class="p-2 text-[#8888A8] hover:text-white rounded-lg hover:bg-[#1C1C27] border border-[#2A2A3A] transition">
          <i data-lucide="volume-2" class="w-4 h-4" id="audio-icon"></i>
        </button>

        <!-- Data & CRM Backup Modal Button -->
        <button onclick="openBackupModal()" class="px-3 py-1.5 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-white text-xs font-medium flex items-center gap-1.5 transition">
          <i data-lucide="hard-drive" class="w-3.5 h-3.5 text-[#6C63FF]"></i>
          <span class="hidden sm:inline">Data & CRM</span>
        </button>

        <!-- Reset All Data -->
        <button onclick="resetAllData()" title="Reset Local Data" class="px-2.5 py-1.5 rounded-lg bg-[#1C1C27] hover:bg-red-500/20 hover:text-red-400 border border-[#2A2A3A] text-[#8888A8] text-xs font-medium transition flex items-center gap-1">
          <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i>
          <span class="hidden lg:inline">Reset</span>
        </button>

      </div>
    </div>

    <!-- STICKY TOP PILL NAVIGATION BAR -->
    <div class="border-t border-[#2A2A3A] bg-[#13131A]/90 backdrop-blur-md overflow-x-auto scrollbar-none py-2 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto flex items-center gap-2">
        <a href="#start-here" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Start Here</a>
        <a href="#roadmap-90" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">90-Day Roadmap</a>
        <a href="#filters" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">5 Filters</a>
        <a href="#reality-check" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Reality Check</a>
        <a href="#roadmap" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Execution Roadmap</a>
        <a href="#projects" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Projects</a>
        <a href="#offer" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Offer Framework</a>
        <a href="#linkedin" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">LinkedIn Studio</a>
        <a href="#outreach" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Outreach CRM</a>
        <a href="#job-search" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Job Search Engine</a>
        <a href="#courses" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Free Courses</a>
        <a href="#resources" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Resources</a>
        <a href="#final-checklist" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Final Checklist</a>
      </div>
    </div>
  </header>

  <!-- MAIN PLAYBOOK CONTENT -->
  <main class="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-16">

    <!-- ========================================== -->
    <!-- SECTION 1: START HERE (HERO & ARBITRAGE) -->
    <!-- ========================================== -->
    <section id="start-here" class="space-y-8 scroll-mt-32">
      
      <!-- Hero Headline & Value Proposition -->
      <div class="space-y-4 max-w-4xl">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
          <span class="w-2 h-2 rounded-full bg-[#00D4AA] animate-pulse"></span>
          THE 0-EXPERIENCE US REMOTE PLAYBOOK
        </div>
        <h1 class="text-3xl sm:text-5xl font-extrabold tracking-tight text-white leading-tight font-heading">
          Land a <span class="text-[#6C63FF]">$60K–$120K</span> Remote US Engineering Role From Anywhere in the World
        </h1>
        <p class="text-base sm:text-lg text-[#8888A8] text-prose leading-relaxed">
          A battle-tested blueprint for international engineers to bypass traditional credential gates, build high-signal proof of work, and close high-paying US startup contracts.
        </p>
        
        <!-- Key Quick Badges -->
        <div class="flex flex-wrap gap-2.5 pt-2">
          <span class="px-3 py-1 rounded-lg bg-[#13131A] border border-[#2A2A3A] text-xs text-slate-300 flex items-center gap-1.5">
            <i data-lucide="dollar-sign" class="w-3.5 h-3.5 text-[#00D4AA]"></i> $60K–$120K / yr Base Rate
          </span>
          <span class="px-3 py-1 rounded-lg bg-[#13131A] border border-[#2A2A3A] text-xs text-slate-300 flex items-center gap-1.5">
            <i data-lucide="clock" class="w-3.5 h-3.5 text-[#6C63FF]"></i> 4-Hour Timezone Overlap
          </span>
          <span class="px-3 py-1 rounded-lg bg-[#13131A] border border-[#2A2A3A] text-xs text-slate-300 flex items-center gap-1.5">
            <i data-lucide="zap" class="w-3.5 h-3.5 text-amber-400"></i> 100% Async-First Delivery
          </span>
          <span class="px-3 py-1 rounded-lg bg-[#13131A] border border-[#2A2A3A] text-xs text-slate-300 flex items-center gap-1.5">
            <i data-lucide="globe" class="w-3.5 h-3.5 text-sky-400"></i> 0 US Visa Required (W-8BEN)
          </span>
        </div>
      </div>

      <!-- Interactive Dynamic Arbitrage Calculator -->
      <div class="card-surface p-6 sm:p-8 space-y-6 bg-[#13131A]">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-[#2A2A3A] pb-4">
          <div>
            <h2 class="text-lg font-bold text-white font-heading flex items-center gap-2">
              <i data-lucide="calculator" class="w-5 h-5 text-[#6C63FF]"></i>
              Geographic Wealth Arbitrage Calculator
            </h2>
            <p class="text-xs text-[#8888A8]">Model your real take-home savings by earning in USD while living in a high-purchasing-power country.</p>
          </div>
          <div class="font-mono text-xs text-[#00D4AA] bg-[#1C1C27] px-3 py-1 rounded-md border border-[#2A2A3A]">
            Real-Time Modeling
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <!-- Sliders Controls -->
          <div class="space-y-6">
            <div class="space-y-2">
              <div class="flex justify-between text-xs">
                <span class="text-slate-300 font-medium">Target US Contractor Rate (Hourly):</span>
                <span id="rate-val" class="font-mono font-bold text-[#00D4AA] text-sm">$45 / hr ($93,600/yr)</span>
              </div>
              <input type="range" id="rate-slider" min="25" max="100" step="5" value="45" oninput="updateArbitrageCalculator()" class="w-full bg-[#1C1C27] rounded-lg h-2 accent-[#6C63FF] cursor-pointer">
              <div class="flex justify-between text-[10px] text-[#8888A8]">
                <span>$25/hr ($52K)</span>
                <span>$50/hr ($104K)</span>
                <span>$100/hr ($208K)</span>
              </div>
            </div>

            <div class="space-y-2">
              <div class="flex justify-between text-xs">
                <span class="text-slate-300 font-medium">Your Monthly In-Country Cost of Living:</span>
                <span id="cost-val" class="font-mono font-bold text-amber-400 text-sm">$800 / mo ($9,600/yr)</span>
              </div>
              <input type="range" id="cost-slider" min="400" max="3000" step="100" value="800" oninput="updateArbitrageCalculator()" class="w-full bg-[#1C1C27] rounded-lg h-2 accent-[#00D4AA] cursor-pointer">
              <div class="flex justify-between text-[10px] text-[#8888A8]">
                <span>$400/mo (Frugal)</span>
                <span>$1,200/mo (Upper Middle)</span>
                <span>$3,000/mo (High Luxury)</span>
              </div>
            </div>
          </div>

          <!-- Dynamic Results Summary -->
          <div class="grid grid-cols-2 gap-4">
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="text-[11px] text-[#8888A8]">Gross Annual USD</div>
              <div id="annual-us-val" class="text-lg sm:text-xl font-bold font-mono text-white">$93,600</div>
              <div class="text-[10px] text-slate-400">@ 40 hrs/wk contractor</div>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="text-[11px] text-[#8888A8]">Annual Local Living Cost</div>
              <div id="annual-local-val" class="text-lg sm:text-xl font-bold font-mono text-amber-400">$9,600</div>
              <div class="text-[10px] text-slate-400">100% comfortable lifestyle</div>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#00D4AA]/40 space-y-1">
              <div class="text-[11px] text-[#00D4AA] font-semibold">Net Liquid Annual Savings</div>
              <div id="annual-savings-val" class="text-lg sm:text-xl font-bold font-mono text-[#00D4AA]">$74,640</div>
              <div class="text-[10px] text-slate-400">~80% savings rate (after tax)</div>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#6C63FF]/40 space-y-1">
              <div class="text-[11px] text-[#6C63FF] font-semibold">Wealth Multiplier</div>
              <div id="multiplier-val" class="text-lg sm:text-xl font-bold font-mono text-[#6C63FF]">9.7x</div>
              <div class="text-[10px] text-slate-400">vs local median dev salary</div>
            </div>
          </div>
        </div>

        <!-- 3-Column Cost Comparison Cards Side by Side -->
        <div class="pt-4 border-t border-[#2A2A3A] space-y-3">
          <div class="text-xs font-mono uppercase tracking-wider text-[#8888A8]">Geographic Reality Comparison</div>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            
            <!-- San Francisco Card -->
            <div class="p-4 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] space-y-2">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-slate-300">San Francisco / NYC</span>
                <span class="text-[10px] font-mono text-red-400 px-1.5 py-0.5 rounded bg-red-500/10">High Burn</span>
              </div>
              <div class="text-xs space-y-1 text-slate-400">
                <div class="flex justify-between"><span>Gross Salary:</span> <span class="font-mono text-slate-200">$150,000</span></div>
                <div class="flex justify-between"><span>Rent & Living:</span> <span class="font-mono text-red-400">-$54,000</span></div>
                <div class="flex justify-between"><span>US Fed & State Tax:</span> <span class="font-mono text-red-400">-$45,000</span></div>
                <div class="flex justify-between pt-1 border-t border-[#2A2A3A] font-bold text-slate-200">
                  <span>Net Annual Savings:</span>
                  <span class="font-mono text-amber-400">~$30,000</span>
                </div>
              </div>
            </div>

            <!-- Austin / US Remote Card -->
            <div class="p-4 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] space-y-2">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-slate-300">Austin / US Remote</span>
                <span class="text-[10px] font-mono text-amber-400 px-1.5 py-0.5 rounded bg-amber-500/10">Moderate Burn</span>
              </div>
              <div class="text-xs space-y-1 text-slate-400">
                <div class="flex justify-between"><span>Gross Salary:</span> <span class="font-mono text-slate-200">$120,000</span></div>
                <div class="flex justify-between"><span>Rent & Living:</span> <span class="font-mono text-amber-400">-$36,000</span></div>
                <div class="flex justify-between"><span>US Fed Tax:</span> <span class="font-mono text-amber-400">-$28,000</span></div>
                <div class="flex justify-between pt-1 border-t border-[#2A2A3A] font-bold text-slate-200">
                  <span>Net Annual Savings:</span>
                  <span class="font-mono text-amber-400">~$42,000</span>
                </div>
              </div>
            </div>

            <!-- India / LatAm / Global Remote Card (YOU) -->
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#00D4AA]/50 space-y-2 relative overflow-hidden">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-[#00D4AA]">Global Remote (YOU)</span>
                <span class="text-[10px] font-mono text-[#00D4AA] px-1.5 py-0.5 rounded bg-[#00D4AA]/10">Maximum Arbitrage</span>
              </div>
              <div class="text-xs space-y-1 text-slate-400">
                <div class="flex justify-between"><span>Gross Rate ($40/hr):</span> <span class="font-mono text-slate-200">$83,200</span></div>
                <div class="flex justify-between"><span>Local Luxury Living:</span> <span class="font-mono text-emerald-400">-$9,600</span></div>
                <div class="flex justify-between"><span>Local Taxes (44ADA):</span> <span class="font-mono text-emerald-400">-$8,500</span></div>
                <div class="flex justify-between pt-1 border-t border-[#2A2A3A] font-bold text-[#00D4AA]">
                  <span>Net Annual Savings:</span>
                  <span class="font-mono text-base text-[#00D4AA]">~$65,100</span>
                </div>
              </div>
            </div>

          </div>
        </div>

        <!-- Insight Quote Callout -->
        <div class="p-4 rounded-xl bg-[#1C1C27] border-l-4 border-[#6C63FF] text-xs sm:text-sm text-slate-300 leading-relaxed italic">
          "The goal is not just a high US salary. The goal is geographic arbitrage: earn in strong USD, live in high purchasing power, and save 70%+ of your income while building world-class engineering chops."
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 2: YOUR 90-DAY ROADMAP (NEW) -->
    <!-- ========================================== -->
    <section id="roadmap-90" class="space-y-6 scroll-mt-32">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#6C63FF]">
          <i data-lucide="calendar" class="w-3.5 h-3.5"></i> STRUCTURED 90-DAY TIMELINE
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          Your 90-Day Step-by-Step AI Roadmap
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          A day-by-day structured curriculum to take you from foundational Python to landing high-paying US remote roles.
        </p>
      </div>

      <!-- 3 Phase Cards Grid -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        <!-- Phase 1: Days 1–30 Foundations -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-4">
            <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
              <div>
                <span class="text-xs font-mono font-semibold text-[#6C63FF]">PHASE 1 (DAYS 1–30)</span>
                <h3 class="text-base font-bold text-white font-heading">Foundations (Weeks 1–4)</h3>
              </div>
              <span class="text-xs px-2 py-0.5 rounded bg-[#6C63FF]/20 text-[#6C63FF] font-mono">Weeks 1–4</span>
            </div>

            <div class="space-y-3 text-xs text-slate-300">
              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-semibold text-white">Day 1–7: Python Mastery & Data Structures</div>
                <div class="text-[11px] text-[#8888A8]">OOP, generators, decorators, time complexity & algorithmic problem solving.</div>
              </div>

              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-semibold text-white">Day 8–14: Math for AI</div>
                <div class="text-[11px] text-[#8888A8]">Linear algebra (vectors, dot products, matrix math), calculus gradients, probability & statistics.</div>
              </div>

              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-semibold text-white">Day 15–21: Data Handling & SQL</div>
                <div class="text-[11px] text-[#8888A8]">Pandas, NumPy, data cleaning, advanced SQL queries, joins, aggregations, window functions.</div>
              </div>

              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-semibold text-white">Day 22–30: Git, APIs & Cloud Basics</div>
                <div class="text-[11px] text-[#8888A8]">FastAPI, RESTful APIs, Git branching workflows, Docker containers, cloud setup on AWS/GCP.</div>
              </div>
            </div>
          </div>

          <!-- Required Outputs Checkboxes -->
          <div class="pt-4 border-t border-[#2A2A3A] space-y-2">
            <div class="text-[11px] font-mono uppercase text-[#6C63FF] font-semibold">Required Outputs:</div>
            <div class="space-y-2 text-xs">
              <label class="flex items-start gap-2.5 cursor-pointer">
                <input type="checkbox" id="nr-1" onchange="toggle90DayItem('phase1', 'nr-1')" class="mt-0.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-[#6C63FF] focus:ring-[#6C63FF]">
                <span class="text-slate-300">One Python API project</span>
              </label>
              <label class="flex items-start gap-2.5 cursor-pointer">
                <input type="checkbox" id="nr-2" onchange="toggle90DayItem('phase1', 'nr-2')" class="mt-0.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-[#6C63FF] focus:ring-[#6C63FF]">
                <span class="text-slate-300">One data analysis project</span>
              </label>
              <label class="flex items-start gap-2.5 cursor-pointer">
                <input type="checkbox" id="nr-3" onchange="toggle90DayItem('phase1', 'nr-3')" class="mt-0.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-[#6C63FF] focus:ring-[#6C63FF]">
                <span class="text-slate-300">Updated GitHub profile</span>
              </label>
            </div>
          </div>
        </div>

        <!-- Phase 2: Days 31–60 ML & Applied AI -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-4">
            <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
              <div>
                <span class="text-xs font-mono font-semibold text-[#00D4AA]">PHASE 2 (DAYS 31–60)</span>
                <h3 class="text-base font-bold text-white font-heading">ML & Applied AI (Weeks 5–8)</h3>
              </div>
              <span class="text-xs px-2 py-0.5 rounded bg-[#00D4AA]/20 text-[#00D4AA] font-mono">Weeks 5–8</span>
            </div>

            <div class="space-y-3 text-xs text-slate-300">
              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-semibold text-white">Day 31–38: Classic Machine Learning</div>
                <div class="text-[11px] text-[#8888A8]">Linear/Logistic regression, Decision Trees, Random Forests, XGBoost, Scikit-Learn pipelines.</div>
              </div>

              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-semibold text-white">Day 39–45: Deep Learning & PyTorch</div>
                <div class="text-[11px] text-[#8888A8]">Neural networks, backpropagation, CNNs, Transformers, attention mechanisms, PyTorch training loops.</div>
              </div>

              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-semibold text-white">Day 46–52: LLMs, RAG & Vector DBs</div>
                <div class="text-[11px] text-[#8888A8]">LangChain, LlamaIndex, ChromaDB/Qdrant, embeddings, semantic search, hybrid retrieval.</div>
              </div>

              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-semibold text-white">Day 53–60: Agentic AI & Tool Calling</div>
                <div class="text-[11px] text-[#8888A8]">CrewAI, LangGraph, autonomous agents, tool integration, function calling, structured outputs.</div>
              </div>
            </div>
          </div>

          <!-- Required Outputs Checkboxes -->
          <div class="pt-4 border-t border-[#2A2A3A] space-y-2">
            <div class="text-[11px] font-mono uppercase text-[#00D4AA] font-semibold">Required Outputs:</div>
            <div class="space-y-2 text-xs">
              <label class="flex items-start gap-2.5 cursor-pointer">
                <input type="checkbox" id="nr-4" onchange="toggle90DayItem('phase2', 'nr-4')" class="mt-0.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-[#00D4AA] focus:ring-[#00D4AA]">
                <span class="text-slate-300">One deployed machine learning project</span>
              </label>
              <label class="flex items-start gap-2.5 cursor-pointer">
                <input type="checkbox" id="nr-5" onchange="toggle90DayItem('phase2', 'nr-5')" class="mt-0.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-[#00D4AA] focus:ring-[#00D4AA]">
                <span class="text-slate-300">One basic RAG application</span>
              </label>
              <label class="flex items-start gap-2.5 cursor-pointer">
                <input type="checkbox" id="nr-6" onchange="toggle90DayItem('phase2', 'nr-6')" class="mt-0.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-[#00D4AA] focus:ring-[#00D4AA]">
                <span class="text-slate-300">First version of your resume</span>
              </label>
            </div>
          </div>
        </div>

        <!-- Phase 3: Days 61–90 Proof, Network & Apply -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-4">
            <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
              <div>
                <span class="text-xs font-mono font-semibold text-amber-400">PHASE 3 (DAYS 61–90)</span>
                <h3 class="text-base font-bold text-white font-heading">Proof, Network & Apply (Weeks 9–12)</h3>
              </div>
              <span class="text-xs px-2 py-0.5 rounded bg-amber-500/20 text-amber-400 font-mono">Weeks 9–12</span>
            </div>

            <div class="space-y-3 text-xs text-slate-300">
              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-semibold text-white">Day 61–68: Production-Grade Capstone</div>
                <div class="text-[11px] text-[#8888A8]">Full-stack AI app, Streamlit/FastAPI, Docker container, cloud hosting, public health check.</div>
              </div>

              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-semibold text-white">Day 69–75: Personal Brand & LinkedIn</div>
                <div class="text-[11px] text-[#8888A8]">16 headline formulas, 5-block About, 3-slot Featured section, 3x/week build-in-public schedule.</div>
              </div>

              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-semibold text-white">Day 76–82: Cold Outreach & Job Search</div>
                <div class="text-[11px] text-[#8888A8]">The 5-5-5 daily application system, cold DMs, recruiter outreach, Boolean search strings.</div>
              </div>

              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-semibold text-white">Day 83–90: Interview Prep & Closing</div>
                <div class="text-[11px] text-[#8888A8]">System design, technical coding, behavioral STAR method, live project teardowns, contract negotiation.</div>
              </div>
            </div>
          </div>

          <!-- Required Outputs Checkboxes -->
          <div class="pt-4 border-t border-[#2A2A3A] space-y-2">
            <div class="text-[11px] font-mono uppercase text-amber-400 font-semibold">Required Outputs:</div>
            <div class="space-y-2 text-xs">
              <label class="flex items-start gap-2.5 cursor-pointer">
                <input type="checkbox" id="nr-7" onchange="toggle90DayItem('phase3', 'nr-7')" class="mt-0.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-amber-400 focus:ring-amber-400">
                <span class="text-slate-300">One production-style AI project</span>
              </label>
              <label class="flex items-start gap-2.5 cursor-pointer">
                <input type="checkbox" id="nr-8" onchange="toggle90DayItem('phase3', 'nr-8')" class="mt-0.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-amber-400 focus:ring-amber-400">
                <span class="text-slate-300">Three pinned GitHub repositories</span>
              </label>
              <label class="flex items-start gap-2.5 cursor-pointer">
                <input type="checkbox" id="nr-9" onchange="toggle90DayItem('phase3', 'nr-9')" class="mt-0.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-amber-400 focus:ring-amber-400">
                <span class="text-slate-300">Updated LinkedIn profile</span>
              </label>
              <label class="flex items-start gap-2.5 cursor-pointer">
                <input type="checkbox" id="nr-10" onchange="toggle90DayItem('phase3', 'nr-10')" class="mt-0.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-amber-400 focus:ring-amber-400">
                <span class="text-slate-300">Live portfolio</span>
              </label>
              <label class="flex items-start gap-2.5 cursor-pointer">
                <input type="checkbox" id="nr-11" onchange="toggle90DayItem('phase3', 'nr-11')" class="mt-0.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-amber-400 focus:ring-amber-400">
                <span class="text-slate-300">Application tracker</span>
              </label>
              <label class="flex items-start gap-2.5 cursor-pointer">
                <input type="checkbox" id="nr-12" onchange="toggle90DayItem('phase3', 'nr-12')" class="mt-0.5 rounded bg-[#0A0A0F] border-[#2A2A3A] text-amber-400 focus:ring-amber-400">
                <span class="text-slate-300">Consistent weekly applications</span>
              </label>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 3: THE 5 FILTERS (MODULE 1) -->
    <!-- ========================================== -->
    <section id="filters" class="space-y-6 scroll-mt-32">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
          <i data-lucide="shield-check" class="w-3.5 h-3.5"></i> MODULE 1: ELIMINATE HIRING FRICTION
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          The 5 Non-Negotiable Filters US Founders Screen For
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          US startups don't reject international talent over technical knowledge — they reject them when they fail these 5 operational filters.
        </p>
      </div>

      <!-- 5 Filter Comparison Cards -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        
        <!-- Filter 1 -->
        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="flex items-center gap-2 text-[#6C63FF] font-semibold text-xs font-mono">
            <span>FILTER 01</span>
          </div>
          <h3 class="text-sm font-bold text-white font-heading">Asynchronous Written Communication</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Write structured, concise updates (BLUF method). No rambling messages. US founders judge seniority by the clarity of your Slack messages and PR descriptions.
          </p>
        </div>

        <!-- Filter 2 -->
        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="flex items-center gap-2 text-[#00D4AA] font-semibold text-xs font-mono">
            <span>FILTER 02</span>
          </div>
          <h3 class="text-sm font-bold text-white font-heading">Technical Autonomy & Debugging Velocity</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Zero ticket-taking mindset. Unblock yourself independently using logs, telemetry, and docs before asking founders questions.
          </p>
        </div>

        <!-- Filter 3 -->
        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="flex items-center gap-2 text-amber-400 font-semibold text-xs font-mono">
            <span>FILTER 03</span>
          </div>
          <h3 class="text-sm font-bold text-white font-heading">4-Hour Timezone Overlap Discipline</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Guarantee a strict 4-hour daily overlap block with US EST or PST business hours (e.g. 7 AM–11 AM EST or 8 PM–12 AM IST).
          </p>
        </div>

        <!-- Filter 4 -->
        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="flex items-center gap-2 text-sky-400 font-semibold text-xs font-mono">
            <span>FILTER 04</span>
          </div>
          <h3 class="text-sm font-bold text-white font-heading">Business Context & ROI Alignment</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Think like a CFO. Know the cost-per-inference of your ML models, server bills, and how your code saves company cash runway.
          </p>
        </div>

        <!-- Filter 5 -->
        <div class="card-surface p-5 space-y-2 bg-[#13131A] md:col-span-2 lg:col-span-2">
          <div class="flex items-center gap-2 text-rose-400 font-semibold text-xs font-mono">
            <span>FILTER 05</span>
          </div>
          <h3 class="text-sm font-bold text-white font-heading">Executive Audio/Video Hygiene & Presence</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            1080p camera at eye level, soft front lighting, zero background echo/noise (Krisp/dedicated mic), direct eye contact into the lens. Disqualification happens in the first 30 seconds of video.
          </p>
        </div>

      </div>

      <!-- Diagnostic 5-Question Audit Tool & Camera/Mic Tester -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        <!-- 5-Question Audit Tool (8 Cols) -->
        <div class="card-surface p-6 space-y-6 bg-[#13131A] lg:col-span-7">
          <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
            <div>
              <h3 class="text-base font-bold text-white font-heading flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-4 h-4 text-[#00D4AA]"></i>
                5-Question Remote Readiness Audit
              </h3>
              <p class="text-xs text-[#8888A8]">Test how a US venture-backed founder would evaluate your behavioral instinct.</p>
            </div>
            <div id="audit-score-badge" class="font-mono text-xs text-[#00D4AA] bg-[#1C1C27] px-2.5 py-1 rounded border border-[#2A2A3A]">
              Score: 0/100
            </div>
          </div>

          <div id="audit-questions-container" class="space-y-6">
            <!-- Questions rendered via JS -->
          </div>

          <div class="pt-4 border-t border-[#2A2A3A] flex items-center justify-between">
            <button onclick="resetAudit()" class="text-xs text-[#8888A8] hover:text-white flex items-center gap-1.5 transition">
              <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i> Retake Audit
            </button>
            <div id="audit-feedback-summary" class="text-xs font-medium text-slate-300"></div>
          </div>
        </div>

        <!-- Live Camera & Mic WebRTC Tester (5 Cols) -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A] lg:col-span-5 flex flex-col justify-between">
          <div class="space-y-2">
            <h3 class="text-base font-bold text-white font-heading flex items-center gap-2">
              <i data-lucide="video" class="w-4 h-4 text-[#6C63FF]"></i>
              Live Video & Audio Hygiene Tester
            </h3>
            <p class="text-xs text-[#8888A8]">Test your webcam framing, eye-level angle, and microphone input level in real-time.</p>
          </div>

          <!-- Video Stream Container -->
          <div class="relative w-full aspect-video rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] overflow-hidden flex items-center justify-center">
            <video id="webcam-video" autoplay playsinline muted class="w-full h-full object-cover hidden"></video>
            <div id="webcam-placeholder" class="text-center p-4 space-y-2">
              <i data-lucide="camera" class="w-8 h-8 text-[#8888A8] mx-auto"></i>
              <p class="text-xs text-[#8888A8]">Camera stream is currently inactive.</p>
            </div>
            <div id="camera-active-badge" class="hidden absolute top-2 right-2 px-2 py-0.5 rounded bg-red-500/80 text-white text-[10px] font-mono flex items-center gap-1">
              <span class="w-1.5 h-1.5 rounded-full bg-white animate-pulse"></span> LIVE
            </div>
          </div>

          <!-- Mic Volume Level Meter -->
          <div class="space-y-1.5">
            <div class="flex justify-between text-xs text-slate-300">
              <span>Microphone Input Level:</span>
              <span id="mic-level-val" class="font-mono text-[11px] text-[#00D4AA]">0%</span>
            </div>
            <div class="w-full bg-[#0A0A0F] h-2 rounded-full overflow-hidden border border-[#2A2A3A]">
              <div id="mic-meter-bar" class="bg-[#00D4AA] h-full rounded-full transition-all duration-75" style="width: 0%"></div>
            </div>
          </div>

          <!-- Tester Action Controls -->
          <div class="pt-2 flex gap-2">
            <button id="start-av-btn" onclick="startCameraMicTest()" class="flex-1 py-2 px-3 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition">
              <i data-lucide="play" class="w-3.5 h-3.5"></i> Test Camera & Mic
            </button>
            <button id="stop-av-btn" onclick="stopCameraMicTest()" class="hidden py-2 px-3 rounded-lg bg-[#1C1C27] hover:bg-red-500/20 text-red-400 border border-[#2A2A3A] text-xs font-semibold flex items-center justify-center gap-1.5 transition">
              <i data-lucide="square" class="w-3.5 h-3.5"></i> Stop
            </button>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 4: REALITY CHECK (MODULE 2) -->
    <!-- ========================================== -->
    <section id="reality-check" class="space-y-6 scroll-mt-32">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-amber-400">
          <i data-lucide="scale" class="w-3.5 h-3.5"></i> MODULE 2: MINDSET & STANDARDS
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          Reality Check: Local Agency vs US Remote Contractor
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          Understanding the massive gap between domestic outsourced IT culture and venture-backed US startup expectations.
        </p>
      </div>

      <!-- 5-Dimension Comparison Table -->
      <div class="card-surface overflow-x-auto bg-[#13131A]">
        <table class="w-full text-left border-collapse text-xs sm:text-sm">
          <thead>
            <tr class="bg-[#1C1C27] text-slate-300 font-heading">
              <th class="p-4 font-bold border-b border-[#2A2A3A]">Operational Dimension</th>
              <th class="p-4 font-bold border-b border-[#2A2A3A] text-red-400">Local IT Agency Mindset</th>
              <th class="p-4 font-bold border-b border-[#2A2A3A] text-[#00D4AA]">US Remote Contractor Standard</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-[#2A2A3A] text-slate-300">
            <tr>
              <td class="p-4 font-semibold text-white">1. Output Measurement</td>
              <td class="p-4 text-[#8888A8]">Hours logged on tracking software, tickets closed, lines of code written.</td>
              <td class="p-4 text-slate-200 font-medium">Shipped business features, latency reduced, server dollars saved, autonomous problem solving.</td>
            </tr>
            <tr>
              <td class="p-4 font-semibold text-white">2. Communication Flow</td>
              <td class="p-4 text-[#8888A8]">Daily mandatory video standups, passive waiting for manager instructions.</td>
              <td class="p-4 text-slate-200 font-medium">100% Async Slack/Loom updates (BLUF format), proactive pull requests, self-directed.</td>
            </tr>
            <tr>
              <td class="p-4 font-semibold text-white">3. Dealing with Ambiguity</td>
              <td class="p-4 text-[#8888A8]">Demands exhaustive PRD and step-by-step specifications before writing code.</td>
              <td class="p-4 text-slate-200 font-medium">Takes 1-sentence problem, explores trade-offs, builds a working prototype + Loom walkthrough.</td>
            </tr>
            <tr>
              <td class="p-4 font-semibold text-white">4. Cost & Business Consciousness</td>
              <td class="p-4 text-[#8888A8]">Calls expensive APIs blindly without calculating token or infrastructure cost.</td>
              <td class="p-4 text-slate-200 font-medium">Implements tiered routing, semantic caching, and local models to keep inference bills sub-$50/mo.</td>
            </tr>
            <tr>
              <td class="p-4 font-semibold text-white">5. Career & Income Trajectory</td>
              <td class="p-4 text-[#8888A8]">$6K–$15K/yr salary, 5% annual increments, trapped in domestic purchasing power.</td>
              <td class="p-4 text-[#00D4AA] font-bold">$60K–$120K/yr ($30–$60/hr), 70%+ net savings, direct USD wire transfers to Wise/bank.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Workplace Scenario Simulator -->
      <div class="card-surface p-6 space-y-6 bg-[#13131A]">
        <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
          <div>
            <h3 class="text-base font-bold text-white font-heading flex items-center gap-2">
              <i data-lucide="gamepad-2" class="w-4 h-4 text-[#6C63FF]"></i>
              Workplace Scenario Simulator
            </h3>
            <p class="text-xs text-[#8888A8]">Select a scenario to test your on-the-job execution judgment in live US startup situations.</p>
          </div>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3" id="scenario-selector-container">
          <button onclick="selectScenario(0)" id="scen-btn-0" class="tab-btn p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] text-left hover:border-[#6C63FF]/50 transition">
            <div class="text-[11px] font-mono text-[#6C63FF] font-semibold">SCENARIO 1</div>
            <div class="text-xs font-bold text-white mt-1">Ambiguous Slack Task</div>
          </button>
          <button onclick="selectScenario(1)" id="scen-btn-1" class="tab-btn p-3 rounded-xl bg-[#13131A] border border-[#2A2A3A] text-left hover:border-[#6C63FF]/50 transition">
            <div class="text-[11px] font-mono text-[#8888A8] font-semibold">SCENARIO 2</div>
            <div class="text-xs font-bold text-white mt-1">Runaway LLM Bill</div>
          </button>
          <button onclick="selectScenario(2)" id="scen-btn-2" class="tab-btn p-3 rounded-xl bg-[#13131A] border border-[#2A2A3A] text-left hover:border-[#6C63FF]/50 transition">
            <div class="text-[11px] font-mono text-[#8888A8] font-semibold">SCENARIO 3</div>
            <div class="text-xs font-bold text-white mt-1">Friday Production Crash</div>
          </button>
          <button onclick="selectScenario(3)" id="scen-btn-3" class="tab-btn p-3 rounded-xl bg-[#13131A] border border-[#2A2A3A] text-left hover:border-[#6C63FF]/50 transition">
            <div class="text-[11px] font-mono text-[#8888A8] font-semibold">SCENARIO 4</div>
            <div class="text-xs font-bold text-white mt-1">Screening Call Setup</div>
          </button>
        </div>

        <div id="scenario-display-card" class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-4">
          <!-- Rendered dynamically via selectScenario() -->
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 5: EXECUTION ROADMAP (MODULE 3) -->
    <!-- ========================================== -->
    <section id="roadmap" class="space-y-6 scroll-mt-32">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="space-y-2">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#6C63FF]">
            <i data-lucide="milestone" class="w-3.5 h-3.5"></i> MODULE 3: 24-MILESTONE EXECUTION SYSTEM
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
            Execution Roadmap: The 4-Phase System
          </h2>
          <p class="text-sm text-[#8888A8] text-prose">
            A comprehensive checklist to take you from 0 experience to a signed $60K–$120K US remote contract.
          </p>
        </div>
        <div class="text-right">
          <div class="text-xs text-[#8888A8]">Overall Roadmap Completion</div>
          <div id="roadmap-total-stat" class="text-lg font-bold font-mono text-[#00D4AA]">0 / 24 Done (0%)</div>
        </div>
      </div>

      <!-- 4 Phase Cards with 24 Interactive Tasks -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6" id="roadmap-phases-container">
        <!-- Rendered via renderRoadmap() in JS -->
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 6: PROJECT BLUEPRINTS -->
    <!-- ========================================== -->
    <section id="projects" class="space-y-6 scroll-mt-32">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
          <i data-lucide="boxes" class="w-3.5 h-3.5"></i> PRODUCTION-GRADE PROOF OF WORK
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          6 Production-Grade Anti-Resume Blueprints
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          Generic todo apps and basic Titanic Kaggle notebooks get ignored. Build these 6 production-grade architectures that prove you can handle enterprise traffic and cost constraints.
        </p>
      </div>

      <!-- 6 Blueprint Cards Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        
        <!-- Blueprint 1 -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-[#00D4AA] px-2 py-0.5 rounded bg-[#00D4AA]/10">BLUEPRINT 01</span>
              <span class="text-[11px] font-mono text-slate-400">Cost Saver</span>
            </div>
            <h3 class="text-base font-bold text-white font-heading">Hybrid Cost-Optimized Classifier</h3>
            <p class="text-xs text-amber-400 font-mono">100K req/day for $23/mo using Tiered Routing</p>
            <p class="text-xs text-[#8888A8] leading-relaxed">
              Startups burning $3,000–$10,000/mo sending every customer request to GPT-4. Solved via Regex -> FastText -> Claude Haiku fallback.
            </p>
            <div class="flex flex-wrap gap-1.5 pt-1">
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Python</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">FastAPI</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Redis</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Docker</span>
            </div>
          </div>
          <button onclick="openBlueprintModal('bp-1')" class="w-full py-2 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-xs font-medium text-slate-200 transition">
            View Architecture & README
          </button>
        </div>

        <!-- Blueprint 2 -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-[#6C63FF] px-2 py-0.5 rounded bg-[#6C63FF]/10">BLUEPRINT 02</span>
              <span class="text-[11px] font-mono text-slate-400">High Scale</span>
            </div>
            <h3 class="text-base font-bold text-white font-heading">Streaming Anomaly & Fraud Engine</h3>
            <p class="text-xs text-[#00D4AA] font-mono">15M events/day real-time Kafka pipeline</p>
            <p class="text-xs text-[#8888A8] leading-relaxed">
              Sub-50ms fraud screening for fintech transactions with sliding window feature aggregation & chaos-tested resilience.
            </p>
            <div class="flex flex-wrap gap-1.5 pt-1">
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Kafka</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">DuckDB</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Prometheus</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Grafana</span>
            </div>
          </div>
          <button onclick="openBlueprintModal('bp-2')" class="w-full py-2 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-xs font-medium text-slate-200 transition">
            View Architecture & README
          </button>
        </div>

        <!-- Blueprint 3 -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-sky-400 px-2 py-0.5 rounded bg-sky-500/10">BLUEPRINT 03</span>
              <span class="text-[11px] font-mono text-slate-400">E-Commerce</span>
            </div>
            <h3 class="text-base font-bold text-white font-heading">E-Commerce Personalization ($0.001/req)</h3>
            <p class="text-xs text-sky-400 font-mono">2-stage retrieval & vector ranking pipeline</p>
            <p class="text-xs text-[#8888A8] leading-relaxed">
              Fast vector ANN candidate generation (top 500 in 8ms) followed by cross-encoder re-ranking for 1M SKU catalogs.
            </p>
            <div class="flex flex-wrap gap-1.5 pt-1">
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Qdrant</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">PyTorch</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">FastAPI</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Redis</span>
            </div>
          </div>
          <button onclick="openBlueprintModal('bp-3')" class="w-full py-2 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-xs font-medium text-slate-200 transition">
            View Architecture & README
          </button>
        </div>

        <!-- Blueprint 4 -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-purple-400 px-2 py-0.5 rounded bg-purple-500/10">BLUEPRINT 04</span>
              <span class="text-[11px] font-mono text-slate-400">Enterprise RAG</span>
            </div>
            <h3 class="text-base font-bold text-white font-heading">Multi-Tenant RAG Engine with Caching</h3>
            <p class="text-xs text-purple-400 font-mono">Per-tenant budget governor & vector isolation</p>
            <p class="text-xs text-[#8888A8] leading-relaxed">
              B2B SaaS document search with row-level security, semantic deduplication, and automated monthly spending caps.
            </p>
            <div class="flex flex-wrap gap-1.5 pt-1">
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">pgvector</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">LlamaIndex</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">FastAPI</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Docker</span>
            </div>
          </div>
          <button onclick="openBlueprintModal('bp-4')" class="w-full py-2 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-xs font-medium text-slate-200 transition">
            View Architecture & README
          </button>
        </div>

        <!-- Blueprint 5 -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-emerald-400 px-2 py-0.5 rounded bg-emerald-500/10">BLUEPRINT 05</span>
              <span class="text-[11px] font-mono text-slate-400">MLOps</span>
            </div>
            <h3 class="text-base font-bold text-white font-heading">Drift-Aware Production MLOps Pipeline</h3>
            <p class="text-xs text-emerald-400 font-mono">Automated retraining via KL Divergence</p>
            <p class="text-xs text-[#8888A8] leading-relaxed">
              Detects silent model accuracy degradation in &lt;60 seconds and executes canary deployments and automated rollbacks.
            </p>
            <div class="flex flex-wrap gap-1.5 pt-1">
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Evidently</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">MLflow</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Actions</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Docker</span>
            </div>
          </div>
          <button onclick="openBlueprintModal('bp-5')" class="w-full py-2 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-xs font-medium text-slate-200 transition">
            View Architecture & README
          </button>
        </div>

        <!-- Blueprint 6 -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-pink-400 px-2 py-0.5 rounded bg-pink-500/10">BLUEPRINT 06</span>
              <span class="text-[11px] font-mono text-slate-400">Data Engineering</span>
            </div>
            <h3 class="text-base font-bold text-white font-heading">High-Throughput Async Data Ingestion</h3>
            <p class="text-xs text-pink-400 font-mono">Extracts & vectors 10,000 PDFs/hr at constant RAM</p>
            <p class="text-xs text-[#8888A8] leading-relaxed">
              Chunked stream processing with backpressure to eliminate memory leaks and crashes during heavy document workloads.
            </p>
            <div class="flex flex-wrap gap-1.5 pt-1">
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Celery</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Redis</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">AWS S3</span>
              <span class="text-[10px] font-mono bg-[#1C1C27] text-slate-300 px-2 py-0.5 rounded border border-[#2A2A3A]">Docker</span>
            </div>
          </div>
          <button onclick="openBlueprintModal('bp-6')" class="w-full py-2 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-xs font-medium text-slate-200 transition">
            View Architecture & README
          </button>
        </div>

      </div>

      <!-- JD Reverse-Engineering Project Mapper -->
      <div class="card-surface p-6 space-y-4 bg-[#13131A]">
        <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
          <div>
            <h3 class="text-base font-bold text-white font-heading flex items-center gap-2">
              <i data-lucide="cpu" class="w-4 h-4 text-[#00D4AA]"></i>
              JD Reverse-Engineering Project Mapper
            </h3>
            <p class="text-xs text-[#8888A8]">Paste target Job Description requirements to instantly receive the optimal portfolio architecture.</p>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
          <div class="lg:col-span-8 space-y-2">
            <textarea id="jd-input-text" rows="3" placeholder="Paste target skills (e.g. 'FastAPI, LangChain, RAG, PyTorch, Kafka, AWS, low-latency search')..." class="w-full p-3 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-slate-200 focus:border-[#6C63FF] focus:outline-none"></textarea>
            <div class="flex gap-2">
              <button onclick="analyzeJDAndRecommend()" class="px-4 py-2 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center gap-1.5 transition">
                <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Map Optimal Project Architecture
              </button>
            </div>
          </div>
          <div class="lg:col-span-4 p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] flex flex-col justify-center space-y-2" id="jd-result-container">
            <div class="text-[11px] font-mono uppercase text-[#8888A8]">Recommended Architecture:</div>
            <div id="jd-recommended-name" class="text-xs font-bold text-[#00D4AA]">Hybrid Cost-Optimized Classifier</div>
            <div id="jd-recommended-reason" class="text-[11px] text-slate-300">Matches 4/5 target keywords. Focus on tiered routing and latency percentiles.</div>
          </div>
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 7: OFFER FRAMEWORK -->
    <!-- ========================================== -->
    <section id="offer" class="space-y-6 scroll-mt-32">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-amber-400">
          <i data-lucide="badge-percent" class="w-3.5 h-3.5"></i> ZERO-RISK HIRING FRAMEWORK
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          The Risk-Reversal Offer Framework
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          How to eliminate 100% of the hiring friction for US founders and get hired on a 1-week paid trial.
        </p>
      </div>

      <!-- 5 Risk Reversals -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        
        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="text-xs font-mono text-amber-400 font-semibold">REVERSAL 01</div>
          <h3 class="text-sm font-bold text-white font-heading">The 1-Week Paid Trial ($1,000–$1,500)</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Offer to build a concrete, scoped feature in 7 days. If they love it, convert to monthly contractor. If not, zero hard feelings.
          </p>
        </div>

        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="text-xs font-mono text-[#00D4AA] font-semibold">REVERSAL 02</div>
          <h3 class="text-sm font-bold text-white font-heading">Milestone-Based Billing</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Eliminate fear of idle hours. Structure payments around shipped deliverables and pull requests, not mystery timesheets.
          </p>
        </div>

        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="text-xs font-mono text-[#6C63FF] font-semibold">REVERSAL 03</div>
          <h3 class="text-sm font-bold text-white font-heading">Daily Asynchronous Loom Walkthroughs</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Record a 90-second video at the end of each day demonstrating exactly what was shipped, tests run, and tomorrow's focus.
          </p>
        </div>

        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="text-xs font-mono text-sky-400 font-semibold">REVERSAL 04</div>
          <h3 class="text-sm font-bold text-white font-heading">Full IP Assignment & US NDA</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Provide a clean US-standard contractor agreement with total intellectual property assignment and confidentiality clauses.
          </p>
        </div>

        <div class="card-surface p-5 space-y-2 bg-[#13131A] md:col-span-2 lg:col-span-2">
          <div class="text-xs font-mono text-emerald-400 font-semibold">REVERSAL 05</div>
          <h3 class="text-sm font-bold text-white font-heading">Guaranteed 4-Hour Timezone Overlap Block</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            State your exact live working overlap hours clearly (e.g. 7:00 AM – 11:00 AM EST). Never leave a founder waiting 24 hours for a critical answer.
          </p>
        </div>

      </div>

      <!-- Proposal Generator Callout -->
      <div class="card-surface p-6 bg-[#13131A] flex flex-col sm:flex-row items-center justify-between gap-4">
        <div>
          <h3 class="text-base font-bold text-white font-heading">Generate a 1-Page Risk-Reversal Proposal Letter</h3>
          <p class="text-xs text-[#8888A8]">Input client details and deliverable to instantly generate a copy-ready proposal document.</p>
        </div>
        <button onclick="openProposalModal()" class="px-5 py-2.5 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center gap-2 transition shrink-0">
          <i data-lucide="file-text" class="w-4 h-4"></i> Open Proposal Generator
        </button>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 8: LINKEDIN STUDIO -->
    <!-- ========================================== -->
    <section id="linkedin" class="space-y-6 scroll-mt-32">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
          <i data-lucide="linkedin" class="w-3.5 h-3.5"></i> INBOUND AUTHORITY MAGNET
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          LinkedIn Optimization Studio
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          Transform your profile into an inbound lead generator and execute a 30-day authority launch plan.
        </p>
      </div>

      <!-- LinkedIn Studio 6 Tabs Container -->
      <div class="card-surface bg-[#13131A] overflow-hidden">
        
        <!-- Tab Navigation Bar (6 Tabs) -->
        <div class="border-b border-[#2A2A3A] bg-[#1C1C27] overflow-x-auto scrollbar-none flex">
          <button onclick="switchLinkedInTab('headlines')" id="li-tab-headlines" class="tab-btn px-4 py-3 text-xs font-semibold text-white bg-[#6C63FF] whitespace-nowrap">
            16 Headline Formulas
          </button>
          <button onclick="switchLinkedInTab('about')" id="li-tab-about" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            5-Block About Generator
          </button>
          <button onclick="switchLinkedInTab('checklist')" id="li-tab-checklist" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            Profile Checklist
          </button>
          <button onclick="switchLinkedInTab('featured')" id="li-tab-featured" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            3-Slot Featured Strategy
          </button>
          <button onclick="switchLinkedInTab('scheduler')" id="li-tab-scheduler" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            3x/Week Scheduler
          </button>
          <button onclick="switchLinkedInTab('launch30')" id="li-tab-launch30" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            30-Day Launch Plan
          </button>
        </div>

        <!-- Tab 1 Content: 16 Headlines -->
        <div id="li-content-headlines" class="p-6 space-y-4">
          <div class="flex items-center justify-between">
            <div class="text-xs text-[#8888A8]">Click any headline formula to copy or customize.</div>
            <div class="text-xs font-mono text-[#00D4AA]">16 High-Converting Formulas</div>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4" id="headlines-grid-container">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- Tab 2 Content: 5-Block About Generator -->
        <div id="li-content-about" class="hidden p-6 space-y-6">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
            <div class="space-y-4">
              <div class="flex items-center justify-between">
                <span class="text-xs font-bold text-white">Choose Pre-Built Template:</span>
                <div class="flex gap-2">
                  <button onclick="loadAboutTemplate('A')" class="px-2.5 py-1 rounded bg-[#1C1C27] text-xs text-slate-300 hover:text-white border border-[#2A2A3A]">Cost Optimizer</button>
                  <button onclick="loadAboutTemplate('B')" class="px-2.5 py-1 rounded bg-[#1C1C27] text-xs text-slate-300 hover:text-white border border-[#2A2A3A]">System Builder</button>
                  <button onclick="loadAboutTemplate('C')" class="px-2.5 py-1 rounded bg-[#1C1C27] text-xs text-slate-300 hover:text-white border border-[#2A2A3A]">Business Mindset</button>
                </div>
              </div>
              <textarea id="about-editor-textarea" rows="12" class="w-full p-3 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-slate-200 focus:border-[#6C63FF] focus:outline-none font-sans leading-relaxed"></textarea>
              <button onclick="copyAboutBio()" class="w-full py-2.5 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition">
                <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy Formatted About Section
              </button>
            </div>
            <div class="p-5 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] space-y-3">
              <div class="text-[11px] font-mono uppercase text-[#00D4AA]">Live LinkedIn Preview</div>
              <div id="about-live-preview" class="text-xs text-slate-300 whitespace-pre-wrap leading-relaxed"></div>
            </div>
          </div>
        </div>

        <!-- Tab 3 Content: Profile Checklist -->
        <div id="li-content-checklist" class="hidden p-6 space-y-4">
          <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
            <span class="text-xs font-bold text-white">10 Critical Profile Hygiene Items</span>
            <span id="li-checklist-stat" class="text-xs font-mono text-[#00D4AA]">0 / 10 Checked</span>
          </div>
          <div class="space-y-3" id="li-checklist-items-container">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- Tab 4 Content: 3-Slot Featured Strategy -->
        <div id="li-content-featured" class="hidden p-6 space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="text-xs font-mono text-[#00D4AA]">SLOT 1: HERO PROJECT</div>
              <h4 class="text-sm font-bold text-white">Production Case Study Repo</h4>
              <p class="text-xs text-[#8888A8]">Pin your best GitHub blueprint with architecture diagram cover image, benchmark tables, and live API demo URL.</p>
            </div>
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="text-xs font-mono text-[#6C63FF]">SLOT 2: HIGHEST ENGAGEMENT</div>
              <h4 class="text-sm font-bold text-white">Technical Breakdown Post</h4>
              <p class="text-xs text-[#8888A8]">Pin your post detailing a specific architectural trade-off, latency bottleneck fix, or failure post-mortem.</p>
            </div>
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="text-xs font-mono text-amber-400">SLOT 3: DIRECT ARTIFACT</div>
              <h4 class="text-sm font-bold text-white">Cost & Architecture PDF</h4>
              <p class="text-xs text-[#8888A8]">A 2-page downloadable PDF tearing down LLM inference costs and showing how tiered routing saves 70%+.</p>
            </div>
          </div>
        </div>

        <!-- Tab 5 Content: 3x/Week Scheduler -->
        <div id="li-content-scheduler" class="hidden p-6 space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="text-xs font-mono text-[#6C63FF]">MONDAY: CONFUSION / BUG</div>
              <h4 class="text-sm font-bold text-white">The Bug Breakdown</h4>
              <p class="text-xs text-[#8888A8]">Explain an obscure bug or memory leak encountered while building your production pipeline and how you solved it.</p>
            </div>
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="text-xs font-mono text-[#00D4AA]">WEDNESDAY: MATH / TRADE-OFF</div>
              <h4 class="text-sm font-bold text-white">Cost & Latency Math</h4>
              <p class="text-xs text-[#8888A8]">Compare two architectures with real numbers (e.g. GPT-4o vs DistilBERT + Haiku fallback under 100K req/day).</p>
            </div>
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="text-xs font-mono text-amber-400">FRIDAY: POST-MORTEM</div>
              <h4 class="text-sm font-bold text-white">System Failure Teardown</h4>
              <p class="text-xs text-[#8888A8]">Deconstruct why a popular AI architecture fails in real production traffic and the 3 guardrails needed.</p>
            </div>
          </div>
        </div>

        <!-- Tab 6 Content: 30-Day Launch Plan -->
        <div id="li-content-launch30" class="hidden p-6 space-y-4">
          <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
            <span class="text-xs font-bold text-white">Interactive 30-Day Authority Launch Plan</span>
            <span id="launch30-stat-badge" class="text-xs font-mono text-[#00D4AA]">0 / 30 Days Done</span>
          </div>
          <div class="space-y-3" id="launch30-items-container">
            <!-- Rendered via JS -->
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 9: OUTREACH CRM (MODULE 4) -->
    <!-- ========================================== -->
    <section id="outreach" class="space-y-6 scroll-mt-32">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="space-y-2">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#6C63FF]">
            <i data-lucide="send" class="w-3.5 h-3.5"></i> MODULE 4: OUTBOUND PIPELINE
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
            Outreach CRM & Lead Generation Pipeline
          </h2>
          <p class="text-sm text-[#8888A8] text-prose">
            Track your outbound campaign, generate high-converting 3-phase DMs, and manage your pipeline across 5 deal stages.
          </p>
        </div>

        <!-- Open 300+ Leads Database Button -->
        <button onclick="openLeadsModal()" class="px-4 py-2 rounded-lg bg-[#00D4AA] hover:bg-[#00b894] text-slate-950 font-bold text-xs flex items-center gap-2 shadow-sm transition">
          <i data-lucide="database" class="w-4 h-4"></i> Browse 300+ Curated Leads
        </button>
      </div>

      <!-- Daily Outreach Habit Tracker Counters -->
      <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
        <div class="card-surface p-4 bg-[#13131A] flex items-center justify-between">
          <div class="space-y-1">
            <div class="text-[11px] text-[#8888A8]">Daily Connections Sent</div>
            <div id="daily-connects-val" class="text-xl font-bold font-mono text-[#6C63FF]">0 / 25</div>
          </div>
          <div class="flex gap-1.5">
            <button onclick="incrementDaily('connects')" class="p-2 rounded bg-[#1C1C27] hover:bg-[#6C63FF] hover:text-white text-slate-300 border border-[#2A2A3A] transition">
              <i data-lucide="plus" class="w-4 h-4"></i>
            </button>
          </div>
        </div>

        <div class="card-surface p-4 bg-[#13131A] flex items-center justify-between">
          <div class="space-y-1">
            <div class="text-[11px] text-[#8888A8]">Substantive Comments</div>
            <div id="daily-comments-val" class="text-xl font-bold font-mono text-[#00D4AA]">0 / 10</div>
          </div>
          <div class="flex gap-1.5">
            <button onclick="incrementDaily('comments')" class="p-2 rounded bg-[#1C1C27] hover:bg-[#00D4AA] hover:text-slate-950 text-slate-300 border border-[#2A2A3A] transition">
              <i data-lucide="plus" class="w-4 h-4"></i>
            </button>
          </div>
        </div>

        <div class="card-surface p-4 bg-[#13131A] flex items-center justify-between">
          <div class="space-y-1">
            <div class="text-[11px] text-[#8888A8]">Personalized DMs Sent</div>
            <div id="daily-dms-val" class="text-xl font-bold font-mono text-amber-400">0 / 5</div>
          </div>
          <div class="flex gap-1.5">
            <button onclick="incrementDaily('dms')" class="p-2 rounded bg-[#1C1C27] hover:bg-amber-500 hover:text-slate-950 text-slate-300 border border-[#2A2A3A] transition">
              <i data-lucide="plus" class="w-4 h-4"></i>
            </button>
          </div>
        </div>
      </div>

      <!-- 3-Phase DM Generator Tool -->
      <div class="card-surface p-6 space-y-4 bg-[#13131A]">
        <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
          <div>
            <h3 class="text-base font-bold text-white font-heading flex items-center gap-2">
              <i data-lucide="message-square" class="w-4 h-4 text-[#6C63FF]"></i>
              3-Phase DM Generator
            </h3>
            <p class="text-xs text-[#8888A8]">Select the outreach phase and customize tokens to generate friction-free messages.</p>
          </div>
          <div class="flex gap-2">
            <button onclick="selectDMPhase(1)" id="dm-btn-1" class="tab-btn px-2.5 py-1 rounded text-xs font-semibold bg-[#6C63FF] text-white">Phase 1 (Value)</button>
            <button onclick="selectDMPhase(2)" id="dm-btn-2" class="tab-btn px-2.5 py-1 rounded text-xs font-semibold bg-[#1C1C27] text-[#8888A8] hover:text-white">Phase 2 (Trade-off)</button>
            <button onclick="selectDMPhase(3)" id="dm-btn-3" class="tab-btn px-2.5 py-1 rounded text-xs font-semibold bg-[#1C1C27] text-[#8888A8] hover:text-white">Phase 3 (Loom)</button>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div class="space-y-3">
            <div class="grid grid-cols-2 gap-2 text-xs">
              <input type="text" id="dm-founder-input" placeholder="Founder Name (e.g. Alex)" value="Alex" oninput="updateDMPreview()" class="p-2 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white focus:border-[#6C63FF] focus:outline-none">
              <input type="text" id="dm-company-input" placeholder="Company Name (e.g. ScaleAI)" value="VentureScale" oninput="updateDMPreview()" class="p-2 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white focus:border-[#6C63FF] focus:outline-none">
            </div>
            <textarea id="dm-message-preview" rows="5" class="w-full p-3 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-slate-200 focus:border-[#6C63FF] focus:outline-none font-sans leading-relaxed"></textarea>
            <button onclick="copyGeneratedDM()" class="w-full py-2 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition">
              <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy DM to Clipboard
            </button>
          </div>
          <div class="p-4 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] space-y-2 text-xs text-slate-300">
            <div class="font-bold text-white flex items-center gap-1.5">
              <i data-lucide="info" class="w-3.5 h-3.5 text-[#00D4AA]"></i> Outreach Rules of Engagement
            </div>
            <ul class="space-y-1.5 text-[11px] text-[#8888A8] list-disc list-inside">
              <li>Never ask for a job or say "I am looking for opportunities" in message 1.</li>
              <li>Always reference a specific engineering challenge or public tech stack element.</li>
              <li>Keep message 1 under 60 words. Total reading time &lt; 15 seconds.</li>
              <li>Propose a 1-sentence trade-off question to ignite a peer-to-peer discussion.</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 5-Column Kanban Board -->
      <div class="space-y-3">
        <div class="flex items-center justify-between">
          <h3 class="text-sm font-bold text-white font-heading">5-Stage Outbound Deal Pipeline</h3>
          <button onclick="openAddLeadModal()" class="px-3 py-1 rounded bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-xs text-white flex items-center gap-1">
            <i data-lucide="plus" class="w-3 h-3"></i> Add Lead
          </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-3" id="kanban-board-container">
          <!-- Rendered via renderKanban() in JS -->
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 10: JOB SEARCH ENGINE (NEW) -->
    <!-- ========================================== -->
    <section id="job-search" class="space-y-8 scroll-mt-32">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
          <i data-lucide="search" class="w-3.5 h-3.5"></i> 2026 REMOTE DISCOVERY & CLOSING
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          The US Remote AI Job Search Engine
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          High-demand career paths, boolean search queries, vetted job board directories, the 5-5-5 daily outbound system, and the AI interview playbook.
        </p>
      </div>

      <!-- Sub-section A: The 6 High-Demand AI & Remote Career Paths -->
      <div class="space-y-4">
        <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-2">
          <h3 class="text-base font-bold text-white font-heading">A. 6 High-Demand AI & Remote Career Paths</h3>
          <span class="text-xs font-mono text-[#00D4AA]">$60K–$150K Contractor Market</span>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          
          <div class="card-surface p-5 space-y-2 bg-[#13131A]">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-[#6C63FF] font-semibold">ROLE 01</span>
              <span class="text-xs font-mono font-bold text-[#00D4AA]">$80K–$130K/yr</span>
            </div>
            <h4 class="text-sm font-bold text-white font-heading">AI Engineer</h4>
            <p class="text-xs text-[#8888A8] leading-relaxed">
              Integrates models into production software. Builds APIs, orchestrates model calling, implements latency caching, and monitors output fidelity.
            </p>
            <div class="text-[11px] text-slate-300 font-mono pt-1">Stack: Python, FastAPI, PyTorch, OpenAI API, Docker</div>
          </div>

          <div class="card-surface p-5 space-y-2 bg-[#13131A]">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-[#6C63FF] font-semibold">ROLE 02</span>
              <span class="text-xs font-mono font-bold text-[#00D4AA]">$90K–$140K/yr</span>
            </div>
            <h4 class="text-sm font-bold text-white font-heading">LLM & RAG Engineer</h4>
            <p class="text-xs text-[#8888A8] leading-relaxed">
              Builds retrieval-augmented generation pipelines, vector database indexing, hybrid search (BM25 + Dense), semantic routing, and evaluation suites.
            </p>
            <div class="text-[11px] text-slate-300 font-mono pt-1">Stack: LangChain, LlamaIndex, Qdrant, Chroma, Ragas</div>
          </div>

          <div class="card-surface p-5 space-y-2 bg-[#13131A]">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-[#6C63FF] font-semibold">ROLE 03</span>
              <span class="text-xs font-mono font-bold text-[#00D4AA]">$85K–$135K/yr</span>
            </div>
            <h4 class="text-sm font-bold text-white font-heading">MLOps Engineer</h4>
            <p class="text-xs text-[#8888A8] leading-relaxed">
              Maintains training and inference infrastructure, CI/CD pipelines for models, data drift monitoring (KL divergence), and containerized microservices.
            </p>
            <div class="text-[11px] text-slate-300 font-mono pt-1">Stack: MLflow, Evidently, Kubernetes, Prometheus, AWS</div>
          </div>

          <div class="card-surface p-5 space-y-2 bg-[#13131A]">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-[#6C63FF] font-semibold">ROLE 04</span>
              <span class="text-xs font-mono font-bold text-[#00D4AA]">$80K–$125K/yr</span>
            </div>
            <h4 class="text-sm font-bold text-white font-heading">Full-Stack AI Engineer</h4>
            <p class="text-xs text-[#8888A8] leading-relaxed">
              Bridges frontend UI and backend AI pipelines. Builds reactive dashboards, chat interfaces, streaming responses, and backend API endpoints.
            </p>
            <div class="text-[11px] text-slate-300 font-mono pt-1">Stack: Next.js, React, Tailwind, FastAPI, Python</div>
          </div>

          <div class="card-surface p-5 space-y-2 bg-[#13131A]">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-[#6C63FF] font-semibold">ROLE 05</span>
              <span class="text-xs font-mono font-bold text-[#00D4AA]">$75K–$120K/yr</span>
            </div>
            <h4 class="text-sm font-bold text-white font-heading">AI Product Developer</h4>
            <p class="text-xs text-[#8888A8] leading-relaxed">
              Focuses on end-to-end product features powered by autonomous agents, tool use, and structured outputs for internal workflows.
            </p>
            <div class="text-[11px] text-slate-300 font-mono pt-1">Stack: CrewAI, LangGraph, Python, Streamlit, Supabase</div>
          </div>

          <div class="card-surface p-5 space-y-2 bg-[#13131A]">
            <div class="flex items-center justify-between">
              <span class="text-xs font-mono text-[#6C63FF] font-semibold">ROLE 06</span>
              <span class="text-xs font-mono font-bold text-[#00D4AA]">$95K–$150K/yr</span>
            </div>
            <h4 class="text-sm font-bold text-white font-heading">Remote AI Solutions Architect</h4>
            <p class="text-xs text-[#8888A8] leading-relaxed">
              Designs cloud architecture, multi-tenant security boundaries, data governance, and cost optimization strategies for enterprise AI adoption.
            </p>
            <div class="text-[11px] text-slate-300 font-mono pt-1">Stack: AWS Cloud, GCP, pgvector, Redis, System Design</div>
          </div>

        </div>
      </div>

      <!-- Sub-section B & C: Search Strings & Job Titles -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
        
        <!-- B: Exact Job Titles (5 cols) -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A] lg:col-span-5">
          <h3 class="text-base font-bold text-white font-heading">B. Exact Job Titles to Target</h3>
          <p class="text-xs text-[#8888A8]">Search across these variants to uncover uncrowded listings:</p>
          
          <div class="space-y-2 text-xs">
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] flex justify-between">
              <span class="text-white font-medium">Entry / Associate:</span>
              <span class="text-[#8888A8]">Junior AI Dev, Associate ML Engineer</span>
            </div>
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] flex justify-between">
              <span class="text-white font-medium">Core / Mid-Level:</span>
              <span class="text-[#8888A8]">AI Engineer, LLM Engineer, Applied ML</span>
            </div>
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] flex justify-between">
              <span class="text-white font-medium">Contractor / Remote:</span>
              <span class="text-[#00D4AA]">US Remote Contractor, AI Specialist</span>
            </div>
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] flex justify-between">
              <span class="text-white font-medium">Infrastructure:</span>
              <span class="text-[#8888A8]">ML Platform Engineer, MLOps Infra</span>
            </div>
          </div>
        </div>

        <!-- C: 10 Boolean Search Strings (7 cols) -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A] lg:col-span-7">
          <div class="flex items-center justify-between">
            <h3 class="text-base font-bold text-white font-heading">C. 10 Boolean Search Strings</h3>
            <span class="text-xs text-[#8888A8]">1-Click Copy</span>
          </div>
          
          <div class="space-y-2 max-h-64 overflow-y-auto pr-1">
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-2 text-xs">
              <span class="font-mono text-slate-300 truncate">"AI Engineer" AND ("remote" OR "anywhere") AND "FastAPI"</span>
              <button onclick="copySearchString('\"AI Engineer\" AND (\"remote\" OR \"anywhere\") AND \"FastAPI\"')" class="px-2 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-[11px] shrink-0 font-medium">Copy</button>
            </div>
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-2 text-xs">
              <span class="font-mono text-slate-300 truncate">"LLM" AND ("RAG" OR "LangChain") AND "contract" AND "worldwide"</span>
              <button onclick="copySearchString('\"LLM\" AND (\"RAG\" OR \"LangChain\") AND \"contract\" AND \"worldwide\"')" class="px-2 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-[11px] shrink-0 font-medium">Copy</button>
            </div>
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-2 text-xs">
              <span class="font-mono text-slate-300 truncate">"Machine Learning Engineer" AND ("Seed" OR "Series A") AND "overlap"</span>
              <button onclick="copySearchString('\"Machine Learning Engineer\" AND (\"Seed\" OR \"Series A\") AND \"overlap\"')" class="px-2 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-[11px] shrink-0 font-medium">Copy</button>
            </div>
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-2 text-xs">
              <span class="font-mono text-slate-300 truncate">"Python" AND "AI" AND ("W-8BEN" OR "contractor" OR "B2B")</span>
              <button onclick="copySearchString('\"Python\" AND \"AI\" AND (\"W-8BEN\" OR \"contractor\" OR \"B2B\")')" class="px-2 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-[11px] shrink-0 font-medium">Copy</button>
            </div>
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-2 text-xs">
              <span class="font-mono text-slate-300 truncate">"Applied AI" AND ("Vector DB" OR "Qdrant" OR "pgvector")</span>
              <button onclick="copySearchString('\"Applied AI\" AND (\"Vector DB\" OR \"Qdrant\" OR \"pgvector\")')" class="px-2 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-[11px] shrink-0 font-medium">Copy</button>
            </div>
          </div>
        </div>

      </div>

      <!-- Sub-section D: Platforms Directory (4 Tabs) -->
      <div class="card-surface bg-[#13131A] overflow-hidden">
        <div class="p-4 border-b border-[#2A2A3A] flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <h3 class="text-base font-bold text-white font-heading">D. Vetted Remote Job Board Directory</h3>
          <div class="flex flex-wrap gap-1.5">
            <button onclick="switchPlatformTab('ai')" id="plat-tab-ai" class="tab-btn px-3 py-1 text-xs font-semibold rounded-lg bg-[#6C63FF] text-white">AI-Specific</button>
            <button onclick="switchPlatformTab('remote')" id="plat-tab-remote" class="tab-btn px-3 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">Remote-First</button>
            <button onclick="switchPlatformTab('reverse')" id="plat-tab-reverse" class="tab-btn px-3 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">Reverse Networks</button>
            <button onclick="switchPlatformTab('outreach')" id="plat-tab-outreach" class="tab-btn px-3 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">Direct Outreach</button>
          </div>
        </div>

        <div class="p-6">
          <div id="plat-content-ai" class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white text-xs">AI Jobs Global</div>
              <p class="text-[11px] text-[#8888A8]">Dedicated directory for machine learning, prompt engineering, and LLM roles.</p>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white text-xs">Hugging Face Jobs</div>
              <p class="text-[11px] text-[#8888A8]">Top AI research labs and open-source startups hiring globally.</p>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white text-xs">Wellfound (AngelList) AI</div>
              <p class="text-[11px] text-[#8888A8]">Filter by Seed/Series A startups with verified remote contractor budgets.</p>
            </div>
          </div>

          <div id="plat-content-remote" class="hidden grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white text-xs">We Work Remotely</div>
              <p class="text-[11px] text-[#8888A8]">The original remote job board with high-paying international contractor roles.</p>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white text-xs">RemoteOK</div>
              <p class="text-[11px] text-[#8888A8]">Live salary transparency and worldwide tech openings.</p>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white text-xs">Himalayas</div>
              <p class="text-[11px] text-[#8888A8]">In-depth company profiles and strict remote-only filtering.</p>
            </div>
          </div>

          <div id="plat-content-reverse" class="hidden grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white text-xs">Toptal</div>
              <p class="text-[11px] text-[#8888A8]">Top 3% freelance network. High hourly rates ($50–$120/hr).</p>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white text-xs">Turing / Braintrust</div>
              <p class="text-[11px] text-[#8888A8]">Vetted engineering matching for US tech companies.</p>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white text-xs">A.Team</div>
              <p class="text-[11px] text-[#8888A8]">High-end cloud teams hired by venture-backed startups for key product sprints.</p>
            </div>
          </div>

          <div id="plat-content-outreach" class="hidden grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white text-xs">Y Combinator Startup Directory</div>
              <p class="text-[11px] text-[#8888A8]">Filter recent YC batches (W24, S24, W25) and pitch founders directly.</p>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white text-xs">Product Hunt Launches</div>
              <p class="text-[11px] text-[#8888A8]">Target newly launched AI tools experiencing sudden server and cost scaling issues.</p>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white text-xs">GitHub Trending Repos</div>
              <p class="text-[11px] text-[#8888A8]">Submit high-value bug fixes and PRs to open-source AI repos that have commercial backing.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Sub-section E & F: Smart Strategies & 5-5-5 Daily System -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        <!-- E: 7 Smart Strategies -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A]">
          <h3 class="text-base font-bold text-white font-heading">E. 7 Smart Application Strategies</h3>
          <div class="space-y-2 text-xs text-slate-300">
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">1. The 2-Minute Video Audit:</span> Record a Loom tearing down an architectural bottleneck before the first interview.
            </div>
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">2. Open Source PR Proof:</span> Fix a documented issue on the company's public repo and attach the PR link.
            </div>
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">3. Direct Founder DM:</span> Bypass HR portals completely and contact technical founders with a trade-off question.
            </div>
            <div class="p-2.5 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">4. Scoped Trial Close:</span> Never ask for full-time on day 1. Close on a 1-week paid trial milestone.
            </div>
          </div>
        </div>

        <!-- F: The 5-5-5 Daily Application System -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A]">
          <div class="flex items-center justify-between">
            <h3 class="text-base font-bold text-white font-heading">F. The 5-5-5 Daily Outbound Habit</h3>
            <span class="text-xs font-mono text-[#00D4AA]">Daily Routine</span>
          </div>
          <div class="space-y-3 text-xs">
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white flex justify-between"><span>5 Quick Applications</span> <span class="text-[#00D4AA]">Portals & Boards</span></div>
              <p class="text-[11px] text-[#8888A8]">Submit 5 high-fit applications on Wellfound, RemoteOK, and Himalayas.</p>
            </div>
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white flex justify-between"><span>5 Tailored Founder DMs</span> <span class="text-[#6C63FF]">LinkedIn / X</span></div>
              <p class="text-[11px] text-[#8888A8]">Send 5 personalized curiosity messages to technical founders with custom project links.</p>
            </div>
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white flex justify-between"><span>5 High-Value Engagements</span> <span class="text-amber-400">Comments & Insights</span></div>
              <p class="text-[11px] text-[#8888A8]">Leave 5 thoughtful technical comments on target decision-makers' posts.</p>
            </div>
          </div>
        </div>

      </div>

      <!-- Sub-section G & H: Cold Outreach Templates & Remote Work Reality -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
        
        <!-- G: 3 Cold Outreach Templates -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A]">
          <div class="flex items-center justify-between">
            <h3 class="text-base font-bold text-white font-heading">G. 3 Cold Outreach Direct Pitch Templates</h3>
            <span class="text-xs text-[#8888A8]">Copy-Ready</span>
          </div>
          <div class="space-y-3">
            <div class="p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="flex justify-between items-center">
                <span class="text-xs font-bold text-white">Template 1: Founder / CTO Direct Pitch</span>
                <button onclick="copyTemplateMessage('tpl-1-text')" class="px-2 py-0.5 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-[10px]">Copy</button>
              </div>
              <p id="tpl-1-text" class="text-xs text-slate-300 font-sans leading-relaxed italic">
                "Hey [Name], noticed [Company] is scaling its RAG document processing. I recently built a tiered classifier that cut inference costs 70% while keeping latency under 30ms. Open-sourced the architecture and benchmarks here: [Link]. Would love to share how we handled tenant cache eviction if you're exploring cost optimizations."
              </p>
            </div>

            <div class="p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="flex justify-between items-center">
                <span class="text-xs font-bold text-white">Template 2: Engineering Manager Trade-off</span>
                <button onclick="copyTemplateMessage('tpl-2-text')" class="px-2 py-0.5 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-[10px]">Copy</button>
              </div>
              <p id="tpl-2-text" class="text-xs text-slate-300 font-sans leading-relaxed italic">
                "Hey [Name], loved your recent post on handling drift in production models. Built an automated retraining pipeline using KL divergence alerts that triggers canaries on GitHub Actions: [Repo Link]. Curious how your team currently benchmarks embeddings drift across user clusters?"
              </p>
            </div>
          </div>
        </div>

        <!-- H: Remote Reality Check & Infrastructure -->
        <div class="card-surface p-6 space-y-4 bg-[#13131A]">
          <h3 class="text-base font-bold text-white font-heading">H. Remote Contractor Infrastructure & Legal</h3>
          <div class="space-y-3 text-xs text-slate-300">
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white">W-8BEN Tax Form (0 US Tax Withholding)</div>
              <p class="text-[11px] text-[#8888A8]">As a non-US citizen working outside the US, you submit Form W-8BEN to certify you owe 0% US withholding tax. You pay taxes locally in your home country.</p>
            </div>
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white">Payment Rails (Wise / Deel / Stripe)</div>
              <p class="text-[11px] text-[#8888A8]">Setup a USD receiving bank account on Wise or Deel for friction-free ACH and wire payouts directly to your local bank.</p>
            </div>
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white">Contractor Terms vs Full-Time</div>
              <p class="text-[11px] text-[#8888A8]">Contractors earn 30–50% higher hourly rates ($40–$80/hr) with full flexibility and zero US visa sponsorship requirements.</p>
            </div>
          </div>
        </div>

      </div>

      <!-- Sub-section I: The AI Interview Playbook (5 Tabs) -->
      <div class="card-surface bg-[#13131A] overflow-hidden">
        <div class="p-4 border-b border-[#2A2A3A] flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <h3 class="text-base font-bold text-white font-heading">I. The AI Interview Playbook & 8 Project Questions</h3>
            <p class="text-xs text-[#8888A8]">Master the technical rounds, system design, and behavioral questions US founders ask.</p>
          </div>
          <div class="flex flex-wrap gap-1">
            <button onclick="switchInterviewTab('coding')" id="int-tab-coding" class="tab-btn px-2.5 py-1 text-xs font-semibold rounded-lg bg-[#6C63FF] text-white">1. Coding</button>
            <button onclick="switchInterviewTab('ml')" id="int-tab-ml" class="tab-btn px-2.5 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">2. ML / Deep</button>
            <button onclick="switchInterviewTab('system')" id="int-tab-system" class="tab-btn px-2.5 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">3. System Design</button>
            <button onclick="switchInterviewTab('behavioral')" id="int-tab-behavioral" class="tab-btn px-2.5 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">4. STAR Behavioral</button>
            <button onclick="switchInterviewTab('project8')" id="int-tab-project8" class="tab-btn px-2.5 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">5. 8 Deep Project Qs</button>
          </div>
        </div>

        <div class="p-6">
          <div id="int-content-coding" class="space-y-3 text-xs text-slate-300">
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Data Structures & Optimization:</span> Focus on HashMaps, sliding window algorithms, binary search, and time/space complexity tradeoffs (Big-O).
            </div>
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Async Python & Concurrency:</span> Be ready to write asyncio task pools, generators, and multi-threaded data consumers.
            </div>
          </div>

          <div id="int-content-ml" class="hidden space-y-3 text-xs text-slate-300">
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Loss Functions & Optimizers:</span> Cross-entropy vs MSE, AdamW vs SGD, learning rate scheduling, and gradient clipping.
            </div>
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Attention & Transformers:</span> Self-attention math (Q, K, V matrices), KV caching in LLMs, and LoRA fine-tuning mechanics.
            </div>
          </div>

          <div id="int-content-system" class="hidden space-y-3 text-xs text-slate-300">
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">RAG Architecture at Scale:</span> Chunking strategies, semantic caching, hybrid BM25 + Vector search, and re-ranking bottlenecks.
            </div>
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Latency & Cost Profiling:</span> Designing systems with p95 &lt; 50ms and $0.0001 per request inference constraints.
            </div>
          </div>

          <div id="int-content-behavioral" class="hidden space-y-3 text-xs text-slate-300">
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">STAR Method:</span> Situation, Task, Action, Result. Always anchor your answers with measurable metrics (e.g. "reduced latency 60%").
            </div>
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Ownership Under Ambiguity:</span> Tell a story of how you resolved an unclear requirement without waiting for a manager.
            </div>
          </div>

          <div id="int-content-project8" class="hidden space-y-3 text-xs text-slate-300">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-bold text-white">1. Why this specific tech stack?</div>
                <div class="text-[11px] text-[#8888A8]">Explain why you chose FastAPI over Flask and Qdrant over Pinecone.</div>
              </div>
              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-bold text-white">2. What failed in your first prototype?</div>
                <div class="text-[11px] text-[#8888A8]">Share an authentic debugging post-mortem and how you fixed it.</div>
              </div>
              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-bold text-white">3. How did you benchmark latency?</div>
                <div class="text-[11px] text-[#8888A8]">Quote p50, p95, and p99 percentiles under Locust load testing.</div>
              </div>
              <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-bold text-white">4. What is the unit cost per inference?</div>
                <div class="text-[11px] text-[#8888A8]">Prove the economic ROI of your hybrid architecture.</div>
              </div>
            </div>
          </div>
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 11: FREE COURSES (NEW) -->
    <!-- ========================================== -->
    <section id="courses" class="space-y-6 scroll-mt-32">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#6C63FF]">
          <i data-lucide="graduation-cap" class="w-3.5 h-3.5"></i> WORLD-CLASS BIG TECH CURRICULUM
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          12 Big Tech Free AI Courses
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          Curated curriculum from Google, DeepLearning.AI, Microsoft, Stanford, MIT, Fast.ai, and Hugging Face with 100% free audit access.
        </p>
      </div>

      <!-- 12 Free Courses Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        
        <!-- Course 1 -->
        <div class="card-surface p-5 space-y-3 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-mono text-[#00D4AA]">DeepLearning.AI</span>
              <span class="px-1.5 py-0.5 rounded bg-[#00D4AA]/10 text-[#00D4AA] text-[10px] font-mono">100% Free</span>
            </div>
            <h3 class="text-sm font-bold text-white font-heading">AI for Everyone & LangChain Series</h3>
            <p class="text-xs text-[#8888A8]">Taught by Andrew Ng. Covers generative AI fundamentals, RAG, and agentic workflows.</p>
          </div>
          <a href="https://www.deeplearning.ai/short-courses/" target="_blank" rel="noopener noreferrer" class="text-xs text-[#6C63FF] hover:underline flex items-center gap-1">
            Official Course Link <i data-lucide="external-link" class="w-3 h-3"></i>
          </a>
        </div>

        <!-- Course 2 -->
        <div class="card-surface p-5 space-y-3 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-mono text-sky-400">Google Cloud</span>
              <span class="px-1.5 py-0.5 rounded bg-sky-500/10 text-sky-400 text-[10px] font-mono">100% Free</span>
            </div>
            <h3 class="text-sm font-bold text-white font-heading">Generative AI Fundamentals</h3>
            <p class="text-xs text-[#8888A8]">Official Google learning path covering LLMs, responsible AI, and Vertex AI architecture.</p>
          </div>
          <a href="https://www.cloudskillsboost.google/course_templates/536" target="_blank" rel="noopener noreferrer" class="text-xs text-[#6C63FF] hover:underline flex items-center gap-1">
            Official Course Link <i data-lucide="external-link" class="w-3 h-3"></i>
          </a>
        </div>

        <!-- Course 3 -->
        <div class="card-surface p-5 space-y-3 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-mono text-blue-400">Microsoft Learn</span>
              <span class="px-1.5 py-0.5 rounded bg-blue-500/10 text-blue-400 text-[10px] font-mono">12 Weeks</span>
            </div>
            <h3 class="text-sm font-bold text-white font-heading">AI for Beginners Curriculum</h3>
            <p class="text-xs text-[#8888A8]">Comprehensive 24-lesson curriculum from Microsoft engineers on symbolic AI to neural networks.</p>
          </div>
          <a href="https://microsoft.github.io/AI-For-Beginners/" target="_blank" rel="noopener noreferrer" class="text-xs text-[#6C63FF] hover:underline flex items-center gap-1">
            Official Course Link <i data-lucide="external-link" class="w-3 h-3"></i>
          </a>
        </div>

        <!-- Course 4 -->
        <div class="card-surface p-5 space-y-3 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-mono text-amber-400">Fast.ai</span>
              <span class="px-1.5 py-0.5 rounded bg-amber-500/10 text-amber-400 text-[10px] font-mono">Top Pick</span>
            </div>
            <h3 class="text-sm font-bold text-white font-heading">Practical Deep Learning for Coders</h3>
            <p class="text-xs text-[#8888A8]">Jeremy Howard's world-famous top-down approach to training modern neural networks with PyTorch.</p>
          </div>
          <a href="https://course.fast.ai/" target="_blank" rel="noopener noreferrer" class="text-xs text-[#6C63FF] hover:underline flex items-center gap-1">
            Official Course Link <i data-lucide="external-link" class="w-3 h-3"></i>
          </a>
        </div>

        <!-- Course 5 -->
        <div class="card-surface p-5 space-y-3 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-mono text-rose-400">Stanford Online</span>
              <span class="px-1.5 py-0.5 rounded bg-rose-500/10 text-rose-400 text-[10px] font-mono">Academic</span>
            </div>
            <h3 class="text-sm font-bold text-white font-heading">CS229: Machine Learning</h3>
            <p class="text-xs text-[#8888A8]">The gold standard university course for statistical learning theory and ML mathematical foundations.</p>
          </div>
          <a href="https://cs229.stanford.edu/" target="_blank" rel="noopener noreferrer" class="text-xs text-[#6C63FF] hover:underline flex items-center gap-1">
            Official Course Link <i data-lucide="external-link" class="w-3 h-3"></i>
          </a>
        </div>

        <!-- Course 6 -->
        <div class="card-surface p-5 space-y-3 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-mono text-purple-400">MIT OpenCourseWare</span>
              <span class="px-1.5 py-0.5 rounded bg-purple-500/10 text-purple-400 text-[10px] font-mono">6.S191</span>
            </div>
            <h3 class="text-sm font-bold text-white font-heading">Introduction to Deep Learning</h3>
            <p class="text-xs text-[#8888A8]">MIT's flagship course on foundation models, generative modeling, and reinforcement learning.</p>
          </div>
          <a href="http://introtodeeplearning.com/" target="_blank" rel="noopener noreferrer" class="text-xs text-[#6C63FF] hover:underline flex items-center gap-1">
            Official Course Link <i data-lucide="external-link" class="w-3 h-3"></i>
          </a>
        </div>

        <!-- Course 7 -->
        <div class="card-surface p-5 space-y-3 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-mono text-yellow-400">Hugging Face</span>
              <span class="px-1.5 py-0.5 rounded bg-yellow-500/10 text-yellow-400 text-[10px] font-mono">Hands-on</span>
            </div>
            <h3 class="text-sm font-bold text-white font-heading">NLP Course & Transformers</h3>
            <p class="text-xs text-[#8888A8]">Master the Hugging Face ecosystem, fine-tuning Transformers, tokenizers, and datasets.</p>
          </div>
          <a href="https://huggingface.co/learn/nlp-course/chapter1/1" target="_blank" rel="noopener noreferrer" class="text-xs text-[#6C63FF] hover:underline flex items-center gap-1">
            Official Course Link <i data-lucide="external-link" class="w-3 h-3"></i>
          </a>
        </div>

        <!-- Course 8 -->
        <div class="card-surface p-5 space-y-3 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-mono text-orange-400">AWS Skill Builder</span>
              <span class="px-1.5 py-0.5 rounded bg-orange-500/10 text-orange-400 text-[10px] font-mono">Cloud ML</span>
            </div>
            <h3 class="text-sm font-bold text-white font-heading">AWS Educate ML Foundations</h3>
            <p class="text-xs text-[#8888A8]">Learn AWS SageMaker, cloud inference pipelines, and scalable model hosting.</p>
          </div>
          <a href="https://aws.amazon.com/training/digital/machine-learning-foundations/" target="_blank" rel="noopener noreferrer" class="text-xs text-[#6C63FF] hover:underline flex items-center gap-1">
            Official Course Link <i data-lucide="external-link" class="w-3 h-3"></i>
          </a>
        </div>

        <!-- Course 9 -->
        <div class="card-surface p-5 space-y-3 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-mono text-emerald-400">OpenAI</span>
              <span class="px-1.5 py-0.5 rounded bg-emerald-500/10 text-emerald-400 text-[10px] font-mono">Official</span>
            </div>
            <h3 class="text-sm font-bold text-white font-heading">OpenAI Cookbook & API Guides</h3>
            <p class="text-xs text-[#8888A8]">Production code patterns for function calling, structured JSON outputs, embeddings, and fine-tuning.</p>
          </div>
          <a href="https://cookbook.openai.com/" target="_blank" rel="noopener noreferrer" class="text-xs text-[#6C63FF] hover:underline flex items-center gap-1">
            Official Course Link <i data-lucide="external-link" class="w-3 h-3"></i>
          </a>
        </div>

        <!-- Course 10 -->
        <div class="card-surface p-5 space-y-3 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-mono text-indigo-400">Full Stack Deep Learning</span>
              <span class="px-1.5 py-0.5 rounded bg-indigo-500/10 text-indigo-400 text-[10px] font-mono">Production</span>
            </div>
            <h3 class="text-sm font-bold text-white font-heading">LLM Bootcamp & Production AI</h3>
            <p class="text-xs text-[#8888A8]">Architecting real-world LLM applications with evaluation frameworks and deployment best practices.</p>
          </div>
          <a href="https://fullstackdeeplearning.com/" target="_blank" rel="noopener noreferrer" class="text-xs text-[#6C63FF] hover:underline flex items-center gap-1">
            Official Course Link <i data-lucide="external-link" class="w-3 h-3"></i>
          </a>
        </div>

        <!-- Course 11 -->
        <div class="card-surface p-5 space-y-3 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-mono text-teal-400">Weights & Biases</span>
              <span class="px-1.5 py-0.5 rounded bg-teal-500/10 text-teal-400 text-[10px] font-mono">MLOps</span>
            </div>
            <h3 class="text-sm font-bold text-white font-heading">ML Practitioner Courses</h3>
            <p class="text-xs text-[#8888A8]">Hands-on experiment tracking, model evaluation, and LLM orchestration with W&B.</p>
          </div>
          <a href="https://www.wandb.courses/" target="_blank" rel="noopener noreferrer" class="text-xs text-[#6C63FF] hover:underline flex items-center gap-1">
            Official Course Link <i data-lucide="external-link" class="w-3 h-3"></i>
          </a>
        </div>

        <!-- Course 12 -->
        <div class="card-surface p-5 space-y-3 bg-[#13131A] flex flex-col justify-between">
          <div class="space-y-1.5">
            <div class="flex items-center justify-between text-xs">
              <span class="font-mono text-red-400">Harvard CS50</span>
              <span class="px-1.5 py-0.5 rounded bg-red-500/10 text-red-400 text-[10px] font-mono">Fundamentals</span>
            </div>
            <h3 class="text-sm font-bold text-white font-heading">CS50’s Intro to AI with Python</h3>
            <p class="text-xs text-[#8888A8]">Covers search algorithms, minimax, machine learning, neural networks, and NLP from scratch.</p>
          </div>
          <a href="https://cs50.harvard.edu/ai/" target="_blank" rel="noopener noreferrer" class="text-xs text-[#6C63FF] hover:underline flex items-center gap-1">
            Official Course Link <i data-lucide="external-link" class="w-3 h-3"></i>
          </a>
        </div>

      </div>

      <!-- Recommended Learning Order Timeline -->
      <div class="card-surface p-6 space-y-4 bg-[#13131A]">
        <h3 class="text-sm font-bold text-white font-heading">Recommended Learning Progression Order</h3>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-3 text-xs">
          <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
            <div class="font-bold text-[#6C63FF]">Stage 1: Core Fundamentals</div>
            <p class="text-[11px] text-[#8888A8]">Harvard CS50 AI + DeepLearning.AI for basic mental models.</p>
          </div>
          <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
            <div class="font-bold text-[#00D4AA]">Stage 2: Applied Deep Learning</div>
            <p class="text-[11px] text-[#8888A8]">Fast.ai + Stanford CS229 for PyTorch mechanics and training.</p>
          </div>
          <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
            <div class="font-bold text-amber-400">Stage 3: LLMs & Transformers</div>
            <p class="text-[11px] text-[#8888A8]">Hugging Face NLP + OpenAI Cookbook for RAG & Agents.</p>
          </div>
          <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
            <div class="font-bold text-sky-400">Stage 4: Production MLOps</div>
            <p class="text-[11px] text-[#8888A8]">Full Stack Deep Learning + Weights & Biases for scale.</p>
          </div>
        </div>
        <p class="text-[11px] text-[#8888A8] italic">Note: All courses listed above are 100% free or audit-free without paywalls.</p>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 12: RESOURCES (EXISTING) -->
    <!-- ========================================== -->
    <section id="resources" class="space-y-6 scroll-mt-32">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
          <i data-lucide="archive" class="w-3.5 h-3.5"></i> COMPANION RESOURCE VAULT
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          Companion Resource Vault
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          Essential cheat sheets, legal templates, video pitch scripts, and compensation benchmarks.
        </p>
      </div>

      <!-- 4 Resource Cards Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        
        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono text-amber-400 font-semibold">LEGAL & TAX</span>
            <span class="text-[10px] font-mono text-[#8888A8]">W-8BEN & Wise</span>
          </div>
          <h3 class="text-sm font-bold text-white font-heading">US Contractor Legal & Tax Cheat Sheet</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Step-by-step guidance on filling Form W-8BEN, setting up cross-border Wise USD accounts, understanding section 44ADA presumptive tax in India, and contracting via single-member LLCs.
          </p>
        </div>

        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono text-[#00D4AA] font-semibold">PORTFOLIO</span>
            <span class="text-[10px] font-mono text-[#8888A8]">High-Signal Template</span>
          </div>
          <h3 class="text-sm font-bold text-white font-heading">High-Converting Portfolio Checklist & Template</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Architecture diagram guidelines, public endpoint health-check setup, latency benchmarking tables, and failure post-mortem writeup templates.
          </p>
        </div>

        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono text-[#6C63FF] font-semibold">OUTREACH VIDEO</span>
            <span class="text-[10px] font-mono text-[#8888A8]">120-Sec Script</span>
          </div>
          <h3 class="text-sm font-bold text-white font-heading">Loom Video Pitch Script for Engineering Roles</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            A word-for-word 2-minute video pitch script walking through your project architecture, cost math, and proposing a 1-week paid trial milestone.
          </p>
        </div>

        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="flex items-center justify-between">
            <span class="text-xs font-mono text-sky-400 font-semibold">COMPENSATION</span>
            <span class="text-[10px] font-mono text-[#8888A8]">Levels & Wellfound</span>
          </div>
          <h3 class="text-sm font-bold text-white font-heading">Remote Tech Compensation Benchmarks</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Real market contractor rate percentiles ($35/hr, $50/hr, $75/hr, $100/hr) across US Seed, Series A, and Series B venture-backed tech startups.
          </p>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 13: FINAL CHECKLIST (NEW) -->
    <!-- ========================================== -->
    <section id="final-checklist" class="space-y-6 scroll-mt-32">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="space-y-2">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
            <i data-lucide="list-checks" class="w-3.5 h-3.5"></i> FINAL PRE-LAUNCH VERIFICATION
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
            Final Readiness Checklist
          </h2>
          <p class="text-sm text-[#8888A8] text-prose">
            Verify your profile, portfolio, outreach infrastructure, and interview readiness before sending your first application.
          </p>
        </div>
        <div class="text-right">
          <div id="final-checklist-progress-badge" class="text-sm font-bold font-mono text-[#00D4AA]">0 / 12 complete (0%)</div>
          <div class="w-32 bg-[#13131A] h-2 rounded-full overflow-hidden border border-[#2A2A3A] mt-1 ml-auto">
            <div id="final-checklist-progress-bar" class="bg-[#00D4AA] h-full rounded-full transition-all duration-300" style="width: 0%"></div>
          </div>
        </div>
      </div>

      <!-- 12-Item Interactive Checklist Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3" id="final-checklist-items-container">
        <!-- Rendered via JS -->
      </div>

      <div class="flex items-center justify-between pt-2">
        <button onclick="resetFinalChecklist()" class="text-xs text-[#8888A8] hover:text-white flex items-center gap-1 transition">
          <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i> Reset Final Checklist
        </button>
      </div>

      <!-- Final Career Rule Callout -->
      <div class="p-6 rounded-xl bg-[#13131A] border border-[#6C63FF]/50 space-y-3">
        <div class="flex items-center gap-2 text-[#6C63FF] font-bold text-sm font-heading">
          <i data-lucide="award" class="w-5 h-5"></i>
          The Golden Rule of Remote US Engineering
        </div>
        <p class="text-xs sm:text-sm text-slate-200 leading-relaxed italic">
          "US companies don't hire remote international engineers to save money on juniors — they hire them to acquire self-directed, autonomous senior talent that communicates flawlessly and solves high-leverage problems without handholding."
        </p>
      </div>

    </section>

  </main>

  <!-- FOOTER -->
  <footer class="mt-20 border-t border-[#2A2A3A] bg-[#0A0A0F] py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col md:flex-row items-center justify-between gap-6">
      
      <div class="space-y-1 text-center md:text-left">
        <div class="font-heading font-bold text-white text-base flex items-center justify-center md:justify-start gap-2">
          <div class="w-6 h-6 rounded bg-[#6C63FF] flex items-center justify-center text-xs font-bold text-white">N</div>
          Naraito's Playbook
        </div>
        <p class="text-xs text-[#8888A8]">Mastering US Remote Engineering Jobs ($60K–$120K) | 0-Experience Edition</p>
      </div>

      <div class="flex flex-wrap items-center justify-center gap-4 text-xs text-[#8888A8]">
        <a href="#start-here" class="hover:text-white transition">Start Here</a>
        <a href="#roadmap-90" class="hover:text-white transition">90-Day Roadmap</a>
        <a href="#filters" class="hover:text-white transition">5 Filters</a>
        <a href="#projects" class="hover:text-white transition">Blueprints</a>
        <a href="#linkedin" class="hover:text-white transition">LinkedIn</a>
        <a href="#job-search" class="hover:text-white transition">Job Search Engine</a>
        <a href="#courses" class="hover:text-white transition">Free Courses</a>
        <button onclick="exportUserDataJSON()" class="text-[#00D4AA] hover:underline">Export Data</button>
      </div>

      <div class="text-xs text-[#8888A8] text-center md:text-right">
        &copy; 2026 Naraito's Playbook. All rights reserved.
      </div>
    </div>
  </footer>

  <!-- ========================================== -->
  <!-- MODALS (BLUEPRINT, LEADS, PROPOSAL, BACKUP)-->
  <!-- ========================================== -->

  <!-- 1. Blueprint README Modal -->
  <div id="blueprint-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="card-surface bg-[#13131A] max-w-3xl w-full max-h-[90vh] flex flex-col overflow-hidden">
      <div class="p-4 border-b border-[#2A2A3A] flex items-center justify-between">
        <h3 id="bp-modal-title" class="font-heading font-bold text-white text-base">Blueprint Details</h3>
        <button onclick="closeModal('blueprint-modal')" class="text-slate-400 hover:text-white p-1"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>
      <div class="p-6 overflow-y-auto space-y-4 text-xs">
        <div id="bp-modal-content" class="space-y-3"></div>
      </div>
    </div>
  </div>

  <!-- 2. 300+ Curated Leads Database Modal -->
  <div id="leads-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="card-surface bg-[#13131A] max-w-5xl w-full max-h-[90vh] flex flex-col overflow-hidden">
      <div class="p-4 border-b border-[#2A2A3A] flex items-center justify-between gap-4">
        <div>
          <h3 class="font-heading font-bold text-white text-base flex items-center gap-2">
            <i data-lucide="database" class="w-4 h-4 text-[#00D4AA]"></i> 300+ Curated US/Canadian Decision-Maker Leads
          </h3>
          <p class="text-xs text-[#8888A8]">Filter target companies and add them directly to your Outbound CRM.</p>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="exportLeadsCSV()" class="px-3 py-1.5 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-xs text-white flex items-center gap-1.5">
            <i data-lucide="download" class="w-3.5 h-3.5"></i> Export CSV
          </button>
          <button onclick="closeModal('leads-modal')" class="text-slate-400 hover:text-white p-1"><i data-lucide="x" class="w-5 h-5"></i></button>
        </div>
      </div>

      <!-- Search & Filters Bar -->
      <div class="p-4 border-b border-[#2A2A3A] bg-[#1C1C27] flex flex-wrap items-center gap-3">
        <div class="flex-1 min-w-[200px]">
          <input type="text" id="lead-search-input" placeholder="Search company, founder, or category..." oninput="filterLeadsTable()" class="w-full px-3 py-1.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-white focus:border-[#6C63FF] focus:outline-none">
        </div>
        <select id="lead-category-filter" onchange="filterLeadsTable()" class="px-3 py-1.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-slate-300 focus:border-[#6C63FF] focus:outline-none">
          <option value="ALL">All Categories</option>
          <option value="AI">AI / Machine Learning</option>
          <option value="Health">Health Care / BioTech</option>
          <option value="SaaS">SaaS / Enterprise</option>
          <option value="Fintech">Fintech / Security</option>
        </select>
        <span id="leads-count-badge" class="text-xs font-mono text-[#00D4AA]">Showing 300+ leads</span>
      </div>

      <!-- Leads Table Container -->
      <div class="flex-1 overflow-y-auto p-4">
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead>
              <tr class="border-b border-[#2A2A3A] text-[#8888A8]">
                <th class="p-2.5">Company</th>
                <th class="p-2.5">Category</th>
                <th class="p-2.5">Location</th>
                <th class="p-2.5">Links</th>
                <th class="p-2.5 text-right">Action</th>
              </tr>
            </thead>
            <tbody id="leads-table-body" class="divide-y divide-[#2A2A3A]">
              <!-- Rendered dynamically via JS -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>

  <!-- 3. Proposal Generator Modal -->
  <div id="proposal-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="card-surface bg-[#13131A] max-w-2xl w-full max-h-[90vh] flex flex-col overflow-hidden">
      <div class="p-4 border-b border-[#2A2A3A] flex items-center justify-between">
        <h3 class="font-heading font-bold text-white text-base">Risk-Reversal Proposal Generator</h3>
        <button onclick="closeModal('proposal-modal')" class="text-slate-400 hover:text-white p-1"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>
      <div class="p-6 overflow-y-auto space-y-4 text-xs">
        <div class="grid grid-cols-2 gap-3">
          <input type="text" id="prop-founder" placeholder="Founder Name" value="Alex" oninput="renderProposalLetter()" class="p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white">
          <input type="text" id="prop-company" placeholder="Startup Name" value="VentureScale AI" oninput="renderProposalLetter()" class="p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white">
          <input type="text" id="prop-deliverable" placeholder="1-Week Deliverable" value="Hybrid Classifier with 70% Cost Reduction" oninput="renderProposalLetter()" class="p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white">
          <input type="text" id="prop-rate" placeholder="Trial Rate (e.g. $1,250)" value="$1,250" oninput="renderProposalLetter()" class="p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white">
        </div>
        <textarea id="prop-output-text" rows="10" class="w-full p-3 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-slate-200 font-mono leading-relaxed"></textarea>
        <button onclick="copyProposalLetter()" class="w-full py-2.5 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition">
          <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy Proposal Letter
        </button>
      </div>
    </div>
  </div>

  <!-- 4. Data Backup & CRM Import/Export Modal -->
  <div id="backup-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="card-surface bg-[#13131A] max-w-md w-full flex flex-col overflow-hidden">
      <div class="p-4 border-b border-[#2A2A3A] flex items-center justify-between">
        <h3 class="font-heading font-bold text-white text-base flex items-center gap-2">
          <i data-lucide="hard-drive" class="w-4 h-4 text-[#6C63FF]"></i> Data & CRM Backup
        </h3>
        <button onclick="closeModal('backup-modal')" class="text-slate-400 hover:text-white p-1"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>
      <div class="p-6 space-y-4 text-xs">
        <p class="text-[#8888A8]">Your progress, checklist states, and Kanban CRM leads are stored locally in your browser. Export a JSON backup to keep your data safe.</p>
        
        <div class="space-y-2">
          <button onclick="exportUserDataJSON()" class="w-full py-2.5 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white font-semibold flex items-center justify-center gap-1.5 transition">
            <i data-lucide="download" class="w-3.5 h-3.5"></i> Export Complete Data JSON
          </button>
          
          <label class="w-full py-2.5 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-slate-200 font-semibold flex items-center justify-center gap-1.5 cursor-pointer transition">
            <i data-lucide="upload" class="w-3.5 h-3.5 text-[#00D4AA]"></i> Import Data JSON
            <input type="file" accept=".json" onchange="importUserDataJSON(event)" class="hidden">
          </label>
        </div>
      </div>
    </div>
  </div>

  <!-- 5. Toast Notification Popup Container -->
  <div id="toast-container" class="fixed bottom-5 right-5 z-50 space-y-2 pointer-events-none"></div>

  <!-- EMBEDDED JAVASCRIPT LIBRARIES & APP ENGINE -->
  <script>
    // Embedded Preloaded Leads
    {curated_leads_content}

    // Embedded Application Engine
    {app_js_content}
  </script>
</body>
</html>
"""

with open(r'D:\us-remote-engineering-playbook\index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated complete index.html successfully!")
