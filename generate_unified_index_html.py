# Python script to build the complete, unified, high-fidelity Naraito's Playbook single-file web app
import os
import re

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
              500: '#6C63FF', // Accent Primary
              600: '#584fe6',
              700: '#4338ca',
            }},
            teal: {{
              400: '#2dd4bf',
              500: '#00D4AA', // Accent Secondary
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

    /* Line Length Constraint for Readability (72-80ch) */
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
        <button id="mobile-menu-btn" class="lg:hidden p-2 text-[#8888A8] hover:text-white rounded-lg hover:bg-[#1C1C27] transition" aria-label="Toggle Navigation">
          <i data-lucide="menu" class="w-5 h-5"></i>
        </button>
        <a href="#hero-section" class="flex items-center gap-2.5 group">
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
        <button id="backup-btn" onclick="openBackupModal()" class="px-3 py-1.5 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-white text-xs font-medium flex items-center gap-1.5 transition">
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
    <div id="mobile-pill-nav" class="border-t border-[#2A2A3A] bg-[#13131A]/90 backdrop-blur-md overflow-x-auto scrollbar-none py-2 px-4 sm:px-6 lg:px-8">
      <div class="max-w-7xl mx-auto flex items-center gap-2">
        <a href="#hero-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Start Here</a>
        <a href="#roadmap-90-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">90-Day Roadmap</a>
        <a href="#filters-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">5 Filters</a>
        <a href="#reality-check-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Reality Check</a>
        <a href="#roadmap-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Execution Roadmap</a>
        <a href="#blueprints-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Projects</a>
        <a href="#offer-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Offer Framework</a>
        <a href="#linkedin-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">LinkedIn Studio</a>
        <a href="#outreach-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Outreach CRM</a>
        <a href="#job-search-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Job Search Engine</a>
        <a href="#courses-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Free Courses</a>
        <a href="#resources-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Resources</a>
        <a href="#final-checklist-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Final Checklist</a>
      </div>
    </div>
  </header>

  <!-- MAIN PLAYBOOK CONTENT -->
  <main class="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-16">

    <!-- ========================================== -->
    <!-- SECTION 1: START HERE (HERO & ARBITRAGE) -->
    <!-- ========================================== -->
    <section id="hero-section" class="space-y-8 scroll-mt-32">
      
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
                <span class="text-slate-300 font-medium">Target US Contractor Salary (Annual USD):</span>
                <span id="calc-salary-display" class="font-mono font-bold text-[#00D4AA] text-sm">$80,000 / year</span>
              </div>
              <input type="range" min="40000" max="150000" step="5000" value="80000" oninput="updateArbitrageCalculator(this.value)" class="w-full bg-[#1C1C27] rounded-lg h-2 accent-[#6C63FF] cursor-pointer">
              <div class="flex justify-between text-[10px] text-[#8888A8]">
                <span>$40K ($20/hr)</span>
                <span>$80K ($40/hr)</span>
                <span>$150K ($75/hr)</span>
              </div>
            </div>

            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="text-xs font-mono text-[#8888A8] uppercase">Founder Cost Advantage</div>
              <div class="flex justify-between text-xs text-slate-300">
                <span>Equivalent SF Local Engineer Cost:</span>
                <span class="font-mono text-slate-400">$300,000 / yr</span>
              </div>
              <div class="flex justify-between text-xs text-slate-300 font-bold">
                <span>US Founder Annual Cash Saved:</span>
                <span id="calc-founder-savings" class="font-mono text-[#00D4AA]">$220,000 / yr</span>
              </div>
            </div>
          </div>

          <!-- Dynamic Results Summary -->
          <div class="grid grid-cols-2 gap-4">
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="text-[11px] text-[#8888A8]">Monthly USD Payout</div>
              <div id="calc-usd-monthly" class="text-lg sm:text-xl font-bold font-mono text-white">$6,667 / mo</div>
              <div class="text-[10px] text-slate-400">Direct wire to Wise/Bank</div>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="text-[11px] text-[#8888A8]">Annual Local Equivalent</div>
              <div id="calc-inr-annual" class="text-lg sm:text-xl font-bold font-mono text-amber-400">₹69,20,000</div>
              <div class="text-[10px] text-slate-400">@ current exchange rates</div>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#00D4AA]/40 space-y-1">
              <div class="text-[11px] text-[#00D4AA] font-semibold">Wealth Multiplier</div>
              <div id="calc-multiplier" class="text-lg sm:text-xl font-bold font-mono text-[#00D4AA]">8.7x</div>
              <div class="text-[10px] text-slate-400">vs local median developer</div>
            </div>
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#6C63FF]/40 space-y-1">
              <div class="text-[11px] text-[#6C63FF] font-semibold">Net Savings Rate</div>
              <div class="text-lg sm:text-xl font-bold font-mono text-[#6C63FF]">75%–85%</div>
              <div class="text-[10px] text-slate-400">Under section 44ADA / local tax</div>
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
    <section id="roadmap-90-section" class="space-y-6 scroll-mt-32">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
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
        <div class="text-right">
          <div id="roadmap-90-progress-badge" class="text-xs font-mono font-bold text-[#00D4AA] bg-[#13131A] px-3 py-1.5 rounded-lg border border-[#2A2A3A]">
            0/12 Outputs (0%)
          </div>
        </div>
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

          <!-- Required Outputs Checkboxes (Rendered by JS) -->
          <div class="pt-4 border-t border-[#2A2A3A] space-y-2">
            <div class="text-[11px] font-mono uppercase text-[#6C63FF] font-semibold">Required Outputs:</div>
            <div id="roadmap-90-p1-outputs" class="space-y-2 text-xs">
              <!-- Dynamically populated by render90DayRoadmap() -->
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

          <!-- Required Outputs Checkboxes (Rendered by JS) -->
          <div class="pt-4 border-t border-[#2A2A3A] space-y-2">
            <div class="text-[11px] font-mono uppercase text-[#00D4AA] font-semibold">Required Outputs:</div>
            <div id="roadmap-90-p2-outputs" class="space-y-2 text-xs">
              <!-- Dynamically populated by render90DayRoadmap() -->
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

          <!-- Required Outputs Checkboxes (Rendered by JS) -->
          <div class="pt-4 border-t border-[#2A2A3A] space-y-2">
            <div class="text-[11px] font-mono uppercase text-amber-400 font-semibold">Required Outputs:</div>
            <div id="roadmap-90-p3-outputs" class="space-y-2 text-xs">
              <!-- Dynamically populated by render90DayRoadmap() -->
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 3: THE 5 FILTERS (MODULE 1) -->
    <!-- ========================================== -->
    <section id="filters-section" class="space-y-6 scroll-mt-32">
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
        
        <!-- 5-Question Audit Tool (7 Cols) -->
        <div class="card-surface p-6 space-y-6 bg-[#13131A] lg:col-span-7">
          <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
            <div>
              <h3 class="text-base font-bold text-white font-heading flex items-center gap-2">
                <i data-lucide="check-circle-2" class="w-4 h-4 text-[#00D4AA]"></i>
                5-Question Remote Readiness Audit
              </h3>
              <p class="text-xs text-[#8888A8]">Test how a US venture-backed founder would evaluate your behavioral instinct.</p>
            </div>
            <div class="flex items-center gap-2">
              <span id="audit-readiness-label" class="text-xs font-mono text-[#8888A8]">Audit In Progress</span>
              <div id="audit-score-circle" class="font-mono text-xs text-[#00D4AA] bg-[#1C1C27] px-2.5 py-1 rounded border border-[#2A2A3A]">
                ?%
              </div>
            </div>
          </div>

          <div id="audit-questions-container" class="space-y-6">
            <!-- Questions rendered via JS -->
          </div>

          <!-- Dynamic Result Box -->
          <div id="audit-result-card" class="hidden p-5 rounded-xl bg-[#1C1C27] border border-[#00D4AA]/40 space-y-3">
            <div class="flex items-center justify-between">
              <h4 id="audit-result-title" class="font-heading font-bold text-sm text-white">Score Result</h4>
              <span id="audit-result-score-large" class="font-mono font-bold text-base text-[#00D4AA]">80%</span>
            </div>
            <p id="audit-result-desc" class="text-xs text-[#8888A8] leading-relaxed"></p>
            <div id="audit-result-recommendations" class="text-xs text-slate-300 p-3 rounded-lg bg-[#13131A] border border-[#2A2A3A]"></div>
          </div>

          <div class="pt-4 border-t border-[#2A2A3A] flex items-center justify-between">
            <button onclick="resetAudit()" class="text-xs text-[#8888A8] hover:text-white flex items-center gap-1.5 transition">
              <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i> Retake Audit
            </button>
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
            <video id="webcam-preview" autoplay playsinline muted class="w-full h-full object-cover hidden"></video>
            <div id="webcam-placeholder" class="text-center p-4 space-y-2">
              <i data-lucide="camera" class="w-8 h-8 text-[#8888A8] mx-auto"></i>
              <p class="text-xs text-[#8888A8]">Camera stream is currently inactive.</p>
            </div>
            <div id="camera-overlay" class="hidden absolute inset-0 pointer-events-none border border-emerald-500/30 flex flex-col justify-between p-3">
              <div class="flex justify-between items-center text-[10px] font-mono text-emerald-400 bg-black/60 px-2 py-0.5 rounded w-fit">
                <span>EYE LEVEL LINE</span>
              </div>
              <div class="w-full border-b border-dashed border-emerald-500/50"></div>
              <div class="text-[10px] font-mono text-slate-400 bg-black/60 px-2 py-0.5 rounded w-fit self-end">
                ALIGN EYES TO UPPER THIRD
              </div>
            </div>
          </div>

          <!-- Tester Action Controls -->
          <div class="pt-2 flex gap-2">
            <button id="start-av-btn" onclick="startCameraTest()" class="flex-1 py-2 px-3 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition">
              <i data-lucide="play" class="w-3.5 h-3.5"></i> Test Camera & Mic
            </button>
            <button id="stop-av-btn" onclick="stopCameraTest()" class="hidden py-2 px-3 rounded-lg bg-[#1C1C27] hover:bg-red-500/20 text-red-400 border border-[#2A2A3A] text-xs font-semibold flex items-center justify-center gap-1.5 transition">
              <i data-lucide="square" class="w-3.5 h-3.5"></i> Stop
            </button>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 4: REALITY CHECK (MODULE 2) -->
    <!-- ========================================== -->
    <section id="reality-check-section" class="space-y-6 scroll-mt-32">
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

        <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-4">
          <div class="space-y-1">
            <span class="text-xs font-mono text-[#6C63FF] font-semibold">SCENARIO: UNEXPECTED LLM COST SPIKE</span>
            <h4 class="text-sm font-bold text-white font-heading">
              "The founder excitedly suggests sending all 100K daily customer queries to GPT-4o for categorization."
            </h4>
            <p class="text-xs text-[#8888A8]">
              You quickly estimate this will burn $4,500/month on OpenAI API calls and add 2 seconds of latency to every user request. How do you respond?
            </p>
          </div>

          <div class="grid grid-cols-1 gap-2.5 pt-2">
            <button onclick="handleScenarioAnswer(1, 'A')" class="p-3.5 rounded-xl bg-[#13131A] hover:bg-[#1C1C27] border border-[#2A2A3A] hover:border-[#6C63FF]/50 text-left text-xs text-slate-300 transition">
              <strong class="text-white block mb-1">Option A: Deferential Ticket-Taker</strong>
              "Yes sure, I will write the Python script to call the OpenAI API for every request as you requested."
            </button>
            <button onclick="handleScenarioAnswer(1, 'B')" class="p-3.5 rounded-xl bg-[#13131A] hover:bg-[#1C1C27] border border-[#2A2A3A] hover:border-[#6C63FF]/50 text-left text-xs text-slate-300 transition">
              <strong class="text-white block mb-1">Option B: Blunt Blocker</strong>
              "No, that's too expensive and slow. We cannot do this."
            </button>
            <button onclick="handleScenarioAnswer(1, 'C')" class="p-3.5 rounded-xl bg-[#13131A] hover:bg-[#1C1C27] border border-[#2A2A3A] hover:border-[#6C63FF]/50 text-left text-xs text-slate-300 transition">
              <strong class="text-white block mb-1">Option C: High-Agency Business-First Engineer (Recommended)</strong>
              "Ran the math on this: 100K calls to GPT-4o will cost ~$4,500/mo. I've designed a 3-tier routing prototype: Regex rules catch 50% ($0), FastText catches 35% ($5/mo), and Claude Haiku only evaluates the 15% complex edge cases ($40/mo). Total cost: $45/mo (99% savings) with sub-30ms p95 latency. Recorded a 90-sec Loom with the benchmark table."
            </button>
          </div>

          <div id="scenario-feedback-box" class="hidden"></div>
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 5: EXECUTION ROADMAP (MODULE 3) -->
    <!-- ========================================== -->
    <section id="roadmap-section" class="space-y-6 scroll-mt-32">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="space-y-2">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#6C63FF]">
            <i data-lucide="milestone" class="w-3.5 h-3.5"></i> MODULE 3: 24-MILESTONE EXECUTION SYSTEM
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
            Execution Roadmap: The 4-Phase System
          </h2>
          <p class="text-sm text-[#8888A8] text-prose">
            A complete step-by-step checklist to take you from 0 experience to a signed $60K–$120K US remote contract.
          </p>
        </div>
        <div class="text-right flex items-center gap-3">
          <span id="roadmap-counter-badge" class="px-2.5 py-1 rounded-md bg-[#13131A] border border-[#2A2A3A] font-mono text-xs text-[#00D4AA]">0/24</span>
          <div id="roadmap-total-percentage" class="text-xl font-bold font-mono text-[#00D4AA]">0%</div>
        </div>
      </div>

      <!-- Phase Tabs Navigation -->
      <div class="card-surface bg-[#13131A] overflow-hidden">
        <div class="border-b border-[#2A2A3A] bg-[#1C1C27] overflow-x-auto scrollbar-none flex">
          <button onclick="switchRoadmapPhase(1)" id="phase-tab-1" class="tab-btn active px-4 py-3 text-xs font-semibold text-white bg-[#6C63FF] whitespace-nowrap">
            Phase 1: Proof of Work
          </button>
          <button onclick="switchRoadmapPhase(2)" id="phase-tab-2" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            Phase 2: Risk Reversal
          </button>
          <button onclick="switchRoadmapPhase(3)" id="phase-tab-3" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            Phase 3: LinkedIn Magnet
          </button>
          <button onclick="switchRoadmapPhase(4)" id="phase-tab-4" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            Phase 4: Outbound & Closing
          </button>
        </div>

        <!-- 4 Phase Checklist Containers (Rendered by JS) -->
        <div class="p-6">
          <div id="phase-content-1" class="space-y-3">
            <div id="phase-1-checklist" class="space-y-3"></div>
          </div>
          <div id="phase-content-2" class="hidden space-y-3">
            <div id="phase-2-checklist" class="space-y-3"></div>
          </div>
          <div id="phase-content-3" class="hidden space-y-3">
            <div id="phase-3-checklist" class="space-y-3"></div>
          </div>
          <div id="phase-content-4" class="hidden space-y-3">
            <div id="phase-4-checklist" class="space-y-3"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 6: PROJECT BLUEPRINTS -->
    <!-- ========================================== -->
    <section id="blueprints-section" class="space-y-6 scroll-mt-32">
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

      <!-- 6 Blueprints Container (Rendered dynamically by renderBlueprints()) -->
      <div id="blueprints-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Rendered via JS -->
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
          <button onclick="loadSampleJD()" class="text-xs text-[#6C63FF] hover:underline font-mono">Load Sample JD</button>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-4">
          <div class="lg:col-span-6 space-y-2">
            <textarea id="jd-input-text" rows="6" placeholder="Paste target skills (e.g. 'FastAPI, LangChain, RAG, PyTorch, Kafka, AWS, low-latency search')..." class="w-full p-3 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-slate-200 focus:border-[#6C63FF] focus:outline-none"></textarea>
            <div class="flex gap-2">
              <button onclick="analyzeJDAndGenerateBlueprint()" class="px-4 py-2 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center gap-1.5 transition">
                <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Map Optimal Project Architecture
              </button>
            </div>
          </div>
          <div class="lg:col-span-6 p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] flex flex-col justify-between space-y-2">
            <div id="jd-output-content" class="text-xs text-slate-300">
              <p class="text-[#8888A8] italic">Click "Map Optimal Project Architecture" or "Load Sample JD" to see tailored architectural recommendations and anti-resume proof points.</p>
            </div>
            <div class="pt-2 border-t border-[#2A2A3A] flex justify-end">
              <button onclick="copyJDOutput()" class="text-xs text-[#00D4AA] hover:underline flex items-center gap-1">
                <i data-lucide="copy" class="w-3 h-3"></i> Copy Plan
              </button>
            </div>
          </div>
        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 7: OFFER FRAMEWORK -->
    <!-- ========================================== -->
    <section id="offer-section" class="space-y-6 scroll-mt-32">
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
        <button onclick="openProposalGeneratorModal()" class="px-5 py-2.5 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center gap-2 transition shrink-0">
          <i data-lucide="file-text" class="w-4 h-4"></i> Open Proposal Generator
        </button>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 8: LINKEDIN STUDIO -->
    <!-- ========================================== -->
    <section id="linkedin-section" class="space-y-6 scroll-mt-32">
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
          <button onclick="switchLinkedInTab('content')" id="li-tab-content" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            3x/Week Scheduler
          </button>
          <button onclick="switchLinkedInTab('launch30')" id="li-tab-launch30" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            30-Day Launch Plan
          </button>
        </div>

        <!-- Tab 1: 16 Headlines -->
        <div id="li-content-headlines" class="p-6 space-y-4">
          <div class="flex items-center justify-between">
            <div class="text-xs text-[#8888A8]">Click any headline formula to copy or customize.</div>
            <div class="text-xs font-mono text-[#00D4AA]">16 High-Converting Formulas</div>
          </div>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4" id="headline-formulas-grid">
            <!-- Rendered via JS -->
          </div>
        </div>

        <!-- Tab 2: 5-Block About Generator -->
        <div id="li-content-about" class="hidden p-6 space-y-6">
          <div class="space-y-4">
            <div class="flex items-center justify-between">
              <span class="text-xs font-bold text-white">Choose Pre-Built Template:</span>
              <div class="flex gap-2">
                <button onclick="loadAboutTemplate('A')" class="px-2.5 py-1 rounded bg-[#1C1C27] text-xs text-slate-300 hover:text-white border border-[#2A2A3A]">Cost Optimizer</button>
                <button onclick="loadAboutTemplate('B')" class="px-2.5 py-1 rounded bg-[#1C1C27] text-xs text-slate-300 hover:text-white border border-[#2A2A3A]">System Builder</button>
                <button onclick="loadAboutTemplate('C')" class="px-2.5 py-1 rounded bg-[#1C1C27] text-xs text-slate-300 hover:text-white border border-[#2A2A3A]">Business Mindset</button>
              </div>
            </div>
            <textarea id="about-textarea" rows="10" oninput="updateAboutWordCount()" class="w-full p-3 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-slate-200 focus:border-[#6C63FF] focus:outline-none font-sans leading-relaxed"></textarea>
            <div class="flex items-center justify-between">
              <span id="about-word-count" class="text-xs font-mono text-[#8888A8]">Word Count: 0 words (Target: 150-250)</span>
              <button onclick="copyAboutText()" class="px-4 py-2 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center gap-1.5 transition">
                <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy Formatted About Bio
              </button>
            </div>
          </div>
        </div>

        <!-- Tab 3: Profile Checklist -->
        <div id="li-content-checklist" class="hidden p-6 space-y-4">
          <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
            <span class="text-xs font-bold text-white font-heading">Complete Profile Hygiene Checklist</span>
            <div class="flex items-center gap-3">
              <span id="profile-checklist-progress-badge" class="text-xs font-mono text-[#00D4AA]">0/23 completed (0%)</span>
              <div class="w-24 bg-[#0A0A0F] h-2 rounded-full overflow-hidden border border-[#2A2A3A]">
                <div id="profile-checklist-progress-bar" class="bg-[#00D4AA] h-full rounded-full transition-all" style="width: 0%"></div>
              </div>
            </div>
          </div>
          <div id="profile-checklist-container" class="space-y-4">
            <!-- Rendered via JS -->
          </div>
          <div class="pt-2 flex justify-end">
            <button onclick="resetProfileChecklist()" class="text-xs text-[#8888A8] hover:text-white flex items-center gap-1">
              <i data-lucide="rotate-ccw" class="w-3 h-3"></i> Reset Profile Checklist
            </button>
          </div>
        </div>

        <!-- Tab 4: 3-Slot Featured Strategy -->
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

        <!-- Tab 5: 3x/Week Scheduler -->
        <div id="li-content-content" class="hidden p-6 space-y-6">
          <div class="flex items-center justify-between">
            <span class="text-xs font-bold text-white">Choose Content Archetype:</span>
            <div class="flex flex-wrap gap-2">
              <button onclick="loadContentPrompt('confusion')" class="px-2.5 py-1 rounded bg-[#1C1C27] text-xs text-slate-300 hover:text-white border border-[#2A2A3A]">1. Bug / Confusion</button>
              <button onclick="loadContentPrompt('mistake')" class="px-2.5 py-1 rounded bg-[#1C1C27] text-xs text-slate-300 hover:text-white border border-[#2A2A3A]">2. Production Mistake</button>
              <button onclick="loadContentPrompt('tradeoff')" class="px-2.5 py-1 rounded bg-[#1C1C27] text-xs text-slate-300 hover:text-white border border-[#2A2A3A]">3. Math Trade-off</button>
              <button onclick="loadContentPrompt('cost')" class="px-2.5 py-1 rounded bg-[#1C1C27] text-xs text-slate-300 hover:text-white border border-[#2A2A3A]">4. Cost Optimization</button>
            </div>
          </div>
          <textarea id="post-draft-textarea" rows="10" class="w-full p-3 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-slate-200 focus:border-[#6C63FF] focus:outline-none font-sans leading-relaxed"></textarea>
          <div class="flex justify-end">
            <button onclick="copyPostDraft()" class="px-4 py-2 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center gap-1.5 transition">
              <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy Post Draft
            </button>
          </div>
        </div>

        <!-- Tab 6: 30-Day Launch Plan -->
        <div id="li-content-launch30" class="hidden p-6 space-y-4">
          <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
            <span class="text-xs font-bold text-white">Interactive 30-Day Authority Launch Plan</span>
            <div class="flex items-center gap-3">
              <span id="launch-30-progress-badge" class="text-xs font-mono text-[#00D4AA]">0/10 completed (0%)</span>
              <div class="w-24 bg-[#0A0A0F] h-2 rounded-full overflow-hidden border border-[#2A2A3A]">
                <div id="launch-30-progress-bar" class="bg-[#00D4AA] h-full rounded-full transition-all" style="width: 0%"></div>
              </div>
            </div>
          </div>
          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs">
              <tbody id="launch-30-tbody" class="divide-y divide-[#2A2A3A]">
                <!-- Rendered via JS -->
              </tbody>
            </table>
          </div>
          <div class="pt-2 flex justify-end">
            <button onclick="resetLaunch30Plan()" class="text-xs text-[#8888A8] hover:text-white flex items-center gap-1">
              <i data-lucide="rotate-ccw" class="w-3 h-3"></i> Reset 30-Day Plan
            </button>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- SECTION 9: OUTREACH CRM (MODULE 4) -->
    <!-- ========================================== -->
    <section id="outreach-section" class="space-y-6 scroll-mt-32">
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
        <button onclick="openLeadDatabaseModal()" class="px-4 py-2 rounded-lg bg-[#00D4AA] hover:bg-[#00b894] text-slate-950 font-bold text-xs flex items-center gap-2 shadow-sm transition">
          <i data-lucide="database" class="w-4 h-4"></i> Browse 300+ Curated Leads
        </button>
      </div>

      <!-- Daily Outreach Habit Tracker Counters -->
      <div class="card-surface p-5 bg-[#13131A] flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="space-y-1 text-center sm:text-left">
          <div class="text-xs font-bold text-white">Daily Outreach Goal (25 DMs / day)</div>
          <p class="text-[11px] text-[#8888A8]">Log each sent connection or message to maintain outbound momentum.</p>
        </div>
        <div class="flex items-center gap-4">
          <div class="flex items-center gap-2">
            <span id="daily-count-display" class="font-mono text-2xl font-bold text-[#00D4AA]">0</span>
            <span class="text-xs text-[#8888A8]">/ 25</span>
          </div>
          <div class="w-28 bg-[#0A0A0F] h-2 rounded-full overflow-hidden border border-[#2A2A3A]">
            <div id="daily-goal-bar" class="bg-[#00D4AA] h-full rounded-full transition-all" style="width: 0%"></div>
          </div>
          <div class="flex gap-1.5">
            <button onclick="adjustDailyCount(-1)" class="p-2 rounded bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-slate-300">
              <i data-lucide="minus" class="w-3.5 h-3.5"></i>
            </button>
            <button onclick="adjustDailyCount(1)" class="p-2 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white">
              <i data-lucide="plus" class="w-3.5 h-3.5"></i>
            </button>
          </div>
          <span id="daily-streak-badge" class="text-xs font-mono text-[#8888A8] bg-[#1C1C27] px-2 py-1 rounded border border-[#2A2A3A]">0 / 25 Today</span>
        </div>
      </div>

      <!-- 3 Cold Outreach Message Templates -->
      <div class="card-surface p-6 space-y-4 bg-[#13131A]">
        <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
          <div>
            <h3 class="text-base font-bold text-white font-heading flex items-center gap-2">
              <i data-lucide="message-square" class="w-4 h-4 text-[#6C63FF]"></i>
              3 Cold Outreach DM Templates
            </h3>
            <p class="text-xs text-[#8888A8]">Select the outreach phase and copy the proven template.</p>
          </div>
          <div class="flex gap-2">
            <button onclick="loadOutreachTemplate(1)" id="outreach-btn-1" class="tab-btn px-2.5 py-1 rounded text-xs font-semibold border border-[#00D4AA] bg-[#1C1C27] text-white">Phase 1 (Value)</button>
            <button onclick="loadOutreachTemplate(2)" id="outreach-btn-2" class="tab-btn px-2.5 py-1 rounded text-xs font-semibold border border-[#2A2A3A] bg-[#1C1C27] text-[#8888A8] hover:text-white">Phase 2 (Trade-off)</button>
            <button onclick="loadOutreachTemplate(3)" id="outreach-btn-3" class="tab-btn px-2.5 py-1 rounded text-xs font-semibold border border-[#2A2A3A] bg-[#1C1C27] text-[#8888A8] hover:text-white">Phase 3 (Loom)</button>
          </div>
        </div>

        <div class="space-y-3">
          <textarea id="outreach-template-text" rows="7" class="w-full p-3 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-slate-200 focus:border-[#6C63FF] focus:outline-none font-sans leading-relaxed"></textarea>
          <div class="flex justify-end">
            <button onclick="copyOutreachTemplate()" class="px-4 py-2 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center gap-1.5 transition">
              <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy Template
            </button>
          </div>
        </div>
      </div>

      <!-- 5-Column Kanban Board -->
      <div class="space-y-3">
        <div class="flex items-center justify-between">
          <h3 class="text-sm font-bold text-white font-heading">5-Stage Outbound Deal Pipeline</h3>
          <button onclick="openAddLeadModal()" class="px-3 py-1.5 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-xs text-white flex items-center gap-1.5 transition">
            <i data-lucide="plus" class="w-3.5 h-3.5 text-[#00D4AA]"></i> Add Custom Lead
          </button>
        </div>

        <div id="kanban-board" class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-3">
          
          <!-- Column 1: Target -->
          <div class="card-surface p-3.5 bg-[#13131A] space-y-3">
            <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-2">
              <span class="text-xs font-bold text-white font-mono">1. TARGET</span>
              <span id="col-count-target" class="text-xs font-mono text-[#8888A8]">0</span>
            </div>
            <div id="col-target-container" class="space-y-2 max-h-96 overflow-y-auto pr-1"></div>
          </div>

          <!-- Column 2: Sent -->
          <div class="card-surface p-3.5 bg-[#13131A] space-y-3">
            <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-2">
              <span class="text-xs font-bold text-[#6C63FF] font-mono">2. SENT</span>
              <span id="col-count-sent" class="text-xs font-mono text-[#6C63FF]">0</span>
            </div>
            <div id="col-sent-container" class="space-y-2 max-h-96 overflow-y-auto pr-1"></div>
          </div>

          <!-- Column 3: Conversation -->
          <div class="card-surface p-3.5 bg-[#13131A] space-y-3">
            <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-2">
              <span class="text-xs font-bold text-sky-400 font-mono">3. IN TALK</span>
              <span id="col-count-conversation" class="text-xs font-mono text-sky-400">0</span>
            </div>
            <div id="col-conversation-container" class="space-y-2 max-h-96 overflow-y-auto pr-1"></div>
          </div>

          <!-- Column 4: Interview / Trial -->
          <div class="card-surface p-3.5 bg-[#13131A] space-y-3">
            <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-2">
              <span class="text-xs font-bold text-amber-400 font-mono">4. TRIAL</span>
              <span id="col-count-interview" class="text-xs font-mono text-amber-400">0</span>
            </div>
            <div id="col-interview-container" class="space-y-2 max-h-96 overflow-y-auto pr-1"></div>
          </div>

          <!-- Column 5: Closed / Offer -->
          <div class="card-surface p-3.5 bg-[#13131A] space-y-3">
            <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-2">
              <span class="text-xs font-bold text-[#00D4AA] font-mono">5. OFFER 🏆</span>
              <span id="col-count-offer" class="text-xs font-mono text-[#00D4AA]">0</span>
            </div>
            <div id="col-offer-container" class="space-y-2 max-h-96 overflow-y-auto pr-1"></div>
          </div>

        </div>
      </div>

    </section>

    <!-- ========================================== -->
    <!-- SECTION 10: JOB SEARCH ENGINE (NEW) -->
    <!-- ========================================== -->
    <section id="job-search-section" class="space-y-8 scroll-mt-32">
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
            <button onclick="switchPlatformTab('startups')" id="platform-tab-startups" class="tab-btn px-3 py-1 text-xs font-semibold rounded-lg bg-[#6C63FF] text-white">AI-Specific</button>
            <button onclick="switchPlatformTab('remote')" id="platform-tab-remote" class="tab-btn px-3 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">Remote-First</button>
            <button onclick="switchPlatformTab('freelance')" id="platform-tab-freelance" class="tab-btn px-3 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">Reverse Networks</button>
            <button onclick="switchPlatformTab('india')" id="platform-tab-india" class="tab-btn px-3 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">Direct Outreach</button>
          </div>
        </div>

        <div class="p-6">
          <div id="platform-content-startups" class="grid grid-cols-1 md:grid-cols-3 gap-4">
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

          <div id="platform-content-remote" class="hidden grid grid-cols-1 md:grid-cols-3 gap-4">
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

          <div id="platform-content-freelance" class="hidden grid grid-cols-1 md:grid-cols-3 gap-4">
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

          <div id="platform-content-india" class="hidden grid grid-cols-1 md:grid-cols-3 gap-4">
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
            <button onclick="switchInterviewTab('python')" id="interview-tab-python" class="tab-btn px-2.5 py-1 text-xs font-semibold rounded-lg bg-[#6C63FF] text-white">1. Coding</button>
            <button onclick="switchInterviewTab('sql')" id="interview-tab-sql" class="tab-btn px-2.5 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">2. SQL</button>
            <button onclick="switchInterviewTab('ml')" id="interview-tab-ml" class="tab-btn px-2.5 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">3. ML / Deep</button>
            <button onclick="switchInterviewTab('llm')" id="interview-tab-llm" class="tab-btn px-2.5 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">4. LLM & RAG</button>
            <button onclick="switchInterviewTab('agents')" id="interview-tab-agents" class="tab-btn px-2.5 py-1 text-xs font-semibold rounded-lg bg-[#1C1C27] text-[#8888A8] hover:text-white">5. 8 Deep Project Qs</button>
          </div>
        </div>

        <div class="p-6">
          <div id="interview-content-python" class="space-y-3 text-xs text-slate-300">
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Data Structures & Optimization:</span> Focus on HashMaps, sliding window algorithms, binary search, and time/space complexity tradeoffs (Big-O).
            </div>
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Async Python & Concurrency:</span> Be ready to write asyncio task pools, generators, and multi-threaded data consumers.
            </div>
          </div>

          <div id="interview-content-sql" class="hidden space-y-3 text-xs text-slate-300">
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Window Functions & Partitioning:</span> ROW_NUMBER, RANK, DENSE_RANK, and LAG/LEAD across tenant partitions.
            </div>
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Indexing & Query Plans:</span> EXPLAIN ANALYZE, B-tree vs GIN indexes, and optimizing large vector joins.
            </div>
          </div>

          <div id="interview-content-ml" class="hidden space-y-3 text-xs text-slate-300">
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Loss Functions & Optimizers:</span> Cross-entropy vs MSE, AdamW vs SGD, learning rate scheduling, and gradient clipping.
            </div>
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Attention & Transformers:</span> Self-attention math (Q, K, V matrices), KV caching in LLMs, and LoRA fine-tuning mechanics.
            </div>
          </div>

          <div id="interview-content-llm" class="hidden space-y-3 text-xs text-slate-300">
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">RAG Architecture at Scale:</span> Chunking strategies, semantic caching, hybrid BM25 + Vector search, and re-ranking bottlenecks.
            </div>
            <div class="p-3 rounded-lg bg-[#1C1C27] border border-[#2A2A3A]">
              <span class="font-bold text-white">Latency & Cost Profiling:</span> Designing systems with p95 &lt; 50ms and $0.0001 per request inference constraints.
            </div>
          </div>

          <div id="interview-content-agents" class="hidden space-y-3 text-xs text-slate-300">
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
    <section id="courses-section" class="space-y-6 scroll-mt-32">
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
    <section id="resources-section" class="space-y-6 scroll-mt-32">
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
    <section id="final-checklist-section" class="space-y-6 scroll-mt-32">
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
        <a href="#hero-section" class="hover:text-white transition">Start Here</a>
        <a href="#roadmap-90-section" class="hover:text-white transition">90-Day Roadmap</a>
        <a href="#filters-section" class="hover:text-white transition">5 Filters</a>
        <a href="#blueprints-section" class="hover:text-white transition">Blueprints</a>
        <a href="#linkedin-section" class="hover:text-white transition">LinkedIn</a>
        <a href="#job-search-section" class="hover:text-white transition">Job Search Engine</a>
        <a href="#courses-section" class="hover:text-white transition">Free Courses</a>
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

  <!-- 1. Proposal Generator Modal -->
  <div id="proposal-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="card-surface bg-[#13131A] max-w-2xl w-full max-h-[90vh] flex flex-col overflow-hidden">
      <div class="p-4 border-b border-[#2A2A3A] flex items-center justify-between">
        <h3 class="font-heading font-bold text-white text-base">Risk-Reversal Proposal Generator</h3>
        <button onclick="closeModal('proposal-modal')" class="text-slate-400 hover:text-white p-1"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>
      <div class="p-6 overflow-y-auto space-y-4 text-xs">
        <div class="grid grid-cols-2 gap-3">
          <input type="text" id="prop-founder-name" placeholder="Founder Name" value="Alex" oninput="generateProposalPreview()" class="p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white focus:border-[#6C63FF] focus:outline-none">
          <input type="text" id="prop-company-name" placeholder="Startup Name" value="NovaScale AI" oninput="generateProposalPreview()" class="p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white focus:border-[#6C63FF] focus:outline-none">
          <input type="text" id="prop-pain-point" placeholder="Pain Point" value="high LLM API costs & latency" oninput="generateProposalPreview()" class="p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white focus:border-[#6C63FF] focus:outline-none">
          <input type="text" id="prop-solution" placeholder="Solution" value="hybrid 3-tier routing architecture" oninput="generateProposalPreview()" class="p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white focus:border-[#6C63FF] focus:outline-none">
        </div>
        <textarea id="proposal-output-text" rows="10" class="w-full p-3 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-slate-200 font-mono leading-relaxed focus:border-[#6C63FF] focus:outline-none"></textarea>
        <button onclick="copyProposalOutput()" class="w-full py-2.5 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition">
          <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy Proposal Letter
        </button>
      </div>
    </div>
  </div>

  <!-- 2. Add Custom Lead Modal -->
  <div id="add-lead-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="card-surface bg-[#13131A] max-w-md w-full flex flex-col overflow-hidden">
      <div class="p-4 border-b border-[#2A2A3A] flex items-center justify-between">
        <h3 class="font-heading font-bold text-white text-base">Add Lead to Outbound CRM</h3>
        <button onclick="closeModal('add-lead-modal')" class="text-slate-400 hover:text-white p-1"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>
      <div class="p-6 space-y-3 text-xs">
        <input type="text" id="lead-name-input" placeholder="Company Name *" class="w-full p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white focus:border-[#6C63FF] focus:outline-none">
        <input type="text" id="lead-founder-input" placeholder="Founder / Tech Lead Name" class="w-full p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white focus:border-[#6C63FF] focus:outline-none">
        <select id="lead-stage-input" class="w-full p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-slate-300 focus:border-[#6C63FF] focus:outline-none">
          <option value="target">1. Target Startup</option>
          <option value="sent">2. DM Sent</option>
          <option value="conversation">3. In Discussion</option>
          <option value="interview">4. Trial / Interview</option>
          <option value="offer">5. Closed / Offer</option>
        </select>
        <input type="text" id="lead-linkedin-input" placeholder="LinkedIn URL" class="w-full p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white focus:border-[#6C63FF] focus:outline-none">
        <input type="text" id="lead-website-input" placeholder="Company Website URL" class="w-full p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white focus:border-[#6C63FF] focus:outline-none">
        <textarea id="lead-notes-input" rows="3" placeholder="Context & personalized hook notes..." class="w-full p-2.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-white focus:border-[#6C63FF] focus:outline-none"></textarea>
        
        <button onclick="saveNewLead()" class="w-full py-2.5 rounded-lg bg-[#00D4AA] hover:bg-[#00b894] text-slate-950 font-bold text-xs flex items-center justify-center gap-1.5 transition">
          <i data-lucide="plus" class="w-3.5 h-3.5"></i> Add Lead to Pipeline
        </button>
      </div>
    </div>
  </div>

  <!-- 3. 300+ Curated Leads Database Modal -->
  <div id="lead-database-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="card-surface bg-[#13131A] max-w-5xl w-full max-h-[90vh] flex flex-col overflow-hidden">
      <div class="p-4 border-b border-[#2A2A3A] flex items-center justify-between gap-4">
        <div>
          <h3 class="font-heading font-bold text-white text-base flex items-center gap-2">
            <i data-lucide="database" class="w-4 h-4 text-[#00D4AA]"></i> 300+ Curated US/Canadian Decision-Maker Leads
          </h3>
          <p class="text-xs text-[#8888A8]">Filter target companies and add them directly to your Outbound CRM.</p>
        </div>
        <button onclick="closeModal('lead-database-modal')" class="text-slate-400 hover:text-white p-1"><i data-lucide="x" class="w-5 h-5"></i></button>
      </div>

      <!-- Search & Sector Filter Pills Bar -->
      <div class="p-4 border-b border-[#2A2A3A] bg-[#1C1C27] space-y-3">
        <div class="flex items-center gap-3">
          <div class="flex-1">
            <input type="text" id="lead-search-input" placeholder="Search company, tech stack, or description..." oninput="filterPreloadedLeads(this.value)" class="w-full px-3 py-1.5 rounded-lg bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-white focus:border-[#6C63FF] focus:outline-none">
          </div>
          <span class="text-xs font-mono text-[#00D4AA] whitespace-nowrap"><span id="leads-count-filtered">300</span> Leads Available</span>
        </div>

        <!-- Quick Filter Pills -->
        <div class="flex flex-wrap gap-1.5 text-xs">
          <button onclick="filterBySector('')" id="sec-pill-all" class="sector-pill px-2.5 py-1 rounded-full bg-[#6C63FF] text-white font-bold transition">All Sectors</button>
          <button onclick="filterBySector('AI')" id="sec-pill-ai" class="sector-pill px-2.5 py-1 rounded-full bg-[#13131A] text-[#8888A8] hover:text-white border border-[#2A2A3A] transition">AI & ML</button>
          <button onclick="filterBySector('Software')" id="sec-pill-saas" class="sector-pill px-2.5 py-1 rounded-full bg-[#13131A] text-[#8888A8] hover:text-white border border-[#2A2A3A] transition">SaaS & Cloud</button>
          <button onclick="filterBySector('Health')" id="sec-pill-health" class="sector-pill px-2.5 py-1 rounded-full bg-[#13131A] text-[#8888A8] hover:text-white border border-[#2A2A3A] transition">HealthTech</button>
          <button onclick="filterBySector('Financial')" id="sec-pill-fintech" class="sector-pill px-2.5 py-1 rounded-full bg-[#13131A] text-[#8888A8] hover:text-white border border-[#2A2A3A] transition">FinTech</button>
          <button onclick="filterBySector('Vancouver')" id="sec-pill-van" class="sector-pill px-2.5 py-1 rounded-full bg-[#13131A] text-[#8888A8] hover:text-white border border-[#2A2A3A] transition">Vancouver</button>
          <button onclick="filterBySector('Toronto')" id="sec-pill-tor" class="sector-pill px-2.5 py-1 rounded-full bg-[#13131A] text-[#8888A8] hover:text-white border border-[#2A2A3A] transition">Toronto</button>
        </div>
      </div>

      <!-- Leads Table Container -->
      <div class="flex-1 overflow-y-auto p-4">
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead>
              <tr class="border-b border-[#2A2A3A] text-[#8888A8]">
                <th class="py-2.5 px-4">Company & Description</th>
                <th class="py-2.5 px-4">Categories</th>
                <th class="py-2.5 px-4">Location</th>
                <th class="py-2.5 px-4">Funding</th>
                <th class="py-2.5 px-4 text-right">Action</th>
              </tr>
            </thead>
            <tbody id="preloaded-leads-tbody" class="divide-y divide-[#2A2A3A]">
              <!-- Rendered dynamically via JS -->
            </tbody>
          </table>
        </div>
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
        <p class="text-[#8888A8]">Your progress, checklist states, and Kanban CRM leads are stored locally in your browser. Export a JSON backup to keep your data safe across devices.</p>
        
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

print("Generated complete, unified index.html successfully!")
