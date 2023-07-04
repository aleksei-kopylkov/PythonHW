def make_dict(**kwargs):
    res_dict = {}
    for kwd, value in kwargs.items():
        res_dict[value] = kwd
    return res_dict


