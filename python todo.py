import json
def menu_show():
    print("1.添加待办")
    print("2.查看全部")
    print("3.查看未完成")
    print("4.标记完成")
    print("5.删除待办")
    print("6.保存并退出")
    print("0.直接退出（不保存）")
def add_todo(todos):
    content = input("请输入待办事项")
    if content.strip() == "":
        print("内容不能为空")
        return
    new_id = len(todos) + 1
    todos.append({"id": new_id, "content": content, "done": False})
    print(f"已添加:{content}")
def mark_undone(todos):
    found = False
    for item in todos:
        if not item["done"]:
            print(f"[ID:{item['id']} , {item['content']}]")
            found = True
    if not found:
        print("目前没有未完成的事项")
def mark_done(todos):
    if len(todos) == 0:
        print("清单为空")
        return
    user_input = input("请输入要标记的完成的事项")
    for item in todos:
        if str(item["id"]) == user_input:
            item["done"] = False
            print(f"[{item['content']}]")
            return
    print("未找到该ID对应的待办事项。")
def list_todos(todos):
    if len(todos) == 0:
        print("清单为空")
        return
    for item in todos:
        mark = "[x]" if item["done"] else "[o]"
        print(f"{mark}{item['id']}{item['content']}")
def delete_todo(todos):
    if len(todos) == 0:
        print("清单为空")
        return
    user_input = input("请输入要删除的待办事项")
    for item in todos:
        if str(item["id"]) == user_input:
            todos.remove(item)
            print(f"[{item['content']}]已成功移除")
            return
    print("未找到该ID对应的待办事项")
def main():
    todos = []
    while True:
        menu_show()
        choice = input("请输入选项")
        if choice == "0":
            print("已退出")
            break
        else:
            if choice == "1":
                add_todo(todos)
            elif choice == "2":
                list_todos(todos)
            elif choice == "3":
                mark_undone(todos)
            elif choice == "4":
                mark_done(todos)
            elif choice == "5":
                delete_todo(todos)
            elif choice == "6":
                with open("todos.json", "w" , encoding = "utf-8") as f:
                    json.dump(todos, f, ensure_ascii = False, indent = 4)
                    print("数据已保存")
                    break
            elif choice == "0":
                break
            else:
                print("这个功能未完善")
if __name__ == "__main__":
    main()

