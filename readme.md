# Diet Optimization
📊 O presente projeto consiste em uma **API** com **modelo linear de otimização** para o problema da dieta, um dos problemas mais clássicos na modelagem e otimização linear.
> Resumindo **O Problema da Dieta**: Uma pessoa necessita de uma quantidade de nutrientes para poder sobrevivier bem e existe um conjunto de alimentos que suprem essa dieta, o objetivo é escolher quais e quantos **alimentos** precisam ser comprados para **suprir** essa **dieta com o menor custo possível**.


**Funcionamentoda da API**: Existe duas rotas uma para arquivo json e outra para leitura dos dados em URL do google sheets. Após submeter os dados é retornado quais e quantos alimentos comprar.

**-->** Uma opção é usar o [frontend do projeto](https://withoutcoffee.github.io/DietOptimizationFrontend/) sem necessidade de instalação (enquanto o heroku funcionar 😅).

**Como usar**: Para usar o projeto é precisa instalar o virtual env com ``pip install virutal env``.
após feito a instalação do virtualenv é preciso criar um ambiente virtual python com ``virtualenv myvenv --python=python3.8``+  
Após feito isso é necessário trocar esse ambiente, com ``source /myvenv/scripts/activate.bin`` no linux ou ``myvenv/Script/activate`` no windows   
Logo feito isso é necessário instalar a libs em ``pip install -r requiriments.txt`` 

- Rota (post) para otimização com dados em formato json: ``localhost:porta/opt/run``
    - Formato de etrada: 
    ```json
    {
        "nutrients":[["Calories (kcal)", 3], ["Protein (g)", 70], ["Calcium (g)", 0.8], ["Iron (mg)", 12], ["Vitamin A (KIU)", 5], ["Vitamin B1 (mg)", 1.8], ["Vitamin B2 (mg)", 2.7], ["Niacin (mg)", 18], ["Vitamin C (mg)", 75]],
        "data":[["Wheat Flour (Enriched)", "10 lb.", 36, 44.7, 1411, 2, 365, 0, 55.4, 33.3, 441, 0]
    }

    ```
    - Formato de saída: 
    ```json
    {
        "result": {
            "Cabbage": {
                "amount": 0.07850104672301408,
                "quantity": 0.02121649911432813
            }
        },
        "amount": 0.760635947447298
    }
    ```
- Rota (post) para otimização com dados em URL sheets google:``localhost:porta/opt/sheets``
    - Formato de etrada: 
    ```json
    {"sheet_url":"https://docs.google.com/spreadsheets/d/1gFzQr62oK6oNVfTGdutsSUFIlNUFgtLaKt7uFwLKuJs/edit?usp=sharing"}
    ```
    - Default data: https://docs.google.com/spreadsheets/d/1gFzQr62oK6oNVfTGdutsSUFIlNUFgtLaKt7uFwLKuJs/edit?usp=sharing
    
**OBS:** Para utilizar dados personalizados é preciso seguir o mesmo padrão do link acima, assim pode-se mudar os produtos, preços e nutrientes para qualquer caso se uso.

## Tecnologias utilizadas
* Python
* Flask
* Pandas
* [OR-Tools](https://developers.google.com/optimization)