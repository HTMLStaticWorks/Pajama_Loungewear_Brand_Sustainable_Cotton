import re, os

BASE = r'c:\Users\Shalani A\Documents\Shalan\Client projects(MAY)\Pajama & Loungewear Brand'

# ─────────────────────────────────────────────
# 1. CSS FIXES — remove black border, unify btn
# ─────────────────────────────────────────────
css_path = os.path.join(BASE, 'assets', 'css', 'style.css')
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Ensure global button reset exists (add after :root block ends)
reset = '''
/* ── Global button / link reset ── */
button, input[type="submit"], input[type="button"] {
    -webkit-appearance: none;
    appearance: none;
    border: none;
    outline: none;
    cursor: pointer;
    font-family: var(--font-main);
}

a.btn, a[class*="btn-"] {
    text-decoration: none;
    outline: none;
}
'''
if '/* ── Global button / link reset ── */' not in css:
    css = css.replace('/* Base Styles */', reset + '\n/* Base Styles */')

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)
print('CSS reset injected.')


# ─────────────────────────────────────────────
# 2. HTML CHANGES per file
# ─────────────────────────────────────────────

# Reusable CTA block builder
def cta_section(dark=True, heading='', subtext='', btn1_href='', btn1_label='', btn2_href='', btn2_label=''):
    bg = 'var(--text-dark)' if dark else 'var(--primary-light)'
    color = 'var(--white)' if dark else 'var(--text-dark)'
    opacity = '0.75' if dark else '0.65'
    btn2_class = 'btn btn-outline' if dark else 'btn btn-outline-primary'
    btn2_html = f'<a href="{btn2_href}" class="{btn2_class}">{btn2_label}</a>' if btn2_href else ''
    return f'''
    <!-- ── CTA Banner ── -->
    <section style="background: {bg}; color: {color}; text-align: center; padding: 80px 0;">
        <div class="container">
            <div class="reveal-up">
                <h2 style="margin-bottom: 15px;">{heading}</h2>
                <p style="opacity: {opacity}; max-width: 560px; margin: 0 auto 35px; font-size: 1.05rem;">{subtext}</p>
                <div style="display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
                    <a href="{btn1_href}" class="btn btn-primary">{btn1_label} <i class="fas fa-arrow-right" style="margin-left: 8px;"></i></a>
                    {btn2_html}
                </div>
            </div>
        </div>
    </section>
'''

# ── home-2.html ──
path = os.path.join(BASE, 'home-2.html')
with open(path, 'r', encoding='utf-8') as f: html = f.read()

# 1. New Arrivals section — add View All CTA
if 'View All New Arrivals' not in html:
    html = html.replace(
        '</div>\n        </div>\n    </section>\n\n    <!-- 3. Sleepwear Categories',
        '</div>\n            <div class="section-cta reveal-up"><a href="pages/shop.html" class="btn btn-primary">View All New Arrivals <i class="fas fa-arrow-right" style="margin-left:8px;"></i></a></div>\n        </div>\n    </section>\n\n    <!-- 3. Sleepwear Categories'
    )

# 2. Shop by Category — add CTA links on each category card
if 'Shop Loungewear' not in html:
    html = html.replace(
        '<div class="category-overlay">\n                        <h3 style="color: white; font-size: 2rem;">Loungewear</h3>\n                    </div>',
        '<div class="category-overlay" style="flex-direction:column;gap:15px;">\n                        <h3 style="color: white; font-size: 2rem;">Loungewear</h3>\n                        <a href="pages/shop.html" class="btn btn-outline" style="font-size:0.85rem;height:38px;padding:0 20px;">Shop Loungewear</a>\n                    </div>'
    )
    html = html.replace(
        '<div class="category-overlay">\n                        <h3 style="color: white; font-size: 2rem;">Sleepwear</h3>\n                    </div>',
        '<div class="category-overlay" style="flex-direction:column;gap:15px;">\n                        <h3 style="color: white; font-size: 2rem;">Sleepwear</h3>\n                        <a href="pages/shop.html" class="btn btn-outline" style="font-size:0.85rem;height:38px;padding:0 20px;">Shop Sleepwear</a>\n                    </div>'
    )

# 3. Care section — upgrade discover-link to btn
html = html.replace(
    '<a href="pages/care-instructions.html" class="discover-link" style="margin-top: 40px;">Full Care Guide</a>',
    '<div style="margin-top:40px;"><a href="pages/care-instructions.html" class="btn btn-primary">Full Care Guide <i class="fas fa-arrow-right" style="margin-left:8px;"></i></a></div>'
)

