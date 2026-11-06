#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Crossxyreggy Enterprise - single-file website.

Everything (pages, CSS, JavaScript) lives in this one file. Running it starts a
local web server, so the whole site works without any other files.

HOW TO RUN
----------
1. Make sure Python 3.7+ is installed  (check with:  python --version)
2. Open a terminal in the folder that contains this file
3. Run:      python crossxyreggy_site.py
4. Your browser opens at  http://localhost:8000
5. Press Ctrl + C in the terminal to stop the server

Optional: choose a different port, e.g.  python crossxyreggy_site.py 9000

ONLINE (FREE CLOUD) HOSTING
---------------------------
This same file also runs on a free cloud host such as Render, so the whole
world can open the website:
  1. Put this file (and an empty requirements.txt) in a folder / GitHub repo.
  2. Create a "Web Service" on https://render.com and point it at that repo.
  3. Build command :  pip install -r requirements.txt
     Start command :  python crossxyreggy_site.py
  4. Render gives you a public https://...onrender.com address.
The cloud host tells the app which port to use through the PORT environment
variable, which the code below reads automatically.
"""

import os
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

DEFAULT_PORT = 8000


# ==========================================================================
#  index.html
# ==========================================================================
INDEX_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Crossxyreggy Enterprise | Graphics, Branding, Printing &amp; Signage</title>
  <meta name="description" content="Crossxyreggy Enterprise delivers professional graphic design, branding, printing, signage installation and marketing solutions for businesses." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

  <!-- ===== Header ===== -->
  <header class="site-header">
    <div class="container nav">
      <a href="index.html" class="brand">
        <span class="brand-mark">C</span>
        <span>Crossxyreggy<small>Enterprise</small></span>
      </a>

      <nav class="nav-links" id="navLinks">
        <a href="index.html" class="active">Home</a>
        <a href="about.html">About</a>
        <a href="services.html">Services</a>
        <a href="portfolio.html">Our Work</a>
        <a href="contact.html">Contact</a>
        <a href="contact.html" class="btn btn--primary nav-cta">Get a Quote</a>
      </nav>

      <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- ===== Hero ===== -->
  <section class="hero">
    <div class="container">
      <span class="eyebrow" style="color:#7fb2ea">Graphics &middot; Branding &middot; Printing &middot; Signage</span>
      <h1>We bring your brand to life — from concept to printed reality.</h1>
      <p>Crossxyreggy Enterprise is a full-service design and print house helping businesses stand out with striking graphics, cohesive branding, quality printing, professional signage and effective marketing.</p>

      <div class="hero-actions">
        <a href="services.html" class="btn btn--primary">Explore Our Services</a>
        <a href="contact.html" class="btn btn--ghost">Request a Quote</a>
      </div>

      <div class="hero-stats">
        <div class="stat"><strong>500+</strong><span>Projects Delivered</span></div>
        <div class="stat"><strong>5</strong><span>Core Services</span></div>
        <div class="stat"><strong>100%</strong><span>Client Focused</span></div>
      </div>
    </div>
  </section>

  <!-- ===== Services overview ===== -->
  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">What We Do</span>
        <h2>Complete creative and print solutions under one roof</h2>
        <p>Everything your business needs to look professional — designed, produced and installed by one trusted partner.</p>
      </div>

      <div class="grid grid--3">
        <article class="card reveal">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 19l7-7 3 3-7 7-3-3z"/><path d="M18 13l-1.5-7.5L2 2l3.5 14.5L13 18l5-5z"/><path d="M2 2l7.586 7.586"/><circle cx="11" cy="11" r="2"/></svg>
          </div>
          <h3>Graphic Design</h3>
          <p>Logos, brochures, flyers, packaging and digital artwork crafted to communicate your message clearly and beautifully.</p>
          <a href="services.html" class="service-link">Learn more &rarr;</a>
        </article>

        <article class="card reveal">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="13.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="14.5" r="2.5"/><circle cx="8.5" cy="7.5" r="2.5"/><circle cx="6.5" cy="15.5" r="2.5"/><path d="M12 22a10 10 0 1 1 0-20"/></svg>
          </div>
          <h3>Branding</h3>
          <p>Brand identity systems, style guides, colour palettes and corporate stationery that make your business instantly recognisable.</p>
          <a href="services.html" class="service-link">Learn more &rarr;</a>
        </article>

        <article class="card reveal">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 6 2 18 2 18 9"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/></svg>
          </div>
          <h3>Printing Services</h3>
          <p>Business cards, banners, posters, large-format and bulk commercial printing — sharp, durable and delivered on time.</p>
          <a href="services.html" class="service-link">Learn more &rarr;</a>
        </article>

        <article class="card reveal">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="12" rx="2"/><path d="M12 16v4"/><path d="M8 20h8"/><path d="M7 9h4"/></svg>
          </div>
          <h3>Signage Installation</h3>
          <p>Shopfront signs, 3D lettering, vehicle branding, billboards and illuminated signage — professionally installed.</p>
          <a href="services.html" class="service-link">Learn more &rarr;</a>
        </article>

        <article class="card reveal">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/></svg>
          </div>
          <h3>Marketing</h3>
          <p>Campaigns, social media graphics, promotional material and brand collateral that grow visibility and drive sales.</p>
          <a href="services.html" class="service-link">Learn more &rarr;</a>
        </article>

        <article class="card reveal">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="9" y1="15" x2="15" y2="15"/></svg>
          </div>
          <h3>Design Consultation</h3>
          <p>Not sure where to start? We help you plan and shape the right visual direction for your project from day one.</p>
          <a href="contact.html" class="service-link">Talk to us &rarr;</a>
        </article>
      </div>
    </div>
  </section>

  <!-- ===== Why us ===== -->
  <section class="section section--soft">
    <div class="container split">
      <div class="reveal">
        <span class="eyebrow">Why Crossxyreggy</span>
        <h2>A creative partner that delivers quality, every time</h2>
        <p>From the first sketch to final installation, we focus on doing things properly. That means clean design, quality materials and work you can be proud to put your name on.</p>
        <ul class="check-list">
          <li>One team handling design, print and installation</li>
          <li>Fast turnaround without cutting corners</li>
          <li>Quality materials and professional finishing</li>
          <li>Clear communication and honest pricing</li>
        </ul>
        <a href="about.html" class="btn btn--outline" style="margin-top:24px">More About Us</a>
      </div>
      <div class="reveal">
        <img src="https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=graphic%20designer%20reviewing%20colour%20brand%20guidelines%20and%20printed%20mockups%20on%20a%20desk%20professional%20studio%20bright%20modern%20corporate&image_size=landscape_4_3" alt="Designer reviewing brand guidelines and printed samples" loading="lazy" />
      </div>
    </div>
  </section>

  <!-- ===== Process ===== -->
  <section class="section">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">How We Work</span>
        <h2>A simple, transparent process</h2>
      </div>
      <div class="grid grid--4">
        <div class="value reveal">
          <div class="value-num">01</div>
          <h3>Consult</h3>
          <p>We listen to your goals and understand your brand and audience.</p>
        </div>
        <div class="value reveal">
          <div class="value-num">02</div>
          <h3>Design</h3>
          <p>We create concepts and refine them until they are exactly right.</p>
        </div>
        <div class="value reveal">
          <div class="value-num">03</div>
          <h3>Produce</h3>
          <p>We print, build and prepare everything to a professional finish.</p>
        </div>
        <div class="value reveal">
          <div class="value-num">04</div>
          <h3>Deliver</h3>
          <p>We install, hand over and support you after the project is done.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- ===== CTA ===== -->
  <section class="section section--soft">
    <div class="container">
      <div class="cta-band reveal">
        <div>
          <h2>Ready to elevate your brand?</h2>
          <p>Tell us about your project and we'll put together a tailored quote — no obligation.</p>
        </div>
        <a href="contact.html" class="btn btn--primary">Get a Free Quote</a>
      </div>
    </div>
  </section>

  <!-- ===== Footer ===== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <a href="index.html" class="brand">
            <span class="brand-mark">C</span>
            <span>Crossxyreggy<small>Enterprise</small></span>
          </a>
          <p>Full-service graphics, branding, printing, signage and marketing solutions for businesses that want to stand out.</p>
          <div class="social-links">
            <a href="https://www.facebook.com/profile.php?id=61578953435664" target="_blank" rel="noopener" aria-label="Facebook">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="portfolio.html">Our Work</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="services.html">Graphic Design</a></li>
            <li><a href="services.html">Branding</a></li>
            <li><a href="services.html">Printing</a></li>
            <li><a href="services.html">Signage</a></li>
            <li><a href="services.html">Marketing</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Get in Touch</h4>
          <ul>
            <li><a href="tel:+263715029199">+263 71 502 9199</a></li>
            <li><a href="tel:+263777297024">+263 77 729 7024</a></li>
            <li><a href="tel:+263774327362">+263 77 432 7362</a></li>
            <li><a href="mailto:info.crossxyreggyentstreammedia@gmail.com">info.crossxyreggyentstreammedia@gmail.com</a></li>
            <li><a href="contact.html">Request a Quote</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; <span id="year">2026</span> Crossxyreggy Enterprise. All rights reserved.</p>
        <p>Graphics &middot; Branding &middot; Printing &middot; Signage &middot; Marketing &middot; <a href="admin.html">Site Admin</a></p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
"""


