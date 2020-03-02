import json

root = None


def create_node(data):
    return {"data": data, "left": None, "right": None}


def insert_node(data):
    global root
    node = create_node(data)
    if root:
        current_node = root
        while current_node:
            if data <= current_node["data"]:
                if current_node["left"] is None:
                    current_node["left"] = node
                    # print("inserted left")
                    break
                else:
                    current_node = current_node["left"]
            else:
                if current_node["right"] is None:
                    current_node["right"] = node
                    # print("inserted right")
                    break
                else:
                    current_node = current_node["right"]
    else:
        root = node


def binary_insertion(arr):
    n = len(arr)
    if n > 0:
        insert_node(arr[n // 2])
    else:
        return

    binary_insertion(arr[: n // 2])
    binary_insertion(arr[n // 2 + 1 :])
    return


if __name__ == "__main__":

    arr = list(range(100))

    for a in arr:
        insert_node(a)
    # binary_insertion(arr)
    # with open("temp.json", "w") as file_out:
    #     json.dump(root, file_out, indent=2)

    current_node = root
    while current_node:
        if current_node["left"]:
            current_node = current_node["left"]

        else:
            print(current_node["data"])
            break

    current_node = root
    while current_node:
        if current_node["right"]:
            current_node = current_node["right"]
        else:
            print(current_node["data"])
            break
    # for a in arr:
    #     insert_node(a)

    # current_node = root
    # while current_node:
    #     print(current_node["data"])
    #     current_node = current_node["right"]