with open(path, 'w', encoding='utf-8') as f: f.write(html)
print('home-2.html updated.')


# ── index.html ──
path = os.path.join(BASE, 'index.html')
with open(path, 'r', encoding='utf-8') as f: html = f.read()

# Fabric / Sustainable section CTA (section 3) — already has btn-primary, check it
# Testimonials section — add CTA after testimonial grid if missing
if 'Start Shopping' not in html and 'section-cta' not in html.split('<!-- 5. Testimonials')[1].split('<!-- 6')[0]:
    html = html.replace(
        '</div>\n        </div>\n    </section>\n\n    <!-- 6. CTA Section',
        '</div>\n            <div class="section-cta reveal-up" style="margin-top:40px;"><a href="pages/shop.html" class="btn btn-primary">Start Shopping <i class="fas fa-arrow-right" style="margin-left:8px;"></i></a></div>\n        </div>\n    </section>\n\n    <!-- 6. CTA Section'
    )

with open(path, 'w', encoding='utf-8') as f: f.write(html)
print('index.html updated.')


# ── faq.html ──
path = os.path.join(BASE, 'pages', 'faq.html')
with open(path, 'r', encoding='utf-8') as f: html = f.read()

# Add Contact Us CTA below "Still have questions?" sustainability block
if 'Contact Our Team' not in html:
    html = html.replace(
        '<a href="fabric-story.html" class="btn btn-primary" style="margin-top: 30px;">Sustainability Report</a>',
        '<div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:30px;"><a href="fabric-story.html" class="btn btn-primary">Sustainability Report <i class="fas fa-arrow-right" style="margin-left:8px;"></i></a><a href="contact.html" class="btn btn-outline-primary">Contact Our Team</a></div>'
    )

with open(path, 'w', encoding='utf-8') as f: f.write(html)
print('faq.html updated.')


# ── about.html ──
path = os.path.join(BASE, 'pages', 'about.html')
with open(path, 'r', encoding='utf-8') as f: html = f.read()

# Add Shop CTA alongside existing Join the Journey btn if missing
if 'Explore Our Collections' not in html:
    html = html.replace(
        '<a href="fabric-story.html" class="btn btn-primary">Join the Journey</a>',
        '<div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;"><a href="fabric-story.html" class="btn btn-primary">Join the Journey <i class="fas fa-arrow-right" style="margin-left:8px;"></i></a><a href="shop.html" class="btn btn-outline-primary">Explore Our Collections</a></div>'
    )

with open(path, 'w', encoding='utf-8') as f: f.write(html)
print('about.html updated.')


# ── collection-details.html ──
path = os.path.join(BASE, 'pages', 'collection-details.html')
with open(path, 'r', encoding='utf-8') as f: html = f.read()

# Add CTA after hero (hero has no CTA currently)
if 'Shop This Collection' not in html:
    html = html.replace(
        '<p>Weightless comfort for warm summer nights.</p>\n        </div>\n    </section>',
        '<p>Weightless comfort for warm summer nights.</p>\n            <div class="hero-btns" style="margin-top:30px;"><a href="shop.html" class="btn btn-primary">Shop This Collection</a><a href="../index.html" class="btn btn-outline" style="margin-left:14px;">Back to Home</a></div>\n        </div>\n    </section>'
    )

with open(path, 'w', encoding='utf-8') as f: f.write(html)
print('collection-details.html updated.')


# ── size-guide.html ──
path = os.path.join(BASE, 'pages', 'size-guide.html')
with open(path, 'r', encoding='utf-8') as f: html = f.read()
# Add a second CTA alongside existing one if missing
if 'View All Collections' not in html:
    html = html.replace(
        '<a href="contact.html" class="btn btn-primary" style="margin-top: 30px;">Chat with a Specialist</a>',
        '<div style="display:flex;gap:14px;justify-content:center;flex-wrap:wrap;margin-top:30px;"><a href="contact.html" class="btn btn-primary">Chat with a Specialist <i class="fas fa-arrow-right" style="margin-left:8px;"></i></a><a href="shop.html" class="btn btn-outline-primary">View All Collections</a></div>'
    )
with open(path, 'w', encoding='utf-8') as f: f.write(html)
print('size-guide.html updated.')


print('\n✅ All CTA fixes applied successfully.')
