#!/bin/bash
read -r presently<presently.txt
if [ $presently == "working" ];
then
echo "working"
else
#echo $presently
## here we will do what actually the attack is , after finishing the attack we have to make a change to 
## at last, after completion of attack , making presently.txt to not working
## just for testing => mkdir hello.txt
read -r firstpending<pending.txt
if [ ${#firstpending} -gt 1 ];
then
echo "Locking ${firstpending} for attack ---===>>>"
rm -rf presently.txt
echo "working" >> presently.txt
## making target and output variable
# Setting IFS (input field separator) value as "."
target=${firstpending}  # storing target
IFS='.'
# Reading the split string into array
read -ra arr <<< "$firstpending"

# Print each value of the array by using the loop
#for val in "${arr[@]}";
#do
#  printf "name = $val\n"
#done
#echo ${arr[-2]}
output=${arr[-2]}
IFS=','  ## after completion of task we are making IFS disable by puting nonsense value so it won't create any problem
echo $target
echo $output
mkdir "./TestingData/${target}"
echo "${target}" >> "./TestingData/topush.txt"
./subfind.sh $target $output
./refine.sh "${output}_subdomains.txt" ${output}
./filtering.sh "${output}_subdomains.txt" ${output}
cp "${output}_subdomains.txt" "./TestingData/${target}/"
sleep 2m 30s
python3 SetTarget.py -t $target
./domain-s3-check.sh $target $output
rm -rf "${output}_subdomains.txt"
python3 remove-pending.py -p $target
## Attack for VPS => subdomains-enumeration
sleep 2m 15s
python3 topush-remove.py -p $target
rm -rf presently.txt
echo "NotWorking" >> presently.txt
sleep 1m 1s
python3 attack_done.py -t $target
rm -rf "./TestingData/${target}"
rm -rf "./TestingData/${target}.txt"
else
echo "Rest!"
fi
fi
#read -r firstpending<test.txt
