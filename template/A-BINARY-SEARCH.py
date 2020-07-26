# -*- coding: utf-8 -*-


def binary_search(nums, target):
    """
    普通二分查找
    """
    if not nums:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) / 2
        num = nums[mid]
        if num == target:
            return mid
        elif num > target:
            right = mid
        else:
            left = mid + 1
    # 注意结束条件
    if right == 0 or left >= len(nums):
        return -1
    return left


def binary_search_left_bound(nums, target):
    """
    左边界
    :param nums:
    :param target:
    :return:
    """
    if not nums:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) / 2
        num = nums[mid]
        if num == target:
            right = mid
        elif num > target:
            right = mid
        else:
            left = mid + 1
    # 注意结束条件
    if left >= len(nums):
        return -1
    if right == 0 and nums[left] != target:
        return -1
    return left


def binary_search_right_bound_1(nums, target):
    """
    右边界
    :param nums:
    :param target:
    :return:
    """
    if not nums:
        return -1
    pre = -1
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) / 2
        num = nums[mid]
        if num == target:
            pre = mid
            left = mid + 1
        elif num > target:
            right = mid
        else:
            left = mid + 1
    return pre


def binary_search_right_bound(nums, target):
    """
    有边界，有问题，左闭右开区间
    :param nums:
    :param target:
    :return:
    """
    if not nums:
        return -1
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) / 2
        num = nums[mid]
        if num == target:
            if mid+1 < len(nums) and nums[mid+1] == target:
                left = mid + 1
            else:
                return mid
        elif num > target:
            right = mid
        else:
            left = mid + 1
    # 注意结束条件
    if left >= len(nums):
        return -1
    if right == 0 and nums[left] != target:
        return -1
    return left


def test_binary_search():
    assert binary_search([2, 3, 4, 5], 1) == -1
    assert binary_search([2, 3, 4, 5], 6) == -1
    assert binary_search([2, 3, 4, 5], 2) == 0
    assert binary_search([2, 3, 4, 5], 3) == 1
    assert binary_search([2, 3, 4, 5], 4) == 2
    assert binary_search([2, 3, 4, 5], 5) == 3


def test_binary_search_left_bound():
    assert binary_search_left_bound([2, 3, 3, 5], 1) == -1
    assert binary_search_left_bound([2, 3, 3, 5], 6) == -1
    assert binary_search_left_bound([2, 3, 3, 5], 2) == 0
    assert binary_search_left_bound([2, 3, 3, 5], 5) == 3
    assert binary_search_left_bound([2, 3, 3, 5], 3) == 1


def test_binary_search_right_bound():
    assert binary_search_right_bound([2, 3, 3, 5], 1) == -1
    assert binary_search_right_bound([2, 3, 3, 5], 6) == -1
    assert binary_search_right_bound([2, 3, 3, 5], 2) == 0
    assert binary_search_right_bound([2, 3, 3, 5], 5) == 3
    assert binary_search_right_bound([2, 3, 3, 5], 3) == 2


if __name__ == '__main__':
    # test_binary_search()
    # test_binary_search_left_bound()
    test_binary_search_right_bound()