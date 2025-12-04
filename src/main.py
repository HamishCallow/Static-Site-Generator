import os
from copy_static import copy_static
from gencontent import generate_pages_recursive

def main():
    copy_static("static", "public")
    output_dir = "public"
    os.makedirs(output_dir, exist_ok=True)
    generate_pages_recursive("content", "template.html", output_dir)

if __name__ == "__main__":
    main()
