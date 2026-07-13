import os
import re

def insert_component_icons(docs_dir="docs", images_dir="images"):
    # Cache available images to validate links and handle naming anomalies
    if not os.path.exists(images_dir):
        print(f"Error: Could not find '{images_dir}' directory.")
        return
        
    available_images = set(os.listdir(images_dir))
    
    # Walk through the docs directory
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.lower() == "index.md" or not file.endswith(".md"):
                continue
                
            filepath = os.path.join(root, file)
            basename = os.path.splitext(file)[0]
            
            # Normalize filename for image mapping (Space/Hyphen to Underscore)
            safe_name = basename.replace(" ", "_").replace("-", "_")
            image_name = f"{safe_name}_400.png"
            
            # Handle naming inversions present in the tree (e.g., 'Arc Arrow' -> 'Arrow_Arc_400.png')
            if image_name not in available_images:
                parts = safe_name.split('_')
                if len(parts) == 2:
                    reversed_name = f"{parts[1]}_{parts[0]}_400.png"
                    if reversed_name in available_images:
                        image_name = reversed_name
                    else:
                        print(f"[WARNING] Missing image for '{file}': Checked for '{image_name}' & '{reversed_name}'")
                else:
                    print(f"[WARNING] Missing image for '{file}': Checked for '{image_name}'")
                    
            # Compute correct relative path from the current markdown file to the images folder
            rel_image_path = os.path.relpath(images_dir, root).replace('\\', '/')
            img_src = f"{rel_image_path}/{image_name}"
            
            img_tag = f'\n<img width="200" height="200" alt="{basename} component icon" src="{img_src}" />\n'
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Idempotency check: skip if this file already has the icon tag injected
            if '<img width="200"' in content and f'src="{img_src}"' in content:
                continue
                
            # Regex targets the primary H1 header at the start of a line
            pattern = re.compile(r'^(#\s+.*)$', re.MULTILINE)
            match = pattern.search(content)
            
            if match:
                # Splice the image tag immediately following the H1 header
                new_content = content[:match.end()] + "\n" + img_tag + content[match.end():]
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"[SUCCESS] Injected icon into: {filepath}")
            else:
                print(f"[WARNING] No H1 header ('# Title') found in: {filepath}")

if __name__ == "__main__":
    insert_component_icons()