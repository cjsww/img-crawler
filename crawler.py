import os
import shutil
from icrawler.builtin import GoogleImageCrawler

presidents = [
    "이승만",
    "윤보선",
    "박정희",
    "최규하",
    "전두환",
    "노태우",
    "김영삼",
    "김대중",
    "노무현",
    "이명박",
    "박근혜",
    "문재인",
    "윤석열",
    "이재명"
]

final_folder = 'all_presidents'
os.makedirs(final_folder, exist_ok=True)

for keyword in presidents:
    name = keyword.split()[0]
    temp_folder = f'_tmp_{name}'
    os.makedirs(temp_folder, exist_ok=True)

    print(f'크롤링 시작: {name}')
    crawler = GoogleImageCrawler(storage={'root_dir': temp_folder})
    crawler.crawl(keyword=keyword, max_num=10)

    # 임시폴더 이미지 → 최종폴더로 이름 붙여서 이동
    for idx, fname in enumerate(sorted(os.listdir(temp_folder))):
        src = os.path.join(temp_folder, fname)
        dst_name = f'{name}_{idx+1}.jpg'
        dst = os.path.join(final_folder, dst_name)
        shutil.move(src, dst)

    shutil.rmtree(temp_folder)
