import os

with open(r'D:\us-remote-engineering-playbook\curated_leads.js', 'r', encoding='utf-8') as f:
    curated_leads_content = f.read()

with open(r'D:\us-remote-engineering-playbook\app.js', 'r', encoding='utf-8') as f:
    app_js_content = f.read()

html_head = """<!DOCTYPE html>
<html lang="en" class="dark scroll-smooth">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Naraito's Playbook | Mastering US Remote Engineering Jobs</title>
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            brand: {
              50: '#ecfdf5',
              100: '#d1fae5',
              400: '#34d399',
              500: '#10b981', // Emerald primary
              600: '#059669',
              700: '#047857',
            },
            accent: {
              400: '#818cf8',
              500: '#6366f1', // Indigo secondary
              600: '#4f46e5',
            },
            dark: {
              950: '#060911',
              900: '#0B1120', // Main background
              850: '#10172A',
              800: '#172239', // Card Surface
              750: '#1F2C47',
              700: '#2D3D5E',
              600: '#475569',
            }
          },
          fontFamily: {
            sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
            mono: ['JetBrains Mono', 'Fira Code', 'monospace'],
          }
        }
      }
    }
  </script>

  <!-- Lucide Icons -->
  <script src="https://unpkg.com/lucide@latest"></script>
  <!-- Canvas Confetti -->
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>

  <!-- Google Fonts: Inter & JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    /* Baseline 8px Typography & Layout System */
    :root {
      --bg-main: #0B1120;
      --surface-card: #10172A;
      --surface-elevated: #172239;
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-hover: rgba(16, 185, 129, 0.35);
    }

    body {
      background-color: var(--bg-main);
      color: #E2E8F0;
      font-feature-settings: "cv02", "cv03", "cv04", "cv11";
    }

    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #0B1120;
    }
    ::-webkit-scrollbar-thumb {
      background: #1F2C47;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #10B981;
    }

    /* Typography Constraints */
    p, li, .text-prose {
      max-width: 76ch;
    }

    /* Refined Surface Cards */
    .glass-card {
      background: rgba(16, 23, 42, 0.75);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border: 1px solid var(--border-subtle);
      border-radius: 1rem;
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }
    .glass-card:hover {
      border-color: var(--border-hover);
    }

    /* Subtle Focus & Glows */
    .glow-emerald {
      box-shadow: 0 4px 20px -2px rgba(16, 185, 129, 0.2);
    }
    .radial-hero-bg {
      background: radial-gradient(ellipse 80% 50% at 50% -20%, rgba(16, 185, 129, 0.12), transparent 70%);
    }

    /* Interactive Tab Buttons */
    .tab-btn {
      transition: all 0.15s ease-in-out;
    }
    .tab-btn.active {
      background: #10B981;
      color: #060911;
      font-weight: 700;
    }

    .sidebar-link {
      transition: all 0.15s ease;
    }
    .sidebar-link.active {
      background: rgba(16, 185, 129, 0.12);
      border-left: 3px solid #10B981;
      color: #34D399;
    }

    /* Table Styles */
    table th, table td {
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    }
    tr:last-child td {
      border-bottom: none;
    }

    /* Form Controls */
    input[type="range"]::-webkit-slider-thumb {
      appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #10B981;
      cursor: pointer;
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.5);
    }

    /* Reduced Motion */
    @media (prefers-reduced-motion: reduce) {
      * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
      }
    }
  </style>
</head>
<body class="bg-dark-900 text-slate-200 font-sans min-h-screen flex flex-col antialiased selection:bg-brand-500 selection:text-dark-950">

  <!-- TOP HEADER / TICKER -->
  <header class="sticky top-0 z-40 bg-dark-900/95 backdrop-blur-md border-b border-dark-750 transition-all">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      
      <!-- Brand / Logo -->
      <div class="flex items-center gap-3">
        <button id="mobile-menu-btn" class="lg:hidden p-2 text-slate-400 hover:text-white rounded-lg hover:bg-dark-800 transition" aria-label="Toggle Navigation">
          <i data-lucide="menu" class="w-5 h-5"></i>
        </button>
        <div class="flex items-center gap-3">
          <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-brand-500 to-accent-500 flex items-center justify-center shadow-md shadow-brand-500/20 shrink-0">
            <i data-lucide="compass" class="w-5 h-5 text-dark-950 font-bold"></i>
          </div>
          <div>
            <div class="font-extrabold text-sm sm:text-base tracking-tight text-white flex items-center gap-2">
              Naraito's Playbook
              <span class="text-[10px] uppercase font-mono px-1.5 py-0.5 rounded bg-brand-500/10 text-brand-400 border border-brand-500/30 font-semibold">0 Exp Edition</span>
            </div>
            <p class="text-xs text-slate-400 hidden sm:block">Mastering US Remote Engineering Jobs ($60K–$120K)</p>
          </div>
        </div>
      </div>

      <!-- Quick Action Stats & Progress -->
      <div class="flex items-center gap-3 sm:gap-6">
        
        <!-- Arbitrage Ticker (Interactive) -->
        <button onclick="openArbitrageModal()" class="hidden md:flex items-center gap-2 px-3 py-1.5 rounded-lg bg-dark-800/80 border border-dark-700 hover:border-brand-500/50 text-xs transition">
          <span class="w-2 h-2 rounded-full bg-brand-400 animate-pulse"></span>
          <span class="text-slate-400">Remote Arbitrage:</span>
          <span class="font-mono text-brand-400 font-bold">$60k–$120k / yr</span>
          <i data-lucide="calculator" class="w-3.5 h-3.5 text-slate-400 ml-1"></i>
        </button>

        <!-- Playbook Readiness Progress Tracker -->
        <div class="flex items-center gap-3">
          <div class="text-right hidden sm:block">
            <div class="text-[11px] font-medium text-slate-400">Roadmap Progress</div>
            <div id="header-progress-text" class="text-xs font-mono font-bold text-brand-400">0% (0/24 tasks)</div>
          </div>
          <div class="w-24 sm:w-28 bg-dark-950 h-2.5 rounded-full overflow-hidden border border-dark-700 p-0.5">
            <div id="header-progress-bar" class="bg-gradient-to-r from-brand-500 to-accent-500 h-full rounded-full transition-all duration-500" style="width: 0%"></div>
          </div>
        </div>

        <!-- Audio toggle button -->
        <button id="audio-toggle-btn" onclick="toggleAudio()" title="Sound Effects" class="p-2 text-slate-400 hover:text-brand-400 rounded-lg hover:bg-dark-800 border border-transparent hover:border-dark-700 transition">
          <i data-lucide="volume-2" class="w-4 h-4" id="audio-icon"></i>
        </button>

        <!-- Export/Backup Menu Button -->
        <button onclick="openBackupModal()" class="px-3.5 py-1.5 rounded-lg bg-accent-600 hover:bg-accent-500 text-white text-xs font-semibold flex items-center gap-1.5 shadow-sm transition">
          <i data-lucide="hard-drive" class="w-3.5 h-3.5"></i>
          <span class="hidden sm:inline">Data & CRM</span>
        </button>

      </div>
    </div>
  </header>

  <!-- MAIN APP CONTAINER -->
  <div class="flex-1 max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8 flex gap-6 lg:gap-8">

    <!-- SIDEBAR NAVIGATION (DESKTOP) -->
    <aside id="sidebar" class="w-64 shrink-0 hidden lg:block">
      <div class="sticky top-24 space-y-4">
        
        <!-- Navigation Menu -->
        <nav class="glass-card p-3 space-y-1">
          <div class="px-3 py-2 text-[11px] font-mono uppercase tracking-wider text-slate-400 font-semibold">Curriculum & Tools</div>
          
          <a href="#hero-section" class="sidebar-link active flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-dark-750 transition">
            <i data-lucide="layout-dashboard" class="w-4 h-4 text-brand-400"></i>
            <span>Overview & Arbitrage</span>
          </a>

          <a href="#diagnostic-section" class="sidebar-link flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-dark-750 transition">
            <div class="flex items-center gap-3">
              <i data-lucide="brain-circuit" class="w-4 h-4 text-accent-400"></i>
              <span>1. The 5 Filters Diagnostic</span>
            </div>
            <span id="diagnostic-badge" class="px-1.5 py-0.5 text-[10px] font-mono rounded bg-dark-750 text-slate-400">Audit</span>
          </a>

          <a href="#av-hygiene-section" class="sidebar-link flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-dark-750 transition">
            <i data-lucide="video" class="w-4 h-4 text-amber-400"></i>
            <span>Camera & Mic Tester</span>
          </a>

          <a href="#matrix-section" class="sidebar-link flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-dark-750 transition">
            <i data-lucide="scale" class="w-4 h-4 text-sky-400"></i>
            <span>2. US vs Traditional Matrix</span>
          </a>

          <a href="#roadmap-section" class="sidebar-link flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-dark-750 transition">
            <div class="flex items-center gap-3">
              <i data-lucide="map" class="w-4 h-4 text-emerald-400"></i>
              <span>3. 5-8 Week Roadmap</span>
            </div>
            <span id="roadmap-counter-badge" class="px-1.5 py-0.5 text-[10px] font-mono rounded bg-brand-500/20 text-brand-400">0/24</span>
          </a>

          <a href="#blueprints-section" class="sidebar-link flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-dark-750 transition">
            <i data-lucide="cpu" class="w-4 h-4 text-violet-400"></i>
            <span>6 Production Blueprints</span>
          </a>

          <a href="#jd-mapper-section" class="sidebar-link flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-dark-750 transition">
            <i data-lucide="file-code-2" class="w-4 h-4 text-pink-400"></i>
            <span>JD Project Mapper</span>
          </a>

          <a href="#offer-framework-section" class="sidebar-link flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-dark-750 transition">
            <i data-lucide="shield-check" class="w-4 h-4 text-emerald-400"></i>
            <span>The Offer Framework</span>
          </a>

          <a href="#linkedin-toolkit-section" class="sidebar-link flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-dark-750 transition">
            <i data-lucide="linkedin" class="w-4 h-4 text-blue-400"></i>
            <span>LinkedIn Toolkit Studio</span>
          </a>

          <a href="#kanban-section" class="sidebar-link flex items-center justify-between px-3 py-2.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-dark-750 transition">
            <div class="flex items-center gap-3">
              <i data-lucide="kanban-square" class="w-4 h-4 text-brand-400"></i>
              <span>4. Outbound CRM & Leads</span>
            </div>
            <span class="px-1.5 py-0.5 text-[10px] font-mono rounded bg-accent-500/20 text-accent-300">CRM</span>
          </a>

          <a href="#resources-section" class="sidebar-link flex items-center gap-3 px-3 py-2.5 rounded-xl text-xs font-medium text-slate-300 hover:text-white hover:bg-dark-750 transition">
            <i data-lucide="folder-down" class="w-4 h-4 text-orange-400"></i>
            <span>Downloads & Resource Hub</span>
          </a>
        </nav>

        <!-- Daily Target Widget -->
        <div class="glass-card p-4 space-y-3">
          <div class="flex items-center justify-between">
            <span class="text-xs font-semibold text-slate-200 flex items-center gap-1.5">
              <i data-lucide="target" class="w-3.5 h-3.5 text-brand-400"></i> Daily Outreach
            </span>
            <span id="daily-streak-badge" class="text-[10px] font-mono bg-brand-500/20 text-brand-300 px-1.5 py-0.5 rounded font-semibold">🎯 25 / Day</span>
          </div>
          <div class="text-xs text-slate-400">Today's DMs Sent:</div>
          <div class="flex items-center gap-2">
            <button onclick="adjustDailyCount(-1)" class="w-7 h-7 rounded-lg bg-dark-750 hover:bg-dark-700 flex items-center justify-center text-slate-300 font-bold transition">-</button>
            <div id="daily-count-display" class="flex-1 text-center font-mono text-lg font-bold text-brand-400 bg-dark-950 py-1 rounded-lg border border-dark-750">0</div>
            <button onclick="adjustDailyCount(1)" class="w-7 h-7 rounded-lg bg-brand-500 hover:bg-brand-600 text-dark-950 font-bold flex items-center justify-center transition">+</button>
          </div>
          <div class="w-full bg-dark-950 h-1.5 rounded-full overflow-hidden">
            <div id="daily-goal-bar" class="bg-brand-400 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
          </div>
          <p class="text-[10px] text-slate-400 text-center">Goal: ~800 founders/month (YC, PH, Canada Leads)</p>
        </div>

      </div>
    </aside>

    <!-- MAIN CONTENT AREA -->
    <main class="flex-1 min-w-0 space-y-12 sm:space-y-16">

      <!-- ========================================== -->
      <!-- SECTION 1: HERO & REMOTE ARBITRAGE         -->
      <!-- ========================================== -->
      <section id="hero-section" class="radial-hero-bg glass-card p-6 sm:p-8 lg:p-10 space-y-8 relative overflow-hidden">
        
        <!-- Hero Headline & Intro -->
        <div class="space-y-4 max-w-3xl">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-500/10 border border-brand-500/30 text-brand-400 text-xs font-semibold">
            <i data-lucide="zap" class="w-3.5 h-3.5"></i>
            The 3x–4x Cost Arbitrage Blueprint for Global Engineers
          </div>
          <h1 class="text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight text-white leading-[1.15]">
            Stop Relying on Degrees.<br/>
            <span class="bg-gradient-to-r from-brand-400 via-emerald-300 to-accent-400 bg-clip-text text-transparent">
              Master Naraito's US Remote Engineering Playbook.
            </span>
          </h1>
          <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
            US venture-funded startups are hiring global engineers at <strong class="text-white font-semibold">$60,000–$120,000/year (₹50L–₹1 Crore)</strong>. 
            Technical skills are almost never the bottleneck—the rejection happens in <em>execution style</em>, <em>ownership maturity</em>, and <em>non-technical presentation</em>.
          </p>
        </div>

        <!-- Key Insight Callout Banner -->
        <div class="p-5 rounded-2xl bg-dark-950/80 border-l-4 border-l-brand-400 border border-dark-750 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div class="flex items-start gap-3.5">
            <div class="w-10 h-10 rounded-xl bg-brand-500/20 text-brand-400 flex items-center justify-center shrink-0 mt-0.5">
              <i data-lucide="lightbulb" class="w-5 h-5"></i>
            </div>
            <div class="space-y-1">
              <h4 class="text-sm font-bold text-white">The Core Insight of US Startup Hiring:</h4>
              <p class="text-xs sm:text-sm text-slate-300">
                “90% of candidates submit certificates and theoretical algorithm definitions. US founders hire for <strong>judgment under ambiguity</strong>, <strong>shipping velocity</strong>, and <strong>autonomous ownership</strong>.”
              </p>
            </div>
          </div>
          <button onclick="scrollToSection('diagnostic-section')" class="shrink-0 px-4 py-2.5 rounded-xl bg-brand-500 hover:bg-brand-600 text-dark-950 font-bold text-xs flex items-center gap-1.5 transition shadow-sm">
            Take Gap Diagnostic <i data-lucide="arrow-right" class="w-4 h-4"></i>
          </button>
        </div>

        <!-- Arbitrage Math Visual Cards -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          
          <!-- Card 1: SF Bay Area Cost -->
          <div class="p-5 rounded-2xl bg-dark-950/70 border border-dark-750 space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-rose-400 uppercase tracking-wider font-mono">San Francisco On-Site</span>
              <i data-lucide="building-2" class="w-4 h-4 text-rose-400"></i>
            </div>
            <div class="font-mono text-2xl sm:text-3xl font-extrabold text-white">$250K–$500K<span class="text-xs text-slate-400 font-normal">/yr</span></div>
            <p class="text-xs text-slate-400 leading-relaxed">Includes base salary ($180k+), employer payroll taxes, healthcare, Bay Area office desk space & equity burn.</p>
            <div class="text-[11px] font-mono text-rose-300 bg-rose-950/40 px-2.5 py-1 rounded border border-rose-900/40">
              High burn rate for early-stage founders
            </div>
          </div>

          <!-- Card 2: Remote Global Engineer -->
          <div class="p-5 rounded-2xl bg-dark-950/90 border border-brand-500/40 space-y-3 shadow-md shadow-brand-500/10">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-brand-400 uppercase tracking-wider font-mono">US Remote Arbitrage</span>
              <span class="px-2 py-0.5 rounded-full bg-brand-500/20 text-brand-300 text-[10px] font-bold font-mono">THE SWEET SPOT</span>
            </div>
            <div class="font-mono text-2xl sm:text-3xl font-extrabold text-brand-400">$60K–$120K<span class="text-xs text-slate-300 font-normal">/yr</span></div>
            <p class="text-xs text-slate-300 leading-relaxed">Equivalent to <strong class="text-white font-mono">₹50L–₹1.02 Crore INR/yr</strong> in-hand. 3x–4x cheaper for the US founder, life-changing wealth for you.</p>
            <div class="text-[11px] font-mono text-brand-300 bg-brand-950/60 px-2.5 py-1 rounded border border-brand-500/30 flex items-center justify-between">
              <span>Founder Saves: $180k+/yr</span>
              <i data-lucide="trending-up" class="w-3.5 h-3.5"></i>
            </div>
          </div>

          <!-- Card 3: Traditional Indian Campus/Service Firm -->
          <div class="p-5 rounded-2xl bg-dark-950/70 border border-dark-750 space-y-3">
            <div class="flex items-center justify-between">
              <span class="text-xs font-semibold text-amber-400 uppercase tracking-wider font-mono">Traditional Indian Firm</span>
              <i data-lucide="landmark" class="w-4 h-4 text-amber-400"></i>
            </div>
            <div class="font-mono text-2xl sm:text-3xl font-extrabold text-slate-200">₹6L–₹14L<span class="text-xs text-slate-400 font-normal">/yr ($7k-$16k)</span></div>
            <p class="text-xs text-slate-400 leading-relaxed">90-day notice periods, rigid bureaucracy, endless Leetcode rounds, and zero autonomous product impact.</p>
            <div class="text-[11px] font-mono text-amber-300 bg-amber-950/40 px-2.5 py-1 rounded border border-amber-900/40">
              Trapped in 10-20% annual increments
            </div>
          </div>

        </div>

        <!-- Interactive Remote Salary & Arbitrage Calculator Slider -->
        <div class="p-6 sm:p-7 rounded-2xl bg-dark-950/90 border border-dark-750 space-y-6">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-dark-800 pb-4">
            <div>
              <h3 class="text-base font-bold text-white flex items-center gap-2">
                <i data-lucide="calculator" class="w-5 h-5 text-brand-400"></i>
                Interactive Remote Arbitrage & Purchasing Power Calculator
              </h3>
              <p class="text-xs text-slate-400">Adjust the slider to simulate remote salary, founder annual savings, and local in-hand value.</p>
            </div>
            <div class="text-xs font-mono text-slate-400 bg-dark-900 px-2.5 py-1 rounded border border-dark-800">USD/INR Rate: ₹86.5 / $1</div>
          </div>

          <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
            
            <div class="space-y-4">
              <div class="flex justify-between items-center">
                <label class="text-xs font-semibold text-slate-300">Target US Remote Annual Compensation:</label>
                <span id="calc-salary-display" class="text-lg font-mono font-extrabold text-brand-400">$85,000 / year</span>
              </div>
              <input 
                id="salary-slider" 
                type="range" 
                min="50000" 
                max="140000" 
                step="5000" 
                value="85000" 
                oninput="updateArbitrageCalculator(this.value)" 
                class="w-full h-2 bg-dark-800 rounded-lg appearance-none cursor-pointer accent-brand-500"
              />
              <div class="flex justify-between text-[11px] text-slate-500 font-mono">
                <span>$50K (Junior Remote)</span>
                <span>$85K (Mid-Level Builder)</span>
                <span>$140K (Senior / Lead)</span>
              </div>

              <div class="p-4 rounded-xl bg-dark-900 border border-dark-800 text-xs text-slate-300 space-y-1.5">
                <div class="font-semibold text-white flex items-center gap-1.5">
                  <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-brand-400"></i>
                  Why US Founders eagerly pay this rate:
                </div>
                <p class="text-slate-400 text-[11px] leading-relaxed">
                  A US founder raising a $1.5M Seed round gets 18 months of runway instead of 7 months when hiring 2 exceptional remote engineers instead of 2 local SF engineers. You are saving their startup from premature death.
                </p>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-4 bg-dark-900/90 p-5 rounded-xl border border-dark-800">
              <div class="space-y-1">
                <span class="text-[11px] text-slate-400 uppercase font-mono">Founder Saves (vs SF)</span>
                <div id="calc-founder-savings" class="text-xl sm:text-2xl font-mono font-bold text-brand-400">$215,000 / yr</div>
                <p class="text-[10px] text-slate-500">Based on $300k SF all-in cost</p>
              </div>
              
              <div class="space-y-1">
                <span class="text-[11px] text-slate-400 uppercase font-mono">Indian In-Hand Annual</span>
                <div id="calc-inr-annual" class="text-xl sm:text-2xl font-mono font-bold text-accent-400">₹73,52,500</div>
                <p class="text-[10px] text-slate-500">~₹6.12 Lakhs / month gross</p>
              </div>

              <div class="space-y-1 pt-3 border-t border-dark-800">
                <span class="text-[11px] text-slate-400 uppercase font-mono">Multiplier vs Indian Campus</span>
                <div id="calc-multiplier" class="text-lg font-mono font-bold text-emerald-300">9.2x</div>
                <p class="text-[10px] text-slate-500">Compared to ₹8L campus package</p>
              </div>

              <div class="space-y-1 pt-3 border-t border-dark-800">
                <span class="text-[11px] text-slate-400 uppercase font-mono">Monthly Inflow</span>
                <div id="calc-usd-monthly" class="text-lg font-mono font-bold text-white">$7,083 / mo</div>
                <p class="text-[10px] text-slate-500">Direct wire / Deel / Stripe</p>
              </div>
            </div>

          </div>
        </div>

      </section>

      <!-- ==================================================== -->
      <!-- SECTION 2: MODULE 1 - INTERACTIVE GAP DIAGNOSTIC     -->
      <!-- ==================================================== -->
      <section id="diagnostic-section" class="space-y-8 scroll-mt-24">
        
        <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-dark-800 pb-6">
          <div class="space-y-2">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-accent-500/10 text-accent-400 text-xs font-semibold">
              <i data-lucide="scan-face" class="w-3.5 h-3.5"></i> Module 1: The 5 Non-Technical Filters
            </div>
            <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              The 5 Filters: Traditional Mindset vs. US Startup Reality
            </h2>
            <p class="text-xs sm:text-sm text-slate-400 max-w-2xl">
              Compare how traditional Indian interview preparation fails in US remote interviews, and complete the 5-question diagnostic audit below.
            </p>
          </div>

          <!-- Audit Score Badge -->
          <div class="glass-card p-4 flex items-center gap-4 shrink-0">
            <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-brand-500 to-accent-500 flex items-center justify-center font-mono text-xl font-black text-dark-950 shadow-md" id="audit-score-circle">
              ?%
            </div>
            <div>
              <div class="text-[11px] text-slate-400 uppercase font-mono">Your Readiness Score</div>
              <div id="audit-readiness-label" class="text-xs font-bold text-slate-300">Audit Not Completed</div>
            </div>
          </div>
        </div>

        <!-- 5 Interactive Filter Toggle Cards -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          
          <!-- Filter 1: Autonomous Ownership -->
          <div class="glass-card p-5 space-y-4 hover:border-accent-500/40 transition">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-lg bg-accent-500/20 text-accent-400 flex items-center justify-center text-xs font-mono font-bold">01</span>
              <span class="text-xs font-semibold text-slate-400 font-mono">Ownership Style</span>
            </div>
            <h3 class="text-base font-bold text-white">Autonomous Ownership</h3>
            
            <div class="space-y-2.5 text-xs">
              <div class="p-3 rounded-xl bg-rose-950/30 border border-rose-900/40 text-rose-200">
                <div class="font-bold text-rose-400 flex items-center gap-1.5 mb-1">
                  <i data-lucide="x-circle" class="w-3.5 h-3.5"></i> Traditional Trait:
                </div>
                “Tell me what to do. I need a Jira ticket with 10 acceptance criteria before I can start.”
              </div>
              <div class="p-3 rounded-xl bg-brand-950/30 border border-brand-900/40 text-emerald-200">
                <div class="font-bold text-brand-400 flex items-center gap-1.5 mb-1">
                  <i data-lucide="check-circle" class="w-3.5 h-3.5"></i> US Startup Mindset:
                </div>
                “Here is the root problem, 2 possible architectures with cost/latency trade-offs, and I already deployed a prototype on a staging branch.”
              </div>
            </div>
          </div>

          <!-- Filter 2: Healthy Disagreement & Pushback -->
          <div class="glass-card p-5 space-y-4 hover:border-accent-500/40 transition">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-lg bg-accent-500/20 text-accent-400 flex items-center justify-center text-xs font-mono font-bold">02</span>
              <span class="text-xs font-semibold text-slate-400 font-mono">Authority Trap</span>
            </div>
            <h3 class="text-base font-bold text-white">Professional Pushback</h3>
            
            <div class="space-y-2.5 text-xs">
              <div class="p-3 rounded-xl bg-rose-950/30 border border-rose-900/40 text-rose-200">
                <div class="font-bold text-rose-400 flex items-center gap-1.5 mb-1">
                  <i data-lucide="x-circle" class="w-3.5 h-3.5"></i> Traditional Trait:
                </div>
                Uncritical deference. Saying “Yes sir/yes boss” to impossible deadlines or flawed architectures out of fear of offending.
              </div>
              <div class="p-3 rounded-xl bg-brand-950/30 border border-brand-900/40 text-emerald-200">
                <div class="font-bold text-brand-400 flex items-center gap-1.5 mb-1">
                  <i data-lucide="check-circle" class="w-3.5 h-3.5"></i> US Startup Mindset:
                </div>
                “I disagree with using GPT-4 here because it will burn $3,500/mo. Here is the math for hybrid rules + Claude 3.5 Haiku saving 70% cost.”
              </div>
            </div>
          </div>

          <!-- Filter 3: Direct Asynchronous Communication -->
          <div class="glass-card p-5 space-y-4 hover:border-accent-500/40 transition">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-lg bg-accent-500/20 text-accent-400 flex items-center justify-center text-xs font-mono font-bold">03</span>
              <span class="text-xs font-semibold text-slate-400 font-mono">Communication</span>
            </div>
            <h3 class="text-base font-bold text-white">Direct Communication</h3>
            
            <div class="space-y-2.5 text-xs">
              <div class="p-3 rounded-xl bg-rose-950/30 border border-rose-900/40 text-rose-200">
                <div class="font-bold text-rose-400 flex items-center gap-1.5 mb-1">
                  <i data-lucide="x-circle" class="w-3.5 h-3.5"></i> Traditional Trait:
                </div>
                Writing 4-paragraph formal emails that bury the answer at the bottom, packed with passive voice and academic filler.
              </div>
              <div class="p-3 rounded-xl bg-brand-950/30 border border-brand-900/40 text-emerald-200">
                <div class="font-bold text-brand-400 flex items-center gap-1.5 mb-1">
                  <i data-lucide="check-circle" class="w-3.5 h-3.5"></i> US Startup Mindset:
                </div>
                <strong>BLUF</strong> (Bottom Line Up Front). 5-sentence maximum. Crisp bullet points with clear actionable decisions and deadlines.
              </div>
            </div>
          </div>

          <!-- Filter 4: Audio/Video & Meeting Hygiene -->
          <div class="glass-card p-5 space-y-4 hover:border-accent-500/40 transition">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-lg bg-accent-500/20 text-accent-400 flex items-center justify-center text-xs font-mono font-bold">04</span>
              <span class="text-xs font-semibold text-slate-400 font-mono">Presence</span>
            </div>
            <h3 class="text-base font-bold text-white">Audio/Video Hygiene</h3>
            
            <div class="space-y-2.5 text-xs">
              <div class="p-3 rounded-xl bg-rose-950/30 border border-rose-900/40 text-rose-200">
                <div class="font-bold text-rose-400 flex items-center gap-1.5 mb-1">
                  <i data-lucide="x-circle" class="w-3.5 h-3.5"></i> Traditional Trait:
                </div>
                Grainy 720p laptop camera pointing at ceiling fan, slouched posture, echoing ambient noise, looking down at screen.
              </div>
              <div class="p-3 rounded-xl bg-brand-950/30 border border-brand-900/40 text-emerald-200">
                <div class="font-bold text-brand-400 flex items-center gap-1.5 mb-1">
                  <i data-lucide="check-circle" class="w-3.5 h-3.5"></i> US Startup Mindset:
                </div>
                1080p eye-level webcam, dedicated diffused lighting, noise-canceling mic, clean background, upright posture, concise articulation.
              </div>
            </div>
          </div>

          <!-- Filter 5: Proactive Public Visibility -->
          <div class="glass-card p-5 space-y-4 hover:border-accent-500/40 transition">
            <div class="flex items-center justify-between">
              <span class="w-8 h-8 rounded-lg bg-accent-500/20 text-accent-400 flex items-center justify-center text-xs font-mono font-bold">05</span>
              <span class="text-xs font-semibold text-slate-400 font-mono">Proof of Work</span>
            </div>
            <h3 class="text-base font-bold text-white">Public Visibility</h3>
            
            <div class="space-y-2.5 text-xs">
              <div class="p-3 rounded-xl bg-rose-950/30 border border-rose-900/40 text-rose-200">
                <div class="font-bold text-rose-400 flex items-center gap-1.5 mb-1">
                  <i data-lucide="x-circle" class="w-3.5 h-3.5"></i> Traditional Trait:
                </div>
                “I shouldn't post online, that's bragging. My certificate and secret local code will speak for itself.”
              </div>
              <div class="p-3 rounded-xl bg-brand-950/30 border border-brand-900/40 text-emerald-200">
                <div class="font-bold text-brand-400 flex items-center gap-1.5 mb-1">
                  <i data-lucide="check-circle" class="w-3.5 h-3.5"></i> US Startup Mindset:
                </div>
                Publishing failure post-mortems, cost breakdown benchmarks, architecture diagrams, and high-impact GitHub READMEs.
              </div>
            </div>
          </div>

          <!-- Summary Action Card -->
          <div class="glass-card p-5 space-y-3 bg-gradient-to-br from-dark-850 to-dark-900 flex flex-col justify-between border-brand-500/30">
            <div>
              <div class="flex items-center gap-2 text-brand-400 text-xs font-bold uppercase font-mono">
                <i data-lucide="sparkles" class="w-4 h-4"></i>
                The Non-Technical Advantage
              </div>
              <h4 class="text-sm font-bold text-white mt-2">Why This Gives You an Unfair Advantage</h4>
              <p class="text-xs text-slate-300 mt-1 leading-relaxed">
                98% of applicants compete solely on tools and leetcode algorithms. When you demonstrate <strong>high-agency ownership</strong> and <strong>business-conscious communication</strong>, you jump directly to the top 2% of hiring manager candidate shortlists.
              </p>
            </div>
            <button onclick="document.getElementById('audit-calculator').scrollIntoView({behavior: 'smooth'})" class="w-full py-2.5 rounded-xl bg-brand-500 hover:bg-brand-600 text-dark-950 text-xs font-bold transition shadow-sm">
              Run Self-Audit Calculator ↓
            </button>
          </div>

        </div>

        <!-- Interactive 5-Question Readiness Audit Score Calculator -->
        <div id="audit-calculator" class="glass-card p-6 sm:p-8 space-y-6 border-dark-750">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-dark-800 pb-5">
            <div>
              <h3 class="text-lg font-bold text-white flex items-center gap-2">
                <i data-lucide="check-square" class="w-5 h-5 text-brand-400"></i>
                Interactive 5-Question US Remote Readiness Self-Audit
              </h3>
              <p class="text-xs text-slate-400">Select how you would genuinely react in each real startup scenario.</p>
            </div>
            <button onclick="resetAudit()" class="text-xs text-slate-400 hover:text-white flex items-center gap-1 font-mono transition">
              <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i> Reset Audit
            </button>
          </div>

          <div id="audit-questions-container" class="space-y-6">
            <!-- Questions rendered via JavaScript -->
          </div>

          <!-- Audit Result Box -->
          <div id="audit-result-card" class="hidden p-6 rounded-2xl bg-dark-950 border border-brand-500/40 space-y-4 shadow-lg">
            <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
              <div class="flex items-center gap-4">
                <div id="audit-result-score-large" class="w-16 h-16 rounded-2xl bg-brand-500 text-dark-950 flex items-center justify-center font-mono font-black text-2xl shadow-md shadow-brand-500/30">
                  100%
                </div>
                <div>
                  <h4 id="audit-result-title" class="text-base font-bold text-white">US Remote Operator Tier</h4>
                  <p id="audit-result-desc" class="text-xs text-slate-300">You exhibit high autonomy and US startup execution maturity.</p>
                </div>
              </div>
              <button onclick="scrollToSection('roadmap-section')" class="px-4 py-2 rounded-xl bg-brand-500 hover:bg-brand-600 text-dark-950 font-bold text-xs flex items-center gap-1.5 transition shadow-sm">
                Proceed to Roadmap <i data-lucide="arrow-right" class="w-4 h-4"></i>
              </button>
            </div>
            <div id="audit-result-recommendations" class="text-xs text-slate-300 p-4 rounded-xl bg-dark-900 border border-dark-800">
              <!-- Recommendations inserted here -->
            </div>
          </div>

        </div>

      </section>

      <!-- ==================================================== -->
      <!-- BONUS SUB-SECTION: CAMERA & MIC HYGIENE TESTER       -->
      <!-- ==================================================== -->
      <section id="av-hygiene-section" class="glass-card p-6 sm:p-8 space-y-6 border-dark-750 scroll-mt-24">
        
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-dark-800 pb-5">
          <div class="space-y-1">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/10 text-amber-400 text-xs font-semibold">
              <i data-lucide="video" class="w-3.5 h-3.5"></i> Filter 4 Live Tool
            </div>
            <h3 class="text-lg sm:text-xl font-bold text-white">
              Live Camera, Framing & Audio Hygiene Diagnostic
            </h3>
            <p class="text-xs text-slate-400">
              US founders make 70% of hiring impressions in the first 90 seconds of a video call. Test your framing and mic directly in-browser.
            </p>
          </div>
          <div class="flex gap-2">
            <button id="start-av-btn" onclick="startCameraTest()" class="px-4 py-2 rounded-xl bg-amber-500 hover:bg-amber-600 text-dark-950 text-xs font-bold flex items-center gap-1.5 transition shadow-sm">
              <i data-lucide="camera" class="w-4 h-4"></i> Test My Camera & Mic
            </button>
            <button id="stop-av-btn" onclick="stopCameraTest()" class="hidden px-3 py-2 rounded-xl bg-dark-750 hover:bg-dark-700 text-slate-200 text-xs font-semibold transition">
              Stop Camera
            </button>
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-start">
          
          <!-- Camera Feed Box -->
          <div class="relative rounded-2xl bg-dark-950 border border-dark-800 aspect-video overflow-hidden flex items-center justify-center">
            <video id="webcam-preview" autoplay playsinline muted class="w-full h-full object-cover hidden"></video>
            
            <!-- Placeholder state -->
            <div id="webcam-placeholder" class="text-center p-6 space-y-2">
              <i data-lucide="camera-off" class="w-10 h-10 text-slate-600 mx-auto"></i>
              <p class="text-xs text-slate-400">Camera preview inactive. Click "Test My Camera & Mic" to start live check.</p>
            </div>

            <!-- Overlays when camera is active -->
            <div id="camera-overlay" class="absolute inset-0 pointer-events-none hidden border-2 border-brand-500/30">
              <!-- Golden Ratio / Eye Level Line -->
              <div class="absolute top-[35%] left-0 right-0 border-b border-dashed border-amber-400/60 flex justify-between px-3">
                <span class="text-[9px] font-mono text-amber-300 bg-dark-900/80 px-1 rounded">Target Eye-Level Line</span>
                <span class="text-[9px] font-mono text-amber-300 bg-dark-900/80 px-1 rounded">Top 1/3 Frame</span>
              </div>
              <div class="absolute bottom-3 left-3 bg-dark-900/90 backdrop-blur px-2.5 py-1 rounded-lg border border-dark-800 text-[10px] font-mono text-brand-400">
                Live Frame Check
              </div>
            </div>
          </div>

          <!-- 5-Point Meeting Hygiene Checklist -->
          <div class="space-y-3">
            <h4 class="text-xs font-bold text-slate-300 uppercase tracking-wider font-mono">The 5-Point Audio/Video Standard:</h4>
            
            <div class="space-y-2">
              <label class="flex items-start gap-3 p-3 rounded-xl bg-dark-950/70 border border-dark-800 cursor-pointer hover:border-dark-700 transition">
                <input type="checkbox" class="mt-0.5 rounded bg-dark-800 border-dark-600 text-brand-500 focus:ring-brand-500" />
                <div class="text-xs">
                  <strong class="text-white">1. Eye-Level Webcam:</strong>
                  <span class="text-slate-400"> Laptop propped up on books or stand so the camera is level with your eyes (never pointing up your chin or showing ceiling fans).</span>
                </div>
              </label>

              <label class="flex items-start gap-3 p-3 rounded-xl bg-dark-950/70 border border-dark-800 cursor-pointer hover:border-dark-700 transition">
                <input type="checkbox" class="mt-0.5 rounded bg-dark-800 border-dark-600 text-brand-500 focus:ring-brand-500" />
                <div class="text-xs">
                  <strong class="text-white">2. Front Light Source:</strong>
                  <span class="text-slate-400"> Soft light facing you (window or $15 ring light behind the screen). No bright backlights turning you into a dark silhouette.</span>
                </div>
              </label>

              <label class="flex items-start gap-3 p-3 rounded-xl bg-dark-950/70 border border-dark-800 cursor-pointer hover:border-dark-700 transition">
                <input type="checkbox" class="mt-0.5 rounded bg-dark-800 border-dark-600 text-brand-500 focus:ring-brand-500" />
                <div class="text-xs">
                  <strong class="text-white">3. Crisp Audio (Mic Isolation):</strong>
                  <span class="text-slate-400"> Use dedicated earphones with mic or USB condenser mic with Krisp / Krisp.ai noise cancellation to eliminate street & fan noise.</span>
                </div>
              </label>

              <label class="flex items-start gap-3 p-3 rounded-xl bg-dark-950/70 border border-dark-800 cursor-pointer hover:border-dark-700 transition">
                <input type="checkbox" class="mt-0.5 rounded bg-dark-800 border-dark-600 text-brand-500 focus:ring-brand-500" />
                <div class="text-xs">
                  <strong class="text-white">4. Neutral / Clutter-Free Background:</strong>
                  <span class="text-slate-400"> Plain wall, organized bookshelf, or neat room. Avoid fake blurry Zoom backgrounds that distort your hair and ears.</span>
                </div>
              </label>

              <label class="flex items-start gap-3 p-3 rounded-xl bg-dark-950/70 border border-dark-800 cursor-pointer hover:border-dark-700 transition">
                <input type="checkbox" class="mt-0.5 rounded bg-dark-800 border-dark-600 text-brand-500 focus:ring-brand-500" />
                <div class="text-xs">
                  <strong class="text-white">5. Direct Eye Contact:</strong>
                  <span class="text-slate-400"> Look at the physical camera lens when speaking, not down at the founder's thumbnail window.</span>
                </div>
              </label>
            </div>

          </div>

        </div>

      </section>

      <!-- ==================================================== -->
      <!-- SECTION 3: MODULE 2 - US STARTUP VS TRADITIONAL MATRIX -->
      <!-- ==================================================== -->
      <section id="matrix-section" class="space-y-8 scroll-mt-24">
        
        <div class="space-y-2 border-b border-dark-800 pb-6">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-500/10 text-sky-400 text-xs font-semibold">
            <i data-lucide="scale" class="w-3.5 h-3.5"></i> Module 2: Evaluation Matrix
          </div>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            Traditional Indian Tech Prep vs. US Startup Reality
          </h2>
          <p class="text-xs sm:text-sm text-slate-400 max-w-2xl">
            See exactly why grinding 500 LeetCode problems or memorizing textbook machine learning definitions gets you rejected by US venture-backed startups.
          </p>
        </div>

        <!-- Comparative Interactive Table -->
        <div class="glass-card overflow-hidden border-dark-750">
          <div class="overflow-x-auto">
            <table class="w-full text-left text-xs border-collapse">
              <thead>
                <tr class="bg-dark-950 border-b border-dark-750 text-slate-400 font-mono uppercase text-[11px]">
                  <th class="py-4 px-5 font-semibold w-1/4">Dimension</th>
                  <th class="py-4 px-5 font-semibold text-rose-400 w-1/4">Traditional Indian Prep / Service Firms</th>
                  <th class="py-4 px-5 font-semibold text-brand-400 w-1/4">US Venture-Funded Startups</th>
                  <th class="py-4 px-5 font-semibold text-slate-300 w-1/4">The Practical Shift</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-dark-800/60">
                
                <tr class="hover:bg-dark-800/40 transition">
                  <td class="py-4 px-5 font-bold text-white flex items-center gap-2">
                    <i data-lucide="award" class="w-4 h-4 text-slate-400"></i> Pedigree & Credentials
                  </td>
                  <td class="py-4 px-5 text-rose-300/90 leading-relaxed">
                    CGPA, college tier (Tier-1 IIT/NIT bias), course certificates (Coursera, Udemy).
                  </td>
                  <td class="py-4 px-5 text-emerald-300 font-medium leading-relaxed">
                    Zero care for CGPA or college name. Proven shipping velocity & public GitHub case studies.
                  </td>
                  <td class="py-4 px-5 text-slate-300 leading-relaxed">
                    Replace resume certificates with a 1-page architecture breakdown and live demo URL.
                  </td>
                </tr>

                <tr class="hover:bg-dark-800/40 transition">
                  <td class="py-4 px-5 font-bold text-white flex items-center gap-2">
                    <i data-lucide="binary" class="w-4 h-4 text-slate-400"></i> Interview Questions
                  </td>
                  <td class="py-4 px-5 text-rose-300/90 leading-relaxed">
                    Inverting binary trees, sorting algorithms, memorized math equations, Leetcode Hard.
                  </td>
                  <td class="py-4 px-5 text-emerald-300 font-medium leading-relaxed">
                    Building under ambiguity, rate-limiting, cost optimization, graceful API fallbacks, system constraints.
                  </td>
                  <td class="py-4 px-5 text-slate-300 leading-relaxed">
                    Ask: “What happens when this API fails at 2 AM or latency spikes 3x?”
                  </td>
                </tr>

                <tr class="hover:bg-dark-800/40 transition">
                  <td class="py-4 px-5 font-bold text-white flex items-center gap-2">
                    <i data-lucide="bug" class="w-4 h-4 text-slate-400"></i> Handling Failures
                  </td>
                  <td class="py-4 px-5 text-rose-300/90 leading-relaxed">
                    Hiding errors, pointing fingers, fearing punishment, presenting only flawless fake projects.
                  </td>
                  <td class="py-4 px-5 text-emerald-300 font-medium leading-relaxed">
                    Writing public post-mortems, documenting data leakage bugs, detailing root-cause debugging.
                  </td>
                  <td class="py-4 px-5 text-slate-300 leading-relaxed">
                    Include a dedicated <em>“What Broke in Production & How I Fixed It”</em> section in README.
                  </td>
                </tr>

                <tr class="hover:bg-dark-800/40 transition">
                  <td class="py-4 px-5 font-bold text-white flex items-center gap-2">
                    <i data-lucide="dollar-sign" class="w-4 h-4 text-slate-400"></i> Architecture & Cost
                  </td>
                  <td class="py-4 px-5 text-rose-300/90 leading-relaxed">
                    Over-engineering with the latest hyped tools regardless of infrastructure burn.
                  </td>
                  <td class="py-4 px-5 text-emerald-300 font-medium leading-relaxed">
                    Cost-per-inference consciousness: Tiered routing (rules → small model → LLM).
                  </td>
                  <td class="py-4 px-5 text-slate-300 leading-relaxed">
                    Demonstrate how your architecture cut LLM bills from $10k/mo to $1k/mo.
                  </td>
                </tr>

                <tr class="hover:bg-dark-800/40 transition">
                  <td class="py-4 px-5 font-bold text-white flex items-center gap-2">
                    <i data-lucide="clock" class="w-4 h-4 text-slate-400"></i> Working Style
                  </td>
                  <td class="py-4 px-5 text-rose-300/90 leading-relaxed">
                    Synchronous 9-hour desk presence, waiting for daily standups to speak up.
                  </td>
                  <td class="py-4 px-5 text-emerald-300 font-medium leading-relaxed">
                    High asynchronous velocity: 2-min Loom screen recordings, crisp Slack updates, PR self-reviews.
                  </td>
                  <td class="py-4 px-5 text-slate-300 leading-relaxed">
                    Never wait for a meeting to unblock yourself. Post the decision and ask for async feedback.
                  </td>
                </tr>

              </tbody>
            </table>
          </div>
        </div>

        <!-- Interactive Workplace Scenario Simulator -->
        <div class="glass-card p-6 sm:p-8 space-y-6 border-dark-750">
          <div class="flex items-center justify-between border-b border-dark-800 pb-4">
            <div>
              <h3 class="text-lg font-bold text-white flex items-center gap-2">
                <i data-lucide="gamepad-2" class="w-5 h-5 text-accent-400"></i>
                Workplace Scenario Simulator: "What Would You Say?"
              </h3>
              <p class="text-xs text-slate-400">Pick how you'd handle this real US startup dilemma to get immediate feedback.</p>
            </div>
            <span class="text-xs font-mono text-accent-400 bg-accent-500/10 px-2.5 py-1 rounded font-semibold">Scenario 1 of 3</span>
          </div>

          <div class="space-y-4">
            <div class="p-4 rounded-xl bg-dark-950 border border-dark-800 space-y-2">
              <span class="text-[11px] font-mono text-amber-400 font-semibold uppercase">The Dilemma:</span>
              <p class="text-sm text-slate-200 leading-relaxed">
                The non-technical founder messages you on Slack at 8:00 AM EST: <br/>
                <em>“Hey! Let's hook up GPT-4 to parse all our 50,000 daily incoming customer support inquiries and auto-reply immediately. Can we launch this tomorrow?”</em>
              </p>
            </div>

            <div class="grid grid-cols-1 gap-3 text-xs">
              
              <button onclick="handleScenarioAnswer(1, 'A')" class="scenario-btn p-4 rounded-xl bg-dark-900 border border-dark-800 hover:border-rose-500/50 text-left transition flex items-start gap-3">
                <span class="w-6 h-6 rounded-lg bg-dark-800 font-mono font-bold flex items-center justify-center shrink-0 text-slate-300">A</span>
                <div>
                  <strong class="text-slate-200">“Yes sure, I will write the Python script right now and deploy it before evening.”</strong>
                  <p class="text-[11px] text-slate-400 mt-1">(Uncritical agreement without assessing cost or hallucinations)</p>
                </div>
              </button>

              <button onclick="handleScenarioAnswer(1, 'B')" class="scenario-btn p-4 rounded-xl bg-dark-900 border border-dark-800 hover:border-rose-500/50 text-left transition flex items-start gap-3">
                <span class="w-6 h-6 rounded-lg bg-dark-800 font-mono font-bold flex items-center justify-center shrink-0 text-slate-300">B</span>
                <div>
                  <strong class="text-slate-200">“No, that is impossible. You didn't give me any PRD or dataset, and LLMs make mistakes so we shouldn't do it.”</strong>
                  <p class="text-[11px] text-slate-400 mt-1">(Pure negative blocker with no alternative solutions)</p>
                </div>
              </button>

              <button onclick="handleScenarioAnswer(1, 'C')" class="scenario-btn p-4 rounded-xl bg-dark-900 border border-dark-800 hover:border-brand-500/50 text-left transition flex items-start gap-3">
                <span class="w-6 h-6 rounded-lg bg-dark-800 font-mono font-bold flex items-center justify-center shrink-0 text-slate-300">C</span>
                <div>
                  <strong class="text-slate-200">“Love the vision! Two critical considerations: (1) 50k calls/day directly on GPT-4 will burn ~$4,500/month. (2) Zero-shot auto-replies risk hallucinations on billing. I propose: (a) Rule regex catches 60% standard questions at $0. (b) Claude 3.5 Haiku handles 35% at $40/mo. (c) Escalate only 5% complex queries. I have a working prototype ready to test on 100 sample tickets in 3 hours. Loom link below.”</strong>
                  <p class="text-[11px] text-slate-400 mt-1">(High-agency: Validates goal, provides cost math, proposes hybrid architecture, shows proof)</p>
                </div>
              </button>

            </div>

            <div id="scenario-feedback-box" class="hidden p-4 rounded-xl text-xs space-y-2"></div>

          </div>

        </div>

      </section>

      <!-- ==================================================== -->
      <!-- SECTION 4: MODULE 3 - 5-TO-8 WEEK ACTION ROADMAP     -->
      <!-- ==================================================== -->
      <section id="roadmap-section" class="space-y-8 scroll-mt-24">
        
        <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4 border-b border-dark-800 pb-6">
          <div class="space-y-2">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 text-xs font-semibold">
              <i data-lucide="map-pin" class="w-3.5 h-3.5"></i> Module 3: Execution Roadmap
            </div>
            <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              The 5-to-8 Week Interactive Action Roadmap
            </h2>
            <p class="text-xs sm:text-sm text-slate-400 max-w-2xl">
              Track your journey from zero experience to signed $60k–$120k US remote contract. All progress and notes are auto-saved to your browser.
            </p>
          </div>

          <!-- Total Roadmap Progress -->
          <div class="flex items-center gap-3">
            <div class="text-right">
              <span id="roadmap-total-percentage" class="text-2xl font-mono font-black text-brand-400">0%</span>
              <span class="text-xs text-slate-400 block">Completed</span>
            </div>
          </div>
        </div>

        <!-- Phase Tabs Navigation -->
        <div class="flex flex-wrap gap-2 p-1.5 rounded-2xl bg-dark-950 border border-dark-800">
          <button onclick="switchRoadmapPhase(1)" id="phase-tab-1" class="tab-btn active px-4 py-2 rounded-xl text-xs font-semibold transition flex items-center gap-2">
            <span>Phase 1: Proof of Work (W1–3)</span>
          </button>
          <button onclick="switchRoadmapPhase(2)" id="phase-tab-2" class="tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-400 hover:text-white transition flex items-center gap-2">
            <span>Phase 2: The Offer Framework (W4)</span>
          </button>
          <button onclick="switchRoadmapPhase(3)" id="phase-tab-3" class="tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-400 hover:text-white transition flex items-center gap-2">
            <span>Phase 3: LinkedIn Branding (W5–6)</span>
          </button>
          <button onclick="switchRoadmapPhase(4)" id="phase-tab-4" class="tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-400 hover:text-white transition flex items-center gap-2">
            <span>Phase 4: Cold Outreach Engine (W7–8)</span>
          </button>
        </div>

        <!-- PHASE 1 CONTENT -->
        <div id="phase-content-1" class="space-y-6">
          <div class="p-5 rounded-2xl bg-dark-950/80 border-l-4 border-l-brand-500 border border-dark-750 space-y-2">
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <i data-lucide="hammer" class="w-5 h-5 text-brand-400"></i>
              Weeks 1–3: Build Production-Grade Proof of Work
            </h3>
            <p class="text-xs sm:text-sm text-slate-300">
              Never build toy projects like Titanic, MNIST, or generic To-Do lists. Map 2–3 high-impact production systems directly to real startup Job Descriptions (JDs) with cost and scale metrics.
            </p>
          </div>

          <!-- Phase 1 Checklist Items -->
          <div class="space-y-3" id="phase-1-checklist">
            <!-- Rendered by JS with interactive checkboxes -->
          </div>
        </div>

        <!-- PHASE 2 CONTENT -->
        <div id="phase-content-2" class="space-y-6 hidden">
          <div class="p-5 rounded-2xl bg-dark-950/80 border-l-4 border-l-accent-500 border border-dark-750 space-y-2">
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <i data-lucide="shield-check" class="w-5 h-5 text-accent-400"></i>
              Week 4: The Offer Framework (De-Risking Founder Friction)
            </h3>
            <p class="text-xs sm:text-sm text-slate-300">
              Founders reject remote candidates because of 5 specific perceived risks. Use our Offer Framework to reverse every risk before they even bring it up.
            </p>
          </div>

          <div class="space-y-3" id="phase-2-checklist"></div>
        </div>

        <!-- PHASE 3 CONTENT -->
        <div id="phase-content-3" class="space-y-6 hidden">
          <div class="p-5 rounded-2xl bg-dark-950/80 border-l-4 border-l-blue-500 border border-dark-750 space-y-2">
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <i data-lucide="linkedin" class="w-5 h-5 text-blue-400"></i>
              Weeks 5–6: LinkedIn Profile & Authentic Content System
            </h3>
            <p class="text-xs sm:text-sm text-slate-300">
              Transform your LinkedIn from an ignored online resume into an inbound magnet using our 16-formula headline bank, 5-block About framework, and 3x/week build-in-public scheduler.
            </p>
          </div>

          <div class="space-y-3" id="phase-3-checklist"></div>
        </div>

        <!-- PHASE 4 CONTENT -->
        <div id="phase-content-4" class="space-y-6 hidden">
          <div class="p-5 rounded-2xl bg-dark-950/80 border-l-4 border-l-amber-500 border border-dark-750 space-y-2">
            <h3 class="text-base font-bold text-white flex items-center gap-2">
              <i data-lucide="send" class="w-5 h-5 text-amber-400"></i>
              Weeks 7–8: The 20–25 Daily Cold Outreach Engine
            </h3>
            <p class="text-xs sm:text-sm text-slate-300">
              Build a steady pipeline contacting 20–25 decision makers daily (~800/month) across Y Combinator, Product Hunt, and Canadian funded startups with value-first personalized pitches.
            </p>
          </div>

          <div class="space-y-3" id="phase-4-checklist"></div>
        </div>

      </section>

      <!-- ==================================================== -->
      <!-- SECTION 5: 6 PRODUCTION PROJECT BLUEPRINTS           -->
      <!-- ==================================================== -->
      <section id="blueprints-section" class="space-y-8 scroll-mt-24">
        
        <div class="space-y-2 border-b border-dark-800 pb-6">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-violet-500/10 text-violet-400 text-xs font-semibold">
            <i data-lucide="cpu" class="w-3.5 h-3.5"></i> Production Proof Blueprints
          </div>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            6 Production-Grade Project Blueprints (Zero Trivial Datasets)
          </h2>
          <p class="text-xs sm:text-sm text-slate-400 max-w-2xl">
            Choose 1 to 2 projects from this blueprint vault. Each project is engineered with realistic scale, cost metrics, and system trade-offs that make US founders stop and interview you.
          </p>
        </div>

        <!-- Project Cards Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6" id="blueprints-container">
          <!-- Populated by JavaScript -->
        </div>

      </section>

      <!-- ==================================================== -->
      <!-- SECTION 6: INTERACTIVE JD PROJECT MAPPER ENGINE     -->
      <!-- ==================================================== -->
      <section id="jd-mapper-section" class="glass-card p-6 sm:p-8 space-y-6 border-dark-750 scroll-mt-24">
        
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-dark-800 pb-5">
          <div class="space-y-1">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-pink-500/10 text-pink-400 text-xs font-semibold">
              <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Custom Blueprint Generator
            </div>
            <h3 class="text-lg sm:text-xl font-bold text-white">
              Target Job Description (JD) Project Mapper
            </h3>
            <p class="text-xs text-slate-400">
              Found a US startup job description you want to target? Paste it below to generate the exact 3-tier proof-of-work project blueprint to build for them.
            </p>
          </div>
          <button onclick="loadSampleJD()" class="text-xs font-mono text-pink-400 hover:text-pink-300 underline">
            Load Sample US Remote JD
          </button>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6 items-start">
          
          <div class="space-y-3">
            <label class="text-xs font-semibold text-slate-300">Paste Target Startup Job Description:</label>
            <textarea 
              id="jd-input-text" 
              rows="9" 
              placeholder="Paste company info, required stack, job responsibilities, and challenges here..."
              class="w-full bg-dark-950 border border-dark-750 rounded-xl p-4 text-xs font-mono text-slate-200 focus:border-pink-500 focus:outline-none transition resize-y leading-relaxed"
            ></textarea>
            
            <div class="flex gap-3">
              <button onclick="analyzeJDAndGenerateBlueprint()" class="flex-1 py-2.5 rounded-xl bg-gradient-to-r from-pink-500 to-accent-600 hover:from-pink-600 hover:to-accent-700 text-white font-bold text-xs flex items-center justify-center gap-2 transition shadow-md">
                <i data-lucide="wand-2" class="w-4 h-4"></i> Generate Tailored Project Blueprint
              </button>
            </div>
          </div>

          <!-- Generated Blueprint Output Box -->
          <div id="jd-output-box" class="p-5 rounded-xl bg-dark-950 border border-dark-800 space-y-4 min-h-[220px]">
            <div class="flex items-center justify-between border-b border-dark-800 pb-3">
              <span class="text-xs font-bold text-pink-400 uppercase font-mono flex items-center gap-1.5">
                <i data-lucide="cpu" class="w-3.5 h-3.5"></i> Generated Tailored Blueprint
              </span>
              <button id="copy-jd-blueprint-btn" onclick="copyJDOutput()" class="text-[11px] font-mono text-slate-400 hover:text-white flex items-center gap-1 transition">
                <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy Plan
              </button>
            </div>
            
            <div id="jd-output-content" class="text-xs text-slate-300 space-y-3 leading-relaxed">
              <p class="text-slate-500 italic">Paste a JD on the left and click "Generate Tailored Project Blueprint" to extract core architectural requirements, key founder risk factors, and recommended MVP architecture.</p>
            </div>
          </div>

        </div>

      </section>

      <!-- ==================================================== -->
      <!-- SECTION 7: THE OFFER FRAMEWORK & PROPOSAL GENERATOR  -->
      <!-- ==================================================== -->
      <section id="offer-framework-section" class="glass-card p-6 sm:p-8 space-y-6 border-dark-750 scroll-mt-24">
        
        <div class="space-y-2 border-b border-dark-800 pb-5">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 text-xs font-semibold">
            <i data-lucide="shield-check" class="w-3.5 h-3.5"></i> Risk Reversal Engine
          </div>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            The Offer Framework: De-Risking Founder Friction
          </h2>
          <p class="text-xs sm:text-sm text-slate-400 max-w-2xl">
            Why do US founders hesitate to hire remote developers? Below are the 5 core friction points and how to reverse the risk into an instant "YES".
          </p>
        </div>

        <!-- 5 Friction Points Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          
          <div class="p-4 rounded-xl bg-dark-950 border border-dark-800 space-y-2">
            <div class="flex items-center gap-2 text-rose-400 text-xs font-bold font-mono">
              <i data-lucide="alert-circle" class="w-4 h-4"></i> Risk 1: Execution Uncertainty
            </div>
            <p class="text-xs text-slate-400">“Will this engineer actually ship clean code or get stuck on basic tasks?”</p>
            <div class="text-xs text-emerald-300 pt-2 border-t border-dark-800 font-medium">
              <strong>Your Risk Reversal:</strong> Paid 1-week scoped trial task with clearly defined deliverables & PR review.
            </div>
          </div>

          <div class="p-4 rounded-xl bg-dark-950 border border-dark-800 space-y-2">
            <div class="flex items-center gap-2 text-rose-400 text-xs font-bold font-mono">
              <i data-lucide="clock" class="w-4 h-4"></i> Risk 2: Timezone Mismatch
            </div>
            <p class="text-xs text-slate-400">“Will they only be awake while we are asleep, creating 24-hour delays?”</p>
            <div class="text-xs text-emerald-300 pt-2 border-t border-dark-800 font-medium">
              <strong>Your Risk Reversal:</strong> Guaranteed 4-hour daily overlap commitment (e.g. 7 AM – 11 AM EST / 5:30 PM – 9:30 PM IST).
            </div>
          </div>

          <div class="p-4 rounded-xl bg-dark-950 border border-dark-800 space-y-2">
            <div class="flex items-center gap-2 text-rose-400 text-xs font-bold font-mono">
              <i data-lucide="message-square" class="w-4 h-4"></i> Risk 3: Communication Fog
            </div>
            <p class="text-xs text-slate-400">“Will they disappear for 4 days without giving updates?”</p>
            <div class="text-xs text-emerald-300 pt-2 border-t border-dark-800 font-medium">
              <strong>Your Risk Reversal:</strong> Daily 2-minute async Loom walkthrough + 3-bullet Slack progress update.
            </div>
          </div>

          <div class="p-4 rounded-xl bg-dark-950 border border-dark-800 space-y-2">
            <div class="flex items-center gap-2 text-rose-400 text-xs font-bold font-mono">
              <i data-lucide="file-text" class="w-4 h-4"></i> Risk 4: Legal & Payroll Hassle
            </div>
            <p class="text-xs text-slate-400">“How do we legally contract with someone in India without complex local entities?”</p>
            <div class="text-xs text-emerald-300 pt-2 border-t border-dark-800 font-medium">
              <strong>Your Risk Reversal:</strong> Seamless international contractor invoicing via Deel, Remote.com, or direct Stripe/Wise wire.
            </div>
          </div>

          <div class="p-4 rounded-xl bg-dark-950 border border-dark-800 space-y-2">
            <div class="flex items-center gap-2 text-rose-400 text-xs font-bold font-mono">
              <i data-lucide="zap" class="w-4 h-4"></i> Risk 5: Speed of Ramp-Up
            </div>
            <p class="text-xs text-slate-400">“Will it take 2 months for them to understand our tech stack?”</p>
            <div class="text-xs text-emerald-300 pt-2 border-t border-dark-800 font-medium">
              <strong>Your Risk Reversal:</strong> Send a pre-interview product audit/teardown finding an active bug or performance improvement.
            </div>
          </div>

          <div class="p-4 rounded-xl bg-dark-950 border border-brand-500/40 space-y-2 flex flex-col justify-between shadow-sm">
            <div>
              <span class="text-xs font-bold text-brand-400 uppercase font-mono">Quick Pitch Deck Generator</span>
              <p class="text-xs text-slate-300 mt-1">Generate a 1-page risk reversal proposal ready to attach in founder DMs.</p>
            </div>
            <button onclick="openProposalGeneratorModal()" class="w-full py-2 rounded-xl bg-brand-500 hover:bg-brand-600 text-dark-950 text-xs font-bold transition shadow-sm">
              Build Risk Reversal Proposal →
            </button>
          </div>

        </div>

      </section>

      <!-- ==================================================== -->
      <!-- SECTION 8: LINKEDIN OPTIMIZATION STUDIO              -->
      <!-- ==================================================== -->
      <section id="linkedin-toolkit-section" class="space-y-8 scroll-mt-24">
        
        <div class="space-y-2 border-b border-dark-800 pb-6">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/10 text-blue-400 text-xs font-semibold">
            <i data-lucide="linkedin" class="w-3.5 h-3.5"></i> Inbound Authority Engine
          </div>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            LinkedIn Optimization Studio (From the ANTERN Toolkit)
          </h2>
          <p class="text-xs sm:text-sm text-slate-400 max-w-2xl">
            Stop listing skills. Start demonstrating judgment. Your profile is not a static resume—it is an inbound system to reduce hiring manager perceived risk.
          </p>
        </div>

        <!-- Studio Tabs -->
        <div class="glass-card p-6 sm:p-8 space-y-6 border-dark-750">
          
          <div class="flex flex-wrap gap-2 border-b border-dark-800 pb-4">
            <button onclick="switchLinkedInTab('headlines')" id="li-tab-headlines" class="tab-btn active px-4 py-2 rounded-xl text-xs font-semibold transition">
              16 Headline Formulas
            </button>
            <button onclick="switchLinkedInTab('about')" id="li-tab-about" class="tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-400 hover:text-white transition">
              5-Block About Generator
            </button>
            <button onclick="switchLinkedInTab('checklist')" id="li-tab-checklist" class="tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-400 hover:text-white transition">
              Profile Audit Checklist
            </button>
            <button onclick="switchLinkedInTab('featured')" id="li-tab-featured" class="tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-400 hover:text-white transition">
              3-Slot Featured Strategy
            </button>
            <button onclick="switchLinkedInTab('content')" id="li-tab-content" class="tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-400 hover:text-white transition">
              3x/Week Content Scheduler
            </button>
            <button onclick="switchLinkedInTab('launch30')" id="li-tab-launch30" class="tab-btn px-4 py-2 rounded-xl text-xs font-semibold text-slate-400 hover:text-white transition">
              30-Day Launch Plan
            </button>
          </div>

          <!-- VALUE EQUATION & INSTRUMENTATION BANNER -->
          <div class="p-4 rounded-xl bg-gradient-to-r from-blue-950/40 via-dark-950 to-dark-900 border border-blue-800/40 space-y-2">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <span class="text-xs font-mono font-bold text-blue-400 flex items-center gap-1.5">
                <i data-lucide="calculator" class="w-4 h-4"></i>
                The Hiring Manager Value Equation
              </span>
              <span class="text-[11px] font-mono text-slate-400">Target Acceptance: <strong class="text-brand-400">40%+</strong> | Target Reply: <strong class="text-accent-400">20%+</strong></span>
            </div>
            <p class="text-xs font-mono text-slate-200">
              <span class="text-emerald-300 font-bold">Value</span> = (<span class="text-white">Dream Outcome</span> × <span class="text-white">Perceived Likelihood</span>) ÷ (<span class="text-white">Time Delay</span> × <span class="text-white">Effort & Sacrifice</span>)
            </p>
            <p class="text-[11px] text-slate-400 leading-relaxed">
              Every section of your LinkedIn must increase <strong>Perceived Likelihood</strong> (they believe you can deliver) and decrease <strong>Time Delay</strong> (you can contribute immediately). Treat your profile like a production ML system: instrument it, measure it, iterate.
            </p>
          </div>

          <!-- TAB 1: 16 HEADLINE FORMULAS -->
          <div id="li-content-headlines" class="space-y-5">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
              <p class="text-xs text-slate-300">
                You have <strong>3 seconds</strong> to communicate value. Your headline must state: <span class="font-mono text-brand-400">Outcome + Target Audience + Proof Metric</span>.
              </p>
              <span class="text-xs font-mono text-slate-400">16 Tested Formulas</span>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4" id="headline-formulas-grid">
              <!-- Rendered by JS -->
            </div>
          </div>

          <!-- TAB 2: 5-BLOCK ABOUT SECTION -->
          <div id="li-content-about" class="space-y-6 hidden">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
              <div>
                <h4 class="text-sm font-bold text-white">The 5-Block About Section Framework (150–250 words)</h4>
                <p class="text-xs text-slate-400">Block 1: The Hook • Block 2: The Proof • Block 3: The Method • Block 4: The Stack • Block 5: The CTA</p>
              </div>
              <div class="flex gap-2">
                <button onclick="loadAboutTemplate('A')" class="px-3 py-1.5 rounded-lg bg-dark-750 hover:bg-dark-700 text-xs text-slate-200 transition">Template A (Cost Builder)</button>
                <button onclick="loadAboutTemplate('B')" class="px-3 py-1.5 rounded-lg bg-dark-750 hover:bg-dark-700 text-xs text-slate-200 transition">Template B (Production First)</button>
                <button onclick="loadAboutTemplate('C')" class="px-3 py-1.5 rounded-lg bg-dark-750 hover:bg-dark-700 text-xs text-slate-200 transition">Template C (Career Switcher)</button>
              </div>
            </div>

            <div class="space-y-4">
              <textarea 
                id="about-textarea" 
                rows="10" 
                class="w-full bg-dark-950 border border-dark-750 rounded-xl p-4 text-xs font-mono text-slate-200 leading-relaxed focus:border-brand-500 focus:outline-none"
              ></textarea>
              <div class="flex justify-between items-center">
                <span id="about-word-count" class="text-xs font-mono text-slate-400">Word Count: 0 words (Target: 150-250)</span>
                <button onclick="copyAboutText()" class="px-4 py-2 rounded-xl bg-brand-500 hover:bg-brand-600 text-dark-950 text-xs font-bold flex items-center gap-1.5 transition shadow-sm">
                  <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy About Pitch
                </button>
              </div>
            </div>
          </div>

          <!-- TAB: PROFILE CHECKLIST (TAB 2) -->
          <div id="li-content-checklist" class="space-y-6 hidden">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-dark-800 pb-4">
              <div>
                <h4 class="text-sm font-bold text-white flex items-center gap-2">
                  <i data-lucide="check-square" class="w-4 h-4 text-blue-400"></i> Profile Checklist
                </h4>
                <p class="text-xs text-slate-400">Complete items in order to reduce hiring manager perceived risk.</p>
              </div>
              <div class="flex items-center gap-3">
                <span id="profile-checklist-progress-badge" class="text-xs font-mono bg-blue-500/20 text-blue-300 px-3 py-1 rounded-lg font-semibold">
                  0/23 completed (0%)
                </span>
                <button onclick="resetProfileChecklist()" class="text-xs text-slate-400 hover:text-rose-400 flex items-center gap-1 font-mono transition">
                  <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i> Reset
                </button>
              </div>
            </div>

            <!-- Progress Bar -->
            <div class="w-full bg-dark-950 h-2 rounded-full overflow-hidden border border-dark-800 p-0.5">
              <div id="profile-checklist-progress-bar" class="bg-gradient-to-r from-blue-500 to-brand-400 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
            </div>

            <!-- 6 Group Categories Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-5" id="profile-checklist-container">
              <!-- Rendered by JS -->
            </div>
          </div>

          <!-- TAB 3: FEATURED 3-SLOT STRATEGY -->
          <div id="li-content-featured" class="space-y-5 hidden">
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
              
              <div class="p-4 rounded-xl bg-dark-950 border border-dark-800 space-y-3">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-bold text-brand-400 font-mono uppercase">Slot 1 (Centerpiece)</span>
                  <span class="text-[10px] bg-brand-500/10 text-brand-300 px-2 py-0.5 rounded font-mono font-semibold">System Proof</span>
                </div>
                <h5 class="text-sm font-bold text-white">Your Best Case Study Repo</h5>
                <p class="text-xs text-slate-400 leading-relaxed">GitHub repo or live demo with comprehensive README, architecture diagram, and cost analysis.</p>
                <div class="text-[11px] font-mono text-slate-300 bg-dark-900 p-2.5 rounded border border-dark-800">
                  Example: <em>“Hybrid Customer Support Classifier: 100K req/day at $23/mo — Full Architecture & Cost Analysis”</em>
                </div>
              </div>

              <div class="p-4 rounded-xl bg-dark-950 border border-dark-800 space-y-3">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-bold text-accent-400 font-mono uppercase">Slot 2 (Social Proof)</span>
                  <span class="text-[10px] bg-accent-500/10 text-accent-300 px-2 py-0.5 rounded font-mono font-semibold">Thinking Proof</span>
                </div>
                <h5 class="text-sm font-bold text-white">Highest Engagement Post</h5>
                <p class="text-xs text-slate-400 leading-relaxed">Your most commented LinkedIn post breaking down a technical trade-off or architectural failure.</p>
                <div class="text-[11px] font-mono text-slate-300 bg-dark-900 p-2.5 rounded border border-dark-800">
                  Example: <em>“Why fine-tuning wasn't worth the cost for 100k requests/mo: The exact math and benchmark results”</em>
                </div>
              </div>

              <div class="p-4 rounded-xl bg-dark-950 border border-dark-800 space-y-3">
                <div class="flex items-center justify-between">
                  <span class="text-xs font-bold text-sky-400 font-mono uppercase">Slot 3 (Visual Artifact)</span>
                  <span class="text-[10px] bg-sky-500/10 text-sky-300 px-2 py-0.5 rounded font-mono font-semibold">Visual Proof</span>
                </div>
                <h5 class="text-sm font-bold text-white">Architecture / Cost Chart</h5>
                <p class="text-xs text-slate-400 leading-relaxed">Visual PDF or diagram showing tiered routing, monitoring metrics, or drift detection graphs.</p>
                <div class="text-[11px] font-mono text-slate-300 bg-dark-900 p-2.5 rounded border border-dark-800">
                  Example: <em>“Single-page PDF: Multi-tiered RAG routing system architecture & memory profiling breakdown”</em>
                </div>
              </div>

            </div>
          </div>

          <!-- TAB 4: 3X/WEEK CONTENT SCHEDULER -->
          <div id="li-content-content" class="space-y-5 hidden">
            <div class="flex items-center justify-between">
              <p class="text-xs text-slate-300">
                Consistency compounds. Pick a post archetype to generate an authentic, high-converting LinkedIn post draft:
              </p>
            </div>

            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-2">
              <button onclick="loadContentPrompt('confusion')" class="p-2.5 rounded-xl bg-dark-950 hover:bg-dark-750 border border-dark-800 text-xs font-medium text-slate-200 text-center transition">
                🤯 Confusion Post
              </button>
              <button onclick="loadContentPrompt('mistake')" class="p-2.5 rounded-xl bg-dark-950 hover:bg-dark-750 border border-dark-800 text-xs font-medium text-slate-200 text-center transition">
                🐛 Mistake / Bug
              </button>
              <button onclick="loadContentPrompt('tradeoff')" class="p-2.5 rounded-xl bg-dark-950 hover:bg-dark-750 border border-dark-800 text-xs font-medium text-slate-200 text-center transition">
                ⚖️ Trade-off Math
              </button>
              <button onclick="loadContentPrompt('cost')" class="p-2.5 rounded-xl bg-dark-950 hover:bg-dark-750 border border-dark-800 text-xs font-medium text-slate-200 text-center transition">
                💰 Cost Breakdown
              </button>
              <button onclick="loadContentPrompt('build')" class="p-2.5 rounded-xl bg-dark-950 hover:bg-dark-750 border border-dark-800 text-xs font-medium text-slate-200 text-center transition">
                🚀 Build in Public
              </button>
              <button onclick="loadContentPrompt('failure')" class="p-2.5 rounded-xl bg-dark-950 hover:bg-dark-750 border border-dark-800 text-xs font-medium text-slate-200 text-center transition">
                💥 Failure Post-Mortem
              </button>
            </div>

            <div class="space-y-3">
              <textarea 
                id="post-draft-textarea" 
                rows="8" 
                class="w-full bg-dark-950 border border-dark-750 rounded-xl p-4 text-xs font-mono text-slate-200 leading-relaxed focus:border-brand-500 focus:outline-none"
                placeholder="Click one of the archetypes above to load a high-converting template..."
              ></textarea>
              <div class="flex justify-end">
                <button onclick="copyPostDraft()" class="px-4 py-2 rounded-xl bg-brand-500 hover:bg-brand-600 text-dark-950 text-xs font-bold flex items-center gap-1.5 transition shadow-sm">
                  <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy Post Draft
                </button>
              </div>
            </div>

          </div>

          <!-- TAB: 30-DAY LAUNCH PLAN (TAB 1) -->
          <div id="li-content-launch30" class="space-y-6 hidden">
            <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-dark-800 pb-4">
              <div>
                <h4 class="text-sm font-bold text-white flex items-center gap-2">
                  <i data-lucide="calendar" class="w-4 h-4 text-emerald-400"></i> 30-Day Launch Plan
                </h4>
                <p class="text-xs text-slate-400">Follow this day-by-day checklist to launch your inbound authority engine.</p>
              </div>
              <div class="flex items-center gap-3">
                <span id="launch-30-progress-badge" class="text-xs font-mono bg-brand-500/20 text-brand-300 px-3 py-1 rounded-lg font-semibold">
                  0/10 completed (0%)
                </span>
                <button onclick="resetLaunch30Plan()" class="text-xs text-slate-400 hover:text-rose-400 flex items-center gap-1 font-mono transition">
                  <i data-lucide="rotate-ccw" class="w-3.5 h-3.5"></i> Reset
                </button>
              </div>
            </div>

            <!-- Progress Bar -->
            <div class="w-full bg-dark-950 h-2 rounded-full overflow-hidden border border-dark-800 p-0.5">
              <div id="launch-30-progress-bar" class="bg-gradient-to-r from-brand-500 to-accent-500 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
            </div>

            <!-- Day-by-Day Checklist Table -->
            <div class="overflow-x-auto rounded-2xl border border-dark-800 bg-dark-950/60">
              <table class="w-full text-left text-xs border-collapse">
                <thead class="bg-dark-950 border-b border-dark-800 text-slate-400 font-mono text-[11px] uppercase">
                  <tr>
                    <th class="py-3 px-4 w-12 text-center">Status</th>
                    <th class="py-3 px-4 w-28">Timeline</th>
                    <th class="py-3 px-4">Milestone & Action Items</th>
                    <th class="py-3 px-4 text-right">Progress</th>
                  </tr>
                </thead>
                <tbody id="launch-30-tbody" class="divide-y divide-dark-800/80 text-slate-300">
                  <!-- Rendered by JS -->
                </tbody>
              </table>
            </div>
          </div>

        </div>

      </section>

      <!-- ==================================================== -->
      <!-- SECTION 9: MODULE 4 - OUTBOUND PROSPECTING CRM       -->
      <!-- ==================================================== -->
      <section id="kanban-section" class="space-y-8 scroll-mt-24">
        
        <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-4 border-b border-dark-800 pb-6">
          <div class="space-y-2">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-brand-500/10 text-brand-400 text-xs font-semibold">
              <i data-lucide="kanban-square" class="w-3.5 h-3.5"></i> Module 4: Outreach CRM
            </div>
            <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              Cold Outreach Kanban & Pipeline Engine
            </h2>
            <p class="text-xs sm:text-sm text-slate-400 max-w-2xl">
              Track decision-maker conversations across 5 recruitment stages. Pre-loaded with verified tech companies from our Canadian & US dataset.
            </p>
          </div>

          <!-- CRM Actions -->
          <div class="flex items-center gap-2">
            <button onclick="openAddLeadModal()" class="px-3.5 py-2 rounded-xl bg-brand-500 hover:bg-brand-600 text-dark-950 text-xs font-bold flex items-center gap-1.5 transition shadow-sm">
              <i data-lucide="plus" class="w-4 h-4"></i> Add Target Lead
            </button>
            <button onclick="openLeadDatabaseModal()" class="px-3.5 py-2 rounded-xl bg-dark-800 hover:bg-dark-750 text-slate-200 border border-dark-700 text-xs font-semibold flex items-center gap-1.5 transition">
              <i data-lucide="database" class="w-4 h-4 text-accent-400"></i> Browse 300+ Preloaded Leads
            </button>
          </div>
        </div>

        <!-- Cold Outreach Message Vault -->
        <div class="glass-card p-6 space-y-4 border-dark-750">
          <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-dark-800 pb-3">
            <h3 class="text-sm font-bold text-white flex items-center gap-2">
              <i data-lucide="send" class="w-4 h-4 text-brand-400"></i>
              Cold Outreach DM & Email Message Generator
            </h3>
            <span class="text-xs text-slate-400">Lead with value, never beg for a job</span>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
            <button onclick="loadOutreachTemplate(1)" id="outreach-btn-1" class="outreach-tab-btn active p-3 rounded-xl bg-dark-950 border border-brand-500/40 text-left transition">
              <div class="font-bold text-xs text-white">Phase 1: Curiosity DM</div>
              <p class="text-[11px] text-slate-400 mt-0.5">For learning stage & asking about specific architecture</p>
            </button>

            <button onclick="loadOutreachTemplate(2)" id="outreach-btn-2" class="outreach-tab-btn p-3 rounded-xl bg-dark-950 border border-dark-800 text-left transition">
              <div class="font-bold text-xs text-white">Phase 2: Trade-off DM</div>
              <p class="text-[11px] text-slate-400 mt-0.5">For comparing approaches on their newly launched feature</p>
            </button>

            <button onclick="loadOutreachTemplate(3)" id="outreach-btn-3" class="outreach-tab-btn p-3 rounded-xl bg-dark-950 border border-dark-800 text-left transition">
              <div class="font-bold text-xs text-white">Phase 3: Ownership Demo DM</div>
              <p class="text-[11px] text-slate-400 mt-0.5">For pitching your cost reduction demo directly to founder</p>
            </button>
          </div>

          <div class="space-y-3">
            <div class="relative">
              <textarea 
                id="outreach-template-text" 
                rows="4" 
                class="w-full bg-dark-950 border border-dark-750 rounded-xl p-3 text-xs font-mono text-slate-200 leading-relaxed focus:border-brand-500 focus:outline-none"
              ></textarea>
            </div>
            <div class="flex justify-between items-center text-xs">
              <span class="text-slate-400 text-[11px]">Replace highlighted placeholders with your actual project links and target info.</span>
              <button onclick="copyOutreachTemplate()" class="px-3.5 py-1.5 rounded-lg bg-brand-500 hover:bg-brand-600 text-dark-950 font-bold flex items-center gap-1.5 transition shadow-sm">
                <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy Message
              </button>
            </div>
          </div>
        </div>

        <!-- Kanban Board Columns -->
        <div class="grid grid-cols-1 md:grid-cols-3 lg:grid-cols-5 gap-4 items-start" id="kanban-board">
          
          <!-- Column 1: Target Startup -->
          <div class="space-y-3">
            <div class="flex items-center justify-between px-3 py-2 rounded-xl bg-dark-950 border border-dark-800">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-slate-400"></span>
                <span class="text-xs font-bold text-slate-200">1. Target Startup</span>
              </div>
              <span id="col-count-target" class="text-xs font-mono px-1.5 py-0.2 rounded bg-dark-800 text-slate-400">0</span>
            </div>
            <div id="col-target-container" class="space-y-2.5 min-h-[300px] p-2 rounded-2xl bg-dark-950/40 border border-dark-800">
              <!-- Cards rendered here -->
            </div>
          </div>

          <!-- Column 2: Outreach Sent -->
          <div class="space-y-3">
            <div class="flex items-center justify-between px-3 py-2 rounded-xl bg-dark-950 border border-dark-800">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-blue-400"></span>
                <span class="text-xs font-bold text-blue-200">2. Outreach Sent</span>
              </div>
              <span id="col-count-sent" class="text-xs font-mono px-1.5 py-0.2 rounded bg-dark-800 text-slate-400">0</span>
            </div>
            <div id="col-sent-container" class="space-y-2.5 min-h-[300px] p-2 rounded-2xl bg-dark-950/40 border border-dark-800">
              <!-- Cards rendered here -->
            </div>
          </div>

          <!-- Column 3: In Conversation -->
          <div class="space-y-3">
            <div class="flex items-center justify-between px-3 py-2 rounded-xl bg-dark-950 border border-dark-800">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-accent-400"></span>
                <span class="text-xs font-bold text-accent-200">3. In Conversation</span>
              </div>
              <span id="col-count-conversation" class="text-xs font-mono px-1.5 py-0.2 rounded bg-dark-800 text-slate-400">0</span>
            </div>
            <div id="col-conversation-container" class="space-y-2.5 min-h-[300px] p-2 rounded-2xl bg-dark-950/40 border border-dark-800">
              <!-- Cards rendered here -->
            </div>
          </div>

          <!-- Column 4: Interview Scheduled -->
          <div class="space-y-3">
            <div class="flex items-center justify-between px-3 py-2 rounded-xl bg-dark-950 border border-dark-800">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
                <span class="text-xs font-bold text-amber-200">4. Interview / Trial</span>
              </div>
              <span id="col-count-interview" class="text-xs font-mono px-1.5 py-0.2 rounded bg-dark-800 text-slate-400">0</span>
            </div>
            <div id="col-interview-container" class="space-y-2.5 min-h-[300px] p-2 rounded-2xl bg-dark-950/40 border border-dark-800">
              <!-- Cards rendered here -->
            </div>
          </div>

          <!-- Column 5: Offer Received -->
          <div class="space-y-3">
            <div class="flex items-center justify-between px-3 py-2 rounded-xl bg-dark-950 border border-brand-500/30">
              <div class="flex items-center gap-2">
                <span class="w-2.5 h-2.5 rounded-full bg-brand-400"></span>
                <span class="text-xs font-bold text-brand-300">5. Offer Won 🏆</span>
              </div>
              <span id="col-count-offer" class="text-xs font-mono px-1.5 py-0.2 rounded bg-brand-500/20 text-brand-400 font-semibold">0</span>
            </div>
            <div id="col-offer-container" class="space-y-2.5 min-h-[300px] p-2 rounded-2xl bg-dark-950/40 border border-brand-500/20">
              <!-- Cards rendered here -->
            </div>
          </div>

        </div>

      </section>

      <!-- ==================================================== -->
      <!-- SECTION 10: RESOURCE HUB & DOWNLOAD CENTER           -->
      <!-- ==================================================== -->
      <section id="resources-section" class="glass-card p-6 sm:p-8 space-y-6 border-dark-750 scroll-mt-24">
        
        <div class="space-y-2 border-b border-dark-800 pb-5">
          <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-orange-500/10 text-orange-400 text-xs font-semibold">
            <i data-lucide="folder-down" class="w-3.5 h-3.5"></i> Resource Vault
          </div>
          <h2 class="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            Original Resources & Implementation Hub
          </h2>
          <p class="text-xs sm:text-sm text-slate-400 max-w-2xl">
            Access the companion Google Docs, spreadsheets, video walkthroughs, and templates referenced in the US Remote Playbook.
          </p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          
          <!-- Link 1: Ayush Video Playbook -->
          <a href="https://youtu.be/C0kwzP6Gt-4" target="_blank" class="p-4 rounded-xl bg-dark-950 border border-dark-800 hover:border-brand-500/50 flex items-start gap-4 transition group">
            <div class="w-10 h-10 rounded-xl bg-rose-500/20 text-rose-400 flex items-center justify-center shrink-0 group-hover:scale-105 transition">
              <i data-lucide="play-circle" class="w-5 h-5"></i>
            </div>
            <div class="space-y-1">
              <div class="flex items-center gap-2">
                <h4 class="text-sm font-bold text-white group-hover:text-brand-400 transition">Ayush's US Remote Playbook Video</h4>
                <i data-lucide="external-link" class="w-3.5 h-3.5 text-slate-500"></i>
              </div>
              <p class="text-xs text-slate-400 leading-relaxed">Complete breakdown of how to reach US founders directly, land $60k-$100k roles, and join the selective Implementation Program.</p>
              <span class="text-[10px] font-mono text-rose-300 font-semibold">YouTube Walkthrough • 25 mins</span>
            </div>
          </a>

          <!-- Link 2: LinkedIn Toolkit Google Doc -->
          <a href="https://docs.google.com/document/d/19Dz_eysTNFiZlvD-UmMJnf9euQwOPYMu8sW9jEPP3xc/edit?usp=sharing" target="_blank" class="p-4 rounded-xl bg-dark-950 border border-dark-800 hover:border-brand-500/50 flex items-start gap-4 transition group">
            <div class="w-10 h-10 rounded-xl bg-blue-500/20 text-blue-400 flex items-center justify-center shrink-0 group-hover:scale-105 transition">
              <i data-lucide="file-text" class="w-5 h-5"></i>
            </div>
            <div class="space-y-1">
              <div class="flex items-center gap-2">
                <h4 class="text-sm font-bold text-white group-hover:text-brand-400 transition">LinkedIn Optimization Toolkit Doc</h4>
                <i data-lucide="external-link" class="w-3.5 h-3.5 text-slate-500"></i>
              </div>
              <p class="text-xs text-slate-400 leading-relaxed">Live companion Google Doc for profile audit checklist, headline formulas, and 30-day launch schedule.</p>
              <span class="text-[10px] font-mono text-blue-300 font-semibold">Google Docs Reference</span>
            </div>
          </a>

          <!-- Link 3: 7,000 Canadian Leads Google Sheet -->
          <a href="https://docs.google.com/spreadsheets/d/1SkFDRzxPi3pWkAVUZYy05RLH9P9CclQELKkw9XghGnM/edit?usp=sharing" target="_blank" class="p-4 rounded-xl bg-dark-950 border border-dark-800 hover:border-brand-500/50 flex items-start gap-4 transition group">
            <div class="w-10 h-10 rounded-xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center shrink-0 group-hover:scale-105 transition">
              <i data-lucide="table" class="w-5 h-5"></i>
            </div>
            <div class="space-y-1">
              <div class="flex items-center gap-2">
                <h4 class="text-sm font-bold text-white group-hover:text-brand-400 transition">7,000 Canadian Funded Startups Sheet</h4>
                <i data-lucide="external-link" class="w-3.5 h-3.5 text-slate-500"></i>
              </div>
              <p class="text-xs text-slate-400 leading-relaxed">Full raw spreadsheet of 7,000 recently funded startups, websites, contact emails, and founders.</p>
              <span class="text-[10px] font-mono text-emerald-300 font-semibold">Google Sheets Database</span>
            </div>
          </a>

          <!-- Link 4: Production Grade Projects Drive -->
          <a href="https://drive.google.com/file/d/1ZqFf0jUoXtyFaQ5tFHYqhjolbKpquQJV/view?usp=sharing" target="_blank" class="p-4 rounded-xl bg-dark-950 border border-dark-800 hover:border-brand-500/50 flex items-start gap-4 transition group">
            <div class="w-10 h-10 rounded-xl bg-violet-500/20 text-violet-400 flex items-center justify-center shrink-0 group-hover:scale-105 transition">
              <i data-lucide="hard-drive" class="w-5 h-5"></i>
            </div>
            <div class="space-y-1">
              <div class="flex items-center gap-2">
                <h4 class="text-sm font-bold text-white group-hover:text-brand-400 transition">Building Production Grade Projects PDF</h4>
                <i data-lucide="external-link" class="w-3.5 h-3.5 text-slate-500"></i>
              </div>
              <p class="text-xs text-slate-400 leading-relaxed">Deep-dive curriculum guide on designing systems that handle real traffic, drift detection, and cost tiering.</p>
              <span class="text-[10px] font-mono text-violet-300 font-semibold">Google Drive Document</span>
            </div>
          </a>

        </div>

      </section>

    </main>

  </div>

  <!-- ==================================================== -->
  <!-- MODALS & OVERLAYS                                    -->
  <!-- ==================================================== -->

  <!-- MODAL 1: ADD CUSTOM LEAD TO KANBAN -->
  <div id="add-lead-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="bg-dark-900 border border-dark-700 rounded-3xl max-w-lg w-full p-6 space-y-5 shadow-2xl">
      <div class="flex items-center justify-between border-b border-dark-800 pb-4">
        <h3 class="text-base font-bold text-white flex items-center gap-2">
          <i data-lucide="user-plus" class="w-4 h-4 text-brand-400"></i> Add Target Startup Lead
        </h3>
        <button onclick="closeModal('add-lead-modal')" class="text-slate-400 hover:text-white transition">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <div class="space-y-3 text-xs">
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Startup / Company Name *</label>
          <input id="lead-name-input" type="text" placeholder="e.g. Cursor, Linear, Retool, QSE Group" class="w-full bg-dark-950 border border-dark-750 rounded-xl px-3 py-2 text-white focus:border-brand-500 focus:outline-none" />
        </div>
        
        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Founder / Decision Maker</label>
            <input id="lead-founder-input" type="text" placeholder="e.g. Aman Sanger" class="w-full bg-dark-950 border border-dark-750 rounded-xl px-3 py-2 text-white focus:border-brand-500 focus:outline-none" />
          </div>
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Pipeline Stage</label>
            <select id="lead-stage-input" class="w-full bg-dark-950 border border-dark-750 rounded-xl px-3 py-2 text-white focus:border-brand-500 focus:outline-none">
              <option value="target">1. Target Startup</option>
              <option value="sent">2. Outreach Sent</option>
              <option value="conversation">3. In Conversation</option>
              <option value="interview">4. Interview / Trial</option>
              <option value="offer">5. Offer Won 🏆</option>
            </select>
          </div>
        </div>

        <div class="grid grid-cols-2 gap-3">
          <div>
            <label class="block text-slate-300 font-semibold mb-1">LinkedIn Profile URL</label>
            <input id="lead-linkedin-input" type="url" placeholder="https://linkedin.com/in/..." class="w-full bg-dark-950 border border-dark-750 rounded-xl px-3 py-2 text-white focus:border-brand-500 focus:outline-none" />
          </div>
          <div>
            <label class="block text-slate-300 font-semibold mb-1">Website URL</label>
            <input id="lead-website-input" type="url" placeholder="https://company.com" class="w-full bg-dark-950 border border-dark-750 rounded-xl px-3 py-2 text-white focus:border-brand-500 focus:outline-none" />
          </div>
        </div>

        <div>
          <label class="block text-slate-300 font-semibold mb-1">Strategic Notes / Proposed Architecture</label>
          <textarea id="lead-notes-input" rows="3" placeholder="e.g. They launched a new search feature. I noticed 4-sec latency. I built a hybrid caching demo to pitch." class="w-full bg-dark-950 border border-dark-750 rounded-xl p-3 text-white focus:border-brand-500 focus:outline-none"></textarea>
        </div>
      </div>

      <div class="flex justify-end gap-3 pt-2">
        <button onclick="closeModal('add-lead-modal')" class="px-4 py-2 rounded-xl bg-dark-800 hover:bg-dark-750 text-slate-300 text-xs font-semibold transition">Cancel</button>
        <button onclick="saveNewLead()" class="px-4 py-2 rounded-xl bg-brand-500 hover:bg-brand-600 text-dark-950 text-xs font-bold flex items-center gap-1.5 transition shadow-sm">
          <i data-lucide="check" class="w-4 h-4"></i> Save to CRM
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL 2: BROWSE PRELOADED LEADS DATABASE (FROM CANADIAN BUSINESSES) -->
  <div id="lead-database-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="bg-dark-900 border border-dark-700 rounded-3xl max-w-4xl w-full max-h-[90vh] flex flex-col p-6 space-y-4 shadow-2xl">
      <div class="flex items-center justify-between border-b border-dark-800 pb-4">
        <div>
          <h3 class="text-base font-bold text-white flex items-center gap-2">
            <i data-lucide="database" class="w-4 h-4 text-accent-400"></i>
            Funded Tech Startup Explorer (300+ Curated Leads)
          </h3>
          <p class="text-xs text-slate-400">Search and import funded software & AI companies directly into your CRM board.</p>
        </div>
        <button onclick="closeModal('lead-database-modal')" class="text-slate-400 hover:text-white transition">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <!-- Search & Filter Bar -->
      <div class="space-y-2.5">
        <div class="flex flex-col sm:flex-row gap-3">
          <div class="relative flex-1">
            <i data-lucide="search" class="w-4 h-4 text-slate-500 absolute left-3 top-2.5"></i>
            <input 
              id="lead-search-input" 
              type="text" 
              oninput="filterPreloadedLeads(this.value)" 
              placeholder="Search 300+ funded Canadian & US startups by name, AI, SaaS, health, fintech, location..." 
              class="w-full bg-dark-950 border border-dark-750 rounded-xl pl-9 pr-3 py-2 text-xs text-white focus:border-accent-500 focus:outline-none"
            />
          </div>
          <div class="text-xs font-mono text-slate-400 flex items-center shrink-0">
            Showing <span id="leads-count-filtered" class="font-bold text-brand-400 mx-1">300</span> companies
          </div>
        </div>

        <!-- Sector & City Quick Filter Buttons -->
        <div class="flex flex-wrap gap-1.5 text-[11px] font-mono">
          <button onclick="filterBySector('')" class="px-2.5 py-1 rounded-lg bg-brand-500 text-dark-950 font-bold sector-pill active transition" id="sec-pill-all">All Sectors</button>
          <button onclick="filterBySector('AI')" class="px-2.5 py-1 rounded-lg bg-dark-800 text-slate-300 hover:bg-dark-750 sector-pill transition" id="sec-pill-ai">🤖 AI / Machine Learning</button>
          <button onclick="filterBySector('Software')" class="px-2.5 py-1 rounded-lg bg-dark-800 text-slate-300 hover:bg-dark-750 sector-pill transition" id="sec-pill-saas">💻 SaaS & Cloud</button>
          <button onclick="filterBySector('Health')" class="px-2.5 py-1 rounded-lg bg-dark-800 text-slate-300 hover:bg-dark-750 sector-pill transition" id="sec-pill-health">🏥 HealthTech</button>
          <button onclick="filterBySector('Financial')" class="px-2.5 py-1 rounded-lg bg-dark-800 text-slate-300 hover:bg-dark-750 sector-pill transition" id="sec-pill-fintech">💳 FinTech & Crypto</button>
          <button onclick="filterBySector('Vancouver')" class="px-2.5 py-1 rounded-lg bg-dark-800 text-slate-300 hover:bg-dark-750 sector-pill transition" id="sec-pill-van">📍 Vancouver</button>
          <button onclick="filterBySector('Toronto')" class="px-2.5 py-1 rounded-lg bg-dark-800 text-slate-300 hover:bg-dark-750 sector-pill transition" id="sec-pill-tor">📍 Toronto</button>
          <button onclick="filterBySector('Montreal')" class="px-2.5 py-1 rounded-lg bg-dark-800 text-slate-300 hover:bg-dark-750 sector-pill transition" id="sec-pill-mtl">📍 Montreal</button>
        </div>
      </div>

      <!-- Table Container -->
      <div class="flex-1 overflow-y-auto border border-dark-800 rounded-2xl bg-dark-950/60">
        <table class="w-full text-left text-xs border-collapse">
          <thead class="bg-dark-950 sticky top-0 border-b border-dark-800 text-slate-400 font-mono text-[11px]">
            <tr>
              <th class="py-3 px-4 font-semibold">Company</th>
              <th class="py-3 px-4 font-semibold">Categories</th>
              <th class="py-3 px-4 font-semibold">Location</th>
              <th class="py-3 px-4 font-semibold">Funding</th>
              <th class="py-3 px-4 font-semibold text-right">Action</th>
            </tr>
          </thead>
          <tbody id="preloaded-leads-tbody" class="divide-y divide-dark-800/80 text-slate-300">
            <!-- Populated by JS -->
          </tbody>
        </table>
      </div>

      <div class="flex justify-between items-center pt-2 text-xs text-slate-400">
        <span>Click "➕ Add to CRM" on any company to import into your pipeline.</span>
        <button onclick="closeModal('lead-database-modal')" class="px-4 py-2 rounded-xl bg-dark-800 hover:bg-dark-750 text-slate-300 font-semibold transition">Close</button>
      </div>
    </div>
  </div>

  <!-- MODAL 3: PROPOSAL / DECK GENERATOR -->
  <div id="proposal-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="bg-dark-900 border border-dark-700 rounded-3xl max-w-2xl w-full p-6 space-y-5 shadow-2xl max-h-[90vh] overflow-y-auto">
      <div class="flex items-center justify-between border-b border-dark-800 pb-4">
        <h3 class="text-base font-bold text-white flex items-center gap-2">
          <i data-lucide="file-text" class="w-4 h-4 text-brand-400"></i> Risk-Reversal Proposal Generator
        </h3>
        <button onclick="closeModal('proposal-modal')" class="text-slate-400 hover:text-white transition">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Target Startup Name</label>
          <input id="prop-company-name" type="text" value="Acme AI" class="w-full bg-dark-950 border border-dark-750 rounded-xl px-3 py-2 text-white focus:border-brand-500 focus:outline-none" />
        </div>
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Founder / Engineering Lead Name</label>
          <input id="prop-founder-name" type="text" value="Alex" class="w-full bg-dark-950 border border-dark-750 rounded-xl px-3 py-2 text-white focus:border-brand-500 focus:outline-none" />
        </div>
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Specific Pain Point / System Bottleneck</label>
          <input id="prop-pain-point" type="text" value="High LLM API bill and 3.5s response latency on search" class="w-full bg-dark-950 border border-dark-750 rounded-xl px-3 py-2 text-white focus:border-brand-500 focus:outline-none" />
        </div>
        <div>
          <label class="block text-slate-300 font-semibold mb-1">Your Proposed Solution</label>
          <input id="prop-solution" type="text" value="Multi-tier hybrid classifier + semantic caching layer" class="w-full bg-dark-950 border border-dark-750 rounded-xl px-3 py-2 text-white focus:border-brand-500 focus:outline-none" />
        </div>
      </div>

      <button onclick="generateProposalPreview()" class="w-full py-2.5 rounded-xl bg-brand-500 hover:bg-brand-600 text-dark-950 font-bold text-xs transition shadow-sm">
        Generate Formatted Proposal ↓
      </button>

      <div class="space-y-2">
        <div class="flex justify-between items-center text-xs">
          <span class="text-slate-400 font-semibold">Generated 1-Page Proposal:</span>
          <button onclick="copyProposalOutput()" class="text-brand-400 hover:underline flex items-center gap-1 font-mono transition">
            <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copy Proposal
          </button>
        </div>
        <textarea id="proposal-output-text" rows="8" class="w-full bg-dark-950 border border-dark-750 rounded-xl p-3 text-xs font-mono text-slate-200 leading-relaxed focus:border-brand-500 focus:outline-none"></textarea>
      </div>
    </div>
  </div>

  <!-- MODAL 4: DATA BACKUP & RESTORE -->
  <div id="backup-modal" class="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm hidden flex items-center justify-center p-4">
    <div class="bg-dark-900 border border-dark-700 rounded-3xl max-w-md w-full p-6 space-y-5 shadow-2xl">
      <div class="flex items-center justify-between border-b border-dark-800 pb-4">
        <h3 class="text-base font-bold text-white flex items-center gap-2">
          <i data-lucide="hard-drive" class="w-4 h-4 text-accent-400"></i> Backup & Data Management
        </h3>
        <button onclick="closeModal('backup-modal')" class="text-slate-400 hover:text-white transition">
          <i data-lucide="x" class="w-5 h-5"></i>
        </button>
      </div>

      <p class="text-xs text-slate-300 leading-relaxed">
        All your roadmap checkboxes, CRM leads, and custom audit scores are saved automatically to your browser's LocalStorage. You can export a JSON backup or reset anytime.
      </p>

      <div class="space-y-2.5">
        <button onclick="exportUserDataJSON()" class="w-full py-2.5 rounded-xl bg-accent-600 hover:bg-accent-500 text-white font-bold text-xs flex items-center justify-center gap-2 transition shadow-sm">
          <i data-lucide="download" class="w-4 h-4"></i> Export My Data (JSON)
        </button>

        <label class="w-full py-2.5 rounded-xl bg-dark-800 hover:bg-dark-750 border border-dark-700 text-slate-200 font-semibold text-xs flex items-center justify-center gap-2 cursor-pointer transition">
          <i data-lucide="upload" class="w-4 h-4"></i> Import Backup JSON
          <input type="file" accept=".json" onchange="importUserDataJSON(event)" class="hidden" />
        </label>

        <button onclick="resetAllData()" class="w-full py-2 rounded-xl bg-rose-950/40 hover:bg-rose-900/60 border border-rose-800/40 text-rose-300 font-semibold text-xs flex items-center justify-center gap-2 transition">
          <i data-lucide="trash-2" class="w-4 h-4"></i> Reset Everything to Default
        </button>
      </div>
    </div>
  </div>

  <!-- TOAST NOTIFICATION CONTAINER -->
  <div id="toast-container" class="fixed bottom-6 right-6 z-50 space-y-2 pointer-events-none"></div>

  <!-- EMBEDDED SINGLE-FILE SCRIPT ENGINE -->
  <script>
"""

html_tail = """
  </script>

</body>
</html>
"""

full_html = html_head + "\n" + curated_leads_content + "\n" + app_js_content + "\n" + html_tail

with open(r'D:\us-remote-engineering-playbook\index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print('Generated single self-contained index.html successfully!')
print(f'Total characters: {len(full_html)}')
