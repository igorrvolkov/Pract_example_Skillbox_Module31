# РЕШЕНИЕ 2


import copy


def zip_dicts(data1: dict, data2: dict, res_data: dict = None) -> dict:
    """
    Функция, которая принимает два словаря одинаковой структуры и объединяет в кортежи значения всех ключей, представленные типами int или str:
    (value1: [int, str], value2 : [int, str]).
    Если значением ключа является список или словарь, функция спускается на уровень ниже.
    Функция написана для упрощения отладки кода (облегчает визуальный поиск расхождений между двумя словарями).

    Ограничения: 1. data1 и data2 должны иметь одинаковую структуру 2. Значения всех ключей в data1 и data2 должны совпадать по типам.

    :param:
        :data1: первый словарь
        :data2: второй словарь
        :res_data: выходной словарь, объединяющий значения двух входных словарей (по умолчанию None). Передаётся в функцию, если происходит её рекурсивный вызов
    :return res_data: выходной словарь, объединяющий значения всех ключей из первого и второго словаря в кортежи
    """
    if res_data is None:
        res_data = copy.deepcopy(data1)

    for key, value in res_data.items():
        if isinstance(value, (int, str)):
            res_data[key] = (data1[key], data2[key])

        elif isinstance(value, dict):
            zip_dicts(value, data2[key], res_data[key])

        elif isinstance(value, list):
            if len(value) == 0:
                dict1[key] = ([], [])
            for index in range(len(value)):
                zip_dicts(value[index], data2[key][index], res_data[key][index])

    return res_data


def find_all_differences(prev_data: dict, last_data: dict, res_data: dict) -> dict:
    """ Функция, сравнивающая два версии одного словаря - старую и новую - на предмет всех несоответствий в значениях ключей.
    При этом в результат записываются несоответствия, которые выявлены на самом нижнем уровне (т.е. значение ключа имеет тип int или str, а не list или dict)
    Если значениями ключей являются вложенные словари или списки, функция рекурсивно обрабатывает их содержимое.
    В таком случае, если несоответствие по какому-либо ключу имеется не по всем значениям ключей вложенного словаря либо элементов списка,
    в результат записываются только те ключи и значения, по которым выявлено несоответствие.

    :param:
        :prev_data: старые данные
        :last_data: новые данные
        :res_data: передаётся глубокая копия last_data, которую обрабатывает функция и затем возвращает в качестве результата

    :return: результат сравнения, сохраняющий структуру входных данных. В случае, если различия между входными отсутствуют, возвращается пустой словарь.
    """
    for key, value in last_data.items():
        if last_data[key] == prev_data[key]:
            res_data.pop(key)

        else:
            if isinstance(value, dict):
                find_all_differences(prev_data[key], last_data[key], res_data[key])
                if not res_data[key]:
                    res_data.pop(key)                   # подобные блоки добавлены для удаления тех ключей,
                # значениями которых после рекурсивного вызова функции становится пустые список, словарь, или список, содержащий пустой словарь

            elif isinstance(value, list):
                for index in range(len(value)):
                    find_all_differences(prev_data[key][index], last_data[key][index], res_data[key][index])
                    if not res_data[key][index]:
                        res_data[key].pop(index)
                if not res_data[key]:
                    res_data.pop(key)

            elif isinstance(value, (int, str)):
                continue

    return res_data


def clear_by_params(data: dict, cleared_data: dict, params) -> dict:
    """
    Функция, производящая фильтрацию словаря по заданным ключам
    :params:
        :data: исходный словарь, по которому происходит итерация
        :cleared_data: копия исходного словаря, который обрабатывает функция

    :return: возвращает обработанный словарь, из которого выброшены ненужные значения и при этом сохранена структура
    """
    for key, value in data.items():
        if key in params:
            continue

        else:
            if isinstance(value, (int, str)) and key not in params:
                cleared_data.pop(key)

            elif isinstance(value, dict):
                clear_by_params(value, cleared_data[key], params)
                if not cleared_data[key]:
                    cleared_data.pop(key)

            elif isinstance(value, list):
                for index in range(len(value)):
                    clear_by_params(value[index], cleared_data[key][index], params)
                    if not cleared_data[key][index]:
                        cleared_data[key].pop(index)

                if not cleared_data[key]:
                    cleared_data.pop(key)

    return cleared_data


def compare(prev_data: dict, last_data: dict, params: list = None) -> dict:
    """ Функция, сравнивающая две версии одного словаря - старую и новую.
    Если параметры не заданы, производится отслеживание всех изменений.
    Если параметры заданы, то сравнение производится только по ним; остальные изменения игнорируются.

    :param:
        :prev_data: старые данные
        :last_data: новые данные
        :res_data: результат сравнения (по умолчанию None). Передаётся в функцию, если происходит её рекурсивный вызов.
        :params: опциональный список параметров, по которым производится сравнение данных в prev_data и last_data

    :return: результат сравнения, сохраняющий структуру входных данных. В случае, если различия между входными отсутствуют, возвращается пустой словарь.
    """
    res_data = copy.deepcopy(last_data)
    result = find_all_differences(prev_data=prev_data, last_data=last_data, res_data=res_data)
    if params:
        result_copy = copy.deepcopy(result)
        result = clear_by_params(data=result, cleared_data=result_copy, params=params)
    return result


# В тестовые данные внесены некоторые изменения по сравнению с исходным заданием
dict1 = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create',
         'data': {'id': 11111111, 'company_id': 111111, 'services': [
             {'id': 9035445, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500, 'amount': 1}],
                  'goods_transactions': [], 'staff': {'id': 1819441, 'name': 'Мастер'},
                  'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111111', 'success_visits_count': 2,
                             'fail_visits_count': 1}, 'clients_count': 1, 'datetime': '2022-01-25T11:00:00+03:00',
                  'create_date': '2022-01-22T00:54:00+03:00', 'online': False, 'attendance': 0, 'confirmed': 1,
                  'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049,
                  'created_user_id': 10573443, 'deleted': False, 'paid_full': 0,
                  'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}

dict2 = {'company_id': 111111, 'resource': 'record', 'resource_id': 406155061, 'status': 'create',
         'data': {'id': 11011111, 'company_id': 111111, 'services': [
             {'id': 22222225, 'title': 'Стрижка', 'cost': 1500, 'cost_per_unit': 1500, 'first_cost': 1500,
              'amount': 1}], 'goods_transactions': [], 'staff': {'id': 1819442, 'name': 'Мастер'},
                  'client': {'id': 130345867, 'name': 'Клиент', 'phone': '79111111101', 'success_visits_count': 2,
                             'fail_visits_count': 0}, 'clients_count': 1, 'datetime': '2022-01-25T13:00:00+03:00',
                  'create_date': '2022-01-22T00:54:00+03:00', 'online': 2, 'attendance': 2, 'confirmed': 1,
                  'seance_length': 3600, 'length': 3600, 'master_request': 1, 'visit_id': 346427049,
                  'created_user_id': 10573443, 'deleted': False, 'paid_full': 1,
                  'last_change_date': '2022-01-22T00:54:00+03:00', 'record_labels': '', 'date': '2022-01-22 10:00:00'}}


if __name__ == '__main__':
    diff_list = ["services", "staff", "datetime", "client", "phone", "id", "online"]
    zipped = zip_dicts(dict1, dict2)
    # print('Zipped dicts:', zipped, sep='\n', end='\n\n')
    result = compare(dict1, dict2, params=diff_list)
    print('Compare by params - test result:', result, sep='\n', end='\n\n')

