import getPostsFromUrl as posts
import ThreadStatistics as stats
import svgTagCloudGenerator as svggen
from time import time

def svgTextFromCnnUrl(cnnurl, N=8, nGram=2, width=740, height=500):
    t = time()
    p = posts.getPostsFromUrl(cnnurl)
    print str(time()-t) + " seconds to fetch " + str(len(p)) + " unfiltered posts from disqus"
    t = time()
    # currently just displays the most common bigrams
    common_ngrams = stats.mostCommonNGramsFromPosts(p,N)
    common_ngrams = stats.nGramsListToTokenStringsList(common_ngrams[nGram-1])
    print str(time()-t) + " seconds to parse all the comments"
    s = svggen.commonTokensListToSVGImage(common_ngrams, width, height)
    return s

