import re
def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Регулярний вираз для українських символів та пунктуації
    ukrainian_pattern = re.compile(r'[^а-яА-ЯёЁіІїЇєЄҐҐ\s]+')
    cleaned_lines = []
    for line in lines:
        cleaned_line = re.sub(ukrainian_pattern, '', line)
        cleaned_line = ' '.join(cleaned_line.split())
        if cleaned_line:
            cleaned_lines.append(cleaned_line)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(cleaned_lines) + '\n')
delete_html_tags('draft.html')