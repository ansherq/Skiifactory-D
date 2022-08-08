from django import template


register = template.Library()


bad_words = [
    'пздц', 'xxx', 'fuck', 'ху', 'bad', 'плохое',
    'слово',
]


@register.filter(name='censor')
def censor(value):
    # module_dir = os.path.dirname(__file__)
    # file_path = os.path.join(module_dir, 'censor_list.txt').encode('utf-8')
    # bad_words = open(file_path, 'r').read()

    x = value.lower()
    if ' ' in x:
        a = list(x.split(' '))
        for i in a:
            if i in bad_words:
                y = a.index(i)
                a.remove(i)
                a.insert(y, '@!%&!2')
                value = (" ".join(a))
                return value

    if x in bad_words:
        x = '@!%&!'
        return x
    else:
        return x