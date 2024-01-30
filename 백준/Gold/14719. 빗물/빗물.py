height, width = map(int, input().split())
block = list(map(int, input().split()))

total_amount = 0

for i in range(1, width - 1):
    left_block_max_height = max(block[:i])
    right_block_max_height = max(block[i+1:])

    smaller_block_height = min(left_block_max_height, right_block_max_height)

    if block[i] < smaller_block_height:
        total_amount += smaller_block_height - block[i]

print(total_amount)