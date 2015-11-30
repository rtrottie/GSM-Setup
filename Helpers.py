__author__ = 'ryan'

def load_variables(file_loc):
    vars = {}
    with open(file_loc) as f:
        for l in f.readlines():
            variable_value = l.split(':')
            vars[variable_value[0].strip()] = variable_value[1].strip()
    return vars