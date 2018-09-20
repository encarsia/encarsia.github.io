#!/usr/bin/env python
# -*- coding: utf-8 -*-

import conf

import markdown
import os
import subprocess

def get_dir_size(directory):
    total = 0
    counter = 0
    for path, dirs, files in os.walk(directory):
        counter += len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])
        for f in files:
            fp = os.path.join(path, f)
            total += os.path.getsize(fp)
    return sizeof_fmt(total), counter

def nikola_cmd(subcmd):
    cmd = ["nikola"] + subcmd.split()
    output = subprocess.run(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            encoding="utf-8",
                            )
    return output

def sizeof_fmt(num, suffix='B'):
    """File size shown in common units"""
    for unit in ['', 'K', 'M', 'G', 'T', 'P', 'E', 'Z']:
        if abs(num) < 1024.0:
            return "%3.1f %s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f %s%s" % (num, 'Y', suffix)

#print("Site:", get_dir_size("output"))
#print("Files:", get_dir_size("output/files"))
#print("Galleries:", get_dir_size("output/galleries"))
#print("Images:", get_dir_size("output/images"))
#print("Posts:", get_dir_size("posts"))
#print("Pages:", get_dir_size("pages"))

#Folder = namedtuple("Folder", "size count")





# run nikola commands to get information
#status = nikola_cmd("status")
#print(status)
#broken_links = nikola_cmd("check -l")
#print(broken_links)
#broken_files = nikola_cmd("check -f")
#print(broken_files)
#themes_installed = nikola_cmd("theme --list-installed")
#print(themes_installed)
#themes_available = nikola_cmd("theme -l")
#print(themes_available)
#plugins_installed = nikola_cmd("plugin --list-installed")
#print(plugins_installed)
#plugins_available = nikola_cmd("plugin -l")
#print(plugins_available)
#shortcodes = [name for name in os.listdir("shortcodes") if os.path.isfile(os.path.join("shortcodes", name))])
#print(shortcodes)

def get_diskusage_string(folders):
    string = """Name | Size | Files
--- | --- | ---
"""
    for name, folder in folders:
        s, c = get_dir_size(folder)
        #infodict[name] = {"size": s, "files": c}
        string += """{} | {} | {}\n""".format(name, s, c)
    return string

template = """
# Title
{disk_usage}
## sub

text

## sub 2

* list item
* another list item
"""
# read template from file
infodict = dict()


folders = [("Site", "output"),
           ("Files", "output/files"),
           ("Galleries", "output/galleries"),
           ("Images", "output/images"),
           ("Posts", "posts"),
           ("Pages", "pages"),
           ]
           
#infodict["disk_usage"] = get_diskusage_string(folders)
#infodict["status"] = nikola_cmd("status").stdout.split("\n")[1].split(",")[0]

broken_links = nikola_cmd("check -l")
print(broken_links)

#txt = template.format(**infodict)
#html = markdown.markdown(txt, extensions=["markdown.extensions.tables"])
#print(html)
#with open("info.html", "w") as f:
#    f.write(html)