# ==========================================================================
#  about.html
# ==========================================================================
ABOUT_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>About Us | Crossxyreggy Enterprise</title>
  <meta name="description" content="Learn about Crossxyreggy Enterprise — a full-service graphics, branding, printing, signage and marketing company." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

  <!-- ===== Header ===== -->
  <header class="site-header">
    <div class="container nav">
      <a href="index.html" class="brand">
        <span class="brand-mark">C</span>
        <span>Crossxyreggy<small>Enterprise</small></span>
      </a>

      <nav class="nav-links" id="navLinks">
        <a href="index.html">Home</a>
        <a href="about.html" class="active">About</a>
        <a href="services.html">Services</a>
        <a href="portfolio.html">Our Work</a>
        <a href="contact.html">Contact</a>
        <a href="contact.html" class="btn btn--primary nav-cta">Get a Quote</a>
      </nav>

      <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- ===== Page banner ===== -->
  <section class="page-banner">
    <div class="container">
      <h1>About Crossxyreggy Enterprise</h1>
      <p>A creative and production studio built on quality craftsmanship and dependable service.</p>
      <div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; About</div>
    </div>
  </section>

  <!-- ===== Intro split ===== -->
  <section class="section">
    <div class="container split">
      <div class="reveal">
        <span class="eyebrow">Who We Are</span>
        <h2>Design with purpose. Production with precision.</h2>
        <p>Crossxyreggy Enterprise is a full-service creative company specialising in graphic design, branding, printing, signage installation and marketing. We work with businesses of all sizes to build and express their identity across every medium — digital, print and physical.</p>
        <p style="margin-top:16px">Our approach is simple: understand the client, design something that works, and produce it to a standard we're proud of. Whether it's a single business card or a complete brand rollout with signage, we treat every project with the same care.</p>
      </div>
      <div class="reveal">
        <img src="https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=modern%20creative%20agency%20team%20meeting%20around%20a%20table%20with%20brand%20design%20boards%20and%20print%20samples%20bright%20professional%20office&image_size=landscape_4_3" alt="Creative team collaborating on a brand project" loading="lazy" />
      </div>
    </div>
  </section>

  <!-- ===== Mission / Vision / Values ===== -->
  <section class="section section--soft">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">What Drives Us</span>
        <h2>Our mission, vision and values</h2>
      </div>

      <div class="grid grid--3">
        <article class="card reveal">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>
          </div>
          <h3>Our Mission</h3>
          <p>To help businesses communicate clearly and look professional through thoughtful design and reliable production.</p>
        </article>

        <article class="card reveal">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
          </div>
          <h3>Our Vision</h3>
          <p>To be the go-to creative and signage partner for businesses that value quality, consistency and service.</p>
        </article>

        <article class="card reveal">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 1 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
          </div>
          <h3>Our Values</h3>
          <p>Quality, honesty, creativity and dependability. We do what we say, and we do it well.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- ===== Why choose us ===== -->
  <section class="section">
    <div class="container split">
      <div class="reveal">
        <img src="https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=large%20format%20printing%20machine%20producing%20colourful%20banners%20in%20a%20clean%20professional%20print%20workshop&image_size=landscape_4_3" alt="Large format printing in the workshop" loading="lazy" />
      </div>
      <div class="reveal">
        <span class="eyebrow">Why Choose Us</span>
        <h2>Everything under one roof</h2>
        <p>Working with a single partner for design, printing and signage saves time, keeps your brand consistent and removes the friction of coordinating multiple suppliers.</p>
        <ul class="check-list">
          <li>Skilled in-house designers and installers</li>
          <li>Consistent brand application across every medium</li>
          <li>Scalable for single jobs or full rollouts</li>
          <li>Reliable turnaround and clear communication</li>
        </ul>
        <a href="services.html" class="btn btn--primary" style="margin-top:24px">See Our Services</a>
      </div>
    </div>
  </section>

  <!-- ===== CTA ===== -->
  <section class="section section--soft">
    <div class="container">
      <div class="cta-band reveal">
        <div>
          <h2>Let's build something great together</h2>
          <p>Whether it's a fresh brand or a single print run, we'd love to hear about your project.</p>
        </div>
        <a href="contact.html" class="btn btn--primary">Contact Us</a>
      </div>
    </div>
  </section>

  <!-- ===== Footer ===== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <a href="index.html" class="brand">
            <span class="brand-mark">C</span>
            <span>Crossxyreggy<small>Enterprise</small></span>
          </a>
          <p>Full-service graphics, branding, printing, signage and marketing solutions for businesses that want to stand out.</p>
          <div class="social-links">
            <a href="https://www.facebook.com/profile.php?id=61578953435664" target="_blank" rel="noopener" aria-label="Facebook">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="portfolio.html">Our Work</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="services.html">Graphic Design</a></li>
            <li><a href="services.html">Branding</a></li>
            <li><a href="services.html">Printing</a></li>
            <li><a href="services.html">Signage</a></li>
            <li><a href="services.html">Marketing</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Get in Touch</h4>
          <ul>
            <li><a href="tel:+263715029199">+263 71 502 9199</a></li>
            <li><a href="tel:+263777297024">+263 77 729 7024</a></li>
            <li><a href="tel:+263774327362">+263 77 432 7362</a></li>
            <li><a href="mailto:info.crossxyreggyentstreammedia@gmail.com">info.crossxyreggyentstreammedia@gmail.com</a></li>
            <li><a href="contact.html">Request a Quote</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; <span id="year">2026</span> Crossxyreggy Enterprise. All rights reserved.</p>
        <p>Graphics &middot; Branding &middot; Printing &middot; Signage &middot; Marketing &middot; <a href="admin.html">Site Admin</a></p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
"""


# ==========================================================================
#  services.html
# ==========================================================================
SERVICES_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Services | Crossxyreggy Enterprise</title>
  <meta name="description" content="Graphic design, branding, printing, signage installation and marketing services from Crossxyreggy Enterprise." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

  <!-- ===== Header ===== -->
  <header class="site-header">
    <div class="container nav">
      <a href="index.html" class="brand">
        <span class="brand-mark">C</span>
        <span>Crossxyreggy<small>Enterprise</small></span>
      </a>

      <nav class="nav-links" id="navLinks">
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="services.html" class="active">Services</a>
        <a href="portfolio.html">Our Work</a>
        <a href="contact.html">Contact</a>
        <a href="contact.html" class="btn btn--primary nav-cta">Get a Quote</a>
      </nav>

      <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- ===== Page banner ===== -->
  <section class="page-banner">
    <div class="container">
      <h1>Our Services</h1>
      <p>Design, branding, printing, signage and marketing — delivered end to end.</p>
      <div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Services</div>
    </div>
  </section>

  <!-- ===== Service 1: Graphic Design ===== -->
  <section class="section">
    <div class="container split">
      <div class="reveal">
        <span class="eyebrow">Service 01</span>
        <h2>Graphic Design</h2>
        <p>Great design makes your business easy to understand and hard to forget. We craft clear, professional visuals tailored to your audience and goals.</p>
        <ul class="check-list">
          <li>Logo design and logo refinement</li>
          <li>Brochures, flyers, posters and menus</li>
          <li>Packaging and label design</li>
          <li>Digital artwork for web and social media</li>
        </ul>
      </div>
      <div class="reveal">
        <img src="https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=graphic%20designer%20working%20on%20a%20logo%20and%20poster%20layouts%20on%20a%20computer%20screen%20creative%20studio%20desk%20overhead&image_size=landscape_4_3" alt="Graphic design work in progress" loading="lazy" />
      </div>
    </div>
  </section>

  <!-- ===== Service 2: Branding ===== -->
  <section class="section section--soft">
    <div class="container split">
      <div class="reveal" style="order:2">
        <span class="eyebrow">Service 02</span>
        <h2>Branding</h2>
        <p>A strong brand is more than a logo. We build complete identity systems that keep your business consistent and recognisable everywhere it appears.</p>
        <ul class="check-list">
          <li>Brand identity and visual systems</li>
          <li>Colour palettes and typography selection</li>
          <li>Brand style guides</li>
          <li>Corporate stationery and templates</li>
        </ul>
      </div>
      <div class="reveal" style="order:1">
        <img src="https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=brand%20identity%20board%20flat%20lay%20with%20logo%20variations%20colour%20swatches%20business%20cards%20and%20stationery%20mockups&image_size=landscape_4_3" alt="Brand identity boards and stationery" loading="lazy" />
      </div>
    </div>
  </section>

  <!-- ===== Service 3: Printing ===== -->
  <section class="section">
    <div class="container split">
      <div class="reveal">
        <span class="eyebrow">Service 03</span>
        <h2>Printing Services</h2>
        <p>From a few hundred business cards to large-format banners, we deliver sharp, durable print with dependable turnaround times.</p>
        <ul class="check-list">
          <li>Business cards, letterheads and invoices</li>
          <li>Flyers, brochures and booklets</li>
          <li>Banners, pull-up stands and posters</li>
          <li>Large-format and bulk commercial printing</li>
        </ul>
      </div>
      <div class="reveal">
        <img src="https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=stacks%20of%20freshly%20printed%20business%20cards%20brochures%20and%20colourful%20banners%20in%20a%20print%20shop&image_size=landscape_4_3" alt="Printed business cards, brochures and banners" loading="lazy" />
      </div>
    </div>
  </section>

  <!-- ===== Service 4: Signage ===== -->
  <section class="section section--soft">
    <div class="container split">
      <div class="reveal" style="order:2">
        <span class="eyebrow">Service 04</span>
        <h2>Signage Installation</h2>
        <p>We design, manufacture and install signage that gets your business noticed — on your building, your shopfront and your vehicles.</p>
        <ul class="check-list">
          <li>Shopfront and building signage</li>
          <li>3D lettering and lightboxes</li>
          <li>Vehicle branding and wraps</li>
          <li>Billboards and site boards</li>
        </ul>
      </div>
      <div class="reveal" style="order:1">
        <img src="https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=workers%20installing%20a%20large%20shopfront%20sign%20on%20a%20building%20exterior%20professional%20signage%20installation&image_size=landscape_4_3" alt="Signage installation on a shopfront" loading="lazy" />
      </div>
    </div>
  </section>

  <!-- ===== Service 5: Marketing ===== -->
  <section class="section">
    <div class="container split">
      <div class="reveal">
        <span class="eyebrow">Service 05</span>
        <h2>Marketing</h2>
        <p>Design is only half the story. We help you put your brand in front of the right people through targeted campaigns and consistent promotional material.</p>
        <ul class="check-list">
          <li>Marketing and campaign collateral</li>
          <li>Social media graphics and templates</li>
          <li>Promotional and event material</li>
          <li>Brand activation support</li>
        </ul>
      </div>
      <div class="reveal">
        <img src="https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=marketing%20campaign%20materials%20spread%20on%20a%20desk%20with%20social%20media%20graphics%20flyers%20and%20branded%20promotional%20items&image_size=landscape_4_3" alt="Marketing campaign materials" loading="lazy" />
      </div>
    </div>
  </section>

  <!-- ===== Extras grid ===== -->
  <section class="section section--soft">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Also Available</span>
        <h2>Extra support to complete your project</h2>
      </div>
      <div class="grid grid--3">
        <article class="card reveal">
          <h3>Design Consultation</h3>
          <p>Guidance on the right visual direction, formats and materials before you commit to print.</p>
        </article>
        <article class="card reveal">
          <h3>Brand Rollouts</h3>
          <p>Applying a single brand consistently across print, signage, vehicles and digital touchpoints.</p>
        </article>
        <article class="card reveal">
          <h3>Artwork Management</h3>
          <p>Files prepared, stored and supplied in print-ready formats whenever you need them again.</p>
        </article>
      </div>
    </div>
  </section>

  <!-- ===== CTA ===== -->
  <section class="section">
    <div class="container">
      <div class="cta-band reveal">
        <div>
          <h2>Need a quote for your project?</h2>
          <p>Send us the details and we'll come back with pricing and timelines.</p>
        </div>
        <a href="contact.html" class="btn btn--primary">Request a Quote</a>
      </div>
    </div>
  </section>

  <!-- ===== Footer ===== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <a href="index.html" class="brand">
            <span class="brand-mark">C</span>
            <span>Crossxyreggy<small>Enterprise</small></span>
          </a>
          <p>Full-service graphics, branding, printing, signage and marketing solutions for businesses that want to stand out.</p>
          <div class="social-links">
            <a href="https://www.facebook.com/profile.php?id=61578953435664" target="_blank" rel="noopener" aria-label="Facebook">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="portfolio.html">Our Work</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="services.html">Graphic Design</a></li>
            <li><a href="services.html">Branding</a></li>
            <li><a href="services.html">Printing</a></li>
            <li><a href="services.html">Signage</a></li>
            <li><a href="services.html">Marketing</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Get in Touch</h4>
          <ul>
            <li><a href="tel:+263715029199">+263 71 502 9199</a></li>
            <li><a href="tel:+263777297024">+263 77 729 7024</a></li>
            <li><a href="tel:+263774327362">+263 77 432 7362</a></li>
            <li><a href="mailto:info.crossxyreggyentstreammedia@gmail.com">info.crossxyreggyentstreammedia@gmail.com</a></li>
            <li><a href="contact.html">Request a Quote</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; <span id="year">2026</span> Crossxyreggy Enterprise. All rights reserved.</p>
        <p>Graphics &middot; Branding &middot; Printing &middot; Signage &middot; Marketing &middot; <a href="admin.html">Site Admin</a></p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
"""


