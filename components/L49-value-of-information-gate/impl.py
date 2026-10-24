# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (Process Iteration Primitives)
"""L49 — 信息价值闸（迭代经济学）

零依赖，stdlib only。python impl.py 看 demo；python selftest.py 跑断言。
"""


def l49_voi(p_flip, impact, cost):
    """信息价值 = 会因此改变决策的概率 × 决策影响 − 查证成本。

    p_flip: 这条信息有多大概率让你改主意（0-1）；impact: 决策值多少；
    """
    ev = p_flip * impact
    net = ev - cost
    return {
        "expected_value": round(ev, 2),
        "cost": cost,
        "net": round(net, 2),
        "verdict": "worth-it" if net > 0 else "not-worth-it",
        "note": "「知道了也不改主意」的信息，价值恒为 0——先问会不会改，再问好不好查",
    }


def l49_demo():
    for p, im, c in ((0.8, 100, 10), (0.05, 100, 10), (0.5, 10, 9), (0.9, 1000, 50)):
        print("  改主意概率%.2f 影响%.0f 成本%.0f -> %s" % (p, im, c, l49_voi(p, im, c)["verdict"]))


def l49_selftest():
    assert l49_voi(0.8, 100, 10)["verdict"] == "worth-it"
    assert l49_voi(0.05, 100, 10)["verdict"] == "not-worth-it"
    assert l49_voi(0.5, 10, 9)["net"] == -4.0
    return True


if __name__ == "__main__":
    l49_demo()
