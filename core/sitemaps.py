# home/sitemaps.py
from django.contrib import sitemaps
from django.shortcuts import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        # these are the named URLs from your `urls.py`
        return ['home', 'about', 'contact']

    def location(self, item):
        return reverse(item)