# ==========================================================================
#  contact.html
# ==========================================================================
CONTACT_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Contact Us | Crossxyreggy Enterprise</title>
  <meta name="description" content="Contact Crossxyreggy Enterprise for graphic design, branding, printing, signage and marketing enquiries." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

  <!-- ===== Header ===== -->
  <header class="site-header">
    <div class="container nav">
      <a href="index.html" class="brand">
        <span class="brand-mark">C</span>
        <span>Crossxyreggy<small>Enterprise</small></span>
      </a>

      <nav class="nav-links" id="navLinks">
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="services.html">Services</a>
        <a href="portfolio.html">Our Work</a>
        <a href="contact.html" class="active">Contact</a>
        <a href="contact.html" class="btn btn--primary nav-cta">Get a Quote</a>
      </nav>

      <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- ===== Page banner ===== -->
  <section class="page-banner">
    <div class="container">
      <h1>Get in Touch</h1>
      <p>Tell us about your project and we'll get back to you within one business day.</p>
      <div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Contact</div>
    </div>
  </section>

  <!-- ===== Contact form + info ===== -->
  <section class="section">
    <div class="container form-wrap">

      <!-- Contact details -->
      <div class="reveal">
        <span class="eyebrow">Contact Details</span>
        <h2>We'd love to hear from you</h2>
        <p style="margin-bottom:32px">Reach us by phone, email or the form, or pop in and see us at the studio.</p>

        <div class="info-block">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          </div>
          <div>
            <h4>Phone / WhatsApp</h4>
            <p>
              <a href="tel:+263715029199">+263 71 502 9199</a><br>
              <a href="tel:+263777297024">+263 77 729 7024</a><br>
              <a href="tel:+263774327362">+263 77 432 7362</a>
            </p>
          </div>
        </div>

        <div class="info-block">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          </div>
          <div>
            <h4>Email</h4>
            <p><a href="mailto:info.crossxyreggyentstreammedia@gmail.com">info.crossxyreggyentstreammedia@gmail.com</a></p>
          </div>
        </div>

        <div class="info-block">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
          </div>
          <div>
            <h4>Address</h4>
            <p>Corner Speke &amp; Leopold Takawira, Reliance Mall, Room F17</p>
          </div>
        </div>

        <div class="info-block">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          </div>
          <div>
            <h4>Business Hours</h4>
            <p>Monday &ndash; Saturday: 7:30 &ndash; 15:00</p>
          </div>
        </div>

        <div class="info-block">
          <div class="card-icon">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>
          </div>
          <div>
            <h4>Follow Us</h4>
            <p><a href="https://www.facebook.com/profile.php?id=61578953435664" target="_blank" rel="noopener">Crossxyreggy Ent Stream Media</a></p>
          </div>
        </div>
      </div>

      <!-- Form -->
      <div class="reveal">
        <form id="contactForm" novalidate>
          <div class="form-group">
            <label for="name">Full Name</label>
            <input type="text" id="name" name="name" class="form-control" placeholder="Your name" required />
          </div>

          <div class="form-group">
            <label for="email">Email Address</label>
            <input type="email" id="email" name="email" class="form-control" placeholder="you@example.com" required />
          </div>

          <div class="form-group">
            <label for="phone">Phone Number</label>
            <input type="tel" id="phone" name="phone" class="form-control" placeholder="Optional" />
          </div>

          <div class="form-group">
            <label for="service">Service Needed</label>
            <select id="service" name="service" class="form-control">
              <option value="">Select a service</option>
              <option>Graphic Design</option>
              <option>Branding</option>
              <option>Printing Services</option>
              <option>Signage Installation</option>
              <option>Marketing</option>
              <option>Other / Not sure</option>
            </select>
          </div>

          <div class="form-group">
            <label for="message">Project Details</label>
            <textarea id="message" name="message" class="form-control" placeholder="Tell us briefly what you need..." required></textarea>
          </div>

          <button type="submit" class="btn btn--primary" style="width:100%">Send Enquiry</button>
          <p class="form-note">This form is a front-end demo. Connect it to your email or form service to receive submissions.</p>
          <div class="form-status" id="formStatus" role="status"></div>
        </form>
      </div>

    </div>
  </section>

  <!-- ===== Map ===== -->
  <section class="section section--soft">
    <div class="container">
      <div class="section-head reveal">
        <span class="eyebrow">Find Us</span>
        <h2>Visit our studio</h2>
        <p>Corner Speke &amp; Leopold Takawira, Reliance Mall, Room F17.</p>
      </div>
      <iframe
        class="map-embed reveal"
        title="Business location map"
        loading="lazy"
        referrerpolicy="no-referrer-when-downgrade"
        src="https://www.openstreetmap.org/export/embed.html?bbox=31.0380%2C-17.8360%2C31.0520%2C-17.8240&layer=mapnik&marker=-17.8300%2C31.0450">
      </iframe>
    </div>
  </section>

  <!-- ===== Footer ===== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <a href="index.html" class="brand">
            <span class="brand-mark">C</span>
            <span>Crossxyreggy<small>Enterprise</small></span>
          </a>
          <p>Full-service graphics, branding, printing, signage and marketing solutions for businesses that want to stand out.</p>
          <div class="social-links">
            <a href="https://www.facebook.com/profile.php?id=61578953435664" target="_blank" rel="noopener" aria-label="Facebook">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="portfolio.html">Our Work</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="services.html">Graphic Design</a></li>
            <li><a href="services.html">Branding</a></li>
            <li><a href="services.html">Printing</a></li>
            <li><a href="services.html">Signage</a></li>
            <li><a href="services.html">Marketing</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Get in Touch</h4>
          <ul>
            <li><a href="tel:+263715029199">+263 71 502 9199</a></li>
            <li><a href="tel:+263777297024">+263 77 729 7024</a></li>
            <li><a href="tel:+263774327362">+263 77 432 7362</a></li>
            <li><a href="mailto:info.crossxyreggyentstreammedia@gmail.com">info.crossxyreggyentstreammedia@gmail.com</a></li>
            <li><a href="contact.html">Request a Quote</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; <span id="year">2026</span> Crossxyreggy Enterprise. All rights reserved.</p>
        <p>Graphics &middot; Branding &middot; Printing &middot; Signage &middot; Marketing &middot; <a href="admin.html">Site Admin</a></p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
