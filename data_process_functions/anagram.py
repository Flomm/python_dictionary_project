def anagram(word, text):
    word = word.lower()
    output_list = []

    for expression in text:
        expression_new = expression.lower()
        if ' ' in expression_new:
            expression_new = ''.join(expression_new.split(' '))
        exp_list = list(expression_new)

        for i in word:
            if i in exp_list:
                exp_list.remove(i)
        if len(exp_list) == 0:
            output_list.append(expression)

    return output_list
