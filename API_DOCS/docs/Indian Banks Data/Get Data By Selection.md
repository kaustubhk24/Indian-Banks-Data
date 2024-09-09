## API To Get Data By Selections

### Get State List

This API is useful if you don't know the IFSC code of the bank but know it's location, So as API as follows to Get Bank Data
```
GET https://bank-apis.justinclicks.com/API/V1/STATE/
```

### Get District List

Now In this Step, we will pass the STATE name in Request, this will return the districts names list
```
GET https://bank-apis.justinclicks.com/API/V1/STATE/MAHARASHTRA/
```

### Get City's List


```
GET https://bank-apis.justinclicks.com/API/V1/STATE/MAHARASHTRA/PUNE/
```

### Get Center's List
```
GET https://bank-apis.justinclicks.com/API/V1/STATE/MAHARASHTRA/PUNE/KHUTBAO
```

### Get Branch List

```
GET https://bank-apis.justinclicks.com/API/V1/STATE/MAHARASHTRA/PUNE/KHUTBAO/KHUTBAO/

```
we made .json files for each branch hence it will give the list of Bank_Name.json

### Get Branch Data

```
GET https://bank-apis.justinclicks.com/API/V1/STATE/MAHARASHTRA/PUNE/KHUTBAO/KHUTBAO/KHUTBHAV.json
```

