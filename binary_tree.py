import json

root = None


def create_node(data):
    return {"data": data, "left": None, "right": None, "depth": None}


def insert_node(data):
    global root
    node = create_node(data)
    if root:
        current_node = root
        while current_node:
            if data <= current_node["data"]:
                if current_node["left"] is None:
                    current_node["left"] = node
                    node["depth"] = current_node["depth"] + 1
                    # print("inserted left")
                    break
                else:
                    current_node = current_node["left"]
            else:
                if current_node["right"] is None:
                    current_node["right"] = node
                    node["depth"] = current_node["depth"] + 1
                    # print("inserted right")
                    break
                else:
                    current_node = current_node["right"]
    else:
        root = node
        root["depth"] = 1


def binary_insertion(arr):
    n = len(arr)
    if n > 0:
        insert_node(arr[n // 2])
    else:
        return

    binary_insertion(arr[: n // 2])
    binary_insertion(arr[n // 2 + 1 :])
    return


def get_min(root):
    current_node = root
    while current_node:
        if current_node["left"]:
            current_node = current_node["left"]
        else:
            return current_node["data"]
            # break


def height(root):
    current_node = root
    if current_node is None:
        return 0

    while current_node:
        return max(height(current_node["left"]), height(current_node["right"])) + 1


def get_max(root):
    current_node = root
    while current_node:
        if current_node["right"]:
            current_node = current_node["right"]
        else:
            return current_node["data"]
            # break


def inorder_traversal(root):
    current_node = root
    if current_node is None:
        return
    else:
        inorder_traversal(current_node["left"])
        print(current_node["data"], end=",")
        inorder_traversal(current_node["right"])


def preorder_traversal(root):
    current_node = root
    if current_node is None:
        return
    else:
        print((current_node["data"], current_node["depth"]), end=",")
        preorder_traversal(current_node["left"])
        preorder_traversal(current_node["right"])


def postorder_traversal(root):
    current_node = root
    if current_node is None:
        return
    else:
        postorder_traversal(current_node["left"])
        postorder_traversal(current_node["right"])
        print(current_node["data"], end=",")


# def delete_node(data,root):
# if

# def create_bst_preorder(arr):


def level_order_traversal(root):
    stack = [root]
    temp_stack = [root]
    current_id = 0
    while current_id < len(temp_stack):
        current_element = temp_stack[current_id]
        # stack.append(current_element)
        if current_element["left"] is not None:
            temp_stack.append(current_element["left"])
            stack.append(current_element["left"])
        else:
            stack.append(None)
        if current_element["right"] is not None:
            temp_stack.append(current_element["right"])
            stack.append(current_element["right"])
        else:
            stack.append(None)

        current_id += 1

    return stack


def visualize_tree(root):
    levels = height(root)
    print(f"{levels=}")
    # preorder_traversal(root)
    # print(postorder_traversal(root))
    l = level_order_traversal(root)
    current_depth = levels
    op_vis = ""
    # op_vis += "_" * (pow(2, levels - current_depth))

    row = []
    for idx, a in enumerate(l[::-1]):
        if a:
            if a["depth"] != current_depth:
                prespace = int(2 ** (levels - current_depth - 1))
                space = int(2 ** (levels - current_depth + 1) - 1)
                print("_" * prespace + ("_" * space).join(row))
                row = []
                current_depth = a["depth"]

            row.append(str(a["data"]))
    prespace = int(2 ** (levels - current_depth - 1))
    space = int(2 ** (levels - current_depth + 1) - 1)
    print("_" * prespace + ("_" * space).join(row))


def inorder_create(arr):
    n = len(arr)
    if n < 1:
        return
    mid = int(n / 2)
    insert_node(arr[mid])
    inorder_create(arr[:mid])
    inorder_create(arr[mid + 1 :])


if __name__ == "__main__":

    arr = list(range(1, 15))
    inorder_create(arr)
    # for a in arr:
    #     insert_node(a)

    visualize_tree(root)
