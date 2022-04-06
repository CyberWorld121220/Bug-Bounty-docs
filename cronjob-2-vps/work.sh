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
mkdir "./TestingData/${target}/${target}_dir"
python3 download_403.py -d ${target}
cat "list403_${output}.txt" | httprobe | sort -u >> "${output}.txt"
cd "Tools/dirsearch/";python3 dirsearch.py -l "./../../${output}.txt" -o "./../../${output}_dir.txt"; cd ../../
python3 remove-pending.py -p $target
mv "${output}_dir.txt" "./TestingData/${target}/${target}_dir/"
rm -rf "${output}.txt"
## starting the attack => 
echo "${target}" >> "./TestingData/topush.txt"
## Attack for VPS => subdomains-enumeration + status check
sleep 2m 2s
python3 topush-remove.py -p $target
rm -rf presently.txt
echo "NotWorking" >> presently.txt
sleep 30s
python3 attack_done.py -t $target
else
echo "Rest!"
fi
fi
#read -r firstpending<test.txt
