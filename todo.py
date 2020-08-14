import requests
import json


def getall_todo(url):
    res = requests.get(url)
    print(res.text)


# def geta_todo(url):
#     id = int(input())
#     res = requests.get(url{i)
#     print(res.text)


def getATODO(todo_id):
    url = f"http://127.0.0.1:5000/todo/api/v1.0/tasks/{todo_id}"

    res = requests.get(url)

    print(res.text)


# def postTodo(data):
#     title=input()
#     description = input()
#     url=f'http://127.0.0.1:5000/todo/api/v1.0/tasks/'


def postTODO(post_data):
    url = "http://127.0.0.1:5000/todo/api/v1.0/tasks"
    res = requests.post(url, json=(post_data))

    print(f"Post Status: {res.status_code}")
    print(res.text)


data = {"title": "Eat Fish", "description": "mere kamar me dard hora hai"}
postTODO(data)

# getATODO(3)
url = "http://127.0.0.1:5000/todo/api/v1.0/tasks"

getall_todo(url)
# geta_todo(url)git pu
