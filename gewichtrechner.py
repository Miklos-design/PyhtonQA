weight= input ("Tell me your weight: ")
parameters= input ("In LBS or KG: ")
weight_inkg= int(weight)/4
weight_inlbs= int(weight)*4

if weight.upper == "L":
    print(weight_inkg)
elif weight == "K" or "k":
    print(weight_inlbs)