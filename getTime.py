import re
import pyperclip

# 事前に勢力図などからログをコピーしよう
country = "なきうさぎ連合"  # 自分の所属する国を入れよう
opponentCountry = "便利屋68"  # 戦ってる相手の国を入れよう

logStr = pyperclip.paste()
opponentCountryLength = len(opponentCountry)
pattern = r"・【戦闘】.*?(?:\d{1,2}日\d{1,2}時\d{1,2}分)"
matchString = re.findall(pattern, logStr)


nameList = []
namePattern = rf"【戦闘】(.+)は.+?(?:{country})"
for s in matchString:
    if f"({country})へ" in s:
        matchS = re.search(namePattern, s)
        matchGroupString = matchS.group(1)
        matchGLength = len(matchGroupString)
        sliceEnd = matchGLength - (opponentCountryLength + 2)
        matchStr = matchGroupString[:sliceEnd]
        nameList.append(matchStr)
nameList.reverse()

timeList = []
timePattern = r"時(\d{1,2})分"
for s in matchString:
    if f"({country})へ" in s:
        matchS = re.search(timePattern, s)
        timeList.append(matchS.group(1))
timeList.reverse()

attackTime = []
for i, n in enumerate(timeList):
    n = int(n)
    nPlusTen = (n + 10) % 60
    nToStr = str(nameList[i]) + " (" + str(n) + "分or" + str(nPlusTen) + "分)"
    attackTime.append(nToStr)
result = "、".join(attackTime)
print(result)
filename = "time.txt"
with open(filename, "w", encoding="Shift-JIS") as f:
    print(result, file=f)
