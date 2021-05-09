def imprimeerror(code, error):
    with open('static/template.html', 'r') as file:
        s = file.read()
        print(s.format('Error', f'{code}: {error}'))
    exit()
