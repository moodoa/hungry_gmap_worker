# hungry_gmap_worker
上班肚子餓了嗎？想規劃旅遊景點嗎？用這支程式幫你找到附近的好東西吧！

![alt text](https://cdn-images-1.medium.com/max/1000/1*NCCUzKGIzM_jbqCTaKuI_g.png)
#### 部屬 app 到 deta 上，並連動 LINE bot。


# 關於 [LINE Messaging API](https://developers.line.biz/en/services/messaging-api/) 的設定
#### 1.Channel secret 在 Basic Settings 裡面可以找到，Channel access token 則是在 Messaging API 裡面。
![alt text](https://cdn-images-1.medium.com/max/1000/1*ZWscTYpEzFrDh25-C4DPUw.png)
#### 2.Messaging API 裡面的 Use webhook 要打開。
#### 3.Webhook URL 輸入由 deta 產生的url，後面要加/callback。
![alt text](https://cdn-images-1.medium.com/max/1000/1*-LbkJAAAtf-7EgIUJrWewQ.png)

# 關於 deta 的設定
#### 1.申請帳號以及安裝 CLI 登入可參考：https://docs.deta.sh/docs/micros/getting_started
#### 2.開啟 PowerShell ，創立一個新的作業資料夾。如創立 hungry_gmap_worker 資料夾為 `deta new --python hungry_gmap_worker` 。
#### 3.此時會出現類似 ![alt text](https://cdn-images-1.medium.com/max/1000/1*D1dyv86VpQFsHTz_dr0nUA.png)，endpoint 上的 url 要輸入進 Webhook URL。
#### 4.進入 hungry_gmap_worker 資料夾，將此 repo 中的 main.py (取代內建的)、hungryworker.py 和 requirements.txt(相依套件) 放進去。
#### 5.PowerShell 輸入 deta deploy，如此便能完成布署。

# 關於 google map api 的設定
#### 1.進入 [Google API 程式庫](https://console.developers.google.com/apis/library) 後登入 google 帳號。
#### 2.搜尋關鍵字 "Maps"，進入 Geocoding API 後點啟用。(Places API 通常會跟著打開，若無則需手動搜尋後點啟用。)
#### 3.啟用後跟著步驟建立 API 專案，將帳號綁定信用卡並取得 API KEY。
![alt text](https://cdn-images-1.medium.com/max/1000/1*K-Lsbr7Vn_bQ1RHSk5nwzw.png)
#### (點選右方的顯示金鑰就能看到 API KEY 了)
#### 4.將申請到的 API KEY 輸入 `hungryworker.py` 中的對應位置。
