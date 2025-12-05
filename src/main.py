import os
import sys
from copy_static import copy_static
from gencontent import generate_pages_recursive

def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    copy_static("static", "docs")
    dir_path_public = "./docs"
    os.makedirs(dir_path_public, exist_ok=True)
    generate_pages_recursive("content", "template.html", dir_path_public, basepath)

if __name__ == "__main__":
    main()
