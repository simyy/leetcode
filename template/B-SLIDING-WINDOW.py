# -*- coding: utf-8 -*-


def sliding_window(S, T):
    """
    滑动窗口
    :param S: 源字符串
    :param T: 目标字符串(可重复)
    :return:
    """
    from collections import defaultdict

    matches = 0
    needs = defaultdict(int)
    window = defaultdict(int)
    for a in T:
        needs[a] += 1

    left, right = 0, 0
    while right < len(S):
        # Sliding Right
        window[S[right]] += 1
        if window[S[right]] == needs[S[right]]:
            matches += 1
        right += 1
        """
        Sliding Left
        """
        # Match all the chars in T
        while matches == len(needs):
            print left, right, S[left:right]
            if S[left] in needs:
                if window[S[left]] == needs[S[left]]:
                    matches -= 1
                window[S[left]] -= 1
            left += 1


if __name__ == '__main__':
    sliding_window("abcabcc", "abcc")