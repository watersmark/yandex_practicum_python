def tree_step(count_even, lvl, seq="(", count_odd=1):

    if count_even + count_odd >= lvl * 2:
        print(seq)
        return

    # идём налево но не больше шагов, чем на lvl
    if count_odd < lvl:
        tree_step(count_even, lvl, seq + '(', count_odd + 1)

    # идём направо только если count_odd > count_even
    if count_odd > count_even:
        tree_step(count_even + 1, lvl, seq + ')', count_odd)


lvl = int(input())
tree_step(0, lvl, seq='(', count_odd=1)
