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
## here you have done your GitDorker task
cd GitDorker;python3 GitDorker.py -q ${target} -d Dorks/medium_dorks.txt -tf tf/TOKENSFILE -o ${output} -lb
mv "${output}_gh_dorks.csv" "./../";cd ..
python3 cleaning.py -f "${output}_gh_dorks.csv" -o ${output}
rm -rf "${output}_gh_dorks.csv"
mv "${output}.txt" "./TestingData/${target}/${output}_gitdork.txt"
python3 remove-pending.py -p $target
## starting the attack => 
## Attack for VPS => subdomains-enumeration + urlcollection
sleep 2m 15s
python3 topush-remove.py -p $target
echo "NotWorking" > presently.txt
#sleep 1m 1s
python3 attack_done.py -t $target
#rm -rf "./TestingData/${target}"
#rm -rf "./TestingData/${target}.txt"
else
echo "Rest!"
fi
fi
#read -r firstpending<test.txt
