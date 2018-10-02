# hex_hmac = ClientCmd|<user>|<command>
# <user>;<command>;<hex hmac><lf>

user="728214"
command=""
key="12345678901234567890"
command="help"
# help + 26 of a + key of 20
for i in $(seq 0 26)
do
    command+="a"
done
command+="$key"
#command="help"
# 42+32 = 74
# 27 + 5 = 32

hex_hmac_input="ClientCmd|$user|$command"
hex_hmac_output=$(echo -n $hex_hmac_input | openssl sha256 -hmac $key -hex | sed 's/^.* //')
output="$user;$command;$hex_hmac_output\n"
echo -e $output > result.txt
nc device1.vikaa.fi 33656 < result.txt
printf "\n"
