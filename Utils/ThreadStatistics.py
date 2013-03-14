import heapq
import extractNgrams as e

# in case I forget
NULL = nil = None

# Returns a list of 2-tuples
# [((nGram tuple)),COUNT),...] x N
def mostCommonNGramsFromPosts(posts, N=12):
    # Basic Algorithm:
    for p in posts:
      n = e.normalizeString(p["raw_message"])
      p["unigrams"] = e.nGramsFromString(n,1)
      p["bigrams"] = e.nGramsFromString(n,2)
      p["trigrams"] = e.nGramsFromString(n,3)
      p["normalized_string"] = n
    # count unigrams and bigrams
    common = lambda s: nCommonNgrams(countNgrams(posts, s),N)
    return [common("unigrams"), common("bigrams"), common("trigrams")]

def findPostsContaining(posts, token):
    ret = []
    for p in posts:
        if p["normalized_string"].find(token) > -1:
            ret.append(p["raw_message"])
    return ret

def mostCommonNGramsFromString(string, N=8):
    n = e.normalizeString(string)
    nGrams = [1,2,3]
    nGrams = map(lambda a: e.nGramsFromString(n,a),nGrams)
    count = [{},{},{}]
    for i in [0,1,2]:
        for gram in nGrams[i]:
            count[i][gram] = count[i].get(gram,0) + 1
        count[i] = flipDictionary(count[i])
        print(nCommonNgrams(count[i],N))
    return nGrams
    

# returns a list of tuples (string tuples, count)
def nCommonNgrams(nGramsCount, N):
    # a dictionary mapping counts to nGrams
    mostCommonNgrams = []
    for c in heapq.nlargest(N, nGramsCount.keys()):
        mostCommonNgrams.extend(zip(nGramsCount[c], [c for _ in xrange(len(nGramsCount[c]))]))
    return mostCommonNgrams[0:N] # ensure it's not too long

def countNgrams(posts, gram_string="unigrams"):
    # returns: {count: [word,...], ...}
    grams = {}
    for post in posts:
        dedupe = set(post[gram_string])
        for gram in dedupe:
            grams[gram] = grams.get(gram, 0) + 1
    return flipDictionary(grams)


def flipDictionary(d):
    inv_map = {}
    for k,v in d.iteritems():
        inv_map[v] = inv_map.get(v, [])
        inv_map[v].append(k)
    return inv_map

def nGramsListToTokenStringsList(l):
    ret = []
    for n,c in l:
        ret.append(tuple([nGramsToTokenString(n),c]))
    return ret

def nGramsToTokenString(n):
    s = ''
    for t in n:
        s = s + " " + t
    return s[1:]
