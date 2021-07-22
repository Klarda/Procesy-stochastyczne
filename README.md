# Procesy-stochastyczne
Materiały z zajęć procesy stochastyczne
# Metoda Monte Carlo
Wyliczanie całki metodą Monte Carlo. Dana jest funkcja $f\left(x\right)=\sqrt{-5x}-5$ oraz granice przedziału $a=-5$ i $b=0$.
Obliczanie wartości całki $\int_{a}^{b}f\left(x\right)dx$. Następnie sprawdzenie rozkładu funkcji i prównanie dwóch metod wyliczenia.

# „Węże i drabiny” 
jest przykładem tradycyjnej gry planszowej. Na planszy składającej się z 24 pół znajdują się węże i drabiny, które łączą oddalone od siebie pola.

 Dzięki drabiną możemy w szybszy sposób „przeskoczyć” kilka pół bliżej mety. Na odwrót trafienie na pole z głową węża, cofa nas o kilka lub kilkanaście pól bliżej startu. Aby zastosować łańcuch Markowa, należy zastosować pewne założenia: 
*	pole 4 zostaje usunięte, jego zastępcą jest pole 16,
*	pole 12 zostaje usunięte, pole 14 będzie jego zamiennikiem,
* Pole 18 zostanie zastąpione przez pole 9,
*	Pole 23 zostanie usunięte na rzecz pola 3. <br />
Takie założenie zapewni odpowiednią numerację rzutów kostką, gdyż przykładowo w chwili trafienia pionka na pole 4, pionek zostaje automatycznie przesunięty na pole 16, a nie  w kolejnej iteracji.
Następne rozważania odbędą się dla sześciennej kostki do gry. <br />
Po każdym rzucie kostką pionek może zostać przesunięty do przodu o 1, 2, 3, 4, 5, 6 z prawdopodobieństwem 1/6 lub o większą liczbę do przodu lub do tyłu w przypadku pól specjalnych. <br />
Kolejnym utrudnieniem jest nie określenie sytuacji gdy liczba pół wynikająca z rzutu kostką jest większa niż pola, które pozostały do mety. W tej sytuacji możemy:
1.	Założyć, że nie ruszamy pionkiem póki liczba oczek z kostki nie będzie mniejsza lub równa liczbie pól do mety
2.	Założyć, że liczba z rzutu kostką może być większa lub równa liczbie pól do mety 
3.	Założyć, że liczbę równą liczbie pól do mety ruszamy pionkiem w kierunku mety, a następnie cofamy się o pozostałą liczbę pół 

Wyniki obliczeń <br />
Aby obliczyć prawdopodobieństwo ukończenia gry w N ruchach napisano funkcję w języku python. <br />
Dla kostki sześcienej otrzymano następujące wyniki: <br />
dla N=  1  :  0.0
dla N=  2  :  0.0
dla N=  3  :  0.0
dla N=  4  :  0.047
dla N=  5  :  0.07
dla N=  6  :  0.079
dla N=  7  :  0.143
dla N=  8  :  0.137
dla N=  9  :  0.097
dla N=  10  :  0.07
dla N=  11  :  0.062
dla N=  12  :  0.045
dla N=  13  :  0.038
dla N=  14  :  0.03
dla N=  15  :  0.019
dla N=  16  :  0.025
dla N=  17  :  0.016
dla N=  18  :  0.021
dla N=  19  :  0.014
dla N=  20  :  0.005
dla N=  21  :  0.011
dla N=  22  :  0.004
dla N=  23  :  0.008
dla N=  24  :  0.006

Dla kostki czterościennej otrzymano następujące wyniki:
dla N=  1  :  0.0
dla N=  2  :  0.0
dla N=  3  :  0.0
dla N=  4  :  0.023
dla N=  5  :  0.082
dla N=  6  :  0.057
dla N=  7  :  0.038
dla N=  8  :  0.031
dla N=  9  :  0.053
dla N=  10  :  0.059
dla N=  11  :  0.05
dla N=  12  :  0.058
dla N=  13  :  0.054
dla N=  14  :  0.041
dla N=  15  :  0.037
dla N=  16  :  0.036
dla N=  17  :  0.036
dla N=  18  :  0.021
dla N=  19  :  0.029
dla N=  20  :  0.019
dla N=  21  :  0.025
dla N=  22  :  0.019
dla N=  23  :  0.019
dla N=  24  :  0.016
