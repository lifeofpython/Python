#!/usr/bin/python
# encoding:utf-8


class C1(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def m1(self):
        print(self.x, self.y)


class C2(C1):
    def m1(self):
        super(C2, self).m1()
        # C1.m1(self)
        print("some special service.")


C2(3, 4).m1()