"""


# ==========================================================================
#  portfolio.html
# ==========================================================================
PORTFOLIO_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Our Work | Crossxyreggy Enterprise</title>
  <meta name="description" content="Browse the Crossxyreggy Enterprise catalogue of design, branding, printing, signage and marketing work." />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

  <!-- ===== Header ===== -->
  <header class="site-header">
    <div class="container nav">
      <a href="index.html" class="brand">
        <span class="brand-mark">C</span>
        <span>Crossxyreggy<small>Enterprise</small></span>
      </a>

      <nav class="nav-links" id="navLinks">
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="services.html">Services</a>
        <a href="portfolio.html" class="active">Our Work</a>
        <a href="contact.html">Contact</a>
        <a href="contact.html" class="btn btn--primary nav-cta">Get a Quote</a>
      </nav>

      <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- ===== Page banner ===== -->
  <section class="page-banner">
    <div class="container">
      <h1>Our Work</h1>
      <p>A catalogue of the design, branding, printing, signage and marketing projects we deliver.</p>
      <div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Our Work</div>
    </div>
  </section>

  <!-- ===== Gallery ===== -->
  <section class="section">
    <div class="container">
      <div class="filter-bar" id="filterBar"></div>
      <div class="gallery" id="gallery"></div>
    </div>
  </section>

  <!-- ===== CTA ===== -->
  <section class="section section--soft">
    <div class="container">
      <div class="cta-band reveal">
        <div>
          <h2>Like what you see?</h2>
          <p>Let's create work you'll be proud to add to this catalogue.</p>
        </div>
        <a href="contact.html" class="btn btn--primary">Start Your Project</a>
      </div>
    </div>
  </section>

  <!-- ===== Footer ===== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <a href="index.html" class="brand">
            <span class="brand-mark">C</span>
            <span>Crossxyreggy<small>Enterprise</small></span>
          </a>
          <p>Full-service graphics, branding, printing, signage and marketing solutions for businesses that want to stand out.</p>
          <div class="social-links">
            <a href="https://www.facebook.com/profile.php?id=61578953435664" target="_blank" rel="noopener" aria-label="Facebook">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="portfolio.html">Our Work</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="services.html">Graphic Design</a></li>
            <li><a href="services.html">Branding</a></li>
            <li><a href="services.html">Printing</a></li>
            <li><a href="services.html">Signage</a></li>
            <li><a href="services.html">Marketing</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Get in Touch</h4>
          <ul>
            <li><a href="tel:+263715029199">+263 71 502 9199</a></li>
            <li><a href="tel:+263777297024">+263 77 729 7024</a></li>
            <li><a href="tel:+263774327362">+263 77 432 7362</a></li>
            <li><a href="mailto:info.crossxyreggyentstreammedia@gmail.com">info.crossxyreggyentstreammedia@gmail.com</a></li>
            <li><a href="contact.html">Request a Quote</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; <span id="year">2026</span> Crossxyreggy Enterprise. All rights reserved.</p>
        <p>Graphics &middot; Branding &middot; Printing &middot; Signage &middot; Marketing &middot; <a href="admin.html">Site Admin</a></p>
      </div>
    </div>
  </footer>

  <!-- ===== Lightbox ===== -->
  <div class="lightbox" id="lightbox" role="dialog" aria-modal="true" aria-label="Image viewer">
    <button class="lightbox-close" aria-label="Close">&times;</button>
    <button class="lightbox-prev" aria-label="Previous image">&#8249;</button>
    <button class="lightbox-next" aria-label="Next image">&#8250;</button>
    <figure class="lightbox-figure">
      <img id="lightboxImg" src="" alt="" />
      <figcaption class="lightbox-caption">
        <small id="lightboxCat"></small>
        <span id="lightboxTitle"></span>
      </figcaption>
    </figure>
  </div>

  <script src="js/main.js"></script>
  <script src="js/portfolio.js"></script>
</body>
</html>
"""


