#分段从头预测会出现重复id,对基因id从头排列
import sys
name_list=[]
index=0
fout = open(sys.argv[3],'w')
with open(sys.argv[1], 'r') as gff1:
    for eachline in gff1:
        line_s = eachline.strip().split('\t')
        if 'gene' == line_s[2]:
            index += 1
            ref_g = 'g'+str(index)
            name_list.append(ref_g)
        else:
            name_list.append(ref_g)

index1=0
with open(sys.argv[2]) as gff_r:
    for eachline in gff_r:
        i = eachline.strip().split('\t')
        ref_set = []
        for n in range(0, 8):
            ref_set.append(i[n])
        ref_list = '\t'.join(ref_set)
        if 'gene' == i[2]:
            fout.write('%s\tID=%s\n'%(ref_list,name_list[index1]))
            index1+=1
            continue
        elif 'transcript' == i[2]:
            fout.write('%s\tID=%s.t1;Parent=%s\n'%(ref_list,name_list[index1],name_list[index1]))
            index1+=1
            continue
        elif 'CDS' == i[2]:
            fout.write('%s\tID=%s.t1.cds;Parent=%s.t1\n'%(ref_list,name_list[index1],name_list[index1]))
            index1+=1
            continue
        else:
            fout.write('%s\tParent=%s.t1\n' %(ref_list, name_list[index1]))
            index1 += 1
            continue
fout.close()
