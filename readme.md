# Diet Optimization
O presente projeto consiste em uma **API** com **modelo linear de otimização** para o problema da dieta, um dos problemas mais clássicos na modelagem e otimização linear.  

> Resumindo **O Problema da Dieta**: Uma pessoa necessita de uma quantidade de nutrientes para poder sobrevivier bem e existe um conjunto de alimentos que suprem essa dieta, o objetivo é escolher quais e quantos **alimentos** precisam ser comprados para **suprir** essa **dieta com o menor custo possível**.  

**Funcionamentoda da API**: Existe duas rotas uma para arquivo json e outra para leitura dos dados em URL do google sheets. Após submeter os dados é retornado quais e quantos alimentos comprar.

**Como usar**:Para usar o projeto é precisa instalar o virtual env, como pip install virutal env.
após feito a instalação do virtualenv é preciso criar um ambiente virtual python com virtualenv <myenv>  
Após necessário trocar esse ambiente, com source /myenv/scripts/activate.bin no linux ou myenv/Script/activate no windows   
Logo feito isso é necessário instalar a libs em pip install -r requeriments.txt  

- Rota para leitura de json:**localhost:porta/opt/run**
- Rota para leitura de sheets google:**localhost:porta/opt/sheets**
    - Default data: https://docs.google.com/spreadsheets/d/1gFzQr62oK6oNVfTGdutsSUFIlNUFgtLaKt7uFwLKuJs/edit?usp=sharing