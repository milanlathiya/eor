# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:01:42 2020

@author: Project2020 group
"""

a=int(input("gravity API"))
b=float(input("viscocity cp"))
b=int(b)
c=int(input("oil saturation%"))
d=int(input("formation type for sandstone- press 1, carbonate - press 2, tar sand - press 3"))
e=int(input("depthft"))

#nitrogen and flue gas
if a>35 and b>=0 and c>40 and (d==1 or 2) and e>=6000:
    if a<48 and b<=1 and c<75:
        npa=(a-35)/(48-35)
        npb=1-(b)
        npc=(c-40)/(75-40)
        print("nitrogen and flue gas is applicable with ",(npa+npb+npc)*100/3,"%")
    
#hydrocarbon injection
if a>23 and b>=0 and c>30 and (d==1 or 2) and e>=4000:
    if a<41 and b<=3 and c<80:
        hpa=(a-23)/(41-23)
        hpb=1-(b/3)
        hpc=(c-30)/(80-30)
        print("Hydrocarbon is applicable with ",(hpa+hpb+hpc)*100/3,"%")

#co2 injection
if a>22 and b>=1 and c>20 and (d==1 or 2) and e>=2500:
    if a<36 and b<=10 and c<55:
        cpa=(a-22)/(36-22)
        cpb=1-((b-1)/(10-1))
        cpc=(c-20)/(55-20)    
        print("CO2 gas is applicable with ",(cpa+cpb+cpc)*100/3,"%")

#immiscible gas injection
if a>12 and b<=600 and c>35 and (d==1 or 2) and e>=1800:
    if c<70:
        ipa=(a-12)/(50-12)
        ipb=1-(b/600)
        ipc=(c-35)/(70-35)     
        print("Immiscible gas is applicable with ",(ipa+ipb+ipc)*100/3,"%")

#Micellar polymer ASP/alkaline
if a>20 and b>=13 and c>35 and d==1 and e>=9000:
    if a<35 and b<=35 and c<53:
        mpa=(a-20)/(35-20)
        mpb=1-((b-13)/(35-13))
        mpc=(c-35)/(70-35)      
        print("Micellar polymer ASP/alkaline is applicable with ",(mpa+mpb+mpc)*100/3)

#polymer flooding
if a>15 and b>=10 and c>50 and d==1 and e<=11500:
    if b<=150 and c<80:
        ppa=(a-15)/(50-15)
        ppb=1-((b-10)/(150-10))
        ppc=(c-50)/(80-50) 
        print("polymer flooding is applicable with ",(ppa+ppb+ppc)*100/3)

#combustion 
if a>35 and b>=1200 and c>50 and d==1 and e<=11500:
    if a<48 and b<=5000 and c<72:
        cmpa=(a-35)/(48-35)
        cmpb=1-((b-1200)/(5000-1200))
        cmpc=(c-50)/(72-50)     
        print("combution is applicable with ",(cmpa+cmpb+cmpc)*100/3)

#steam
if a>8 and b>=4700 and c>40 and d==1 and e<=4500:
    if a<14 and b<=200000 and c<66:
        cmpa=(a-8)/(14-8)
        cmpb=1-((b-4700)/(200000-4700))
        cmpc=(c-40)/(66-40)  
        print("steam is applicable with ",(cmpa+cmpb+cmpc)*100/3)

#surface mining
if d==3:
    print("surface mining is applicable with","100%")


