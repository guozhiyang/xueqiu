过期原因

## 背景：

```
应该是无用户登录状态下，最长的cookie有效期为一个月（后面可以尝试登录状态下，测试看看具体cookie能保持登录时间）
```



## 恢复步骤：

```
大体思路为整个cookie过期了，包括以下三个文件：
gettop100_toexcel_file.py （图1）
getRebalancestock.py （图2）
second_copy.py（图3）
```

图1

![1610012182915](C:\Users\61631\AppData\Roaming\Typora\typora-user-images\1610012182915.png)



图2

![1610012249335](C:\Users\61631\AppData\Roaming\Typora\typora-user-images\1610012249335.png)

图3

​	![1610012273548](C:\Users\61631\AppData\Roaming\Typora\typora-user-images\1610012273548.png)



### 图1恢复

```
1、使用burp suite进行流量拦截

```

```
2、找到具体的top100的链接。（在HTTP history里面找最长的length）
```

https://api.xueqiu.com/cubes/rank/arena_cubes.json?count=20&cube_level=1&list_param=list_overall&market=cn&page=1&_=1610009452248&_s=650924&_t=DA4FF810-74FC-4B3C-A65B-CFEE8A243EFA.5007108385.1610009149412.1610009425251

![1610012413933](C:\Users\61631\AppData\Roaming\Typora\typora-user-images\1610012413933.png)

```
3、将请求发送到repeater中
```

![1610012482727](C:\Users\61631\AppData\Roaming\Typora\typora-user-images\1610012482727.png)

```
4、粘贴其中的cookie项的值。如
GET /cubes/rank/arena_cubes.json?count=20&cube_level=1&list_param=list_overall&market=cn&page=1&_=1610009452248&_s=650924&_t=DA4FF810-74FC-4B3C-A65B-CFEE8A243EFA.5007108385.1610009149412.1610009425251 HTTP/1.1
Host: api.xueqiu.com
Accept: application/json
Accept-Encoding: gzip, deflate
Connection: close
Cookie: xq_a_token=e4d5a3cf69a131e0dd1f402eb65e66dc3fcdab27;xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOjUwMDcxMDgzODUsImlzcyI6InVjIiwiZXhwIjoxNjEyNjAwNjExLCJjdG0iOjE2MTAwMDg2MTEyNzEsImNpZCI6IldpQ2lteHBqNUgifQ.dbBPgvEBMjy67oXq6gmFRi9Q8VCID1FOliYIBNNHGhFrWQPmK7AOXB3H0ORZ2Gd_3sQvqSPzUzf8UvWErL7dTx1MA4MKf0kPCM_P4-KOR88xuRDpE9PSh-N_JKzoriiQdGyN_Cy1kp1qvzQf-dTTRms06oPUvNJnPHCZZQqziGIN7JIgLvHv2zLNiD6d-Kis86vszSNn6o3SGdkK8rxMP33h7TM0NCftb7nVpTHmVrWjkcmEtEFTfQ0xUPuLCV-l2yJthjaJMySkdmrzQuw0Adj-X7k4Od-YrnbJFeI_WvZ0E2qLjZfsLf1q4pkG7Ita2ztGBAJx2rkruwILp5HJ-Q;u=5007108385
X-Device-ID: DA4FF810-74FC-4B3C-A65B-CFEE8A243EFA
User-Agent: Xueqiu iPhone 12.26 （这个值也最好保持一致）
Accept-Language: zh-Hans-CN;q=1
X-Device-OS: iOS 14.0
X-Device-Model-Name: Unknown Device
```

### 图2恢复

```
1、图1恢复后，找到以下链接
https://api.xueqiu.com/cubes/show.json?_t=1NETEASEda8d1c2949d3ede8df407938af7c49da.5007108385.1604931242783.1604932210159&_s=a48f5d&ret_last_buy_rb_id=true&mix_rebalancing=true&symbol=ZH2247635
```

```
2、在浏览器直接访问，然后F12，获得其中的cookie信息
```

![1610012645610](C:\Users\61631\AppData\Roaming\Typora\typora-user-images\1610012645610.png)

```
3、最终值Cookie: device_id=24700f9f1986800ab4fcc880530dd0ed; s=c215pkjwcq; bid=85974d5c8b844517db5e365540222743_kh5kmssc; xq_a_token=ad26f3f7a7733dcd164fe15801383e62b6033003; xqat=ad26f3f7a7733dcd164fe15801383e62b6033003; xq_r_token=15b43888685621c645835bfe2d97242dc20b9005; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTYxMTI4MzA4NCwiY3RtIjoxNjEwMDA1NzE1OTQxLCJjaWQiOiJkOWQwbjRBWnVwIn0.Qtb2eiziDpDCDMJF2Mo1UxRbpyFuhI5O5yFgZSNr0tSLO3jcqXLaKvf_5Sx9BAlAPqxMlQ93cjDw05SSOozpV29liOw1ZN2uqbubJuT7T9Y9vqLu9tfHYu_IUgUs4qE12qqYCVhmtWunmy3zuz0iHQpYh5CmBvnlx_20aJpqhOhxMgultz1iUWjLpI7QTdzUXsHPGEhVgR2GVY-eIWNjDd-dWfTwNUEDt9mZO3cABfSPdetbSK2DRhUYV9JTX9V6ciwQIYh_dl6ZrCQC_V3bBnExAzwfr2iIcquUNIIi3MzwRAdSsLf9VhR7mtyTeQ-NZ_yd7fInXkp6B6rGMDbAoQ; u=471610005753132; Hm_lvt_1db88642e346389874251b5a1eded6e3=1610005752; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1610005764
```

### 文件替换

```
以上cookie替换后，在替换完文件后即可完成整体设计
```





## 20200126替换cookie方案

![1611664719238](C:\Users\61631\AppData\Roaming\Typora\typora-user-images\1611664719238.png)



直接采用以上cookie，替换以上3个python文件中的cookie值，即可。

注意：：：：！！！！ 目前测试时，使用wifi节流手机的流量后，用burp suite可以repeater访问 api。但是使用PC端是访问不了了。

在全部替换cookie后，又可以访问。