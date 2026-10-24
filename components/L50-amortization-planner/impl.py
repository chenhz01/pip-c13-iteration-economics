# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (Process Iteration Primitives)
"""L50 — 摊销规划（迭代经济学）

零依赖，stdlib only。python impl.py 看 demo；python selftest.py 跑断言。
"""


def l50_amortize(one_time, per_use_saving, uses):
    """一次性投入能否被 N 次复用摊平：回本点 = 投入 / 每次节省。"""
    if per_use_saving <= 0:
        return {"breakeven": None, "verdict": "never-pays", "note": "每次不省，永远回不了本"}
    be = one_time / per_use_saving
    return {
        "breakeven_uses": round(be, 2),
        "uses": uses,
        "net": round(per_use_saving * uses - one_time, 2),
        "verdict": "pays-off" if uses >= be else "not-yet",
        "note": "回本点 %.1f 次；预计用 %d 次" % (be, uses),
    }


def l50_demo():
    for ot, sv, u in ((1000, 100, 20), (1000, 100, 5), (500, 0, 100)):
        print("  投入%-5d 每次省%-4d 用%-3d次 -> %s" % (ot, sv, u, l50_amortize(ot, sv, u)))


def l50_selftest():
    r = l50_amortize(1000, 100, 20)
    assert r["breakeven_uses"] == 10.0 and r["verdict"] == "pays-off" and r["net"] == 1000
    assert l50_amortize(1000, 100, 5)["verdict"] == "not-yet"
    assert l50_amortize(500, 0, 100)["verdict"] == "never-pays"
    return True


if __name__ == "__main__":
    l50_demo()
