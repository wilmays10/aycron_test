 var attribution = new ol.control.Attribution({
     collapsible: false
 });

var map = new ol.Map({
    controls: ol.control.defaults({attribution: false}).extend([attribution]),
    layers: [
        new ol.layer.Tile({
            source: new ol.source.OSM()
        })
    ],
    target: document.getElementById('map'),
    view: new ol.View({
        center: ol.proj.fromLonLat([-64.1862, -31.4074]),
        zoom: 12.5
    })
});