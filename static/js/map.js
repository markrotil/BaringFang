var LeafIcon = L.Icon.extend({
    options: {
        iconSize: [18, 18],
        iconAnchor: [12, 74],
        popupAnchor: [-3, -76]
    }
})


var Amzn = new LeafIcon({ iconUrl: 'amazon pin.png' }),
    Appl = new LeafIcon({ iconUrl: 'apple pin.png' }),
    Googl = new LeafIcon({ iconUrl: 'google pin.png' }),
    FacB = new LeafIcon({ iconUrl: 'facebook pin.png' }),
    Nflx = new LeafIcon({ iconUrl: 'netflix pin.png' }),
    Micrsft = new LeafIcon({ iconUrl: 'microsoft pin.png' });


// Create the tile layer that will be the background of our map
var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 5,
    id: "light-v10",
    accessToken: API_KEY
});

// Initialize all of the LayerGroups we'll be using
var layers = {
    Amazon: new L.LayerGroup(),
    Apple: new L.LayerGroup(),
    Facebook: new L.LayerGroup(),
    Google: new L.LayerGroup(),
    Netflix: new L.LayerGroup(),
    Microsoft: new L.LayerGroup()

};

// Create the map with our layers
var map = L.map("map-id", {
    center: [40.73, -74.0059],
    zoom: 35,
    layers: [
        layers.Amazon,
        layers.Apple,
        layers.Facebook,
        layers.Google,
        layers.Netflix,
        layers.Microsoft
    ]
});

// Add our 'lightmap' tile layer to the map
lightmap.addTo(map);

// Create an overlays object to add to the layer control
var overlays = {
    "Amazon": layers.Amazon,
    "Apple": layers.Apple,
    "Facebook": layers.Facebook,
    "Google": layers.Google,
    "Netflix": layers.Netflix,
    "Microsoft": layers.Microsoft
};

// Create a control for our layers, add our overlay layers to it
L.control.layers(null, overlays).addTo(map);

// Create a legend to display information about our map
var info = L.control({
    position: "bottomright"
});

// When the layer control is added, insert a div with the class of "legend"
info.onAdd = function () {
    var div = L.DomUtil.create("div", "legend");
    return div;
};
// Add the info legend to the map
info.addTo(map);

// Initialize an object containing icons for each layer group
var icons = {
    Amazon: Amzn,

    Apple: Appl,

    Netflix: Googl,

    Facebook: FacB,

    Google: Nflx,

    Microsoft: Micrsft
};

// Perform an API call to the Citi Bike Station Information endpoint
d3.json("/office", function (infoRes) {

    // When the first API call is complete, perform another call to the Citi Bike Station Status endpoint
    d3.json("/office", function (Company) {
        var updatedAt = infoRes.last_updated;
        var stationStatus = Company.off_list;
        var stationInfo = infoRes.off_list;

        // Create an object to keep of the number of markers in each layer
        var stationCount = {
            Amazon: 0,
            Apple: 0,
            Facebook: 0,
            Google: 0,
            Netflix: 0
        };

        // Initialize a stationStatusCode, which will be used as a key to access the appropriate layers, icons, and station count for layer group
        var stationStatusCode;

        // Loop through the stations (they're the same size and have partially matching data)
        for (var i = 0; i < stationInfo.length; i++) {

            // Create a new station object with properties of both station objects
            var station = Object.assign({}, stationInfo[i], stationStatus[i]);
            // If a station is listed but not installed, it's coming soon
            if (!station.Company == "Amazon") {
                stationStatusCode = "Amazon";
            }
            // If a station has no bikes available, it's Apple
            else if (!station.Company == "Apple") {
                stationStatusCode = "Apple";
            }
            // If a station is installed but isn't renting, it's out of order
            else if (!station.Company == "Facebook") {
                stationStatusCode = "Facebook";
            }
            // If a station has less than 5 bikes, it's status is Facebook
            else if (!station.Company == "Google") {
                stationStatusCode = "Google";
            }
            // If a station has less than 5 bikes, it's status is Facebook
            else if (!station.Company == "Microsoft") {
                stationStatusCode = "Microsoft";
            }
            // Otherwise the station is Google
            else {
                stationStatusCode = "Netflix";
            }

            // Update the station count
            stationCount[stationStatusCode]++;
            // Create a new marker with the appropriate icon and coordinates
            var newMarker = L.marker([station.lattitude, station.longitude], {
                icon: icons[stationStatusCode]
            });

            // Add the new marker to the appropriate layer
            newMarker.addTo(layers[stationStatusCode]);

            // Bind a popup to the marker that will  display on click. This will be rendered as HTML
            newMarker.bindPopup(station.Company + "<br> Office: " + station.Office + "<br>" + station.Country + " Bikes Available");
        }

        // Call the updateLegend function, which will... update the legend!
        updateLegend(updatedAt, stationCount);
    });
});

// Update the legend's innerHTML with the last updated time and station count
function updateLegend(time, stationCount) {
    document.querySelector(".legend").innerHTML = [
        "<p>Updated: " + moment.unix(time).format("h:mm:ss A") + "</p>",
        "<p" + stationCount.Netflix + "</p>",
        "<p" + stationCount.Amazon + "</p>",
        "<p" + stationCount.Apple + "</p>",
        "<p" + stationCount.Facebook + "</p>",
        "<p" + stationCount.Google + "</p>"
    ].join("");
}


console.log(infoRes);
console.log(statusRes);