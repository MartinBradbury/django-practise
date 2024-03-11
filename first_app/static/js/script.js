console.log('testing testing testing');
const apiKey = 'HMEY6vWRioll4rhP5rBHRcAKCXvsUEti';

// Create a map style object using the ZXY service.
const style = {
    "version": 8,
    "sources": {
        "raster-tiles": {
            "type": "raster",
            "tiles": [ "https://api.os.uk/maps/raster/v1/zxy/Outdoor_3857/{z}/{x}/{y}.png?key=" + apiKey ],
            "tileSize": 256
        }
    },
    "layers": [{
        "id": "os-maps-zxy",
        "type": "raster",
        "source": "raster-tiles"
    }]
};

// Initialize the map object.
const map = new maplibregl.Map({
    container: 'map',
    minZoom: 6,
    maxZoom: 19,
    style: style,
    maxBounds: [
        [ -10.76418, 49.528423 ],
        [ 1.9134116, 61.331151 ]
    ],
    center: [ -2.968, 54.425 ],
    zoom: 13
});

map.dragRotate.disable(); // Disable map rotation using right click + drag.
map.touchZoomRotate.disableRotation(); // Disable map rotation using touch rotation gesture.

// Add navigation control (excluding compass button) to the map.
map.addControl(new maplibregl.NavigationControl({
    showCompass: false
}));
