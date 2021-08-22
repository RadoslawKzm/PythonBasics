"""You are given height of christmass tree, printout christmass tree in console.
input : height=5
output:
    *
   ***
  *****
 *******
*********

Good luck :)
"""


def christmas_tree(*, height: int) -> str:
    list_ = []
    for i in range(1, height + 1):
        list_.append(f"""{'*' * (i * 2 - 1):^{height * 2 - 1}}""")
    output = "\n".join(list_)
    return output


def christmas_tree_upgraded(*, height: int) -> str:
    return "\n".join([f"""{'*' * (i * 2 - 1):^{height * 2 - 1}}""" for i in range(1, height + 1)])


if __name__ == "__main__":
    print(christmas_tree(height=5))
    print(christmas_tree_upgraded(height=5))
