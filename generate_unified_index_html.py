# Python script to build the complete, unified, high-fidelity Naraito's Playbook single-file web app
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
  <meta name="description" content="Naraito's personal step-by-step system to land a $60k–$120k US remote AI engineering role from India." />
  <meta property="og:title" content="Naraito's Playbook — Zero to US Remote AI Job" />
  <meta property="og:description" content="Step-by-step interactive system: learn AI skills, build proof of work, find jobs, craft your offer, build LinkedIn, launch outreach." />
  <meta property="og:url" content="https://naraitos-playbook.vercel.app/" />
  
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
        animation: none !important;
        transition: none !important;
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
            <div class="text-[10px] uppercase font-mono text-[#8888A8]">Overall Progress:</div>
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
        <a href="#hero-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Home</a>
        <a href="#opportunity-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Opportunity</a>
        <a href="#reality-check-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Reality Check</a>
        <a href="#filters-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Diagnose</a>
        <a href="#learn-skills-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Learn Skills</a>
        <a href="#roadmap-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Build Proof</a>
        <a href="#job-search-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Find Jobs</a>
        <a href="#offer-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Craft Offer</a>
        <a href="#linkedin-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">LinkedIn</a>
        <a href="#outreach-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Outreach</a>
        <a href="#resources-section" class="nav-pill px-3 py-1 text-xs font-medium rounded-full bg-[#1C1C27] text-slate-300 border border-[#2A2A3A]">Resources</a>
      </div>
    </div>
  </header>

  <!-- TODAY'S FOCUS CARD (PART 2) -->
  <div id="todays-focus-bar" class="bg-[#13131A] border-b border-[#2A2A3A] py-2.5 px-4 sm:px-6 lg:px-8 sticky top-[105px] z-40">
    <div class="max-w-7xl mx-auto flex flex-col sm:flex-row sm:items-center justify-between gap-3">
      <div class="flex items-center gap-2.5 text-xs flex-1 min-w-0">
        <span class="px-2 py-0.5 rounded bg-[#6C63FF]/20 text-[#6C63FF] border border-[#6C63FF]/30 font-mono font-bold shrink-0 flex items-center gap-1">
          <i data-lucide="crosshair" class="w-3.5 h-3.5"></i> Today's Focus
        </span>
        <span id="todays-focus-task" class="text-slate-200 truncate font-medium">Loading your next milestone...</span>
      </div>
      <div class="flex items-center gap-3 shrink-0">
        <span id="todays-focus-progress" class="text-[11px] font-mono text-[#00D4AA] hidden md:inline">0/24 roadmap tasks complete</span>
        <button onclick="scrollToSection('roadmap-section')" class="px-3 py-1 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-medium shrink-0 transition flex items-center gap-1">
          Jump to Task &rarr;
        </button>
      </div>
    </div>
  </div>

  <!-- MAIN PLAYBOOK CONTENT (STEP-BY-STEP NUMBERED FLOW) -->
  <main class="max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-16">

    <!-- ========================================== -->
    <!-- STEP 0: HOME (HERO & ARBITRAGE CALCULATOR) -->
    <!-- ========================================== -->
    <section id="hero-section" class="space-y-8 scroll-mt-36">
      
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

        <!-- Action CTA & Readiness Check Button -->
        <div class="pt-2 flex flex-wrap gap-3 items-center">
          <button onclick="scrollToSection('filters-section')" class="px-5 py-2.5 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs sm:text-sm font-semibold flex items-center gap-2 transition shadow-lg shadow-indigo-500/20">
            Check My US Readiness &rarr;
          </button>
          <button onclick="scrollToSection('opportunity-section')" class="px-4 py-2.5 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-slate-300 text-xs sm:text-sm font-medium transition">
            Explore The Opportunity &darr;
          </button>
        </div>

        <!-- Author Card (Part 3) -->
        <div class="pt-3">
          <div class="p-3.5 rounded-xl bg-[#13131A] border border-[#2A2A3A] text-xs text-[#8888A8] flex items-center gap-3">
            <div class="w-8 h-8 rounded-full bg-[#6C63FF] flex items-center justify-center text-white font-bold font-heading text-xs shrink-0">N</div>
            <div>
              <span class="text-slate-200 font-semibold">Built by Naraito (Uduthalaboina Sai Varshith)</span> &middot; Final-year B.Tech AI/ML &middot; BITS Warangal &middot; GitHub: <a href="https://github.com/Naraito-ai" target="_blank" class="text-[#6C63FF] hover:underline">Naraito-ai</a>
            </div>
          </div>
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

        <!-- 3-Column Cost Comparison Cards Side by Side (Wrapped in overflow-x: auto) -->
        <div class="pt-4 border-t border-[#2A2A3A] space-y-3">
          <div class="text-xs font-mono uppercase tracking-wider text-[#8888A8]">Geographic Reality Comparison</div>
          <div class="overflow-x-auto">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 min-w-[600px] md:min-w-0">
              
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
        </div>

        <!-- Insight Quote Callout -->
        <div class="p-4 rounded-xl bg-[#1C1C27] border-l-4 border-[#6C63FF] text-xs sm:text-sm text-slate-300 leading-relaxed italic">
          "The goal is not just a high US salary. The goal is geographic arbitrage: earn in strong USD, live in high purchasing power, and save 70%+ of your income while building world-class engineering chops."
        </div>
      </div>

      <!-- Single Line Transition Note -->
      <div class="p-4 rounded-xl bg-[#13131A] border border-[#2A2A3A] text-center text-xs text-slate-300 font-medium">
        This is your personal step-by-step system to land a $60k–$120k US remote AI role. Follow the steps in order.
      </div>
    </section>

    <!-- ========================================== -->
    <!-- STEP 1: THE OPPORTUNITY -->
    <!-- ========================================== -->
    <section id="opportunity-section" class="space-y-6 scroll-mt-36 pt-4 border-t border-[#2A2A3A]">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
          <span class="font-bold text-[#6C63FF]">STEP 01</span> &middot; MARKET FORCES & TIMING
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          The Opportunity: Why US Startups Need You Now
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          Understand the macro shift in venture-backed tech hiring and why founders prefer high-agency international contractors.
        </p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="w-8 h-8 rounded-lg bg-[#6C63FF]/20 text-[#6C63FF] flex items-center justify-center font-bold text-sm mb-2">1</div>
          <h3 class="text-sm font-bold text-white font-heading">Runway Extension</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            US Seed and Series A founders extend their runway by 3x by hiring top international engineers at $60K–$120K instead of $250K+ in San Francisco.
          </p>
        </div>
        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="w-8 h-8 rounded-lg bg-[#00D4AA]/20 text-[#00D4AA] flex items-center justify-center font-bold text-sm mb-2">2</div>
          <h3 class="text-sm font-bold text-white font-heading">Zero Visa Friction</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            You work as an independent international B2B contractor. Submit IRS Form W-8BEN, invoice via Deel/Wise, with 0% US tax withholding and zero sponsorship.
          </p>
        </div>
        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="w-8 h-8 rounded-lg bg-amber-500/20 text-amber-400 flex items-center justify-center font-bold text-sm mb-2">3</div>
          <h3 class="text-sm font-bold text-white font-heading">Async Execution Velocity</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Startups move 24/7 with overnight development loops. With a 4-hour overlap block, tasks handed off in US evening are delivered by next morning.
          </p>
        </div>
        <div class="card-surface p-5 space-y-2 bg-[#13131A]">
          <div class="w-8 h-8 rounded-lg bg-sky-500/20 text-sky-400 flex items-center justify-center font-bold text-sm mb-2">4</div>
          <h3 class="text-sm font-bold text-white font-heading">Bypass Gatekeepers</h3>
          <p class="text-xs text-[#8888A8] leading-relaxed">
            Forget automated HR ATS portals. Deal directly with technical founders and CTOs who judge you on working code, latency metrics, and trial tasks.
          </p>
        </div>
      </div>
    </section>

    <!-- ========================================== -->
    <!-- STEP 2: REALITY CHECK -->
    <!-- ========================================== -->
    <section id="reality-check-section" class="space-y-6 scroll-mt-36 pt-4 border-t border-[#2A2A3A]">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-amber-400">
          <span class="font-bold text-[#6C63FF]">STEP 02</span> &middot; MINDSET & STANDARDS
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          Reality Check: Local Agency vs US Remote Contractor
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          See exactly why traditional Indian prep gets you rejected — and what US founders actually evaluate.
        </p>
      </div>

      <!-- 5-Dimension Comparison Table (Wrapped in overflow-x: auto) -->
      <div class="card-surface overflow-x-auto bg-[#13131A]">
        <table class="w-full text-left border-collapse text-xs sm:text-sm min-w-[650px]">
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
              Workplace Scenario Simulator: What Would You Say?
            </h3>
            <p class="text-xs text-[#8888A8]">Test your on-the-job execution judgment in live US startup situations.</p>
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
    <!-- STEP 3: DIAGNOSE YOURSELF -->
    <!-- ========================================== -->
    <section id="filters-section" class="space-y-6 scroll-mt-36 pt-4 border-t border-[#2A2A3A]">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
          <span class="font-bold text-[#6C63FF]">STEP 03</span> &middot; ELIMINATE HIRING FRICTION
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          Diagnose Yourself: The 5 Non-Negotiable Filters
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          Complete the 5-question self-audit and test your camera and audio setup.
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
            
            <div class="pt-2">
              <button onclick="scrollToSection('roadmap-section')" class="w-full py-2.5 rounded-lg bg-[#00D4AA] hover:bg-[#00b894] text-slate-950 font-bold text-xs flex items-center justify-center gap-1.5 transition">
                Proceed to Roadmap &rarr;
              </button>
            </div>
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
    <!-- STEP 4: LEARN THE RIGHT SKILLS (NEW SECTION) -->
    <!-- ========================================== -->
    <section id="learn-skills-section" class="space-y-6 scroll-mt-36 pt-4 border-t border-[#2A2A3A]">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="space-y-2">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#6C63FF]">
            <span class="font-bold text-[#6C63FF]">STEP 04</span> &middot; STRUCTURED CURRICULUM
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
            Learn The Right Skills
          </h2>
          <p class="text-sm text-[#8888A8] text-prose">
            Master Python, data handling, machine learning, generative AI, and MLOps through a structured path.
          </p>
        </div>
        <div class="text-right">
          <div id="skills-roadmap-progress-badge" class="text-xs font-mono font-bold text-[#00D4AA] bg-[#13131A] px-3 py-1.5 rounded-lg border border-[#2A2A3A]">
            0/7 Steps Complete (0%)
          </div>
        </div>
      </div>

      <!-- Step 4 Tabs Navigation -->
      <div class="card-surface bg-[#13131A] overflow-hidden">
        <div class="border-b border-[#2A2A3A] bg-[#1C1C27] overflow-x-auto scrollbar-none flex">
          <button onclick="switchLearnSkillsTab('roadmap')" id="skills-tab-roadmap" class="tab-btn px-4 py-3 text-xs font-semibold text-white bg-[#6C63FF] whitespace-nowrap">
            AI Roadmap
          </button>
          <button onclick="switchLearnSkillsTab('skills')" id="skills-tab-skills" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            Must-Have Skills
          </button>
          <button onclick="switchLearnSkillsTab('courses')" id="skills-tab-courses" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            Free Courses
          </button>
        </div>

        <!-- Tab 1: AI Roadmap Vertical Stepper -->
        <div id="skills-content-roadmap" class="p-6 space-y-6">
          <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
            <div>
              <h3 class="text-sm font-bold text-white font-heading">7-Step Interactive AI Roadmap</h3>
              <p class="text-xs text-[#8888A8]">Check off each step as you complete the learning and build outputs.</p>
            </div>
            <div class="w-28 bg-[#0A0A0F] h-2 rounded-full overflow-hidden border border-[#2A2A3A]">
              <div id="skills-roadmap-progress-bar" class="bg-[#00D4AA] h-full rounded-full transition-all" style="width: 0%"></div>
            </div>
          </div>

          <!-- Vertical Stepper Items Container (Rendered dynamically) -->
          <div id="skills-stepper-container" class="space-y-4">
            <!-- Dynamically populated by renderSkillsRoadmap() -->
          </div>

          <div class="pt-2 flex justify-end">
            <button onclick="resetSkillsRoadmap()" class="text-xs text-[#8888A8] hover:text-white flex items-center gap-1 transition">
              <i data-lucide="rotate-ccw" class="w-3 h-3"></i> Reset AI Roadmap
            </button>
          </div>
        </div>

        <!-- Tab 2: Must-Have Skills (2 Columns) -->
        <div id="skills-content-skills" class="hidden p-6 space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            <!-- Left Column: Must-Have Technical Skills -->
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-3">
              <div class="flex items-center gap-2 text-xs font-mono font-bold text-[#00D4AA] uppercase pb-2 border-b border-[#2A2A3A]">
                <i data-lucide="code-2" class="w-4 h-4"></i> Must-Have Technical Skills
              </div>
              <ol class="space-y-2 text-xs text-slate-200">
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium"><strong class="text-white">1. Python Programming</strong> &mdash; OOP, async, data structures, profiling</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium"><strong class="text-white">2. SQL and Data Handling</strong> &mdash; Pandas, DuckDB, joins, window functions</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium"><strong class="text-white">3. Machine Learning Fundamentals</strong> &mdash; Scikit-Learn, XGBoost, evaluation</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium"><strong class="text-white">4. LLM Application Development</strong> &mdash; Prompting, function calling, structured outputs</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium"><strong class="text-white">5. RAG and Vector Search</strong> &mdash; Qdrant, Chroma, chunking, hybrid search</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium"><strong class="text-white">6. AI Agents and Automation</strong> &mdash; LangGraph, CrewAI, multi-agent workflows</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium"><strong class="text-white">7. AI Evaluation</strong> &mdash; Ragas, precision/recall, toxicity & hallucination checks</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium"><strong class="text-white">8. Backend Development</strong> &mdash; FastAPI, Redis caching, REST endpoints</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium"><strong class="text-white">9. Deployment and MLOps</strong> &mdash; Docker, Prometheus, CI/CD, AWS/GCP</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium"><strong class="text-white">10. Security and Responsible AI</strong> &mdash; Prompt injection defense, PII masking</li>
              </ol>
            </div>

            <!-- Right Column: Important Complementary Skills -->
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-3">
              <div class="flex items-center gap-2 text-xs font-mono font-bold text-[#6C63FF] uppercase pb-2 border-b border-[#2A2A3A]">
                <i data-lucide="layers" class="w-4 h-4"></i> Important Complementary Skills
              </div>
              <ul class="space-y-2 text-xs text-slate-200">
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium">&bull; Git and GitHub workflows, PR etiquette, issue tracking</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium">&bull; Basic system design & microservices latency trade-offs</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium">&bull; Cloud platforms (AWS, GCP, Modal, Fly.io, Render)</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium">&bull; Data engineering fundamentals (Pipelines, ETL, streaming)</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium">&bull; Technical writing (Architecture teardowns, documentation)</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium">&bull; Product thinking (Translating business needs to code)</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium">&bull; Communication and presentation (Async Loom walkthroughs)</li>
                <li class="p-2.5 rounded-lg bg-[#13131A] border border-[#2A2A3A] font-medium">&bull; Understanding business requirements & cost consciousness</li>
              </ul>
            </div>

          </div>

          <!-- Bottom Note Callout -->
          <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#00D4AA]/40 text-xs text-slate-300 leading-relaxed italic">
            "Companies do not hire AI engineers only for knowing models. They hire people who can convert AI capabilities into reliable products."
          </div>
        </div>

        <!-- Tab 3: Free Courses -->
        <div id="skills-content-courses" class="hidden p-6 space-y-6">
          <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
            <div>
              <h3 class="text-sm font-bold text-white font-heading">Curated Free Courses & Learning Paths</h3>
              <p class="text-xs text-[#8888A8]">100% free courses from top industry organizations.</p>
            </div>
            <span class="px-2.5 py-1 rounded bg-[#00D4AA]/10 text-[#00D4AA] border border-[#00D4AA]/30 text-xs font-mono font-semibold">
              Recommended Order
            </span>
          </div>

          <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#6C63FF]/40 text-xs text-slate-300 italic">
            "Do not try to complete every course. Select one course from each stage and build a small project after completing it."
          </div>

          <div class="space-y-3 text-xs">
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white flex items-center justify-between">
                <span>1. OpenAI AI Foundations or IBM AI Fundamentals</span>
                <span class="text-[10px] font-mono text-[#00D4AA]">Stage 1: Beginner</span>
              </div>
              <p class="text-[11px] text-[#8888A8]">Beginner intro to AI, LLMs, responsible AI and prompting. Good starting point for complete beginners.</p>
            </div>

            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white flex items-center justify-between">
                <span>2. Google Machine Learning Crash Course</span>
                <span class="text-[10px] font-mono text-[#6C63FF]">Stage 2: Core ML</span>
              </div>
              <p class="text-[11px] text-[#8888A8]">Practical ML with videos, interactive visualizations and exercises. Best for learners who already understand basic Python and mathematics.</p>
            </div>

            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white flex items-center justify-between">
                <span>3. Microsoft AI for Beginners</span>
                <span class="text-[10px] font-mono text-amber-400">Stage 3: Deep Learning</span>
              </div>
              <p class="text-[11px] text-[#8888A8]">24-lesson curriculum covering neural networks, computer vision, NLP, deep learning and AI ethics.</p>
            </div>

            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white flex items-center justify-between">
                <span>4. Microsoft Generative AI for Beginners</span>
                <span class="text-[10px] font-mono text-sky-400">Stage 4: GenAI</span>
              </div>
              <p class="text-[11px] text-[#8888A8]">21 lessons on building Generative AI applications using Python or TypeScript. Covers prompting, RAG, vector databases and responsible AI.</p>
            </div>

            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white flex items-center justify-between">
                <span>5. Hugging Face LLM Course</span>
                <span class="text-[10px] font-mono text-rose-400">Stage 5: Transformers</span>
              </div>
              <p class="text-[11px] text-[#8888A8]">Detailed course on Transformers, tokenizers, datasets, fine-tuning and sharing AI applications.</p>
            </div>

            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white flex items-center justify-between">
                <span>6. Microsoft AI Agents Course or Hugging Face AI Agents Course</span>
                <span class="text-[10px] font-mono text-emerald-400">Stage 6: Agents</span>
              </div>
              <p class="text-[11px] text-[#8888A8]">Learn to build AI agents using smolagents, LlamaIndex and LangGraph.</p>
            </div>

            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
              <div class="font-bold text-white flex items-center justify-between">
                <span>7. AWS, NVIDIA or Databricks</span>
                <span class="text-[10px] font-mono text-indigo-400">Stage 7: Cloud & Scale</span>
              </div>
              <p class="text-[11px] text-[#8888A8]">Based on the jobs you want to target. Learning content is free, certification exams are separate.</p>
            </div>
          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- STEP 5: BUILD PROOF OF WORK -->
    <!-- ========================================== -->
    <section id="roadmap-section" class="space-y-8 scroll-mt-36 pt-4 border-t border-[#2A2A3A]">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="space-y-2">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
            <span class="font-bold text-[#6C63FF]">STEP 05</span> &middot; PRODUCTION ARTIFACTS
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
            Build Proof of Work
          </h2>
          <p class="text-sm text-[#8888A8] text-prose">
            Build 1–2 production-grade projects mapped to real startup job descriptions.
          </p>
        </div>
        <div class="text-right flex items-center gap-3">
          <span id="roadmap-counter-badge" class="px-2.5 py-1 rounded-md bg-[#13131A] border border-[#2A2A3A] font-mono text-xs text-[#00D4AA]">0/24</span>
          <div id="roadmap-total-percentage" class="text-xl font-bold font-mono text-[#00D4AA]">0%</div>
        </div>
      </div>

      <!-- 6 Blueprints Section -->
      <div class="space-y-4">
        <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-2">
          <h3 class="text-base font-bold text-white font-heading">6 Production-Grade Anti-Resume Blueprints</h3>
          <span class="text-xs font-mono text-[#00D4AA]">Zero Toy Projects</span>
        </div>
        <div id="blueprints-container" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <!-- Rendered via JS -->
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
              <p class="text-[#8888A8] italic">Your output will appear here.</p>
            </div>
            <div class="pt-2 border-t border-[#2A2A3A] flex justify-end">
              <button onclick="copyJDOutput()" class="text-xs text-[#00D4AA] hover:underline flex items-center gap-1">
                <i data-lucide="copy" class="w-3 h-3"></i> Copy Plan
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Execution Roadmap: The 4-Phase System -->
      <div class="card-surface bg-[#13131A] overflow-hidden">
        <div class="p-4 border-b border-[#2A2A3A] bg-[#1C1C27] flex items-center justify-between">
          <h3 class="text-base font-bold text-white font-heading">Module 3: 24-Milestone Execution System</h3>
          <span class="text-xs font-mono text-[#00D4AA]">4 Phases &middot; 24 Tasks</span>
        </div>
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

        <!-- 4 Phase Checklist Containers -->
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
    <!-- STEP 6: FIND THE RIGHT JOBS (NEW SECTION) -->
    <!-- ========================================== -->
    <section id="job-search-section" class="space-y-6 scroll-mt-36 pt-4 border-t border-[#2A2A3A]">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
          <span class="font-bold text-[#6C63FF]">STEP 06</span> &middot; MARKET DISCOVERY
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          Find The Right Jobs
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          Discover uncrowded opportunities across curated startup boards, exact job title variants, and Boolean search strings.
        </p>
      </div>

      <!-- Step 6 Tabs Container -->
      <div class="card-surface bg-[#13131A] overflow-hidden">
        <div class="border-b border-[#2A2A3A] bg-[#1C1C27] overflow-x-auto scrollbar-none flex">
          <button onclick="switchFindJobsTab('platforms')" id="findjobs-tab-platforms" class="tab-btn px-4 py-3 text-xs font-semibold text-white bg-[#6C63FF] whitespace-nowrap">
            Job Platforms (28)
          </button>
          <button onclick="switchFindJobsTab('titles')" id="findjobs-tab-titles" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            Job Titles
          </button>
          <button onclick="switchFindJobsTab('strings')" id="findjobs-tab-strings" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            Search Strings
          </button>
          <button onclick="switchFindJobsTab('roles')" id="findjobs-tab-roles" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            Open Roles
          </button>
        </div>

        <!-- Tab 1: Job Platforms (28 Platforms in 5 Categories) -->
        <div id="findjobs-content-platforms" class="p-6 space-y-6 text-xs">
          
          <!-- Category 1 -->
          <div class="space-y-3">
            <h4 class="font-bold text-sm text-white font-mono uppercase tracking-wider text-[#6C63FF] border-b border-[#2A2A3A] pb-2">
              AI, STARTUP & ENTRY-LEVEL PLATFORMS
            </h4>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>1. Wellfound</span> <a href="https://wellfound.com/jobs" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Best for startup jobs and direct access to founders. Check "Hires Remotely From" section before applying.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>2. Y Combinator: Work at a Startup</span> <a href="https://www.ycombinator.com/jobs?remote=true" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Funded YC startups, early-stage AI companies and Founding AI Engineer roles.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>3. Simplify Jobs</span> <a href="https://simplify.jobs" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">AI, ML, internship, new-grad and entry-level opportunities with application tracking tools.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>4. AIJobs.net</span> <a href="https://aijobs.net" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Dedicated job board for AI, ML, NLP, computer vision, data science and MLOps roles.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>5. Built In</span> <a href="https://builtin.com/jobs" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Tech and startup companies with salary, benefits and company culture info.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>6. Startup Jobs</span> <a href="https://startup.jobs/remote-jobs" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Large startup database with filters for remote, internships and tech stack.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>7. F6S Jobs</span> <a href="https://www.f6s.com/jobs" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Startups, accelerators and growing tech companies across different countries.</p>
              </div>
            </div>
          </div>

          <!-- Category 2 -->
          <div class="space-y-3">
            <h4 class="font-bold text-sm text-white font-mono uppercase tracking-wider text-[#00D4AA] border-b border-[#2A2A3A] pb-2">
              REMOTE-FIRST JOB BOARDS
            </h4>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>8. Himalayas</span> <a href="https://himalayas.app/jobs/worldwide" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Worldwide remote jobs with filters for country, salary, seniority, timezone and employment type.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>9. Remote Rocketship</span> <a href="https://www.remoterocketship.com" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Searches company career pages for remote opportunities not visible on major job boards.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>10. We Work Remotely</span> <a href="https://weworkremotely.com" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Remote AI, engineering, data, product and software development roles.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>11. Remote OK</span> <a href="https://remoteok.com/remote-ai-jobs" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Remote AI and engineering jobs with filters for salary, region, technology and experience.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>12. Remotive</span> <a href="https://remotive.com/remote-ai-jobs" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Curated remote software development, data and technology jobs with clearly mentioned location restrictions.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>13. Working Nomads</span> <a href="https://www.workingnomads.com" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Fully remote, full-time, part-time and contractual roles across technology careers.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>14. Remote.co</span> <a href="https://remote.co" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Remote-friendly companies and developer, data, product and technical roles.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>15. Jobspresso</span> <a href="https://jobspresso.co" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Hand-picked remote opportunities from companies in development, data, product and operations.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>16. FlexJobs</span> <a href="https://www.flexjobs.com" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Screened remote and flexible job listings. Full access may require a paid subscription.</p>
              </div>
            </div>
          </div>

          <!-- Category 3 -->
          <div class="space-y-3">
            <h4 class="font-bold text-sm text-white font-mono uppercase tracking-wider text-amber-400 border-b border-[#2A2A3A] pb-2">
              FREELANCE & VETTED TALENT NETWORKS
            </h4>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>17. Arc</span> <a href="https://arc.dev" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Full-time and freelance ML, Generative AI, deep learning and MLOps opportunities.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>18. Braintrust</span> <a href="https://www.usebraintrust.com/jobs" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Remote AI, ML, design and engineering contracts. More suitable for candidates with some professional experience.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>19. Turing</span> <a href="https://www.turing.com/jobs" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Matches developers with remote international AI opportunities after profile and skill assessments.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>20. Toptal</span> <a href="https://www.toptal.com" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Highly selective freelance network for experienced developers, data scientists and AI professionals.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>21. Contra</span> <a href="https://contra.com" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Independent projects and AI, automation or software development portfolio showcase.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>22. Upwork</span> <a href="https://www.upwork.com" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Smaller AI automation, chatbot, RAG, data analysis and machine learning projects for paid proof of work.</p>
              </div>
            </div>
          </div>

          <!-- Category 4 -->
          <div class="space-y-3">
            <h4 class="font-bold text-sm text-white font-mono uppercase tracking-wider text-sky-400 border-b border-[#2A2A3A] pb-2">
              BROAD & INDIA-FOCUSED PLATFORMS
            </h4>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-3">
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>23. LinkedIn Jobs</span> <a href="https://www.linkedin.com/jobs" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Use job-title, experience, location and "past week" filters. Combine with referrals and messages to recruiters.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>24. Indeed</span> <a href="https://in.indeed.com" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">High-volume aggregator for discovering AI openings and understanding skills companies demand.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>25. Cutshort</span> <a href="https://cutshort.io/jobs" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">India-focused technology platform with startup, product-company, AI and remote engineering roles.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="flex justify-between font-bold text-white"><span>26. Instahyre</span> <a href="https://www.instahyre.com" target="_blank" class="text-[#00D4AA] hover:underline flex items-center gap-0.5">Visit <i data-lucide="external-link" class="w-3 h-3"></i></a></div>
                <p class="text-[11px] text-[#8888A8]">Curated platform for Indian technology professionals including AI, ML, data and software engineering.</p>
              </div>
            </div>
          </div>

          <!-- Category 5 -->
          <div class="space-y-3">
            <h4 class="font-bold text-sm text-white font-mono uppercase tracking-wider text-rose-400 border-b border-[#2A2A3A] pb-2">
              TWO MORE DISCOVERY METHODS
            </h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-bold text-white">27. Direct Company Career Pages</div>
                <p class="text-[11px] text-[#8888A8]">Create a list of 30 AI companies and check their career pages every week. Many positions appear on Greenhouse, Ashby or Lever before reaching LinkedIn.</p>
              </div>
              <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-1">
                <div class="font-bold text-white">28. GitHub, X and Founder Communities</div>
                <p class="text-[11px] text-[#8888A8]">Follow AI startup founders, open-source maintainers and engineering leaders. Early-stage companies often announce internships and founding-team roles directly through their communities.</p>
              </div>
            </div>
          </div>

          <!-- Bottom Note Callout -->
          <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#6C63FF]/40 text-xs text-slate-300 italic">
            "Do not use all platforms daily. Pick: 2 startup platforms + 2 remote-first + 1 broad + 1 India-focused + 1 freelance if relevant."
          </div>

        </div>

        <!-- Tab 2: Job Titles (4 Columns) -->
        <div id="findjobs-content-titles" class="hidden p-6 space-y-6 text-xs">
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            
            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="font-mono font-bold text-[#6C63FF] border-b border-[#2A2A3A] pb-1.5 uppercase">BEGINNER & INTERNSHIP</div>
              <ul class="space-y-1 text-slate-200">
                <li>&bull; AI Engineer Intern</li>
                <li>&bull; Machine Learning Intern</li>
                <li>&bull; Data Science Intern</li>
                <li>&bull; AI Research Intern</li>
                <li>&bull; Junior Machine Learning Engineer</li>
                <li>&bull; Associate AI Engineer</li>
                <li>&bull; Graduate AI Engineer</li>
                <li>&bull; Python AI Developer</li>
              </ul>
            </div>

            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="font-mono font-bold text-[#00D4AA] border-b border-[#2A2A3A] pb-1.5 uppercase">APPLIED AI & GENERATIVE AI</div>
              <ul class="space-y-1 text-slate-200">
                <li>&bull; Applied AI Engineer</li>
                <li>&bull; AI Product Engineer</li>
                <li>&bull; Generative AI Developer</li>
                <li>&bull; LLM Engineer</li>
                <li>&bull; RAG Engineer</li>
                <li>&bull; AI Automation Engineer</li>
                <li>&bull; AI Agent Engineer</li>
                <li>&bull; Conversational AI Engineer</li>
              </ul>
            </div>

            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="font-mono font-bold text-amber-400 border-b border-[#2A2A3A] pb-1.5 uppercase">ML & PLATFORM</div>
              <ul class="space-y-1 text-slate-200">
                <li>&bull; Machine Learning Engineer</li>
                <li>&bull; Deep Learning Engineer</li>
                <li>&bull; NLP Engineer</li>
                <li>&bull; Computer Vision Engineer</li>
                <li>&bull; MLOps Engineer</li>
                <li>&bull; AI Platform Engineer</li>
                <li>&bull; Model Evaluation Engineer</li>
                <li>&bull; Data Engineer, AI/ML</li>
              </ul>
            </div>

            <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-2">
              <div class="font-mono font-bold text-sky-400 border-b border-[#2A2A3A] pb-1.5 uppercase">CUSTOMER-FACING & STARTUP</div>
              <ul class="space-y-1 text-slate-200">
                <li>&bull; AI Solutions Engineer</li>
                <li>&bull; Forward Deployed Engineer</li>
                <li>&bull; AI Implementation Engineer</li>
                <li>&bull; AI Technical Support Engineer</li>
                <li>&bull; AI Developer Advocate</li>
                <li>&bull; Founding AI Engineer</li>
              </ul>
            </div>

          </div>

          <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#00D4AA]/40 text-xs text-slate-300 italic">
            "Do not search only for 'AI Engineer.' Different companies use different titles for similar work. Select five titles that match your current skills and create job alerts for them."
          </div>
        </div>

        <!-- Tab 3: Search Strings (10 Copyable Boolean Strings) -->
        <div id="findjobs-content-strings" class="hidden p-6 space-y-6 text-xs">
          <div class="space-y-2">
            
            <div class="p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-3">
              <code class="font-mono text-slate-200 truncate">"Applied AI Engineer" AND (remote OR worldwide)</code>
              <button onclick="copySearchString('\"Applied AI Engineer\" AND (remote OR worldwide)')" class="px-3 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold shrink-0">Copy</button>
            </div>

            <div class="p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-3">
              <code class="font-mono text-slate-200 truncate">("LLM Engineer" OR "RAG Engineer") AND (junior OR intern)</code>
              <button onclick="copySearchString('(\"LLM Engineer\" OR \"RAG Engineer\") AND (junior OR intern)')" class="px-3 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold shrink-0">Copy</button>
            </div>

            <div class="p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-3">
              <code class="font-mono text-slate-200 truncate">"AI Product Engineer" AND Python AND remote</code>
              <button onclick="copySearchString('\"AI Product Engineer\" AND Python AND remote')" class="px-3 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold shrink-0">Copy</button>
            </div>

            <div class="p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-3">
              <code class="font-mono text-slate-200 truncate">("Machine Learning Intern" OR "AI Intern") AND startup</code>
              <button onclick="copySearchString('(\"Machine Learning Intern\" OR \"AI Intern\") AND startup')" class="px-3 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold shrink-0">Copy</button>
            </div>

            <div class="p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-3">
              <code class="font-mono text-slate-200 truncate">"Generative AI Developer" AND (India OR APAC OR worldwide)</code>
              <button onclick="copySearchString('\"Generative AI Developer\" AND (India OR APAC OR worldwide)')" class="px-3 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold shrink-0">Copy</button>
            </div>

            <div class="p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-3">
              <code class="font-mono text-slate-200 truncate">("Forward Deployed Engineer" OR "AI Solutions Engineer") AND remote</code>
              <button onclick="copySearchString('(\"Forward Deployed Engineer\" OR \"AI Solutions Engineer\") AND remote')" class="px-3 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold shrink-0">Copy</button>
            </div>

            <div class="p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-3">
              <code class="font-mono text-slate-200 truncate">site:jobs.ashbyhq.com ("AI Engineer" OR "LLM Engineer") remote</code>
              <button onclick="copySearchString('site:jobs.ashbyhq.com (\"AI Engineer\" OR \"LLM Engineer\") remote')" class="px-3 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold shrink-0">Copy</button>
            </div>

            <div class="p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-3">
              <code class="font-mono text-slate-200 truncate">site:jobs.lever.co ("AI Engineer" OR "Machine Learning Engineer") India</code>
              <button onclick="copySearchString('site:jobs.lever.co (\"AI Engineer\" OR \"Machine Learning Engineer\") India')" class="px-3 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold shrink-0">Copy</button>
            </div>

            <div class="p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-3">
              <code class="font-mono text-slate-200 truncate">site:boards.greenhouse.io ("AI Intern" OR "ML Intern")</code>
              <button onclick="copySearchString('site:boards.greenhouse.io (\"AI Intern\" OR \"ML Intern\")')" class="px-3 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold shrink-0">Copy</button>
            </div>

            <div class="p-3 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] flex items-center justify-between gap-3">
              <code class="font-mono text-slate-200 truncate">site:ycombinator.com/companies ("AI Engineer" OR "Machine Learning") "Remote (IN)"</code>
              <button onclick="copySearchString('site:ycombinator.com/companies (\"AI Engineer\" OR \"Machine Learning\") \"Remote (IN)\"')" class="px-3 py-1 rounded bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold shrink-0">Copy</button>
            </div>

          </div>

          <div class="p-4 rounded-xl bg-[#1C1C27] border border-[#6C63FF]/40 text-xs text-slate-300 italic">
            "Apply only to positions posted within the last 7 days. Create alerts so new roles come to you."
          </div>
        </div>

        <!-- Tab 4: Open Roles (5 Verified Cards) -->
        <div id="findjobs-content-roles" class="hidden p-6 space-y-6 text-xs">
          <div class="p-3.5 rounded-xl bg-[#1C1C27] border border-amber-500/40 text-xs text-amber-300">
            Note: "Job openings close quickly. Verify location, eligibility and current status on the official page before applying."
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            
            <!-- Card 1 -->
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-3 flex flex-col justify-between">
              <div class="space-y-2">
                <div class="flex justify-between items-start">
                  <h4 class="font-bold text-white text-sm">Machine Learning Engineer Intern (Paid)</h4>
                  <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-[#00D4AA] font-bold">Internship</span>
                </div>
                <div class="text-slate-300 font-medium">Company: Peakflo</div>
                <div class="text-[11px] text-[#8888A8]">Location: India, Remote</div>
                <div class="text-[11px] text-[#8888A8]">Type: Paid internship — Students and freshers</div>
                <div class="text-[11px] text-slate-300 font-mono pt-1">Skills: Python, machine learning, NLP, prompt engineering</div>
              </div>
              <div class="pt-3 border-t border-[#2A2A3A]">
                <a href="https://www.ycombinator.com/companies/peakflo/jobs/I4Ehwpd-machine-learning-ml-engineer-intern-paid-india-remote" target="_blank" class="w-full py-2 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition">
                  Apply on YC <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                </a>
              </div>
            </div>

            <!-- Card 2 -->
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-3 flex flex-col justify-between">
              <div class="space-y-2">
                <div class="flex justify-between items-start">
                  <h4 class="font-bold text-white text-sm">AI Applied Engineer — Voice First Internship</h4>
                  <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-[#00D4AA] font-bold">Internship</span>
                </div>
                <div class="text-slate-300 font-medium">Company: SuperKalam</div>
                <div class="text-[11px] text-[#8888A8]">Location: India, Remote</div>
                <div class="text-[11px] text-[#8888A8]">Type: Internship — Voice AI and applied ML</div>
                <div class="text-[11px] text-slate-300 font-mono pt-1">Skills: Python, Node.js, machine learning</div>
              </div>
              <div class="pt-3 border-t border-[#2A2A3A]">
                <a href="https://www.ycombinator.com/companies/superkalam/jobs/DKwCjWa-ai-applied-engineer-voice-first-internship" target="_blank" class="w-full py-2 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition">
                  Apply on YC <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                </a>
              </div>
            </div>

            <!-- Card 3 -->
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-3 flex flex-col justify-between">
              <div class="space-y-2">
                <div class="flex justify-between items-start">
                  <h4 class="font-bold text-white text-sm">Forward Deployed Engineer</h4>
                  <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-[#6C63FF]/10 text-[#6C63FF] font-bold">Full-Time</span>
                </div>
                <div class="text-slate-300 font-medium">Company: Peakflo</div>
                <div class="text-[11px] text-[#8888A8]">Location: India, Remote</div>
                <div class="text-[11px] text-[#8888A8]">Type: Full-time — 1+ year experience</div>
                <div class="text-[11px] text-slate-300 font-mono pt-1">Skills: Python, SQL, machine learning, NLP, customer problem-solving</div>
              </div>
              <div class="pt-3 border-t border-[#2A2A3A]">
                <a href="https://www.ycombinator.com/companies/peakflo/jobs/vIrPzMj-forward-deployed-engineer-fde-india-remote" target="_blank" class="w-full py-2 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition">
                  Apply on YC <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                </a>
              </div>
            </div>

            <!-- Card 4 -->
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-3 flex flex-col justify-between">
              <div class="space-y-2">
                <div class="flex justify-between items-start">
                  <h4 class="font-bold text-white text-sm">Software Engineer, AI</h4>
                  <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-[#6C63FF]/10 text-[#6C63FF] font-bold">Full-Time</span>
                </div>
                <div class="text-slate-300 font-medium">Company: Respan</div>
                <div class="text-[11px] text-[#8888A8]">Location: India, Remote</div>
                <div class="text-[11px] text-[#8888A8]">Type: Full-time — 3+ years</div>
                <div class="text-[11px] text-slate-300 font-mono pt-1">Focus: AI agents, evaluation, observability and production systems</div>
              </div>
              <div class="pt-3 border-t border-[#2A2A3A]">
                <a href="https://www.ycombinator.com/companies/respan/jobs" target="_blank" class="w-full py-2 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition">
                  Apply on YC <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                </a>
              </div>
            </div>

            <!-- Card 5 -->
            <div class="p-5 rounded-xl bg-[#1C1C27] border border-[#2A2A3A] space-y-3 flex flex-col justify-between">
              <div class="space-y-2">
                <div class="flex justify-between items-start">
                  <h4 class="font-bold text-white text-sm">AI Software Engineer, Python</h4>
                  <span class="text-[10px] font-mono px-2 py-0.5 rounded bg-[#6C63FF]/10 text-[#6C63FF] font-bold">Full-Time</span>
                </div>
                <div class="text-slate-300 font-medium">Company: Zimperium</div>
                <div class="text-[11px] text-[#8888A8]">Location: India, Remote (Bangalore)</div>
                <div class="text-[11px] text-[#8888A8]">Type: Full-time</div>
                <div class="text-[11px] text-slate-300 font-mono pt-1">Focus: AI development with strong Python and software engineering fundamentals</div>
              </div>
              <div class="pt-3 border-t border-[#2A2A3A]">
                <a href="https://jobs.lever.co/zimperium?location=Bangalore%2C+" target="_blank" class="w-full py-2 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center justify-center gap-1.5 transition">
                  Apply on Lever <i data-lucide="external-link" class="w-3.5 h-3.5"></i>
                </a>
              </div>
            </div>

          </div>
        </div>

      </div>
    </section>

    <!-- ========================================== -->
    <!-- STEP 7: CRAFT YOUR OFFER -->
    <!-- ========================================== -->
    <section id="offer-section" class="space-y-6 scroll-mt-36 pt-4 border-t border-[#2A2A3A]">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-amber-400">
          <span class="font-bold text-[#6C63FF]">STEP 07</span> &middot; ZERO-RISK HIRING FRAMEWORK
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          Craft Your Offer: The Risk-Reversal Framework
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          Eliminate every reason a founder has to say no before they ask.
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
    <!-- STEP 8: BUILD YOUR LINKEDIN -->
    <!-- ========================================== -->
    <section id="linkedin-section" class="space-y-6 scroll-mt-36 pt-4 border-t border-[#2A2A3A]">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
          <span class="font-bold text-[#6C63FF]">STEP 08</span> &middot; INBOUND AUTHORITY MAGNET
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          Build Your LinkedIn: Inbound Authority Magnet
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          Build your LinkedIn into an inbound system that makes founders want to reach out to you.
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
          <button onclick="switchLinkedInTab('featured')" id="li-tab-featured" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            3-Slot Featured Strategy
          </button>
          <button onclick="switchLinkedInTab('content')" id="li-tab-content" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            3x/Week Scheduler
          </button>
          <button onclick="switchLinkedInTab('launch30')" id="li-tab-launch30" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            30-Day Launch Plan
          </button>
          <button onclick="switchLinkedInTab('checklist')" id="li-tab-checklist" class="tab-btn px-4 py-3 text-xs font-semibold text-[#8888A8] hover:text-white whitespace-nowrap">
            Profile Checklist
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

        <!-- Tab 3: 3-Slot Featured Strategy -->
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

        <!-- Tab 4: 3x/Week Scheduler -->
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

        <!-- Tab 5: 30-Day Launch Plan -->
        <div id="li-content-launch30" class="hidden p-6 space-y-4">
          <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
            <div>
              <h3 class="text-xs font-bold text-white">Interactive 30-Day Authority Launch Plan</h3>
              <p class="text-[11px] text-[#8888A8]">Day-by-day checklist saved automatically in your browser.</p>
            </div>
            <div class="flex items-center gap-3">
              <span id="launch-30-progress-badge" class="text-xs font-mono text-[#00D4AA]">0/10 days complete (0%)</span>
              <div class="w-24 bg-[#0A0A0F] h-2 rounded-full overflow-hidden border border-[#2A2A3A]">
                <div id="launch-30-progress-bar" class="bg-[#00D4AA] h-full rounded-full transition-all" style="width: 0%"></div>
              </div>
            </div>
          </div>
          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs min-w-[500px]">
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

        <!-- Tab 6: Profile Checklist -->
        <div id="li-content-checklist" class="hidden p-6 space-y-4">
          <div class="flex items-center justify-between border-b border-[#2A2A3A] pb-3">
            <div>
              <h3 class="text-xs font-bold text-white font-heading">Complete Profile Hygiene Checklist</h3>
              <p class="text-[11px] text-[#8888A8]">23 checkpoints across 6 core profile areas.</p>
            </div>
            <div class="flex items-center gap-3">
              <span id="profile-checklist-progress-badge" class="text-xs font-mono text-[#00D4AA]">0/23 complete (0%)</span>
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

      </div>
    </section>

    <!-- ========================================== -->
    <!-- STEP 9: LAUNCH OUTREACH -->
    <!-- ========================================== -->
    <section id="outreach-section" class="space-y-6 scroll-mt-36 pt-4 border-t border-[#2A2A3A]">
      <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div class="space-y-2">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#6C63FF]">
            <span class="font-bold text-[#6C63FF]">STEP 09</span> &middot; OUTBOUND PIPELINE
          </div>
          <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
            Launch Outreach: Outbound CRM & Lead Pipeline
          </h2>
          <p class="text-sm text-[#8888A8] text-prose">
            Contact 20–25 founders daily using value-first DMs. Track every conversation.
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
    <!-- STEP 10: RESOURCES & DATA CONTROLS -->
    <!-- ========================================== -->
    <section id="resources-section" class="space-y-8 scroll-mt-36 pt-4 border-t border-[#2A2A3A]">
      <div class="space-y-2">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-[#1C1C27] border border-[#2A2A3A] text-xs font-mono text-[#00D4AA]">
          <span class="font-bold text-[#6C63FF]">STEP 10</span> &middot; COMPANION VAULT
        </div>
        <h2 class="text-2xl sm:text-3xl font-bold text-white font-heading">
          Resources & Implementation Hub
        </h2>
        <p class="text-sm text-[#8888A8] text-prose">
          Access all companion guides, spreadsheets, and video walkthroughs.
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

      <!-- Final Readiness Checklist -->
      <div id="final-checklist-section" class="card-surface p-6 space-y-4 bg-[#13131A]">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-[#2A2A3A] pb-3">
          <div>
            <h3 class="text-base font-bold text-white font-heading flex items-center gap-2">
              <i data-lucide="list-checks" class="w-4 h-4 text-[#00D4AA]"></i>
              Final Pre-Launch Verification Checklist
            </h3>
            <p class="text-xs text-[#8888A8]">Verify your profile, portfolio, outreach infrastructure, and interview readiness before sending your first application.</p>
          </div>
          <div class="text-right">
            <div id="final-checklist-progress-badge" class="text-xs font-bold font-mono text-[#00D4AA]">0 / 12 complete (0%)</div>
            <div class="w-28 bg-[#0A0A0F] h-2 rounded-full overflow-hidden border border-[#2A2A3A] mt-1 ml-auto">
              <div id="final-checklist-progress-bar" class="bg-[#00D4AA] h-full rounded-full transition-all" style="width: 0%"></div>
            </div>
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3" id="final-checklist-items-container">
          <!-- Rendered via JS -->
        </div>

        <div class="flex items-center justify-between pt-2">
          <button onclick="resetFinalChecklist()" class="text-xs text-[#8888A8] hover:text-white flex items-center gap-1 transition">
            <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i> Reset Final Checklist
          </button>
        </div>
      </div>

      <!-- Data Backup & Controls Section -->
      <div class="p-6 rounded-xl bg-[#13131A] border border-[#2A2A3A] flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="space-y-1 text-center sm:text-left">
          <h3 class="text-sm font-bold text-white font-heading">Data Portability & Local Storage Controls</h3>
          <p class="text-xs text-[#8888A8]">All checklist items, roadmap progress, and CRM leads are stored 100% locally in your browser.</p>
        </div>
        <div class="flex flex-wrap gap-2">
          <button onclick="exportUserDataJSON()" class="px-3.5 py-2 rounded-lg bg-[#6C63FF] hover:bg-[#584fe6] text-white text-xs font-semibold flex items-center gap-1.5 transition">
            <i data-lucide="download" class="w-3.5 h-3.5"></i> Export Data JSON
          </button>
          <label class="px-3.5 py-2 rounded-lg bg-[#1C1C27] hover:bg-[#2A2A3A] border border-[#2A2A3A] text-slate-200 text-xs font-semibold flex items-center gap-1.5 cursor-pointer transition">
            <i data-lucide="upload" class="w-3.5 h-3.5 text-[#00D4AA]"></i> Import Backup
            <input type="file" accept=".json" onchange="importUserDataJSON(event)" class="hidden">
          </label>
          <button onclick="resetAllData()" class="px-3.5 py-2 rounded-lg bg-[#1C1C27] hover:bg-red-500/20 hover:text-red-400 border border-[#2A2A3A] text-[#8888A8] text-xs font-semibold transition flex items-center gap-1.5">
            <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i> Reset All
          </button>
        </div>
      </div>

    </section>

  </main>

  <!-- FOOTER (PART 3) -->
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
        <a href="#hero-section" class="hover:text-white transition">Home</a>
        <a href="#opportunity-section" class="hover:text-white transition">Opportunity</a>
        <a href="#reality-check-section" class="hover:text-white transition">Reality Check</a>
        <a href="#filters-section" class="hover:text-white transition">Diagnose</a>
        <a href="#learn-skills-section" class="hover:text-white transition">Learn Skills</a>
        <a href="#roadmap-section" class="hover:text-white transition">Build Proof</a>
        <a href="#job-search-section" class="hover:text-white transition">Find Jobs</a>
        <a href="#offer-section" class="hover:text-white transition">Craft Offer</a>
        <a href="#linkedin-section" class="hover:text-white transition">LinkedIn</a>
        <a href="#outreach-section" class="hover:text-white transition">Outreach</a>
        <a href="#resources-section" class="hover:text-white transition">Resources</a>
      </div>

      <div class="text-xs text-[#8888A8] text-center md:text-right">
        &copy; 2026 Naraito's Playbook &middot; Built by Uduthalaboina Sai Varshith &middot; Last updated: September 2026 &middot; All data saved locally in your browser
      </div>
    </div>
  </footer>

  <!-- ========================================== -->
  <!-- MODALS (PROPOSAL, ADD LEAD, DATABASE, BACKUP) -->
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
        <textarea id="proposal-output-text" rows="10" placeholder="Your output will appear here" class="w-full p-3 rounded-xl bg-[#0A0A0F] border border-[#2A2A3A] text-xs text-slate-200 font-mono leading-relaxed focus:border-[#6C63FF] focus:outline-none"></textarea>
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
          <table class="w-full text-left text-xs min-w-[650px]">
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
              <tr><td colspan="5" class="py-8 text-center text-[#8888A8]">Loading leads...</td></tr>
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