# ==========================================================================
#  css/style.css
# ==========================================================================
STYLE_CSS = r"""/* ==========================================================================
   Crossxyreggy Enterprise — Corporate Website
   ========================================================================== */

:root {
  --navy: #0d2340;
  --navy-2: #14355e;
  --blue: #1c66c4;
  --blue-light: #3d8bdb;
  --accent: #f5a623;
  --text: #1f2a37;
  --muted: #5b6b7f;
  --line: #e2e8f0;
  --bg: #ffffff;
  --bg-soft: #f4f7fb;
  --radius: 10px;
  --shadow: 0 10px 30px rgba(13, 35, 64, 0.08);
  --shadow-lg: 0 20px 50px rgba(13, 35, 64, 0.14);
  --container: 1160px;
  --transition: 0.25s ease;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  scroll-behavior: smooth;
}

body {
  font-family: "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  color: var(--text);
  background: var(--bg);
  line-height: 1.65;
  font-size: 16px;
  -webkit-font-smoothing: antialiased;
}

img {
  max-width: 100%;
  display: block;
}

a {
  color: var(--blue);
  text-decoration: none;
  transition: color var(--transition);
}

a:hover {
  color: var(--blue-light);
}

h1, h2, h3, h4 {
  line-height: 1.25;
  color: var(--navy);
  font-weight: 700;
}

h1 { font-size: clamp(2rem, 4vw, 3rem); }
h2 { font-size: clamp(1.6rem, 3vw, 2.25rem); }
h3 { font-size: 1.25rem; }

p { color: var(--muted); }

ul { list-style: none; }

/* ---------- Layout helpers ---------- */
.container {
  width: 100%;
  max-width: var(--container);
  margin: 0 auto;
  padding: 0 24px;
}

.section {
  padding: 80px 0;
}

.section--soft { background: var(--bg-soft); }

.section-head {
  text-align: center;
  max-width: 680px;
  margin: 0 auto 56px;
}

.section-head p { margin-top: 14px; font-size: 1.05rem; }

.eyebrow {
  display: inline-block;
  font-size: 0.8rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  font-weight: 700;
  color: var(--blue);
  margin-bottom: 12px;
}

/* ---------- Buttons ---------- */
.btn {
  display: inline-block;
  padding: 13px 28px;
  border-radius: var(--radius);
  font-weight: 600;
  font-size: 0.95rem;
  border: 2px solid transparent;
  cursor: pointer;
  transition: all var(--transition);
  text-align: center;
}

.btn--primary {
  background: var(--blue);
  color: #fff;
}

.btn--primary:hover {
  background: var(--navy-2);
  color: #fff;
  transform: translateY(-2px);
  box-shadow: var(--shadow);
}

.btn--ghost {
  background: transparent;
  border-color: rgba(255, 255, 255, 0.5);
  color: #fff;
}

.btn--ghost:hover {
  background: #fff;
  color: var(--navy);
}

.btn--outline {
  background: transparent;
  border-color: var(--blue);
  color: var(--blue);
}

.btn--outline:hover {
  background: var(--blue);
  color: #fff;
}

/* ---------- Header / Nav ---------- */
.site-header {
  position: sticky;
  top: 0;
  z-index: 100;
  background: #fff;
  border-bottom: 1px solid var(--line);
  box-shadow: 0 2px 12px rgba(13, 35, 64, 0.04);
}

.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 76px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 12px;
  font-weight: 800;
  font-size: 1.15rem;
  color: var(--navy);
  letter-spacing: -0.01em;
}

.brand:hover { color: var(--navy); }

.brand-mark {
  width: 40px;
  height: 40px;
  border-radius: 9px;
  background: linear-gradient(135deg, var(--blue), var(--navy));
  color: #fff;
  display: grid;
  place-items: center;
  font-size: 1.15rem;
  font-weight: 800;
  flex-shrink: 0;
}

.brand small {
  display: block;
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--muted);
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 6px;
}

.nav-links a {
  padding: 9px 16px;
  border-radius: 8px;
  color: var(--navy);
  font-weight: 600;
  font-size: 0.95rem;
}

.nav-links a:hover { background: var(--bg-soft); color: var(--blue); }

.nav-links a.active { color: var(--blue); }

.nav-cta { margin-left: 12px; }

.nav-toggle {
  display: none;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
}

.nav-toggle span {
  display: block;
  width: 24px;
  height: 2px;
  background: var(--navy);
  margin: 5px 0;
  transition: var(--transition);
}

/* ---------- Hero ---------- */
.hero {
  position: relative;
  color: #fff;
  background: linear-gradient(135deg, rgba(13, 35, 64, 0.92), rgba(20, 53, 94, 0.82)),
    url("https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=professional%20modern%20graphic%20design%20studio%20workspace%20with%20branding%20mockups%20color%20swatches%20and%20printer%20wide%20shot%20corporate%20blue%20tones&image_size=landscape_16_9") center/cover no-repeat;
  padding: 120px 0 110px;
}

.hero h1 { color: #fff; max-width: 780px; }

.hero p {
  color: rgba(255, 255, 255, 0.86);
  font-size: 1.12rem;
  max-width: 620px;
  margin: 22px 0 34px;
}

.hero-actions { display: flex; flex-wrap: wrap; gap: 14px; }

.hero-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 48px;
  margin-top: 64px;
  padding-top: 34px;
  border-top: 1px solid rgba(255, 255, 255, 0.18);
}

.hero-stats .stat strong {
  display: block;
  font-size: 2rem;
  color: #fff;
}

.hero-stats .stat span {
  font-size: 0.85rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.7);
}

/* ---------- Grids ---------- */
.grid {
  display: grid;
  gap: 28px;
}

.grid--3 { grid-template-columns: repeat(3, 1fr); }
.grid--2 { grid-template-columns: repeat(2, 1fr); }
.grid--4 { grid-template-columns: repeat(4, 1fr); }

/* ---------- Cards ---------- */
.card {
  background: #fff;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 32px;
  transition: all var(--transition);
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow);
  border-color: transparent;
}

.card h3 { margin-bottom: 10px; }

.card-icon {
  width: 52px;
  height: 52px;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--blue), var(--navy));
  display: grid;
  place-items: center;
  margin-bottom: 20px;
  color: #fff;
}

.card-icon svg { width: 26px; height: 26px; }

.service-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  margin-top: 16px;
  font-weight: 600;
  font-size: 0.9rem;
}

/* ---------- About / feature split ---------- */
.split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: center;
}

.split img { border-radius: var(--radius); box-shadow: var(--shadow-lg); }

.check-list { margin-top: 24px; }

.check-list li {
  position: relative;
  padding-left: 32px;
  margin-bottom: 14px;
  color: var(--muted);
}

.check-list li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 6px;
  width: 18px;
  height: 18px;
  border-radius: 50%;
  background: var(--blue);
}

.check-list li::after {
  content: "";
  position: absolute;
  left: 6px;
  top: 10px;
  width: 5px;
  height: 9px;
  border: solid #fff;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

/* ---------- Values / steps ---------- */
.value {
  text-align: center;
  padding: 32px 20px;
}

.value-num {
  font-size: 2.4rem;
  font-weight: 800;
  color: var(--accent);
  line-height: 1;
}

.value h3 { margin: 14px 0 8px; }

/* ---------- CTA band ---------- */
.cta-band {
  background: linear-gradient(135deg, var(--navy), var(--navy-2));
  color: #fff;
  border-radius: var(--radius);
  padding: 56px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 32px;
  flex-wrap: wrap;
}

.cta-band h2 { color: #fff; }

.cta-band p {
  color: rgba(255, 255, 255, 0.82);
  margin-top: 10px;
  max-width: 540px;
}

/* ---------- Page banner ---------- */
.page-banner {
  background: linear-gradient(135deg, var(--navy), var(--navy-2));
  color: #fff;
  padding: 72px 0;
  text-align: center;
}

.page-banner h1 { color: #fff; }

.page-banner p {
  color: rgba(255, 255, 255, 0.8);
  margin-top: 12px;
  max-width: 620px;
  margin-left: auto;
  margin-right: auto;
}

.breadcrumb {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.65);
  margin-top: 18px;
}

.breadcrumb a { color: rgba(255, 255, 255, 0.85); }

/* ---------- Forms ---------- */
.form-wrap {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 56px;
}

.form-group { margin-bottom: 20px; }

.form-group label {
  display: block;
  font-weight: 600;
  font-size: 0.9rem;
  margin-bottom: 8px;
  color: var(--navy);
}

.form-control {
  width: 100%;
  padding: 13px 16px;
  border: 1px solid var(--line);
  border-radius: 8px;
  font-family: inherit;
  font-size: 1rem;
  color: var(--text);
  background: #fff;
  transition: border-color var(--transition), box-shadow var(--transition);
}

.form-control:focus {
  outline: none;
  border-color: var(--blue);
  box-shadow: 0 0 0 3px rgba(28, 102, 196, 0.14);
}

textarea.form-control { resize: vertical; min-height: 140px; }

.form-note {
  font-size: 0.85rem;
  color: var(--muted);
  margin-top: 10px;
}

.form-status {
  margin-top: 16px;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 0.92rem;
  display: none;
}

.form-status.success {
  display: block;
  background: #e7f6ec;
  color: #1a7f37;
  border: 1px solid #b7e3c5;
}

/* ---------- Contact info blocks ---------- */
.info-block {
  display: flex;
  gap: 18px;
  margin-bottom: 28px;
}

.info-block .card-icon {
  width: 46px;
  height: 46px;
  margin-bottom: 0;
  flex-shrink: 0;
}

.info-block h4 { margin-bottom: 4px; }

.info-block p { margin: 0; }

.info-block a { color: var(--muted); }

.info-block a:hover { color: var(--blue); }

/* ---------- Map ---------- */
.map-embed {
  border: 0;
  width: 100%;
  height: 320px;
  border-radius: var(--radius);
  filter: grayscale(0.2);
}

/* ---------- Footer ---------- */
.site-footer {
  background: var(--navy);
  color: rgba(255, 255, 255, 0.72);
  padding: 64px 0 0;
}

.footer-grid {
  display: grid;
  grid-template-columns: 1.6fr 1fr 1fr 1.2fr;
  gap: 40px;
  padding-bottom: 48px;
}

.site-footer .brand { color: #fff; }

.site-footer .brand small { color: rgba(255, 255, 255, 0.55); }

.footer-about p {
  color: rgba(255, 255, 255, 0.66);
  margin-top: 18px;
  font-size: 0.93rem;
}

.footer-col h4 {
  color: #fff;
  font-size: 0.95rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 18px;
}

.footer-col li { margin-bottom: 11px; }

.footer-col a { color: rgba(255, 255, 255, 0.72); font-size: 0.94rem; }

.footer-col a:hover { color: #fff; }

.footer-bottom {
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  padding: 22px 0;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
  font-size: 0.87rem;
}

.footer-bottom p { color: rgba(255, 255, 255, 0.6); }

.social-links {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

.social-links a {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  display: grid;
  place-items: center;
  color: rgba(255, 255, 255, 0.8);
  transition: all var(--transition);
}

.social-links a:hover {
  background: var(--blue);
  color: #fff;
  transform: translateY(-2px);
}

.social-links svg { width: 18px; height: 18px; }

/* ---------- Portfolio filters ---------- */
.filter-bar {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 10px;
  margin-bottom: 44px;
}

.filter-btn {
  padding: 10px 20px;
  border: 1px solid var(--line);
  background: #fff;
  color: var(--navy);
  border-radius: 999px;
  font-family: inherit;
  font-size: 0.92rem;
  font-weight: 600;
  cursor: pointer;
  transition: all var(--transition);
}

.filter-btn:hover { border-color: var(--blue); color: var(--blue); }

.filter-btn.active {
  background: var(--blue);
  border-color: var(--blue);
  color: #fff;
}

/* ---------- Portfolio gallery ---------- */
.gallery {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 22px;
}

.gallery-item {
  position: relative;
  border-radius: var(--radius);
  overflow: hidden;
  cursor: pointer;
  background: var(--bg-soft);
  aspect-ratio: 4 / 3;
  box-shadow: var(--shadow);
}

.gallery-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.gallery-item:hover img { transform: scale(1.06); }

.gallery-overlay {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding: 22px;
  background: linear-gradient(to top, rgba(13, 35, 64, 0.88), rgba(13, 35, 64, 0.05) 65%);
  opacity: 0;
  transition: opacity var(--transition);
}

.gallery-item:hover .gallery-overlay { opacity: 1; }

.gallery-overlay span {
  color: var(--accent);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.gallery-overlay h3 {
  color: #fff;
  font-size: 1.05rem;
  margin-top: 6px;
}

.gallery-empty {
  grid-column: 1 / -1;
  text-align: center;
  padding: 60px 20px;
  color: var(--muted);
}

/* ---------- Lightbox ---------- */
.lightbox {
  position: fixed;
  inset: 0;
  z-index: 200;
  background: rgba(9, 20, 36, 0.94);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 32px;
}

.lightbox.open { display: flex; }

.lightbox-figure {
  max-width: 960px;
  width: 100%;
  text-align: center;
}

.lightbox-figure img {
  max-height: 76vh;
  width: auto;
  margin: 0 auto;
  border-radius: var(--radius);
  box-shadow: var(--shadow-lg);
}

.lightbox-caption {
  color: #fff;
  margin-top: 18px;
  font-size: 1.05rem;
  font-weight: 600;
}

.lightbox-caption small {
  display: block;
  color: var(--accent);
  font-size: 0.75rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin-bottom: 6px;
}

.lightbox-close,
.lightbox-prev,
.lightbox-next {
  position: absolute;
  background: rgba(255, 255, 255, 0.12);
  border: none;
  color: #fff;
  cursor: pointer;
  border-radius: 50%;
  width: 48px;
  height: 48px;
  font-size: 1.5rem;
  line-height: 1;
  display: grid;
  place-items: center;
  transition: background var(--transition);
}

.lightbox-close:hover,
.lightbox-prev:hover,
.lightbox-next:hover { background: rgba(255, 255, 255, 0.28); }

.lightbox-close { top: 24px; right: 24px; }
.lightbox-prev { left: 24px; top: 50%; transform: translateY(-50%); }
.lightbox-next { right: 24px; top: 50%; transform: translateY(-50%); }

/* ---------- Reveal animation ---------- */
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}

.reveal.in { opacity: 1; transform: none; }

/* ---------- Responsive ---------- */
@media (max-width: 980px) {
  .grid--3, .grid--4 { grid-template-columns: repeat(2, 1fr); }
  .gallery { grid-template-columns: repeat(2, 1fr); }
  .split { grid-template-columns: 1fr; gap: 40px; }
  .form-wrap { grid-template-columns: 1fr; gap: 40px; }
  .footer-grid { grid-template-columns: 1fr 1fr; }

  .nav-toggle { display: block; }

  .nav-links {
    position: absolute;
    top: 76px;
    left: 0;
    right: 0;
    flex-direction: column;
    align-items: stretch;
    background: #fff;
    border-bottom: 1px solid var(--line);
    padding: 12px 24px 20px;
    gap: 4px;
    box-shadow: var(--shadow);
    display: none;
  }

  .nav-links.open { display: flex; }

  .nav-links a { padding: 12px 14px; }

  .nav-cta { margin: 8px 0 0; }
}

@media (max-width: 620px) {
  .section { padding: 56px 0; }
  .grid--3, .grid--4, .grid--2 { grid-template-columns: 1fr; }
  .gallery { grid-template-columns: 1fr; }
  .footer-grid { grid-template-columns: 1fr; }
  .hero { padding: 84px 0 72px; }
  .hero-stats { gap: 28px; }
  .cta-band { padding: 36px 26px; }
  .card { padding: 26px; }
  .lightbox-prev { left: 10px; }
  .lightbox-next { right: 10px; }
  .lightbox-close { top: 12px; right: 12px; }
}

/* ---------- Photo Manager (admin.html) ---------- */
.admin-steps {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 22px;
  margin-bottom: 40px;
  list-style: none;
}

.admin-steps li {
  display: flex;
  gap: 16px;
  background: var(--bg-soft);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 22px;
}

.admin-steps li > span {
  flex-shrink: 0;
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background: var(--blue);
  color: #fff;
  font-weight: 700;
  display: grid;
  place-items: center;
}

.admin-steps strong { display: block; color: var(--navy); margin-bottom: 4px; }
.admin-steps p { font-size: 0.92rem; margin: 0; }

.admin-steps code {
  background: #fff;
  border: 1px solid var(--line);
  border-radius: 5px;
  padding: 1px 6px;
  font-size: 0.85em;
  color: var(--navy);
}

.admin-card {
  background: #fff;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  padding: 30px;
  box-shadow: var(--shadow);
  margin-bottom: 28px;
}

.admin-card h2 { font-size: 1.35rem; }

.admin-card-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 18px;
  flex-wrap: wrap;
  margin-bottom: 6px;
}

.admin-card-head small { color: var(--muted); font-weight: 600; font-size: 0.9rem; }

.admin-actions { display: flex; gap: 10px; flex-wrap: wrap; }

.btn--sm { padding: 10px 18px; font-size: 0.88rem; }

.admin-note { font-size: 0.9rem; color: var(--muted); margin: 6px 0 18px; }
.admin-note--warn { color: #b42318; font-weight: 600; }

.dropzone {
  border: 2px dashed #b9c8db;
  border-radius: var(--radius);
  background: var(--bg-soft);
  padding: 44px 24px;
  text-align: center;
  cursor: pointer;
  transition: all var(--transition);
}

.dropzone:hover,
.dropzone.dragging {
  border-color: var(--blue);
  background: #eef5fd;
}

.dropzone-icon {
  width: 54px;
  height: 54px;
  margin: 0 auto 16px;
  border-radius: 50%;
  background: var(--blue);
  color: #fff;
  font-size: 1.8rem;
  line-height: 1;
  display: grid;
  place-items: center;
}

.dropzone strong { display: block; color: var(--navy); font-size: 1.05rem; }
.dropzone span { display: block; color: var(--muted); font-size: 0.9rem; margin-top: 6px; }

.admin-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 18px;
}

.admin-item {
  position: relative;
  background: var(--bg-soft);
  border: 1px solid var(--line);
  border-radius: var(--radius);
  overflow: hidden;
  padding-bottom: 14px;
}

.admin-item img {
  width: 100%;
  aspect-ratio: 4 / 3;
  object-fit: cover;
  background: #dfe7f1;
}

.admin-badge {
  position: absolute;
  top: 10px;
  left: 10px;
  background: var(--accent);
  color: #3a2600;
  font-size: 0.7rem;
  font-weight: 800;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 4px 9px;
  border-radius: 999px;
}

.admin-remove {
  position: absolute;
  top: 8px;
  right: 8px;
  width: 30px;
  height: 30px;
  border: none;
  border-radius: 50%;
  background: rgba(13, 35, 64, 0.72);
  color: #fff;
  font-size: 1.15rem;
  line-height: 1;
  cursor: pointer;
  display: grid;
  place-items: center;
  transition: background var(--transition);
}

.admin-remove:hover { background: #b42318; }

.admin-input,
.admin-select {
  width: calc(100% - 24px);
  margin: 12px 12px 0;
  padding: 9px 12px;
  border: 1px solid var(--line);
  border-radius: 8px;
  font-family: inherit;
  font-size: 0.9rem;
  color: var(--text);
  background: #fff;
}

.admin-input:focus,
.admin-select:focus {
  outline: none;
  border-color: var(--blue);
  box-shadow: 0 0 0 3px rgba(28, 102, 196, 0.14);
}

.admin-empty {
  text-align: center;
  color: var(--muted);
  padding: 40px 20px;
}

.admin-tip {
  background: #fff9ec;
  border: 1px solid #f5dfa8;
  border-radius: var(--radius);
  padding: 18px 22px;
  font-size: 0.92rem;
  color: #6b5417;
}

.admin-tip code {
  background: #fff;
  border: 1px solid #f0dcae;
  border-radius: 5px;
  padding: 1px 6px;
  font-size: 0.85em;
}

@media (max-width: 980px) {
  .admin-steps { grid-template-columns: 1fr; }
  .admin-grid { grid-template-columns: repeat(3, 1fr); }
}

@media (max-width: 620px) {
  .admin-grid { grid-template-columns: repeat(2, 1fr); }
  .admin-card { padding: 22px; }
}
"""


