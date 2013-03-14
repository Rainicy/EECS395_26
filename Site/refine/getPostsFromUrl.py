#  Author: Alex Madjar
#  Scrapes comments from CNN articles
#  Main function is getPostsFromUrl(url)

import urllib2
import urllib
import json

# Top level "get everything" function
# Returns a filtered list of dictionaries (posts)
# Each dictionary corresponds to a comment
# And contains:
#   -  "raw_message" - the comment (original)
def getPostsFromUrl(url):
  return filterPosts(cnnurlToAllPostsList(url))

# TODO: Better way to hide this?
disqus_private_key = 'wMzRaAsqBKB8ClrS0Ri1dnZVC0GMVgoxnCN0DbUKYzQM0vYWdNcMJCYwbZO68nSY'
disqus_url = 'http://disqus.com/api/3.0/threads/listPosts.json?api_secret={0!s}&limit=100&thread=link:{1!s}&forum=cnn'
disqus_next_url = disqus_url + "&cursor={2!s}"


def getFirstPage(url):
  durl = disqus_url.format(disqus_private_key, urllib.quote_plus(url))
  return run_durl(durl)

def run_durl(durl):
  try:
    socket = urllib2.urlopen(durl)
    raw_json = socket.read()
    socket.close()
  except (urllib2.HTTPError):
  	return json.loads('{"code":400}')
  parsed_json = json.loads(raw_json)
  return parsed_json

def getNextPage(url, n):
  durl = disqus_next_url.format(disqus_private_key, urllib.quote_plus(url), n)
  return run_durl(durl)

def cnnurlToAllPostsList(url):
  json = getFirstPage(url)
  if json['code'] != 0:
    return list()
  allposts = json['response']
  pages = 10
  while (json['code'] == 0) and (json['cursor']['hasNext']) and (pages > 0):
    json = getNextPage(url, json['cursor']['next'])
    allposts.extend(json['response'])
    pages = pages - 1
  return allposts

def isTopLevelPost(post):
    return post["parent"] == None

def isLongPost(post):
    return len(post["raw_message"]) >= 75

# filters:  replies, short posts 
# feel free to comment out filters to leave those posts
def filterPosts(posts_list):
  filtered_list = posts_list
  # filtered_list = filter(isTopLevelPost, filtered_list)
  filtered_list = filter(isLongPost, filtered_list)
  filtered_list = filter(lambda p: not(p["isDeleted"]), filtered_list)
  filtered_list = filter(lambda p: not(p["isSpam"]), filtered_list)
  filtered_list = dedupePosts(filtered_list)
  return filtered_list

def dedupePosts(posts):
  deduped = []
  messages = set()
  for p in posts:
    if p["raw_message"] not in messages:
      messages.add(p["raw_message"])
      deduped.append(p)
  return deduped


cnnurl = 'http://www.cnn.com/2012/05/02/justice/florida-famu-charges/index.html'

def updateExamplePostsFile():
  f = open('examplePosts.py','w')
  f.write('posts=')
  posts = getPostsFromUrl(cnnurl)
  f.write(str(posts))
  f.close()


def runQuickTest():
  # testing url
  import time
  t = time.time()
  g = getPostsFromUrl(cnnurl)
  t = 'It took {} seconds to fetch {} posts'.format(
                                      time.time()-t, len(g))
  print t
  print ''
  print 'An example post object:'
  print g[0]

if __name__ == '__main__':
    runQuickTest()

