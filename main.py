import json
import sympy as sp


def open_json():
    with open('Combinacional_toJSon.json', 'r') as archivo:
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
            # a2 = cell['A2']
            # local_func = return_concat_and(local_func, a2, 'a2')
            # a3 = cell['A3']
            # local_func = return_concat_and(local_func, a3, 'a3', True)
            # a4 = cell['A4']
            # local_func = return_concat_and(local_func, a4, 'a4')
            b0 = cell['B0']
            local_func = return_concat_and(local_func, b0, 'b0')
            b1 = cell['B1']
            local_func = return_concat_and(local_func, b1, 'b1')
            # b2 = cell['B2']
            # local_func = return_concat_and(local_func, b2, 'b2')
            # b3 = cell['B3']
            # local_func = return_concat_and(local_func, b3, 'b3', True)
            # b4 = cell['B4']
            # local_func = return_concat_and(local_func, b4, 'b4')
            # c_in = cell['Cin']
            # local_func = return_concat_and(local_func, c_in, 'c_in', True)
            c0 = cell['C0']
            local_func = return_concat_and(local_func, c0, 'c0')
            c1 = cell['C1']
            local_func = return_concat_and(local_func, c1, 'c1', True)
            func = func + "(" + local_func + ")" + '|'
    return func[:-1]


def on_adapt_to_wincupl(func):
    function_local = str(func)
    return function_local.replace('~', '!').replace('|', '#').replace(' ', '')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = open_json()
    function_s0 = on_get_function('s0', data)
    function_s1 = on_get_function('s1', data)
    function_s2 = on_get_function('s2', data)

    a0, a1, b0, b1, c0, c1 = sp.symbols('a0 a1 b0 b1 c0 c1', boolean=True)

    try:
        simp_s0 = sp.simplify(function_s0)
        simp_s1 = sp.simplify(function_s1)
        simp_s2 = sp.simplify(function_s2)
        # s0 = sp.simplify(function_s0)
        # print(s0)

    except:
        print('Error al simplificar')
        exit(1)

    # win_function_s0 = on_adapt_to_wincupl(s0)

    object_json = {
        's0': on_adapt_to_wincupl(simp_s0),
        's1': on_adapt_to_wincupl(simp_s1),
        's2': on_adapt_to_wincupl(simp_s2)
    }
    with open('FuncionesComb.json', 'w') as archivo:
        json.dump(object_json, archivo)