# ==========================================================================
#  js/main.js
# ==========================================================================
MAIN_JS = r"""/* ==========================================================================
   Crossxyreggy Enterprise — Site interactions
   ========================================================================== */

document.addEventListener("DOMContentLoaded", function () {
  /* ---- Mobile navigation toggle ---- */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");

  if (toggle && links) {
    toggle.addEventListener("click", function () {
      links.classList.toggle("open");
      var expanded = links.classList.contains("open");
      toggle.setAttribute("aria-expanded", expanded ? "true" : "false");
    });

    links.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        links.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---- Scroll reveal ---- */
  var revealEls = document.querySelectorAll(".reveal");

  if ("IntersectionObserver" in window && revealEls.length) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("in");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );

    revealEls.forEach(function (el) {
      observer.observe(el);
    });
  } else {
    revealEls.forEach(function (el) {
      el.classList.add("in");
    });
  }

  /* ---- Contact form (client-side only) ---- */
  var form = document.getElementById("contactForm");

  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();

      var status = document.getElementById("formStatus");
      var name = form.querySelector("#name").value.trim();

      if (status) {
        status.textContent =
          "Thank you" +
          (name ? ", " + name : "") +
          "! Your enquiry has been received. We will get back to you within one business day.";
        status.className = "form-status success";
      }

      form.reset();
    });
  }

  /* ---- Footer year ---- */
  var yearEl = document.getElementById("year");
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }
});
"""


# ==========================================================================
#  js/portfolio.js
# ==========================================================================
PORTFOLIO_JS = r"""/* ==========================================================================
   Crossxyreggy Enterprise — Work Catalogue (Portfolio)

   The list of work pictures sits between the PORTFOLIO DATA markers below.
   You can edit it by hand here, or use the Photo Manager page (admin.html)
   to add pictures without touching any code.
   ========================================================================== */

var PORTFOLIO_STORAGE_KEY = "cxs_portfolio";

/* == PORTFOLIO DATA START == */
var publishedItems = [
  // --- Graphics ---
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=elegant%20logo%20design%20presented%20on%20a%20clean%20studio%20backdrop%20branding%20mockup&image_size=landscape_4_3", title: "Logo Design", category: "Graphics" },
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=colourful%20event%20poster%20design%20mockup%20on%20a%20wall%20graphic%20design%20portfolio&image_size=landscape_4_3", title: "Poster Design", category: "Graphics" },
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=product%20packaging%20design%20mockup%20boxes%20and%20labels%20studio%20lighting&image_size=landscape_4_3", title: "Packaging Design", category: "Graphics" },

  // --- Branding ---
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=brand%20identity%20board%20flat%20lay%20with%20logo%20colour%20palette%20and%20typography%20samples&image_size=landscape_4_3", title: "Brand Identity System", category: "Branding" },
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=corporate%20stationery%20set%20business%20cards%20letterhead%20and%20folder%20branding%20mockup&image_size=landscape_4_3", title: "Corporate Stationery", category: "Branding" },
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=brand%20style%20guide%20booklet%20open%20showing%20colour%20and%20logo%20guidelines%20on%20a%20desk&image_size=landscape_4_3", title: "Brand Style Guide", category: "Branding" },

  // --- Printing ---
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=stack%20of%20premium%20printed%20business%20cards%20on%20a%20dark%20surface%20close%20up&image_size=landscape_4_3", title: "Business Cards", category: "Printing" },
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=folded%20brochures%20and%20flyers%20printed%20in%20full%20colour%20displayed%20on%20a%20table&image_size=landscape_4_3", title: "Brochures & Flyers", category: "Printing" },
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=large%20format%20printed%20banner%20and%20pull%20up%20display%20stand%20in%20a%20showroom&image_size=landscape_4_3", title: "Banners & Large Format", category: "Printing" },

  // --- Signage ---
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=modern%20shopfront%20sign%20with%20illuminated%203d%20lettering%20on%20a%20building&image_size=landscape_4_3", title: "Shopfront Signage", category: "Signage" },
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=van%20with%20full%20colour%20vehicle%20branding%20and%20graphics%20wrap%20parked%20outside&image_size=landscape_4_3", title: "Vehicle Branding", category: "Signage" },
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=large%20outdoor%20billboard%20advertising%20sign%20on%20a%20roadside%20structure&image_size=landscape_4_3", title: "Billboards", category: "Signage" },

  // --- Marketing ---
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=social%20media%20marketing%20graphics%20grid%20on%20a%20phone%20screen%20branded%20posts&image_size=landscape_4_3", title: "Social Media Graphics", category: "Marketing" },
  { src: "https://coresg-normal.trae.ai/api/ide/v1/text_to_image?prompt=promotional%20event%20stand%20with%20branded%20backdrop%20and%20marketing%20material%20in%20a%20mall&image_size=landscape_4_3", title: "Promotional Stand", category: "Marketing" }
];
/* == PORTFOLIO DATA END == */

/* What actually appears on the page. On the owner's own device this is replaced
   by the newest set saved from the Photo Manager, so changes can be previewed
   before publishing. Visitors always see exactly what is written above. */
var portfolioItems = publishedItems;

(function () {
  try {
    var saved = localStorage.getItem(PORTFOLIO_STORAGE_KEY);
    if (saved) {
      var parsed = JSON.parse(saved);
      if (Array.isArray(parsed)) portfolioItems = parsed;
    }
  } catch (e) {
    /* fall back to the published list */
  }
})();

/* ==========================================================================
   Gallery rendering — no need to edit below this line
   ========================================================================== */

document.addEventListener("DOMContentLoaded", function () {
  var gallery = document.getElementById("gallery");
  var filterBar = document.getElementById("filterBar");
  if (!gallery) return;

  var lightbox = document.getElementById("lightbox");
  var lbImg = document.getElementById("lightboxImg");
  var lbCat = document.getElementById("lightboxCat");
  var lbTitle = document.getElementById("lightboxTitle");
  var currentIndex = 0;
  var visibleItems = portfolioItems.slice();

  /* ---- Build filter buttons from the categories used ---- */
  var categories = ["All"];
  portfolioItems.forEach(function (item) {
    if (categories.indexOf(item.category) === -1) categories.push(item.category);
  });

  if (filterBar) {
    categories.forEach(function (cat) {
      var btn = document.createElement("button");
      btn.className = "filter-btn" + (cat === "All" ? " active" : "");
      btn.type = "button";
      btn.textContent = cat;
      btn.addEventListener("click", function () {
        filterBar.querySelectorAll(".filter-btn").forEach(function (b) {
          b.classList.remove("active");
        });
        btn.classList.add("active");
        render(cat === "All" ? portfolioItems : portfolioItems.filter(function (i) {
          return i.category === cat;
        }));
      });
      filterBar.appendChild(btn);
    });
  }

  /* ---- Render the gallery grid ---- */
  function render(items) {
    visibleItems = items;
    gallery.innerHTML = "";

    if (!items.length) {
      var empty = document.createElement("p");
      empty.className = "gallery-empty";
      empty.textContent = "No work to show here yet. Add pictures with the Photo Manager.";
      gallery.appendChild(empty);
      return;
    }

    items.forEach(function (item, index) {
      var card = document.createElement("figure");
      card.className = "gallery-item";
      card.setAttribute("tabindex", "0");
      card.setAttribute("role", "button");
      card.setAttribute("aria-label", "View " + item.title);

      card.innerHTML =
        '<img src="' + item.src + '" alt="' + item.title + '" loading="lazy" />' +
        '<figcaption class="gallery-overlay">' +
        "<span>" + item.category + "</span>" +
        "<h3>" + item.title + "</h3>" +
        "</figcaption>";

      card.addEventListener("click", function () { openLightbox(index); });
      card.addEventListener("keydown", function (e) {
        if (e.key === "Enter" || e.key === " ") {
          e.preventDefault();
          openLightbox(index);
        }
      });

      gallery.appendChild(card);
    });
  }

  /* ---- Lightbox ---- */
  function openLightbox(index) {
    currentIndex = index;
    showSlide();
    lightbox.classList.add("open");
    document.body.style.overflow = "hidden";
  }

  function showSlide() {
    var item = visibleItems[currentIndex];
    if (!item) return;
    lbImg.src = item.src;
    lbImg.alt = item.title;
    lbCat.textContent = item.category;
    lbTitle.textContent = item.title;
  }

  function closeLightbox() {
    lightbox.classList.remove("open");
    document.body.style.overflow = "";
  }

  function step(dir) {
    currentIndex = (currentIndex + dir + visibleItems.length) % visibleItems.length;
    showSlide();
  }

  if (lightbox) {
    lightbox.querySelector(".lightbox-close").addEventListener("click", closeLightbox);
    lightbox.querySelector(".lightbox-prev").addEventListener("click", function () { step(-1); });
    lightbox.querySelector(".lightbox-next").addEventListener("click", function () { step(1); });

    lightbox.addEventListener("click", function (e) {
      if (e.target === lightbox) closeLightbox();
    });

    document.addEventListener("keydown", function (e) {
      if (!lightbox.classList.contains("open")) return;
      if (e.key === "Escape") closeLightbox();
      if (e.key === "ArrowLeft") step(-1);
      if (e.key === "ArrowRight") step(1);
    });
  }

  /* ---- First render ---- */
  render(portfolioItems);
});
"""


