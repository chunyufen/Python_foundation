# week 1/summary.md

input()
print()
eval()
print() formatted

# 註解

單行註：以#井號開頭，其後為註解內容。
多行註解：以'''三個單引號開頭和結尾。

# 數位

- 包含整數和浮點數
- 整數：數字中的整數，包含正整數和負整數。
- 浮點數：數學中的實數，有小數部分，包含正負數。

# 字串
- 單引號或雙引號所包括的有序字元；有序指有索引值。
- 如："123" 是字串，123 是數字。
- 如：
    - [-5, -4, -3, -2, -1]
    - '我是字串'
    - [0, 1, 2, 3, 4]
- 反向遞減 即表示倒數第幾個，最後一個為倒數第一個，即-1
- 取得單一字元：使用[]方括號取得字串中單一字符
    - 取得單一字串的格式：<字串>[索引]
    - '我是字串'[0] 回傳'我'
    - '我是字串'[-1],回傳'串'
- 切片：傳回字串中一段子字串
    - 取得子字串的格式：<字串>[M:N]
    - '我是字串'[1:3] 回傳'是字'，從1到3前，不包括3。
    - '我是字串'[0：-1],返回'我是字元'，從0到倒數第一個前，不包括倒數第一個。

# 清單

- 由 0 個或多個資料組成的有序序列。
    - ['F','C']
- 使用關鍵字 in 判斷一個元素是否在清單中
    - 'c' in ['C','c'] 返回布林值 True，如果前者不在列表中返回False

# 語句與函數

## 賦值語句

- 由賦值符號'='構成的一行程式碼

## 分支語句（if elif else）

- 由判斷條件決定程式運行方向的語句
- if True: 注意條件判斷後有冒號
    print('列印1') 注意在條件判斷內部程式碼區塊有程式碼縮排
- else：有冒號
- print('印製2')

## 函數

- 根據輸入參數產生不同輸出的功能過程
- 函数格式： <函数名> (<参数>)
- 這些都是函数
    - input()
    - eval()
    - print()

# python 程式的部分函數

## python程式的輸入與輸出

- 透過 input() 和 print()輸入和輸出

## input() 輸入函數

- 從控制台獲得使用者輸入內容的函數

- 格式：<變數> = input(<提示訊息字串>)
- TempStr = input('請輸入內容：')
- 使用input函數在控制台提示使用者輸入內容，並獲得使用者輸入的內容賦值給變數
- 注意：輸入的內容為字串格式傳回給變數

## print() 輸出函數

- 以字符形式向控制台輸出結果的函數
- #格式：print(<輸出字串或字串變數>)

## format() 格式化

- print()函數的格式化：
- print("轉換後的溫度是{:.2f}".format(C))
- 字符串内部的{}表示槽，後續變量填充到槽中
- {:.2f}表示將變量C填入這個位置時取小數點後2位

## eval() 評估函數

- 去掉參數最外側引號並執行餘下語句的函數，簡單叫評估函數。
- 格式： eval(<字串或字串變數>)
- eval('1') # 數字字串去掉引號變成數字
1
- eval('1+2') # 去掉引號後是語句1+2 執行它得到3
- eval('"1+2"') # 去掉引號是字串"1+2"
"1+2"
- eval('print("Hello")') # 去掉引號後是語句print("Hello")，執行它印出Hello