select count(*) from planes where speed is not null; -- 23
select min(speed), max(speed) from planes; -- 90/432

select format(sum(distance),0) FROM study.flights where year=2013 and month=1; -- 27,188,805
select sum(distance) FROM study.flights where year=2013 and month=1 and tailnum is null; -- 81763

select p.manufacturer, sum(f.distance) 
from study.flights f join study.planes p on f.tailnum=p.tailnum 
where f.year=2013 and f.month=7 and f.day=5
group by p.manufacturer;

/* # manufacturer, sum(f.distance)
AIRBUS, 195089
AIRBUS INDUSTRIE, 78786
AMERICAN AIRCRAFT INC, 2199
BARKER JACK L, 937
BOEING, 335028
BOMBARDIER INC, 31160
CANADAIR, 1142
CESSNA, 2898
DOUGLAS, 1089
EMBRAER, 77909
GULFSTREAM AEROSPACE, 1157
MCDONNELL DOUGLAS, 7486
MCDONNELL DOUGLAS AIRCRAFT CO, 15690
MCDONNELL DOUGLAS CORPORATION, 4767 */

select p.manufacturer, sum(f.distance) 
from study.planes p left join study.flights f on f.tailnum=p.tailnum 
where f.year=2013 and f.month=7 and f.day=5
group by p.manufacturer;

/* # manufacturer, sum(f.distance)
AIRBUS, 195089
AIRBUS INDUSTRIE, 78786
AMERICAN AIRCRAFT INC, 2199
BARKER JACK L, 937
BOEING, 335028
BOMBARDIER INC, 31160
CANADAIR, 1142
CESSNA, 2898
DOUGLAS, 1089
EMBRAER, 77909
GULFSTREAM AEROSPACE, 1157
MCDONNELL DOUGLAS, 7486
MCDONNELL DOUGLAS AIRCRAFT CO, 15690
MCDONNELL DOUGLAS CORPORATION, 4767 */

# In July 2013, which airline experienced the worst delay in departure at each airport?

SELECT p.name as airport, l.name as airline, avg(dep_delay)
FROM study.flights f join study.airports p on f.origin = p.faa
join study.airlines l on 
f.carrier = l.carrier
WHERE year=2013 and month=7
group by p.name, l.name
order by p.name, avg(dep_delay) desc;

/* # airport, airline, avg(dep_delay)
John F Kennedy Intl, Virgin America, 39.7655
John F Kennedy Intl, ExpressJet Airlines Inc., 34.1709
John F Kennedy Intl, Endeavor Air Inc., 33.9375
John F Kennedy Intl, JetBlue Airways, 25.2557
John F Kennedy Intl, Envoy Air, 23.7924
John F Kennedy Intl, Delta Air Lines Inc., 19.8970
John F Kennedy Intl, United Air Lines Inc., 18.5220
John F Kennedy Intl, American Airlines Inc., 15.1998
John F Kennedy Intl, US Airways Inc., 8.2350
John F Kennedy Intl, Hawaiian Airlines Inc., -1.7097
La Guardia, AirTran Airways Corporation, 41.1627
La Guardia, Frontier Airlines Inc., 31.8103
La Guardia, ExpressJet Airlines Inc., 28.3099
La Guardia, JetBlue Airways, 23.6842
La Guardia, Mesa Airlines Inc., 22.4348
La Guardia, Southwest Airlines Co., 22.0887
La Guardia, Delta Air Lines Inc., 21.6727
La Guardia, United Air Lines Inc., 20.8654
La Guardia, Envoy Air, 18.9049
La Guardia, US Airways Inc., 10.0869
La Guardia, Endeavor Air Inc., 9.8333
La Guardia, American Airlines Inc., 9.4913
Newark Liberty Intl, Virgin America, 27.5419
Newark Liberty Intl, Southwest Airlines Co., 27.2500
Newark Liberty Intl, ExpressJet Airlines Inc., 25.9134
Newark Liberty Intl, Envoy Air, 24.6682
Newark Liberty Intl, JetBlue Airways, 23.4225
Newark Liberty Intl, Endeavor Air Inc., 20.2619
Newark Liberty Intl, United Air Lines Inc., 20.1306
Newark Liberty Intl, Delta Air Lines Inc., 18.2219
Newark Liberty Intl, American Airlines Inc., 11.3356
Newark Liberty Intl, US Airways Inc., 8.4261
Newark Liberty Intl, Alaska Airlines Inc., 2.4194 */
