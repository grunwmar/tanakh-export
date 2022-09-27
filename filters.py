import re

def replace_brackets(string, old=('[', ']'), new=('<em>', '</em>')):
    try:
        re_brackets = re.compile(f'(\{old[0]}([\w\s\d.,!?:;\'\u00A0-\u0903"\-\<\>/\"]*)\{old[1]})')
        found_brackets = re_brackets.findall(string)
        new_string = string

        for brackets in found_brackets:
            new_string = new_string.replace(brackets[0], f'{new[0]}{brackets[1]}{new[1]}')

        return new_string
    except TypeError:
        ...
    return string



def fix_yiddish_letters(string):
    try:
        substitute_list = [
            ["וו", "װ"],
            ["וי", "ױ"],
            ["יי", "ײ"],
            ["ײַ", "ײַ"],
            ["יִ", "יִ"],
        ]
        for s in substitute_list:
            subst_regx = re.compile("{}".format(s[0]), 0)
            string = subst_regx.sub(s[1], string)
    except TypeError:
        return string
    return string


def unescape_angle_brackets(string):
    return string.replace('&gt;', '>').replace('&lt;', '<')
