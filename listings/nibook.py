#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import glob

GHP = '/path/to//GitHub/Page'
DL_DIR = '/relpath/to/dlfolder'

POSTS = []
SPHDIR = os.getcwd()
META = '''.. meta::
   :http-equiv=Content-Type: text/html; charset=UTF-8

'''

def collect_posts():
    #get posts
    with open('index.lst') as f:
        lines = f.readlines()
    for line in lines:
        if not line.strip('\n') == '':
            POSTS.append(line.strip('\n')+'.rst')
    print('Posts collected...')
    
def copy_posts():
    #copy posts into /posts folder
    #TODO copy only if file has been changed since last run
    if not os.path.exists(SPHDIR+'/posts'):
        os.makedirs(SPHDIR+'/posts')
    for post in POSTS:
        shutil.copy2('{}/posts/{}'.format(GHP, post),'posts')
    print('Posts copied to Sphinx folder...')

def create_index():
    #insert post filenames to index template and save as index.rst
    with open('index.tmpl') as f:
        lines = f.readlines()
    pos =lines.index('    .. include-start\n')
    del lines[pos]
    for post in reversed(POSTS):
        lines.insert(pos, '    posts/{}\n'.format(post[:-4]))
    with open('index.rst', 'w') as f:
        f.writelines(lines)
    ('Index.rst generated from template...')

def sph_title(src):
    #convert title comment to chapter, position is always line 1
    #convert Nikola slugs into internal reference, position is always line 2 but title function inserts 3
    #insert meta tag for correct encoding when running kindlegen
    title = src[0][10:].strip()
    src.insert(0,'{}\n'.format(title))
    src.insert(0,'{}\n'.format('*'*len(title)))
    src.insert(2,'{}\n'.format('*'*len(title)))
    slug = src[4].split()[2]
    ref = '.. _{}:\n\n'.format(slug)
    src.insert(0,ref)
    src.insert(0, META)

def sph_edit(src):
    #delete unwanted content like table of contents
    #convert custom Nikola directives thumbnail and listing to image and literalinclude
    #use original files and images with Sphinx, demands relative paths
    #delete custom G+ link, this won't work if you use the raw directive in any other way
    for pos, line in enumerate(src):
        if line.startswith(del_lines):
            del src[pos]
        elif line.startswith('.. thumbnail::') or line.startswith('.. image::'):
            del src[pos]
            new_line = '.. image:: ../{}{}\n'.format(os.path.relpath(GHP), line.split()[2])
            src.insert(pos, new_line)
        elif line.startswith('.. listing::'):
            del src[pos]
            filename, lang = line.split()[2], line.split()[3]
            new_line = '.. literalinclude:: ../{}/listings/{}\n'.format(os.path.relpath(GHP), filename)
            src.insert(pos, new_line)
            new_line = '    :language: {}\n'.format(lang)
            src.insert(pos+1, new_line)
        ### !!! Delete the following if statement if you use the raw directive !!!
        elif line.startswith('.. raw:: html'):
            for x in range(4):
                del src[pos]

def sph_deslug(src):
    '''convert internal links using slug into working internal link
        Example:    in:  `description <link://slug/thisisit>`_
                    out: `description <filenameofslugorigin.xhtml#thisisit>`_
            
            normally slug == filename but sometimes things aren't normal
            this example only works with epub builder, links are broken with LaTeX builder
            
            probably the easiest way is to format links to
                    out: description (:ref:`thisisit`)
            because the references have already been set in sph_title function
            the only (cosmetic) issue is the link text being separated from the link
            
            that'll do
            
        Explanation of string splits:
                    
                    Sentence with a `slugified link <link://slug/thisisit>`_.
            1)'>`_' [0]                                                  |  |[1] post
            2)' <'  [0]                            ||[1]                 |-----------
            3)'`'   [0] pre        ||[1] descr      |--------------------|-----------
            4)'/'   -------------------------------||[0]  ||[2] |[3] ref |-----------
    '''
    for pos, line in enumerate(src):
        while '<link://slug/' in line:
            split1 = line.split('>`_', 1)   #always process first link
            split2 = split1[0].split(' <')
            split3 = split2[0].split('`')
            split4 = split2[1].split('/')
            pre = split3[0]
            descr = split3[1]
            ref = split4[3]
            post = split1[1]
            line = '{} {} (:ref:`{}`){}'.format(pre, descr, ref, post)
            del src[pos]
            src.insert(pos, line)

if __name__ == "__main__":

    collect_posts()
    copy_posts()
    create_index()
    ##########   prepare rst source files for Sphinx  ###########
    for post in POSTS:
        #read source file into string variable
        with open('posts/'+post) as f:
            nikola_source = f.readlines()

        sph_title(nikola_source)
        
        #tuple of strings to select for deletion
        del_lines = ('.. class::',
                    '.. contents::')
        sph_edit(nikola_source)
        sph_deslug(nikola_source)

        #write edited source code into file 
        with open('posts/'+post, 'w') as f:
            f.writelines(nikola_source)
        print('File ({}) prepared...'.format(post))
    ##############################################################
    print('Ready for Sphinx.')

    while 1:
        print()
        cmd = input("Run Sphinx epub builder? (Y/n) ")
        if cmd == 'n':
            break
        elif cmd == 'y' or cmd == 'j' or cmd == '':
            subprocess.run(['make','clean','epub'])
            break
        else:
            print("Invalid input. Try again...")

    while 1:
        print()
        cmd = input("Run Sphinx latex builder? (Y/n) ")
        if cmd == 'n':
            break
        elif cmd == 'y' or cmd == 'j' or cmd == '':
            subprocess.run(['make','latexpdf'])
            break
        else:
            print("Invalid input. Try again...")

    while 1:
        print()
        cmd = input("Run KindleGen? (Y/n) ")
        if cmd == 'n':
            break
        elif cmd == 'y' or cmd == 'j' or cmd == '':
            os.chdir('_build/epub')
            subprocess.run(['kindlegen',glob.glob('*.epub')[0]])
            break
        else:
            print("Invalid input. Try again...")

    while 1:
        print()
        cmd = input("Copy files to download directory? (Y/n) ")
        if cmd == 'n':
            break
        elif cmd == 'y' or cmd == 'j' or cmd == '':
            shutil.copy2(glob.glob('*.epub')[0], GHP+DL_DIR)
            shutil.copy2(glob.glob('*.mobi')[0], GHP+DL_DIR)
            os.chdir('../latex')
            shutil.copy2(glob.glob('*.pdf')[0], GHP+DL_DIR)
            break
        else:
            print("Invalid input. Try again...")

    while 1:
        print()
        cmd = input("Deploy files to GitHub Page? (Y/n) ")
        if cmd == 'n':
            break
        elif cmd == 'y' or cmd == 'j' or cmd == '':
            os.chdir(GHP)
            subprocess.run(['nikola','build'])
            subprocess.run(['nikola','github_deploy']) 
            break
        else:
            print("Invalid input. Try again...")

    print('\nThis is the end.')