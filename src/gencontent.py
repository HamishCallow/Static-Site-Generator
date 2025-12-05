import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines =  markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            return title
    raise Exception("Invalid markdown: no h1 header")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        from_content = f.read()
    with open(template_path) as f:
        template_content = f.read()
    html_node = markdown_to_html_node(from_content)
    html_string = html_node.to_html()
    title = extract_title(from_content)
    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_string)
    template_content = template_content.replace('href="/', f'href="{basepath}')
    template_content = template_content.replace('src="/', f'src="{basepath}')
    dirname = os.path.dirname(dest_path)
    os.makedirs(dirname, exist_ok=True)
    with open(dest_path, mode="w") as f:
        f.write(template_content)

def generate_pages_recursive(dir_path_content, template_file, dest_dir_path, basepath):
    for entry_name in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, entry_name)
        dest_dir_for_entry = os.path.join(dest_dir_path, entry_name)
        src_path_obj = Path(src_path)
        output_html_path = (Path(dest_dir_path) / src_path_obj.name).with_suffix(".html")
        if os.path.isfile(src_path) and src_path.endswith(".md"):
            generate_page(src_path, template_file, output_html_path, basepath)
        elif os.path.isdir(src_path):
            os.makedirs(dest_dir_for_entry, exist_ok=True)
            generate_pages_recursive(src_path, template_file, dest_dir_for_entry, basepath)






