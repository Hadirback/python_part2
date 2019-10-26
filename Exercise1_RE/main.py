import re

def get_text_from_file(path):
    try:
        with open(path, 'r', encoding='UTF-8') as f:
            return f.read()
    except Exception as ex:
        print(f"Ошибка! {ex}")


def get_all_sentence(text):
    pattern = re.compile('.*?(?:[.?!]{1}\s|[.?!]{1}$)')
    return re.findall(pattern, text)


def show_items_list(list):
    for row in list:
        print('---')
        print(row)


def get_words(text):
    pattern = re.compile('\w{4,}')
    return re.findall(pattern, text)


def show_top_10_words(list):
    dictionary = dict((item, list.count(item)) for item in set(list))
    print(dictionary)
    count = 0
    for w in sorted(dictionary, key=dictionary.get, reverse=True):
        count += 1
        print(f'("{w}", {dictionary[w]})')
        if count == 10:
            break


def get_all_reference(text):
    pattern = re.compile('[\w\d]+\.[\w\d/]+(?:[^.\s]|\.?[\w\d/?=&]+)')
    return re.findall(pattern, text)


def get_sites(list):
    pattern = re.compile('/')
    list_sites = []
    for row in get_all_reference(text):
        list_sites.append(re.split(pattern, row)[0])

    return list_sites


def show_sites(list):
    dictionary_sites = dict((item, list.count(item)) for item in set(list))
    count = 0
    for w in sorted(dictionary_sites, key=dictionary_sites.get, reverse=True):
        count += 1
        print(f'("{w}", {dictionary_sites[w]})')
        if count == 1:
            break


def change_text(text):
    pattern = re.compile('[\w\d]+\.[\w\d/]+(?:[^.\s]|\.?[\w\d/?=&]+)')
    return re.sub(pattern, 'Ссылка отобразится после регистрации', text)


text = get_text_from_file('text')
print(text)
if text:

    sentence_list = get_all_sentence(text)
    show_items_list(sentence_list)

    words_list = get_words(text)
    # show_items_list(words_list)
    show_top_10_words(words_list)

    reference = get_all_reference(text)
    list_sites = get_sites(reference)

    if list_sites:
        show_sites(list_sites)

    print(change_text(text))