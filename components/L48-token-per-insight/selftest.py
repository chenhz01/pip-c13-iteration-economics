# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (Process Iteration Primitives)
"""L48 selftest — 断言写在实现旁边，改坏了立刻红。"""
import impl


def main():
    impl.l48_selftest()
    print("PASS L48 token-per-insight")


if __name__ == "__main__":
    main()
