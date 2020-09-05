import re

md = open("mdtoop.md", "rt+", encoding='UTF-8')
toc_list = []
""" read the md """
for line in md:
    # print(line, end='')
    """ search all heading """
    if line.startswith('#'):  # re.match('#', line)
        # findall() will return a list, we get its length
        # num = re.findall('#', line).__len__()
        num = line.count('#')
        toc_name = line[num+1:].replace('\n', '').strip(' ')
        """ handle the idx to comply the github rules"""
        idx_str = toc_name.lower().replace(' ', '-')\
            .replace('.', '').replace('*', '').replace('(', '').replace('（', '').replace('[', '').replace('【', '')\
            .replace(')', '').replace('）', '').replace(']', '').replace('】', '')  # ignore replacement of "_"
        """control the indentation and format toc"""
        toc_line = ''.join([('  '*(num-1)), '- [{0}](#{1})\n'.format(toc_name, idx_str)])
        toc_list.append(toc_line)

# I can only write them in the end
md.writelines(toc_list)
md.close()
