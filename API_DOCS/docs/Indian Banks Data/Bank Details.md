### API To Get Bank Details Using IFSC

If you have the IFSC Code of Bank & you want to get complete details of the respective bank, You need to send HTTP GET Request to the given URL 

Make sure you pass the IFSC code only in UPPERCASE. For example, if you want to access data of branch having IFSC code as MAHB0001012, then your request URL will be 
```
GET https://bank-apis.justinclicks.com/API/V1/IFSC/MAHB0001012/
```