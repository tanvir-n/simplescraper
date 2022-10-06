"""""""""""""""""""""""""""""""""""""""""""""
* 
* Title: web crawler / web scraper
* Description: This is a sample web crawler to crawle all the API and get all the book information
* Author: Tanvir Nayem
* Date: 08-29-20
* 
"""""""""""""""""""""""""""""""""""""""""""""

import re
from urllib import request
import requests
import asyncio


def extract_all_href(content):
    regular_expr = re.compile(r'<article class="product_pod">.*?<h3>.*?<a href="(.*?)"')
    # print(content)
    href = re.findall(regular_expr, content)
    links = ['http://books.toscrape.com/catalogue/' + x for x in href]
    return links


async def get_all_the_content(url):
    response = requests.get(url=url)
    content = re.sub('\s+',' ', response.text)
    return content

def generate_index_page_link():
    all_link = []
    for i in range(1, 51):
        link = 'http://books.toscrape.com/catalogue/page-{}.html'.format(i)
        all_link.append(link)
    return all_link

def get_all_page_link():
    all_index_page = generate_index_page_link()
    all_page_link = []
    for link in all_index_page:
        content = asyncio.run(get_all_the_content(link))
        links = extract_all_href(content=content)
        print('crawling', link)
        all_page_link.extend(links)
    
    return all_page_link

async def get_all_info_of_a_book(url):
    response = requests.get(url=url)
    content = re.sub('\s+',' ', response.text)
    title_re = re.compile(r'<div class="col-sm-6 product_main">.*?<h1>(.*?)</h1>')
    in_stock_re = re.compile(r'<p class="instock availability">.*?<i class="icon-ok"></i>(.*?)</p>')
    description_re = re.compile(r'<div id="product_description" class="sub-header">.*?<p>(.*?)</p>')
    upc_re = re.compile(r'<th>UPC</th>.*?<td>(.*?)</td>')
    product_type_re = re.compile(r'<th>Product Type</th>.*?<td>(.*?)</td>')
    price_incl_tx_re = re.compile(r'<th>Price \(incl. tax\)</th>.*?<td>(.*?)</td>')
    tax_re = re.compile(r'<th>Tax</th>.*?<td>(.*?)</td>')

    title = re.findall(title_re, content)[0]
    in_stock = re.findall(in_stock_re, content)[0]
    description = re.findall(description_re, content)[0]
    upc = re.findall(upc_re, content)[0]
    product_type = re.findall(product_type_re, content)[0]
    price_incl_tx = re.findall(price_incl_tx_re, content)[0]
    tax = re.findall(tax_re, content)[0]

    return (title, description, in_stock, upc, product_type, price_incl_tx, tax)


if __name__=='__main__':
    all_links = get_all_page_link()
    all_book_info = []
    for item in all_links:
        book_info = asyncio.run(get_all_info_of_a_book(item))
        all_book_info.append(book_info)
    
    # update the database with the specific data
    # print(all_book_info)