# ==========================================================================
#  js/admin.js
# ==========================================================================
ADMIN_JS = r"""/* ==========================================================================
   Crossxyreggy Enterprise — Photo Manager (admin.html)

   Lets you add, rename, re-categorise and remove the pictures in your
   "Our Work" gallery without editing any code, then download an updated
   js/portfolio.js ready to publish.
   ========================================================================== */

(function () {
  "use strict";

  var STORAGE_KEY =
    typeof PORTFOLIO_STORAGE_KEY !== "undefined" ? PORTFOLIO_STORAGE_KEY : "cxs_portfolio";

  var CATEGORIES = ["Graphics", "Branding", "Printing", "Signage", "Marketing"];
  var MAX_DIM = 1400; /* longest side of a saved picture, in pixels */
  var QUALITY = 0.8; /* JPEG quality, 0 - 1 */

  var grid = document.getElementById("adminGrid");
  if (!grid) return;

  var dropzone = document.getElementById("dropzone");
  var fileInput = document.getElementById("fileInput");
  var emptyMsg = document.getElementById("adminEmpty");
  var note = document.getElementById("uploadNote");
  var countLabel = document.getElementById("countLabel");
  var downloadBtn = document.getElementById("downloadBtn");
  var resetBtn = document.getElementById("resetBtn");

  /* The published list (from js/portfolio.js) and the owner's saved changes. */
  var base = typeof publishedItems !== "undefined" ? publishedItems.slice() : [];
  var publishedSrcs = {};
  base.forEach(function (item) {
    publishedSrcs[item.src] = true;
  });

  var working = loadSaved() || base.slice();

  /* ---------- storage ---------- */

  function loadSaved() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var parsed = JSON.parse(raw);
      return Array.isArray(parsed) ? parsed : null;
    } catch (e) {
      return null;
    }
  }

  function save() {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(working));
      setNote("");
    } catch (e) {
      setNote(
        "This device has run out of space for new photos. Press \"Download gallery file\", then \"Undo all changes\", before adding more.",
        true
      );
    }
  }

  /* ---------- helpers ---------- */

  function setNote(message, isWarning) {
    note.textContent = message || "";
    note.className = "admin-note" + (isWarning ? " admin-note--warn" : "");
  }

  function isPublished(item) {
    return publishedSrcs[item.src] === true;
  }

  function titleFromFileName(name) {
    var clean = String(name).replace(/\.[^.]+$/, "").replace(/[-_]+/g, " ").trim();
    if (!clean) return "New Photo";
    return clean.charAt(0).toUpperCase() + clean.slice(1);
  }

  function shrinkImage(file) {
    return new Promise(function (resolve, reject) {
      var reader = new FileReader();
      reader.onerror = function () { reject(new Error("read")); };
      reader.onload = function () {
        var img = new Image();
        img.onerror = function () { reject(new Error("decode")); };
        img.onload = function () {
          var w = img.naturalWidth;
          var h = img.naturalHeight;
          var scale = Math.min(1, MAX_DIM / Math.max(w, h));
          var cw = Math.max(1, Math.round(w * scale));
          var ch = Math.max(1, Math.round(h * scale));

          var canvas = document.createElement("canvas");
          canvas.width = cw;
          canvas.height = ch;

          var ctx = canvas.getContext("2d");
          ctx.fillStyle = "#ffffff";
          ctx.fillRect(0, 0, cw, ch);
          ctx.drawImage(img, 0, 0, cw, ch);

          resolve(canvas.toDataURL("image/jpeg", QUALITY));
        };
        img.src = reader.result;
      };
      reader.readAsDataURL(file);
    });
  }

  /* ---------- adding pictures ---------- */

  function addFiles(fileList) {
    var images = [];
    for (var i = 0; i < fileList.length; i++) {
      var f = fileList[i];
      if (f && f.type && f.type.indexOf("image/") === 0) images.push(f);
    }

    if (!images.length) {
      setNote("Those files were not pictures. Please choose JPG, PNG or WEBP images.", true);
      return;
    }

    setNote("Adding " + images.length + (images.length > 1 ? " photos" : " photo") + "\u2026");

    var chain = Promise.resolve();
    images.forEach(function (file) {
      chain = chain.then(function () {
        return shrinkImage(file)
          .then(function (dataUrl) {
            working.push({
              src: dataUrl,
              title: titleFromFileName(file.name),
              category: CATEGORIES[0]
            });
            render();
          })
          .catch(function () {
            /* skip unreadable file */
          });
      });
    });

    chain.then(function () {
      save();
      render();
      setNote(images.length + (images.length > 1 ? " photos added." : " photo added."));
    });
  }

  /* ---------- rendering ---------- */

  function render() {
    grid.innerHTML = "";
    emptyMsg.hidden = working.length > 0;
    countLabel.textContent = working.length ? "(" + working.length + ")" : "";
    downloadBtn.disabled = working.length === 0;

    working.forEach(function (item, index) {
      var card = document.createElement("div");
      card.className = "admin-item";

      var thumb = document.createElement("img");
      thumb.src = item.src;
      thumb.alt = item.title;
      thumb.loading = "lazy";
      card.appendChild(thumb);

      if (!isPublished(item)) {
        var badge = document.createElement("span");
        badge.className = "admin-badge";
        badge.textContent = "New";
        card.appendChild(badge);
      }

      var remove = document.createElement("button");
      remove.type = "button";
      remove.className = "admin-remove";
      remove.setAttribute("aria-label", "Remove " + item.title);
      remove.textContent = "\u00d7";
      remove.addEventListener("click", function () {
        working.splice(index, 1);
        save();
        render();
      });
      card.appendChild(remove);

      var title = document.createElement("input");
      title.type = "text";
      title.className = "admin-input";
      title.value = item.title;
      title.setAttribute("aria-label", "Picture name");
      title.addEventListener("input", function () {
        working[index].title = title.value;
        save();
      });
      card.appendChild(title);

      var select = document.createElement("select");
      select.className = "admin-select";
      select.setAttribute("aria-label", "Picture category");
      CATEGORIES.forEach(function (cat) {
        var option = document.createElement("option");
        option.value = cat;
        option.textContent = cat;
        if (cat === item.category) option.selected = true;
        select.appendChild(option);
      });
      select.addEventListener("change", function () {
        working[index].category = select.value;
        save();
      });
      card.appendChild(select);

      grid.appendChild(card);
    });
  }

  /* ---------- building the new gallery file ---------- */

  function download() {
    var json = JSON.stringify(
      working.map(function (item) {
        return { src: item.src, title: item.title, category: item.category };
      }),
      null,
      2
    );

    fetch("js/portfolio.js", { cache: "no-store" })
      .then(function (response) {
        if (!response.ok) throw new Error("fetch");
        return response.text();
      })
      .then(function (source) {
        var start = "/* == PORTFOLIO DATA START == */";
        var end = "/* == PORTFOLIO DATA END == */";
        var a = source.indexOf(start);
        var b = source.indexOf(end);
        if (a === -1 || b === -1) throw new Error("markers");

        var block = start + "\nvar publishedItems = " + json + ";\n" + end;
        var output = source.slice(0, a) + block + source.slice(b + end.length);
        saveFile(output, "portfolio.js");
        setNote("Gallery file downloaded. Next: upload it to Netlify to replace js/portfolio.js.");
      })
      .catch(function () {
        setNote(
          "Could not build the file automatically. Please open this page through your website (or the Python server) and try again.",
          true
        );
      });
  }

  function saveFile(text, fileName) {
    var blob = new Blob([text], { type: "application/javascript;charset=utf-8" });
    var url = URL.createObjectURL(blob);
    var link = document.createElement("a");
    link.href = url;
    link.download = fileName;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    setTimeout(function () { URL.revokeObjectURL(url); }, 2000);
  }

  /* ---------- events ---------- */

  dropzone.addEventListener("click", function () { fileInput.click(); });

  dropzone.addEventListener("keydown", function (e) {
    if (e.key === "Enter" || e.key === " ") {
      e.preventDefault();
      fileInput.click();
    }
  });

  /* Stop the file dialog's own click from bubbling back into the dropzone. */
  fileInput.addEventListener("click", function (e) {
    e.stopPropagation();
  });

  fileInput.addEventListener("change", function () {
    if (fileInput.files && fileInput.files.length) addFiles(fileInput.files);
    fileInput.value = "";
  });

  ["dragenter", "dragover"].forEach(function (name) {
    dropzone.addEventListener(name, function (e) {
      e.preventDefault();
      dropzone.classList.add("dragging");
    });
  });

  ["dragleave", "drop"].forEach(function (name) {
    dropzone.addEventListener(name, function (e) {
      e.preventDefault();
      dropzone.classList.remove("dragging");
    });
  });

  dropzone.addEventListener("drop", function (e) {
    if (e.dataTransfer && e.dataTransfer.files && e.dataTransfer.files.length) {
      addFiles(e.dataTransfer.files);
    }
  });

  downloadBtn.addEventListener("click", download);

  resetBtn.addEventListener("click", function () {
    if (!window.confirm("Undo all changes made on this page and go back to the photos that are already online?")) {
      return;
    }
    try { localStorage.removeItem(STORAGE_KEY); } catch (e) { /* ignore */ }
    working = base.slice();
    setNote("");
    render();
  });

  render();
})();
"""


