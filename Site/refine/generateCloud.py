import getPostsFromUrl as posts
import ThreadStatistics as stats
import svgTagCloudGenerator as svggen
import articleTextFromUrl as art
from time import time

def svgTextFromCnnUrl(cnnurl, p=None, width=1000, height=1500):
    common_ngrams = commonNGrams(cnnurl, p)
    #print str(time()-t) + " seconds to parse all the comments"
    s = svggen.commonTokensListToSVGImage(common_ngrams, width, height)
    return s

def jsListOfNgrams(cnnurl, p=None):
    common_ngrams = commonNGrams(cnnurl, p)
    jsList = "";
    for g in common_ngrams:
        jsList = jsList + ",{text: \"" + g[0].strip() + "\", weight: " + str(g[1]).strip() + "}"
    return jsList[1:]

def commonNGrams(cnnurl, p, N=30, bn=12):
    article_ngrams = stats.mostCommonNGramsFromString(art.articleTextFromURL(cnnurl),10)
    if p == None:
        p = posts.getPostsFromUrl(cnnurl)
    common_ngrams = stats.mostCommonNGramsFromPosts(p,N)
    bigrams = filter(lambda x: x[0] not in article_ngrams[1], common_ngrams[1])
    unigrams = filter(lambda x: x[0] not in article_ngrams[0], common_ngrams[0])
    bigrams = bigrams[0:bn]
    # fake reweighting by multiplying the bigram counts by a constant
    bigrams = map(lambda x: tuple([x[0], x[1]*3]), bigrams)
    unigrams = unigrams[0:(N-bn)]
    common_ngrams = unigrams
    common_ngrams.extend(bigrams)
    common_ngrams = stats.nGramsListToTokenStringsList(common_ngrams)
    return common_ngrams