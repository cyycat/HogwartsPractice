"""
1、怎么点击按钮

2、怎么在输入框中输入内容

3、怎么定位元素 （ID、name、css、xpath）——》 xpath  、 css

"""

"""
1、xpath  定位元素
定义：
XML Path Language
用于解析html与xml

作用于：appium、selenium
缺点：比较慢，因为xpath是从头到尾的一点点去遍历，从而导致速度慢

xpath 常用操作
id和name 基本可以唯一找到一个页面元素
用id和name属性，再根据层次间的关系，可以定位到99%的元素
$x('//*[@id="1"]//h3')

"""

"""
2、css selector
作用于：appium、selenium   （注意：appium原生控件是不支持css selector的，手机APP中嵌套网页webview，此时可以用css selector）
优点：速度快，css selector是用样式进行定位的，所以比较快

写法：本质与xpath一致，写法稍有不同
$('#s_tab a:nth-last-child(1)')   等价于   $('[id="s_tab"] a:nth-last-child(1)')
"""