# ==========================================================================
#  admin.html
# ==========================================================================
ADMIN_HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Photo Manager | Crossxyreggy Enterprise</title>
  <meta name="robots" content="noindex" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>

  <!-- ===== Header ===== -->
  <header class="site-header">
    <div class="container nav">
      <a href="index.html" class="brand">
        <span class="brand-mark">C</span>
        <span>Crossxyreggy<small>Enterprise</small></span>
      </a>

      <nav class="nav-links" id="navLinks">
        <a href="index.html">Home</a>
        <a href="about.html">About</a>
        <a href="services.html">Services</a>
        <a href="portfolio.html">Our Work</a>
        <a href="contact.html">Contact</a>
        <a href="contact.html" class="btn btn--primary nav-cta">Get a Quote</a>
      </nav>

      <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <!-- ===== Page banner ===== -->
  <section class="page-banner">
    <div class="container">
      <h1>Photo Manager</h1>
      <p>Add pictures of your work to the &ldquo;Our Work&rdquo; gallery &mdash; no coding needed. This page is for the site owner.</p>
      <div class="breadcrumb"><a href="index.html">Home</a> &nbsp;/&nbsp; Photo Manager</div>
    </div>
  </section>

  <!-- ===== Photo manager ===== -->
  <section class="section">
    <div class="container">

      <ol class="admin-steps">
        <li>
          <span>1</span>
          <div>
            <strong>Add your photos</strong>
            <p>Click the box below and pick pictures from your phone or computer.</p>
          </div>
        </li>
        <li>
          <span>2</span>
          <div>
            <strong>Save the gallery file</strong>
            <p>Press &ldquo;Download gallery file&rdquo; to save the updated <code>portfolio.js</code>.</p>
          </div>
        </li>
        <li>
          <span>3</span>
          <div>
            <strong>Put it online</strong>
            <p>On Netlify, replace <code>js/portfolio.js</code> with the file you downloaded. Your photos then show for everyone.</p>
          </div>
        </li>
      </ol>

      <div class="admin-card">
        <h2>1. Add photos</h2>
        <p class="admin-note">Choose several photos at once if you like. Big photos are shrunk automatically so your site stays fast.</p>

        <div class="dropzone" id="dropzone" tabindex="0" role="button" aria-label="Add photos">
          <div class="dropzone-icon">+</div>
          <strong>Click to choose photos</strong>
          <span>or drag &amp; drop them here &middot; JPG, PNG or WEBP</span>
          <input type="file" id="fileInput" accept="image/*" multiple hidden />
        </div>
        <p class="admin-note" id="uploadNote"></p>
      </div>

      <div class="admin-card">
        <div class="admin-card-head">
          <h2>2. Your gallery <small id="countLabel"></small></h2>
          <div class="admin-actions">
            <button class="btn btn--outline btn--sm" id="resetBtn" type="button">Undo all changes</button>
            <button class="btn btn--primary btn--sm" id="downloadBtn" type="button" disabled>Download gallery file</button>
          </div>
        </div>
        <p class="admin-note">Tap the name or category under any picture to change it. Pictures marked <strong>New</strong> are only on this device until you upload the downloaded file.</p>

        <div class="admin-grid" id="adminGrid"></div>
        <p class="admin-empty" id="adminEmpty" hidden>No photos yet. Click the box above to add some.</p>
      </div>

      <div class="admin-tip">
        <strong>Tip:</strong> keep the downloaded <code>portfolio.js</code> file safe. It contains all your pictures, so you can always put them back if you change device.
      </div>

    </div>
  </section>

  <!-- ===== Footer ===== -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-about">
          <a href="index.html" class="brand">
            <span class="brand-mark">C</span>
            <span>Crossxyreggy<small>Enterprise</small></span>
          </a>
          <p>Full-service graphics, branding, printing, signage and marketing solutions for businesses that want to stand out.</p>
          <div class="social-links">
            <a href="https://www.facebook.com/profile.php?id=61578953435664" target="_blank" rel="noopener" aria-label="Facebook">
              <svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Company</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">About Us</a></li>
            <li><a href="services.html">Services</a></li>
            <li><a href="portfolio.html">Our Work</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Services</h4>
          <ul>
            <li><a href="services.html">Graphic Design</a></li>
            <li><a href="services.html">Branding</a></li>
            <li><a href="services.html">Printing</a></li>
            <li><a href="services.html">Signage</a></li>
            <li><a href="services.html">Marketing</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Get in Touch</h4>
          <ul>
            <li><a href="tel:+263715029199">+263 71 502 9199</a></li>
            <li><a href="tel:+263777297024">+263 77 729 7024</a></li>
            <li><a href="tel:+263774327362">+263 77 432 7362</a></li>
            <li><a href="mailto:info.crossxyreggyentstreammedia@gmail.com">info.crossxyreggyentstreammedia@gmail.com</a></li>
            <li><a href="contact.html">Request a Quote</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; <span id="year">2026</span> Crossxyreggy Enterprise. All rights reserved.</p>
        <p>Graphics &middot; Branding &middot; Printing &middot; Signage &middot; Marketing &middot; <a href="admin.html">Site Admin</a></p>
      </div>
    </div>
  </footer>

  <script src="js/main.js"></script>
  <script src="js/portfolio.js"></script>
  <script src="js/admin.js"></script>
</body>
</html>
"""


# ==========================================================================
#  Web server
# ==========================================================================

PAGES = {
    "/": INDEX_HTML,
    "/index.html": INDEX_HTML,
    "/about.html": ABOUT_HTML,
    "/services.html": SERVICES_HTML,
    "/contact.html": CONTACT_HTML,
    "/portfolio.html": PORTFOLIO_HTML,
    "/admin.html": ADMIN_HTML,
}

ASSETS = {
    "/css/style.css": "text/css; charset=utf-8",
    "/js/main.js": "application/javascript; charset=utf-8",
    "/js/portfolio.js": "application/javascript; charset=utf-8",
    "/js/admin.js": "application/javascript; charset=utf-8",
}

ASSET_BODIES = {
    "/css/style.css": STYLE_CSS,
    "/js/main.js": MAIN_JS,
    "/js/portfolio.js": PORTFOLIO_JS,
    "/js/admin.js": ADMIN_JS,
}

MIME_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".gif": "image/gif",
    ".ico": "image/x-icon",
    ".txt": "text/plain; charset=utf-8",
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class WebsiteHandler(BaseHTTPRequestHandler):
    """Serves the built-in pages/assets, plus any real files next to this script."""

    server_version = "CrossxyreggySite/1.0"

    def do_GET(self):
        path = self.path.split("?", 1)[0].split("#", 1)[0]

        # 1) Built-in pages
        if path in PAGES:
            self.send_text(PAGES[path], "text/html; charset=utf-8")
            return

        # 2) Built-in CSS / JS
        if path in ASSET_BODIES:
            self.send_text(ASSET_BODIES[path], ASSETS[path])
            return

        # 3) Optional: real files sitting next to this script (e.g. images/portfolio/)
        if self.try_serve_file(path):
            return

        self.send_error_page(404, "Not Found")

    def do_HEAD(self):
        path = self.path.split("?", 1)[0]
        if path in PAGES:
            body = PAGES[path].encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            return
        self.send_error_page(404, "Not Found")

    def try_serve_file(self, path):
        relative = path.lstrip("/").replace("/", os.sep)
        if not relative:
            return False

        target = os.path.normpath(os.path.join(BASE_DIR, relative))
        if not target.startswith(BASE_DIR):
            return False  # block directory traversal
        if not os.path.isfile(target):
            return False

        ext = os.path.splitext(target)[1].lower()
        ctype = MIME_TYPES.get(ext, "application/octet-stream")
        try:
            with open(target, "rb") as handle:
                data = handle.read()
        except OSError:
            return False

        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)
        return True

    def send_text(self, text, content_type):
        data = text.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        self.wfile.write(data)

    def send_error_page(self, code, message):
        body = (
            "<!DOCTYPE html><html><head><meta charset='utf-8'>"
            "<title>{0} {1}</title></head><body style='font-family:sans-serif;"
            "padding:60px;text-align:center;color:#0d2340'>"
            "<h1 style='font-size:3rem;margin:0'>{0}</h1><p>{1}</p>"
            "<p><a href='/'>Back to home</a></p></body></html>"
        ).format(code, message).encode("utf-8")

        self.send_response(code)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt, *args):
        # Keep the console tidy; comment this out to see every request.
        pass


def main():
    # Cloud hosts (Render, Railway, Fly...) tell the app which port to use
    # through the PORT environment variable. Locally we fall back to the
    # command-line argument, then to the default port.
    env_port = os.environ.get("PORT")
    port = DEFAULT_PORT
    if env_port and env_port.isdigit():
        port = int(env_port)
    elif len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Ignoring invalid port argument:", sys.argv[1])

    # "" / "0.0.0.0" accepts connections from anywhere (needed online).
    host = os.environ.get("HOST", "0.0.0.0")

    url = "http://localhost:{0}/".format(port)

    try:
        httpd = ThreadingHTTPServer((host, port), WebsiteHandler)
    except OSError as exc:
        print("Could not start the server on port {0}: {1}".format(port, exc))
        print("Try another port, e.g.:  python {0} 8080".format(os.path.basename(__file__)))
        return

    print("=" * 62)
    print("  Crossxyreggy Enterprise website is running")
    print("=" * 62)
    print("  Local URL : {0}".format(url))
    print("  Pages     : /  /about.html  /services.html  /portfolio.html  /contact.html")
    print("  Photo tool: {0}admin.html  (add pictures to your gallery)".format(url))
    print("  Stop with : Ctrl + C")
    print("=" * 62)

    # Only pop open a browser for a normal desktop run, not on a cloud server.
    if not env_port:
        threading.Timer(1.0, lambda: webbrowser.open(url)).start()

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped. Goodbye.")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    main()
