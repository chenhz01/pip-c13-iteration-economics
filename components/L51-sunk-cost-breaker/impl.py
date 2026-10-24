# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (Process Iteration Primitives)
"""L51 — 沉没成本断路（迭代经济学）

零依赖，stdlib only。python impl.py 看 demo；python selftest.py 跑断言。
"""


def l51_continue(spent, remaining_expected, cost_to_finish, p_success=1.0):
    """只看「从现在起」：未来净收益 = 成功概率×剩余期望 − 完工成本。

    已花的不进公式。这不是冷酷，是唯一正确的算法。
    """
    future = p_success * remaining_expected - cost_to_finish
    roi = future / cost_to_finish if cost_to_finish else None
    return {
        "sunk_ignored": spent,
        "future_net": round(future, 2),
        "roi": round(roi, 3) if roi is not None else None,
        "verdict": "stop" if future <= 0 else ("continue-narrow" if roi is not None and roi < 0.2 else "continue"),
        "note": "已投入 %.0f 与这个决定无关；只看未来净收益" % spent,
    }


def l51_demo():
    for sp, rem, cst, p in ((10000, 5000, 1000, 0.9), (10000, 500, 1000, 0.9),
                            (100, 900, 1000, 0.9), (100, 5000, 1000, 0.3)):
        r = l51_continue(sp, rem, cst, p)
        print("  已花%-6d 剩余期望%-5d 完工成本%-5d p=%.1f -> %s (未来净%.0f)"
              % (sp, rem, cst, p, r["verdict"], r["future_net"]))


def l51_selftest():
    assert l51_continue(10000, 5000, 1000, 0.9)["verdict"] == "continue"
    assert l51_continue(10000, 500, 1000, 0.9)["verdict"] == "stop"
    # 已花多少都不影响判决
    a = l51_continue(0, 500, 1000, 0.9)["verdict"]
    b = l51_continue(999999, 500, 1000, 0.9)["verdict"]
    assert a == b == "stop"
    return True


if __name__ == "__main__":
    l51_demo()
