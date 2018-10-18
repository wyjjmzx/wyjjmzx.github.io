from itertools import combinations as cb
#设置条件

maxSkill = [5,5,5]
bestSkill = [1,5,1]


#初始化
a = [[[0 for i in range(6)] for j in range(6)] for k in range(6)]
b = [[[0 for i in range(6)] for j in range(6)] for k in range(6)]

#定义正反喂分别返回的期望资源消耗值
def wantSkill(ijk):
    if ijk[0]>=bestSkill[0] and ijk[1]>=bestSkill[1] and ijk[2]>=bestSkill[2]:
        return True
    else:
        return False
        
def 正喂(b,ijk):
    ret=0
    canAddSkill=0
    if wantSkill(ijk):
        return ret
    for t in range(3):
        if ijk[t] >= maxSkill[t]:
            continue
        canAddSkill+=1
        ni,nj,nk=[ijk[tt]+1 if tt==t else ijk[tt] for tt in range(3)]
        ret+=b[ni][nj][nk]
    ret/=canAddSkill
    ret+=1
    return ret

def 反喂(b,ijk):
    ret=0
    total=sum(ijk)
    if wantSkill(ijk):
        return ret
    if total >= sum(maxSkill):
        return ret
    total-=2
    prob1=[1]
    prob2=[]
    temp1=[[1,1,1]]
    temp2=[]
    for _ in range(total):
        for i in range(len(temp1)):
            tempijk=temp1[i]
            canAddSkillNum=3#判断每个技能下次能加多少个技能
            for t in range(3):
                if tempijk[t] >= maxSkill[t]:
                    canAddSkillNum-=1
            for t in range(3):
                if tempijk[t] >= maxSkill[t]:
                    continue
                ni,nj,nk=[tempijk[tt]+1 if tt==t else tempijk[tt] for tt in range(3)]
                if [ni,nj,nk] not in temp2:
                    temp2.append([ni,nj,nk])
                    prob2.append(1/canAddSkillNum*prob1[i])
                else:
                    for ii in range(len(temp2)):
                        if [ni,nj,nk]==temp2[ii]:
                            prob2[ii]+=1/canAddSkillNum*prob1[i]
        prob1=prob2
        prob2=[]
        temp1=temp2
        temp2=[]
    for i in range(len(temp1)):
        ret+=b[temp1[i][0]][temp1[i][1]][temp1[i][2]]*prob1[i]
    ret+=1
    return ret
print("注释：\n“当前技能”是指当前技能的情况，如121表示技能为1，2，1；\n“正反策略”为应当进行的正反喂策略，其中1表示正喂，-1表示反喂，0表示两者无差别；\n“消耗期望”是指按照最优策略加满技能的期望。因为浮点数的缘故，数据可能有正负0.01的误差\n")
print("当前假设：满技能为",*maxSkill,"，最节省资源的达到目标的技能为",*bestSkill,"。\n",sep="")
print("当前技能","正反策略","正喂消耗","反喂消耗",sep="\t")
for total in range(sum(maxSkill),2,-1):
    temp=list(range(1,total))
    all=cb(temp,2)
    ijk=[0,0,0]
    for temp in all:
        ijk[0]=temp[0]
        ijk[1]=temp[1]-temp[0]
        ijk[2]=total-temp[1]
        if ijk[0]>maxSkill[0] or ijk[1]>maxSkill[1] or ijk[2]>maxSkill[2]:
            continue
        ret1=正喂(b,ijk)
        ret2=反喂(b,ijk)
        if ret1-ret2<0.01 and ret1-ret2>-0.01:
            b[ijk[0]][ijk[1]][ijk[2]]=ret1
        elif ret1<ret2:
            a[ijk[0]][ijk[1]][ijk[2]]=1
            b[ijk[0]][ijk[1]][ijk[2]]=ret1
        elif ret1>ret2:
            a[ijk[0]][ijk[1]][ijk[2]]=-1
            b[ijk[0]][ijk[1]][ijk[2]]=ret2

        #print(*ijk,"\t\t",a[ijk[0]][ijk[1]][ijk[2]],"\t\t","%.2f"%b[ijk[0]][ijk[1]][ijk[2]],sep="")
        print(*ijk,"\t\t",a[ijk[0]][ijk[1]][ijk[2]],"\t\t","%.2f"%ret1,"\t\t%.2f"%ret2,sep="")
            
input()




