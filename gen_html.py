import base64

def b64(name):
    with open(f'images/{name}.png', 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode()

p2  = b64('p2')
p4a = b64('p4a')
p4b = b64('p4b')
p6a = b64('p6a')
p6b = b64('p6b')
p6c = b64('p6c')
p6d = b64('p6d')

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="robots" content="noindex, nofollow" />
  <title>TouchStay — Q2 2026 Product Strategy</title>
  <script>
    (function(){{
      var correct = '1608';
      var stored = sessionStorage.getItem('ts_pin');
      if (stored !== correct) {{
        var attempt = prompt('Enter PIN to access this page:');
        if (attempt !== correct) {{
          document.documentElement.innerHTML = '<div style="font-family:sans-serif;text-align:center;padding:100px;color:#64748b"><h2>Access Denied</h2><p>Incorrect PIN. Please refresh and try again.</p></div>';
          throw new Error('Access denied');
        }}
        sessionStorage.setItem('ts_pin', correct);
      }}
    }})();
  </script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --ts-navy:    #0f2b46;
      --ts-teal:    #0e7c7b;
      --ts-teal-lt: #14a8a7;
      --ts-sky:     #e8f6f6;
      --ts-amber:   #f59e0b;
      --ts-green:   #10b981;
      --ts-border:  #e2e8f0;
      --ts-bg:      #f8fafc;
      --text:       #1e293b;
      --text-muted: #64748b;
      --radius:     10px;
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: Inter, sans-serif; background: var(--ts-bg); color: var(--text); line-height: 1.65; font-size: 15px; }}

    /* NAV */
    nav {{ position: sticky; top: 0; z-index: 100; background: rgba(15,43,70,0.97); backdrop-filter: blur(8px); border-bottom: 1px solid rgba(255,255,255,0.08); }}
    .nav-inner {{ max-width: 1100px; margin: 0 auto; display: flex; align-items: center; gap: 2rem; padding: 0 1.5rem; height: 54px; }}
    .nav-logo {{ font-weight: 700; font-size: 15px; color: #fff; letter-spacing: -0.3px; white-space: nowrap; }}
    .nav-logo span {{ color: var(--ts-teal-lt); }}
    .nav-links {{ display: flex; gap: 0; list-style: none; overflow-x: auto; flex: 1; }}
    .nav-links a {{ display: block; padding: 0 0.85rem; height: 54px; line-height: 54px; color: rgba(255,255,255,0.65); text-decoration: none; font-size: 13px; font-weight: 500; white-space: nowrap; transition: color 0.15s; }}
    .nav-links a:hover {{ color: #fff; }}

    /* HERO */
    .hero {{ background: linear-gradient(135deg, var(--ts-navy) 0%, #164e63 60%, var(--ts-teal) 100%); padding: 80px 1.5rem 72px; text-align: center; color: #fff; }}
    .hero-label {{ display: inline-block; background: rgba(255,255,255,0.12); border: 1px solid rgba(255,255,255,0.2); border-radius: 100px; padding: 4px 16px; font-size: 12px; font-weight: 600; letter-spacing: 0.8px; text-transform: uppercase; margin-bottom: 22px; color: var(--ts-teal-lt); }}
    .hero h1 {{ font-size: clamp(2rem,5vw,3.2rem); font-weight: 800; letter-spacing: -1px; line-height: 1.15; max-width: 700px; margin: 0 auto 16px; }}
    .hero-sub {{ font-size: 17px; color: rgba(255,255,255,0.7); max-width: 560px; margin: 0 auto 40px; }}
    .hero-kpis {{ display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; max-width: 800px; margin: 0 auto; }}
    .hero-kpi {{ background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.18); border-radius: var(--radius); padding: 18px 28px; min-width: 160px; }}
    .hero-kpi .val {{ font-size: 1.9rem; font-weight: 800; letter-spacing: -1px; display: block; }}
    .hero-kpi .lbl {{ font-size: 12px; color: rgba(255,255,255,0.6); margin-top: 2px; display: block; }}
    .hero-kpi.accent .val {{ color: var(--ts-teal-lt); }}

    /* LAYOUT */
    .page {{ max-width: 1100px; margin: 0 auto; padding: 0 1.5rem; }}
    section {{ padding: 64px 0; }}
    section + section {{ border-top: 1px solid var(--ts-border); }}

    /* SECTION HEADER */
    .sec-eyebrow {{ font-size: 11px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; color: var(--ts-teal); margin-bottom: 8px; }}
    .sec-title {{ font-size: clamp(1.5rem,3vw,2rem); font-weight: 800; letter-spacing: -0.5px; color: var(--ts-navy); margin-bottom: 12px; }}
    .sec-desc {{ color: var(--text-muted); max-width: 680px; margin-bottom: 40px; font-size: 15.5px; }}

    /* METRIC STRIP */
    .metric-strip {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(180px,1fr)); gap: 16px; margin-bottom: 40px; }}
    .metric-card {{ background: #fff; border: 1px solid var(--ts-border); border-radius: var(--radius); padding: 20px 20px 18px; position: relative; overflow: hidden; }}
    .metric-card::before {{ content: ''; position: absolute; top: 0; left: 0; right: 0; height: 3px; background: var(--ts-teal); border-radius: var(--radius) var(--radius) 0 0; }}
    .metric-card.amber::before {{ background: var(--ts-amber); }}
    .metric-card.green::before {{ background: var(--ts-green); }}
    .metric-card.navy::before  {{ background: var(--ts-navy); }}
    .metric-label {{ font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.8px; color: var(--text-muted); margin-bottom: 6px; }}
    .metric-value {{ font-size: 1.6rem; font-weight: 800; color: var(--ts-navy); letter-spacing: -0.5px; }}
    .metric-sub {{ font-size: 12px; color: var(--text-muted); margin-top: 4px; }}
    .metric-badge {{ display: inline-block; margin-top: 6px; padding: 2px 8px; border-radius: 100px; font-size: 11px; font-weight: 600; background: #dcfce7; color: #166534; }}
    .metric-badge.warn {{ background: #fef3c7; color: #92400e; }}

    /* TABLES */
    .table-wrap {{ overflow-x: auto; border-radius: var(--radius); border: 1px solid var(--ts-border); margin-bottom: 32px; }}
    table {{ width: 100%; border-collapse: collapse; background: #fff; font-size: 13.5px; }}
    th {{ background: var(--ts-navy); color: #fff; padding: 11px 14px; text-align: left; font-weight: 600; font-size: 12px; letter-spacing: 0.3px; white-space: nowrap; }}
    td {{ padding: 10px 14px; border-bottom: 1px solid var(--ts-border); color: var(--text); }}
    tr:last-child td {{ border-bottom: none; }}
    tr:hover td {{ background: #f8fafc; }}
    .total-row td {{ font-weight: 700; background: var(--ts-sky); color: var(--ts-navy); }}
    .num {{ text-align: right; font-variant-numeric: tabular-nums; }}

    /* PILLARS GRID */
    .pillars-grid {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(240px,1fr)); gap: 20px; margin-bottom: 48px; }}
    .pillar-card {{ background: #fff; border: 1px solid var(--ts-border); border-radius: var(--radius); padding: 28px 24px; position: relative; overflow: hidden; text-decoration: none; display: block; transition: box-shadow 0.2s, transform 0.2s; }}
    .pillar-card:hover {{ box-shadow: 0 8px 24px rgba(0,0,0,0.1); transform: translateY(-2px); }}
    .pillar-num {{ position: absolute; top: 16px; right: 18px; font-size: 3rem; font-weight: 900; color: var(--ts-sky); line-height: 1; letter-spacing: -2px; user-select: none; }}
    .pillar-tag {{ display: inline-block; padding: 3px 10px; border-radius: 100px; font-size: 11px; font-weight: 600; margin-bottom: 12px; background: var(--ts-sky); color: var(--ts-teal); }}
    .pillar-card h3 {{ font-size: 1.05rem; font-weight: 700; color: var(--ts-navy); margin-bottom: 10px; line-height: 1.3; }}
    .pillar-card p {{ font-size: 13.5px; color: var(--text-muted); line-height: 1.6; }}

    /* PILLAR DETAIL */
    .pillar-section {{ background: #fff; border: 1px solid var(--ts-border); border-radius: 14px; padding: 36px 36px 32px; margin-bottom: 28px; }}
    .pillar-section-header {{ display: flex; align-items: flex-start; gap: 16px; margin-bottom: 28px; }}
    .pillar-badge {{ width: 46px; height: 46px; border-radius: 12px; background: var(--ts-teal); color: #fff; font-weight: 800; font-size: 1.1rem; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
    .pillar-badge.amber {{ background: var(--ts-amber); }}
    .pillar-badge.navy  {{ background: var(--ts-navy); }}
    .pillar-badge.green {{ background: var(--ts-green); }}
    .pillar-section-header h3 {{ font-size: 1.25rem; font-weight: 800; color: var(--ts-navy); margin-bottom: 4px; }}
    .pillar-section-header p {{ color: var(--text-muted); font-size: 14px; }}
    .two-col {{ display: grid; grid-template-columns: 1fr 1fr; gap: 28px; }}
    @media (max-width: 640px) {{ .two-col {{ grid-template-columns: 1fr; }} }}
    .sub-heading {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: var(--ts-teal); margin-bottom: 10px; }}
    ul.bullet {{ list-style: none; padding: 0; }}
    ul.bullet li {{ padding: 5px 0 5px 20px; font-size: 14px; color: var(--text); position: relative; border-bottom: 1px solid #f1f5f9; line-height: 1.5; }}
    ul.bullet li:last-child {{ border-bottom: none; }}
    ul.bullet li::before {{ content: "\\2192"; position: absolute; left: 0; color: var(--ts-teal); font-size: 12px; top: 6px; }}
    .assumption-box {{ background: #fffbeb; border: 1px solid #fde68a; border-radius: 8px; padding: 14px 16px; margin-top: 16px; }}
    .assumption-box .label {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: #92400e; margin-bottom: 6px; }}
    .assumption-box ul {{ padding-left: 16px; font-size: 13px; color: #78350f; }}
    .assumption-box ul li {{ margin-bottom: 4px; }}

    /* SCREENSHOTS */
    .screen-wrap {{ margin-top: 28px; }}
    .screen-label {{ font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; color: var(--ts-teal); margin-bottom: 10px; }}
    .screen-img {{ width: 100%; border-radius: 10px; border: 1px solid var(--ts-border); box-shadow: 0 4px 24px rgba(0,0,0,0.08); display: block; cursor: pointer; transition: transform 0.2s, box-shadow 0.2s; }}
    .screen-img:hover {{ transform: scale(1.02); box-shadow: 0 8px 32px rgba(0,0,0,0.12); }}
    .screen-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 28px; }}
    .screen-caption {{ font-size: 12px; color: var(--text-muted); margin-top: 7px; text-align: center; }}
    @media (max-width: 640px) {{ .screen-grid {{ grid-template-columns: 1fr; }} }}

    /* INVEST/PIVOT/EXIT */
    .ipx-grid {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(260px,1fr)); gap: 16px; margin-top: 20px; }}
    .ipx-card {{ border-radius: var(--radius); padding: 20px; }}
    .ipx-card.invest {{ background: #f0fdf4; border: 1px solid #bbf7d0; }}
    .ipx-card.pivot  {{ background: #fefce8; border: 1px solid #fde68a; }}
    .ipx-card h4 {{ font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.8px; margin-bottom: 10px; }}
    .ipx-card.invest h4 {{ color: #166534; }}
    .ipx-card.pivot  h4 {{ color: #92400e; }}
    .ipx-card ul {{ list-style: none; padding: 0; }}
    .ipx-card ul li {{ font-size: 13px; padding: 8px 0; border-bottom: 1px solid rgba(0,0,0,0.06); color: var(--text); }}
    .ipx-card ul li:last-child {{ border-bottom: none; }}

    /* MOONSHOT */
    .moonshot-hero {{ background: linear-gradient(135deg, var(--ts-navy) 0%, #1e3a5f 100%); border-radius: 16px; padding: 48px 44px 40px; color: #fff; margin-bottom: 40px; }}
    .moonshot-hero .eyebrow {{ font-size: 11px; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; color: var(--ts-teal-lt); margin-bottom: 10px; }}
    .moonshot-hero h3 {{ font-size: 1.8rem; font-weight: 800; letter-spacing: -0.5px; margin-bottom: 12px; }}
    .moonshot-hero p {{ color: rgba(255,255,255,0.72); font-size: 15px; max-width: 680px; }}
    .moonshot-problems {{ display: grid; grid-template-columns: repeat(auto-fit,minmax(180px,1fr)); gap: 12px; margin-top: 28px; }}
    .moonshot-problem {{ background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.14); border-radius: 8px; padding: 14px 16px; font-size: 13.5px; color: rgba(255,255,255,0.8); }}

    .simple-mode-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-bottom: 40px; }}
    @media (max-width: 700px) {{ .simple-mode-grid {{ grid-template-columns: 1fr; }} }}
    .simple-feat-header {{ display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }}
    .simple-feat-icon {{ width: 32px; height: 32px; border-radius: 8px; background: var(--ts-sky); display: flex; align-items: center; justify-content: center; font-size: 15px; flex-shrink: 0; }}
    .simple-feat h4 {{ font-size: 1rem; font-weight: 700; color: var(--ts-navy); }}
    .simple-feat p {{ font-size: 13.5px; color: var(--text-muted); margin-bottom: 14px; line-height: 1.55; }}

    .persona-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 28px; }}
    @media (max-width: 640px) {{ .persona-grid {{ grid-template-columns: 1fr; }} }}
    .persona-card {{ border-radius: 12px; overflow: hidden; border: 1px solid var(--ts-border); box-shadow: 0 2px 12px rgba(0,0,0,0.06); }}
    .persona-card-head {{ padding: 14px 18px; font-weight: 700; font-size: 13px; display: flex; align-items: center; gap: 8px; }}
    .persona-card-head.convert {{ background: #ecfdf5; color: #065f46; }}
    .persona-card-head.explore {{ background: #eff6ff; color: #1e40af; }}
    .persona-card img {{ width: 100%; display: block; border-top: 1px solid var(--ts-border); cursor: pointer; transition: opacity 0.2s; }}
    .persona-card img:hover {{ opacity: 0.9; }}

    /* ROADMAP */
    .priority-badge {{ display: inline-block; padding: 2px 8px; border-radius: 100px; font-size: 11px; font-weight: 600; }}
    .p-critic {{ background: #fee2e2; color: #991b1b; }}
    .p-high   {{ background: #fef3c7; color: #92400e; }}
    .p-mid    {{ background: #e0f2fe; color: #075985; }}
    .mrr-badge {{ display: inline-block; padding: 2px 8px; border-radius: 100px; font-size: 11px; font-weight: 600; }}
    .mrr-new    {{ background: #dcfce7; color: #166534; }}
    .mrr-upsell {{ background: #ede9fe; color: #5b21b6; }}
    .mrr-retain {{ background: #e0f2fe; color: #075985; }}
    .ice-high {{ color: var(--ts-teal); font-weight: 700; }}
    .ice-mid  {{ color: var(--text-muted); font-weight: 600; }}

    footer {{ background: var(--ts-navy); color: rgba(255,255,255,0.5); text-align: center; padding: 28px 1.5rem; font-size: 13px; }}
    footer strong {{ color: rgba(255,255,255,0.8); }}
    .gap-top {{ margin-top: 20px; }}
    @media (max-width: 700px) {{ .pillar-section {{ padding: 24px 20px; }} .moonshot-hero {{ padding: 32px 24px; }} }}

    /* MODAL */
    .modal {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9); z-index: 1000; align-items: center; justify-content: center; }}
    .modal.active {{ display: flex; }}
    .modal-content {{ position: relative; display: flex; align-items: center; justify-content: center; }}
    .modal-img {{ max-width: 95vw; max-height: 90vh; width: auto; height: auto; object-fit: contain; display: block; }}
    .modal-close {{ position: fixed; top: 20px; right: 20px; background: rgba(0,0,0,0.6); color: #fff; border: none; width: 44px; height: 44px; border-radius: 50%; font-size: 28px; cursor: pointer; display: flex; align-items: center; justify-content: center; transition: background 0.2s; z-index: 1001; }}
    .modal-close:hover {{ background: rgba(0,0,0,0.8); }}
  </style>
</head>
<body>

<nav>
  <div class="nav-inner">
    <div class="nav-logo">Touch<span>Stay</span> &mdash; Q2 2026</div>
    <ul class="nav-links">
      <li><a href="#pillars">Pillars</a></li>
      <li><a href="#pillar-1">Value First</a></li>
      <li><a href="#pillar-2">Upsell</a></li>
      <li><a href="#pillar-3">AI Onboarding</a></li>
      <li><a href="#pillar-4">Feature Maturity</a></li>
      <li><a href="#roadmap">Roadmap</a></li>
      <li><a href="#moonshot">Moonshot</a></li>
    </ul>
  </div>
</nav>

<div class="hero">
  <div class="hero-label">Q2 2026 &middot; Product Strategy &middot; V2</div>
</div>

<div class="page">

<section id="pillars">
  <div class="sec-eyebrow">Strategic Pillars</div>
  <div class="sec-title">Four Pillars to Hit the Q2 Target</div>
  <p class="sec-desc">Each pillar targets a specific lever in the growth equation &mdash; top-of-funnel conversion, ARPU expansion, trial-to-paid improvement, and feature monetisation.</p>
  <div class="pillars-grid">
    <a class="pillar-card" href="#pillar-1">
      <span class="pillar-num">1</span>
      <span class="pillar-tag">Conversion</span>
      <h3>Value First Interface</h3>
      <p>Show the guidebook <strong>before we ask for anything</strong>. Move value perception from <strong>G3 to pre-G1</strong> with an AI chatbot + live preview on the homepage.</p>
    </a>
    <a class="pillar-card" href="#pillar-2">
      <span class="pillar-num">2</span>
      <span class="pillar-tag">ARPU</span>
      <h3>Upselling to Increase ARPU</h3>
      <p>Leverage new tier pricing to drive <strong>$6.4K/month upsell MRR</strong> from new accounts and unlock <strong>$40K total legacy migration potential</strong>.</p>
    </a>
    <a class="pillar-card" href="#pillar-3">
      <span class="pillar-num">3</span>
      <span class="pillar-tag">Trial Conversion</span>
      <h3>AI Handholding for Manual GB Creation</h3>
      <p><strong>60% of G3s</strong> skip OTA links and churn. AI-guided creation closes the gap and replicates the <strong>15pp lift</strong> from auto-imported guidebooks.</p>
    </a>
    <a class="pillar-card" href="#pillar-4">
      <span class="pillar-num">4</span>
      <span class="pillar-tag">Feature Maturity</span>
      <h3>Invest / Pivot / Exit Framework</h3>
      <p>Give every active feature a clear mandate: invest and build, pivot the go-to-market, or cut. Prevents over-building and focuses resources.</p>
    </a>
  </div>
</section>

<section id="pillar-1">
  <div class="sec-eyebrow">Pillar 1 &mdash; Value First</div>
  <div class="sec-title">Value First Interface</div>
  <p class="sec-desc">Our <strong>biggest top-of-funnel lever</strong>. We currently convert <strong>46K monthly visitors at 1.63%</strong> to G1. We need <strong>2%</strong> &mdash; and we get there by showing value <em>before</em> we ask for anything.</p>
  <div class="pillar-section">
    <div class="pillar-section-header">
      <div class="pillar-badge">1</div>
      <div><h3>Why this matters now</h3><p>Value perception today sits at <strong>G3 &mdash; after signup</strong>. We need to move it to <strong>before G1</strong>.</p></div>
    </div>
    <div class="two-col">
      <div>
        <div class="sub-heading">Goals</div>
        <ul class="bullet">
          <li>Reduce time-to-value perception &mdash; show results before signup</li>
          <li>Move value perception from G3 to before G1</li>
          <li>Increase G1 conversion rate from <strong>1.63% to &gt;2%</strong></li>
        </ul>
        <div class="sub-heading gap-top">How</div>
        <ul class="bullet">
          <li>Live guidebook preview on homepage and key landing pages</li>
          <li>AI Onboarding Assistant chatbot replaces the current data-collection sign-up form</li>
          <li>Chatbot drives conversation from a value-first perspective &mdash; then collects email and creates account naturally</li>
          <li>More natural data collection as a by-product of the conversation</li>
        </ul>
      </div>
      <div>
        <div class="assumption-box" style="margin-top:0">
          <div class="label">Assumptions to Test</div>
          <ul>
            <li>Faster value perception = higher G1 conversion</li>
            <li>Our audience is AI-friendly enough for a chatbot sign-up</li>
            <li>If not: keep the preview, replace chat with traditional sign-up form (but lose behavioural insights)</li>
          </ul>
        </div>
        <div class="screen-wrap">
          <div class="screen-label">Homepage &mdash; AI chatbot + live guidebook preview</div>
          <img class="screen-img" src="{p2}" alt="Homepage AI chatbot sign-up with live guidebook preview side by side" onclick="openModal(this)" />
        </div>
      </div>
    </div>
  </div>
</section>

<section id="pillar-2">
  <div class="sec-eyebrow">Pillar 2 &mdash; Upsell</div>
  <div class="sec-title">Upselling to Increase ARPU</div>
  <p class="sec-desc">New tier pricing delivers a projected blended ARPU of <strong>$31.84 (+26% vs current $25.16)</strong>, opening <strong>$6.4K/month in upsell MRR</strong> from new accounts &mdash; plus <strong>$40K total legacy migration potential</strong>.</p>
  <div class="pillar-section">
    <div class="pillar-section-header">
      <div class="pillar-badge amber">2</div>
      <div><h3>Tier Pricing Analysis</h3><p>Tiered pricing offers a natural blended ARPU increase if we can ensure adequate upsell pressure.</p></div>
    </div>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Tier</th><th>New Monthly Rate</th><th>New Annual (Eff. Mo)</th><th>Proj. Blended ARPU</th><th>Legacy Blended ARPU</th></tr></thead>
        <tbody>
          <tr><td>1 &mdash; Starter</td><td>$12.50</td><td>$8.25</td><td>$11.43</td><td>$11.43</td></tr>
          <tr><td>2 &mdash; Growth</td><td>$15.00</td><td>$11.58</td><td>$40.61</td><td>$33.84</td></tr>
          <tr><td>3 &mdash; Pro</td><td>$18.00</td><td>$13.25</td><td>$203.52</td><td>$141.33</td></tr>
          <tr><td>4 &mdash; Enterprise</td><td>$20.00</td><td>$14.92</td><td>$767.31</td><td>$479.57</td></tr>
          <tr class="total-row"><td colspan="2">Blended ARPU Improvement</td><td colspan="3"><strong>$31.84 (+26%)</strong> vs $25.16 on legacy pricing</td></tr>
        </tbody>
      </table>
    </div>
    <div class="two-col">
      <div>
        <div class="sub-heading">Tactic 1 &mdash; Tier Upgrades from New Accounts</div>
        <ul class="bullet">
          <li>Gate new features to Growth &amp; Pro plans only: Task Manager, Campaign Manager, SubDomains, Friendly URL</li>
          <li>Creates a clear reason to upgrade at signup &mdash; drives <strong>$6.4K/month upsell MRR</strong></li>
        </ul>
        <div class="sub-heading gap-top">Tactic 2 &mdash; Legacy &rarr; Growth Migration</div>
        <ul class="bullet">
          <li><strong>2,000 current Legacy clients</strong> pay $0&ndash;3/property to upgrade to Growth tier pricing</li>
          <li><strong>$40K total upsell MRR potential</strong> across the base</li>
          <li>Pair with opt-in migration incentives and <a href="https://store-activation-to-growth.vercel.app/" target="_blank" style="color:inherit;">Store ROI Calculator</a> to de-risk the ask</li>
        </ul>
      </div>
      <div>
        <div class="sub-heading">Tactic 3 &mdash; Store as Conversion Hook</div>
        <ul class="bullet">
          <li>Currently giving Store for free &mdash; move to Growth/Pro only to create upgrade incentive</li>
          <li><a href="https://store-activation-to-growth.vercel.app/" target="_blank" style="color:inherit;">Store ROI Calculator</a> positions Store as a business case, not just a feature</li>
          <li><strong>2% commission model</strong>: $300K transacted value/month = <strong>$6K MRR</strong></li>
        </ul>
        <div class="sub-heading gap-top">Tactic 4 &mdash; Upsell Signals to Pipedrive</div>
        <ul class="bullet">
          <li><strong>15-day feature trials</strong> on Growth/Pro features for Legacy &amp; Starter accounts</li>
          <li>Trial expires &rarr; upgrade screen presented automatically</li>
          <li>Trial start &amp; end signals sent to Pipedrive to alert sales</li>
        </ul>
      </div>
    </div>
    <div class="assumption-box">
      <div class="label">Assumptions to Test</div>
      <ul>
        <li>Tiered pricing is compelling enough to convert new users directly into Growth/Pro plans</li>
        <li>Per-property upgrade cost is palatable &mdash; even at <strong>+70% max increase</strong> &mdash; when paired with the Store ROI Calculator</li>
      </ul>
    </div>
  </div>
</section>

<section id="pillar-3">
  <div class="sec-eyebrow">Pillar 3 &mdash; AI Onboarding</div>
  <div class="sec-title">AI Handholding for Manual Guidebook Creation</div>
  <p class="sec-desc"><strong>60% of G3s</strong> skip OTA links &mdash; their guidebooks are never ready to share, so they churn during trial. AI-guided creation aims to replicate the <strong>15pp conversion lift</strong> we see with auto-imported guidebooks.</p>
  <div class="pillar-section">
    <div class="pillar-section-header">
      <div class="pillar-badge green">3</div>
      <div><h3>Why this matters now</h3><p>Target <strong>G4/G3 &gt;40%</strong> (cohorted by org start date) to achieve MRR target. Current manual path <strong>leaves users stranded</strong> before share-ready state.</p></div>
    </div>
    <div class="two-col">
      <div>
        <div class="sub-heading">Goals</div>
        <ul class="bullet">
          <li>Close the gap for the <strong>60% of G3s</strong> who don&apos;t have an OTA link</li>
          <li>Get manual-path users to <strong>&ldquo;share ready&rdquo; state</strong> before they churn</li>
          <li>Target G4/G3 conversion rate <strong>&gt;40%</strong></li>
        </ul>
        <div class="sub-heading gap-top">How</div>
        <ul class="bullet">
          <li>After AI-assisted sign-up, detect no-OTA-link path and launch AI-guided manual creation flow</li>
          <li>AI Assistant guides the user section by section until the guidebook is share-ready</li>
          <li>Replicates the <strong>15pp conversion lift</strong> seen with auto-imported guidebooks</li>
        </ul>
        <div class="assumption-box">
          <div class="label">Assumptions to Test</div>
          <ul>
            <li>Our audience is AI-friendly enough for a guided chat creation experience</li>
            <li>If not: replace chat with a quick-action checklist (but lose behavioural insights)</li>
          </ul>
        </div>
      </div>
      <div>
        <div class="screen-grid" style="margin-top:0">
          <div>
            <img class="screen-img" src="{p4a}" alt="AI chatbot collecting AirBnB link to auto-fill guidebook" onclick="openModal(this)" />
            <div class="screen-caption">AI-assisted onboarding: chatbot collects OTA link and auto-builds the guidebook</div>
          </div>
          <div>
            <img class="screen-img" src="{p4b}" alt="AI-guided manual guidebook creation" onclick="openModal(this)" />
            <div class="screen-caption">Manual path: AI guides user section by section to share-ready state</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="pillar-4">
  <div class="sec-eyebrow">Pillar 4 &mdash; Feature Maturity</div>
  <div class="sec-title">Invest / Pivot / Exit Framework</div>
  <p class="sec-desc">Drive upsell MRR through complementary value to the guidebook. Every active feature gets a <strong>clear mandate: build it out, pivot the go-to-market, or cut it entirely</strong>.</p>
  <div class="pillar-section">
    <div class="pillar-section-header">
      <div class="pillar-badge navy">4</div>
      <div><h3>Feature decision framework</h3><p>Clear investment signals prevent over-building and ensure resources go to the highest-impact work.</p></div>
    </div>
    <div class="ipx-grid">
      <div class="ipx-card invest">
        <h4>Invest &mdash; Active Build</h4>
        <ul>
          <li><strong>Message Hub &ndash; Guest Chatbot</strong><br><span style="color:#64748b;font-size:12px">Core capability; baseline expectation from property owners. High effort, build phase.</span></li>
          <li><strong>Task Manager</strong><br><span style="color:#64748b;font-size:12px">New feature with potential to drive Growth/Pro upsell through collaborative multi-user workflows.</span></li>
          <li><strong>Store</strong><br><span style="color:#64748b;font-size:12px">Minor additions + PMS integrations to fully cover transactional needs.</span></li>
        </ul>
      </div>
      <div class="ipx-card pivot">
        <h4>Pivot &mdash; Polish &amp; Market</h4>
        <ul>
          <li><strong>CRM</strong><br><span style="color:#64748b;font-size:12px">Low adoption but also under-promoted. No new features &mdash; polish the UX and focus marketing effort to prove value. Let adoption data decide the next step.</span></li>
        </ul>
      </div>
    </div>
    <div class="assumption-box">
      <div class="label">Assumptions to Test</div>
      <ul>
        <li>Guest Chatbot is a <strong>core value offering</strong> and a baseline expectation from property owners</li>
        <li>Task Manager drives <strong>Growth/Pro upsells</strong> and achieves meaningful feature adoption</li>
        <li>Store delivers a <strong>clear ROI</strong> for property owners and justifies the upgrade ask</li>
        <li>CRM in its current form is a good value offering that just needs <strong>better positioning</strong></li>
      </ul>
    </div>
  </div>
</section>

<section id="roadmap">
  <div class="sec-eyebrow">Q2 2026 Roadmap</div>
  <div class="sec-title">Prioritised Feature Backlog</div>
  <p class="sec-desc">14 items ranked by execution order, with ICE scores, MRR category, expected impact, and status alignment. <strong>Critical items directly drive the Q2 MRR target.</strong> &mdash; <a href="https://docs.google.com/spreadsheets/d/15smucuCcHUA8aZTHT48MRB-y99SEhxDwrtPfVDTcoTI/edit?gid=0#gid=0" target="_blank" style="color:inherit;">View full backlog &rarr;</a></p>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>#</th>
          <th>Category</th>
          <th>Feature</th>
          <th>Description</th>
          <th class="num">ICE</th>
          <th>MRR Category</th>
          <th>Impact</th>
          <th>Alignment</th>
          <th>GTM Confidence</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1</td>
          <td>Upsell</td>
          <td>Legacy &rarr; Tier Upgrade Behavior</td>
          <td>Replicate feature upgrade states Starter &rarr; Growth to Legacy &rarr; Tiered. 15-day trials, upgrade screen, intent signals to Pipedrive. Trial Pro plan should have all features active.</td>
          <td class="num ice-high">240</td>
          <td><span class="mrr-badge mrr-upsell">Upsell MRR</span></td>
          <td>Very High</td>
          <td><span class="priority-badge p-critic">Critic</span></td>
          <td>High</td>
        </tr>
        <tr>
          <td>2</td>
          <td>Upsell</td>
          <td><a href="https://store-activation-to-growth.vercel.app/" target="_blank" style="color:inherit;">Store ROI Calculator</a> Upgrade</td>
          <td><a href="https://store-activation-to-growth.vercel.app/" target="_blank" style="color:inherit;">ROI calculator</a> and upgrade form from Legacy to Tiers page</td>
          <td class="num ice-high">200</td>
          <td><span class="mrr-badge mrr-upsell">Upsell MRR</span></td>
          <td>Very High</td>
          <td><span class="priority-badge p-critic">Critic</span></td>
          <td>Very High</td>
        </tr>
        <tr>
          <td>3</td>
          <td>Other</td>
          <td>1 USD/GBP/EUR/AUD/CAD Campaign</td>
          <td>$1 / 3-month campaign ability via Stripe subscription API</td>
          <td class="num ice-high">73.1</td>
          <td><span class="mrr-badge mrr-new">New MRR</span></td>
          <td>High</td>
          <td><span class="priority-badge p-critic">Critic</span></td>
          <td>Very High</td>
        </tr>
        <tr>
          <td>4</td>
          <td>Value First</td>
          <td>HomePage &mdash; AI Sign-up &amp; Preview</td>
          <td>Side-by-side chatbot + live guidebook preview. Mimics sign-up flow through chatbot. Phase 1.1: place on Homepage and other key pages. Primary G1 driver.</td>
          <td class="num ice-high">100</td>
          <td><span class="mrr-badge mrr-new">New MRR</span></td>
          <td>Very High</td>
          <td><span class="priority-badge p-critic">Critic</span></td>
          <td>High</td>
        </tr>
        <tr>
          <td>5</td>
          <td>Store</td>
          <td>Store Tips</td>
          <td>Add Tips as a template product to give property owners ideas for their store.</td>
          <td class="num ice-mid">72</td>
          <td><span class="mrr-badge mrr-new">New MRR</span></td>
          <td>Low</td>
          <td><span class="priority-badge p-mid">Mid</span></td>
          <td>High</td>
        </tr>
        <tr>
          <td>6</td>
          <td>Upsell</td>
          <td>Cancel / Downgrade Reasons</td>
          <td>Centralise voice-of-customer data on plan &amp; quantity changes. Integrate to Pipedrive.</td>
          <td class="num ice-mid">81</td>
          <td><span class="mrr-badge mrr-retain">Retention MRR</span></td>
          <td>Mid</td>
          <td><span class="priority-badge p-high">High</span></td>
          <td>Mid</td>
        </tr>
        <tr>
          <td>7</td>
          <td>Other</td>
          <td>Technical Maintenance</td>
          <td>Foundation &amp; infrastructure work</td>
          <td class="num ice-high">1000</td>
          <td>&mdash;</td>
          <td>&mdash;</td>
          <td>&mdash;</td>
          <td>&mdash;</td>
        </tr>
        <tr>
          <td>8</td>
          <td>Message Hub</td>
          <td>2WM &mdash; 10DLC &amp; Brand Registration</td>
          <td>Opt-out SMS compliance for +1 numbers before any SMS is sent. Store opt-out flag on contact and invitation. Invitation messages get &ldquo;Opt out&rdquo; status.</td>
          <td class="num ice-mid">61.7</td>
          <td><span class="mrr-badge mrr-upsell">Upsell MRR</span></td>
          <td>Mid</td>
          <td><span class="priority-badge p-critic">Critic</span></td>
          <td>Very High</td>
        </tr>
        <tr>
          <td>9</td>
          <td>Message Hub</td>
          <td>Chatbot Escalation &amp; Parties Notification</td>
          <td>Detect guest frustration or human-intervention requests via SMS. Notify host, update contact info if missing.</td>
          <td class="num ice-mid">86.4</td>
          <td><span class="mrr-badge mrr-upsell">Upsell MRR</span></td>
          <td>Mid</td>
          <td><span class="priority-badge p-critic">Critic</span></td>
          <td>High</td>
        </tr>
        <tr>
          <td>10</td>
          <td>Value First</td>
          <td>Manual GB Creation &mdash; AI Assisted</td>
          <td>AI-guided creation for non-OTA-link users. From demo content to share-ready state through conversational flow.</td>
          <td class="num ice-mid">20.6</td>
          <td><span class="mrr-badge mrr-new">New MRR</span></td>
          <td>High</td>
          <td><span class="priority-badge p-high">High</span></td>
          <td>Mid</td>
        </tr>
        <tr>
          <td>11</td>
          <td>Message Hub</td>
          <td>Message Hub &mdash; Train Chatbot</td>
          <td>Chatbot training via structured Q&amp;A list &amp; document upload. Label by guidebook, org, or account level.</td>
          <td class="num ice-mid">36</td>
          <td><span class="mrr-badge mrr-retain">Retention MRR</span></td>
          <td>Mid</td>
          <td><span class="priority-badge p-critic">Critic</span></td>
          <td>Very High</td>
        </tr>
        <tr>
          <td>12</td>
          <td>Other</td>
          <td>Task Manager &mdash; Collaborative Work</td>
          <td>Improve Task Manager with collaborative workflows to drive multi-seat needs and Growth &rarr; Pro upgrades.</td>
          <td class="num ice-mid">30.4</td>
          <td><span class="mrr-badge mrr-upsell">Upsell MRR</span></td>
          <td>Mid</td>
          <td><span class="priority-badge p-high">High</span></td>
          <td>Very High</td>
        </tr>
        <tr>
          <td>13</td>
          <td>Message Hub</td>
          <td>CRM Polishing</td>
          <td>Download, filter/sorting, contact deletion, invitation-to-contact interaction, create task from CRM.</td>
          <td class="num ice-mid">30.4</td>
          <td><span class="mrr-badge mrr-upsell">Upsell MRR</span></td>
          <td>Mid</td>
          <td><span class="priority-badge p-high">High</span></td>
          <td>Low</td>
        </tr>
        <tr>
          <td>14</td>
          <td>Upsell</td>
          <td>Split Campaign Manager &mdash; Store &amp; Message Hub</td>
          <td>Split Campaign Manager between Starter and Growth. Store Campaigns &rarr; Store section. Campaigns &rarr; Message Hub.</td>
          <td class="num ice-mid">21.6</td>
          <td><span class="mrr-badge mrr-upsell">Upsell MRR</span></td>
          <td>Low</td>
          <td><span class="priority-badge p-high">High</span></td>
          <td>Very High</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>

<section id="moonshot">
  <div class="sec-eyebrow">Moonshot Vision</div>
  <div class="sec-title">The Simple Mode</div>
  <div class="moonshot-hero">
    <div class="eyebrow">What this solves for TouchStay</div>
    <h3>One interface to rule them all</h3>
    <p>A <strong>value-first design</strong> that always shows the result of your action. Clean, persona-driven, and built on an <strong>AI chatbot &mdash; not yet an agent</strong> &mdash; that guides without acting autonomously.</p>
    <div class="moonshot-problems">
      <div class="moonshot-problem">Top-funnel size (G1s) &mdash; currently challenged</div>
      <div class="moonshot-problem">Conversion to paid (G4/G3) &mdash; downward trend</div>
      <div class="moonshot-problem">Few upsell surfaces &mdash; interface too crowded</div>
      <div class="moonshot-problem">Low discoverability of new features</div>
    </div>
  </div>

  <div class="simple-mode-grid">
    <div class="simple-feat">
      <div class="simple-feat-header">
        <div class="simple-feat-icon">&#10024;</div>
        <h4>Value First Design</h4>
      </div>
      <p>Always showing you the result of your action &mdash; not the action itself. The interface leads with outcomes, not inputs.</p>
      <img class="screen-img" src="{p6a}" alt="Value first design: AI chatbot with AirBnB link + live guidebook preview" onclick="openModal(this)" />
    </div>
    <div class="simple-feat">
      <div class="simple-feat-header">
        <div class="simple-feat-icon">&#129302;</div>
        <h4>AI Chatbot, Not Yet an Agent</h4>
      </div>
      <p>Helps, guides, and provides interfaces &mdash; but doesn&apos;t take action on your behalf yet. One chat pane, one live preview. Nothing competing for attention.</p>
      <img class="screen-img" src="{p6b}" alt="Clean interface: chat pane left, guidebook editor/preview right" onclick="openModal(this)" />
    </div>
  </div>

  <div class="persona-grid">
    <div class="persona-card">
      <div class="persona-card-head convert">&#9989; &nbsp; Convert &mdash; Drive Feature Usage</div>
      <img src="{p6c}" alt="Convert persona: Anna guides guidebook creation and content management" onclick="openModal(this)" />
    </div>
    <div class="persona-card">
      <div class="persona-card-head explore">&#128269; &nbsp; Explore &mdash; Discover Features &amp; Tiers</div>
      <img src="{p6d}" alt="Explore persona: Alex drives guest onboarding and messaging automation" onclick="openModal(this)" />
    </div>
  </div>
</section>

</div>

<footer>
  <strong>TouchStay Q2 2026 Product Strategy</strong> &mdash; Confidential &middot; For Executive Review &middot; V2
</footer>

<!-- MODAL -->
<div id="imageModal" class="modal">
  <div class="modal-content">
    <button class="modal-close" onclick="closeModal()">&times;</button>
    <img id="modalImage" class="modal-img" src="" alt="" />
  </div>
</div>

<script>
function openModal(img) {{
  const modal = document.getElementById('imageModal');
  const modalImg = document.getElementById('modalImage');
  modalImg.src = img.src;
  modalImg.alt = img.alt;
  modal.classList.add('active');
}}

function closeModal() {{
  const modal = document.getElementById('imageModal');
  modal.classList.remove('active');
}}

document.getElementById('imageModal').addEventListener('click', function(e) {{
  if (e.target === this) closeModal();
}});

document.addEventListener('keydown', function(e) {{
  if (e.key === 'Escape') closeModal();
}});
</script>

</body>
</html>"""

out = 'D:/TouchStay/Claude Projects/index.html'
with open(out, 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Done. Size: {len(html)//1024} KB')
