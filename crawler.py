from icrawler.builtin import GoogleImageCrawler

crawler = GoogleImageCrawler(storage={'root_dir': '문재인'})
crawler.crawl(keyword='문재인 대통령 얼굴 사진', max_num=20)
