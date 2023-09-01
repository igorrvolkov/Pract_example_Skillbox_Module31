# РЕШЕНИЕ 1


import json


def compare(last_data: dict, prev_data: dict, params: list, res_data=None) -> dict:
    """
    Функция для сравнения новых и старых данных, представленных в двух словарях одинаковой структуры

    :param:
        :last_data: новые данные
        :prev_data: старые данные
        :params: параметры, по которым производится сравнение данных

    :return res_data: новый словарь, в который записываются различия между входными данными.
        В случае обнаружения различия между значениями параметра в last_dict и prev_dict в res_data записывается новое значение параметра из last_dict.
        Если различий по параметрам не обнаружено, возвращается пустой словарь.

    """
    if res_data is None:
        res_data = {}

    for key, value in last_data.items():

        if key in params and last_data[key] != prev_data[key]:
            res_data[key] = value

        elif isinstance(value, dict):
            compare(value, prev_data[key], params, res_data)

        elif isinstance(value, list):
            for index in range(len(value)):
                compare(value[index], prev_data[key][index], params, res_data)

    return res_data


if __name__ == '__main__':
    with open('json_old.json', 'r') as file1, open('json_new.json', 'r') as file2:
        dict1, dict2 = json.load(file1), json.load(file2)

    diff_list = ["services", "staff", "datetime"]
    result = compare(prev_data=dict1, last_data=dict2, params=diff_list)
    print(result)

    with open('result.json', 'w') as result_file:
        json.dump(result, result_file, indent=4)
