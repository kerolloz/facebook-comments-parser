import re

file = open('comments.txt', 'r')
comments_html = file.read()
handles = re.findall('<span class="UFICommentBody"><span>(.*?)</span>', comments_html)

print(len(handles))
with open('handles_special_training.txt', 'w') as out_file:
    for handle in handles:
        out_file.write("%s, " % handle)
        print(handle)

