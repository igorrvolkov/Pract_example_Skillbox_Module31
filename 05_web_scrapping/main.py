import re
import requests


def get_content_among_h3_tags(html_text: str) -> None:
    """
    Функция, которая принимает html-код страницы в виде текста
    и распечатывает все заголовки между тегами <h3...> </h3>
    """
    filter1 = r'<h3.*?>.*?</h3>'
    result1 = re.findall(filter1, html_text)
    filter2 = r'(?<=>).*(?=<)'
    result2 = []
    for line in result1:
        result2.append(re.search(filter2, line).group())
    print(result2)


# код для тестирования
if __name__ == '__main__':
    # тест из задания
    with open('examples.html', 'r') as f:
        html_text = f.read()
    print('Test 1')
    get_content_among_h3_tags(html_text)
    print()

    # дополнительные тесты
    test_urls = ['http://www.columbia.edu/~fdc/sample.html',
                 'https://i-vd.org.ru/chapter2/',
                 'https://www.schoolsw3.com/html/tryit.php?filename=tryhtml_basic_headings']

    for test_num, url in enumerate(test_urls, 2):
        print(f'Test {test_num}\tURL:{url}')
        html_text = requests.get(url).text
        get_content_among_h3_tags(html_text)
        print()

