import json
import sympy as sp


def open_json():
    with open('Comparador.json', 'r') as archivo:
        datos_json = json.load(archivo)
    return datos_json


def return_concat_and(local_func, value, var, no_and=False):
    if value == 1:
        local_func_inter = local_func + var + '&'
    elif value == 0:
        local_func_inter = local_func + '~' + var + '&'
    else:
        local_func_inter = local_func
        return local_func_inter
    if no_and:
        return local_func_inter[:-1]
    return local_func_inter


def on_get_function(salida, data):
    func = ''
    output_uppercase = salida.upper()
    for (cell) in data:
        s = cell[output_uppercase]
        local_func = ''
        if s == 1:
            a0 = cell['A0']
            local_func = return_concat_and(local_func, a0, 'a0')
            a1 = cell['A1']
            local_func = return_concat_and(local_func, a1, 'a1')
            a2 = cell['A2']
            local_func = return_concat_and(local_func, a2, 'a2')
            a3 = cell['A3']
            local_func = return_concat_and(local_func, a3, 'a3')
            # a4 = cell['A4']
            # local_func = return_concat_and(local_func, a4, 'a4')
            b0 = cell['B0']
            local_func = return_concat_and(local_func, b0, 'b0')
            b1 = cell['B1']
            local_func = return_concat_and(local_func, b1, 'b1')
            b2 = cell['B2']
            local_func = return_concat_and(local_func, b2, 'b2')
            b3 = cell['B3']
            local_func = return_concat_and(local_func, b3, 'b3', True)
            # b4 = cell['B4']
            # local_func = return_concat_and(local_func, b4, 'b4')
            # c_in = cell['Cin']
            # local_func = return_concat_and(local_func, c_in, 'c_in', True)
            func = func + "(" + local_func + ")" + '|'
    return func[:-1]


def on_adapt_to_wincupl(func):
    function_local = str(func)
    return function_local.replace('~', '!').replace('|', '#').replace(' ', '')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = open_json()
    function_s6 = on_get_function('S6', data)
    # S5 funcion
    function_s5 = on_get_function('S5', data)
    # S4 funcion
    function_s4 = on_get_function('S4', data)
    # S3 funcion
    function_s3 = on_get_function('S3', data)
    # S2 funcion
    function_s2 = on_get_function('S2', data)
    # S1 funcion
    function_s1 = on_get_function('S1', data)
    # S0 funcion
    function_s0 = on_get_function('S0', data)
    print(on_adapt_to_wincupl(function_s0))

    a0, a1, a2, a3, b0, b1, b2, b3 = sp.symbols('a0 a1 a2 a3 b0 b1 b2 b3', boolean=True)

    try:

        s0 = sp.simplify(function_s0)
        print(s0)
        s1 = sp.simplify(function_s1)
        print(s1)
        s2 = sp.simplify(function_s2)
        print(s2)
        s3 = sp.simplify(function_s3)
        print(s3)
        s4 = sp.simplify(function_s4)
        print(s4)
        s5 = sp.simplify(function_s5)
        print(s5)
        s6 = sp.simplify(function_s6)
        print(s5)
    except:
        print('Error al simplificar')
        exit(1)

    win_function_s0 = on_adapt_to_wincupl(s0)
    win_function_s1 = on_adapt_to_wincupl(s1)
    win_function_s2 = on_adapt_to_wincupl(s2)
    win_function_s3 = on_adapt_to_wincupl(s3)
    win_function_s4 = on_adapt_to_wincupl(s4)
    win_function_s5 = on_adapt_to_wincupl(s5)
    win_function_s6 = on_adapt_to_wincupl(s6)

    print(win_function_s0)
    print(win_function_s1)
    print(win_function_s2)
    print(win_function_s3)
    print(win_function_s4)
    print(win_function_s5)
    print(win_function_s6)

    object_json = {
        'S6': win_function_s6,
        'S5': win_function_s5,
        'S4': win_function_s4,
        'S3': win_function_s3,
        'S2': win_function_s2,
        'S1': win_function_s1,
        'S0': win_function_s0
    }
    with open('funcionesComparador.json', 'w') as archivo:
        json.dump(object_json, archivo)
