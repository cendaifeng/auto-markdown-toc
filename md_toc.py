#
# File: [md_toc.py]
# Author: cendaifeng
# Date：2020-09-09
#
import os
import sys


def init(file_name):
    md = open(file_name, "r", encoding='UTF-8')

    toc_list = ['## 目录\n', '\n']

    is_code = False

    """ read the md line by line """
    for line in md:
        # except code blocks
        if '```' in line:
            is_code = not is_code

        if is_code:
            continue

        """ search all heading """
        if line.startswith('#'):

            # get the heading level
            num = line.count('#')
            toc_title = line[num + 1:].replace('\n', '').strip(' ')

            """ handle the idx to comply the github rules """
            idx = idx_handle(toc_title)

            """ control the indentation and format toc """
            toc_line = ''.join([('  ' * (num - 1)), '- [{0}](#{1})\n'.format(toc_title, idx)])
            toc_list.append(toc_line)

    # turn the iterator to the beginning
    md.seek(0)
    write_file(toc_list, md)
    print('SUCCESS!\n')
    print('**** Created by cendaifeng (https://github.com/cendaifeng/auto-markdown-toc) ****')


def idx_handle(toc_title):
    idx_str = toc_title.lower().replace(' ', '-') \
        .replace('.', '').replace('*', '')\
        .replace('(', '').replace('（', '').replace('[', '').replace('【', '') \
        .replace(')', '').replace('）', '').replace(']', '').replace('】', '') \
        .replace('#', '').replace('?', '')\
        .replace('@', '').replace('$', '').replace('&', '')  # ignore replacement of "_"
    return idx_str


def write_file(toc_list, md_list):
    if len(toc_list) == 2:
        print('==== can not detect any heading in the markdown ====')
        print('...  program EXIT')
        sys.exit(-1)
    else:
        new_file = open(md_name[:md_name.find('.')] + '_with_toc.md', 'w', encoding='UTF-8')
        toc_list.extend(['\n', '<br/>\n', '\n'])
        toc_list.extend(md_list)
        new_file.writelines(toc_list)
        new_file.close()


if __name__ == '__main__':

    try:
        md_name = sys.argv[1]  # input argument（file to analyzing）
    except IndexError:
        print("==== haven`t input a filename after .py ====\n"
              "e.g. \"python md_toc.py MyMD.md\"")
        sys.exit(-1)

    if os.path.exists(md_name):  # whether the file exists
        init(md_name)
    else:
        print('==== ' + md_name + ' is not found in current path ====')
        l = os.listdir(os.getcwd())
        files = []
        for item in l:
            if os.path.isfile(item):
                files.append(item)
        if len(files) > 0:
            print('in this path ONLY:')
            for f in files:
                print(f)
        else:
            print('this path is empty')

