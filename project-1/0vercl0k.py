'''
迭代是Python最强大的功能之一，是访问集合元素的一种方式。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器：
'''


class Thread:
    Obj = []  # 定义一个数组
    Index = 0  # 定义一个索引长度
    AllocLength = 100  # 定义分配长度

    def __init__(self):  # 构造函数
        for i in range(self.AllocLength):
            self.Obj.append(i)

    def __iter__(self):  # 迭代函数  用于转换迭代器，并且将Index索引为0
        self.Index = 0
        return self  # 将self成员变量返回给调用者

    def __next__(self):  # 下一个操作， 看函数代码逻辑 ，将index加1 并且返回对应的值   因为前面加了1 数据需要对准才行所以也 减1
        if self.Index <= self.AllocLength:
            self.Index += 1
            return self.Obj[self.Index - 1]
        else:
            raise StopIteration  # 超过就通过 raise 触发异常

    def __int__(self):
        return self.Obj[self.Index]  # 使用int类型时直接输出当前索引位置的值


if __name__ == '__main__':
    '''基本迭代器
    迭代器对该List进行 容器封装
    列表与迭代器区别一个是起始位置可控，最后位置可控。
    每一次遍历，起始位置和更多参数迭代器不会发生变化
    列表只能充当变量型的使用，虽然Python已经给其封装了一些功能，但是还是有很多缺陷。
    '''
    # 普通列表
    List = [1, 2, 3, 4, 5]

    Index = 0
    print("Index:%d = %d" % (Index, List[Index]))
    Index += 1
    print("Index:%d = %d" % (Index, List[Index]))
    Index = 0

    for i in List:
        print(f"List[{Index}] = {i}")
        Index += 1

    # 通过长度进行遍历
    for Index in range(len(List)):
        print(f"List[{Index}] = {List[Index]}")

    # 转换迭代器
    Iter = iter(List)  # 转化为迭代器
    print("================= Iter =====================")
    # 迭代器 是通过 next 去实现定位下一个表头
    print("Text:%d" % next(Iter))  # 定位下一个表头，并且返回下一个表头的值
    print("Text:%d" % next(Iter))  # 定位下一个表头，并且返回下一个表头的值
    print("Text:%d" % next(Iter))  # 定位下一个表头，并且返回下一个表头的值
    print("Text:%d" % next(Iter))  # 定位下一个表头，并且返回下一个表头的值
    print("Text:%d" % next(Iter))  # 定位下一个表头，并且返回下一个表头的值

    try:
        print("Text:%d" % next(Iter))  # 定位下一个表头，并且返回下一个表头的值
    except StopIteration:
        print("StopIteration ")  # 如果遍历超过了长度就会报StopIteration错误。

    Iter = iter(List)
    # 也可以直接使用for直接循环
    for i in Iter:
        print(i)
    # 看到这里发现跟列表没啥区别。所以演示一波使用
    print("---------------- Class  -----------------")
    # 看上面Thread类
    thObj_Object = Thread()
    thObj = iter(thObj_Object)

    print(next(thObj))
    print(next(thObj))
    print(next(thObj))
    print(next(thObj))
# 小结 迭代器是一种非常强大的数据结构，但是其只能进行一些遍历等等操作。  通过迭代器 可以使遍历代码更优雅规范。
