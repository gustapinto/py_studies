text1 = 'Hello'
text2 = 'World'

print('hello world')  # The simple way

print('{} {}'.format(text1, text2))  # The ordered way

print('{hello} {world}'.format(world=text2, hello=text1))  # The named way

print(f'{text1} {text2}')  # The f'{}' way
