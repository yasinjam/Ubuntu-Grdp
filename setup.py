import pexpect
child = pexpect.spawn ('bash setup.sh')
child.expect ('Enter a PIN of at least six digits: ')
child.sendline ('556677')
child.expect ('Enter the same PIN again: ')
child.sendline ('556677')
print child.before
child.interact()
