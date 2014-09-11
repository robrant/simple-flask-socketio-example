// Add a leaflet map to the div
var map = L.map('map');

// Get the features into a leaflet recognised geojson
var features = {% autoescape off %} {{ cells }} {% endautoescape %};
geojson = L.geoJson(features, {style : style,
			    onEachFeature: function (feature, layer) {
			        layer.bindPopup(feature.properties.description);
			    }
			}
		);
geojson.addTo(map);

// Add a scale bar
L.control.scale().addTo(map);

// Get the bounds of the features and derive the zoom level
map.fitBounds(geojson.getBounds());
var zoomLevel = map.getZoom();

// Source some tiles
L.tileLayer('http://{s}.tile.cloudmade.com/b04077cbdf8c4aa7b32ebffb94fb8004/{styleId}/256/{z}/{x}/{y}.png', {
		    maxZoom: 18,
		    styleId: 22677
			}).addTo(map);

