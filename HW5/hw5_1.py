def get_file_info(path: str):
    path = path.split("/")
    ext = path[-1].split(".")[1]
    name = path[-1].split(".")[0]
    res_path = "/".join(path[:-1])
    return ext, name, res_path


print(get_file_info("/Users/alekseikopylkov/Courses/PythonHW/HW4/hw4_1.py"))