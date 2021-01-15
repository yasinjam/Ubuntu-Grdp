expect -c '
spawn ./yo.sh
expect "Enter a PIN of at least six digits: "
send "123456\r"
expect "Enter the same PIN again: "
send "123456\r"
expect eof
'
