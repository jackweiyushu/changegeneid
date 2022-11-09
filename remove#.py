#因为从头预测的结果含有#行，不利于下面分析，去除#行
import sys
fclear = open(sys.argv[2],'w')
#去除含#的行
with open(sys.argv[1], 'r') as gff1:
        for line in gff1:
            if line[0]=="#":
                continue
            else:
                fclear.write(str(line))
fclear.close()
