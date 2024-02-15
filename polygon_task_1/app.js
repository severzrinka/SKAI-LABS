document.addEventListener("DOMContentLoaded", function () {
  // Kreiranje karte
  var map = new ol.Map({
    target: "map", // div s ID-om "map"
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM(), // Dodavanje OpenStreetMap
      }),
    ],
  });
  // Učitavanje podataka o poligonu iz JSON-a
  fetch("polygon.json")
    .then((response) => response.json()) // Pretvaranje u JSON format
    .then((polygonData) => {
      // Pretvaranje koordinata poligona u koordinata karte
      var polygonCoords = polygonData.polygon.map((coord) =>
        ol.proj.fromLonLat(coord)
      );
      // Kreiranje poligona koristeći koordinate
      var polygon = new ol.geom.Polygon([polygonCoords]);
      var feature = new ol.Feature(polygon);
      var style = new ol.style.Style({
        fill: new ol.style.Fill({
          color: "rgba(255, 100, 50, 0.5)", //postavljanje boje
        }),
        stroke: new ol.style.Stroke({
          color: "#ff0000", // Postavljanje boje ruba
          width: 2, // Debljina ruba
        }),
      });
      var vectorSource = new ol.source.Vector({
        features: [feature], // Dodavanje u izvor vektora
      });
      var vectorLayer = new ol.layer.Vector({
        source: vectorSource, // Postavljanje izvora vektora
        style: style, // Postavljanje stila sloja vektora
      });

      map.addLayer(vectorLayer);
      map.getView().fit(polygon, { padding: [20, 20, 20, 20] }); // Zumiranje i centriranje karte na poligon
    })
    .catch((error) => console.error("Error: ", error)); // Prikazivanje greške ako dođe do problema pri učitavanju
});
