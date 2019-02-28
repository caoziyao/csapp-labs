# coding: utf-8


from lang.base.kind import Kind


def is_leaf(node):
    """

    :param node:
    :return:
    """
    _type = node.type

    if _type in [Kind.number, Kind.id]:
        return True
    else:
        return False
