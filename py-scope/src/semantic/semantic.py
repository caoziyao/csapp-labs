# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/24 
@desc:
"""
from src.common.expression import Kind
from src.common.utils import is_leaf
from src.semantic.sem_table import SemTable

table = SemTable()


class Sematic(object):

    def __init__(self, root):
        global table
        self.root = root
        self.table = table
        self.semfunc = {
            Kind.plus: self.check_stm_plus,
            Kind.var: self.check_stm_var,
            Kind.print: self.check_stm_print,
            Kind.k_if: self.check_stm_kif,
            Kind.kwhile: self.check_stm_kwhile,
            Kind.kdef: self.check_stm_def,
            # Kind.minus: check_minus,
            # Kind.times: check_times,
            # Kind.div: check_div,
            # Kind.number: check_number,
            # Kind.id: check_id,
            # Kind.true: check_true,
            # Kind.false: check_false,
            # Kind.undefind: check_undefind,
        }

    def check_stm_kwhile(self, node):
        """

        :param node:
        :return:
        """
        pass

    def check_stm_def(self, node):
        """

        :param node:
        :return:
        """
        pass

    def check_stm_var(self, node):
        left = node.left
        right = node.right

        if self.check_id(left):
            name = left.value
            self.table.enter(name, Kind.var)

        self.check_stm_expression(right)

        return True

    def check_stm_kif(self, node):
        """

        :return:
        """
        pass

    def is_id(self, node):
        """
        是 Id
        :param node:
        :return:
        """
        if node.type == Kind.id:
            return True
        else:
            return False

    def is_lookup(self, node):
        """
        是否已经声明
        :param node:
        :return:
        """
        table = self.table
        value = node.value
        if table.lookup(value):
            return True
        else:
            return False

    def check_stm_print(self, node):
        """
        如果右边为 id
        :param node:
        :return:
        """
        left = node.left
        right = node.right

        if self.is_id(right):
            if not self.is_lookup(right):
                raise Exception('{} is undefined'.format(right.value))
        #     name = left.value
        #     self.table.enter(name, Kind.var)
        #
        # self.check_stm_expression(right)

        return True

    def check_stm_expression(self, node):
        """
        校验表达式
        :param node:
        :return:
        """
        m = {
            Kind.plus: self.check_stm_plus,
            Kind.times: self.check_stm_times,
        }
        if node:
            ltype = self.check_stm_expression(node.left)
            rtype = self.check_stm_expression(node.right)

            if is_leaf(node):
                # 叶子节点
                return node.type
            else:
                kind = node.type
                f = m.get(kind, None)
                if f:
                    t = f(node, ltype, rtype)
                else:
                    raise Exception('not check_expression')
                return t

    def check_same_var(self, ltype, rtype):
        """
        left 类型 == right 类型
        :param left:
        :param right:
        :return:
        """
        # ltype = left.type
        # rtype = right.type
        if ltype != rtype:
            raise Exception('type mismatch {} != {}'.format(ltype.name, rtype.name))

        return True

    def check_stm_times(self, node, ltype, rtype):
        """

        :param node:
        :param ltype:
        :param rtype:
        :return:
        """
        self.check_same_var(ltype, rtype)

        return ltype

    def check_stm_plus(self, node, ltype, rtype):
        """

        :param node:
        :param ltype:
        :param rtype:
        :return:
        """
        self.check_same_var(ltype, rtype)

        return ltype

    def sem_node(self, node):
        kind = node.type
        f = self.semfunc.get(kind, None)
        if f:
            r = f(node)
        else:
            raise Exception('not sem {}'.format(kind))

        return r

    def check_id(self, node):
        """
        校验 id
        :param node:
        :return:
        """
        kind = node.type
        if kind != Kind.id:
            raise Exception('expect ID but {}'.format(kind))

        return True

    def sem(self):

        self.sem_node(self.root)
