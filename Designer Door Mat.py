height, width = map(int,input().split())

pattern = [('.|.'*(2*i + 1)).center(width, '-') for i in range(height//2)]

print('\n'.join(pattern + ['WELCOME'.center(width, '-')] + pattern[::-1]))
