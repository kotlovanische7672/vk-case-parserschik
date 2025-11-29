from bs4 import BeautifulSoup
import re

def parse_cases():
    with open('vk_cases.html', 'r', encoding='utf-8') as file:
        content = file.read()
    
    cases = []
    
    lines = content.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        date_match = re.search(r'(\d{2}\.\d{2}\.\d{4})', line)
        if date_match:
            date = date_match.group(1)
            title = re.sub(r'\s*–\s*Кейс о работе с VK Рекламой\s*', '', line.replace(date, '')).strip()
            
            if title and len(title) > 10:
                case_data = {
                    'title': title,
                    'date': date,
                    'link': generate_link(title)
                }
                cases.append(case_data)
    
    return cases

def generate_link(title):
    base_url = "https://ads.vk.com/cases/"
    slug = re.sub(r'[^a-zA-Zа-яА-Я0-9\s]', '', title)
    slug = re.sub(r'\s+', '-', slug.lower().strip())
    return base_url + slug

if __name__ == "__main__":
    result = parse_cases()
    print(f"Найдено кейсов: {len(result)}")
    for i, case in enumerate(result, 1):
        print(f"\n--- Кейс {i} ---")
        print(f"Название: {case['title']}")
        print(f"Дата: {case['date']}")
        print(f"Ссылка: {case['link']}")