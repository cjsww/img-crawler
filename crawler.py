from icrawler.builtin import GoogleImageCrawler

presidents = [
    "이승만 대통령 얼굴 사진",
    "윤보선 대통령 얼굴 사진",
    "박정희 대통령 얼굴 사진",
    "최규하 대통령 얼굴 사진",
    "전두환 대통령 얼굴 사진",
    "노태우 대통령 얼굴 사진",
    "김영삼 대통령 얼굴 사진",
    "김대중 대통령 얼굴 사진",
    "노무현 대통령 얼굴 사진",
    "이명박 대통령 얼굴 사진",
    "박근혜 대통령 얼굴 사진",
    "문재인 대통령 얼굴 사진",
    "윤석열 대통령 얼굴 사진"
    "이재명 대통령 얼굴 사진"
]

for name in presidents:
    folder = name.split()[0]  # 이름만 폴더 이름으로
    crawler = GoogleImageCrawler(storage={'root_dir': folder})
    crawler.crawl(keyword=name, max_num=50)
