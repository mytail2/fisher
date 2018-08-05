#!/usr/bin/env python


class Resource:
    def __enter__(self):
        print("连接资源")
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if tb != None:
            print("处理错误")
        else:
            print("无需处理")
        print("释放资源")
        return True

    def query(self):
        print("查询")

try:
    with Resource() as resource:
        1/0
        resource.query()
except Exception as ex:
    pass

