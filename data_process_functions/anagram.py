def anagram(word, text):
    word = word.lower()
    output_list = []

    for expression in text:
        if expression.lower() != word:
            expression_new = expression.lower()
            if ' ' in expression_new:
                expression_new = ''.join(expression_new.split(' '))
            exp_list = list(expression_new)
            test_word = list(word)
            if len(exp_list) == len(test_word):
                for i in word:
                    if i in exp_list:
                        test_word.remove(i)
                if len(test_word) == 0:
                    output_list.append(expression)

    return output_list
