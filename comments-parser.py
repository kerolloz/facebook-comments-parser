#!/usr/bin/python3
import re

file = open('comments_html.txt', 'r')
comments_html = file.read()
comments = re.findall('<span class="UFICommentBody"><span>(.*?)</span>', comments_html)

print(len(comments))
with open('parsed_comments.txt', 'w') as out_file:
    for comment in comments:
        out_file.write("%s, " % comment)
        print(comment)

