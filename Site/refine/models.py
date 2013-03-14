from django import forms
from django.db import models
import generateCloud
import svgTagCloudGenerator as svggen
import getPostsFromUrl as posts
import ThreadStatistics as thread
import re

class SearchBox(forms.Form):
    Search = forms.CharField(max_length=200)

class CreateWordCloud(models.Model):
    @staticmethod
    def getPosts(url):
        return posts.getPostsFromUrl(url)
    
    @staticmethod
    def makeSVG(img, posts):
        return generateCloud.svgTextFromCnnUrl(img, p=posts)
    
    @staticmethod
    def trimURL(url):
        link_pattern = re.compile("^.*\.html?")
        m = re.match(link_pattern, url)
        return m.group(0)
    
    @staticmethod
    def listNGrams(url, posts):
        return generateCloud.jsListOfNgrams(url, p=posts)

    @staticmethod
    def getPostsContaining(token, posts):
        return thread.findPostsContaining(posts, token)
