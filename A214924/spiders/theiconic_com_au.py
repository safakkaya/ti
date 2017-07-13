from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class TheiconicComAu(BasePortiaSpider):
    name = "www.theiconic.com.au"
    allowed_domains = [u'www.theiconic.com.au']
    start_urls = [
        u'http://www.theiconic.com.au/nike-power-legend-women-s-high-rise-training-tights-488916.html']
    rules = [
        Rule(
            LinkExtractor(
                allow=(u'.html', u'/sale/'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'.product-information',
                [
                    Field(
                        u'Cat_1',
                        '.medium-7 > .product-gallery > div:nth-child(1) > .small-12 > .breadcrumbs > li:nth-child(1) > .ga-track-link-click *::text',
                        []),
                    Field(
                        u'Cat_2',
                        '.medium-7 > .product-gallery > div:nth-child(1) > .small-12 > .breadcrumbs > li:nth-child(2) > .ga-track-link-click *::text',
                        []),
                    Field(
                        u'Cat_3',
                        '.medium-7 > .product-gallery > div:nth-child(1) > .small-12 > .breadcrumbs > li:nth-child(3) > .ga-track-link-click *::text',
                        []),
                    Field(
                        u'Image',
                        '.medium-7 > .product-gallery > div:nth-child(3) > .small-12 > .main-image-frame > .img > .owl-wrapper-outer > .owl-wrapper > div:nth-child(1) > .image-wrapper > .image-frame > img::attr(src)',
                        []),
                    Field(
                        u'Brand',
                        '.medium-5 > .main > .item-details > .product-info > .product-title > .small-12 > .product-name > .brand-title > a *::text',
                        []),
                    Field(
                        u'Name',
                        '.medium-5 > .main > .item-details > .product-info > .product-title > .small-12 > .product-name > span:nth-child(2) *::text',
                        []),
                    Field(
                        u'Price',
                        '.medium-5 > .main > .item-details > .product-info > .product-price > .small-12 > .price *::text',
                        [],
                        True),
                    Field(
                        u'Colour',
                        '.medium-5 > .main > .item-details > .add-to-bag > .row > .small-12 > .ti-dropdown > .dropdown > span > .color-name *::text',
                        []),
                    Field(
                        u'Size',
                        '.medium-5 > .main > .item-details > .add-to-bag > .ng-pristine > div:nth-child(1) > .small-7 > .ti-dropdown > .f-dropdown *::text',
                        []),
                    Field(
                        u'Description',
                        '.medium-5 > .main > .item-details > .accordion > dd *::text',
                        [])]),
            Item(
                PortiaItem,
                None,
                u'.product-information',
                [
                    Field(
                        u'Cat_1',
                        '.medium-7 > .product-gallery > div:nth-child(1) > .small-12 > .breadcrumbs > li:nth-child(1) > .ga-track-link-click *::text',
                        []),
                    Field(
                        u'Cat_2',
                        '.medium-7 > .product-gallery > div:nth-child(1) > .small-12 > .breadcrumbs > li:nth-child(2) > .ga-track-link-click *::text',
                        []),
                    Field(
                        u'Cat_3',
                        '.medium-7 > .product-gallery > div:nth-child(1) > .small-12 > .breadcrumbs > li:nth-child(3) > .ga-track-link-click *::text',
                        []),
                    Field(
                        u'Image',
                        '.medium-7 > .product-gallery > div:nth-child(3) > .small-12 > .main-image-frame > .img > .owl-wrapper-outer > .owl-wrapper > div:nth-child(1) > .image-wrapper > .image-frame > img::attr(src)',
                        []),
                    Field(
                        u'Name',
                        '.medium-5 > .main > .item-details > .product-info > .product-title > .small-12 > .product-name > span:nth-child(2) *::text',
                        []),
                    Field(
                        u'Colour',
                        '.medium-5 > .main > .item-details > .product-info > .product-price > .small-12 *::text',
                        []),
                    Field(
                        u'PriceRrp',
                        '.medium-5 > .main > .item-details > .product-info > .product-price > .small-12 > .original *::text',
                        []),
                    Field(
                        u'PriceSale',
                        '.medium-5 > .main > .item-details > .product-info > .product-price > .small-12 > .final *::text',
                        []),
                    Field(
                        u'Size',
                        '.medium-5 > .main > .item-details > .add-to-bag > .ng-pristine > div:nth-child(1) > .small-7 > .ti-dropdown > .f-dropdown *::text',
                        []),
                    Field(
                        u'Description',
                        '.medium-5 > .main > .item-details > .accordion *::text',
                        [])])]]
