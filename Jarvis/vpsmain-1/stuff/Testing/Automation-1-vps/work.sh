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
mkdir "./TestingData/${target}/${target}_domain"
echo "${target}" >> "./TestingData/topush.txt"
#./subfind.sh $target $output
##python3 download.py -d $target ## instead of downloding we will copy this locally
cp -r "/media/boxlogin/ExtraStuff1/hunt/PenTest/${target}" .
mv $target/"${output}_subdomains.txt" .
rm -rf $target
python3 domain-status-checker.py -f "${output}_subdomains.txt"
mv *"${output}.txt" "./TestingData/${target}/${target}_domain"
python3 launch_dir.py -t ${target} -p "./TestingData/${target}/${target}_domain"
rm -rf "${output}_subdomains.txt"
## launching the image capturer
./imagecapture.sh $target $output
python3 remove-pending.py -p $target
## starting the attack => 

## Attack for VPS => subdomains-enumeration + status check
sleep 2m 2s
python3 topush-remove.py -p $target
rm -rf presently.txt
echo "NotWorking" >> presently.txt
sleep 30s
python3 attack_done.py -t $target
sleep 59s
#rm -rf "./TestingData/${target}"
#rm -rf "./TestingData/${target}.txt"
else
echo "Rest!"
fi
fi
#read -r firstpending<test.txt
