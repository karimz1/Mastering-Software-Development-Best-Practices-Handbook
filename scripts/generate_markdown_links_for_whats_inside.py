"""
This script is a convenient tool for generating Table of Contents sections in markdown files.
It effectively extracts h2 headers and generates markdown links for them, making it easy to navigate through a document. 
"""

from pathlib import Path

def get_h2_links(markdown_text):
    lines = markdown_text.split('\n')
    links = []
    for line in lines:
        if line.startswith('## '):
            header_name = line[3:]  # remove '## ' from the start of the line
            link_id = header_name.replace(' ', '-').lower()  # convert to lowercase and replace spaces with hyphens
            link = f"- [{header_name}](#{link_id})"
            links.append(link)
    return links

def main():
    fpath = "../ReadMe.md"
    content = Path(fpath).read_text(encoding='utf-8')

    print("Display Generated Markdown links for: \"What's Inside\"\n\n")
    for link in get_h2_links(content):
        print(link)


if(__name__ == "__main__"):
    main()
    