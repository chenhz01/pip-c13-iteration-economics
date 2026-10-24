# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (Process Iteration Primitives)
"""L48 — 每洞见成本（迭代经济学）

零依赖，stdlib only。python impl.py 看 demo；python selftest.py 跑断言。
"""


def l48_cost(tokens, insights, dedup=True):
    """insights: 字符串列表。去重后才是「新洞见」——重复三遍不算三个。"""
    uniq = list(dict.fromkeys(insights)) if dedup else list(insights)
    n = len(uniq)
    cost = tokens / n if n else None
    return {
        "tokens": tokens,
        "insights_raw": len(insights),
        "insights_unique": n,
        "duplicate_rate": round(1 - n / len(insights), 3) if insights else 0.0,
        "token_per_insight": round(cost, 1) if cost else None,
        "verdict": "expensive" if cost and cost > 2000 else ("ok" if cost else "no-insight"),
        "note": "洞见为 0 时，本轮成本是纯消耗——这是唯一需要立刻停的情况",
    }


def l48_demo():
    r = l48_cost(12000, ["负结论A", "负结论A", "负结论B"])
    print("  ", r)
    print("  零洞见:", l48_cost(8000, [])["verdict"])


def l48_selftest():
    r = l48_cost(12000, ["a", "a", "b"])
    assert r["insights_unique"] == 2 and r["token_per_insight"] == 6000.0
    assert r["duplicate_rate"] == round(1 - 2 / 3, 3)
    assert l48_cost(1, [])["token_per_insight"] is None
    assert l48_cost(100, ["a"])["verdict"] == "ok"
    return True


if __name__ == "__main__":
    l48_demo()
