#!/usr/bin/python


import os 
import folium 


m=folium.Map(location=[ 52.5672408, 13.5496179],zoom_start=12,
tiles='OpenStreetMap')

iconprefix = 'fa'
iconname='tree'
iconcolor='green'

folium.Marker(location=[ 52.5672408, 13.5496179],popup='Westpark, Marzahn, Marzahn-Hellersdorf, Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5669814, 13.5266280],popup='Park Quartierspark Randowstraße, Neu-Hohenschönhausen'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5683269, 13.5205335],popup='Park Quartierspark Warnitzer Bogen, Neu-Hohenschönhausen'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5512849, 13.5534115],popup='Park Hochzeitspark, Marzahn, Marzahn-Hellersdorf'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[   52.5399858, 13.5340907],popup='Park Gewerbepark Georg Knorr, Marzahn, Marzahn-Hellersdorf'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[ 52.5711314, 13.5393277],popup='Park Gutspark Falkenberg, Falkenberg, Lichtenberg, Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5702663, 13.5363501],popup='Park Falkenberg, Lichtenberg'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5646386, 13.5460964],popup='Park Marzahn, Marzahn-Hellersdorf'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[   52.5594839, 13.5528538],popup='Park GSG Gewerbehof Wolfener Straße, Marzahn, Marzahn-Hellersdorf'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5527416, 13.5216413],popup='Park Roderichplatz, Alt-Hohenschönhausen, Lichtenberg'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5129506, 13.4129602],popup='Park Köllnischer Park, Spandauer Vorstadt, Mitte, Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[   52.5604681, 13.5141742],popup='Park Neu-Hohenschönhausen, Lichtenberg, Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5181311, 13.4238362],popup='Park Mitte,Berin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[   52.5733293, 13.5160151],popup='Park Wartenberg,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[   52.5054698, 13.4222520],popup='Park Immergrüner Garten, Mitte,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[   52.5051972, 13.4218341],popup='Park Ehemaliger Luisenstädtischer Kanal, Mitte,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[   52.5061195, 13.4195858],popup='Park Michaelkirchplatz, Mitte,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5043207, 13.4170892],popup='Park Rosengarten,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5176400, 13.4235036],popup='Park Lotos Vihara,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5171898, 13.4222327],popup='Park Plansche,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5136444, 13.4138683],popup='Park Märkischer Platz, Spandauer Vorstadt,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5114133, 13.4137279],popup='Park Schulze-Delitzsch-Platz,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[ 52.5040852, 13.4172108],popup='Park Luisenstädtischer Kanal, Kreuzberg, Friedrichshain-Kreuzberg,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5039883, 13.4148046],popup='Park Alfred-Döblin-Platz, Kreuzberg, Friedrichshain-Kreuzberg,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5015188, 13.4160953],popup='Park Oranienplatz, Kreuzberg, Friedrichshain-Kreuzberg'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5034341, 13.4202789],popup='Park Kreuzberg, Friedrichshain-Kreuzberg,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5095647, 13.4078953],popup='Park Waldpflanzen, Mitte,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5146549, 13.4259464],popup='Park Fhain, Friedrichshain-Kreuzberg,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5095647, 13.4078953],popup='Park Spandauer Vorstadt, Mitte,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[   52.5096702, 13.4075679],popup='Park Luisenstädtischer Kanal, Kreuzberg, Friedrichshain-Kreuzberg,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[   52.5021062, 13.4247442],popup='Park Mariannenplatz, Kreuzberg, Friedrichshain-Kreuzberg,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5064389, 13.4275212],popup='Park Blütensträucher, Mitte,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5184957, 13.4039812],popup='Park Marx-Engels Forum, Spandauer Vorstadt,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5210743, 13.3187621],popup='Park Charlottenburg, Charlottenburg-Wilmersdorf,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5116124, 13.4342223],popup='Park Hermann-Stöhr-Platz, Fhain, Friedrichshain-Kreuzberg,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[   52.5295197, 13.4161583],popup='Park Kollwitzkiez, Prenzlauer Berg, Pankow,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[ 52.5246349, 13.3149914],popup='Park Goslarer Platz, Charlottenburg, Charlottenburg-Wilmersdorf,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[ 52.5288817, 13.3257359],popup='Park Moabit, Mitte,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[ 52.5407525, 13.4461580],popup='Park Einsteinpark, Prenzlauer Berg, Pankow,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[  52.5479846, 13.4506532],popup='Park Antonplatz, Komponistenviertel, Weißensee, Pankow,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[ 52.5490259, 13.4425171],popup='Park Weißensee, Pankow,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[52.5530890, 13.4488508 ],popup='Park Mirbachplatz, Weißensee, Pankow,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[ 52.5467332, 13.4420245],popup='Park Ostseeplatz, Prenzlauer Berg, Pankow,Berlin'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)

folium.Marker(location=[ 52.5350062, 13.4456284],popup='Park Prenzlauer Berg, Pankow'
              ,icon=folium.Icon(color=iconcolor,prefix= iconprefix, icon=iconname)).add_to(m)



m.save(os.path.join('Park in Berlin'))
m
