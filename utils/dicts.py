def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу, если ключ существует.
    :param collection: исходный словарь
    :param key: исходный ключ
    :param default: значение по умолчанию
    :return: значение по переданному ключу или значение по умолчанию
    """
    if collection == {}:
        return default

    return collection[key]
