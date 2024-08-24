# Explanation
## what is primitive element of the group?
primitive element in a finite field 𝐹𝑞, each power of the element must produce a different, non-zero element of the field until all the non-zero elements have been generated.
## Example
![Screenshot_2024-08-25_00-05-54](https://github.com/user-attachments/assets/47cd88ec-08b7-41ee-9933-7c17b4062856)
![Screenshot_2024-08-25_00-06-48](https://github.com/user-attachments/assets/99a299f8-0168-4394-a413-4d398c19a513)

# Code
```python
base=2
p=28151

while 1:
    sisa=1
    ans=[]
    finish=True
    for i in range (p-1):
        sisa=(base*sisa)%p
        if sisa in ans:
            finish=False
            break
        else: ans.append(sisa)
    if finish:
        print("result=",base)
        break
    print(base)
    base+=1
```
