import fractions
def calc_fractions(num1=input(), num2=input()):
    num1_list = num1.split("/")
    num2_list = num2.split("/")
    nominator1 = int(num1_list[0])
    nominator2 = int(num2_list[0])
    denominator1 = int(num1_list[1])
    denominator2 = int(num2_list[1])
    sum_of_fract = str(int((nominator1 * (lcf(denominator1, denominator2) / denominator1))) + int(
        (nominator2 * (lcf(denominator1, denominator2) / denominator2)))) + "/" + \
                   str(int(lcf(denominator1, denominator2)))
    mult_of_fract = str(int(nominator1 * nominator2)) + "/" + str(int(denominator1 * denominator2))
    return sum_of_fract, mult_of_fract


def gct(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    else:
        return num1


def lcf(num1, num2):
    return (num1 * num2) / gct(num1, num2)


print(calc_fractions())