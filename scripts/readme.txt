v scriptTwints.js arr prekopiraš username po katerih hočeš searchat (politiki, 25 trolov etc.)
Ta nam potem generiral datoteke posameznih uporabnikv z mentioni, retweeti...

ElasticQueryTwints 90 vrstica definiraš index, če hočeš searchati po drugi bazi.

127 vrstica, se definira v katero mapo hočeš shraniti npr. /politiki.
- Če skrejpaš vse ne glede na username (glej npr. scriptPolitiki.js) potem je treba napisati, v 
isto vrstico še ime datoteke. 

skripta getTop30 users nam zgenerira iste uporabnike, ki imajo le top30 podatke kategorij.
-> za grafe trolov, je ta datoteka dovolj in se jo kopira v assests trolls.


getTopX.js kličemo nad skriptami, ki imajo vse userje. torej hashtagi politikov, mentioni politikov etc.
primer klica. node getTopX ./pot-do-datoteke/datoteka 30 ./pot-kamor-se-shrani/ime-datoteke

Ustvarjeno datoteko prekopiramo v components/charts glej hashtagTop30Politiki <- v Makro.vue za način klica.





