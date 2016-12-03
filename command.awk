awk 'BEGIN{FS = "\t";total = 0}{print $3;total+=$3}END{print "average = " (total/6338)}' baker_glyco.txt 

echo 'baker_glyco.txt' | xargs -I filename wc -l filename | xargs -n1 -I {} awk 'BEGIN{FS = "\t";total = 0}{print $3,total+=$3}END{print (total/6338)}' filename

awk '{print $1}' nglycotmcommon.txt | xargs -n1 -I {} grep {} tmonly.txt // not useful

 awk '{print $1 }' second.txt | xargs -I name sed -i.sfu '/name/d' first.txt // real code to obtain first-second file. 

awk '{print $1}' ~/desktop/file/N-glyco-TM-common/baker.txt | xargs -I name sed -i.txt '/name/d' ~/desktop/file/TM_only/baker.txt // order of file : small -> big

awk '{print $1}' ~/desktop/file/ngtc/human.txt | xargs -I {} sed -i.txt '/{}/d' ~/desktop/file/TM_only/human.txt

awk 'BEGIN{FS = "[|-]"}{print $2}'

awk '{print $1}' ~/desktop/N-glyco/baker.txt | xargs -I {} sed -i.txt '/{}/d' ~/desktop/real/baker.txt