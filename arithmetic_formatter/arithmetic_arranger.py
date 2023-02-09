import re


def arithmetic_arranger(*problems):
    try:
        probs, is_res = problems
        probs_len, three_lines, results, result_gap = vertical_format(probs)
        forth_line = ''
        for i in range(probs_len):
            forth_line += result_gap[i] * ' ' + results[i] + 4 * ' '
        return three_lines + '\n' + forth_line.rstrip()
    except:
        return vertical_format(problems[0], flag=False)


def vertical_format(probs, flag=True):
    probs_len = len(probs)
    if probs_len > 5:
        return "Error: Too many problems."
    pre_nums = []
    suf_nums = []
    operators = []
    cal_result = []
    for prob in probs:
        if '+' not in prob and '-' not in prob:
            return "Error: Operator must be '+' or '-'."
        prob = re.sub('\s', '', prob)
        pre_num, suf_num = re.split('[+-]', prob)
        if not pre_num.isdigit() or not suf_num.isdigit():
            return "Error: Numbers must only contain digits."
        if len(pre_num) > 4 or len(suf_num) > 4:
            return "Error: Numbers cannot be more than four digits."
        pre_nums.append(pre_num)
        suf_nums.append(suf_num)
        operators.append('+' if '+' in prob else '-')
        cal_result.append(str(eval(prob)))

    pre_num_lens = [len(pre) for pre in pre_nums]
    suf_num_lens = [len(suf) for suf in suf_nums]
    zip_lens = list(zip(pre_num_lens, suf_num_lens))
    max_lens = [max(lens) for lens in zip_lens]
    dash_len = [lens + 2 for lens in max_lens]
    pre_num_gaps = [dash_len[i] - pre_num_lens[i] for i in range(len(dash_len))]
    suf_num_gaps = [dash_len[i] - suf_num_lens[i] - 1 for i in range(len(dash_len))]

    first_line = second_line = third_line = ''
    for i in range(probs_len):
        first_line += pre_num_gaps[i] * ' ' + pre_nums[i] + 4 * ' '
        second_line += operators[i] + suf_num_gaps[i] * ' ' + suf_nums[i] + 4 * ' '
        third_line += dash_len[i] * '-' + 4 * ' '
    first_three_line = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + third_line.rstrip()

    if not flag:
        return first_three_line

    result_len = [len(result) for result in cal_result]
    result_num_gaps = [dash_len[i] - result_len[i] for i in range(len(dash_len))]
    return probs_len, first_three_line, cal_result, result_num_gaps


def main():
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))


if __name__ == '__main__':
    main()
