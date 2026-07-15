import os
import csv
import re

def sanitize_filename(name):
    # Remove invalid path characters
    return re.sub(r'[\\/*?:"<>|]', "", name).replace(" ", "_")

def html_to_md(html_str):
    if not html_str: return ""
    
    # Strip the bounding html/body tags
    md = re.sub(r'</?(html|body)>', '', html_str, flags=re.IGNORECASE)
    
    # Convert standard HTML layout tags to Markdown equivalents
    md = re.sub(r'<h1>(.*?)</h1>', r'# \1\n\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<h2>(.*?)</h2>', r'## \1\n\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<h3>(.*?)</h3>', r'### \1\n\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<p>(.*?)</p>', r'\1\n\n', md, flags=re.IGNORECASE)
    md = re.sub(r'</?(b|strong)>', '**', md, flags=re.IGNORECASE)
    md = re.sub(r'</?(i|em)>', '*', md, flags=re.IGNORECASE)
    md = re.sub(r'<ul>(.*?)</ul>', r'\n\1\n', md, flags=re.IGNORECASE)
    md = re.sub(r'<li>(.*?)</li>', r'* \1\n', md, flags=re.IGNORECASE)
    
    # Clean up excess line breaks caused by regex replacements
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()

def generate_markdown_docs():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(script_dir, 'Component_Data.csv')
    docs_dir = os.path.join(script_dir, 'docs')

    os.makedirs(docs_dir, exist_ok=True)

    categories = set()
    category_order = 1

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        headers = reader.fieldnames
        
        for row in reader:
            full_name = row.get('Full Name', '').strip()
            if not full_name: continue
                
            category = row.get('Category', '').strip()
            if not category: category = "Uncategorized"
                
            short_desc = row.get('Short Description', '').strip()
            help_desc = row.get('Help Description', '').strip()
            md_help = html_to_md(help_desc)
            
            # 1. Manage Category Folder and Index files for Just-the-docs
            cat_dir = os.path.join(docs_dir, category)
            if category not in categories:
                categories.add(category)
                os.makedirs(cat_dir, exist_ok=True)
                
                index_path = os.path.join(cat_dir, 'index.md')
                with open(index_path, 'w', encoding='utf-8') as idx_f:
                    idx_f.write(f"---\nlayout: default\ntitle: \"{category}\"\nhas_children: true\nnav_order: {category_order}\n---\n\n# {category}\n\nThis section contains a range of customisable {category} components.\n")
                category_order += 1
            
            # 2. Extract Inputs
            inputs = []
            i = 1
            while f'Input {i} Full Name' in headers:
                inp_name = row.get(f'Input {i} Full Name', '').strip()
                inp_desc = row.get(f'Input {i} Desc', '').strip()
                if inp_name: inputs.append((inp_name, inp_desc))
                i += 1
                
            # 3. Extract Outputs
            outputs = []
            j = 1
            while f'Output {j} Full Name' in headers:
                out_name = row.get(f'Output {j} Full Name', '').strip()
                out_desc = row.get(f'Output {j} Desc', '').strip()
                if out_name: outputs.append((out_name, out_desc))
                j += 1
                
            # 4. Extract Menus
            menus = []
            k = 1
            while f'Menu {k} Name' in headers:
                menu_name = row.get(f'Menu {k} Name', '').strip()
                if menu_name: menus.append(menu_name)
                k += 1

            # 5. Construct Markdown Content
            md_content = f"---\nlayout: default\ntitle: \"{full_name}\"\nparent: \"{category}\"\n---\n\n# {full_name}\n\n#### {short_desc}\n\n"
            
            if md_help: md_content += f"{md_help}\n\n"
            
            if inputs:
                md_content += "___\n\n### Inputs\n"
                for name, desc in inputs: md_content += f"**{name}**\n{desc}\n\n"
                    
            if outputs:
                md_content += "___\n\n### Outputs\n"
                for name, desc in outputs: md_content += f"**{name}**\n{desc}\n\n"
                    
            if menus:
                md_content += "___\n\n### Menu Options\n"
                for name in menus: md_content += f"**{name}**\n\"Explanation...\"\n\n"
            
            # 6. Write to File
            file_name = sanitize_filename(full_name) + '.md'
            file_path = os.path.join(cat_dir, file_name)
            
            with open(file_path, 'w', encoding='utf-8') as md_f:
                md_f.write(md_content.strip() + '\n')
                
    print(f"Documentation extraction complete. Files generated in: {docs_dir}")

if __name__ == '__main__':
    generate_markdown_docs()