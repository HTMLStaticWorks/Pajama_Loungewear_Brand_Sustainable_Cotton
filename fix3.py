import glob, re, os

project_dir = r'c:\Users\Shalani A\Documents\Shalan\Client projects(MAY)\Pajama & Loungewear Brand'

# Update HTML files
for root, _, files in os.walk(project_dir):
    for filename in files:
        if filename.endswith('.html'):
            f = os.path.join(root, filename)
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Replace globe icon with text 'RTL'
            content = re.sub(
                r'<button class="icon-btn rtl-toggle"[^>]*>.*?<i class="fas fa-globe"></i>.*?</button>', 
                r'<button class="icon-btn rtl-toggle" title="Switch Direction">RTL</button>', 
                content
            )
            
            # Also clean up any inline styles on rtl-toggle since we will handle it in CSS
            content = re.sub(
                r'<button class="icon-btn rtl-toggle" style="[^"]*">RTL</button>', 
                r'<button class="icon-btn rtl-toggle" title="Switch Direction">RTL</button>', 
                content
            )
            
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)

# Update style.css
css_path = os.path.join(project_dir, 'assets', 'css', 'style.css')
with open(css_path, 'r', encoding='utf-8') as file:
    css_content = file.read()

# Add border-radius to .btn
if 'border-radius: 50px;' not in css_content.split('.btn {')[1].split('}')[0]:
    css_content = css_content.replace('.btn {\n', '.btn {\n    border-radius: 50px;\n')

# Add specific styles for the text-based rtl-toggle
rtl_style = '''
.icon-btn.rtl-toggle {
    font-size: 0.8rem;
    font-weight: 700;
    width: auto;
    padding: 0 15px;
    border-radius: 50px;
}
'''
if '.icon-btn.rtl-toggle' not in css_content:
    css_content += rtl_style

with open(css_path, 'w', encoding='utf-8') as file:
    file.write(css_content)

print('Done')
