#Ascii.py
asc码自动转码
比如输入6611753
自动转换成字母
Bu2
第一版<br>：
        
从末尾三个数字开始匹配
如果小于122就保留
不是就从末尾两个进行匹配
以此类推
第二版<br>：
        
从末尾三个数字开始匹配
如果小于122就保留
不是就从末尾两个进行匹配
以此类推
总体完成逻辑
突然觉得有问题，回去修改一下。。。。
第三版<br>：
        
从末尾三个数字开始匹配<br>
如果小于122就保留<br>
不是就从末尾两个进行匹配<br>
以此类推<br>
def __init__(self,pic_id):<br>
构造函数时输入你想要转码的数字<br>
比如说107107107<br>
注意要写入的数字必须为str<br>
def start(self):<br>
开始函数<br>
a=asc_change("107107107")<br>
实例化类后<br>
直接a.start()开始执行转码<br>
最终会return一个res字符串<br>
就是答案了<br>
def find(self,pic_id,times):<br>
逻辑匹配函数<br>
def cut_down(self,pic_id,times):<br>
原字符串匹配后去掉已匹配的字符串<br>
##有问题随时留言即可
