from deepdiff import DeepDiff



f1 ={"param":{"shuId":123,"num":10}}
f2 ={"param":{"shuId":222,"num":10}}

qq=DeepDiff(f1,f2)
print(qq)