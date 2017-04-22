import urllib2
import json

import sys
sys.path.append('..')
from item.models import item

class Spider():
    url = "https://hacker-news.firebaseio.com/v0/"

    def __init__(self):
        pass

    def get_top(self):
        top_url = self.url+"topstories.json"
        op = urllib2.urlopen(top_url)
        top_list = json.loads(op.read())
        return top_list

    def get_stories(self, stories_list):
        for sto_num in stories_list:
            sto_url = self.url + "item/" + str(sto_num) + ".json"
            op = urllib2.urlopen(sto_url)
            struct_str = json.loads(op.read())
            # print struct_str
            # self.save_to(str(struct_str), "top_list")

    def save_to(self, content, filename):
        f = open(filename, 'w')
        f.write(content)

    def read_from(self, filename):
        f = open(filename)
        return f.read()

    def get_comment(self):
        pass

    def get_user(self):
        pass

    def save_one_story(self):
        # i = item()
        pass

    def start(self):
        top_list = self.get_top()
        self.get_stories(top_list)

if __name__ == "__main__":

    spider = Spider()
    # spider.get_top()
    spider.start()
